import json
import urllib.request
import urllib.error
import urllib.parse
import re

SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM"
SOURCE_GID = 954545565
ROADMAP_SPREADSHEET_ID = "1RN2dglTLMsSvXQLQTiBLZ0TmhN0hPESZyV5pr6Gjgwc"
ROADMAP_GID = 1531584370
BACKLOG_SYNC_GID = 1413103355

TOKEN_PATH = "/Users/hathuy/.gemini/antigravity/plugin_data/gsheets/token.json"

def get_valid_token():
    with open(TOKEN_PATH) as f:
        data = json.load(f)
    client_id = data.get('client_id')
    client_secret = data.get('client_secret')
    refresh_token = data.get('token', {}).get('refresh_token')
    
    url = 'https://oauth2.googleapis.com/token'
    params = urllib.parse.urlencode({
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=params, method='POST')
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            data['token']['access_token'] = res['access_token']
            with open(TOKEN_PATH, 'w') as f_out:
                json.dump(data, f_out, indent=2)
            return res['access_token']
    except Exception as e:
        print("Refresh token error:", e)
        return data.get('token', {}).get('access_token')

access_token = get_valid_token()

def api_call(url, data=None, method='GET'):
    global access_token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8') if data else None,
        headers=headers,
        method=method
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("API ERROR DETAILS:", e.code, e.read().decode())
        raise

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return {
        'red': int(hex_str[0:2], 16) / 255.0,
        'green': int(hex_str[2:4], 16) / 255.0,
        'blue': int(hex_str[4:6], 16) / 255.0
    }

STATUS_STEPS = {
    'Chưa tiếp nhận': {
        'step': 1, 'percent': '12.5%',
        'taskBg': '#F1F5F9', 'border': '#CBD5E1', 'barColor': '#94A3B8', 'badgeColor': '#475569'
    },
    'Đã tiếp nhận yêu cầu': {
        'step': 2, 'percent': '25.0%',
        'taskBg': '#DBEAFE', 'border': '#93C5FD', 'barColor': '#3B82F6', 'badgeColor': '#1D4ED8'
    },
    'Đang phân tích/Document': {
        'step': 3, 'percent': '37.5%',
        'taskBg': '#FFEDD5', 'border': '#FDBA74', 'barColor': '#F97316', 'badgeColor': '#C2410C'
    },
    'Transfer DEV/PO reviewed': {
        'step': 4, 'percent': '50.0%',
        'taskBg': '#FFF1F2', 'border': '#FECDD3', 'barColor': '#FB7185', 'badgeColor': '#BE123C'
    },
    'DEV In Progress': {
        'step': 5, 'percent': '62.5%',
        'taskBg': '#FEF9C3', 'border': '#FDE047', 'barColor': '#EAB308', 'badgeColor': '#A16207'
    },
    'UAT': {
        'step': 6, 'percent': '75.0%',
        'taskBg': '#F3E8FF', 'border': '#D8B4FE', 'barColor': '#9333EA', 'badgeColor': '#6B21A8'
    },
    'QC/CSOC': {
        'step': 7, 'percent': '87.5%',
        'taskBg': '#E0F2FE', 'border': '#7DD3FC', 'barColor': '#0284C7', 'badgeColor': '#0369A1'
    },
    'Done': {
        'step': 8, 'percent': '100.0%',
        'taskBg': '#D1FAE5', 'border': '#6EE7B7', 'barColor': '#10B981', 'badgeColor': '#047857'
    }
}

PRIO_STYLE = {
    'P1': {'color': '#DC2626', 'label': '[P1]'},
    'P2': {'color': '#EA580C', 'label': '[P2]'},
    'P3': {'color': '#2563EB', 'label': '[P3]'},
    'P4': {'color': '#64748B', 'label': '[P4]'}
}

MONTH_BG = {
    'm10': '#F8FAFC',
    'm11': '#FAF7FD',
    'm12': '#F2FBF6'
}

def get_epic_color(epic):
    if not epic: return '#1E40AF'
    ep = str(epic).lower()
    if 'cms' in ep and 'web' in ep:
        return '#047857' if ep.startswith('web') else '#1E40AF'
    if 'cms' in ep: return '#1E40AF'
    if 'web' in ep: return '#047857'
    return '#1E40AF'

def normalize_status(raw):
    if not raw: return 'Chưa tiếp nhận'
    s = raw.strip().lower()
    if any(k in s for k in ['done', 'hoàn thành', 'closed', 'đã xong', 'pass uat', 'pass']):
        return 'Done'
    if 'transfer' in s or 'po reviewed' in s or (('review' in s or 'po' in s) and 'in progress' not in s):
        return 'Transfer DEV/PO reviewed'
    if 'in progress' in s or 'dev' in s or 'phát triển' in s:
        return 'DEV In Progress'
    if 'uat' in s or 'test' in s or 'nghiệm thu' in s:
        return 'UAT'
    if any(k in s for k in ['ba/document', 'ba', 'phân tích', 'document', 'analysis', 'doc']):
        return 'Đang phân tích/Document'
    if any(k in s for k in ['to do', 'todo', 'chưa tiếp nhận', 'new', 'open']):
        return 'Chưa tiếp nhận'
    if any(k in s for k in ['tiếp nhận', 'nhận yêu cầu', 'received']):
        return 'Đã tiếp nhận yêu cầu'
    if 'qc' in s or 'csoc' in s:
        return 'QC/CSOC'
    return raw.strip()

def clean_desc(desc):
    if not desc: return 'Quy chuẩn cấu hình và tích hợp hệ thống'
    desc = re.sub(r'https?://[^\s]+', '', desc).strip()
    desc = re.sub(r'^(Tài liệu:\s*Thiết kế:\s*|Tài liệu:\s*|Thiết kế:\s*|-\s*)', '', desc, flags=re.IGNORECASE).strip()
    lines = [re.sub(r'^-\s*', '', l).strip() for l in desc.split('\n') if l.strip()]
    desc = ' - '.join(lines)
    desc = re.sub(r'\s*-\s*-\s*', ' - ', desc)
    desc = re.sub(r'\s{2,}', ' ', desc).strip()
    if not desc or desc == '-' or len(desc) < 3:
        desc = 'Quy chuẩn cấu hình và tích hợp hệ thống'
    return desc

# 1. Fetch Source Data from Sheet GID 954545565
source_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SOURCE_SPREADSHEET_ID}/values/'%F0%9F%93%8C%20Product%20Backlog%20FCP'!A1:J70"
source_val = api_call(source_url)
rows = source_val.get('values', [])

header_idx = 2
headers = rows[header_idx]

def parse_tl(tl):
    if not tl: return None
    tl = tl.strip().lower()
    if tl in ['-', 'n/a', '', 'timeline mong muốn', 'timeline', 'thời gian', 'kế hoạch', 'target']: return None
    
    has10 = bool(re.search(r'(?:tháng|thg|\bt)\s*10|oct|\b10\b', tl))
    has11 = bool(re.search(r'(?:tháng|thg|\bt)\s*11|nov|\b11\b', tl))
    has12 = bool(re.search(r'(?:tháng|thg|\bt)\s*12|dec|\b12\b', tl))
    
    if has10 and has11:
        return {'timeGroup': 'span-10-11', 'startM': 10, 'endM': 11, 'startCol': 0, 'totalCols': 8, 'label': 'Tháng 10 - Tháng 11'}
    if has11 and has12:
        return {'timeGroup': 'span-11-12', 'startM': 11, 'endM': 12, 'startCol': 4, 'totalCols': 8, 'label': 'Tháng 11 - Tháng 12'}
    if has10:
        return {'timeGroup': 't10', 'startM': 10, 'endM': 10, 'startCol': 0, 'totalCols': 4, 'label': 'Tháng 10'}
    if has11:
        return {'timeGroup': 't11', 'startM': 11, 'endM': 11, 'startCol': 4, 'totalCols': 4, 'label': 'Tháng 11'}
    if has12:
        return {'timeGroup': 't12', 'startM': 12, 'endM': 12, 'startCol': 8, 'totalCols': 4, 'label': 'Tháng 12'}
    return None

PRIO_WEIGHTS = {'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4}

raw_tasks = []
seen_titles = set()

for row in rows[header_idx + 1:]:
    if len(row) < 3 or not row[2].strip():
        continue
    title_full = row[2].strip()
    title = title_full.split('\n')[0].strip()
    if not title or len(title) < 2:
        continue
    clean_key = title.lower()
    if clean_key in seen_titles:
        continue
    
    epic = row[1].strip() if len(row) > 1 else ''
    prio = row[5].strip() if len(row) > 5 else 'P2'
    tl_raw = row[6].strip() if len(row) > 6 else ''
    pic = row[7].strip() if len(row) > 7 else ''
    raw_status = row[8].strip() if len(row) > 8 else ''
    raw_desc = row[3].strip() if len(row) > 3 else ''
    
    status = normalize_status(raw_status)
    if 'pending' in status.lower() or 'pending' in raw_status.lower():
        continue
    
    tl_parsed = parse_tl(tl_raw)
    if not tl_parsed:
        continue
    
    seen_titles.add(clean_key)
    raw_tasks.append({
        'title': title,
        'epic': epic,
        'desc': clean_desc(raw_desc),
        'prio': prio,
        'pic': pic,
        'status': status,
        'rawStatus': raw_status,
        'timeline': tl_raw,
        'timeGroup': tl_parsed['timeGroup'],
        'startM': tl_parsed['startM'],
        'endM': tl_parsed['endM'],
        'startCol': tl_parsed['startCol'],
        'totalCols': tl_parsed['totalCols']
    })

# Sắp xếp theo trình tự thời gian Thác Nước Gantt
time_order = ['t10', 'span-10-11', 't11', 'span-11-12', 't12']
sorted_tasks = []
for grp in time_order:
    sub = [t for t in raw_tasks if t['timeGroup'] == grp]
    sub.sort(key=lambda t: PRIO_WEIGHTS.get(t['prio'], 99))
    sorted_tasks.extend(sub)

print(f"Qualified tasks to sync: {len(sorted_tasks)}")

# 2. Build Waterfall Gantt Layout
# Total rows:
# Row 0: Banner (34px)
# Row 1: Quick Jump Navigation (24px)
# Row 2: Month Headers (28px)
# Each task: Card (34px), Bar (6px), Spacer (4px) => 3 rows
# Legend: (24px)
# Spacer: (4px)
# Footer: (22px)

TOTAL_ROWS = 3 + len(sorted_tasks) * 3 + 3
print(f"Total rows: {TOTAL_ROWS}")

batch_requests = []

# Unmerge all existing
batch_requests.append({
    'unmergeCells': {
        'range': {'sheetId': ROADMAP_GID}
    }
})

# Resize sheet and FREEZE TOP 3 ROWS!
batch_requests.append({
    'updateSheetProperties': {
        'properties': {
            'sheetId': ROADMAP_GID,
            'gridProperties': {
                'rowCount': TOTAL_ROWS,
                'columnCount': 12,
                'frozenRowCount': 3,  # CỐ ĐỊNH 3 DÒNG TIÊU ĐỀ ĐỂ CUỘN CHUỘT VẪN THẤY THÁNG 10, 11, 12!
                'hideGridlines': True
            }
        },
        'fields': 'gridProperties.rowCount,gridProperties.columnCount,gridProperties.frozenRowCount,gridProperties.hideGridlines'
    }
})

# Set column widths: 145px each for cols 0..11 (total 1740px)
batch_requests.append({
    'updateDimensionProperties': {
        'range': {
            'sheetId': ROADMAP_GID,
            'dimension': 'COLUMNS',
            'startIndex': 0,
            'endIndex': 12
        },
        'properties': {'pixelSize': 145},
        'fields': 'pixelSize'
    }
})

# Set Row Heights
row_heights = [
    (0, 1, 34),
    (1, 2, 26),
    (2, 3, 28)
]
cur_r = 3
for t in sorted_tasks:
    row_heights.append((cur_r, cur_r + 1, 34))
    row_heights.append((cur_r + 1, cur_r + 2, 6))
    row_heights.append((cur_r + 2, cur_r + 3, 4))
    cur_r += 3

row_heights.append((cur_r, cur_r + 1, 24))     # Legend
row_heights.append((cur_r + 1, cur_r + 2, 4))  # Spacer
row_heights.append((cur_r + 2, cur_r + 3, 22)) # Footer

for start_r, end_r, px in row_heights:
    batch_requests.append({
        'updateDimensionProperties': {
            'range': {
                'sheetId': ROADMAP_GID,
                'dimension': 'ROWS',
                'startIndex': start_r,
                'endIndex': end_r
            },
            'properties': {'pixelSize': px},
            'fields': 'pixelSize'
        }
    })

# Merges
merges = [
    # Banner
    {'sheetId': ROADMAP_GID, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 12},
    # Month 10
    {'sheetId': ROADMAP_GID, 'startRowIndex': 2, 'endRowIndex': 3, 'startColumnIndex': 0, 'endColumnIndex': 4},
    # Month 11
    {'sheetId': ROADMAP_GID, 'startRowIndex': 2, 'endRowIndex': 3, 'startColumnIndex': 4, 'endColumnIndex': 8},
    # Month 12
    {'sheetId': ROADMAP_GID, 'startRowIndex': 2, 'endRowIndex': 3, 'startColumnIndex': 8, 'endColumnIndex': 12},
]

cur_r = 3
for t in sorted_tasks:
    start_c = t['startCol']
    total_c = t['totalCols']
    left_c = 3 if total_c == 4 else 6
    right_c = total_c - left_c
    
    cfg = STATUS_STEPS.get(t['status'], STATUS_STEPS['Chưa tiếp nhận'])
    is_done = (t['status'] == 'Done')
    if is_done:
        colored_cols = total_c
    else:
        if total_c == 8:
            colored_cols = cfg['step']
        else:
            colored_cols = 1 if cfg['step'] <= 2 else (2 if cfg['step'] <= 5 else 3)
        if colored_cols < 1: colored_cols = 1
        if colored_cols >= total_c: colored_cols = total_c - 1
    white_cols = total_c - colored_cols

    # Card Left
    merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r, 'endRowIndex': cur_r + 1, 'startColumnIndex': start_c, 'endColumnIndex': start_c + left_c})
    # Card Right
    if right_c > 1:
        merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r, 'endRowIndex': cur_r + 1, 'startColumnIndex': start_c + left_c, 'endColumnIndex': start_c + total_c})
    
    # Progress Bar Colored
    if colored_cols > 1:
        merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r + 1, 'endRowIndex': cur_r + 2, 'startColumnIndex': start_c, 'endColumnIndex': start_c + colored_cols})
    # Progress Bar White (if any)
    if white_cols > 1:
        merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r + 1, 'endRowIndex': cur_r + 2, 'startColumnIndex': start_c + colored_cols, 'endColumnIndex': start_c + total_c})

    cur_r += 3

# Legend 6 items
for i in range(6):
    merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r, 'endRowIndex': cur_r + 1, 'startColumnIndex': i * 2, 'endColumnIndex': i * 2 + 2})
# Footer
merges.append({'sheetId': ROADMAP_GID, 'startRowIndex': cur_r + 2, 'endRowIndex': cur_r + 3, 'startColumnIndex': 0, 'endColumnIndex': 12})

for m in merges:
    batch_requests.append({
        'mergeCells': {
            'range': m,
            'mergeType': 'MERGE_ALL'
        }
    })

# Build Row Data
row_data_list = []

# Row 0: Banner
banner_cell = {
    'userEnteredValue': {'stringValue': 'FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)'},
    'userEnteredFormat': {
        'backgroundColorStyle': {'rgbColor': hex_to_rgb('#F37021')},
        'horizontalAlignment': 'CENTER',
        'verticalAlignment': 'MIDDLE',
        'textFormat': {
            'fontFamily': 'Times New Roman',
            'fontSize': 14,
            'bold': True,
            'foregroundColorStyle': {'rgbColor': hex_to_rgb('#FFFFFF')}
        }
    }
}
row_data_list.append({'values': [banner_cell] + [{}] * 11})

# Row 1: Thanh Lọc Đa Trạng Thái Checkbox (12 Cột = 6 Cặp Checkbox + Nhãn)
filter_configs = [
    {'col': 0, 'label': '🔘 TẤT CẢ', 'bg': '#EFF6FF', 'text': '#1D4ED8', 'border': '#BFDBFE'},
    {'col': 2, 'label': '🟢 DONE', 'bg': '#DCFCE7', 'text': '#15803D', 'border': '#BBF7D0'},
    {'col': 4, 'label': '🟣 UAT', 'bg': '#F3E8FF', 'text': '#7E22CE', 'border': '#E9D5FF'},
    {'col': 6, 'label': '🟡 DEV IN PROG', 'bg': '#FEF9C3', 'text': '#A16207', 'border': '#FEF08A'},
    {'col': 8, 'label': '🟠 BA & TRANS', 'bg': '#FFEDD5', 'text': '#C2410C', 'border': '#FED7AA'},
    {'col': 10, 'label': '⚪ TO DO', 'bg': '#F1F5F9', 'text': '#475569', 'border': '#CBD5E1'}
]

row1_values = [None] * 12
for fc in filter_configs:
    c_idx = fc['col']
    l_idx = c_idx + 1
    # Ô Checkbox
    row1_values[c_idx] = {
        'userEnteredValue': {'boolValue': True},
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(fc['bg'])},
            'horizontalAlignment': 'CENTER',
            'verticalAlignment': 'MIDDLE',
            'borders': {
                'top': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}},
                'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}},
                'left': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}},
                'right': {'style': 'NONE'}
            }
        }
    }
    # Ô Nhãn
    row1_values[l_idx] = {
        'userEnteredValue': {'stringValue': fc['label']},
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(fc['bg'])},
            'horizontalAlignment': 'LEFT',
            'verticalAlignment': 'MIDDLE',
            'textFormat': {
                'fontFamily': 'Times New Roman',
                'fontSize': 10,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(fc['text'])}
            },
            'borders': {
                'top': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}},
                'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}},
                'left': {'style': 'NONE'},
                'right': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(fc['border'])}}
            }
        }
    }
row_data_list.append({'values': row1_values})

# Row 2: Month Headers
m10_cell = {
    'userEnteredValue': {'stringValue': 'THÁNG 10 / 2026'},
    'userEnteredFormat': {
        'backgroundColorStyle': {'rgbColor': hex_to_rgb('#005696')},
        'horizontalAlignment': 'CENTER',
        'verticalAlignment': 'MIDDLE',
        'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 11, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb('#FFFFFF')}},
        'borders': {d: {'style': 'SOLID_MEDIUM', 'colorStyle': {'rgbColor': hex_to_rgb('#003D6B')}} for d in ['top', 'bottom', 'left', 'right']}
    }
}
m11_cell = {
    'userEnteredValue': {'stringValue': 'THÁNG 11 / 2026'},
    'userEnteredFormat': {
        'backgroundColorStyle': {'rgbColor': hex_to_rgb('#6B21A8')},
        'horizontalAlignment': 'CENTER',
        'verticalAlignment': 'MIDDLE',
        'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 11, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb('#FFFFFF')}},
        'borders': {d: {'style': 'SOLID_MEDIUM', 'colorStyle': {'rgbColor': hex_to_rgb('#581C87')}} for d in ['top', 'bottom', 'left', 'right']}
    }
}
m12_cell = {
    'userEnteredValue': {'stringValue': 'THÁNG 12 / 2026'},
    'userEnteredFormat': {
        'backgroundColorStyle': {'rgbColor': hex_to_rgb('#047857')},
        'horizontalAlignment': 'CENTER',
        'verticalAlignment': 'MIDDLE',
        'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 11, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb('#FFFFFF')}},
        'borders': {d: {'style': 'SOLID_MEDIUM', 'colorStyle': {'rgbColor': hex_to_rgb('#065F46')}} for d in ['top', 'bottom', 'left', 'right']}
    }
}
row_data_list.append({'values': [m10_cell, {}, {}, {}, m11_cell, {}, {}, {}, m12_cell, {}, {}, {}]})

def canvas_cell(col_idx):
    bg = MONTH_BG['m10'] if col_idx < 4 else (MONTH_BG['m11'] if col_idx < 8 else MONTH_BG['m12'])
    return {'userEnteredFormat': {'backgroundColorStyle': {'rgbColor': hex_to_rgb(bg)}}}

# Task Rows
for t in sorted_tasks:
    cfg = STATUS_STEPS.get(t['status'], STATUS_STEPS['Chưa tiếp nhận'])
    prio_cfg = PRIO_STYLE.get(t['prio'], PRIO_STYLE['P2'])
    is_done = (t['status'] == 'Done')
    
    start_c = t['startCol']
    total_c = t['totalCols']
    left_c = 3 if total_c == 4 else 6
    right_c = total_c - left_c
    
    if is_done:
        colored_cols = total_c
    else:
        if total_c == 8:
            colored_cols = cfg['step']
        else:
            colored_cols = 1 if cfg['step'] <= 2 else (2 if cfg['step'] <= 5 else 3)
        if colored_cols < 1: colored_cols = 1
        if colored_cols >= total_c: colored_cols = total_c - 1
    white_cols = total_c - colored_cols

    pastel_bg = cfg['taskBg']
    card_border = '#CBD5E1'
    left_accent = cfg['barColor']

    epic_tag = f"[{t['epic']}]"
    full_title = f"{epic_tag} {t['title']}"
    title_font_size = 10 if len(full_title) > 42 else 11
    
    title_color = '#065F46' if is_done else '#0F172A'
    epic_color = '#047857' if is_done else get_epic_color(t['epic'])
    desc_color = '#047857' if is_done else '#475569'
    prio_color = prio_cfg['color']
    status_color = cfg['badgeColor']

    max_desc_len = 160 if left_c >= 6 else 80
    final_desc = t['desc']
    if len(final_desc) > max_desc_len:
        final_desc = final_desc[:max_desc_len - 3].strip() + '...'

    left_text = f"{full_title}\n{final_desc}"
    
    runs_left = [
        {
            'startIndex': 0,
            'format': {
                'fontFamily': 'Times New Roman',
                'fontSize': title_font_size,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(epic_color)}
            }
        },
        {
            'startIndex': len(epic_tag) + 1,
            'format': {
                'fontFamily': 'Times New Roman',
                'fontSize': title_font_size,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(title_color)}
            }
        },
        {
            'startIndex': len(full_title) + 1,
            'format': {
                'fontFamily': 'Times New Roman',
                'fontSize': 9,
                'italic': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(desc_color)}
            }
        }
    ]

    left_cell = {
        'userEnteredValue': {'stringValue': left_text},
        'textFormatRuns': runs_left,
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(pastel_bg)},
            'horizontalAlignment': 'LEFT',
            'verticalAlignment': 'MIDDLE',
            'wrapStrategy': 'CLIP',
            'borders': {
                'top': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}},
                'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}},
                'left': {'style': 'SOLID_THICK', 'colorStyle': {'rgbColor': hex_to_rgb(left_accent)}}
            }
        }
    }

    prio_tag = f"[{t['prio']}]"
    disp_status = t['status']
    if disp_status in ['PO reviewed/Transfer DEV', 'Transfer DEV/PO reviewed']: disp_status = 'Transfer DEV'
    elif disp_status == 'Đang phân tích/Document': disp_status = 'BA/Doc'
    elif disp_status == 'Đã tiếp nhận yêu cầu': disp_status = 'Đã tiếp nhận'
    elif disp_status == 'Chưa tiếp nhận': disp_status = 'To do'
    status_tag = f"[{disp_status}]"
    right_text = f"{prio_tag}\n{status_tag}"

    runs_right = [
        {
            'startIndex': 0,
            'format': {
                'fontFamily': 'Times New Roman',
                'fontSize': 10,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(prio_color)}
            }
        },
        {
            'startIndex': len(prio_tag) + 1,
            'format': {
                'fontFamily': 'Times New Roman',
                'fontSize': 9,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(status_color)}
            }
        }
    ]

    right_cell = {
        'userEnteredValue': {'stringValue': right_text},
        'textFormatRuns': runs_right,
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(pastel_bg)},
            'horizontalAlignment': 'RIGHT',
            'verticalAlignment': 'MIDDLE',
            'wrapStrategy': 'CLIP',
            'borders': {
                'top': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}},
                'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}},
                'right': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}}
            }
        }
    }

    # Card row
    card_row_cells = [canvas_cell(c) for c in range(12)]
    card_row_cells[start_c] = left_cell
    for c_i in range(start_c + 1, start_c + left_c): card_row_cells[c_i] = {}
    card_row_cells[start_c + left_c] = right_cell
    for c_i in range(start_c + left_c + 1, start_c + total_c): card_row_cells[c_i] = {}
    row_data_list.append({'values': card_row_cells})

    # Progress bar row
    bar_row_cells = [canvas_cell(c) for c in range(12)]
    prog_color_cell = {
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(cfg['barColor'])},
            'borders': {
                'left': {'style': 'SOLID_THICK', 'colorStyle': {'rgbColor': hex_to_rgb(left_accent)}},
                'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb('#059669' if is_done else cfg['barColor'])}}
            }
        }
    }
    bar_row_cells[start_c] = prog_color_cell
    for c_i in range(start_c + 1, start_c + colored_cols): bar_row_cells[c_i] = {}
    if white_cols > 0:
        white_cell = {
            'userEnteredFormat': {
                'backgroundColorStyle': {'rgbColor': hex_to_rgb('#F8FAFC')},
                'borders': {
                    'bottom': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}},
                    'right': {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(card_border)}}
                }
            }
        }
        bar_row_cells[start_c + colored_cols] = white_cell
        for c_i in range(start_c + colored_cols + 1, start_c + total_c): bar_row_cells[c_i] = {}
    row_data_list.append({'values': bar_row_cells})

    # Spacer row
    spacer_row_cells = [canvas_cell(c) for c in range(12)]
    row_data_list.append({'values': spacer_row_cells})

# Legend Row
legend_defs = [
    ('Done (100% Full)', '#D1FAE5', '#10B981', '#065F46'),
    ('UAT (75.0%)', '#F3E8FF', '#9333EA', '#6B21A8'),
    ('DEV In Progress (62.5%)', '#FEF9C3', '#EAB308', '#A16207'),
    ('Transfer DEV (50.0%)', '#FFF1F2', '#FB7185', '#BE123C'),
    ('BA / Document (37.5%)', '#FFEDD5', '#F97316', '#C2410C'),
    ('To do / Tiếp nhận (12.5-25%)', '#F1F5F9', '#94A3B8', '#475569')
]
legend_cells = [{}] * 12
for idx, (label, bg, border, txt_color) in enumerate(legend_defs):
    c_idx = idx * 2
    legend_cells[c_idx] = {
        'userEnteredValue': {'stringValue': f'■ {label}'},
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(bg)},
            'horizontalAlignment': 'CENTER',
            'verticalAlignment': 'MIDDLE',
            'textFormat': {
                'fontFamily': 'Times New Roman',
                'fontSize': 9,
                'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(txt_color)}
            },
            'borders': {d: {'style': 'SOLID', 'colorStyle': {'rgbColor': hex_to_rgb(border)}} for d in ['top', 'bottom', 'left', 'right']}
        }
    }
row_data_list.append({'values': legend_cells})

# Spacer before footer
row_data_list.append({'values': [{'userEnteredFormat': {'backgroundColorStyle': {'rgbColor': hex_to_rgb("#FFFFFF")}}}] * 12})

# Footer Row
footer_cell = {
    'userEnteredValue': {'stringValue': 'Nguồn: Backlog Website & CMS FPT.vn (Q4/2026) — Bố cục Thác nước Gantt (Waterfall Timeline)'},
    'userEnteredFormat': {
        'backgroundColorStyle': {'rgbColor': hex_to_rgb("#FFFFFF")},
        'horizontalAlignment': 'CENTER',
        'verticalAlignment': 'MIDDLE',
        'textFormat': {
            'fontFamily': 'Times New Roman',
            'fontSize': 9,
            'italic': True,
            'foregroundColorStyle': {'rgbColor': hex_to_rgb('#64748B')}
        }
    }
}
row_data_list.append({'values': [footer_cell] + [{}] * 11})

# Append updateCells request
batch_requests.append({
    'updateCells': {
        'range': {
            'sheetId': ROADMAP_GID,
            'startRowIndex': 0,
            'endRowIndex': len(row_data_list),
            'startColumnIndex': 0,
            'endColumnIndex': 12
        },
        'rows': row_data_list,
        'fields': 'userEnteredValue,userEnteredFormat,textFormatRuns'
    }
})

# Xóa Data Validation cũ trên toàn bộ Hàng 2
batch_requests.append({
    'setDataValidation': {
        'range': {
            'sheetId': ROADMAP_GID,
            'startRowIndex': 1,
            'endRowIndex': 2,
            'startColumnIndex': 0,
            'endColumnIndex': 12
        }
    }
})

# Checkbox Data Validation BOOLEAN cho 6 ô Checkbox (Row index 1, Cột 0, 2, 4, 6, 8, 10)
for fc in filter_configs:
    batch_requests.append({
        'setDataValidation': {
            'range': {
                'sheetId': ROADMAP_GID,
                'startRowIndex': 1,
                'endRowIndex': 2,
                'startColumnIndex': fc['col'],
                'endColumnIndex': fc['col'] + 1
            },
            'rule': {
                'condition': {
                    'type': 'BOOLEAN'
                },
                'showCustomUi': True
            }
        }
    })

print(f"Executing batch update on Roadmap_Timeline_Q4 with {len(batch_requests)} operations...")
batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{ROADMAP_SPREADSHEET_ID}:batchUpdate"
res1 = api_call(batch_url, {'requests': batch_requests}, method='POST')
print("Successfully updated Roadmap_Timeline_Q4 to Waterfall Gantt with Frozen Header & Quick Nav!")

# 3. Update Backlog_Data_Sync
sync_rows_data = []

# Title Row
sync_title_cell = {
    'userEnteredValue': {'stringValue': 'DANH SÁCH CHI TIẾT USER STORIES (ĐỒNG BỘ REALTIME TỪ GOOGLE SHEET GỐC)'},
    'userEnteredFormat': {
        'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 14, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb('#005696')}},
        'verticalAlignment': 'MIDDLE'
    }
}
sync_rows_data.append({'values': [sync_title_cell] + [{}] * 8})
sync_rows_data.append({'values': [{}] * 9})

# Headers Row
sync_headers = ['STT', 'Hệ thống', 'User Story / Đầu mục công việc', 'Tiến độ', 'Ưu tiên', 'PIC', 'Trạng thái', 'Timeline', 'Ghi chú tiến trình']
header_cells = []
for h in sync_headers:
    header_cells.append({
        'userEnteredValue': {'stringValue': h},
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb('#005696')},
            'horizontalAlignment': 'CENTER',
            'verticalAlignment': 'MIDDLE',
            'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb('#FFFFFF')}}
        }
    })
sync_rows_data.append({'values': header_cells})

for idx, t in enumerate(sorted_tasks, start=1):
    cfg = STATUS_STEPS.get(t['status'], STATUS_STEPS['Chưa tiếp nhận'])
    prio_cfg = PRIO_STYLE.get(t['prio'], PRIO_STYLE['P2'])
    note = f"Tháng {t['startM']} - Tháng {t['endM']}" if t['timeGroup'].startswith('span') else f"Hoàn thành trong T{t['endM']}"
    
    stt_c = {'userEnteredValue': {'numberValue': idx}, 'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    sys_c = {'userEnteredValue': {'stringValue': f"[{t['epic']}]"}, 'userEnteredFormat': {'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    title_c = {'userEnteredValue': {'stringValue': t['title']}, 'userEnteredFormat': {'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    prog_c = {'userEnteredValue': {'stringValue': cfg['percent']}, 'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10, 'bold': True}}}
    prio_c = {'userEnteredValue': {'stringValue': t['prio']}, 'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10, 'bold': True, 'foregroundColorStyle': {'rgbColor': hex_to_rgb(prio_cfg['color'])}}}}
    pic_c = {'userEnteredValue': {'stringValue': t['pic']}, 'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    
    status_c = {
        'userEnteredValue': {'stringValue': t['status']},
        'userEnteredFormat': {
            'backgroundColorStyle': {'rgbColor': hex_to_rgb(cfg['taskBg'])},
            'horizontalAlignment': 'CENTER',
            'textFormat': {
                'fontFamily': 'Times New Roman', 'fontSize': 10, 'bold': True,
                'foregroundColorStyle': {'rgbColor': hex_to_rgb(cfg['badgeColor'])}
            }
        }
    }
    tl_c = {'userEnteredValue': {'stringValue': t['timeline']}, 'userEnteredFormat': {'horizontalAlignment': 'CENTER', 'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    note_c = {'userEnteredValue': {'stringValue': note}, 'userEnteredFormat': {'textFormat': {'fontFamily': 'Times New Roman', 'fontSize': 10}}}
    
    sync_rows_data.append({'values': [stt_c, sys_c, title_c, prog_c, prio_c, pic_c, status_c, tl_c, note_c]})

sync_requests = [
    {
        'unmergeCells': {'range': {'sheetId': BACKLOG_SYNC_GID}}
    },
    {
        'updateSheetProperties': {
            'properties': {
                'sheetId': BACKLOG_SYNC_GID,
                'gridProperties': {
                    'rowCount': len(sync_rows_data) + 2,
                    'columnCount': 9
                }
            },
            'fields': 'gridProperties.rowCount,gridProperties.columnCount'
        }
    },
    {
        'mergeCells': {
            'range': {'sheetId': BACKLOG_SYNC_GID, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 9},
            'mergeType': 'MERGE_ALL'
        }
    },
    {
        'updateCells': {
            'range': {
                'sheetId': BACKLOG_SYNC_GID,
                'startRowIndex': 0,
                'endRowIndex': len(sync_rows_data),
                'startColumnIndex': 0,
                'endColumnIndex': 9
            },
            'rows': sync_rows_data,
            'fields': 'userEnteredValue,userEnteredFormat'
        }
    },
    {
        'autoResizeDimensions': {
            'dimensions': {
                'sheetId': BACKLOG_SYNC_GID,
                'dimension': 'COLUMNS',
                'startIndex': 0,
                'endIndex': 9
            }
        }
    }
]

print('Executing update on Backlog_Data_Sync...')
res2 = api_call(batch_url, {'requests': sync_requests}, method='POST')
print('Successfully updated Backlog_Data_Sync!')
print('ALL DONE!')

# -*- coding: utf-8 -*-
"""BPMN swimlane - Luồng Voucher Phase 2 (Internet/Combo & SKU/Camera)."""

ESC = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

LEFT_PAD = 260
LANE_W   = 420
LANE_X   = {0: LEFT_PAD, 1: LEFT_PAD+LANE_W, 2: LEFT_PAD+2*LANE_W}
LANES = [
    ("KHÁCH HÀNG",                            LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("WEBSITE FPT.VN (FRONTEND)",             LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("BACKEND & ECP (VOUCHER ENGINE)",         LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
HEADER_H = 46
ROW_H    = 90
TOP      = 80
BOXW, BOXH = 248, 58
NARROW   = 190

def lane_cx(l, half="c"):
    x = LANE_X[l]
    if half == "c":  return x + LANE_W/2
    if half == "l":  return x + LANE_W*0.27
    if half == "r":  return x + LANE_W*0.73

def row_y(r): return TOP + HEADER_H + r*ROW_H + ROW_H/2

# id: (lane, row, half, kind, label)
# kind: start | end | task | gw
N = {
  "start":    (0,  0, "c", "start", "Bắt đầu:\nChọn ưu đãi"),
  "k1":       (0,  1, "c", "task",  "Vào giỏ hàng (SKU)\nhoặc trang Checkout (Internet/Combo)"),
  "k2":       (0,  2, "c", "task",  "Click 'Chọn ưu đãi'\nhoặc nhập mã khuyến mãi"),
  "f1":       (1,  2, "c", "task",  "Mở popup Ưu đãi:\nSection Mã giảm giá + Chọn ưu đãi"),
  "b1":       (2,  3, "c", "task",  "Lấy danh sách voucher\ncủa KH từ ECP"),
  "gw_has":   (1,  4, "c", "gw",    "Có ưu đãi\nkhả dụng?"),
  "f2_no":    (1,  5, "r", "task",  "Hiển thị:\n'Rất tiếc, quý khách\nkhông có mã ưu đãi'"),
  "f2_yes":   (1,  5, "l", "task",  "Hiển thị danh sách:\nActive lên đầu · Label D-3\nScroll khi > 452px"),
  "k3":       (0,  6, "c", "task",  "Nhập mã tay\nhoặc chọn voucher từ list"),
  "gw_input": (1,  7, "c", "gw",    "Cách nhập\nvoucher?"),
  "f3_code":  (1,  8, "l", "task",  "KH nhập mã tay\n→ Bấm 'Áp dụng'"),
  "f3_pick":  (1,  8, "r", "task",  "KH chọn từ popup\n→ Bấm 'Sử dụng ưu đãi'"),
  "b2":       (2,  9, "c", "task",  "Validate voucher:\n• Điều kiện đơn tối thiểu\n• PTTT hợp lệ\n• SL SP / Khu vực / Loại trừ"),
  "gw_valid": (2, 10, "c", "gw",    "Voucher\nhợp lệ?"),
  "b3_ok":    (2, 11, "l", "task",  "Tính số tiền giảm\n→ Trả kết quả FE"),
  "b3_err":   (2, 11, "r", "task",  "Trả mã lỗi:\n• Không đủ điều kiện\n• Loại trừ với voucher khác\n• Mã không tồn tại"),
  "f4_ok":    (1, 12, "l", "task",  "Áp dụng giảm giá:\nCập nhật tổng tiền · Đóng popup\nHiển thị '1 ưu đãi' trên section"),
  "f4_err":   (1, 12, "r", "task",  "Disable voucher + Show thông báo:\n• 'Không đủ điều kiện tham gia'\n• 'Không áp dụng đồng thời...'"),
  "k4":       (0, 13, "c", "task",  "Xem tóm tắt giảm giá\ntrên đơn hàng"),
  "gw_change":(0, 14, "c", "gw",    "KH muốn\nthay đổi ưu đãi?"),
  "k5":       (0, 15, "c", "task",  "Tiếp tục thanh toán\n(bước Xác nhận & Thanh toán)"),
  "end_ok":   (0, 16, "l", "end",   "Đơn hàng\nhoàn tất"),
  "end_no":   (0,  5, "r", "end",   "Không có\nưu đãi"),
}

EDGES = [
  ("start",    "k1",      "",            False),
  ("k1",       "k2",      "",            False),
  ("k2",       "f1",      "",            False),
  ("f1",       "b1",      "",            False),
  ("b1",       "gw_has",  "",            False),
  ("gw_has",   "f2_yes",  "Có",          False),
  ("gw_has",   "f2_no",   "Không",       False),
  ("f2_no",    "end_no",  "",            False),
  ("f2_yes",   "k3",      "",            False),
  ("k3",       "gw_input","",            False),
  ("gw_input", "f3_code", "Nhập mã",     False),
  ("gw_input", "f3_pick", "Chọn popup",  False),
  ("f3_code",  "b2",      "",            False),
  ("f3_pick",  "b2",      "",            False),
  ("b2",       "gw_valid","",            False),
  ("gw_valid", "b3_ok",   "Có",          False),
  ("gw_valid", "b3_err",  "Không",       False),
  ("b3_ok",    "f4_ok",   "",            False),
  ("b3_err",   "f4_err",  "",            False),
  ("f4_ok",    "k4",      "",            False),
  ("f4_err",   "k3",      "Chỉnh lại",   True),
  ("k4",       "gw_change","",           False),
  ("gw_change","k3",      "Có",          True),
  ("gw_change","k5",      "Không",       False),
  ("k5",       "end_ok",  "",            False),
]

ANNOTATIONS = [
  (1, 3, "l", "[VCP-BR-01] Tên/Mô tả/Ảnh\nvoucher: CMS cấu hình\nriêng cho Web"),
  (2, 9, "r", "[VCP-BR-02] Cơ cấu loại trừ:\nKhi chọn A → disable B\n'Không áp dụng đồng thời'"),
  (1, 5, "c", "[VCP-BR-03] Sort: Active lên\nđầu · D-3 label 'Sắp hết hạn'\nScroll popup > 452px"),
]

# ─────────── SVG BUILDERS ───────────
def circle(cx,cy,r,fill,stroke,sw=2):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def diamond(cx,cy,half,fill,stroke,sw=2):
    pts=f"{cx},{cy-half} {cx+half},{cy} {cx},{cy+half} {cx-half},{cy}"
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def rounded_rect(cx,cy,w,h,fill,stroke,sw=1.5,r=8):
    x,y=cx-w/2, cy-h/2
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def text_block(cx,cy,label,color="#000",fs=9.5,bold=False):
    lines=[l for l in label.split("\n") if l.strip()]
    n=len(lines); lh=13
    start_y=cy - (n-1)*lh/2
    fw="bold" if bold else "normal"
    out=""
    for i,ln in enumerate(lines):
        dy=start_y+i*lh
        out+=f'<text x="{cx}" y="{dy}" text-anchor="middle" dominant-baseline="middle" font-family="Arial" font-size="{fs}" fill="{color}" font-weight="{fw}">{ESC(ln)}</text>\n'
    return out

def node_svg(nid):
    l,r,half,kind,label = N[nid][:5]
    cx,cy = lane_cx(l,half), row_y(r)
    lane_col = LANES[l][3]
    out=""
    if kind=="start":
        out+=circle(cx,cy,18,"#d6f5d6",lane_col,2.5)
        out+=text_block(cx,cy,label,lane_col,8.5)
    elif kind=="end":
        out+=circle(cx,cy,18,"#fde0d0",lane_col,2.5)
        out+=circle(cx,cy,13,"#c00000","#c00000",0)
        out+=text_block(cx,cy+28,label,"#c00000",8.5)
    elif kind=="task":
        w=BOXW; h=BOXH
        out+=rounded_rect(cx,cy,w,h,"white",lane_col,1.5)
        out+=text_block(cx,cy,label,lane_col,8.5)
    elif kind=="gw":
        out+=diamond(cx,cy,26,"#fff9e6",lane_col,2)
        out+=text_block(cx,cy,label,lane_col,8.5)
    return out

def get_edge_pts(src,dst):
    l0,r0,h0,k0,_=N[src][:5]; cx0,cy0=lane_cx(l0,h0),row_y(r0)
    l1,r1,h1,k1,_=N[dst][:5]; cx1,cy1=lane_cx(l1,h1),row_y(r1)
    if k0=="gw": cy0=cy0+26
    elif k0=="start" or k0=="end": cy0=cy0+18
    else: cy0=cy0+BOXH/2
    if k1=="gw": cy1=cy1-26
    elif k1=="start" or k1=="end": cy1=cy1-18
    else: cy1=cy1-BOXH/2
    return cx0,cy0,cx1,cy1

def arrow(x1,y1,x2,y2,dashed=False,color="#333",label="",label_color="#555"):
    dash=""
    if dashed: dash='stroke-dasharray="6,4"'
    mid_x=(x1+x2)/2; mid_y=(y1+y2)/2
    if abs(x1-x2)>10:
        path=f"M{x1},{y1} C{x1},{mid_y} {x2},{mid_y} {x2},{y2}"
    else:
        path=f"M{x1},{y1} L{x2},{y2}"
    out=f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1.5" {dash} marker-end="url(#arr)"/>\n'
    if label:
        out+=f'<text x="{mid_x+4}" y="{mid_y-4}" font-family="Arial" font-size="8" fill="{label_color}">{ESC(label)}</text>\n'
    return out

def annotation_svg(row, col_half, lane_idx, text):
    ax = lane_cx(lane_idx, col_half) + BOXW/2 + 14
    ay = row_y(row) - BOXH/2
    lines = text.split("\n")
    h = len(lines)*13+10; w=180
    out = f'<rect x="{ax}" y="{ay}" width="{w}" height="{h}" rx="4" fill="#fffbe6" stroke="#f0c040" stroke-width="1" stroke-dasharray="5,3"/>\n'
    out += f'<line x1="{ax-14}" y1="{ay+h/2}" x2="{ax}" y2="{ay+h/2}" stroke="#f0c040" stroke-width="1" stroke-dasharray="4,3"/>\n'
    for i,ln in enumerate(lines):
        out += f'<text x="{ax+6}" y="{ay+13+i*13}" font-family="Arial" font-size="8" fill="#7b5e00">{ESC(ln)}</text>\n'
    return out

def build_svg():
    total_rows = max(N[nid][1] for nid in N) + 1
    TOTAL_H = TOP + HEADER_H + total_rows*ROW_H + 60
    TOTAL_W = LEFT_PAD + len(LANES)*LANE_W + 220

    lines=[f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{TOTAL_W}" height="{TOTAL_H}">
<defs>
  <marker id="arr" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
  </marker>
</defs>
<!-- BG -->
<rect width="{TOTAL_W}" height="{TOTAL_H}" fill="white"/>
''']

    # Title
    lines.append(f'<rect x="0" y="0" width="{TOTAL_W}" height="{TOP}" fill="#1f4e78"/>')
    lines.append(f'<text x="{TOTAL_W//2}" y="28" text-anchor="middle" font-family="Arial" font-size="15" font-weight="bold" fill="white">BPMN — LUỒNG CHỌN VÀ ÁP DỤNG VOUCHER (PHASE 2)</text>')
    lines.append(f'<text x="{TOTAL_W//2}" y="52" text-anchor="middle" font-family="Arial" font-size="10" fill="#a8c8f0">Phạm vi: Dịch vụ Internet/Combo (Checkout) · Sản phẩm SKU/Camera (Giỏ hàng)</text>')
    lines.append(f'<text x="{TOTAL_W//2}" y="68" text-anchor="middle" font-family="Arial" font-size="9" fill="#7aa8d0">FPT.VN · Voucher Phase 2 · 2025</text>')

    # Pool border
    pool_x = LEFT_PAD - 8
    pool_y = TOP
    pool_w = len(LANES)*LANE_W + 16
    pool_h = HEADER_H + total_rows*ROW_H + 8
    lines.append(f'<rect x="{pool_x}" y="{pool_y}" width="{pool_w}" height="{pool_h}" rx="6" fill="none" stroke="#999" stroke-width="1.5"/>')

    # Pool label (left sidebar)
    lines.append(f'<rect x="{LEFT_PAD-260}" y="{TOP}" width="248" height="{pool_h}" rx="4" fill="#f0f4fa" stroke="#ccc" stroke-width="1"/>')
    lines.append(f'<text x="{LEFT_PAD-136}" y="{TOP + pool_h//2}" text-anchor="middle" dominant-baseline="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#1f4e78" transform="rotate(-90,{LEFT_PAD-136},{TOP + pool_h//2})">LUỒNG VOUCHER FPT.VN PHASE 2</text>')

    # Lanes
    lh = HEADER_H + total_rows*ROW_H + 8
    for i,(lname,lx,lw,lc,lbg) in enumerate(LANES):
        lines.append(f'<rect x="{lx}" y="{TOP}" width="{lw}" height="{lh}" fill="{lbg}" stroke="#bbb" stroke-width="1"/>')
        lines.append(f'<rect x="{lx}" y="{TOP}" width="{lw}" height="{HEADER_H}" fill="{lc}" opacity="0.15" stroke="#bbb" stroke-width="1"/>')
        lines.append(f'<text x="{lx+lw//2}" y="{TOP+HEADER_H//2+5}" text-anchor="middle" font-family="Arial" font-size="10.5" font-weight="bold" fill="{lc}">{ESC(lname)}</text>')
        # row guides
        for r in range(total_rows+1):
            gy = TOP + HEADER_H + r*ROW_H
            lines.append(f'<line x1="{lx}" y1="{gy}" x2="{lx+lw}" y2="{gy}" stroke="#e0e8f0" stroke-width="0.5"/>')

    # Nodes
    for nid in N:
        lines.append(node_svg(nid))

    # Edges
    for (src,dst,lbl,dashed) in EDGES:
        x1,y1,x2,y2 = get_edge_pts(src,dst)
        lines.append(arrow(x1,y1,x2,y2,dashed,label=lbl))

    # Annotations
    for (row, half, lane_hint, txt) in ANNOTATIONS:
        ann_lane = {"l":0,"c":1,"r":2}.get(lane_hint,1)
        lines.append(annotation_svg(row, "c", ann_lane, txt))

    # Legend
    lx0 = LEFT_PAD - 258
    ly0 = TOP + pool_h + 10
    lines.append(f'<text x="{lx0}" y="{ly0+14}" font-family="Arial" font-size="9.5" font-weight="bold" fill="#1f4e78">LEGEND (Ký hiệu BPMN)</text>')
    items=[
        ("#d6f5d6","#1f4e78","start","Start Event"),
        ("#fde0d0","#c00000","end",  "End Event"),
        ("white",  "#2e75b6","task", "Task / Activity"),
        ("#fff9e6","#7030a0","gw",   "Exclusive Gateway (×)"),
        ("white",  "none",   "ann",  "Text Annotation (BR)"),
        ("white",  "none",   "dash", "Luồng quay lui (nét đứt)"),
    ]
    for i,(fc,sc,tp,lbl) in enumerate(items):
        lyi=ly0+30+i*20
        if tp=="start": lines.append(circle(lx0+10,lyi,8,fc,sc,2))
        elif tp=="end":  lines.append(circle(lx0+10,lyi,8,fc,sc,2)+circle(lx0+10,lyi,5,"#c00000","#c00000",0))
        elif tp=="task": lines.append(rounded_rect(lx0+10,lyi,30,14,fc,sc,1.5,3))
        elif tp=="gw":   lines.append(diamond(lx0+10,lyi,10,fc,sc,1.5))
        elif tp=="ann":  lines.append(f'<rect x="{lx0+3}" y="{lyi-7}" width="14" height="14" rx="2" fill="#fffbe6" stroke="#f0c040" stroke-width="1" stroke-dasharray="4,2"/>')
        elif tp=="dash": lines.append(f'<line x1="{lx0+3}" y1="{lyi}" x2="{lx0+20}" y2="{lyi}" stroke="#333" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arr)"/>')
        lines.append(f'<text x="{lx0+26}" y="{lyi+4}" font-family="Arial" font-size="8.5" fill="#333">{ESC(lbl)}</text>')

    lines.append('</svg>')
    return "\n".join(lines)

if __name__ == "__main__":
    svg = build_svg()
    out_path = "diagrams/voucher_bpmn.svg"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {out_path}")

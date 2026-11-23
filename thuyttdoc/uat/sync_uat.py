#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: sync_uat.py
Mục đích: Đồng bộ 2 chiều (Bidirectional Synchronization) giữa file UAT Excel local và Google Sheet online.
Dự án: Xây dựng luồng giỏ hàng trên website (FPT.vn)
Mã hiệu UAT: 4.0-BM/PM/HDCV/FTEL
Spreadsheet ID Online: 1WGZ07fepEO91UXKi5AuSrwf00gQq87yGTnrRxD5_ooQ
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
import openpyxl

TOKEN_PATH = '/Users/hathuy/.gemini/antigravity/plugin_data/gsheets/token.json'
SPREADSHEET_ID = '1WGZ07fepEO91UXKi5AuSrwf00gQq87yGTnrRxD5_ooQ'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_XLSX_PATH = os.path.join(SCRIPT_DIR, 'UAT_GioHang_FPT_VN.xlsx')

def get_valid_token():
    """Lấy access_token hợp lệ từ token.json, tự động refresh nếu hết hạn."""
    if not os.path.exists(TOKEN_PATH):
        raise FileNotFoundError(f"Không tìm thấy file token tại: {TOKEN_PATH}")
    
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
            token = res['access_token']
            data['token']['access_token'] = token
            with open(TOKEN_PATH, 'w') as f_out:
                json.dump(data, f_out, indent=2)
            return token
    except Exception as e:
        print(f"[Cảnh báo] Refresh token lỗi ({e}), sử dụng access_token hiện tại.")
        return data.get('token', {}).get('access_token')

def pull_from_online():
    """Tải dữ liệu mới nhất từ Google Sheets online về đè vào file local Excel."""
    print(f"[*] Đang kết nối Google Sheets (ID: {SPREADSHEET_ID})...")
    token = get_valid_token()
    url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=xlsx"
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
    
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            if os.path.exists(LOCAL_XLSX_PATH):
                backup_path = LOCAL_XLSX_PATH + f".bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                os.rename(LOCAL_XLSX_PATH, backup_path)
                print(f"[+] Đã tạo bản sao lưu local tại: {os.path.basename(backup_path)}")
            
            with open(LOCAL_XLSX_PATH, 'wb') as f:
                f.write(content)
            print(f"[✓] Đồng bộ PULL thành công! Đã cập nhật file local: {LOCAL_XLSX_PATH} ({len(content)} bytes)")
    except Exception as e:
        print(f"[!] Lỗi khi PULL từ Google Sheets: {e}")
        sys.exit(1)

def push_to_online():
    """Đọc dữ liệu từ file local Excel và đẩy cập nhật lên Google Sheets online."""
    if not os.path.exists(LOCAL_XLSX_PATH):
        print(f"[!] Không tìm thấy file local tại: {LOCAL_XLSX_PATH}")
        sys.exit(1)
        
    print(f"[*] Đang đọc file local: {LOCAL_XLSX_PATH}...")
    wb = openpyxl.load_workbook(LOCAL_XLSX_PATH, data_only=False)
    
    # 1. Đọc dữ liệu Report từ local (bắt đầu từ hàng 10)
    ws_report = wb['Report']
    test_rows = []
    r = 10
    while r <= ws_report.max_row:
        no_val = ws_report.cell(r, 2).value
        if not no_val:
            break
        row_data = [
            str(no_val),
            str(ws_report.cell(r, 3).value or ''),
            str(ws_report.cell(r, 4).value or ''),
            '', '',
            str(ws_report.cell(r, 7).value or ''),
            '', '',
            str(ws_report.cell(r, 10).value or ''),
            str(ws_report.cell(r, 11).value or ''),
            str(ws_report.cell(r, 12).value or ''),
            str(ws_report.cell(r, 13).value or '')
        ]
        test_rows.append(row_data)
        r += 1

    end_row = 9 + len(test_rows)
    print(f"[*] Đã đọc được {len(test_rows)} kịch bản test (Row 10 đến Row {end_row}).")
    
    # 2. Đọc dữ liệu Summary từ local
    ws_summary = wb['Summary']
    summary_rows = []
    for sr in range(10, 25):
        mod_no = ws_summary.cell(sr, 2).value
        if mod_no:
            summary_rows.append([
                str(mod_no),
                str(ws_summary.cell(sr, 3).value or ''),
                str(ws_summary.cell(sr, 4).value or ''),
                str(ws_summary.cell(sr, 5).value or '')
            ])
            
    token = get_valid_token()
    
    payload = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {
                "range": f"Report!B10:M{end_row}",
                "values": test_rows
            },
            {
                "range": f"Summary!B10:E{9 + len(summary_rows)}",
                "values": summary_rows
            }
        ]
    }
    
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values:batchUpdate"
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }, method='POST')
    
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"[✓] Đồng bộ PUSH thành công lên Google Sheets online!")
            print(f"    - Tổng số ô cập nhật: {res.get('totalUpdatedCells', 0)}")
            print(f"    - Link online: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    except Exception as e:
        print(f"[!] Lỗi khi PUSH lên Google Sheets: {e}")
        sys.exit(1)

def show_status():
    """Kiểm tra và báo cáo trạng thái đồng bộ giữa local và online."""
    print("=" * 65)
    print(" BÁO CÁO TRẠNG THÁI ĐỒNG BỘ UAT - FPT TELECOM")
    print("=" * 65)
    print(f"• Local file:  {LOCAL_XLSX_PATH}")
    if os.path.exists(LOCAL_XLSX_PATH):
        mtime = datetime.fromtimestamp(os.path.getmtime(LOCAL_XLSX_PATH)).strftime('%Y-%m-%d %H:%M:%S')
        wb = openpyxl.load_workbook(LOCAL_XLSX_PATH, data_only=True)
        ws = wb['Report']
        tc_count = 0
        passed_count = 0
        for r in range(10, ws.max_row + 1):
            if ws.cell(r, 2).value:
                tc_count += 1
                if ws.cell(r, 10).value == 'PASSED':
                    passed_count += 1
        print(f"  - Trạng thái:  Tồn tại (Sửa đổi lần cuối: {mtime})")
        print(f"  - Số Test Case: {tc_count} kịch bản (Passed: {passed_count}/{tc_count})")
    else:
        print(f"  - Trạng thái:  Chưa có file local.")
        
    print(f"• Online Sheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    try:
        token = get_valid_token()
        meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}?includeGridData=false"
        req = urllib.request.Request(meta_url, headers={'Authorization': f'Bearer {token}'})
        with urllib.request.urlopen(req) as resp:
            s_data = json.loads(resp.read().decode('utf-8'))
            title = s_data['properties']['title']
            sheets = [s['properties']['title'] for s in s_data['sheets']]
            print(f"  - Tiêu đề:     {title}")
            print(f"  - Các Sheets:  {', '.join(sheets)}")
            print(f"  - Kết nối:     Trực tuyến (API OAuth2 Active)")
    except Exception as e:
        print(f"  - Kết nối:     Lỗi ({e})")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Công cụ đồng bộ 2 chiều UAT FPT Telecom giữa Local Excel và Google Sheets.")
    parser.add_argument("--push", action="store_true", help="Đẩy dữ liệu từ Local Excel lên Google Sheets")
    parser.add_argument("--pull", action="store_true", help="Tải dữ liệu từ Google Sheets về Local Excel")
    parser.add_argument("--status", action="store_true", help="Xem trạng thái đồng bộ giữa 2 bên")
    
    args = parser.parse_args()
    if args.push:
        push_to_online()
    elif args.pull:
        pull_from_online()
    elif args.status:
        show_status()
    else:
        show_status()
        print("\nHướng dẫn sử dụng:")
        print("  python3 sync_uat.py --push   : Đẩy thay đổi từ Local lên Google Sheets")
        print("  python3 sync_uat.py --pull   : Tải thay đổi từ Google Sheets về Local")
        print("  python3 sync_uat.py --status : Kiểm tra trạng thái đồng bộ")

if __name__ == '__main__':
    main()

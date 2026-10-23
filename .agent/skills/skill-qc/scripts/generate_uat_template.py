#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: generate_uat_template.py
Mục đích: Tự động sinh file Excel UAT Template chuẩn FPT Telecom (4 sheets: Cover, Summary, Report, Guideline)
Đặc điểm:
- Ứng dụng chuẩn 3 màu nhận diện thương hiệu FPT (Xanh dương #0054A6, Cam #F26522, Xanh lá #009E49)
- Vận dụng tư duy Designer: trực quan, phân cấp thị giác rõ ràng, font Times New Roman, dễ thao tác
- Tích hợp công thức tính tự động SUM/COUNTIF, Dropdown Data Validation và Conditional Formatting
"""

import os
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# --- BẢNG MÀU CHUẨN THƯƠNG HIỆU FPT & DESIGN SYSTEM ---
FPT_BLUE_HEX = "0054A6"        # Xanh dương FPT - Đại diện cho công nghệ, độ tin cậy, vững bền
FPT_ORANGE_HEX = "F26522"      # Cam FPT - Đại diện cho nhiệt huyết, năng động, sáng tạo
FPT_GREEN_HEX = "009E49"       # Xanh lá FPT - Đại diện cho sức sống, đổi mới, thành công

# Bảng màu hỗ trợ (Neutral & Semantic Soft Tints theo tiêu chuẩn Designer)
BG_LIGHT_BLUE = "F0F4F9"       # Nền xanh dịu cho dòng chẵn hoặc ô tiêu đề phụ
BG_LIGHT_GRAY = "F8FAFC"       # Nền xám nhạt trung tính
BG_BORDER_GRAY = "CBD5E1"      # Viền xám mờ tinh tế (Slate 300)
TEXT_DARK = "1E293B"           # Màu chữ chính (Slate 800)
TEXT_MUTED = "64748B"          # Màu chữ phụ (Slate 500)
WHITE = "FFFFFF"

# Màu trạng thái Semantic (Dịu mắt, độ tương phản chuẩn WCAG AA)
FILL_PASSED = "D1FAE5"         # Xanh lục nhạt
TEXT_PASSED = "065F46"         # Xanh lục sẫm
FILL_FAILED = "FEE2E2"         # Đỏ nhạt
TEXT_FAILED = "991B1B"         # Đỏ sẫm
FILL_PENDING = "FEF3C7"        # Vàng cam nhạt
TEXT_PENDING = "92400E"        # Nâu cam sẫm
FILL_NA = "F1F5F9"             # Xám bạc
TEXT_NA = "475569"             # Xám sẫm

FONT_FAMILY = "Times New Roman"

def create_thin_border(color=BG_BORDER_GRAY):
    s = Side(style='thin', color=color)
    return Border(left=s, right=s, top=s, bottom=s)

def create_header_border():
    s = Side(style='thin', color="FFFFFF")
    return Border(left=s, right=s, top=s, bottom=s)

def style_range(ws, cell_range, font=None, fill=None, border=None, alignment=None):
    """Áp dụng style cho toàn bộ vùng ô (bao gồm các ô bị merge)"""
    for row in ws[cell_range]:
        for cell in row:
            if font: cell.font = font
            if fill: cell.fill = fill
            if border: cell.border = border
            if alignment: cell.alignment = alignment

def build_cover_sheet(wb):
    ws = wb.create_sheet(title="Cover")
    ws.views.sheetView[0].showGridLines = True
    
    # Cấu hình độ rộng cột
    for col_idx in range(1, 16):
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = 10 if col_idx not in (2, 6, 9) else 18

    # Dòng 10: Tiêu đề lớn
    ws.merge_cells("B10:O10")
    ws["B10"] = "USER ACCEPTANCE TEST - UAT"
    ws["B10"].font = Font(name=FONT_FAMILY, size=24, bold=True, color=FPT_ORANGE_HEX)
    ws["B10"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[10].height = 50

    # Dòng 12: Mã hiệu
    ws.merge_cells("F12:H12")
    ws["F12"] = "Mã hiệu"
    ws["F12"].font = Font(name=FONT_FAMILY, size=12, bold=True, color=FPT_BLUE_HEX)
    ws["F12"].alignment = Alignment(horizontal="center", vertical="center")
    ws["F12"].fill = PatternFill(start_color=BG_LIGHT_BLUE, fill_type="solid")
    
    ws.merge_cells("I12:K12")
    ws["I12"] = "4.0-BM/PM/HDCV/FTEL"
    ws["I12"].font = Font(name=FONT_FAMILY, size=12, bold=True, color=TEXT_DARK)
    ws["I12"].alignment = Alignment(horizontal="center", vertical="center")

    # Dòng 13: Phiên bản
    ws.merge_cells("F13:H13")
    ws["F13"] = "Phiên bản"
    ws["F13"].font = Font(name=FONT_FAMILY, size=12, bold=True, color=FPT_BLUE_HEX)
    ws["F13"].alignment = Alignment(horizontal="center", vertical="center")
    ws["F13"].fill = PatternFill(start_color=BG_LIGHT_BLUE, fill_type="solid")

    ws.merge_cells("I13:K13")
    ws["I13"] = "1.0"
    ws["I13"].font = Font(name=FONT_FAMILY, size=12, bold=True, color=TEXT_DARK)
    ws["I13"].alignment = Alignment(horizontal="center", vertical="center")

    thin_border = create_thin_border()
    style_range(ws, "F12:K13", border=thin_border)
    ws.row_dimensions[12].height = 25
    ws.row_dimensions[13].height = 25

def build_summary_sheet(wb):
    ws = wb.create_sheet(title="Summary")
    ws.views.sheetView[0].showGridLines = True

    # Cấu hình độ rộng cột
    ws.column_dimensions["A"].width = 5
    ws.column_dimensions["B"].width = 8
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 35
    ws.column_dimensions["E"].width = 25
    ws.column_dimensions["F"].width = 35

    # Dòng 1: Tiêu đề Sheet
    ws["D1"] = "UAT SUMMARY"
    ws["D1"].font = Font(name=FONT_FAMILY, size=20, bold=True, color=FPT_ORANGE_HEX)
    ws["D1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 35

    # Bảng Metadata dự án (Dòng 3 - 6)
    meta_fields = [
        (3, "Project name", "FPT.VN", "Testing start date", ""),
        (4, "Version", "1.0", "Testing end date", ""),
        (5, "PO - Product Owner", "ThuyTT104", "Account Test - Division", "ISC / Tester"),
        (6, "PM - Project Manager", "", "", "")
    ]

    thin_border = create_thin_border()
    header_fill = PatternFill(start_color=BG_LIGHT_BLUE, fill_type="solid")

    for r, label_c, val_d, label_e, val_f in meta_fields:
        ws.row_dimensions[r].height = 24
        # Cột C
        ws.cell(r, 3, label_c).font = Font(name=FONT_FAMILY, size=12, bold=True, color=FPT_BLUE_HEX)
        ws.cell(r, 3).fill = header_fill
        ws.cell(r, 3).border = thin_border
        ws.cell(r, 3).alignment = Alignment(vertical="center")

        # Cột D
        ws.cell(r, 4, val_d).font = Font(name=FONT_FAMILY, size=12, bold=(r==5), color=TEXT_DARK)
        ws.cell(r, 4).border = thin_border
        ws.cell(r, 4).alignment = Alignment(vertical="center")

        # Cột E
        if label_e:
            ws.cell(r, 5, label_e).font = Font(name=FONT_FAMILY, size=12, bold=True, color=FPT_BLUE_HEX)
            ws.cell(r, 5).fill = header_fill
            ws.cell(r, 5).border = thin_border
            ws.cell(r, 5).alignment = Alignment(vertical="center")

            # Cột F
            ws.cell(r, 6, val_f).font = Font(name=FONT_FAMILY, size=12, color=TEXT_DARK)
            ws.cell(r, 6).border = thin_border
            ws.cell(r, 6).alignment = Alignment(vertical="center")

    # Dòng 9: Header danh sách Module
    ws.row_dimensions[9].height = 28
    headers_summary = [
        (2, "NO."),
        (3, "MODULE"),
        (4, "STATUS"),
        (5, "COMMENTS")
    ]
    # Merge E9:F9 cho Comments rộng rãi
    ws.merge_cells("E9:F9")

    blue_fill = PatternFill(start_color=FPT_BLUE_HEX, fill_type="solid")
    white_bold = Font(name=FONT_FAMILY, size=12, bold=True, color=WHITE)

    for col_idx, text in headers_summary:
        cell = ws.cell(9, col_idx, text)
        cell.font = white_bold
        cell.fill = blue_fill
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = create_header_border()
    ws.cell(9, 6).fill = blue_fill
    ws.cell(9, 6).border = create_header_border()

    # Dòng 10 - 20: Danh sách Module mẫu
    for idx, r in enumerate(range(10, 21), start=1):
        ws.row_dimensions[r].height = 22
        ws.merge_cells(f"E{r}:F{r}")
        ws.cell(r, 2, f"{float(idx):.1f}").alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(r, 2).font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_BLUE_HEX)
        
        for c in range(2, 7):
            ws.cell(r, c).border = thin_border
            if c != 2:
                ws.cell(r, c).font = Font(name=FONT_FAMILY, size=11, color=TEXT_DARK)
                ws.cell(r, c).alignment = Alignment(vertical="center")

def build_report_sheet(wb):
    ws = wb.create_sheet(title="Report")
    ws.views.sheetView[0].showGridLines = True

    # Cấu hình độ rộng các cột
    col_widths = {
        'A': 4,
        'B': 7,    # NO.
        'C': 30,   # MODULE
        'D': 15,   # STEPS 1
        'E': 15,   # STEPS 2
        'F': 15,   # STEPS 3 (Merged D-F: 45)
        'G': 15,   # EXPECTED 1
        'H': 15,   # EXPECTED 2
        'I': 15,   # EXPECTED 3 (Merged G-I: 45)
        'J': 15,   # R1 STATUS
        'K': 35,   # R1 DESCRIPTION
        'L': 16,   # R1 ACTION
        'M': 35,   # R1 NOTE
        'N': 15,   # R2 STATUS
        'O': 35,   # R2 MÔ TẢ LỖI
        'P': 16,   # R2 ACTION
        'Q': 35,   # R2 NOTE
        'R': 15,   # R3 STATUS
        'S': 35,   # R3 MÔ TẢ LỖI
        'T': 16,   # R3 ACTION
        'U': 35,   # R3 NOTE
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

    # Dòng 1: Tiêu đề Sheet
    ws["D1"] = "UAT REPORT"
    ws["D1"].font = Font(name=FONT_FAMILY, size=24, bold=True, color=FPT_ORANGE_HEX)
    ws["D1"].alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 40

    # --- BẢNG THỐNG KÊ DASHBOARD KẾT QUẢ VÒNG TEST (Dòng 3 - 5) ---
    dash_headers = ["NO.", "ROUND", "TOTAL", "PASSED", "FAILED", "PENDING", "N/A"]
    ws.row_dimensions[3].height = 26
    
    header_blue_light = PatternFill(start_color="DCE6F1", fill_type="solid")
    font_dash_hdr = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_BLUE_HEX)
    thin_border = create_thin_border()

    for idx, text in enumerate(dash_headers, start=2):
        cell = ws.cell(3, idx, text)
        cell.font = font_dash_hdr
        cell.fill = header_blue_light
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    # Dòng 4: Round 1 Counts
    ws.row_dimensions[4].height = 24
    ws.cell(4, 2, 1.0).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 3, "ROUND 1").alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 3).font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_GREEN_HEX)
    ws.cell(4, 3).fill = PatternFill(start_color="E2EFDA", fill_type="solid")

    ws.cell(4, 4, "=SUM($E4:$H4)").font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_BLUE_HEX)
    ws.cell(4, 4).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 4).fill = PatternFill(start_color="FFF2CC", fill_type="solid")

    ws.cell(4, 5, '=COUNTIF($J$10:$J$50,"PASSED")').alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 5).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_PASSED)

    ws.cell(4, 6, '=COUNTIF($J$10:$J$50,"FAILED")').alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 6).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_FAILED)

    ws.cell(4, 7, '=COUNTIF($J$10:$J$50,"PENDING")').alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 7).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_PENDING)

    ws.cell(4, 8, '=COUNTIF($J$10:$J$50,"N/A")').alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(4, 8).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_NA)

    for c in range(2, 9):
        ws.cell(4, c).border = thin_border

    # Dòng 5: TOTAL
    ws.row_dimensions[5].height = 24
    ws.merge_cells("B5:C5")
    ws.cell(5, 2, "TOTAL").alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(5, 2).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_DARK)
    ws.cell(5, 2).fill = PatternFill(start_color="E9EEF4", fill_type="solid")
    ws.cell(5, 3).fill = PatternFill(start_color="E9EEF4", fill_type="solid")

    for idx, col_letter in enumerate(["D", "E", "F", "G", "H"], start=4):
        cell = ws.cell(5, idx, f"=SUM({col_letter}4)")
        cell.font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_BLUE_HEX)
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.fill = PatternFill(start_color="FFF2CC" if col_letter == "D" else "E9EEF4", fill_type="solid")
        cell.border = thin_border
    ws.cell(5, 2).border = thin_border
    ws.cell(5, 3).border = thin_border

    # --- BẢNG TEST CASES CHI TIẾT ---
    # Dòng 7: Round Timeline Headers
    ws.row_dimensions[7].height = 28
    round_spans = [
        ("J7:M7", "ROUND 1 - FROM  [20/10/2026]   TO  [27/10/2026]"),
        ("N7:Q7", "ROUND 2 - FROM  [  /  /    ]   TO  [  /  /    ]"),
        ("R7:U7", "ROUND 3 - FROM  [  /  /    ]   TO  [  /  /    ]")
    ]
    fill_round_blue = PatternFill(start_color="1F4E79", fill_type="solid")
    for span, title in round_spans:
        ws.merge_cells(span)
        first_cell = ws[span.split(":")[0]]
        first_cell.value = title
        first_cell.font = Font(name=FONT_FAMILY, size=12, bold=True, color=WHITE)
        first_cell.alignment = Alignment(horizontal="center", vertical="center")
        style_range(ws, span, fill=fill_round_blue, border=create_header_border())

    # Dòng 8: Nhóm kết quả và Phản hồi ISC
    ws.row_dimensions[8].height = 30
    sub_headers = [
        ("J8:K8", "TEST RESULT\n(Đơn vị tham gia Test thông báo kết quả)", FPT_BLUE_HEX, WHITE),
        ("L8:M8", "ISC FEEDBACK\n(Đội phát triển phản hồi xử lý)", FPT_GREEN_HEX, WHITE),
        ("N8:O8", "TEST RESULT\n(Đơn vị tham gia Test thông báo kết quả)", FPT_BLUE_HEX, WHITE),
        ("P8:Q8", "ISC FEEDBACK\n(Đội phát triển phản hồi xử lý)", FPT_GREEN_HEX, WHITE),
        ("R8:S8", "TEST RESULT\n(Đơn vị tham gia Test thông báo kết quả)", FPT_BLUE_HEX, WHITE),
        ("T8:U8", "ISC FEEDBACK\n(Đội phát triển phản hồi xử lý)", FPT_GREEN_HEX, WHITE)
    ]
    for span, title, bg_color, txt_color in sub_headers:
        ws.merge_cells(span)
        first_cell = ws[span.split(":")[0]]
        first_cell.value = title
        first_cell.font = Font(name=FONT_FAMILY, size=11, bold=True, color=txt_color)
        first_cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        style_range(ws, span, fill=PatternFill(start_color=bg_color, fill_type="solid"), border=create_header_border())

    # Dòng 9: Header các cột nghiệp vụ
    ws.row_dimensions[9].height = 36
    ws.merge_cells("D9:F9")
    ws.merge_cells("G9:I9")

    cols_d9 = [
        (2, "NO."),
        (3, "MODULE\n(Màn hình/Chức năng)"),
        (4, "STEPS TO EXECUTE\n(Mô tả các bước thực hiện)"),
        (7, "EXPECTED RESULT\n(Kết quả mong đợi)"),
        (10, "STATUS"),
        (11, "DESCRIPTION"),
        (12, "ACTION"),
        (13, "NOTE"),
        (14, "STATUS"),
        (15, "MÔ TẢ LỖI"),
        (16, "ACTION"),
        (17, "NOTE"),
        (18, "STATUS"),
        (19, "MÔ TẢ LỖI"),
        (20, "ACTION"),
        (21, "NOTE")
    ]

    fill_col_blue = PatternFill(start_color=FPT_BLUE_HEX, fill_type="solid")
    fill_col_green = PatternFill(start_color=FPT_GREEN_HEX, fill_type="solid")

    for col_idx, label in cols_d9:
        cell = ws.cell(9, col_idx, label)
        cell.font = Font(name=FONT_FAMILY, size=11, bold=True, color=WHITE)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        # Nếu là cột thuộc ISC Feedback (Action/Note)
        if col_idx in (12, 13, 16, 17, 20, 21):
            cell.fill = fill_col_green
        else:
            cell.fill = fill_col_blue
        cell.border = create_header_border()

    # Áp dụng fill & border cho các ô bị merge D9:F9, G9:I9
    style_range(ws, "D9:F9", fill=fill_col_blue, border=create_header_border())
    style_range(ws, "G9:I9", fill=fill_col_blue, border=create_header_border())

    # Dòng 10: Dòng VÍ DỤ MẪU (VD)
    ws.row_dimensions[10].height = 65
    ws.merge_cells("D10:F10")
    ws.merge_cells("G10:I10")

    ws.cell(10, 2, "VD").alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(10, 2).font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_ORANGE_HEX)
    ws.cell(10, 2).fill = PatternFill(start_color="FFF3E0", fill_type="solid")

    ws.cell(10, 3, "Gửi và xác thực mã OTP").alignment = Alignment(vertical="center", wrap_text=True)
    ws.cell(10, 3).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_DARK)

    sample_steps = "1. Truy cập trang fpt.vn/nang-cap.\n2. Nhập số điện thoại hợp lệ (10 số, bắt đầu 03, 05, 07, 08, 09).\n3. Bấm 'Xác nhận'."
    ws.cell(10, 4, sample_steps).alignment = Alignment(vertical="top", wrap_text=True)
    ws.cell(10, 4).font = Font(name=FONT_FAMILY, size=10, color=TEXT_DARK)

    sample_expected = "1. Hệ thống gọi API gửi SMS OTP.\n2. Hiển thị popup nhập OTP với thời gian đếm ngược (05:00)."
    ws.cell(10, 7, sample_expected).alignment = Alignment(vertical="top", wrap_text=True)
    ws.cell(10, 7).font = Font(name=FONT_FAMILY, size=10, color=TEXT_DARK)

    ws.cell(10, 10, "PASSED").alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(10, 10).font = Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_PASSED)
    ws.cell(10, 10).fill = PatternFill(start_color=FILL_PASSED, fill_type="solid")

    ws.cell(10, 11, "OTP nhận đúng trong 5s, countdown hiển thị chuẩn").alignment = Alignment(vertical="center", wrap_text=True)
    ws.cell(10, 12, "DONE").alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(10, 12).font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_GREEN_HEX)
    ws.cell(10, 13, "Đã verify trên môi trường Staging").alignment = Alignment(vertical="center", wrap_text=True)

    for c in range(2, 22):
        ws.cell(10, c).border = thin_border
    style_range(ws, "D10:F10", border=thin_border)
    style_range(ws, "G10:I10", border=thin_border)

    # Dòng 11 - 44: Các dòng Test Case trống được format sẵn chuẩn chỉnh
    for idx, r in enumerate(range(11, 45), start=1):
        ws.row_dimensions[r].height = 45
        ws.merge_cells(f"D{r}:F{r}")
        ws.merge_cells(f"G{r}:I{r}")

        # Cột B: NO.
        cell_no = ws.cell(r, 2, f"{float(idx):.1f}")
        cell_no.alignment = Alignment(horizontal="center", vertical="center")
        cell_no.font = Font(name=FONT_FAMILY, size=11, bold=True, color=FPT_BLUE_HEX)
        
        # Zebra striping nền xám rất nhẹ cho dễ theo dõi
        row_fill = PatternFill(start_color=BG_LIGHT_GRAY if idx % 2 == 1 else WHITE, fill_type="solid")
        
        for c in range(2, 22):
            cell = ws.cell(r, c)
            cell.border = thin_border
            cell.fill = row_fill
            if c in (3, 4, 7, 11, 13, 15, 17, 19, 21):
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                cell.font = Font(name=FONT_FAMILY, size=10, color=TEXT_DARK)
            elif c in (10, 12, 14, 16, 18, 20):
                cell.alignment = Alignment(horizontal="center", vertical="center")
                cell.font = Font(name=FONT_FAMILY, size=11, bold=True)

        style_range(ws, f"D{r}:F{r}", border=thin_border, fill=row_fill)
        style_range(ws, f"G{r}:I{r}", border=thin_border, fill=row_fill)

    # --- DATA VALIDATION (DROPDOWNS) ---
    dv_status = DataValidation(type="list", formula1='"PASSED,FAILED,PENDING,N/A"', allow_blank=True)
    dv_status.error ='Vui lòng chọn trạng thái: PASSED, FAILED, PENDING, N/A'
    dv_status.errorTitle = 'Trạng thái không hợp lệ'
    ws.add_data_validation(dv_status)
    dv_status.add("J10:J50")
    dv_status.add("N10:N50")
    dv_status.add("R10:R50")

    dv_action = DataValidation(type="list", formula1='"DONE,DOING,CANCELLED,NEXT PLAN"', allow_blank=True)
    dv_action.error ='Vui lòng chọn hành động: DONE, DOING, CANCELLED, NEXT PLAN'
    dv_action.errorTitle = 'Hành động không hợp lệ'
    ws.add_data_validation(dv_action)
    dv_action.add("L10:L50")
    dv_action.add("P10:P50")
    dv_action.add("T10:T50")

    # --- CONDITIONAL FORMATTING (TỰ ĐỘNG HIGHLIGHT MÀU ĐẸP) ---
    rule_passed = CellIsRule(operator='equal', formula=['"PASSED"'], stopIfTrue=True,
                             fill=PatternFill(start_color=FILL_PASSED, end_color=FILL_PASSED, fill_type="solid"),
                             font=Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_PASSED))
    rule_failed = CellIsRule(operator='equal', formula=['"FAILED"'], stopIfTrue=True,
                             fill=PatternFill(start_color=FILL_FAILED, end_color=FILL_FAILED, fill_type="solid"),
                             font=Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_FAILED))
    rule_pending = CellIsRule(operator='equal', formula=['"PENDING"'], stopIfTrue=True,
                              fill=PatternFill(start_color=FILL_PENDING, end_color=FILL_PENDING, fill_type="solid"),
                              font=Font(name=FONT_FAMILY, size=11, bold=True, color=TEXT_PENDING))
    rule_na = CellIsRule(operator='equal', formula=['"N/A"'], stopIfTrue=True,
                         fill=PatternFill(start_color=FILL_NA, end_color=FILL_NA, fill_type="solid"),
                         font=Font(name=FONT_FAMILY, size=11, color=TEXT_NA))

    for col_let in ["J", "N", "R"]:
        rng = f"{col_let}11:{col_let}50"
        ws.conditional_formatting.add(rng, rule_passed)
        ws.conditional_formatting.add(rng, rule_failed)
        ws.conditional_formatting.add(rng, rule_pending)
        ws.conditional_formatting.add(rng, rule_na)

    rule_done = CellIsRule(operator='equal', formula=['"DONE"'], stopIfTrue=True,
                           fill=PatternFill(start_color="D1FAE5", fill_type="solid"),
                           font=Font(name=FONT_FAMILY, size=11, bold=True, color="047857"))
    rule_doing = CellIsRule(operator='equal', formula=['"DOING"'], stopIfTrue=True,
                            fill=PatternFill(start_color="FEF3C7", fill_type="solid"),
                            font=Font(name=FONT_FAMILY, size=11, bold=True, color="B45309"))
    rule_cancelled = CellIsRule(operator='equal', formula=['"CANCELLED"'], stopIfTrue=True,
                                fill=PatternFill(start_color="F1F5F9", fill_type="solid"),
                                font=Font(name=FONT_FAMILY, size=11, color="64748B"))

    for col_let in ["L", "P", "T"]:
        rng = f"{col_let}11:{col_let}50"
        ws.conditional_formatting.add(rng, rule_done)
        ws.conditional_formatting.add(rng, rule_doing)
        ws.conditional_formatting.add(rng, rule_cancelled)

def build_guideline_sheet(wb):
    ws = wb.create_sheet(title="Guideline")
    ws.views.sheetView[0].showGridLines = True

    # Cấu hình độ rộng cột
    ws.column_dimensions["A"].width = 5
    ws.column_dimensions["B"].width = 5
    ws.column_dimensions["C"].width = 110

    # Dòng 2: Tiêu đề Hướng dẫn
    ws.row_dimensions[2].height = 40
    ws["C2"] = "Hướng dẫn sử dụng Template UAT"
    ws["C2"].font = Font(name=FONT_FAMILY, size=22, bold=True, color=FPT_ORANGE_HEX)
    ws["C2"].alignment = Alignment(vertical="center")

    guidelines = [
        (4, "1. Phạm vi áp dụng", True, FPT_BLUE_HEX, 14),
        (5, "- Áp dụng cho các dự án mới/nâng cấp có thay đổi Impact từ Medium trở lên (Medium/High).", False, TEXT_DARK, 12),
        (6, "- Áp dụng cho PO, User UAT.", False, TEXT_DARK, 12),
        (8, "2. Cấu trúc file", True, FPT_BLUE_HEX, 14),
        (9, "- Cover: Thông tin chung Template.", False, TEXT_DARK, 12),
        (10, "- Summary: Tổng hợp kết quả và xác nhận UAT cuối cùng của PO.", False, TEXT_DARK, 12),
        (11, "- Report 1_Module: Mẫu UAT khi tổ chức theo Module/Chức năng.", False, TEXT_DARK, 12),
        (12, "- Report 2_Process: Mẫu UAT khi tổ chức theo Quy trình end-to-end.", False, TEXT_DARK, 12),
        (13, "  Thường áp dụng cho UAT theo luồng nghiệp vụ hoặc các dự án cần đáp ứng nhanh yêu cầu kinh doanh (biz demand), ad-hoc.", False, TEXT_MUTED, 11),
        (15, "3. Cách sử dụng", True, FPT_BLUE_HEX, 14),
        (16, "3.1 Thống nhất với PO về phạm vi và cách tổ chức UAT:", True, TEXT_DARK, 12),
        (17, "- Chọn 1 trong 2 dạng: theo Module (Report 1) hoặc theo Process (Report 2).", False, TEXT_DARK, 12),
        (19, "3.2 Điền thông tin chung tại sheet Summary.", True, TEXT_DARK, 12),
        (21, "3.3 Tại sheet Report được chọn:", True, TEXT_DARK, 12),
        (22, "- BA/PIC tạo Test Scenario/Test Case.", False, TEXT_DARK, 12),
        (23, "- User/PO thực hiện UAT, ghi kết quả (Pass/Fail), ghi chú và evidence (link hình, log...).", False, TEXT_DARK, 12),
        (25, "3.4 File của dự án - Sheet Report:", True, TEXT_DARK, 12),
        (26, "- Sau khi thống nhất chọn Report 1 hoặc Report 2, BA/PIC có thể tinh gọn Hide/Delete sheet Report không sử dụng.", False, TEXT_DARK, 12),
        (28, "3.5 Thiết kế UAT theo nghiệp vụ & hệ thống:", True, TEXT_DARK, 12),
        (29, "- Ưu tiên thiết kế case theo nghiệp vụ/ý nghĩa hệ thống, không chỉ theo màn hình đơn lẻ.", False, TEXT_DARK, 12),
        (30, "- Dự án nhiều hệ thống/nhóm chức năng: dùng 1 file UAT, BA/PIC có thể Duplicate sheet Report 1/Report 2 và đặt tên theo hệ thống/nhóm chức năng (VD: Report_CRM, Report_Billing...).", False, TEXT_DARK, 12),
        (31, "- Với cross system, mỗi nhóm phải có cả Happy case và Unhappy case (data sai, lỗi tích hợp…) để kiểm tra ràng buộc các hệ thống.", False, FPT_ORANGE_HEX, 12),
        (33, "- Trường hợp có nhiều PO theo hệ thống:", True, TEXT_DARK, 12),
        (34, "  + PO từng hệ thống xác nhận kết quả tại bảng “PO UAT Decision by System” trên Summary.", False, TEXT_DARK, 12),
        (35, "  + Business Owner/Lead PO cập nhật “Overall UAT Decision” cho toàn bộ phạm vi UAT.", False, TEXT_DARK, 12),
        (37, "4. Xác nhận & lưu trữ", True, FPT_BLUE_HEX, 14),
        (38, "4.1 Sau khi hoàn tất UAT:", True, TEXT_DARK, 12),
        (39, "- PO confirm kết quả UAT tại sheet Summary và các thông tin tại Sheet Report phải được update Latest Update (để mapping với thông tin PO confirm).", False, TEXT_DARK, 12),
        (40, "- PO confirm kết quả UAT & đính kèm link/file qua Email.", False, TEXT_DARK, 12),
        (42, "4.2 QA/PIC phụ trách:", True, TEXT_DARK, 12),
        (43, "- QA/PIC lưu trữ tài liệu vào Thư mục dự án.", False, TEXT_DARK, 12)
    ]

    for r, text, is_bold, color, size in guidelines:
        ws.row_dimensions[r].height = 24 if is_bold else 20
        cell = ws.cell(r, 3, text)
        cell.font = Font(name=FONT_FAMILY, size=size, bold=is_bold, color=color)
        cell.alignment = Alignment(vertical="center", wrap_text=True)

def generate_template(output_file):
    wb = openpyxl.Workbook()
    # Xoá sheet mặc định
    default_sheet = wb.active
    wb.remove(default_sheet)

    print("Building Sheet: Cover...")
    build_cover_sheet(wb)
    print("Building Sheet: Summary...")
    build_summary_sheet(wb)
    print("Building Sheet: Report...")
    build_report_sheet(wb)
    print("Building Sheet: Guideline...")
    build_guideline_sheet(wb)

    os.makedirs(os.path.dirname(os.path.abspath(output_file)), exist_ok=True)
    wb.save(output_file)
    print(f"✅ UAT Template generated successfully at: {output_file}")

if __name__ == "__main__":
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/templates/uat_template_fpt_standard.xlsx"
    generate_template(out_path)

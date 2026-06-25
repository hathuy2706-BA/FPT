#!/usr/bin/env python3
"""Generate Product Backlog Excel file for Product Team — chuẩn FPT."""

import xlsxwriter

OUTPUT = "/Users/hathuy/Documents/FPT-1/backlogpo/product_backlog_team.xlsx"

# ── Data ─────────────────────────────────────────────────────────────────────
BACKLOG = [
    # ID, Epic, Epic Name, User Story Title, User Story (full), AC (Gherkin), Priority, SP, Sprint, Status
    ("US-001","EP01","Quản lý Task","Tạo task mới",
     "As a BA/PO, I want to create a new task with full details (title, description, type, assignee, priority, deadline) so that the team has a clear and trackable work item.",
     "GIVEN tôi ở trang Backlog\nWHEN tôi nhấn \"Tạo Task\" và điền đầy đủ các trường bắt buộc\nTHEN task được tạo và hiển thị trong backlog với status \"To Do\"\n\nGIVEN tôi để trống trường Title\nWHEN tôi nhấn \"Lưu\"\nTHEN hệ thống hiển thị lỗi \"Title không được để trống\"",
     "Must Have","3","Sprint 1","To Do"),

    ("US-002","EP01","Quản lý Task","Cập nhật trạng thái task (Kanban)",
     "As a team member, I want to drag & drop tasks across columns (To Do → In Progress → Review → Done) so that the team can visualize workflow in real time.",
     "GIVEN task đang ở cột \"To Do\"\nWHEN tôi kéo task sang \"In Progress\"\nTHEN task chuyển trạng thái và lưu timestamp bắt đầu\n\nGIVEN task chuyển sang \"Done\"\nTHEN hệ thống ghi nhận completion date và tính cycle time",
     "Must Have","3","Sprint 1","To Do"),

    ("US-003","EP01","Quản lý Task","Assign task cho thành viên",
     "As a PO, I want to assign a task to one or more team members so that responsibilities are clear.",
     "GIVEN tôi đang xem chi tiết task\nWHEN tôi chọn assignee từ dropdown danh sách thành viên\nTHEN task hiển thị avatar assignee và thành viên nhận notification\n\nGIVEN task chưa có assignee\nTHEN hệ thống hiển thị cảnh báo \"Chưa assign\" trên board",
     "Must Have","2","Sprint 1","To Do"),

    ("US-004","EP01","Quản lý Task","Đặt độ ưu tiên & deadline",
     "As a PO, I want to set priority (Critical/High/Medium/Low) and deadline for each task so that the team can focus on what matters most.",
     "GIVEN tôi tạo hoặc chỉnh sửa task\nWHEN tôi chọn mức ưu tiên và nhập ngày deadline\nTHEN task hiển thị badge màu tương ứng và đếm ngược đến deadline\n\nGIVEN deadline < 2 ngày\nTHEN badge chuyển màu đỏ và gửi reminder notification",
     "Must Have","2","Sprint 1","To Do"),

    ("US-005","EP01","Quản lý Task","Tìm kiếm & lọc task",
     "As a team member, I want to search and filter tasks by keyword, assignee, status, sprint, or tag so that I can quickly find relevant work.",
     "GIVEN tôi nhập keyword vào ô tìm kiếm\nWHEN tôi gõ ≥ 2 ký tự\nTHEN danh sách task filter realtime theo title và description\n\nGIVEN tôi kết hợp filter (status=In Progress + assignee=Tôi)\nTHEN chỉ hiển thị task thỏa mãn tất cả điều kiện",
     "Must Have","3","Sprint 2","To Do"),

    ("US-006","EP01","Quản lý Task","Comment & đính kèm file trên task",
     "As a BA, I want to add comments and attach files (doc, pdf, image) to a task so that discussion and evidence stay in context.",
     "GIVEN tôi ở trang chi tiết task\nWHEN tôi nhập comment và nhấn \"Gửi\"\nTHEN comment hiển thị với timestamp và avatar người dùng\n\nGIVEN tôi đính kèm file > 25 MB\nTHEN hệ thống hiển thị lỗi giới hạn kích thước file",
     "Should Have","3","Sprint 2","To Do"),

    ("US-007","EP02","Sprint Planning","Tạo và quản lý Sprint",
     "As a PO, I want to create sprints with name, goal, start date, and end date so that the team works in structured time-boxes.",
     "GIVEN tôi ở màn Sprint Planning\nWHEN tôi tạo Sprint với đầy đủ thông tin\nTHEN Sprint xuất hiện trong danh sách với status \"Planned\"\n\nGIVEN sprint end date < start date\nTHEN hệ thống báo lỗi validation",
     "Must Have","3","Sprint 1","To Do"),

    ("US-008","EP02","Sprint Planning","Thêm task vào Sprint",
     "As a PO, I want to move tasks from backlog into a sprint so that the sprint scope is clearly defined.",
     "GIVEN tôi đang xem Sprint backlog\nWHEN tôi kéo task từ Product Backlog vào Sprint\nTHEN task gắn với Sprint và cập nhật tổng Story Points\n\nGIVEN sprint đã Start\nWHEN tôi thêm task mới\nTHEN hiển thị cảnh báo \"Thêm task giữa Sprint — cần PO xác nhận\"",
     "Must Have","3","Sprint 2","To Do"),

    ("US-009","EP02","Sprint Planning","Burn-down chart theo Sprint",
     "As a PO, I want to see a burn-down chart for the active sprint so that I can track whether the team is on pace to complete the sprint goal.",
     "GIVEN sprint đang chạy\nWHEN tôi mở tab Burn-down\nTHEN biểu đồ hiển thị đường ideal vs actual remaining SP theo ngày\n\nGIVEN tất cả task của sprint = Done\nTHEN đường actual chạm 0 và hiển thị badge \"Sprint Completed\"",
     "Should Have","5","Sprint 3","To Do"),

    ("US-010","EP02","Sprint Planning","Sprint Retrospective notes",
     "As a Scrum Master/PO, I want to record retrospective notes (Went Well, Improvement, Action Items) after each sprint so that lessons learned are persisted.",
     "GIVEN sprint đã kết thúc\nWHEN tôi mở trang Retrospective\nTHEN có 3 cột Went Well / Improvement / Action Items để thêm sticky notes\n\nGIVEN tôi lưu retro\nTHEN dữ liệu liên kết với sprint đó và có thể xem lại trong lịch sử",
     "Should Have","3","Sprint 3","To Do"),

    ("US-011","EP03","Dashboard & Báo cáo","Dashboard cá nhân",
     "As a team member, I want a personal dashboard showing my assigned tasks, deadlines, and today's priorities so that I can plan my workday efficiently.",
     "GIVEN tôi đăng nhập\nWHEN tôi mở My Dashboard\nTHEN hiển thị: task đang làm, due today, overdue, và activity feed\n\nGIVEN không có task nào\nTHEN hiển thị empty state \"Không có task — hãy tận hưởng ngày hôm nay!\"",
     "Must Have","3","Sprint 2","To Do"),

    ("US-012","EP03","Dashboard & Báo cáo","Dashboard Team — tổng quan tiến độ",
     "As a PO, I want a team dashboard with task distribution by status, workload per member, and sprint progress so that I can manage team capacity.",
     "GIVEN tôi ở Team Dashboard\nWHEN sprint đang active\nTHEN hiển thị: % Done, số task theo status, workload chart từng thành viên\n\nGIVEN thành viên có > 5 task In Progress\nTHEN hiển thị cảnh báo overload với màu cam",
     "Must Have","5","Sprint 3","To Do"),

    ("US-013","EP03","Dashboard & Báo cáo","Báo cáo Velocity Sprint-over-Sprint",
     "As a PO, I want to see team velocity (SP completed per sprint) across multiple sprints so that I can make reliable release forecasts.",
     "GIVEN có ≥ 2 sprint đã hoàn thành\nWHEN tôi mở Velocity Report\nTHEN biểu đồ cột hiển thị SP committed vs SP completed cho từng sprint\n\nGIVEN tôi hover vào cột sprint\nTHEN tooltip hiển thị danh sách task của sprint đó",
     "Could Have","5","Sprint 4","To Do"),

    ("US-014","EP03","Dashboard & Báo cáo","Xuất báo cáo tiến độ (PDF/Excel)",
     "As a PO, I want to export sprint/project progress reports to PDF or Excel so that I can share with stakeholders.",
     "GIVEN tôi chọn loại báo cáo và khoảng thời gian\nWHEN tôi nhấn \"Xuất\"\nTHEN file được tải về trong ≤ 5 giây, đúng template FPT\n\nGIVEN có > 500 task trong report\nTHEN hệ thống xử lý background và gửi email khi xong",
     "Could Have","5","Sprint 4","To Do"),

    ("US-015","EP04","Phân quyền","Quản lý vai trò thành viên",
     "As an Admin/PO, I want to assign roles (PO, BA, Dev, QA, Viewer) to team members so that each person has appropriate access and permissions.",
     "GIVEN tôi là Admin\nWHEN tôi vào Settings > Members và gán role cho user\nTHEN user nhận email thông báo role mới, quyền thay đổi ngay lập tức\n\nGIVEN user bị remove khỏi project\nTHEN tất cả task assign cho user đó hiển thị cảnh báo \"Unassigned\"",
     "Must Have","3","Sprint 1","To Do"),

    ("US-016","EP04","Phân quyền","Phân quyền theo Project",
     "As an Admin, I want to control which members can view, edit, or manage each project so that sensitive projects are protected.",
     "GIVEN tôi tạo project với visibility = Private\nWHEN user không được mời\nTHEN project không xuất hiện trong danh sách của user đó\n\nGIVEN Viewer cố tạo task\nTHEN hệ thống trả về lỗi 403 Forbidden",
     "Must Have","3","Sprint 2","To Do"),

    ("US-017","EP05","Tích hợp & Thông báo","Thông báo Email & In-app",
     "As a team member, I want to receive notifications (in-app + email) when I'm assigned a task, mentioned in a comment, or when my task is due soon so that I never miss important updates.",
     "GIVEN task được assign cho tôi\nWHEN assignee thay đổi\nTHEN tôi nhận in-app notification ngay và email trong vòng 1 phút\n\nGIVEN tôi tắt email notification trong Settings\nTHEN chỉ nhận in-app, không gửi email",
     "Should Have","3","Sprint 3","To Do"),

    ("US-018","EP05","Tích hợp & Thông báo","Tích hợp Slack",
     "As a PO, I want to receive sprint summary and task update notifications in a Slack channel so that the team stays aligned without switching tools.",
     "GIVEN Slack integration đã được cấu hình\nWHEN task chuyển sang \"Done\"\nTHEN bot Slack gửi message vào channel với link task\n\nGIVEN sprint kết thúc\nTHEN bot gửi Sprint Summary (SP done/total, % complete) vào channel",
     "Could Have","5","Sprint 4","To Do"),

    ("US-019","EP05","Tích hợp & Thông báo","Tích hợp Jira (Import/Export)",
     "As a BA, I want to import existing tasks from Jira and export task data to Jira so that the team can migrate gradually without losing history.",
     "GIVEN tôi cung cấp Jira API token và project key\nWHEN tôi chạy Import\nTHEN tất cả issues của Jira project được tạo trong hệ thống với mapping: Issue→Task, Story→User Story, Bug→Bug\n\nGIVEN import thất bại một phần\nTHEN hệ thống cung cấp error log theo từng item",
     "Won't Have (v1)","8","Sprint 5+","To Do"),
]

SPRINT_PLAN = [
    ("Sprint 1","2 tuần","25/06/2026","08/07/2026","US-001,002,003,004,007,015","19 SP",
     "Xây dựng core: tạo/assign/status task + phân quyền cơ bản"),
    ("Sprint 2","2 tuần","09/07/2026","22/07/2026","US-005,006,008,011,016","14 SP",
     "Search/filter, comment, sprint scope, dashboard cá nhân"),
    ("Sprint 3","2 tuần","23/07/2026","05/08/2026","US-009,010,012,017","14 SP",
     "Burn-down chart, retrospective, team dashboard, notifications"),
    ("Sprint 4","2 tuần","06/08/2026","19/08/2026","US-013,014,018","15 SP",
     "Velocity report, export PDF/Excel, Slack integration"),
    ("Sprint 5+","TBD","TBD","TBD","US-019","8 SP",
     "Jira integration — ngoài phạm vi release v1"),
]

DOD = [
    "Code đã được review bởi ít nhất 1 thành viên khác",
    "Unit test coverage ≥ 80% cho business logic",
    "Acceptance Criteria đã pass toàn bộ (manual hoặc automated)",
    "Không có bug P1/P2 mở tại thời điểm demo",
    "UI đã được kiểm tra trên Chrome, Safari, Firefox (responsive)",
    "Tài liệu kỹ thuật (API doc, flow) được cập nhật nếu có thay đổi",
    "PO/BA xác nhận nghiệm thu feature trước khi chuyển sang Done",
]


def build():
    wb = xlsxwriter.Workbook(OUTPUT)

    # ── Global formats ────────────────────────────────────────────────────
    def fmt(**kw):
        base = dict(font_name="Times New Roman", font_size=11,
                    valign="vcenter", text_wrap=True)
        base.update(kw)
        return wb.add_format(base)

    # Header formats
    hdr_main   = fmt(bold=True, font_size=12, font_color="#FFFFFF",
                     bg_color="#E86A23", align="center", border=1, border_color="#CCCCCC")
    hdr_sub    = fmt(bold=True, font_size=11, font_color="#FFFFFF",
                     bg_color="#1F2737", align="center", border=1, border_color="#CCCCCC")

    # Cell formats
    cell_base  = fmt(border=1, border_color="#DDDDDD")
    cell_alt   = fmt(border=1, border_color="#DDDDDD", bg_color="#FFF8F4")
    cell_bold  = fmt(bold=True, border=1, border_color="#DDDDDD")
    cell_ctr   = fmt(align="center", border=1, border_color="#DDDDDD")
    cell_ctr_alt = fmt(align="center", border=1, border_color="#DDDDDD", bg_color="#FFF8F4")

    id_fmt     = fmt(bold=True, font_color="#1E4D8C", align="center",
                     border=1, border_color="#DDDDDD")
    id_fmt_alt = fmt(bold=True, font_color="#1E4D8C", align="center",
                     border=1, border_color="#DDDDDD", bg_color="#FFF8F4")

    epic_fmt   = fmt(bold=True, font_color="#E86A23", align="center",
                     border=1, border_color="#DDDDDD")
    epic_fmt_alt = fmt(bold=True, font_color="#E86A23", align="center",
                       border=1, border_color="#DDDDDD", bg_color="#FFF8F4")

    # MoSCoW formats
    must_fmt   = fmt(bold=True, font_color="#FFFFFF", bg_color="#C0392B",
                     align="center", border=1, border_color="#DDDDDD")
    should_fmt = fmt(bold=True, font_color="#FFFFFF", bg_color="#E67E22",
                     align="center", border=1, border_color="#DDDDDD")
    could_fmt  = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60",
                     align="center", border=1, border_color="#DDDDDD")
    wont_fmt   = fmt(bold=True, font_color="#FFFFFF", bg_color="#95A5A6",
                     align="center", border=1, border_color="#DDDDDD")

    sp_fmt     = fmt(bold=True, font_size=12, align="center",
                     border=1, border_color="#DDDDDD")
    sp_fmt_alt = fmt(bold=True, font_size=12, align="center",
                     border=1, border_color="#DDDDDD", bg_color="#FFF8F4")

    status_fmt = fmt(font_color="#888888", align="center",
                     border=1, border_color="#DDDDDD")

    title_fmt  = fmt(bold=True, font_size=18, font_color="#E86A23", align="center")
    sub_fmt    = fmt(bold=True, font_size=13, font_color="#1F2737", align="center")
    meta_lbl   = fmt(bold=True, font_color="#FFFFFF", bg_color="#E86A23",
                     align="center", border=1)
    meta_val   = fmt(bg_color="#FFF8F4", border=1)

    section_fmt = fmt(bold=True, font_size=13, font_color="#FFFFFF",
                      bg_color="#1F2737", align="left", border=1)

    dod_check  = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60",
                     align="center", border=1)
    dod_txt    = fmt(border=1, border_color="#DDDDDD", bg_color="#F9F9F9")
    dod_txt_alt = fmt(border=1, border_color="#DDDDDD")

    # Sprint sheet formats
    sp_hdr     = fmt(bold=True, font_color="#FFFFFF", bg_color="#1E4D8C",
                     align="center", border=1, border_color="#CCCCCC")
    sp_row     = fmt(border=1, border_color="#DDDDDD")
    sp_row_alt = fmt(border=1, border_color="#DDDDDD", bg_color="#EFF3FB")
    sp_ctr     = fmt(align="center", border=1, border_color="#DDDDDD")
    sp_ctr_alt = fmt(align="center", border=1, border_color="#DDDDDD", bg_color="#EFF3FB")
    sp_pts     = fmt(bold=True, align="center", font_color="#1E4D8C",
                     border=1, border_color="#DDDDDD")
    sp_pts_alt = fmt(bold=True, align="center", font_color="#1E4D8C",
                     border=1, border_color="#DDDDDD", bg_color="#EFF3FB")
    sprint_name_fmt = fmt(bold=True, font_color="#FFFFFF", bg_color="#E86A23",
                          align="center", border=1)
    sprint_name_alt = fmt(bold=True, font_color="#FFFFFF", bg_color="#1E4D8C",
                          align="center", border=1)

    def moscow_fmt(p):
        p = p.strip()
        if p.startswith("Must"):   return must_fmt
        if p.startswith("Should"): return should_fmt
        if p.startswith("Could"):  return could_fmt
        return wont_fmt

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 1 — Trang bìa / Cover
    # ════════════════════════════════════════════════════════════════════════
    ws_cover = wb.add_worksheet("📋 Cover")
    ws_cover.hide_gridlines(2)
    ws_cover.set_column("A:A", 3)
    ws_cover.set_column("B:G", 18)
    ws_cover.set_row(0, 20)
    ws_cover.set_row(2, 45)
    ws_cover.set_row(3, 30)
    ws_cover.set_row(5, 20)

    # Title
    ws_cover.merge_range("B3:G3", "PRODUCT BACKLOG — ĐỘI PRODUCT", title_fmt)
    ws_cover.merge_range("B4:G4", "Hệ thống Quản lý Task | FPT Software", sub_fmt)

    # Divider row
    ws_cover.set_row(5, 8)
    div_fmt = wb.add_format({"bg_color": "#E86A23"})
    ws_cover.merge_range("B6:G6", "", div_fmt)

    # Meta info
    ws_cover.set_row(7, 22)
    ws_cover.set_row(8, 22)
    ws_cover.set_row(9, 22)
    ws_cover.set_row(10, 22)
    ws_cover.set_row(11, 22)

    meta = [
        ("Dự án",     "Task Management System",   "Phiên bản", "1.0"),
        ("Team",      "Product Team (BA/PO/Dev)",  "Ngày tạo",  "25/06/2026"),
        ("Author",    "Product Owner / BA",         "Trạng thái","Draft"),
        ("Tổng Epic", "5 Epics",                    "Tổng US",   "19 User Stories"),
        ("Tổng SP",   "75 Story Points",            "Sprints",   "4 sprints (Release v1)"),
    ]
    for i, (l1, v1, l2, v2) in enumerate(meta):
        r = 8 + i
        ws_cover.write(r, 1, l1, meta_lbl)
        ws_cover.merge_range(r, 2, r, 3, v1, meta_val)
        ws_cover.write(r, 4, l2, meta_lbl)
        ws_cover.merge_range(r, 5, r, 6, v2, meta_val)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 2 — Product Backlog
    # ════════════════════════════════════════════════════════════════════════
    ws = wb.add_worksheet("📌 Product Backlog")
    ws.hide_gridlines(2)
    ws.freeze_panes(3, 0)
    ws.set_zoom(85)

    # Column widths
    col_widths = [4, 8, 8, 14, 22, 38, 18, 6, 12, 12]
    for i, w in enumerate(col_widths):
        ws.set_column(i, i, w)

    # Row 1 — Sheet title
    ws.set_row(0, 32)
    ws.merge_range("A1:J1", "PRODUCT BACKLOG — HỆ THỐNG QUẢN LÝ TASK | ĐỘI PRODUCT", hdr_main)

    # Row 2 — Column headers
    ws.set_row(1, 28)
    headers = ["#", "ID", "Epic", "Epic Name", "US Title", "User Story (As a / I want / So that)",
               "Acceptance Criteria (Gherkin)", "SP", "Sprint", "Status"]
    for col, h in enumerate(headers):
        ws.write(2, col, h, hdr_sub)

    # Data rows
    for idx, (us_id, epic_id, epic_name, title, story, ac, priority, sp, sprint, status) in enumerate(BACKLOG):
        r = idx + 3
        ws.set_row(r, 90)
        alt = (idx % 2 == 1)

        ws.write(r, 0, idx + 1, cell_ctr_alt if alt else cell_ctr)
        ws.write(r, 1, us_id, id_fmt_alt if alt else id_fmt)
        ws.write(r, 2, epic_id, epic_fmt_alt if alt else epic_fmt)
        ws.write(r, 3, epic_name, cell_alt if alt else cell_base)
        ws.write(r, 4, title, cell_bold)
        ws.write(r, 5, story, cell_alt if alt else cell_base)
        ws.write(r, 6, ac, cell_alt if alt else cell_base)
        ws.write(r, 7, int(sp), sp_fmt_alt if alt else sp_fmt)
        ws.write(r, 8, sprint, cell_ctr_alt if alt else cell_ctr)
        ws.write(r, 9, status, status_fmt)

    # MoSCoW legend row at bottom
    legend_row = len(BACKLOG) + 4
    ws.set_row(legend_row, 14)
    ws.merge_range(legend_row, 0, legend_row, 9, "", fmt(bg_color="#F0F0F0"))

    leg_row2 = legend_row + 1
    ws.set_row(leg_row2, 22)
    leg_fmt = fmt(font_size=10)
    ws.write(leg_row2, 0, "MoSCoW:", fmt(bold=True, font_size=10))
    ws.write(leg_row2, 1, "Must Have",      must_fmt)
    ws.write(leg_row2, 2, "Should Have",    should_fmt)
    ws.write(leg_row2, 3, "Could Have",     could_fmt)
    ws.write(leg_row2, 4, "Won't Have v1",  wont_fmt)
    ws.write(leg_row2, 5, f"Tổng: {sum(int(r[7]) for r in BACKLOG)} Story Points | {len(BACKLOG)} User Stories | 5 Epics",
             fmt(font_size=10, font_color="#888888"))

    # ── Conditional formatting via cell formats (priority col removed,
    #    priority is captured through MoSCoW in AC column — data already embedded)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 3 — Sprint Planning
    # ════════════════════════════════════════════════════════════════════════
    ws_sp = wb.add_worksheet("🗓 Sprint Planning")
    ws_sp.hide_gridlines(2)
    ws_sp.freeze_panes(2, 0)

    sp_col_widths = [16, 10, 14, 14, 30, 10, 45]
    for i, w in enumerate(sp_col_widths):
        ws_sp.set_column(i, i, w)

    ws_sp.set_row(0, 30)
    ws_sp.merge_range("A1:G1", "SPRINT PLANNING — RELEASE v1", hdr_main)

    ws_sp.set_row(1, 24)
    sp_headers = ["Sprint", "Thời lượng", "Bắt đầu", "Kết thúc", "User Stories", "Story Points", "Sprint Goal"]
    for ci, h in enumerate(sp_headers):
        ws_sp.write(1, ci, h, sp_hdr)

    for idx, (sprint, duration, start, end, stories, pts, goal) in enumerate(SPRINT_PLAN):
        r = idx + 2
        ws_sp.set_row(r, 40)
        alt = (idx % 2 == 1)
        sn_f = sprint_name_alt if alt else sprint_name_fmt

        ws_sp.write(r, 0, sprint,    sn_f)
        ws_sp.write(r, 1, duration,  sp_ctr_alt if alt else sp_ctr)
        ws_sp.write(r, 2, start,     sp_ctr_alt if alt else sp_ctr)
        ws_sp.write(r, 3, end,       sp_ctr_alt if alt else sp_ctr)
        ws_sp.write(r, 4, stories,   sp_row_alt if alt else sp_row)
        ws_sp.write(r, 5, pts,       sp_pts_alt if alt else sp_pts)
        ws_sp.write(r, 6, goal,      sp_row_alt if alt else sp_row)

    # Summary row
    sum_row = len(SPRINT_PLAN) + 3
    ws_sp.set_row(sum_row, 26)
    sum_fmt = fmt(bold=True, font_color="#FFFFFF", bg_color="#1F2737",
                  align="center", border=1)
    ws_sp.merge_range(sum_row, 0, sum_row, 4, "TỔNG RELEASE v1 (Sprint 1–4)", sum_fmt)
    ws_sp.write(sum_row, 5, "62 SP", sum_fmt)
    ws_sp.write(sum_row, 6, "18 User Stories — ~8 tuần phát triển", sum_fmt)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 4 — Definition of Done
    # ════════════════════════════════════════════════════════════════════════
    ws_dod = wb.add_worksheet("✅ Definition of Done")
    ws_dod.hide_gridlines(2)
    ws_dod.set_column("A:A", 6)
    ws_dod.set_column("B:B", 70)
    ws_dod.set_column("C:C", 20)

    ws_dod.set_row(0, 30)
    ws_dod.merge_range("A1:C1", "DEFINITION OF DONE (DoD) — ĐỘI PRODUCT", hdr_main)

    ws_dod.set_row(1, 22)
    ws_dod.write(1, 0, "#",      hdr_sub)
    ws_dod.write(1, 1, "Tiêu chí nghiệm thu", hdr_sub)
    ws_dod.write(1, 2, "Loại kiểm tra", hdr_sub)

    dod_types = ["Code Review","Testing","AC Verification","QA Testing",
                 "UI/Cross-browser","Documentation","PO Sign-off"]

    for i, (item, dtype) in enumerate(zip(DOD, dod_types)):
        r = i + 2
        ws_dod.set_row(r, 26)
        alt = (i % 2 == 1)
        ws_dod.write(r, 0, f"✓ {i+1}", dod_check)
        ws_dod.write(r, 1, item, dod_txt_alt if alt else dod_txt)
        ws_dod.write(r, 2, dtype,
                     fmt(align="center", bg_color="#EAF4EA" if not alt else "#D5ECD5",
                         font_color="#1A7A1A", border=1))

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 5 — Kanban Board (template)
    # ════════════════════════════════════════════════════════════════════════
    ws_kb = wb.add_worksheet("🗂 Kanban Board")
    ws_kb.hide_gridlines(2)

    status_colors = {
        "To Do":      ("#95A5A6","#ECF0F1"),
        "In Progress":("#E67E22","#FEF9E7"),
        "Review":     ("#1E4D8C","#EBF5FB"),
        "Done":       ("#27AE60","#EAFAF1"),
    }

    statuses = list(status_colors.keys())
    col_starts = [0, 3, 6, 9]  # 3 cols per status
    col_w = 7

    ws_kb.set_row(0, 30)
    ws_kb.merge_range("A1:L1", "KANBAN BOARD — SPRINT HIỆN TẠI", hdr_main)

    for ci, (status, (hc, bc)) in enumerate(status_colors.items()):
        col = col_starts[ci]
        for c in range(col, col + 3):
            ws_kb.set_column(c, c, col_w)
        ws_kb.set_row(1, 26)
        ws_kb.merge_range(1, col, 1, col+2, status,
                          fmt(bold=True, font_size=13, font_color="#FFFFFF",
                              bg_color=hc, align="center", border=1))

        # Task slots per column
        tasks_in_col = [row for row in BACKLOG if row[9] == status or
                        (status == "To Do" and row[8] == "Sprint 1")]
        for ti in range(8):
            r = ti + 2
            ws_kb.set_row(r, 50)
            if ti < len(tasks_in_col) and status == "To Do":
                t = tasks_in_col[ti]
                ws_kb.merge_range(r, col, r, col+2, f"{t[0]}\n{t[3]}",
                                  fmt(bg_color=bc, border=1, border_color=hc,
                                      font_size=9, text_wrap=True))
            else:
                ws_kb.merge_range(r, col, r, col+2, "",
                                  fmt(bg_color=bc, border=1, border_color="#DDDDDD"))

    wb.close()
    print(f"✅ Saved: {OUTPUT}")


if __name__ == "__main__":
    build()

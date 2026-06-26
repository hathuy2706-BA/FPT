#!/usr/bin/env python3
"""Generate Product Backlog Excel — chuẩn FPT.
   Bao gồm auto-formula + import task vận hành từ Backlog FPTvn & Roadmap 18.5."""

import xlsxwriter

OUTPUT = "/Users/hathuy/Documents/FPT-1/backlogpo/product_backlog_team.xlsx"

# ── Dữ liệu vận hành import từ Google Sheets ─────────────────────────────────
# Columns: ID, Nguồn, Tên Task, Đầu mục/Mô tả, Sản phẩm, URL, Timeline, Ưu tiên, PIC Ecom, PIC Thực hiện, Trạng thái, Ghi chú
OPS = [
    # ── Backlog FPTvn (18 tasks, loại trừ Done) ─────────────────────────────
    ("OP-001","Backlog FPTvn","Hiển thị giá cloud camera",
     "Không chia giá cloud theo mắt camera → Hiển thị giá buffet cloud 50.000đ/tháng. Cho khách chọn gói cloud theo kỳ.",
     "Camera","https://fpt.vn/shop/camera/payment","15/4","High","","","To Do",
     "Nhờ Hà check với chị Linh"),
    ("OP-002","Backlog FPTvn","Trang thanh toán Camera — gói cloud 3D buffet",
     "Bỏ 'x5' trên gói cloud 3D buffet 6 tháng. Khi KH chọn tự lắp đặt → không hiển thị phí lắp.",
     "Camera","https://fpt.vn/shop/camera/payment","15/4","High","ThuyTT104","","In Progress",
     "Đang làm việc với chính sách"),
    ("OP-003","Backlog FPTvn","Update page local theo UI mới",
     "Local pages và goi-dich-vu đang là source cũ → không linh hoạt thêm/chỉnh sửa section. Cần chuẩn hoá theo UI 2.0.",
     "Internet","https://fpt.vn/lap-internet-wifi-hcm","24/4","High","Anhtd55","","To Do",
     "Local: add section rồi; Breadcrumbs chưa; Heading 1 chưa"),
    ("OP-004","Backlog FPTvn","Luồng nâng cấp 5 dịch vụ",
     "Nâng cấp VVIP, Camera, AP, băng thông, wifi6 bổ sung. Mapping chính sách nâng cấp.",
     "Internet","/nang-cap","","High","LongNH156","","In Progress",""),
    ("OP-005","Backlog FPTvn","LDP FCM",
     "Landing page FCM — 22/5 golive 2 LDP.",
     "Internet","","","Medium","LongNH156","","In Progress",
     "22/5 là golive 2 LDP"),
    ("OP-006","Backlog FPTvn","CMS Tổng đài wifi — 5 mẫu LDP",
     "Thiết kế & cấu hình 5 mẫu LDP trên CMS cho tổng đài wifi.",
     "","","","High","DoanhCN","","",""),
    ("OP-007","Backlog FPTvn","LDP nâng cấp — bổ sung luồng giao hàng Camera",
     "Bổ sung luồng giao hàng cho Camera trên LDP nâng cấp.",
     "","","26/5","High","ThuyTT104","","In Progress",""),
    ("OP-008","Backlog FPTvn","LDP FCitizen",
     "LDP dành riêng cho FPTers. Chờ FTQ phản hồi quy trình bán gói.",
     "","","","High","SonLN11","","To Do",
     "Chờ FTQ phản hồi quy trình bán gói dành riêng cho FPTers"),
    ("OP-009","Backlog FPTvn","Exit-intent popup trang Camera",
     "Trigger desktop: mouse move back vào logo/breadcrumb/nav. Trigger mobile: scroll up nhanh.",
     "Camera","/camera\n/camera/*","06/08/2026","High","SonLN11","","",""),
    ("OP-010","Backlog FPTvn","API Giá Vàng & Điểm thi Đại học (Always-on)",
     "Tích hợp API giá vàng SJC/9999 realtime. Widget hiển thị giá. Tích hợp API điểm thi ĐH.",
     "Internet","","06/06/2026","Low","SonLN11","","",
     "Không ưu tiên giai đoạn này"),
    ("OP-011","Backlog FPTvn","Trang Author Profile Chuyên gia Camera",
     "URL: /tac-gia/chuyen-gia-ky-thuat. Hiển thị 3-5 expert profile: ảnh thực, tên, chức vụ, chứng chỉ.",
     "Camera","/tac-gia/chuyen-gia-ky-thuat","19/06","Medium","SonLN11","","",""),
    ("OP-012","Backlog FPTvn","LDP Ngoại Hạng Anh (NHA)",
     "LP tổng hợp: Kết quả trận đấu, Bảng xếp hạng cập nhật tự động qua API. 2 layout intent kết quả NHA.",
     "Internet/SA","https://fpt.vn/ngoai-hang-anh/lich-thi-dau","20/06/2026","Low","SonLN11","","",
     "Không ưu tiên giai đoạn này"),
    ("OP-013","Backlog FPTvn","Video Hub (FPT Play)",
     "Block video tự động lấy nguồn từ YouTube FPT Play (Recap/Highlight). Schema VideoObject, lazy-load, responsive.",
     "Internet/SA","https://fpt.vn/ngoai-hang-anh","27/06/2026","Medium","SonLN11","","",""),
    ("OP-014","Backlog FPTvn","Structured Data Schema cho nội dung SEO",
     "Triển khai JSON-LD: Article, BreadcrumbList, FAQPage, Product. Tool kiểm tra: Google Rich Results.",
     "Internet","","03/06/2026","High","SonLN11","","",""),
    ("OP-015","Backlog FPTvn","Core Web Vitals — cải thiện LCP/CLS",
     "LCP < 2.5s, CLS < 0.1. Tối ưu images (WebP/AVIF), preload critical CSS, giảm layout shift.",
     "Internet","","03/06/2026","High","SonLN11","","",""),
    ("OP-016","Backlog FPTvn","Luồng mua mới Camera — bổ sung giỏ hàng",
     "BA đánh giá xây dựng thêm luồng hướng dẫn. Không mua cùng lúc 1 cam ngoài trời + 1 cam trong nhà → bổ sung giỏ hàng.",
     "Camera","","24/06/2026","High","","","",
     "Bổ sung thêm luồng giỏ hàng — đã bsung vào Backlog"),
    ("OP-017","Backlog FPTvn","Luồng Mua mới Camera — đứt gãy tại bước Thanh toán",
     "Thao tác mua mới Camera Play bị đứt gãy tại bước Thanh toán. Cần fix flow.",
     "Camera","","24/06/2026","High","","","",""),
    ("OP-018","Backlog FPTvn","Luồng Mua mới Camera — fix combo",
     "Không mua cùng lúc 1 cam ngoài trời và 1 cam trong nhà → bổ sung giỏ hàng combo.",
     "Camera","","24/06/2026","High","","","",""),
    # ── Roadmap 18.5 (14 tasks, loại trừ Done) ───────────────────────────────
    ("RM-001","Roadmap 18.5","Luồng bán Camera chỉ giao hàng: Sàn TMĐT",
     "Luồng bán Camera chỉ giao hàng trên Sàn TMĐT. Chưa có chỗ nâng cấp Camera combo trên HD net only.",
     "Camera","Sàn TMĐT","20/6","High","Anh LongNH158","","In Progress",
     "Chưa có chỗ nâng cấp camera combo trên HD net only"),
    ("RM-002","Roadmap 18.5","LDP FCitizen — UI/UX & chính sách gói bán",
     "Thiết kế UI/UX LDP FCitizen và cập nhật chính sách/gói bán & verify thông tin theo chính sách tháng.",
     "Internet","https://fcitizen.fpt.vn/ → fpt.vn/fcitizen","06/03/2026","Medium",
     "Anh LongNH158","Anh Thuận","To Do","Rồi sẽ bán thế nào? hay chỉ sửa UI LDP?"),
    ("RM-003","Roadmap 18.5","Luồng nâng cấp 5 Dịch vụ - FPT.vn",
     "Thiết kế UI/UX, map chính sách nâng cấp 5 dịch vụ trên website FPT.vn.",
     "Nâng cấp/ bán thêm","FPT.vn","30/6","Medium",
     "Anh LongNH158","Anh ManhDT3","",""),
    ("RM-004","Roadmap 18.5","Hub vinh danh Giới thiệu bạn bè trên App HiFPT",
     "Tạo mục vinh danh KH Giới thiệu bạn bè: Level Cơ bản, Bạc, Vàng, Kim cương.",
     "Giới thiệu bạn bè","HiFPT","30/6","Medium",
     "LinhTT119","Chị Tuyết Vũ HiFPT","",""),
    ("RM-005","Roadmap 18.5","LDP Giới thiệu bạn bè — Người được giới thiệu",
     "LDP điều hướng KH được giới thiệu vào mua toàn bộ sản phẩm FPT qua chương trình GTBB.",
     "Giới thiệu bạn bè","FPT.vn","30/7","Medium",
     "Anh LongNH158","Anh Thuận & Anh Tài","",""),
    ("RM-006","Roadmap 18.5","Tích hợp Auto Pay trên website FPT.vn",
     "Tích hợp luồng tự động lưu thẻ và thanh toán định kỳ cho KH mua Dịch vụ trên website FPT.vn.",
     "Thanh toán","FPT.vn","30/6","Medium",
     "Anh LongNH158","Chị Tuyết Vũ HiFPT","","Cần làm rõ kịch bản thanh toán auto pay"),
    ("RM-007","Roadmap 18.5","Gửi E-Card khi mua gói SA Play trên FPT.vn & HiFPT",
     "Khi KH mua gói SA Play, lựa chọn hình thức 'KH nhận mã và tự kích hoạt' → gửi E-Card cho bạn bè.",
     "SA Play","FPT.vn & HiFPT","30/6","Medium",
     "LinhTT119","","","ISC đánh dấu KH đi theo luồng nhận mã; FPL trả thông tin qua ZNS"),
    ("RM-008","Roadmap 18.5","Landing Page Camera GenZ",
     "Thiết kế UI/UX LDP Camera GenZ. Mapping & config gói bán & chính sách.",
     "Camera","FPT.vn & HiFPT","30/6","High",
     "Anh LongNH158","","","Đánh giá lại mức độ ưu tiên → owner?"),
    ("RM-009","Roadmap 18.5","Luồng Recall",
     "Kênh bán: FPT.vn & HiFPT. Sản phẩm: Internet Only, Combo Internet+Phim, Camera.",
     "","FPT.vn & HiFPT","","","LinhTT119","","",""),
    ("RM-010","Roadmap 18.5","Luồng Autocall — tích hợp ZNS",
     "Tích hợp ZNS cho Autocall tệp KH hiện hữu — Nâng cấp/bán thêm dịch vụ.",
     "","","","High","Anh LongNH158","","",""),
    ("RM-011","Roadmap 18.5","Cross-sell FPTPlay.vn",
     "Xây dựng luồng cross-sell từ FPT.vn sang FPTPlay.vn.",
     "","","","High","","","",""),
    ("RM-012","Roadmap 18.5","Self-Service Cam trên sàn TMĐT",
     "Triển khai Self-Service Camera trên các sàn TMĐT (Shopee, Lazada, Tiki).",
     "","","","High","","","",""),
    ("RM-013","Roadmap 18.5","Chính sách GTBB tặng thiết bị Cam & Cloud",
     "Áp dụng chính sách Giới Thiệu Bạn Bè tặng kèm thiết bị Camera và gói Cloud.",
     "","","","High","","","",""),
    ("RM-014","Roadmap 18.5","(Task chưa đặt tên — cần bổ sung)",
     "Task chưa có tên và mô tả. Cần PO xác nhận.",
     "","","","","","","",""),
]

# ── Product Backlog gốc ───────────────────────────────────────────────────────
BACKLOG = [
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
    ("Sprint 1","2 tuần","25/06/2026","08/07/2026","US-001,002,003,004,007,015","19 SP","Xây dựng core: tạo/assign/status task + phân quyền cơ bản"),
    ("Sprint 2","2 tuần","09/07/2026","22/07/2026","US-005,006,008,011,016","14 SP","Search/filter, comment, sprint scope, dashboard cá nhân"),
    ("Sprint 3","2 tuần","23/07/2026","05/08/2026","US-009,010,012,017","14 SP","Burn-down chart, retrospective, team dashboard, notifications"),
    ("Sprint 4","2 tuần","06/08/2026","19/08/2026","US-013,014,018","15 SP","Velocity report, export PDF/Excel, Slack integration"),
    ("Sprint 5+","TBD","TBD","TBD","US-019","8 SP","Jira integration — ngoài phạm vi release v1"),
]

DOD = [
    ("Code đã được review bởi ít nhất 1 thành viên khác","Code Review"),
    ("Unit test coverage ≥ 80% cho business logic","Testing"),
    ("Acceptance Criteria đã pass toàn bộ (manual hoặc automated)","AC Verification"),
    ("Không có bug P1/P2 mở tại thời điểm demo","QA Testing"),
    ("UI đã được kiểm tra trên Chrome, Safari, Firefox (responsive)","UI/Cross-browser"),
    ("Tài liệu kỹ thuật (API doc, flow) được cập nhật nếu có thay đổi","Documentation"),
    ("PO/BA xác nhận nghiệm thu feature trước khi chuyển sang Done","PO Sign-off"),
]

# ── Số dòng đầu tiên chứa data thực sự (sau 2 header rows) ───────────────────
BL_DATA_START_ROW  = 3   # row index (0-based) trong sheet Product Backlog
BL_LAST_ROW        = BL_DATA_START_ROW + len(BACKLOG) - 1
OPS_DATA_START_ROW = 3   # trong sheet Vận hành
OPS_LAST_ROW       = OPS_DATA_START_ROW + len(OPS) - 1


def build():
    wb = xlsxwriter.Workbook(OUTPUT)

    # ── Global format helper ──────────────────────────────────────────────
    def fmt(**kw):
        base = dict(font_name="Times New Roman", font_size=11,
                    valign="vcenter", text_wrap=True)
        base.update(kw)
        return wb.add_format(base)

    hdr_orange = fmt(bold=True, font_size=12, font_color="#FFFFFF",
                     bg_color="#E86A23", align="center", border=1, border_color="#BBBBBB")
    hdr_dark   = fmt(bold=True, font_size=11, font_color="#FFFFFF",
                     bg_color="#1F2737", align="center", border=1, border_color="#BBBBBB")
    hdr_blue   = fmt(bold=True, font_size=11, font_color="#FFFFFF",
                     bg_color="#1E4D8C", align="center", border=1, border_color="#BBBBBB")

    cell_base  = fmt(border=1, border_color="#DDDDDD")
    cell_alt   = fmt(border=1, border_color="#DDDDDD", bg_color="#FFF8F4")
    cell_ctr   = fmt(align="center", border=1, border_color="#DDDDDD")
    cell_ctr_a = fmt(align="center", border=1, border_color="#DDDDDD", bg_color="#FFF8F4")
    cell_bold  = fmt(bold=True, border=1, border_color="#DDDDDD")

    id_fmt     = fmt(bold=True, font_color="#1E4D8C", align="center", border=1)
    id_fmt_a   = fmt(bold=True, font_color="#1E4D8C", align="center",
                     border=1, bg_color="#FFF8F4")
    epic_fmt   = fmt(bold=True, font_color="#E86A23", align="center", border=1)
    epic_fmt_a = fmt(bold=True, font_color="#E86A23", align="center",
                     border=1, bg_color="#FFF8F4")
    sp_fmt     = fmt(bold=True, font_size=12, align="center", border=1)
    sp_fmt_a   = fmt(bold=True, font_size=12, align="center",
                     border=1, bg_color="#FFF8F4")

    must_f   = fmt(bold=True, font_color="#FFFFFF", bg_color="#C0392B", align="center", border=1)
    should_f = fmt(bold=True, font_color="#FFFFFF", bg_color="#E67E22", align="center", border=1)
    could_f  = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60", align="center", border=1)
    wont_f   = fmt(bold=True, font_color="#FFFFFF", bg_color="#95A5A6", align="center", border=1)

    meta_lbl = fmt(bold=True, font_color="#FFFFFF", bg_color="#E86A23",
                   align="center", border=1)
    meta_val = fmt(bg_color="#FFF8F4", border=1)
    meta_formula = fmt(bold=True, font_color="#E86A23", bg_color="#FFF0E8",
                       align="center", border=1, font_size=12)

    title_fmt = fmt(bold=True, font_size=18, font_color="#E86A23", align="center")
    sub_fmt   = fmt(bold=True, font_size=13, font_color="#1F2737",  align="center")
    div_fmt   = wb.add_format({"bg_color": "#E86A23"})

    dod_chk   = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60",
                    align="center", border=1)
    dod_txt   = fmt(border=1, border_color="#DDDDDD", bg_color="#F9F9F9")
    dod_txt_a = fmt(border=1, border_color="#DDDDDD")
    dod_type  = fmt(align="center", font_color="#1A7A1A", border=1, bg_color="#EAF4EA")
    dod_typ_a = fmt(align="center", font_color="#1A7A1A", border=1, bg_color="#D5ECD5")

    def moscow_fmt(p):
        if p.startswith("Must"):   return must_f
        if p.startswith("Should"): return should_f
        if p.startswith("Could"):  return could_f
        return wont_f

    # status color helper
    def st_fmt(st):
        m = {"In Progress": fmt(bold=True, font_color="#E67E22", align="center",
                                bg_color="#FEF9E7", border=1),
             "To Do":       fmt(font_color="#1E4D8C", align="center",
                                bg_color="#EBF5FB", border=1),
             "Done":        fmt(font_color="#27AE60", align="center",
                                bg_color="#EAFAF1", border=1),
             "":            fmt(font_color="#AAAAAA", align="center", border=1)}
        return m.get(st, fmt(align="center", border=1))

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 1 — Cover  (với auto-formula)
    # ════════════════════════════════════════════════════════════════════════
    ws_cv = wb.add_worksheet("📋 Cover")
    ws_cv.hide_gridlines(2)
    ws_cv.set_column("A:A", 3)
    ws_cv.set_column("B:G", 18)

    ws_cv.merge_range("B3:G3", "PRODUCT BACKLOG — ĐỘI PRODUCT", title_fmt)
    ws_cv.merge_range("B4:G4", "Hệ thống Quản lý Task | FPT Software", sub_fmt)
    ws_cv.set_row(2, 45); ws_cv.set_row(3, 28); ws_cv.set_row(5, 8)
    ws_cv.merge_range("B6:G6", "", div_fmt)

    # Meta tĩnh
    static_meta = [
        (8,  "Dự án",      "Task Management System",   "Phiên bản",  "1.0"),
        (9,  "Team",       "Product Team (BA/PO/Dev)",  "Ngày tạo",   "25/06/2026"),
        (10, "Author",     "Product Owner / BA",         "Trạng thái", "Draft"),
    ]
    for r, l1, v1, l2, v2 in static_meta:
        ws_cv.set_row(r, 22)
        ws_cv.write(r, 1, l1, meta_lbl)
        ws_cv.merge_range(r, 2, r, 3, v1, meta_val)
        ws_cv.write(r, 4, l2, meta_lbl)
        ws_cv.merge_range(r, 5, r, 6, v2, meta_val)

    # Meta động — AUTO FORMULA
    ws_cv.set_row(11, 26)
    ws_cv.set_row(12, 26)
    ws_cv.set_row(13, 26)

    # Tổng US = COUNTA cột B (ID) trong Product Backlog, trừ header
    ws_cv.write(11, 1, "Tổng User Stories", meta_lbl)
    ws_cv.write_formula(11, 2,
        f"=COUNTA('📌 Product Backlog'!B{BL_DATA_START_ROW+1}:B1000)"
        f"+COUNTA('🔄 Vận hành'!A{OPS_DATA_START_ROW+1}:A1000)",
        meta_formula)
    ws_cv.merge_range(11, 2, 11, 3,
        f"=COUNTA('📌 Product Backlog'!B{BL_DATA_START_ROW+1}:B1000)"
        f"+COUNTA('🔄 Vận hành'!A{OPS_DATA_START_ROW+1}:A1000)",
        meta_formula)
    ws_cv.write(11, 4, "Tổng Epics", meta_lbl)
    # SUMPRODUCT để đếm unique epics
    ws_cv.write_formula(11, 5,
        f"=SUMPRODUCT(1/COUNTIF('📌 Product Backlog'!C{BL_DATA_START_ROW+1}:C{BL_LAST_ROW+1},"
        f"'📌 Product Backlog'!C{BL_DATA_START_ROW+1}:C{BL_LAST_ROW+1}))",
        meta_formula)
    ws_cv.merge_range(11, 5, 11, 6,
        f"=SUMPRODUCT(1/COUNTIF('📌 Product Backlog'!C{BL_DATA_START_ROW+1}:C{BL_LAST_ROW+1},"
        f"'📌 Product Backlog'!C{BL_DATA_START_ROW+1}:C{BL_LAST_ROW+1}))",
        meta_formula)

    ws_cv.write(12, 1, "Tổng Story Points (US)", meta_lbl)
    ws_cv.write_formula(12, 2,
        f"=SUM('📌 Product Backlog'!H{BL_DATA_START_ROW+1}:H{BL_LAST_ROW+1})",
        meta_formula)
    ws_cv.merge_range(12, 2, 12, 3,
        f"=SUM('📌 Product Backlog'!H{BL_DATA_START_ROW+1}:H{BL_LAST_ROW+1})",
        meta_formula)
    ws_cv.write(12, 4, "Tổng Task Vận hành", meta_lbl)
    ws_cv.write_formula(12, 5,
        f"=COUNTA('🔄 Vận hành'!A{OPS_DATA_START_ROW+1}:A1000)",
        meta_formula)
    ws_cv.merge_range(12, 5, 12, 6,
        f"=COUNTA('🔄 Vận hành'!A{OPS_DATA_START_ROW+1}:A1000)",
        meta_formula)

    ws_cv.write(13, 1, "In Progress (Vận hành)", meta_lbl)
    ws_cv.write_formula(13, 2,
        f"=COUNTIF('🔄 Vận hành'!K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"In Progress\")",
        meta_formula)
    ws_cv.merge_range(13, 2, 13, 3,
        f"=COUNTIF('🔄 Vận hành'!K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"In Progress\")",
        meta_formula)
    ws_cv.write(13, 4, "To Do (Vận hành)", meta_lbl)
    ws_cv.write_formula(13, 5,
        f"=COUNTIF('🔄 Vận hành'!K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"To Do\")",
        meta_formula)
    ws_cv.merge_range(13, 5, 13, 6,
        f"=COUNTIF('🔄 Vận hành'!K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"To Do\")",
        meta_formula)

    note_fmt = fmt(font_size=9, font_color="#888888", align="center")
    ws_cv.merge_range("B16:G16",
        "* Các ô màu cam tự động cập nhật khi thêm/sửa dữ liệu trong sheet Product Backlog và Vận hành.",
        note_fmt)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 2 — Product Backlog (US gốc)
    # ════════════════════════════════════════════════════════════════════════
    ws = wb.add_worksheet("📌 Product Backlog")
    ws.hide_gridlines(2)
    ws.freeze_panes(3, 0)
    ws.set_zoom(85)

    col_w = [4, 8, 8, 14, 22, 38, 38, 6, 12, 12]
    for i, w in enumerate(col_w): ws.set_column(i, i, w)

    ws.set_row(0, 32)
    ws.merge_range("A1:J1",
        "PRODUCT BACKLOG — HỆ THỐNG QUẢN LÝ TASK | ĐỘI PRODUCT", hdr_orange)

    ws.set_row(1, 28)
    for ci, h in enumerate(["#","ID","Epic","Epic Name","US Title",
                             "User Story (As a/I want/So that)",
                             "Acceptance Criteria (Gherkin)","SP","Sprint","Status"]):
        ws.write(2, ci, h, hdr_dark)

    for idx, (us_id, epic_id, epic_name, title, story, ac, priority, sp, sprint, status) in enumerate(BACKLOG):
        r   = idx + BL_DATA_START_ROW
        alt = (idx % 2 == 1)
        ws.set_row(r, 90)
        ws.write(r, 0, idx+1,    cell_ctr_a if alt else cell_ctr)
        ws.write(r, 1, us_id,    id_fmt_a   if alt else id_fmt)
        ws.write(r, 2, epic_id,  epic_fmt_a if alt else epic_fmt)
        ws.write(r, 3, epic_name, cell_alt  if alt else cell_base)
        ws.write(r, 4, title,    cell_bold)
        ws.write(r, 5, story,    cell_alt   if alt else cell_base)
        ws.write(r, 6, ac,       cell_alt   if alt else cell_base)
        ws.write(r, 7, int(sp),  sp_fmt_a   if alt else sp_fmt)
        ws.write(r, 8, sprint,   cell_ctr_a if alt else cell_ctr)
        ws.write(r, 9, status,   st_fmt(status))

    # ── Dòng tổng hợp cuối ──
    sum_row = BL_LAST_ROW + 2
    ws.set_row(sum_row, 24)
    sum_f = fmt(bold=True, font_color="#FFFFFF", bg_color="#1F2737",
                align="center", border=1)
    ws.merge_range(sum_row, 0, sum_row, 6, "TỔNG", sum_f)
    ws.write_formula(sum_row, 7,
        f"=SUM(H{BL_DATA_START_ROW+1}:H{BL_LAST_ROW+1})", sum_f)
    ws.write_formula(sum_row, 8,
        f"=COUNTA(I{BL_DATA_START_ROW+1}:I{BL_LAST_ROW+1})&\" sprints\"", sum_f)
    ws.write_formula(sum_row, 9,
        f"=COUNTA(J{BL_DATA_START_ROW+1}:J{BL_LAST_ROW+1})&\" US\"", sum_f)

    # ── Legend MoSCoW ──
    leg = sum_row + 2
    ws.set_row(leg, 22)
    ws.write(leg, 0, "MoSCoW:", fmt(bold=True, font_size=10))
    for ci, (lbl, f2) in enumerate([("Must Have",must_f),("Should Have",should_f),
                                     ("Could Have",could_f),("Won't Have v1",wont_f)]):
        ws.write(leg, ci+1, lbl, f2)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 3 — Vận hành (import từ Backlog FPTvn + Roadmap 18.5)
    # ════════════════════════════════════════════════════════════════════════
    ws_op = wb.add_worksheet("🔄 Vận hành")
    ws_op.hide_gridlines(2)
    ws_op.freeze_panes(3, 0)
    ws_op.set_zoom(85)

    op_col_w = [8, 14, 22, 32, 12, 20, 12, 10, 14, 18, 12, 26]
    for i, w in enumerate(op_col_w): ws_op.set_column(i, i, w)

    ws_op.set_row(0, 32)
    ws_op.merge_range("A1:L1",
        "TASK VẬN HÀNH — Import từ Backlog FPTvn & Roadmap 18.5  |  Loại trừ: Done",
        hdr_orange)

    op_headers = ["ID","Nguồn","Tên Task","Mô tả yêu cầu","Sản phẩm",
                  "URL liên quan","Timeline","Ưu tiên","PIC Ecom",
                  "PIC Thực hiện","Trạng thái","Ghi chú"]
    ws_op.set_row(1, 28)
    for ci, h in enumerate(op_headers):
        ws_op.write(2, ci, h, hdr_dark)

    src_fptfvn = fmt(bold=True, font_color="#1E4D8C", align="center",
                     bg_color="#EBF5FB", border=1)
    src_roadmap = fmt(bold=True, font_color="#6C3483", align="center",
                      bg_color="#F5EEF8", border=1)

    prio_high   = fmt(bold=True, font_color="#C0392B", align="center", border=1)
    prio_med    = fmt(bold=True, font_color="#E67E22", align="center", border=1)
    prio_low    = fmt(bold=True, font_color="#27AE60", align="center", border=1)
    prio_empty  = fmt(font_color="#AAAAAA",  align="center", border=1)

    def prio_fmt(p):
        p = str(p).strip()
        if p == "High":   return prio_high
        if p == "Medium": return prio_med
        if p == "Low":    return prio_low
        return prio_empty

    for idx, (oid, src, name, desc, prod, url, tl, prio, pic_ecom,
              pic_impl, status, note) in enumerate(OPS):
        r   = idx + OPS_DATA_START_ROW
        alt = (idx % 2 == 1)
        ws_op.set_row(r, 75)

        bg_base = "#F0F7FF" if src == "Backlog FPTvn" else "#F8F0FF"
        bg_alt  = "#E8F4FF" if src == "Backlog FPTvn" else "#F0E8FF"
        bg = bg_alt if alt else bg_base

        c_base = fmt(border=1, border_color="#DDDDDD", bg_color=bg)
        c_ctr  = fmt(align="center", border=1, border_color="#DDDDDD", bg_color=bg)

        ws_op.write(r, 0,  oid,      id_fmt_a if alt else id_fmt)
        ws_op.write(r, 1,  src,      src_roadmap if src=="Roadmap 18.5" else src_fptfvn)
        ws_op.write(r, 2,  name,     fmt(bold=True, border=1, bg_color=bg))
        ws_op.write(r, 3,  desc,     c_base)
        ws_op.write(r, 4,  prod,     c_ctr)
        ws_op.write(r, 5,  url,      c_base)
        ws_op.write(r, 6,  tl,       c_ctr)
        ws_op.write(r, 7,  prio,     prio_fmt(prio))
        ws_op.write(r, 8,  pic_ecom, c_ctr)
        ws_op.write(r, 9,  pic_impl, c_ctr)
        ws_op.write(r, 10, status,   st_fmt(status))
        ws_op.write(r, 11, note,     c_base)

    # ── Dòng tổng hợp cuối ──
    op_sum = OPS_LAST_ROW + 2
    ws_op.set_row(op_sum, 24)
    sum_op = fmt(bold=True, font_color="#FFFFFF", bg_color="#1F2737",
                 align="center", border=1)
    ws_op.merge_range(op_sum, 0, op_sum, 1, "TỔNG", sum_op)
    ws_op.write_formula(op_sum, 2,
        f"=COUNTA(A{OPS_DATA_START_ROW+1}:A{OPS_LAST_ROW+1})&\" tasks\"", sum_op)
    ws_op.write_formula(op_sum, 3,
        f"=COUNTIF(B{OPS_DATA_START_ROW+1}:B{OPS_LAST_ROW+1},\"Backlog FPTvn\")"
        f"&\" FPTvn | \""
        f"&COUNTIF(B{OPS_DATA_START_ROW+1}:B{OPS_LAST_ROW+1},\"Roadmap 18.5\")"
        f"&\" Roadmap\"", sum_op)
    ws_op.write_formula(op_sum, 10,
        f"=COUNTIF(K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"In Progress\")"
        f"&\" In Progress | \""
        f"&COUNTIF(K{OPS_DATA_START_ROW+1}:K{OPS_LAST_ROW+1},\"To Do\")"
        f"&\" To Do\"", sum_op)
    for ci in [4,5,6,7,8,9,11]:
        ws_op.write(op_sum, ci, "", sum_op)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 4 — Sprint Planning
    # ════════════════════════════════════════════════════════════════════════
    ws_sp = wb.add_worksheet("🗓 Sprint Planning")
    ws_sp.hide_gridlines(2); ws_sp.freeze_panes(2, 0)
    for i, w in enumerate([16,10,14,14,30,10,45]):
        ws_sp.set_column(i, i, w)

    ws_sp.set_row(0, 30)
    ws_sp.merge_range("A1:G1", "SPRINT PLANNING — RELEASE v1", hdr_orange)
    ws_sp.set_row(1, 24)
    for ci, h in enumerate(["Sprint","Thời lượng","Bắt đầu","Kết thúc",
                             "User Stories","Story Points","Sprint Goal"]):
        ws_sp.write(1, ci, h, hdr_blue)

    sn_f  = fmt(bold=True,font_color="#FFFFFF",bg_color="#E86A23",align="center",border=1)
    sn_fa = fmt(bold=True,font_color="#FFFFFF",bg_color="#1E4D8C",align="center",border=1)
    sp_r  = fmt(border=1, border_color="#DDDDDD")
    sp_ra = fmt(border=1, border_color="#DDDDDD", bg_color="#EFF3FB")
    sp_c  = fmt(align="center", border=1, border_color="#DDDDDD")
    sp_ca = fmt(align="center", border=1, border_color="#DDDDDD", bg_color="#EFF3FB")
    sp_pt = fmt(bold=True, align="center", font_color="#1E4D8C", border=1)
    sp_pa = fmt(bold=True, align="center", font_color="#1E4D8C", border=1, bg_color="#EFF3FB")

    for idx, (sprint, dur, start, end, stories, pts, goal) in enumerate(SPRINT_PLAN):
        r = idx + 2; alt = (idx % 2 == 1)
        ws_sp.set_row(r, 40)
        ws_sp.write(r, 0, sprint,  sn_fa if alt else sn_f)
        ws_sp.write(r, 1, dur,     sp_ca if alt else sp_c)
        ws_sp.write(r, 2, start,   sp_ca if alt else sp_c)
        ws_sp.write(r, 3, end,     sp_ca if alt else sp_c)
        ws_sp.write(r, 4, stories, sp_ra if alt else sp_r)
        ws_sp.write(r, 5, pts,     sp_pa if alt else sp_pt)
        ws_sp.write(r, 6, goal,    sp_ra if alt else sp_r)

    sr = len(SPRINT_PLAN) + 3
    ws_sp.set_row(sr, 26)
    sf = fmt(bold=True,font_color="#FFFFFF",bg_color="#1F2737",align="center",border=1)
    ws_sp.merge_range(sr,0,sr,4,"TỔNG RELEASE v1 (Sprint 1–4)",sf)
    ws_sp.write(sr,5,"62 SP",sf)
    ws_sp.write(sr,6,"18 User Stories — ~8 tuần phát triển",sf)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 5 — Definition of Done
    # ════════════════════════════════════════════════════════════════════════
    ws_dod = wb.add_worksheet("✅ Definition of Done")
    ws_dod.hide_gridlines(2)
    ws_dod.set_column("A:A", 6)
    ws_dod.set_column("B:B", 70)
    ws_dod.set_column("C:C", 20)
    ws_dod.set_row(0, 30)
    ws_dod.merge_range("A1:C1", "DEFINITION OF DONE (DoD) — ĐỘI PRODUCT", hdr_orange)
    ws_dod.set_row(1, 22)
    ws_dod.write(1, 0, "#",         hdr_dark)
    ws_dod.write(1, 1, "Tiêu chí nghiệm thu", hdr_dark)
    ws_dod.write(1, 2, "Loại kiểm tra", hdr_dark)
    for i, (item, dtype) in enumerate(DOD):
        r = i+2; alt = (i % 2 == 1)
        ws_dod.set_row(r, 26)
        ws_dod.write(r, 0, f"✓ {i+1}", dod_chk)
        ws_dod.write(r, 1, item, dod_txt_a if alt else dod_txt)
        ws_dod.write(r, 2, dtype, dod_typ_a if alt else dod_type)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 6 — Kanban Board
    # ════════════════════════════════════════════════════════════════════════
    ws_kb = wb.add_worksheet("🗂 Kanban Board")
    ws_kb.hide_gridlines(2)
    ws_kb.set_row(0, 30)
    ws_kb.merge_range("A1:L1", "KANBAN BOARD — SPRINT HIỆN TẠI", hdr_orange)

    cols_kb = [("To Do","#95A5A6","#ECF0F1"),("In Progress","#E67E22","#FEF9E7"),
               ("Review","#1E4D8C","#EBF5FB"),("Done","#27AE60","#EAFAF1")]
    starts  = [0, 3, 6, 9]

    for (status, hc, bc), col_s in zip(cols_kb, starts):
        for c in range(col_s, col_s+3): ws_kb.set_column(c, c, 7)
        ws_kb.set_row(1, 26)
        ws_kb.merge_range(1, col_s, 1, col_s+2, status,
                          fmt(bold=True,font_size=13,font_color="#FFFFFF",
                              bg_color=hc,align="center",border=1))
        sprint1_tasks = [t for t in BACKLOG if t[8]=="Sprint 1" and t[9]==status]
        for ti in range(8):
            r = ti+2; ws_kb.set_row(r, 50)
            if ti < len(sprint1_tasks):
                t = sprint1_tasks[ti]
                ws_kb.merge_range(r,col_s,r,col_s+2, f"{t[0]}\n{t[3]}",
                                  fmt(bg_color=bc,border=1,border_color=hc,
                                      font_size=9,text_wrap=True))
            else:
                ws_kb.merge_range(r,col_s,r,col_s+2,"",
                                  fmt(bg_color=bc,border=1,border_color="#DDDDDD"))

    wb.close()
    print(f"✅ Saved: {OUTPUT}")
    print(f"   Sheets: Cover (auto-formula), Product Backlog ({len(BACKLOG)} US),")
    print(f"           Vận hành ({len(OPS)} tasks: 18 FPTvn + 14 Roadmap),")
    print(f"           Sprint Planning, DoD, Kanban Board")


if __name__ == "__main__":
    build()

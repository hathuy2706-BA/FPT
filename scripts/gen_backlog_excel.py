#!/usr/bin/env python3
"""Product Backlog Excel — FPT Telecom.
   Columns: # | ID | Epic | Epic Name | US Title | User Story | AC | SP |
            Timeline mong muốn | Timeline ISC | PIC (BA) |
            Trạng thái (dropdown) | Nguồn | Ghi chú"""

import xlsxwriter

OUTPUT = "/Users/hathuy/Documents/FPT-1/backlogpo/product_backlog_team.xlsx"

TRANG_THAI = [
    "Chưa tiếp nhận yêu cầu",
    "Đã tiếp nhận yêu cầu",
    "Đang phân tích",
    "Đang trao đổi PBLQ",
    "Đã bàn giao ISC",
    "In Progress DEV",
    "UAT",
    "Done",
]

# ── Dữ liệu ──────────────────────────────────────────────────────────────────
# Tuple: (id, epic, epic_name, us_title, user_story, ac,
#         priority, sp,
#         timeline, tl_isc, pic_ba,
#         trang_thai, nguon, ghi_chu)

BACKLOG = [
    # ══ Backlog FPTvn ══════════════════════════════════════════════════════
    ("BF-001","","Camera",
     "Hiển thị giá Cloud Camera theo gói buffet",
     "Là khách hàng mua Camera FPT, tôi muốn xem giá cloud hiển thị dạng gói buffet (50.000đ/tháng) thay vì chia theo số mắt camera, để dễ so sánh và quyết định mua.",
     "CHO TRƯỚC tôi ở trang thanh toán Camera\nKHI tôi xem phần chọn gói cloud\nTHÌ giá hiển thị 50.000đ/tháng dạng buffet, không chia theo từng mắt camera",
     "High","5","15/04","","",
     "Đã tiếp nhận yêu cầu","Backlog FPTvn","Nhờ Hà check với chị Linh"),

    ("BF-002","","Camera",
     "Cập nhật giao diện thanh toán Camera – gói cloud 3D buffet",
     "Là khách hàng mua Camera FPT, tôi muốn giao diện trang thanh toán hiển thị đúng gói cloud (bỏ nhãn 'x5') và ẩn phí lắp đặt khi chọn tự lắp, để tránh nhầm lẫn và tăng tỷ lệ chuyển đổi.",
     "CHO TRƯỚC tôi ở trang thanh toán Camera\nKHI tôi chọn gói cloud 3D buffet 6 tháng\nTHÌ nhãn 'x5' không hiển thị\n\nCHO TRƯỚC tôi chọn hình thức Tự lắp đặt\nTHÌ dòng phí lắp đặt bị ẩn hoàn toàn",
     "High","5","15/04","","",
     "In Progress DEV","Backlog FPTvn","Đang làm việc với chính sách"),

    ("BF-003","","Internet",
     "Cập nhật trang địa phương theo giao diện mới",
     "Là quản trị viên nội dung CMS, tôi muốn các trang địa phương (/lap-internet-wifi-hcm…) được chuyển sang nền tảng UI mới để thêm/chỉnh sửa section linh hoạt, chuẩn hoá breadcrumb và Heading 1.",
     "CHO TRƯỚC tôi đăng nhập CMS\nKHI tôi mở trang địa phương /lap-internet-wifi-[tinh]\nTHÌ giao diện mới hiển thị và tôi có thể thêm section mới\n\nCHO TRƯỚC tôi lưu thay đổi\nTHÌ nội dung hiển thị đúng trên FE, không lỗi layout",
     "High","5","24/04","","",
     "Đã tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-004","","Internet",
     "Luồng nâng cấp 5 dịch vụ trên FPT.vn",
     "Là khách hàng FPT đang sử dụng dịch vụ, tôi muốn nâng cấp các dịch vụ (VVIP, Camera, AP, băng thông, wifi6) trực tiếp trên FPT.vn, để hoàn tất nâng cấp mà không cần gọi tổng đài.",
     "CHO TRƯỚC tôi đăng nhập tài khoản FPT\nKHI tôi vào trang /nang-cap\nTHÌ hiển thị 5 dịch vụ có thể nâng cấp kèm giá\n\nKHI tôi chọn nâng cấp và xác nhận\nTHÌ đơn hàng được tạo và tôi nhận thông báo xác nhận",
     "High","5","","","",
     "In Progress DEV","Backlog FPTvn",""),

    ("BF-005","","Internet",
     "LDP FCM",
     "Là khách hàng tiềm năng sử dụng FCM, tôi muốn truy cập trang landing page FCM đầy đủ thông tin gói cước và nút đăng ký, để đăng ký dịch vụ nhanh chóng.",
     "CHO TRƯỚC tôi truy cập URL LDP FCM\nKHI trang tải xong\nTHÌ hiển thị đầy đủ thông tin gói cước, hình ảnh và nút CTA\n\nKHI tôi nhấn đăng ký\nTHÌ điều hướng đúng đến luồng mua",
     "Medium","3","","","",
     "In Progress DEV","Backlog FPTvn","22/5 golive 2 LDP"),

    ("BF-006","","",
     "CMS Tổng đài wifi – 5 mẫu LDP",
     "Là người quản trị nội dung, tôi muốn có 5 mẫu Landing Page cho tổng đài wifi trên CMS, để team content tự thiết kế và triển khai campaign mà không cần lập trình viên.",
     "CHO TRƯỚC tôi đăng nhập CMS\nKHI tôi chọn Tạo LDP mới\nTHÌ có 5 mẫu template sẵn để chọn\n\nKHI tôi publish LDP\nTHÌ trang hiển thị đúng trên FE",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-007","","Camera",
     "Bổ sung luồng giao hàng Camera trong LDP nâng cấp",
     "Là khách hàng nâng cấp Camera FPT, tôi muốn có tùy chọn giao hàng Camera trong luồng nâng cấp trên LDP, để hoàn tất đơn nâng cấp và nhận thiết bị mà không cần liên hệ riêng.",
     "CHO TRƯỚC tôi ở LDP nâng cấp Camera\nKHI tôi chọn gói nâng cấp\nTHÌ xuất hiện tùy chọn Giao hàng tận nơi hoặc Tự lắp đặt\n\nKHI tôi chọn giao hàng và điền địa chỉ\nTHÌ đơn hàng xác nhận với thông tin giao hàng đầy đủ",
     "High","5","26/05","","",
     "In Progress DEV","Backlog FPTvn",""),

    ("BF-008","","Internet",
     "LDP FCitizen – trang dành riêng cho FPTers",
     "Là nhân viên FPT (FPTer), tôi muốn truy cập trang landing page riêng cho FCitizen hiển thị gói cước ưu đãi và quy trình đăng ký nội bộ, để đăng ký dịch vụ với mức giá ưu đãi dành riêng.",
     "CHO TRƯỚC tôi truy cập trang FCitizen\nKHI tôi chưa xác thực là FPTer\nTHÌ hệ thống yêu cầu xác thực email @fpt.com.vn\n\nKHI xác thực thành công\nTHÌ hiển thị các gói cước ưu đãi dành riêng cho FPTers",
     "High","5","","","",
     "Đã tiếp nhận yêu cầu","Backlog FPTvn","Chờ FTQ phản hồi quy trình bán gói"),

    ("BF-009","","Camera",
     "Exit-intent popup trang Camera",
     "Là khách hàng đang rời trang Camera FPT, tôi muốn thấy popup ưu đãi cuối cùng trước khi thoát trang, để có thêm cơ hội xem ưu đãi và quyết định đăng ký.",
     "CHO TRƯỚC tôi đang xem trang /camera trên máy tính\nKHI con trỏ di chuyển ra phía thanh điều hướng trình duyệt\nTHÌ popup exit-intent xuất hiện sau 300ms\n\nCHO TRƯỚC tôi dùng điện thoại\nKHI tôi scroll lên nhanh\nTHÌ popup hiện; chỉ hiện tối đa 1 lần/phiên",
     "High","5","06/08/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-010","","Internet",
     "Tích hợp API Giá Vàng & Điểm thi Đại học",
     "Là người dùng FPT.vn, tôi muốn xem thông tin giá vàng SJC/9999 và điểm thi đại học theo thời gian thực ngay trên website, để tra cứu nhanh mà không cần rời trang.",
     "CHO TRƯỚC widget giá vàng được kích hoạt\nKHI tôi mở trang chứa widget\nTHÌ dữ liệu giá vàng cập nhật trong vòng 5 phút\n\nCHO TRƯỚC API ngừng hoạt động\nTHÌ widget hiển thị Đang cập nhật thay vì báo lỗi",
     "Low","2","06/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn","Không ưu tiên giai đoạn này"),

    ("BF-011","","Camera",
     "Trang Author Profile Chuyên gia Camera FPT",
     "Là khách hàng tìm hiểu Camera FPT, tôi muốn xem trang giới thiệu chuyên gia kỹ thuật (ảnh, tên, chức vụ, chứng chỉ), để tin tưởng hơn vào chất lượng sản phẩm và dịch vụ.",
     "CHO TRƯỚC tôi truy cập /tac-gia/chuyen-gia-ky-thuat\nKHI trang tải xong\nTHÌ hiển thị 3–5 thẻ profile chuyên gia với ảnh thực, tên, chức vụ và chứng chỉ\n\nCHO TRƯỚC trang được lập index SEO\nTHÌ có schema markup dạng Person",
     "Medium","3","19/06","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-012","","Internet/SA",
     "LDP Ngoại Hạng Anh (NHA)",
     "Là người hâm mộ bóng đá dùng gói SA Play FPT, tôi muốn truy cập trang tổng hợp NHA xem kết quả và bảng xếp hạng cập nhật tự động, để theo dõi giải đấu mà không cần tìm nhiều nơi.",
     "CHO TRƯỚC tôi truy cập /ngoai-hang-anh\nKHI trang tải xong\nTHÌ hiển thị bảng xếp hạng và kết quả trận đấu gần nhất từ API\n\nCHO TRƯỚC tỷ số thay đổi sau trận\nTHÌ dữ liệu tự cập nhật trong vòng 30 phút",
     "Low","2","20/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn","Không ưu tiên giai đoạn này"),

    ("BF-013","","Internet/SA",
     "Video Hub – Block video tự động từ FPT Play",
     "Là người dùng FPT.vn quan tâm nội dung thể thao, tôi muốn xem block video Recap/Highlight tự động cập nhật từ YouTube FPT Play ngay trên website, để không cần chuyển sang YouTube.",
     "CHO TRƯỚC block Video Hub được nhúng vào trang\nKHI tôi mở trang\nTHÌ hiển thị tối đa 6 video mới nhất từ YouTube FPT Play\n\nKHI tôi nhấn vào video\nTHÌ phát inline, không chuyển trang; video lazy-load không ảnh hưởng LCP",
     "Medium","3","27/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-014","","Internet",
     "Bảng giá gói cước theo ID trên trang tin tức",
     "Là người quản trị nội dung, tôi muốn gắn thành phần bảng giá gói cước theo ID vào bài viết, để giá hiển thị tự động cập nhật theo hệ thống mà không cần chỉnh sửa thủ công từng bài.",
     "CHO TRƯỚC tôi chèn shortcode [goi-cuoc id=X] vào bài viết CMS\nKHI trang tin tức tải\nTHÌ hiển thị đúng tên gói, giá và mô tả ngắn từ hệ thống\n\nKHI gói cước thay đổi giá trong hệ thống\nTHÌ bài viết tự động hiển thị giá mới",
     "High","5","03/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-015","","Internet",
     "Banner thay đổi nhanh bằng shortcode trên trang tin tức",
     "Là người quản trị nội dung, tôi muốn thay đổi banner khuyến mại trong bài viết tin tức bằng shortcode thay vì chỉnh từng bài, để cập nhật nhanh khi chương trình kết thúc.",
     "CHO TRƯỚC tôi chèn shortcode banner vào bài viết\nKHI chương trình khuyến mại kết thúc\nTHÌ tôi chỉ cần cập nhật 1 nơi và tất cả bài dùng shortcode đó tự cập nhật\n\nCHO TRƯỚC shortcode được cấu hình\nTHÌ banner hỗ trợ ảnh và link điều hướng",
     "High","5","03/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-016","","Camera",
     "Luồng LDP Nâng cấp Cam 200K – tối ưu thanh toán",
     "Là khách hàng Camera FPT muốn nâng cấp lên gói 200K, tôi muốn hoàn tất thanh toán ngay trên FPT.vn mà không bị chuyển hướng ra ngoài hoặc gặp lỗi, để việc nâng cấp diễn ra liền mạch.",
     "CHO TRƯỚC tôi ở LDP nâng cấp Camera\nKHI tôi chọn gói 200K và nhấn thanh toán\nTHÌ không bị chuyển hướng sang trang ngoài\n\nKHI thanh toán thành công\nTHÌ hiển thị trang xác nhận với thông tin đơn hàng và thời gian kích hoạt",
     "High","5","24/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-017","","Camera",
     "Luồng Mua mới Camera – sửa đứt gãy tại bước thanh toán",
     "Là khách hàng mua mới Camera FPT, tôi muốn hoàn tất thanh toán mà không bị gián đoạn ở bước cuối, để đơn hàng được xử lý và nhận xác nhận ngay.",
     "CHO TRƯỚC tôi đã chọn camera và điền thông tin\nKHI tôi nhấn Xác nhận thanh toán\nTHÌ hệ thống xử lý và chuyển sang trang thành công\n\nCHO TRƯỚC xảy ra lỗi kỹ thuật\nTHÌ hệ thống hiển thị thông báo lỗi rõ ràng và cho phép thử lại",
     "High","5","24/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    ("BF-018","","Camera",
     "Luồng Mua mới Camera – bổ sung giỏ hàng combo",
     "Là khách hàng mua Camera FPT, tôi muốn chọn đồng thời nhiều loại camera (ngoài trời + trong nhà) trong cùng một đơn hàng, để mua combo tiện lợi mà không cần đặt nhiều đơn riêng.",
     "CHO TRƯỚC tôi đang ở trang chọn Camera\nKHI tôi thêm camera ngoài trời vào giỏ\nTHÌ hệ thống cho phép tiếp tục thêm camera trong nhà\n\nKHI tôi vào giỏ hàng\nTHÌ hiển thị đầy đủ cả 2 sản phẩm với giá tổng chính xác",
     "High","5","24/06/2026","","",
     "Chưa tiếp nhận yêu cầu","Backlog FPTvn",""),

    # ══ Roadmap 18.5 ═══════════════════════════════════════════════════════
    ("RM-001","","Camera",
     "Luồng bán Camera chỉ giao hàng – Sàn TMĐT",
     "Là khách hàng mua Camera FPT qua sàn TMĐT, tôi muốn thực hiện luồng mua hàng chỉ giao hàng (không bao gồm lắp đặt), để nhận thiết bị nhanh chóng và tự lắp đặt.",
     "CHO TRƯỚC tôi chọn mua Camera trên sàn TMĐT\nKHI tôi chọn hình thức Chỉ giao hàng\nTHÌ hệ thống không yêu cầu đặt lịch lắp đặt\n\nKHI đơn được tạo\nTHÌ trạng thái chuyển sang Đang xử lý giao hàng và tôi nhận thông báo",
     "High","5","20/06","","",
     "In Progress DEV","Roadmap 18.5","Chưa có chỗ nâng cấp camera combo trên HD net only"),

    ("RM-002","","Internet",
     "LDP FCitizen – UI/UX & cập nhật chính sách gói bán",
     "Là nhân viên FPT (FPTer), tôi muốn truy cập trang FCitizen tại fpt.vn/fcitizen với giao diện mới và chính sách gói bán được cập nhật, để biết chính xác quyền lợi và đăng ký đúng chính sách.",
     "CHO TRƯỚC tôi truy cập fpt.vn/fcitizen\nKHI trang tải\nTHÌ giao diện mới hiển thị đúng design\n\nCHO TRƯỚC chính sách gói bán được cập nhật\nTHÌ thông tin trên trang phản ánh đúng, không lệch với hệ thống backend",
     "Medium","3","06/03/2026","","",
     "Đã tiếp nhận yêu cầu","Roadmap 18.5","Cần làm rõ quy trình bán: chỉ sửa UI hay có luồng bán mới?"),

    ("RM-003","","Nâng cấp/bán thêm",
     "Luồng nâng cấp 5 Dịch vụ – FPT.vn",
     "Là khách hàng FPT muốn bổ sung hoặc nâng cấp dịch vụ, tôi muốn thực hiện luồng nâng cấp 5 loại dịch vụ trực tiếp trên FPT.vn, để hoàn tất mà không phải liên hệ tổng đài.",
     "CHO TRƯỚC tôi đang đăng nhập trên FPT.vn\nKHI tôi vào trang nâng cấp\nTHÌ hiển thị đủ 5 dịch vụ với chính sách giá rõ ràng\n\nKHI tôi hoàn tất nâng cấp\nTHÌ nhận xác nhận và dịch vụ kích hoạt trong vòng 24 giờ",
     "Medium","3","30/06","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-004","","Giới thiệu bạn bè",
     "Hub vinh danh Giới thiệu bạn bè trên App HiFPT",
     "Là khách hàng tham gia chương trình Giới thiệu bạn bè, tôi muốn xem trang vinh danh thành tích (Cơ bản/Bạc/Vàng/Kim cương) trên App HiFPT, để được ghi nhận và có thêm động lực giới thiệu.",
     "CHO TRƯỚC tôi mở App HiFPT và đã tham gia GTBB\nKHI tôi vào mục Vinh danh\nTHÌ hiển thị level hiện tại, số người đã giới thiệu và phần thưởng tương ứng\n\nCHO TRƯỚC tôi đạt đủ điều kiện lên level mới\nTHÌ hệ thống gửi thông báo chúc mừng",
     "Medium","3","30/06","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-005","","Giới thiệu bạn bè",
     "LDP Giới thiệu bạn bè – Người được giới thiệu",
     "Là người được bạn bè giới thiệu đến FPT, tôi muốn truy cập trang landing page riêng giải thích ưu đãi và hướng dẫn đăng ký, để hiểu ngay quyền lợi và hoàn tất đăng ký nhanh chóng.",
     "CHO TRƯỚC tôi nhấn link giới thiệu từ bạn\nKHI trang LDP tải\nTHÌ hiển thị tên người giới thiệu, ưu đãi áp dụng và nút đăng ký\n\nKHI tôi đăng ký thành công\nTHÌ hệ thống ghi nhận mã giới thiệu và cả hai bên nhận thưởng theo chính sách",
     "Medium","3","30/07","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-006","","Thanh toán",
     "Tích hợp Auto Pay trên website FPT.vn",
     "Là khách hàng đăng ký dịch vụ FPT định kỳ, tôi muốn lưu thẻ và kích hoạt tự động gia hạn trên FPT.vn, để không bị gián đoạn dịch vụ do quên thanh toán.",
     "CHO TRƯỚC tôi đăng nhập FPT.vn\nKHI tôi vào cài đặt thanh toán và thêm thẻ\nTHÌ thẻ được mã hóa và lưu an toàn\n\nKHI đến kỳ gia hạn\nTHÌ hệ thống tự trừ tiền và gửi thông báo; khi thất bại tôi nhận cảnh báo trong vòng 24 giờ",
     "Medium","3","30/06","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5","Cần làm rõ kịch bản thanh toán auto pay với team HiFPT"),

    ("RM-007","","SA Play",
     "Gửi E-Card khi khách hàng mua gói SA Play",
     "Là khách hàng mua gói SA Play trên FPT.vn hoặc HiFPT, tôi muốn gửi E-Card kỹ thuật số cho bạn bè sau khi mua gói, để bạn tôi tự kích hoạt dịch vụ một cách tiện lợi.",
     "CHO TRƯỚC tôi mua gói SA Play và chọn hình thức Tặng bạn bè\nKHI thanh toán thành công\nTHÌ hệ thống gửi E-Card qua email/SMS cho người nhận\n\nKHI người nhận nhấn kích hoạt\nTHÌ mã được ghi nhận và dịch vụ kích hoạt cho tài khoản họ",
     "Medium","3","30/06","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5","ISC đánh dấu KH đi theo luồng nhận mã; FPL trả thông tin qua ZNS"),

    ("RM-008","","Camera",
     "Landing Page Camera GenZ",
     "Là khách hàng trẻ (GenZ) quan tâm đến Camera FPT, tôi muốn trải nghiệm trang landing page phong cách GenZ hiển thị sản phẩm, giá và ưu đãi nổi bật, để dễ dàng quyết định đăng ký.",
     "CHO TRƯỚC tôi truy cập LDP Camera GenZ\nKHI trang tải\nTHÌ giao diện hiển thị đúng concept GenZ, tải dưới 3 giây\n\nKHI tôi nhấn Đăng ký ngay\nTHÌ chuyển đúng đến luồng mua và chính sách được áp dụng đầy đủ",
     "High","5","30/06","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5","Cần đánh giá lại mức độ ưu tiên và xác nhận owner"),

    ("RM-009","","Internet",
     "Luồng Recall – tái kết nối khách hàng cũ",
     "Là khách hàng FPT đã từng dừng sử dụng dịch vụ, tôi muốn nhận đề xuất kích hoạt lại dịch vụ phù hợp qua FPT.vn hoặc HiFPT, để quay lại sử dụng với ưu đãi tái kết nối.",
     "CHO TRƯỚC tôi thuộc tệp khách hàng Recall\nKHI tôi truy cập FPT.vn hoặc HiFPT\nTHÌ hệ thống hiển thị banner/popup đề xuất tái kết nối với gói phù hợp\n\nKHI tôi nhấn Đăng ký lại\nTHÌ luồng mua tự điền sẵn thông tin cũ",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-010","","Internet",
     "Luồng Autocall – tích hợp ZNS nâng cấp/bán thêm",
     "Là người quản lý chiến dịch bán hàng FPT, tôi muốn tích hợp ZNS vào hệ thống Autocall để tiếp cận khách hàng hiện hữu nhằm nâng cấp hoặc bán thêm dịch vụ, để tỷ lệ tiếp cận tăng và chi phí SMS giảm.",
     "CHO TRƯỚC chiến dịch Autocall được cấu hình với ZNS\nKHI hệ thống gọi đến số điện thoại trong tệp data\nTHÌ tin ZNS được gửi khi cuộc gọi không bắt máy\n\nKHI khách hàng phản hồi ZNS\nTHÌ log được ghi nhận trong hệ thống CRM",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-011","","Internet/SA",
     "Cross-sell FPTPlay.vn",
     "Là khách hàng Internet FPT, tôi muốn thấy đề xuất nâng cấp/thêm gói FPT Play khi duyệt FPT.vn, để biết về gói giải trí bổ sung và dễ dàng nâng cấp trong một giao dịch.",
     "CHO TRƯỚC tôi đang đăng nhập FPT.vn\nKHI tôi xem trang sản phẩm Internet\nTHÌ hiển thị block cross-sell gói SA Play với giá nâng cấp\n\nKHI tôi nhấn Thêm vào gói\nTHÌ gói SA Play được thêm vào đơn hàng hiện tại",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-012","","Camera",
     "Self-Service Cam trên sàn TMĐT",
     "Là khách hàng mua Camera FPT qua sàn TMĐT, tôi muốn tự xử lý các yêu cầu sau mua (cài đặt, báo lỗi, gia hạn cloud) qua giao diện self-service, để không cần gọi hotline cho vấn đề đơn giản.",
     "CHO TRƯỚC tôi đã mua Camera FPT qua sàn\nKHI tôi vào khu vực quản lý đơn hàng\nTHÌ có tùy chọn Hỗ trợ kỹ thuật và Gia hạn Cloud\n\nKHI tôi gửi yêu cầu hỗ trợ\nTHÌ ticket được tạo và tôi nhận mã tra cứu trong vòng 5 phút",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),

    ("RM-013","","Camera",
     "Chính sách GTBB tặng thiết bị Cam & Cloud",
     "Là khách hàng tham gia chương trình Giới thiệu bạn bè Camera FPT, tôi muốn nhận thiết bị Camera và gói Cloud làm phần thưởng khi giới thiệu thành công, để có thêm lợi ích thực sự.",
     "CHO TRƯỚC tôi đã giới thiệu thành công 1 khách hàng mới đăng ký Camera\nKHI điều kiện chính sách được đáp ứng\nTHÌ hệ thống tự động tạo lệnh thưởng thiết bị/cloud cho tôi\n\nKHI phần thưởng được xử lý\nTHÌ tôi nhận thông báo và thông tin bàn giao trong vòng 5 ngày làm việc",
     "High","5","","","",
     "Chưa tiếp nhận yêu cầu","Roadmap 18.5",""),
]

# ── Row config ────────────────────────────────────────────────────────────────
DATA_START = 3
DATA_LAST  = DATA_START + len(BACKLOG) - 1
N_BF       = sum(1 for t in BACKLOG if t[0].startswith("BF"))
N_RM       = sum(1 for t in BACKLOG if t[0].startswith("RM"))

# Column indices (0-based)
# A  B   C     D          E         F            G   H   I    J       K       L           M       N
# #  ID  Epic  EpicName   USTitle   UserStory    AC  SP  TL   TLISC   PIC_BA  TrangThai   Nguon   GhiChu
COL_TT  = 11   # Trạng thái
COL_NG  = 12   # Nguồn
COL_GC  = 13   # Ghi chú


def build():
    wb = xlsxwriter.Workbook(OUTPUT)

    # ── Format helper ─────────────────────────────────────────────────────
    def fmt(**kw):
        base = dict(font_name="Times New Roman", font_size=11,
                    valign="vcenter", text_wrap=True)
        base.update(kw)
        return wb.add_format(base)

    hdr_or  = fmt(bold=True, font_size=12, font_color="#FFFFFF",
                  bg_color="#E86A23", align="center", border=1)
    hdr_dk  = fmt(bold=True, font_size=10, font_color="#FFFFFF",
                  bg_color="#1F2737", align="center", border=1)

    c_base  = fmt(border=1, border_color="#DDDDDD")
    c_alt   = fmt(border=1, border_color="#DDDDDD", bg_color="#F0F7FF")
    c_ctr   = fmt(align="center", border=1, border_color="#DDDDDD")
    c_ctr_a = fmt(align="center", border=1, border_color="#DDDDDD", bg_color="#F0F7FF")
    c_bold  = fmt(bold=True, border=1, border_color="#DDDDDD")
    c_bold_a= fmt(bold=True, border=1, border_color="#DDDDDD", bg_color="#F0F7FF")
    c_empty = fmt(border=1, italic=True, font_color="#BBBBBB", bg_color="#F5F5F5")
    c_emp_a = fmt(border=1, italic=True, font_color="#BBBBBB", bg_color="#EBEBEB")
    c_note  = fmt(border=1, border_color="#DDDDDD", bg_color="#FFFDE7",
                  font_color="#5D4037")
    c_note_a= fmt(border=1, border_color="#DDDDDD", bg_color="#FFF9C4",
                  font_color="#5D4037")

    id_bf   = fmt(bold=True, font_color="#1E4D8C", align="center",
                  border=1, bg_color="#EBF5FB")
    id_bf_a = fmt(bold=True, font_color="#1E4D8C", align="center",
                  border=1, bg_color="#D6EAF8")
    id_rm   = fmt(bold=True, font_color="#6C3483", align="center",
                  border=1, bg_color="#F5EEF8")
    id_rm_a = fmt(bold=True, font_color="#6C3483", align="center",
                  border=1, bg_color="#EBE0F5")

    high_f  = fmt(bold=True, font_color="#FFFFFF", bg_color="#C0392B",
                  align="center", border=1)
    med_f   = fmt(bold=True, font_color="#FFFFFF", bg_color="#E67E22",
                  align="center", border=1)
    low_f   = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60",
                  align="center", border=1)
    emp_pf  = fmt(font_color="#AAAAAA", align="center", border=1)

    sp_f    = fmt(bold=True, font_size=12, align="center",
                  border=1, bg_color="#FEF9E7")
    sp_fa   = fmt(bold=True, font_size=12, align="center",
                  border=1, bg_color="#FDF2E9")

    src_bf  = fmt(bold=True, font_color="#1E4D8C", align="center",
                  bg_color="#EBF5FB", border=1, font_size=9)
    src_rm  = fmt(bold=True, font_color="#6C3483", align="center",
                  bg_color="#F5EEF8", border=1, font_size=9)

    # ── Trạng thái formats (màu theo từng giai đoạn) ──────────────────────
    TT_COLORS = {
        "Chưa tiếp nhận yêu cầu": ("#AAAAAA", "#F5F5F5"),
        "Đã tiếp nhận yêu cầu":   ("#1E4D8C", "#EBF5FB"),
        "Đang phân tích":          ("#7D6608", "#FEF9E7"),
        "Đang trao đổi PBLQ":      ("#784212", "#FDEBD0"),
        "Đã bàn giao ISC":         ("#1A5276", "#D6EAF8"),
        "In Progress DEV":          ("#E67E22", "#FFF3E0"),
        "UAT":                      ("#1E8449", "#EAFAF1"),
        "Done":                     ("#FFFFFF", "#27AE60"),
    }
    tt_fmts = {}
    for label, (fc, bg) in TT_COLORS.items():
        tt_fmts[label] = fmt(bold=True, font_color=fc, bg_color=bg,
                             align="center", border=1, font_size=10)

    def st_fmt(s):
        return tt_fmts.get(s, fmt(font_color="#AAAAAA", align="center", border=1))

    def id_fmt(oid, alt):
        return (id_bf_a if alt else id_bf) if oid.startswith("BF") \
               else (id_rm_a if alt else id_rm)

    def prio_fmt(p):
        return {"High": high_f, "Medium": med_f, "Low": low_f}.get(p, emp_pf)

    # ── Config sheet (ẩn) chứa list dropdown ─────────────────────────────
    ws_cfg = wb.add_worksheet("_Config")
    ws_cfg.hide()
    for i, val in enumerate(TRANG_THAI):
        ws_cfg.write(i, 0, val)
    # Named range = Config!$A$1:$A$8
    cfg_range = f"_Config!$A$1:$A${len(TRANG_THAI)}"

    n   = len(BACKLOG)
    d1  = DATA_START + 1
    d2  = DATA_LAST  + 1

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 1 — Cover
    # ════════════════════════════════════════════════════════════════════════
    meta_lbl= fmt(bold=True, font_color="#FFFFFF", bg_color="#E86A23",
                  align="center", border=1)
    meta_val= fmt(bg_color="#FFF8F4", border=1)
    meta_fml= fmt(bold=True, font_color="#E86A23", bg_color="#FFF0E8",
                  align="center", border=1, font_size=13)
    title_f = fmt(bold=True, font_size=20, font_color="#E86A23", align="center")
    sub_f   = fmt(bold=True, font_size=13, font_color="#1F2737",  align="center")
    div_f   = wb.add_format({"bg_color": "#E86A23"})
    note_f  = fmt(font_size=9, font_color="#888888", align="center")

    cv = wb.add_worksheet("📋 Cover")
    cv.hide_gridlines(2)
    cv.set_column("A:A", 3); cv.set_column("B:G", 19)
    cv.set_row(2, 50); cv.set_row(3, 30); cv.set_row(5, 8)
    cv.merge_range("B3:G3", "PRODUCT BACKLOG — FPT TELECOM", title_f)
    cv.merge_range("B4:G4", "Hệ thống FPT.vn / HiFPT  |  Đội Product", sub_f)
    cv.merge_range("B6:G6", "", div_f)

    for r, l1, v1, l2, v2 in [
        (8,  "Đơn vị",     "FPT Telecom — Đội Product",   "Hệ thống",   "FPT.vn / HiFPT"),
        (9,  "Nguồn data", "Backlog FPTvn + Roadmap 18.5", "Ngày tạo",   "28/06/2026"),
        (10, "Author",     "Product Owner / BA",            "Trạng thái", "Draft v1.1"),
    ]:
        cv.set_row(r, 22)
        cv.write(r, 1, l1, meta_lbl); cv.merge_range(r, 2, r, 3, v1, meta_val)
        cv.write(r, 4, l2, meta_lbl); cv.merge_range(r, 5, r, 6, v2, meta_val)

    for r in [11, 12, 13, 14, 15]: cv.set_row(r, 28)

    # Công thức tự động — tham chiếu cột L (Trạng thái) và M (Nguồn)
    def formula_row(row, lbl1, f1, lbl2, f2):
        cv.write(row, 1, lbl1, meta_lbl)
        cv.write_formula(row, 2, f1, meta_fml)
        cv.merge_range(row, 2, row, 3, f1, meta_fml)
        cv.write(row, 4, lbl2, meta_lbl)
        cv.write_formula(row, 5, f2, meta_fml)
        cv.merge_range(row, 5, row, 6, f2, meta_fml)

    formula_row(11,
        "Tổng Task Backlog",
        f"=COUNTA('📌 Product Backlog'!A{d1}:A{d2})",
        "Tổng SP",
        f"=SUM('📌 Product Backlog'!H{d1}:H{d2})")

    formula_row(12,
        "Backlog FPTvn",
        f"=COUNTIF('📌 Product Backlog'!M{d1}:M{d2},\"Backlog FPTvn\")",
        "Roadmap 18.5",
        f"=COUNTIF('📌 Product Backlog'!M{d1}:M{d2},\"Roadmap 18.5\")")

    formula_row(13,
        "Chưa tiếp nhận",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Chưa tiếp nhận yêu cầu\")",
        "Đã tiếp nhận",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Đã tiếp nhận yêu cầu\")")

    formula_row(14,
        "Đang phân tích / Trao đổi",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Đang phân tích\")"
        f"+COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Đang trao đổi PBLQ\")",
        "Đã bàn giao ISC / DEV",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Đã bàn giao ISC\")"
        f"+COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"In Progress DEV\")")

    formula_row(15,
        "UAT",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"UAT\")",
        "Done",
        f"=COUNTIF('📌 Product Backlog'!L{d1}:L{d2},\"Done\")")

    cv.merge_range("B18:G18",
        "* Các ô màu cam tự động cập nhật khi thêm/sửa dữ liệu. "
        "Cột Trạng thái có trình thả xuống — chọn từ danh sách 8 giai đoạn.",
        note_f)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 2 — Product Backlog
    # Columns (14 cột A–N):
    # A:#  B:ID  C:Epic  D:EpicName  E:USTitle  F:UserStory  G:AC
    # H:SP  I:TL  J:TLISC  K:PIC_BA  L:TrangThai  M:Nguon  N:GhiChu
    # ════════════════════════════════════════════════════════════════════════
    ws = wb.add_worksheet("📌 Product Backlog")
    ws.hide_gridlines(2)
    ws.freeze_panes(3, 0)
    ws.set_zoom(80)

    col_widths = [4, 8, 6, 16, 22, 33, 33, 5, 11, 11, 13, 22, 13, 26]
    for i, w in enumerate(col_widths):
        ws.set_column(i, i, w)

    ws.set_row(0, 34)
    ws.merge_range("A1:N1",
        "PRODUCT BACKLOG — FPT TELECOM  |  FPT.vn & HiFPT  |  Loại trừ: Done",
        hdr_or)

    ws.set_row(1, 6)
    ws.set_row(2, 32)
    headers = [
        "#", "ID", "Epic\n(để trống)", "Epic Name\n(Sản phẩm)",
        "US Title\n(Đầu mục công việc)",
        "User Story\n(thuần Việt)",
        "Acceptance Criteria\n(CHO TRƯỚC / KHI / THÌ)",
        "SP",
        "Timeline\nmong muốn",
        "Timeline\nISC",
        "PIC\n(BA)",
        "Trạng thái ▼",
        "Nguồn",
        "Ghi chú",
    ]
    for ci, h in enumerate(headers):
        ws.write(2, ci, h, hdr_dk)

    for idx, (oid, epic, epic_name, us_title, us, ac,
              prio, sp, tl, tl_isc, pic_ba,
              trang_thai, nguon, ghi_chu) in enumerate(BACKLOG):
        r   = idx + DATA_START
        alt = (idx % 2 == 1)
        ws.set_row(r, 85)

        ws.write(r,  0, idx + 1,   c_ctr_a if alt else c_ctr)
        ws.write(r,  1, oid,       id_fmt(oid, alt))
        ws.write(r,  2, epic,      c_emp_a if alt else c_empty)
        ws.write(r,  3, epic_name, c_alt   if alt else c_base)
        ws.write(r,  4, us_title,  c_bold_a if alt else c_bold)
        ws.write(r,  5, us,        c_alt   if alt else c_base)
        ws.write(r,  6, ac,        c_alt   if alt else c_base)
        ws.write(r,  7, int(sp),   sp_fa   if alt else sp_f)
        ws.write(r,  8, tl,        c_ctr_a if alt else c_ctr)
        ws.write(r,  9, tl_isc,    c_ctr_a if alt else c_ctr)
        ws.write(r, 10, pic_ba,    c_ctr_a if alt else c_ctr)
        ws.write(r, 11, trang_thai, st_fmt(trang_thai))
        ws.write(r, 12, nguon,     src_rm if "Roadmap" in nguon else src_bf)
        ws.write(r, 13, ghi_chu,   c_note_a if alt else c_note)

    # ── Dropdown validation cho cột L (Trạng thái) ───────────────────────
    ws.data_validation(
        DATA_START, COL_TT,        # first row/col
        DATA_LAST,  COL_TT,        # last row/col
        {
            "validate": "list",
            "source":   cfg_range,
            "input_title":   "Chọn trạng thái",
            "input_message": "\n".join(TRANG_THAI),
            "error_title":   "Giá trị không hợp lệ",
            "error_message": "Vui lòng chọn từ danh sách.",
        }
    )

    # ── Tổng ─────────────────────────────────────────────────────────────
    sum_r = DATA_LAST + 2
    sf    = fmt(bold=True, font_color="#FFFFFF", bg_color="#1F2737",
                align="center", border=1)
    ws.set_row(sum_r, 24)
    ws.merge_range(sum_r, 0, sum_r, 6, "TỔNG", sf)
    ws.write_formula(sum_r,  7, f"=SUM(H{d1}:H{d2})", sf)
    ws.write_formula(sum_r,  8, f"=COUNTA(A{d1}:A{d2})&\" tasks\"", sf)
    for ci in range(9, 14):
        ws.write(sum_r, ci, "", sf)

    # ── Legend ────────────────────────────────────────────────────────────
    leg = sum_r + 2
    ws.set_row(leg, 20)
    ws.write(leg, 0, "Chú thích:", fmt(bold=True, font_size=10))
    ws.write(leg, 1, "BF-xxx = Backlog FPTvn", src_bf)
    ws.write(leg, 2, "RM-xxx = Roadmap 18.5",  src_rm)
    ws.write(leg, 3, "Cột L: Trạng thái có trình thả xuống — click ô để chọn",
             fmt(font_size=9, font_color="#555555", italic=True))
    ws.write(leg, 6, "Epic: để trống — PO/BA tự điền",
             fmt(font_size=9, font_color="#888888", italic=True))

    # ── Trạng thái color legend ───────────────────────────────────────────
    leg2 = leg + 1
    ws.set_row(leg2, 18)
    for ci, (label, (fc, bg)) in enumerate(TT_COLORS.items()):
        if ci >= 14: break
        ws.write(leg2, ci, label,
                 fmt(bold=True, font_color=fc, bg_color=bg,
                     align="center", border=1, font_size=8))

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 3 — Definition of Done
    # ════════════════════════════════════════════════════════════════════════
    ws_dod = wb.add_worksheet("✅ Definition of Done")
    ws_dod.hide_gridlines(2)
    ws_dod.set_column("A:A", 6)
    ws_dod.set_column("B:B", 72)
    ws_dod.set_column("C:C", 22)
    ws_dod.set_row(0, 30)
    ws_dod.merge_range("A1:C1",
        "DEFINITION OF DONE (DoD) — FPT TELECOM | ĐỘI PRODUCT", hdr_or)
    ws_dod.set_row(1, 22)
    ws_dod.write(1, 0, "#",                   hdr_dk)
    ws_dod.write(1, 1, "Tiêu chí nghiệm thu", hdr_dk)
    ws_dod.write(1, 2, "Loại kiểm tra",        hdr_dk)

    dod_items = [
        ("Yêu cầu đã được BA/PO xác nhận và sign-off trước khi dev",     "BA Sign-off"),
        ("Acceptance Criteria đã pass toàn bộ (manual hoặc automated)",  "AC Verification"),
        ("Code đã được review bởi ít nhất 1 thành viên khác",            "Code Review"),
        ("Không có bug P1/P2 mở tại thời điểm demo",                     "QA Testing"),
        ("UI đã được kiểm tra trên Chrome, Safari, Firefox (responsive)", "UI/Cross-browser"),
        ("Tài liệu kỹ thuật (API, flow) được cập nhật nếu có thay đổi",  "Documentation"),
        ("Timeline ISC được xác nhận và đồng bộ với bên ISC",            "ISC Sync"),
    ]
    dck  = fmt(bold=True, font_color="#FFFFFF", bg_color="#27AE60",
               align="center", border=1)
    for i, (item, dtype) in enumerate(dod_items):
        r   = i + 2
        alt = (i % 2 == 1)
        ws_dod.set_row(r, 26)
        ws_dod.write(r, 0, f"✓ {i+1}", dck)
        ws_dod.write(r, 1, item,
                     fmt(border=1) if alt else fmt(border=1, bg_color="#F9F9F9"))
        ws_dod.write(r, 2, dtype,
                     fmt(align="center", font_color="#1A7A1A", border=1,
                         bg_color="#D5ECD5" if alt else "#EAF4EA"))

    wb.close()
    print(f"✅ Saved: {OUTPUT}")
    print(f"   Tasks: {n} ({N_BF} BF + {N_RM} RM)")
    print(f"   Columns: 14 (A–N) | Dropdown Trạng thái: {len(TRANG_THAI)} giá trị")


if __name__ == "__main__":
    build()

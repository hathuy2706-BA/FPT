#!/usr/bin/env python3
"""Generate Product Backlog Excel — chuẩn FPT.
   Import task vận hành từ Backlog FPTvn & Roadmap 18.5 vào sheet Product Backlog chính."""

import xlsxwriter

OUTPUT = "/Users/hathuy/Documents/FPT-1/backlogpo/product_backlog_team.xlsx"

# ── Task vận hành import (EPIC để trống, US Title = Đầu mục công việc, US/AC thuần Việt) ──
# Columns: id, epic_id, epic_name, us_title, user_story, ac, priority, sp, sprint, status, nguon
IMPORTED = [
    # ── Backlog FPTvn ─────────────────────────────────────────────────────
    ("BF-001","","Camera",
     "Hiển thị giá Cloud Camera theo gói buffet",
     "Là khách hàng mua Camera FPT, tôi muốn xem giá cloud hiển thị dạng gói buffet (50.000đ/tháng) thay vì chia theo số mắt camera, để dễ so sánh và quyết định mua.",
     "CHO TRƯỚC tôi ở trang thanh toán Camera\nKHI tôi xem phần chọn gói cloud\nTHÌ giá hiển thị 50.000đ/tháng dạng buffet, không chia theo từng mắt camera",
     "High","5","Sprint hiện tại","To Do","Backlog FPTvn"),
    ("BF-002","","Camera",
     "Cập nhật giao diện thanh toán Camera – gói cloud 3D buffet",
     "Là khách hàng mua Camera FPT, tôi muốn giao diện trang thanh toán hiển thị đúng gói cloud (bỏ nhãn 'x5') và ẩn phí lắp đặt khi chọn tự lắp, để tránh nhầm lẫn và tăng tỷ lệ chuyển đổi.",
     "CHO TRƯỚC tôi ở trang thanh toán Camera\nKHI tôi chọn gói cloud 3D buffet 6 tháng\nTHÌ nhãn 'x5' không hiển thị\n\nCHO TRƯỚC tôi chọn hình thức Tự lắp đặt\nTHÌ dòng phí lắp đặt bị ẩn hoàn toàn",
     "High","5","Sprint hiện tại","In Progress","Backlog FPTvn"),
    ("BF-003","","Internet",
     "Cập nhật trang địa phương theo giao diện mới",
     "Là quản trị viên nội dung CMS, tôi muốn các trang địa phương (/lap-internet-wifi-hcm…) được chuyển sang nền tảng UI mới để thêm/chỉnh sửa section linh hoạt, chuẩn hoá breadcrumb và Heading 1.",
     "CHO TRƯỚC tôi đăng nhập CMS\nKHI tôi mở trang địa phương dạng /lap-internet-wifi-[tinh]\nTHÌ giao diện mới hiển thị và tôi có thể thêm section mới\n\nCHO TRƯỚC tôi lưu thay đổi\nTHÌ nội dung hiển thị đúng trên FE, không lỗi layout",
     "High","5","Sprint hiện tại","To Do","Backlog FPTvn"),
    ("BF-004","","Internet",
     "Luồng nâng cấp 5 dịch vụ trên FPT.vn",
     "Là khách hàng FPT đang sử dụng dịch vụ, tôi muốn nâng cấp các dịch vụ (VVIP, Camera, AP, băng thông, wifi6) trực tiếp trên FPT.vn, để hoàn tất nâng cấp mà không cần gọi tổng đài.",
     "CHO TRƯỚC tôi đăng nhập tài khoản FPT\nKHI tôi vào trang /nang-cap\nTHÌ hiển thị 5 dịch vụ có thể nâng cấp kèm giá\n\nKHI tôi chọn nâng cấp và xác nhận\nTHÌ đơn hàng được tạo và tôi nhận thông báo xác nhận",
     "High","5","Sprint hiện tại","In Progress","Backlog FPTvn"),
    ("BF-005","","Internet",
     "LDP FCM",
     "Là khách hàng tiềm năng sử dụng FCM, tôi muốn truy cập trang landing page FCM đầy đủ thông tin gói cước và nút đăng ký, để đăng ký dịch vụ nhanh chóng.",
     "CHO TRƯỚC tôi truy cập URL LDP FCM\nKHI trang tải xong\nTHÌ hiển thị đầy đủ thông tin gói cước, hình ảnh và nút CTA đăng ký\n\nKHI tôi nhấn đăng ký\nTHÌ điều hướng đúng đến luồng mua",
     "Medium","3","Sprint hiện tại","In Progress","Backlog FPTvn"),
    ("BF-006","","",
     "CMS Tổng đài wifi – 5 mẫu LDP",
     "Là người quản trị nội dung, tôi muốn có 5 mẫu Landing Page cho tổng đài wifi trên CMS, để team content tự thiết kế và triển khai campaign mà không cần lập trình viên.",
     "CHO TRƯỚC tôi đăng nhập CMS\nKHI tôi chọn Tạo LDP mới\nTHÌ có 5 mẫu template sẵn để chọn\n\nKHI tôi publish LDP\nTHÌ trang hiển thị đúng trên FE",
     "High","5","Backlog","","Backlog FPTvn"),
    ("BF-007","","Camera",
     "Bổ sung luồng giao hàng Camera trong LDP nâng cấp",
     "Là khách hàng nâng cấp Camera FPT, tôi muốn có tùy chọn giao hàng Camera trong luồng nâng cấp trên LDP, để hoàn tất đơn nâng cấp và nhận thiết bị mà không cần liên hệ riêng.",
     "CHO TRƯỚC tôi ở LDP nâng cấp Camera\nKHI tôi chọn gói nâng cấp\nTHÌ xuất hiện tùy chọn Giao hàng tận nơi hoặc Tự lắp đặt\n\nKHI tôi chọn giao hàng và điền địa chỉ\nTHÌ đơn hàng xác nhận với thông tin giao hàng đầy đủ",
     "High","5","Sprint hiện tại","In Progress","Backlog FPTvn"),
    ("BF-008","","Internet",
     "LDP FCitizen – trang dành riêng cho FPTers",
     "Là nhân viên FPT (FPTer), tôi muốn truy cập trang landing page riêng cho FCitizen hiển thị gói cước ưu đãi và quy trình đăng ký nội bộ, để đăng ký dịch vụ với mức giá ưu đãi dành riêng.",
     "CHO TRƯỚC tôi truy cập trang FCitizen\nKHI tôi chưa xác thực là FPTer\nTHÌ hệ thống yêu cầu xác thực email @fpt.com.vn\n\nKHI xác thực thành công\nTHÌ hiển thị các gói cước ưu đãi dành riêng cho FPTers",
     "High","5","Backlog","To Do","Backlog FPTvn"),
    ("BF-009","","Camera",
     "Exit-intent popup trang Camera",
     "Là khách hàng đang rời trang Camera FPT, tôi muốn thấy popup ưu đãi cuối cùng trước khi thoát trang, để có thêm cơ hội xem ưu đãi và quyết định đăng ký.",
     "CHO TRƯỚC tôi đang xem trang /camera trên máy tính\nKHI con trỏ di chuyển ra phía thanh điều hướng trình duyệt\nTHÌ popup exit-intent xuất hiện sau 300ms\n\nCHO TRƯỚC tôi dùng điện thoại\nKHI tôi scroll lên nhanh\nTHÌ popup hiện lên; chỉ hiện tối đa 1 lần/phiên",
     "High","5","Sprint tiếp theo","","Backlog FPTvn"),
    ("BF-010","","Internet",
     "Tích hợp API Giá Vàng & Điểm thi Đại học (Always-on)",
     "Là người dùng FPT.vn, tôi muốn xem thông tin giá vàng SJC/9999 và điểm thi đại học theo thời gian thực ngay trên website, để tra cứu nhanh mà không cần rời trang.",
     "CHO TRƯỚC widget giá vàng được kích hoạt\nKHI tôi mở trang chứa widget\nTHÌ dữ liệu giá vàng cập nhật trong vòng 5 phút\n\nCHO TRƯỚC API ngừng hoạt động\nTHÌ widget hiển thị Đang cập nhật thay vì lỗi",
     "Low","2","Backlog","","Backlog FPTvn"),
    ("BF-011","","Camera",
     "Trang Author Profile Chuyên gia Camera FPT",
     "Là khách hàng tìm hiểu Camera FPT, tôi muốn xem trang giới thiệu chuyên gia kỹ thuật (ảnh, tên, chức vụ, chứng chỉ), để tin tưởng hơn vào chất lượng sản phẩm và dịch vụ.",
     "CHO TRƯỚC tôi truy cập /tac-gia/chuyen-gia-ky-thuat\nKHI trang tải xong\nTHÌ hiển thị 3–5 thẻ profile chuyên gia với ảnh thực, tên, chức vụ và chứng chỉ\n\nCHO TRƯỚC trang được lập index SEO\nTHÌ có schema markup dạng Person",
     "Medium","3","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-012","","Internet/SA",
     "LDP Ngoại Hạng Anh (NHA)",
     "Là người hâm mộ bóng đá dùng gói SA Play FPT, tôi muốn truy cập trang tổng hợp NHA xem kết quả và bảng xếp hạng cập nhật tự động, để theo dõi giải đấu mà không cần tìm nhiều nơi.",
     "CHO TRƯỚC tôi truy cập /ngoai-hang-anh\nKHI trang tải xong\nTHÌ hiển thị bảng xếp hạng và kết quả trận đấu gần nhất từ API\n\nCHO TRƯỚC tỷ số thay đổi sau trận\nTHÌ dữ liệu tự cập nhật trong vòng 30 phút",
     "Low","2","Backlog","","Backlog FPTvn"),
    ("BF-013","","Internet/SA",
     "Video Hub – Block video tự động từ FPT Play",
     "Là người dùng FPT.vn quan tâm nội dung thể thao, tôi muốn xem block video Recap/Highlight tự động cập nhật từ YouTube FPT Play ngay trên website, để không cần chuyển sang YouTube.",
     "CHO TRƯỚC block Video Hub được nhúng vào trang\nKHI tôi mở trang\nTHÌ hiển thị tối đa 6 video mới nhất từ kênh YouTube FPT Play\n\nKHI tôi nhấn vào video\nTHÌ phát inline không chuyển trang; video lazy-load không ảnh hưởng LCP",
     "Medium","3","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-014","","Internet",
     "Bảng giá gói cước theo ID trên trang tin tức",
     "Là người quản trị nội dung, tôi muốn gắn thành phần bảng giá gói cước theo ID vào bài viết, để giá hiển thị tự động cập nhật theo hệ thống mà không cần chỉnh sửa thủ công từng bài.",
     "CHO TRƯỚC tôi chèn shortcode [goi-cuoc id=X] vào bài viết CMS\nKHI trang tin tức tải\nTHÌ hiển thị đúng tên gói, giá và mô tả ngắn từ hệ thống\n\nKHI gói cước thay đổi giá trong hệ thống\nTHÌ bài viết tự động hiển thị giá mới",
     "High","5","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-015","","Internet",
     "Banner thay đổi nhanh bằng shortcode trên trang tin tức",
     "Là người quản trị nội dung, tôi muốn thay đổi banner khuyến mại trong bài viết tin tức bằng shortcode thay vì chỉnh từng bài, để cập nhật nhanh khi chương trình kết thúc.",
     "CHO TRƯỚC tôi chèn shortcode banner vào bài viết\nKHI chương trình khuyến mại kết thúc\nTHÌ tôi chỉ cần cập nhật 1 nơi và tất cả bài dùng shortcode đó tự cập nhật\n\nCHO TRƯỚC shortcode được cấu hình\nTHÌ banner hỗ trợ hiển thị ảnh và link điều hướng",
     "High","5","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-016","","Camera",
     "Luồng LDP Nâng cấp Cam 200K – tối ưu thanh toán",
     "Là khách hàng Camera FPT muốn nâng cấp lên gói 200K, tôi muốn hoàn tất thanh toán ngay trên FPT.vn mà không bị chuyển hướng ra ngoài hoặc gặp lỗi, để việc nâng cấp diễn ra liền mạch.",
     "CHO TRƯỚC tôi ở LDP nâng cấp Camera\nKHI tôi chọn gói 200K và nhấn thanh toán\nTHÌ không bị chuyển hướng sang trang ngoài\n\nKHI thanh toán thành công\nTHÌ hiển thị trang xác nhận với thông tin đơn hàng và thời gian kích hoạt",
     "High","5","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-017","","Camera",
     "Luồng Mua mới Camera – sửa đứt gãy tại bước thanh toán",
     "Là khách hàng mua mới Camera FPT, tôi muốn hoàn tất thanh toán mà không bị gián đoạn ở bước cuối, để đơn hàng được xử lý và nhận xác nhận ngay.",
     "CHO TRƯỚC tôi đã chọn camera và điền thông tin\nKHI tôi nhấn Xác nhận thanh toán\nTHÌ hệ thống xử lý và chuyển sang trang thành công\n\nCHO TRƯỚC xảy ra lỗi kỹ thuật\nTHÌ hệ thống hiển thị thông báo lỗi rõ ràng và cho phép thử lại",
     "High","5","Sprint hiện tại","","Backlog FPTvn"),
    ("BF-018","","Camera",
     "Luồng Mua mới Camera – bổ sung giỏ hàng combo",
     "Là khách hàng mua Camera FPT, tôi muốn chọn đồng thời nhiều loại camera (ngoài trời + trong nhà) trong cùng một đơn hàng, để mua combo tiện lợi mà không cần đặt nhiều đơn riêng.",
     "CHO TRƯỚC tôi đang ở trang chọn Camera\nKHI tôi thêm camera ngoài trời vào giỏ\nTHÌ hệ thống cho phép tiếp tục thêm camera trong nhà\n\nKHI tôi vào giỏ hàng\nTHÌ hiển thị đầy đủ cả 2 sản phẩm với giá tổng chính xác",
     "High","5","Sprint hiện tại","","Backlog FPTvn"),
    # ── Roadmap 18.5 ─────────────────────────────────────────────────────
    ("RM-001","","Camera",
     "Luồng bán Camera chỉ giao hàng – Sàn TMĐT",
     "Là khách hàng mua Camera FPT qua sàn TMĐT, tôi muốn thực hiện luồng mua hàng chỉ giao hàng (không bao gồm lắp đặt), để nhận thiết bị nhanh chóng và tự lắp đặt.",
     "CHO TRƯỚC tôi chọn mua Camera trên sàn TMĐT\nKHI tôi chọn hình thức Chỉ giao hàng\nTHÌ hệ thống không yêu cầu đặt lịch lắp đặt\n\nKHI đơn được tạo\nTHÌ trạng thái chuyển sang Đang xử lý giao hàng và tôi nhận thông báo",
     "High","5","Sprint hiện tại","In Progress","Roadmap 18.5"),
    ("RM-002","","Internet",
     "LDP FCitizen – UI/UX & cập nhật chính sách gói bán",
     "Là nhân viên FPT (FPTer), tôi muốn truy cập trang FCitizen tại fpt.vn/fcitizen với giao diện mới và chính sách gói bán được cập nhật, để biết chính xác quyền lợi và đăng ký đúng chính sách.",
     "CHO TRƯỚC tôi truy cập fpt.vn/fcitizen\nKHI trang tải\nTHÌ giao diện mới hiển thị đúng design\n\nCHO TRƯỚC chính sách gói bán được cập nhật\nTHÌ thông tin trên trang phản ánh đúng, không lệch với hệ thống backend",
     "Medium","3","Backlog","To Do","Roadmap 18.5"),
    ("RM-003","","Nâng cấp/bán thêm",
     "Luồng nâng cấp 5 Dịch vụ – FPT.vn",
     "Là khách hàng FPT muốn bổ sung hoặc nâng cấp dịch vụ, tôi muốn thực hiện luồng nâng cấp 5 loại dịch vụ trực tiếp trên FPT.vn, để hoàn tất mà không phải liên hệ tổng đài.",
     "CHO TRƯỚC tôi đang đăng nhập trên FPT.vn\nKHI tôi vào trang nâng cấp\nTHÌ hiển thị đủ 5 dịch vụ với chính sách giá rõ ràng\n\nKHI tôi hoàn tất nâng cấp\nTHÌ nhận xác nhận và dịch vụ được kích hoạt trong vòng 24 giờ",
     "Medium","3","Sprint hiện tại","","Roadmap 18.5"),
    ("RM-004","","Giới thiệu bạn bè",
     "Hub vinh danh Giới thiệu bạn bè trên App HiFPT",
     "Là khách hàng tham gia chương trình Giới thiệu bạn bè, tôi muốn xem trang vinh danh thành tích (Cơ bản/Bạc/Vàng/Kim cương) trên App HiFPT, để được ghi nhận và có thêm động lực giới thiệu.",
     "CHO TRƯỚC tôi mở App HiFPT và đã tham gia GTBB\nKHI tôi vào mục Vinh danh\nTHÌ hiển thị level hiện tại, số người đã giới thiệu và phần thưởng\n\nCHO TRƯỚC tôi đạt đủ điều kiện lên level mới\nTHÌ hệ thống gửi thông báo chúc mừng",
     "Medium","3","Sprint hiện tại","","Roadmap 18.5"),
    ("RM-005","","Giới thiệu bạn bè",
     "LDP Giới thiệu bạn bè – Người được giới thiệu",
     "Là người được bạn bè giới thiệu đến FPT, tôi muốn truy cập trang landing page riêng giải thích ưu đãi và hướng dẫn đăng ký, để hiểu ngay quyền lợi và hoàn tất đăng ký nhanh chóng.",
     "CHO TRƯỚC tôi nhấn link giới thiệu từ bạn\nKHI trang LDP tải\nTHÌ hiển thị tên người giới thiệu, ưu đãi áp dụng và nút đăng ký\n\nKHI tôi đăng ký thành công\nTHÌ hệ thống ghi nhận mã giới thiệu và cả hai bên nhận thưởng theo chính sách",
     "Medium","3","Sprint tiếp theo","","Roadmap 18.5"),
    ("RM-006","","Thanh toán",
     "Tích hợp Auto Pay trên website FPT.vn",
     "Là khách hàng đăng ký dịch vụ FPT định kỳ, tôi muốn lưu thẻ và kích hoạt tự động gia hạn trên FPT.vn, để không bị gián đoạn dịch vụ do quên thanh toán.",
     "CHO TRƯỚC tôi đăng nhập FPT.vn\nKHI tôi vào cài đặt thanh toán và thêm thẻ\nTHÌ thẻ được mã hóa và lưu an toàn\n\nKHI đến kỳ gia hạn\nTHÌ hệ thống tự trừ tiền và gửi thông báo; khi thanh toán thất bại tôi nhận cảnh báo trong vòng 24 giờ",
     "Medium","3","Sprint hiện tại","","Roadmap 18.5"),
    ("RM-007","","SA Play",
     "Gửi E-Card khi khách hàng mua gói SA Play",
     "Là khách hàng mua gói SA Play trên FPT.vn hoặc HiFPT, tôi muốn gửi E-Card kỹ thuật số cho bạn bè sau khi mua gói, để bạn tôi tự kích hoạt dịch vụ một cách tiện lợi.",
     "CHO TRƯỚC tôi mua gói SA Play và chọn hình thức Tặng bạn bè\nKHI thanh toán thành công\nTHÌ hệ thống gửi E-Card qua email/SMS cho người nhận\n\nKHI người nhận nhấn kích hoạt\nTHÌ mã được ghi nhận và dịch vụ kích hoạt cho tài khoản họ",
     "Medium","3","Sprint hiện tại","","Roadmap 18.5"),
    ("RM-008","","Camera",
     "Landing Page Camera GenZ",
     "Là khách hàng trẻ (GenZ) quan tâm đến Camera FPT, tôi muốn trải nghiệm trang landing page phong cách GenZ hiển thị sản phẩm, giá và ưu đãi nổi bật, để dễ dàng quyết định đăng ký.",
     "CHO TRƯỚC tôi truy cập LDP Camera GenZ\nKHI trang tải\nTHÌ giao diện hiển thị đúng concept GenZ, tải trong dưới 3 giây\n\nKHI tôi nhấn Đăng ký ngay\nTHÌ chuyển đúng đến luồng mua và chính sách được áp dụng đầy đủ",
     "High","5","Sprint hiện tại","","Roadmap 18.5"),
    ("RM-009","","Internet",
     "Luồng Recall – tái kết nối khách hàng cũ",
     "Là khách hàng FPT đã từng dừng sử dụng dịch vụ, tôi muốn nhận đề xuất kích hoạt lại dịch vụ phù hợp qua FPT.vn hoặc HiFPT, để quay lại sử dụng với ưu đãi tái kết nối.",
     "CHO TRƯỚC tôi thuộc tệp khách hàng Recall\nKHI tôi truy cập FPT.vn hoặc HiFPT\nTHÌ hệ thống hiển thị banner/popup đề xuất tái kết nối với gói phù hợp\n\nKHI tôi nhấn Đăng ký lại\nTHÌ luồng mua tự điền sẵn thông tin cũ",
     "High","5","Backlog","","Roadmap 18.5"),
    ("RM-010","","Internet",
     "Luồng Autocall – tích hợp ZNS nâng cấp/bán thêm",
     "Là người quản lý chiến dịch bán hàng FPT, tôi muốn tích hợp ZNS vào hệ thống Autocall để tiếp cận khách hàng hiện hữu nhằm nâng cấp hoặc bán thêm dịch vụ, để tỷ lệ tiếp cận tăng và chi phí SMS giảm.",
     "CHO TRƯỚC chiến dịch Autocall được cấu hình với ZNS\nKHI hệ thống gọi đến số điện thoại trong tệp data\nTHÌ tin ZNS được gửi khi cuộc gọi không bắt máy\n\nKHI khách hàng phản hồi ZNS\nTHÌ log được ghi nhận trong hệ thống CRM",
     "High","5","Backlog","","Roadmap 18.5"),
    ("RM-011","","Internet/SA",
     "Cross-sell FPTPlay.vn",
     "Là khách hàng Internet FPT, tôi muốn thấy đề xuất nâng cấp/thêm gói FPT Play khi duyệt FPT.vn, để biết về gói giải trí bổ sung và dễ dàng nâng cấp trong một giao dịch.",
     "CHO TRƯỚC tôi đang đăng nhập FPT.vn\nKHI tôi xem trang sản phẩm Internet\nTHÌ hiển thị block cross-sell gói SA Play với giá nâng cấp\n\nKHI tôi nhấn Thêm vào gói\nTHÌ gói SA Play được thêm vào đơn hàng hiện tại",
     "High","5","Backlog","","Roadmap 18.5"),
    ("RM-012","","Camera",
     "Self-Service Cam trên sàn TMĐT",
     "Là khách hàng mua Camera FPT qua sàn TMĐT, tôi muốn tự xử lý các yêu cầu sau mua (cài đặt, báo lỗi, gia hạn cloud) qua giao diện self-service, để không cần gọi hotline cho vấn đề đơn giản.",
     "CHO TRƯỚC tôi đã mua Camera FPT qua sàn\nKHI tôi vào khu vực quản lý đơn hàng\nTHÌ có tùy chọn Hỗ trợ kỹ thuật và Gia hạn Cloud\n\nKHI tôi gửi yêu cầu hỗ trợ\nTHÌ ticket được tạo và tôi nhận mã tra cứu trong vòng 5 phút",
     "High","5","Backlog","","Roadmap 18.5"),
    ("RM-013","","Camera",
     "Chính sách GTBB tặng thiết bị Cam & Cloud",
     "Là khách hàng tham gia chương trình Giới thiệu bạn bè Camera FPT, tôi muốn nhận thiết bị Camera và gói Cloud làm phần thưởng khi giới thiệu thành công, để có thêm lợi ích thực sự từ việc giới thiệu.",
     "CHO TRƯỚC tôi đã giới thiệu thành công 1 khách hàng mới đăng ký Camera\nKHI điều kiện chính sách được đáp ứng\nTHÌ hệ thống tự động tạo lệnh thưởng thiết bị/cloud cho tôi\n\nKHI phần thưởng được xử lý\nTHÌ tôi nhận thông báo và thông tin bàn giao trong vòng 5 ngày làm việc",
     "High","5","Backlog","","Roadmap 18.5"),
]

# ── Product Backlog gốc (US hệ thống Task Management) ─────────────────────────
BACKLOG_US = [
    ("US-001","EP01","Quản lý Task","Tạo task mới",
     "As a BA/PO, I want to create a new task with full details so that the team has a clear work item.",
     "GIVEN tôi ở trang Backlog\nWHEN tôi nhấn Tạo Task và điền đầy đủ các trường bắt buộc\nTHEN task được tạo với status To Do\n\nGIVEN tôi để trống Title\nWHEN tôi nhấn Lưu\nTHEN hệ thống báo lỗi Title không được để trống",
     "Must Have","3","Sprint 1","To Do"),
    ("US-002","EP01","Quản lý Task","Cập nhật trạng thái task (Kanban)",
     "As a team member, I want to drag & drop tasks across columns so that the team can visualize workflow.",
     "GIVEN task ở cột To Do\nWHEN tôi kéo sang In Progress\nTHEN task chuyển trạng thái và lưu timestamp\n\nGIVEN task chuyển sang Done\nTHEN hệ thống ghi nhận completion date",
     "Must Have","3","Sprint 1","To Do"),
    ("US-003","EP01","Quản lý Task","Assign task cho thành viên",
     "As a PO, I want to assign a task to team members so that responsibilities are clear.",
     "GIVEN tôi đang xem chi tiết task\nWHEN tôi chọn assignee từ dropdown\nTHEN task hiển thị avatar assignee và thành viên nhận notification",
     "Must Have","2","Sprint 1","To Do"),
    ("US-004","EP01","Quản lý Task","Đặt độ ưu tiên & deadline",
     "As a PO, I want to set priority and deadline for each task so that the team focuses on what matters.",
     "GIVEN tôi tạo hoặc chỉnh sửa task\nWHEN tôi chọn mức ưu tiên và nhập deadline\nTHEN task hiển thị badge màu tương ứng\n\nGIVEN deadline < 2 ngày\nTHEN badge chuyển màu đỏ và gửi reminder",
     "Must Have","2","Sprint 1","To Do"),
    ("US-005","EP01","Quản lý Task","Tìm kiếm & lọc task",
     "As a team member, I want to search and filter tasks by keyword, assignee, status so that I can find work quickly.",
     "GIVEN tôi nhập keyword\nWHEN tôi gõ ≥ 2 ký tự\nTHEN danh sách filter realtime\n\nGIVEN tôi kết hợp filter\nTHEN chỉ hiển thị task thỏa mãn tất cả điều kiện",
     "Must Have","3","Sprint 2","To Do"),
    ("US-006","EP01","Quản lý Task","Comment & đính kèm file trên task",
     "As a BA, I want to add comments and attach files to a task so that discussion stays in context.",
     "GIVEN tôi ở trang chi tiết task\nWHEN tôi nhập comment và nhấn Gửi\nTHEN comment hiển thị với timestamp\n\nGIVEN tôi đính kèm file > 25 MB\nTHEN hệ thống hiển thị lỗi giới hạn",
     "Should Have","3","Sprint 2","To Do"),
    ("US-007","EP02","Sprint Planning","Tạo và quản lý Sprint",
     "As a PO, I want to create sprints with name, goal, start/end date so that the team works in time-boxes.",
     "GIVEN tôi ở màn Sprint Planning\nWHEN tôi tạo Sprint với đầy đủ thông tin\nTHEN Sprint xuất hiện với status Planned\n\nGIVEN sprint end date < start date\nTHEN hệ thống báo lỗi validation",
     "Must Have","3","Sprint 1","To Do"),
    ("US-008","EP02","Sprint Planning","Thêm task vào Sprint",
     "As a PO, I want to move tasks from backlog into a sprint so that sprint scope is defined.",
     "GIVEN tôi đang xem Sprint backlog\nWHEN tôi kéo task từ Backlog vào Sprint\nTHEN task gắn với Sprint và cập nhật tổng Story Points\n\nGIVEN sprint đã Start\nWHEN tôi thêm task mới\nTHEN hiển thị cảnh báo cần PO xác nhận",
     "Must Have","3","Sprint 2","To Do"),
    ("US-009","EP02","Sprint Planning","Burn-down chart theo Sprint",
     "As a PO, I want to see a burn-down chart so that I can track whether the team is on pace.",
     "GIVEN sprint đang chạy\nWHEN tôi mở tab Burn-down\nTHEN biểu đồ hiển thị đường ideal vs actual theo ngày\n\nGIVEN tất cả task = Done\nTHEN đường actual chạm 0 và hiển thị badge Sprint Completed",
     "Should Have","5","Sprint 3","To Do"),
    ("US-010","EP02","Sprint Planning","Sprint Retrospective notes",
     "As a PO, I want to record retrospective notes after each sprint so that lessons are persisted.",
     "GIVEN sprint đã kết thúc\nWHEN tôi mở trang Retrospective\nTHEN có 3 cột Went Well / Improvement / Action Items\n\nGIVEN tôi lưu retro\nTHEN dữ liệu liên kết với sprint đó",
     "Should Have","3","Sprint 3","To Do"),
    ("US-011","EP03","Dashboard & Báo cáo","Dashboard cá nhân",
     "As a team member, I want a personal dashboard so that I can plan my workday efficiently.",
     "GIVEN tôi đăng nhập\nWHEN tôi mở My Dashboard\nTHEN hiển thị task đang làm, due today, overdue\n\nGIVEN không có task nào\nTHEN hiển thị empty state",
     "Must Have","3","Sprint 2","To Do"),
    ("US-012","EP03","Dashboard & Báo cáo","Dashboard Team – tổng quan tiến độ",
     "As a PO, I want a team dashboard so that I can manage team capacity.",
     "GIVEN tôi ở Team Dashboard khi sprint đang active\nWHEN tôi mở tab\nTHEN hiển thị % Done, số task theo status, workload từng thành viên\n\nGIVEN thành viên có > 5 task In Progress\nTHEN hiển thị cảnh báo overload",
     "Must Have","5","Sprint 3","To Do"),
    ("US-013","EP03","Dashboard & Báo cáo","Báo cáo Velocity Sprint-over-Sprint",
     "As a PO, I want to see team velocity across multiple sprints so that I can forecast releases.",
     "GIVEN có ≥ 2 sprint đã hoàn thành\nWHEN tôi mở Velocity Report\nTHEN biểu đồ cột hiển thị SP committed vs completed\n\nGIVEN tôi hover vào cột\nTHEN tooltip hiển thị danh sách task",
     "Could Have","5","Sprint 4","To Do"),
    ("US-014","EP03","Dashboard & Báo cáo","Xuất báo cáo tiến độ (PDF/Excel)",
     "As a PO, I want to export progress reports so that I can share with stakeholders.",
     "GIVEN tôi chọn loại báo cáo và khoảng thời gian\nWHEN tôi nhấn Xuất\nTHEN file tải về trong ≤ 5 giây\n\nGIVEN có > 500 task\nTHEN xử lý background và gửi email khi xong",
     "Could Have","5","Sprint 4","To Do"),
    ("US-015","EP04","Phân quyền","Quản lý vai trò thành viên",
     "As an Admin, I want to assign roles (PO/BA/Dev/QA/Viewer) so that each person has appropriate access.",
     "GIVEN tôi là Admin\nWHEN tôi gán role cho user\nTHEN user nhận email thông báo và quyền thay đổi ngay\n\nGIVEN user bị remove\nTHEN task của user đó hiển thị cảnh báo Unassigned",
     "Must Have","3","Sprint 1","To Do"),
    ("US-016","EP04","Phân quyền","Phân quyền theo Project",
     "As an Admin, I want to control member access per project so that sensitive projects are protected.",
     "GIVEN tôi tạo project với visibility Private\nWHEN user không được mời\nTHEN project không xuất hiện trong danh sách của user đó\n\nGIVEN Viewer cố tạo task\nTHEN hệ thống trả về lỗi 403",
     "Must Have","3","Sprint 2","To Do"),
    ("US-017","EP05","Tích hợp & Thông báo","Thông báo Email & In-app",
     "As a team member, I want to receive notifications when assigned or mentioned so that I never miss updates.",
     "GIVEN task được assign cho tôi\nWHEN assignee thay đổi\nTHEN tôi nhận in-app notification ngay và email trong 1 phút\n\nGIVEN tôi tắt email trong Settings\nTHEN chỉ nhận in-app",
     "Should Have","3","Sprint 3","To Do"),
    ("US-018","EP05","Tích hợp & Thông báo","Tích hợp Slack",
     "As a PO, I want sprint summaries in Slack so that the team stays aligned.",
     "GIVEN Slack integration đã cấu hình\nWHEN task chuyển sang Done\nTHEN bot gửi message vào channel với link task\n\nGIVEN sprint kết thúc\nTHEN bot gửi Sprint Summary",
     "Could Have","5","Sprint 4","To Do"),
    ("US-019","EP05","Tích hợp & Thông báo","Tích hợp Jira (Import/Export)",
     "As a BA, I want to import/export tasks with Jira so that the team can migrate gradually.",
     "GIVEN tôi cung cấp Jira API token và project key\nWHEN tôi chạy Import\nTHEN tất cả issues được tạo với mapping đúng\n\nGIVEN import thất bại một phần\nTHEN hệ thống cung cấp error log theo từng item",
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

ALL_TASKS = BACKLOG_US + [
    (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9])
    for r in IMPORTED
]

BL_DATA_ROW   = 3
BL_LAST_ROW   = BL_DATA_ROW + len(ALL_TASKS) - 1


def build():
    wb = xlsxwriter.Workbook(OUTPUT)

    def fmt(**kw):
        base = dict(font_name="Times New Roman", font_size=11,
                    valign="vcenter", text_wrap=True)
        base.update(kw)
        return wb.add_format(base)

    hdr_orange = fmt(bold=True,font_size=12,font_color="#FFFFFF",bg_color="#E86A23",align="center",border=1)
    hdr_dark   = fmt(bold=True,font_size=11,font_color="#FFFFFF",bg_color="#1F2737",align="center",border=1)
    hdr_blue   = fmt(bold=True,font_size=11,font_color="#FFFFFF",bg_color="#1E4D8C",align="center",border=1)

    cell_base  = fmt(border=1,border_color="#DDDDDD")
    cell_alt   = fmt(border=1,border_color="#DDDDDD",bg_color="#FFF8F4")
    cell_imp   = fmt(border=1,border_color="#DDDDDD",bg_color="#F0F7FF")
    cell_imp_a = fmt(border=1,border_color="#DDDDDD",bg_color="#E8F4FF")
    cell_ctr   = fmt(align="center",border=1,border_color="#DDDDDD")
    cell_ctr_a = fmt(align="center",border=1,border_color="#DDDDDD",bg_color="#FFF8F4")
    cell_bold  = fmt(bold=True,border=1,border_color="#DDDDDD")
    cell_bold_imp = fmt(bold=True,border=1,border_color="#DDDDDD",bg_color="#F0F7FF")

    id_us  = fmt(bold=True,font_color="#1E4D8C",align="center",border=1)
    id_us_a= fmt(bold=True,font_color="#1E4D8C",align="center",border=1,bg_color="#FFF8F4")
    id_imp = fmt(bold=True,font_color="#27AE60",align="center",border=1,bg_color="#F0F7FF")
    id_imp_a=fmt(bold=True,font_color="#27AE60",align="center",border=1,bg_color="#E8F4FF")

    epic_f = fmt(bold=True,font_color="#E86A23",align="center",border=1)
    epic_a = fmt(bold=True,font_color="#E86A23",align="center",border=1,bg_color="#FFF8F4")
    epic_empty = fmt(font_color="#AAAAAA",align="center",border=1,italic=True,bg_color="#F5F5F5")
    epic_empty_a=fmt(font_color="#AAAAAA",align="center",border=1,italic=True,bg_color="#EEEEEE")

    sp_f   = fmt(bold=True,font_size=12,align="center",border=1)
    sp_fa  = fmt(bold=True,font_size=12,align="center",border=1,bg_color="#FFF8F4")
    sp_imp = fmt(bold=True,font_size=12,align="center",border=1,bg_color="#F0F7FF")
    sp_impa= fmt(bold=True,font_size=12,align="center",border=1,bg_color="#E8F4FF")

    must_f  = fmt(bold=True,font_color="#FFFFFF",bg_color="#C0392B",align="center",border=1)
    shl_f   = fmt(bold=True,font_color="#FFFFFF",bg_color="#E67E22",align="center",border=1)
    cld_f   = fmt(bold=True,font_color="#FFFFFF",bg_color="#27AE60",align="center",border=1)
    wnt_f   = fmt(bold=True,font_color="#FFFFFF",bg_color="#95A5A6",align="center",border=1)
    high_f  = fmt(bold=True,font_color="#C0392B",align="center",border=1)
    med_f   = fmt(bold=True,font_color="#E67E22",align="center",border=1)
    low_f   = fmt(bold=True,font_color="#27AE60",align="center",border=1)
    emp_f   = fmt(font_color="#AAAAAA",align="center",border=1)

    st_ip  = fmt(bold=True,font_color="#E67E22",align="center",bg_color="#FEF9E7",border=1)
    st_td  = fmt(font_color="#1E4D8C",align="center",bg_color="#EBF5FB",border=1)
    st_dn  = fmt(font_color="#27AE60",align="center",bg_color="#EAFAF1",border=1)
    st_em  = fmt(font_color="#AAAAAA",align="center",border=1)

    src_bf = fmt(bold=True,font_color="#1E4D8C",align="center",bg_color="#EBF5FB",border=1,font_size=9)
    src_rm = fmt(bold=True,font_color="#6C3483",align="center",bg_color="#F5EEF8",border=1,font_size=9)
    src_us = fmt(font_color="#888888",align="center",border=1,font_size=9)

    meta_lbl = fmt(bold=True,font_color="#FFFFFF",bg_color="#E86A23",align="center",border=1)
    meta_val = fmt(bg_color="#FFF8F4",border=1)
    meta_fml = fmt(bold=True,font_color="#E86A23",bg_color="#FFF0E8",align="center",border=1,font_size=12)
    title_f  = fmt(bold=True,font_size=18,font_color="#E86A23",align="center")
    sub_f    = fmt(bold=True,font_size=13,font_color="#1F2737",align="center")
    div_f    = wb.add_format({"bg_color":"#E86A23"})

    def moscow_fmt(p):
        if p.startswith("Must"):   return must_f
        if p.startswith("Should"): return shl_f
        if p.startswith("Could"):  return cld_f
        return wnt_f

    def prio_fmt(p):
        if p=="High":   return high_f
        if p=="Medium": return med_f
        if p=="Low":    return low_f
        return emp_f

    def status_fmt(s):
        if s=="In Progress": return st_ip
        if s=="To Do":       return st_td
        if s=="Done":        return st_dn
        return st_em

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 1 — Cover
    # ════════════════════════════════════════════════════════════════════════
    ws_cv = wb.add_worksheet("📋 Cover")
    ws_cv.hide_gridlines(2)
    ws_cv.set_column("A:A",3); ws_cv.set_column("B:G",18)
    ws_cv.set_row(2,45); ws_cv.set_row(3,28); ws_cv.set_row(5,8)
    ws_cv.merge_range("B3:G3","PRODUCT BACKLOG — ĐỘI PRODUCT",title_f)
    ws_cv.merge_range("B4:G4","Hệ thống Quản lý Task | FPT Software",sub_f)
    ws_cv.merge_range("B6:G6","",div_f)

    for r,l1,v1,l2,v2 in [
        (8,"Dự án","Task Management System","Phiên bản","1.0"),
        (9,"Team","Product Team (BA/PO/Dev)","Ngày tạo","25/06/2026"),
        (10,"Author","Product Owner / BA","Trạng thái","Draft"),
    ]:
        ws_cv.set_row(r,22)
        ws_cv.write(r,1,l1,meta_lbl); ws_cv.merge_range(r,2,r,3,v1,meta_val)
        ws_cv.write(r,4,l2,meta_lbl); ws_cv.merge_range(r,5,r,6,v2,meta_val)

    for r in [11,12,13,14]: ws_cv.set_row(r,26)

    n_us  = len(BACKLOG_US)
    n_imp = len(IMPORTED)
    d1,d2 = BL_DATA_ROW+1, BL_LAST_ROW+1

    ws_cv.write(11,1,"Tổng User Stories (hệ thống)",meta_lbl)
    ws_cv.write_formula(11,2, f"=COUNTA('📌 Product Backlog'!B{BL_DATA_ROW+1}:B{BL_DATA_ROW+n_us})",meta_fml)
    ws_cv.merge_range(11,2,11,3,f"=COUNTA('📌 Product Backlog'!B{BL_DATA_ROW+1}:B{BL_DATA_ROW+n_us})",meta_fml)
    ws_cv.write(11,4,"Tổng Task Vận hành",meta_lbl)
    ws_cv.write_formula(11,5,f"=COUNTA('📌 Product Backlog'!B{BL_DATA_ROW+n_us+1}:B{d2})",meta_fml)
    ws_cv.merge_range(11,5,11,6,f"=COUNTA('📌 Product Backlog'!B{BL_DATA_ROW+n_us+1}:B{d2})",meta_fml)

    ws_cv.write(12,1,"Tổng Story Points (hệ thống)",meta_lbl)
    ws_cv.write_formula(12,2,f"=SUM('📌 Product Backlog'!H{BL_DATA_ROW+1}:H{BL_DATA_ROW+n_us})",meta_fml)
    ws_cv.merge_range(12,2,12,3,f"=SUM('📌 Product Backlog'!H{BL_DATA_ROW+1}:H{BL_DATA_ROW+n_us})",meta_fml)
    ws_cv.write(12,4,"Tổng SP (Vận hành)",meta_lbl)
    ws_cv.write_formula(12,5,f"=SUM('📌 Product Backlog'!H{BL_DATA_ROW+n_us+1}:H{d2})",meta_fml)
    ws_cv.merge_range(12,5,12,6,f"=SUM('📌 Product Backlog'!H{BL_DATA_ROW+n_us+1}:H{d2})",meta_fml)

    ws_cv.write(13,1,"Tổng Epics (unique)",meta_lbl)
    ws_cv.write_formula(13,2,
        f"=SUMPRODUCT((LEN('📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us})>0)"
        f"/COUNTIF('📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us},"
        f"'📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us}&\"\"))",
        meta_fml)
    ws_cv.merge_range(13,2,13,3,
        f"=SUMPRODUCT((LEN('📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us})>0)"
        f"/COUNTIF('📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us},"
        f"'📌 Product Backlog'!C{BL_DATA_ROW+1}:C{BL_DATA_ROW+n_us}&\"\"))",
        meta_fml)
    ws_cv.write(13,4,"In Progress (Vận hành)",meta_lbl)
    ws_cv.write_formula(13,5,f"=COUNTIF('📌 Product Backlog'!J{BL_DATA_ROW+n_us+1}:J{d2},\"In Progress\")",meta_fml)
    ws_cv.merge_range(13,5,13,6,f"=COUNTIF('📌 Product Backlog'!J{BL_DATA_ROW+n_us+1}:J{d2},\"In Progress\")",meta_fml)

    ws_cv.write(14,1,"Tổng tất cả tasks",meta_lbl)
    ws_cv.write_formula(14,2,f"=COUNTA('📌 Product Backlog'!B{d1}:B{d2})",meta_fml)
    ws_cv.merge_range(14,2,14,3,f"=COUNTA('📌 Product Backlog'!B{d1}:B{d2})",meta_fml)
    ws_cv.write(14,4,"To Do (Vận hành)",meta_lbl)
    ws_cv.write_formula(14,5,f"=COUNTIF('📌 Product Backlog'!J{BL_DATA_ROW+n_us+1}:J{d2},\"To Do\")",meta_fml)
    ws_cv.merge_range(14,5,14,6,f"=COUNTIF('📌 Product Backlog'!J{BL_DATA_ROW+n_us+1}:J{d2},\"To Do\")",meta_fml)

    ws_cv.merge_range("B17:G17",
        "* Các ô màu cam tự động cập nhật khi thêm/sửa dữ liệu trong sheet Product Backlog.",
        fmt(font_size=9,font_color="#888888",align="center"))

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 2 — Product Backlog (US hệ thống + Task vận hành gộp chung)
    # ════════════════════════════════════════════════════════════════════════
    ws = wb.add_worksheet("📌 Product Backlog")
    ws.hide_gridlines(2); ws.freeze_panes(3,0); ws.set_zoom(80)

    for i,w in enumerate([4,8,8,14,22,36,36,6,16,12,14]): ws.set_column(i,i,w)

    ws.set_row(0,32)
    ws.merge_range("A1:K1","PRODUCT BACKLOG — HỆ THỐNG QUẢN LÝ TASK + VẬN HÀNH FPTvn | ĐỘI PRODUCT",hdr_orange)

    ws.set_row(1,28)
    for ci,h in enumerate(["#","ID","Epic","Epic Name","US Title",
                            "User Story / Mô tả (thuần Việt)",
                            "Acceptance Criteria (Gherkin – thuần Việt)",
                            "SP","Sprint","Status","Nguồn"]):
        ws.write(2,ci,h,hdr_dark)

    # ── Phần 1: US hệ thống (US-001 → US-019) ──
    group_hdr_us = fmt(bold=True,font_size=10,font_color="#FFFFFF",
                       bg_color="#1F2737",align="left",border=1)
    ws.set_row(BL_DATA_ROW-1,20)
    ws.merge_range(BL_DATA_ROW-1,0,BL_DATA_ROW-1,10,
                   "▼ PHẦN 1 — USER STORIES HỆ THỐNG QUẢN LÝ TASK (US-001 → US-019)",group_hdr_us)

    for idx,(us_id,epic_id,epic_name,title,story,ac,priority,sp,sprint,status) in enumerate(BACKLOG_US):
        r   = idx + BL_DATA_ROW
        alt = (idx%2==1)
        ws.set_row(r,80)
        ws.write(r,0,idx+1,   cell_ctr_a if alt else cell_ctr)
        ws.write(r,1,us_id,   id_us_a    if alt else id_us)
        ws.write(r,2,epic_id, epic_a     if alt else epic_f)
        ws.write(r,3,epic_name,cell_alt  if alt else cell_base)
        ws.write(r,4,title,   cell_bold)
        ws.write(r,5,story,   cell_alt   if alt else cell_base)
        ws.write(r,6,ac,      cell_alt   if alt else cell_base)
        ws.write(r,7,int(sp), sp_fa      if alt else sp_f)
        ws.write(r,8,sprint,  cell_ctr_a if alt else cell_ctr)
        ws.write(r,9,status,  status_fmt(status))
        ws.write(r,10,"Hệ thống",src_us)

    # ── Phần 2: Task vận hành import ──
    imp_start = BL_DATA_ROW + len(BACKLOG_US)
    group_hdr_imp = fmt(bold=True,font_size=10,font_color="#FFFFFF",
                        bg_color="#1E4D8C",align="left",border=1)
    ws.set_row(imp_start-1,20)
    ws.merge_range(imp_start-1,0,imp_start-1,10,
                   f"▼ PHẦN 2 — TASK VẬN HÀNH IMPORT (Backlog FPTvn: BF-001→BF-018 | Roadmap 18.5: RM-001→RM-013)",
                   group_hdr_imp)

    for idx,(oid,epic_id,epic_name,title,story,ac,priority,sp,sprint,status,nguon) in enumerate(IMPORTED):
        r   = idx + imp_start
        alt = (idx%2==1)
        ws.set_row(r,80)
        ws.write(r,0, idx+1,      fmt(align="center",border=1,bg_color="#E8F4FF" if alt else "#F0F7FF"))
        ws.write(r,1, oid,        id_imp_a if alt else id_imp)
        ws.write(r,2, epic_id,    epic_empty_a if alt else epic_empty)
        ws.write(r,3, epic_name,  cell_imp_a if alt else cell_imp)
        ws.write(r,4, title,      cell_bold_imp)
        ws.write(r,5, story,      cell_imp_a if alt else cell_imp)
        ws.write(r,6, ac,         cell_imp_a if alt else cell_imp)
        ws.write(r,7, int(sp),    sp_impa if alt else sp_imp)
        ws.write(r,8, sprint,     fmt(align="center",border=1,bg_color="#E8F4FF" if alt else "#F0F7FF"))
        ws.write(r,9, status,     status_fmt(status))
        ws.write(r,10,nguon,      src_rm if "Roadmap" in nguon else src_bf)

    # ── Dòng tổng ──
    sum_r = BL_LAST_ROW + 2
    sf = fmt(bold=True,font_color="#FFFFFF",bg_color="#1F2737",align="center",border=1)
    ws.set_row(sum_r,24)
    ws.merge_range(sum_r,0,sum_r,6,"TỔNG",sf)
    ws.write_formula(sum_r,7,f"=SUM(H{BL_DATA_ROW+1}:H{BL_LAST_ROW+1})",sf)
    ws.write_formula(sum_r,8,f"=COUNTA(B{BL_DATA_ROW+1}:B{BL_LAST_ROW+1})&\" tasks\"",sf)
    ws.write(sum_r,9,"",sf); ws.write(sum_r,10,"",sf)

    # ── MoSCoW legend ──
    leg = sum_r+2; ws.set_row(leg,22)
    ws.write(leg,0,"MoSCoW:",fmt(bold=True,font_size=10))
    for ci,(lbl,f2) in enumerate([("Must Have",must_f),("Should Have",shl_f),
                                    ("Could Have",cld_f),("Won't Have v1",wnt_f)]):
        ws.write(leg,ci+1,lbl,f2)
    ws.write(leg,5,"ID xanh lá = Task vận hành import từ FPTvn/Roadmap",
             fmt(font_size=9,font_color="#27AE60"))

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 3 — Sprint Planning
    # ════════════════════════════════════════════════════════════════════════
    ws_sp = wb.add_worksheet("🗓 Sprint Planning")
    ws_sp.hide_gridlines(2); ws_sp.freeze_panes(2,0)
    for i,w in enumerate([16,10,14,14,30,10,45]): ws_sp.set_column(i,i,w)
    ws_sp.set_row(0,30); ws_sp.merge_range("A1:G1","SPRINT PLANNING — RELEASE v1",hdr_orange)
    ws_sp.set_row(1,24)
    for ci,h in enumerate(["Sprint","Thời lượng","Bắt đầu","Kết thúc","User Stories","Story Points","Sprint Goal"]):
        ws_sp.write(1,ci,h,hdr_blue)
    sn_f=fmt(bold=True,font_color="#FFFFFF",bg_color="#E86A23",align="center",border=1)
    sn_a=fmt(bold=True,font_color="#FFFFFF",bg_color="#1E4D8C",align="center",border=1)
    sr=fmt(border=1,border_color="#DDDDDD"); sra=fmt(border=1,bg_color="#EFF3FB")
    sc=fmt(align="center",border=1); sca=fmt(align="center",border=1,bg_color="#EFF3FB")
    spt=fmt(bold=True,align="center",font_color="#1E4D8C",border=1)
    spa=fmt(bold=True,align="center",font_color="#1E4D8C",border=1,bg_color="#EFF3FB")
    for i,(sprint,dur,s,e,stories,pts,goal) in enumerate(SPRINT_PLAN):
        r=i+2; alt=(i%2==1); ws_sp.set_row(r,40)
        ws_sp.write(r,0,sprint,sn_a if alt else sn_f)
        ws_sp.write(r,1,dur,sca if alt else sc); ws_sp.write(r,2,s,sca if alt else sc)
        ws_sp.write(r,3,e,sca if alt else sc); ws_sp.write(r,4,stories,sra if alt else sr)
        ws_sp.write(r,5,pts,spa if alt else spt); ws_sp.write(r,6,goal,sra if alt else sr)
    sr2=len(SPRINT_PLAN)+3; ws_sp.set_row(sr2,26)
    sf2=fmt(bold=True,font_color="#FFFFFF",bg_color="#1F2737",align="center",border=1)
    ws_sp.merge_range(sr2,0,sr2,4,"TỔNG RELEASE v1 (Sprint 1–4)",sf2)
    ws_sp.write(sr2,5,"62 SP",sf2); ws_sp.write(sr2,6,"18 User Stories — ~8 tuần",sf2)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 4 — Definition of Done
    # ════════════════════════════════════════════════════════════════════════
    ws_dod=wb.add_worksheet("✅ Definition of Done")
    ws_dod.hide_gridlines(2)
    ws_dod.set_column("A:A",6); ws_dod.set_column("B:B",70); ws_dod.set_column("C:C",20)
    ws_dod.set_row(0,30); ws_dod.merge_range("A1:C1","DEFINITION OF DONE (DoD)",hdr_orange)
    ws_dod.set_row(1,22)
    ws_dod.write(1,0,"#",hdr_dark); ws_dod.write(1,1,"Tiêu chí nghiệm thu",hdr_dark)
    ws_dod.write(1,2,"Loại kiểm tra",hdr_dark)
    dck=fmt(bold=True,font_color="#FFFFFF",bg_color="#27AE60",align="center",border=1)
    dt =fmt(border=1,bg_color="#F9F9F9"); dta=fmt(border=1)
    dty=fmt(align="center",font_color="#1A7A1A",border=1,bg_color="#EAF4EA")
    dtya=fmt(align="center",font_color="#1A7A1A",border=1,bg_color="#D5ECD5")
    for i,(item,dtype) in enumerate(DOD):
        r=i+2; alt=(i%2==1); ws_dod.set_row(r,26)
        ws_dod.write(r,0,f"✓ {i+1}",dck)
        ws_dod.write(r,1,item,dta if alt else dt)
        ws_dod.write(r,2,dtype,dtya if alt else dty)

    # ════════════════════════════════════════════════════════════════════════
    # SHEET 5 — Kanban Board
    # ════════════════════════════════════════════════════════════════════════
    ws_kb=wb.add_worksheet("🗂 Kanban Board")
    ws_kb.hide_gridlines(2)
    ws_kb.set_row(0,30); ws_kb.merge_range("A1:L1","KANBAN BOARD — SPRINT HIỆN TẠI",hdr_orange)
    cols_kb=[("To Do","#95A5A6","#ECF0F1"),("In Progress","#E67E22","#FEF9E7"),
             ("Review","#1E4D8C","#EBF5FB"),("Done","#27AE60","#EAFAF1")]
    for (st,hc,bc),col_s in zip(cols_kb,[0,3,6,9]):
        for c in range(col_s,col_s+3): ws_kb.set_column(c,c,7)
        ws_kb.set_row(1,26)
        ws_kb.merge_range(1,col_s,1,col_s+2,st,
                          fmt(bold=True,font_size=13,font_color="#FFFFFF",bg_color=hc,align="center",border=1))
        sp1=[t for t in BACKLOG_US if t[8]=="Sprint 1" and t[9]==st]
        for ti in range(8):
            r=ti+2; ws_kb.set_row(r,50)
            if ti<len(sp1):
                t=sp1[ti]
                ws_kb.merge_range(r,col_s,r,col_s+2,f"{t[0]}\n{t[3]}",
                                  fmt(bg_color=bc,border=1,border_color=hc,font_size=9,text_wrap=True))
            else:
                ws_kb.merge_range(r,col_s,r,col_s+2,"",
                                  fmt(bg_color=bc,border=1,border_color="#DDDDDD"))

    wb.close()
    print(f"✅ Saved: {OUTPUT}")
    print(f"   US hệ thống: {len(BACKLOG_US)} | Task vận hành: {len(IMPORTED)} (18 FPTvn + 13 Roadmap)")
    print(f"   Tổng rows Product Backlog: {len(ALL_TASKS)}")


if __name__ == "__main__":
    build()

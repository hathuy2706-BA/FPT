# -*- coding: utf-8 -*-
"""
Cập nhật bảng Kịch Bản Chuẩn - Tech Spec sang ngôn ngữ kinh doanh (Business-friendly)
Dành cho sheet 'Kich Ban Chuan - Tech Spec'
Theo chuẩn Senior BA & Product Owner:
- Bỏ các chi tiết kỹ thuật quá sâu (Backend State, API, Redux/CSS)
- Tập trung vào Tình huống mua hàng, Quy tắc nghiệp vụ, Xử lý khi có thay đổi
- Bổ sung Cột Câu hỏi khai vấn / Mong muốn đội Kinh doanh (Questions for Sales/Biz)
- Định dạng chuẩn Font: Times New Roman, Bảng % co giãn, màu sắc trang nhã
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import csv
import os

# Dữ liệu 13 nhóm kịch bản đã được chuyển ngữ Business và bổ sung câu hỏi cho Đội Kinh doanh
modules_biz = [
    {
        "module": "1. Tổ hợp số lượng (Basic 1:1)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua đúng tỷ lệ 1:1: Mua 1 Camera Play 4 và chọn 1 Charm tiêu chuẩn (Basic)",
                "pre": "Giỏ hàng có 1 Camera Play 4 (giá niêm yết). Kho còn Charm tiêu chuẩn.",
                "rule": "Mua 1 Camera Play 4 kích hoạt quyền mua 1 Charm tiêu chuẩn với giá 0đ. Hạn mức Charm 0đ tối đa = Số lượng Camera trong giỏ hàng (1 Cam = 1 Charm 0đ).",
                "alt": "Nếu mẫu Charm tiêu chuẩn khách chọn bị hết hàng: Cho phép khách chọn sang mẫu Charm tiêu chuẩn khác còn hàng.",
                "biz_question": "Đội Kinh doanh có muốn giới hạn số lượng Camera tối đa được mua kèm Charm 0đ trên mỗi đơn hàng không (VD: Tối đa 5 Cam/đơn để tránh gom hàng)?"
            },
            {
                "br": "BR-02",
                "scenario": "Vượt hạn mức (Cùng mẫu): Mua 1 Cam, khách chọn 2 Charm cùng Mẫu A",
                "pre": "Đã có 1 Camera và 1 Charm A (0đ) trong giỏ. Khách bấm chọn thêm 1 Charm A nữa.",
                "rule": "Tách 2 Charm A thành 2 dòng riêng: 01 chiếc tính giá 0đ (theo Camera), 01 chiếc tính giá bán lẻ gốc niêm yết 150.000đ. Không tính giá trung bình cộng.",
                "alt": "Nếu khách bấm giảm bớt 1 Charm A: Hệ thống luôn ưu tiên giữ lại chiếc 0đ cho khách, bỏ chiếc tính tiền.",
                "biz_question": "Khi khách chọn vượt quá số lượng 0đ, Kinh doanh muốn hệ thống tự động tính giá bán lẻ món thứ 2 hay hiển thị thông báo chặn không cho chọn thêm?"
            },
            {
                "br": "BR-03",
                "scenario": "Vượt hạn mức (Khác mẫu - Khác giá): Mua 1 Cam, chọn 1 Charm A (100k) và 1 Charm B (150k)",
                "pre": "1 Camera Play 4 trong giỏ, khách tick chọn 1 Charm A (giá gốc 100k) và 1 Charm B (giá gốc 150k).",
                "rule": "Ưu tiên quyền lợi tốt nhất cho khách (Best-deal): Tự động tặng 0đ cho Charm có giá trị cao nhất (Charm B - 150k), Charm còn lại (Charm A - 100k) tính giá bán lẻ gốc.",
                "alt": "Nếu khách bỏ chọn Charm B: Hệ thống tự động chuyển Charm A thành 0đ ngay lập tức để bảo vệ quyền lợi quà tặng của khách.",
                "biz_question": "Kinh doanh muốn ưu tiên tặng món có giá trị cao nhất (Best-deal for Customer) để tăng độ hài lòng, hay tặng món rẻ nhất để tối ưu chi phí quà tặng cho công ty?"
            },
            {
                "br": "BR-04",
                "scenario": "Dưới hạn mức: Mua 3 Camera nhưng khách chỉ chọn 1 Charm Mẫu A",
                "pre": "Giỏ hàng có 3 Camera (được 3 suất Charm 0đ), nhưng khách chỉ chọn 1 Charm A.",
                "rule": "Không ép buộc mua đủ số lượng quà. Khách có toàn quyền mua ít hơn hạn mức. Hệ thống hiển thị lời nhắc nhẹ nhàng nhưng không chặn luồng thanh toán.",
                "alt": "Khách bỏ qua lời nhắc và thanh toán: Đơn hàng chỉ xuất 3 Camera + 1 Charm. Quyền nhận 2 Charm còn lại sẽ hết hiệu lực khi đơn hoàn tất.",
                "biz_question": "Có cần gửi email/SMS nhắc nhở tặng voucher bù cho 2 suất quà khách chưa chọn không, hay mặc định khách tự nguyện từ bỏ quà tặng?"
            },
            {
                "br": "BR-05",
                "scenario": "Không chọn quà: Mua 2 Camera nhưng không chọn bất kỳ Charm nào",
                "pre": "Có 2 Camera Play 4 trong giỏ, khách không chọn phụ kiện nào và bấm đi đến thanh toán.",
                "rule": "Ưu đãi Charm 0đ là chính sách 'Mua Kèm Ngay', KHÔNG quy đổi thành tiền mặt, KHÔNG tự động bảo lưu thành voucher cho đơn hàng sau.",
                "alt": "Tại bước thanh toán: Hiển thị hộp thoại xác nhận ngắn: 'Bạn đang bỏ qua 2 Charm 0đ tặng kèm. Bạn có muốn chọn quà ngay không?'.",
                "biz_question": "Kinh doanh có đồng ý cho phép khách bỏ qua quà tặng không, và nếu sau này khách gọi lên tổng đài khiếu nại đòi quà thì CSKH xử lý thế nào?"
            },
            {
                "br": "BR-06",
                "scenario": "Giảm số lượng Camera (Đồng bộ ngược): Đang có 2 Cam + 2 Charm A (0đ), giảm Cam xuống 1",
                "pre": "Giỏ hàng có 2 Camera + 2 Charm A (cả 2 đều 0đ). Khách bấm giảm bớt 1 Camera.",
                "rule": "Suất ưu đãi 0đ giảm từ 2 xuống 1. Giữ nguyên 2 Charm A trong giỏ nhưng chiếc thứ 2 tự động chuyển thành tính giá niêm yết (150.000đ). Không tự ý xóa hàng của khách.",
                "alt": "Khách có quyền bấm xóa dòng Charm tính tiền 150.000đ nếu không có nhu cầu mua thêm.",
                "biz_question": "Kinh doanh muốn giữ lại Charm và chuyển sang tính giá gốc, hay tự động xóa bớt 1 Charm để giỏ hàng chỉ còn đúng 1 Camera + 1 Charm 0đ?"
            },
            {
                "br": "BR-07",
                "scenario": "Giảm Camera khi đang chọn nhiều mẫu khác nhau: Đang có 2 Cam + 1 Charm A + 1 Charm B, giảm Cam xuống 1",
                "pre": "Giỏ có 2 Cam + 1 Charm A (0đ) + 1 Charm B (0đ). Khách giảm Camera xuống 1.",
                "rule": "Chỉ còn 1 suất 0đ: Giữ món có giá trị cao nhất làm 0đ, món còn lại tính giá gốc. Nếu 2 món bằng giá, giữ món khách chọn trước làm 0đ.",
                "alt": "Cho phép khách nhấp chuột trực tiếp vào lựa chọn để hoán đổi quyền 0đ giữa Mẫu A và Mẫu B một cách dễ dàng.",
                "biz_question": "Khi giảm số lượng Camera, Kinh doanh muốn hệ thống tự động chọn món 0đ theo quy tắc có sẵn hay bắt buộc bật bảng hỏi để khách tự tay chọn?"
            },
            {
                "br": "BR-08",
                "scenario": "Mua số lượng lớn: Khách mua 10 Camera, muốn chia quà cho cả 3 mẫu Charm A, B, C",
                "pre": "Khách mua số lượng lớn (10 Camera Play 4, được 10 suất Charm 0đ).",
                "rule": "Cho phép khách gõ trực tiếp số lượng từng mẫu Charm vào ô nhập liệu (thay vì bấm nút [+] 10 lần). Tổng số lượng Charm 0đ không vượt quá 10.",
                "alt": "Hiển thị thanh tiến trình trực quan: 'Đã phân bổ: 7/10 Charm 0đ'. Nếu nhập quá 10, số lượng vượt sẽ tự động tính theo giá bán lẻ.",
                "biz_question": "Chính sách mua số lượng lớn (trên 10 chiếc) áp dụng cho khách hàng cá nhân hay có kênh bán hàng sỉ/B2B riêng với mức chiết khấu khác?"
            },
            {
                "br": "BR-09",
                "scenario": "Đổi mẫu phụ kiện: Đang có 3 Cam + 3 Charm (1A, 1B, 1C), muốn đổi C thành A",
                "pre": "Đã chọn tối đa 3 Charm (1A, 1B, 1C). Suất quà 0đ khả dụng = 0.",
                "rule": "Khi khách giảm số lượng Mẫu C về 0, suất 0đ ngay lập tức được giải phóng. Khách bấm tăng Mẫu A lên 2 chiếc thì chiếc thứ 2 được hưởng giá 0đ.",
                "alt": "Nếu khách tăng Mẫu A trước khi giảm Mẫu C: Chiếc A thứ 2 tạm tính giá bán lẻ 150k cho đến khi khách giảm bớt Mẫu C.",
                "biz_question": "Trải nghiệm đổi quà nên diễn ra trực tiếp tại giỏ hàng hay cần nút 'Đổi quà tặng' chuyên biệt để khách thao tác thuận tiện nhất?"
            },
            {
                "br": "BR-10",
                "scenario": "Xóa Camera khỏi giỏ: Đang có 1 Cam + 1 Charm 0đ, khách bấm xóa Camera",
                "pre": "Có 1 Camera Play 4 + 1 Charm 0đ trong giỏ hàng. Khách bấm nút 'Xóa' Camera.",
                "rule": "Quy tắc ràng buộc: Charm 0đ không thể tồn tại độc lập khi không có Camera. Xóa Camera sẽ làm mất điều kiện nhận quà tặng 0đ.",
                "alt": "Hệ thống hỏi khách: 'Xóa Camera sẽ mất quà tặng 0đ. Bạn có muốn giữ lại Charm với giá bán lẻ 150.000đ không? [Xóa tất cả] [Giữ Charm giá gốc]'.",
                "biz_question": "Kinh doanh muốn tự động xóa sạch Charm đi kèm khi xóa Camera, hay giữ lại Charm và thông báo tính giá gốc?"
            }
        ]
    },
    {
        "module": "2. Phụ thu nâng cấp (Charm Premium +50k)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua kết hợp Bản thường & Bản cao cấp: Mua 2 Cam, chọn 1 Charm Basic (0đ) + 1 Charm Premium (+50k)",
                "pre": "2 Camera Play 4 (được 2 suất ưu đãi). Kho còn cả mẫu Basic và mẫu Premium.",
                "rule": "1 Camera được đổi 1 Charm tiêu chuẩn 0đ HOẶC nâng cấp lên Charm Premium với mức phụ thu ưu đãi +50.000đ/chiếc (thay vì giá bán lẻ gốc 200.000đ).",
                "alt": "Hóa đơn hiển thị rõ: Tiền Camera + Phụ thu nâng cấp Charm Premium 50.000đ (Tiết kiệm 150.000đ).",
                "biz_question": "Khoản thu 50.000đ này kế toán sẽ ghi nhận vào doanh thu phụ kiện Charm hay phân bổ giảm trừ vào giá bán của Camera?"
            },
            {
                "br": "BR-02",
                "scenario": "Vượt hạn mức kết hợp: Mua 1 Cam, chọn cả 1 Charm Basic + 1 Charm Premium",
                "pre": "1 Camera Play 4 (chỉ có 1 suất ưu đãi). Khách chọn 2 món phụ kiện khác loại.",
                "rule": "Áp dụng suất ưu đãi cho món mang lại quyền lợi cao nhất: Charm Basic 0đ + Charm Premium tính giá bán lẻ gốc 200k (Tổng tiền phụ kiện = 200k).",
                "alt": "Nếu khách muốn áp dụng suất ưu đãi cho Premium (trả 50k) và trả tiền gốc cho Basic (150k): Tổng tiền phụ kiện vẫn là 200k.",
                "biz_question": "Kinh doanh có đồng ý cho khách chủ động chọn món nào được hưởng ưu đãi (Basic 0đ hay Premium 50k) trong trường hợp này không?"
            },
            {
                "br": "BR-03",
                "scenario": "Đổi ý nâng cấp (Swap): Đang chọn Charm Basic 0đ, khách bấm đổi sang Charm Premium",
                "pre": "Giỏ có 1 Cam + 1 Charm Basic 0đ. Khách tick chọn sang mẫu Premium.",
                "rule": "Hệ thống tự động hủy chọn mẫu Basic và áp dụng mức phụ thu +50.000đ cho mẫu Premium. Tổng số tiền thanh toán tăng thêm đúng 50.000đ.",
                "alt": "Giao diện cập nhật tức thì, có thông báo: 'Đã nâng cấp lên phiên bản Charm Premium (+50.000đ)'.",
                "biz_question": "Có cần làm nổi bật lợi ích 'Chỉ thêm 50k sở hữu ngay bản Giới hạn/Cao cấp' để kích thích khách hàng nâng cấp (Upsell) không?"
            },
            {
                "br": "BR-04",
                "scenario": "Tăng số lượng Camera khi đang có Charm Premium: Đang có 1 Cam + 1 Premium (+50k), tăng Cam lên 2",
                "pre": "Giỏ có 1 Cam + 1 Charm Premium (+50k). Khách bấm [+] tăng Camera lên 2.",
                "rule": "Giữ nguyên 1 Charm Premium (+50k) và mở thêm 01 ô quà tặng còn trống để khách tự do chọn thêm món thứ 2. KHÔNG tự động nhân đôi Premium thành 2 cái (+100k).",
                "alt": "Khách có thể chọn thêm 1 Charm Basic (0đ) hoặc thêm 1 Charm Premium (+50k) tùy nhu cầu.",
                "biz_question": "Khi khách tăng Camera, Kinh doanh muốn hệ thống gợi ý chọn thêm quà ngay hay để khách tự vào giỏ hàng chọn sau?"
            },
            {
                "br": "BR-05",
                "scenario": "Giảm Camera khi đang có cả 2 loại: Đang có 2 Cam + 1 Basic (0đ) + 1 Premium (+50k), giảm Cam xuống 1",
                "pre": "Giỏ có 2 Cam + 1 Basic + 1 Premium. Khách bấm [-] giảm Camera về 1.",
                "rule": "Suất ưu đãi giảm còn 1: Ưu tiên giữ lại suất Charm Basic 0đ, chiếc Charm Premium chuyển sang tính theo giá bán lẻ gốc 200.000đ.",
                "alt": "Hiển thị thông báo nhanh cho khách chọn: 'Giữ Charm Basic 0đ' hoặc 'Giữ Charm Premium ưu đãi 50k (bỏ Basic)'.",
                "biz_question": "Kinh doanh muốn ưu tiên giữ suất miễn phí (0đ) hay giữ suất có phụ thu (+50k) khi khách giảm số lượng mua?"
            },
            {
                "br": "BR-06",
                "scenario": "Chính sách đổi trả khi có phụ thu nâng cấp",
                "pre": "Đơn hàng hoàn tất gồm 1 Camera Play 4 (800k) + 1 Charm Premium (50k). Khách muốn trả Camera, giữ lại Charm.",
                "rule": "Khách trả Camera nhưng giữ Charm Premium: Charm không còn điều kiện mua kèm, bị tính theo giá bán lẻ gốc (200k). Số tiền hoàn lại = Tiền Camera (800k) - Chênh lệch Charm (200k - 50k = 150k) = 650.000đ.",
                "alt": "Nếu khách trả lại cả Camera và Charm Premium còn nguyên vẹn: Hoàn đủ 100% số tiền thực thu (850.000đ).",
                "biz_question": "Kinh doanh có đồng ý với phương án cấn trừ tiền hoàn chênh lệch này không, hay bắt buộc khách phải trả đủ cả bộ mới được hoàn tiền?"
            }
        ]
    },
    {
        "module": "3. Bán chéo số lượng (Mua thêm Charm 2, 3 giảm 50%)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua nhiều Charm giá khác nhau: 1 Cam, chọn 3 Charm giá gốc khác nhau (100k, 150k, 200k)",
                "pre": "Chính sách: Mua 1 Cam được 1 Charm 0đ + tối đa 2 Charm tiếp theo giảm 50%. Khách chọn 3 Charm (100k, 150k, 200k).",
                "rule": "Ưu tiên tối đa quyền lợi khách hàng: Chiếc 200k tặng 0đ (tiết kiệm 200k). Chiếc 150k giảm 50% còn 75k. Chiếc 100k giảm 50% còn 50k. Tổng phụ kiện = 125k (Tiết kiệm 325k).",
                "alt": "Nếu chính sách kinh doanh ưu tiên bảo vệ lợi nhuận: Tặng 0đ cho chiếc rẻ nhất (100k) và giảm 50% cho 2 chiếc còn lại.",
                "biz_question": "Kinh doanh lựa chọn phương án nào: Tối ưu lợi ích cho khách (giảm giá chiếc đắt nhất) hay Bảo vệ doanh thu (giảm giá chiếc rẻ nhất)?"
            },
            {
                "br": "BR-02",
                "scenario": "Vượt trần ưu đãi: Mua 1 Cam nhưng khách chọn tới 5 Charm",
                "pre": "1 Camera Play 4. Hạn mức tối đa: 1 Charm 0đ + 2 Charm giảm 50% (Tổng tối đa 3 chiếc có ưu đãi). Khách chọn 5 Charm.",
                "rule": "Chiếc thứ 1: Tặng 0đ. Chiếc thứ 2 và 3: Giảm 50%. Chiếc thứ 4 và thứ 5: Tính nguyên giá bán lẻ 100%.",
                "alt": "Nếu khách mua thêm Camera thứ 2: Hạn mức mở rộng thành 2 chiếc 0đ + 4 chiếc 50%, chiếc thứ 4 và 5 tự động chuyển sang hưởng giảm 50% ngay.",
                "biz_question": "Giới hạn mua thêm giảm 50% nên chốt là tối đa 2 chiếc hay mở rộng theo tỷ lệ số Camera mua?"
            },
            {
                "br": "BR-03",
                "scenario": "Xóa Camera khi đang có Charm 0đ và Charm giảm 50%",
                "pre": "Giỏ có 1 Camera + 1 Charm 0đ + 1 Charm giảm 50%. Khách xóa Camera khỏi giỏ.",
                "rule": "Toàn bộ ưu đãi mua kèm bị vô hiệu lực. Hệ thống cảnh báo và chuyển toàn bộ các Charm về giá niêm yết 100% nếu khách muốn giữ giỏ, hoặc xóa toàn bộ.",
                "alt": "Bảng hỏi: 'Xóa Camera sẽ làm mất toàn bộ ưu đãi phụ kiện 0đ và giảm 50%. Bạn có muốn tiếp tục? [Xóa tất cả] [Giữ Charm giá gốc]'.",
                "biz_question": "Kinh doanh có muốn áp dụng mức giảm giá khác (VD: Giảm 10% khách hàng mới) nếu khách quyết định giữ lại phụ kiện không?"
            },
            {
                "br": "BR-04",
                "scenario": "Dịch chuyển thứ tầng ưu đãi khi giảm Camera: Giảm Cam từ 2 xuống 1",
                "pre": "Giỏ có 2 Cam + 2 Charm (0đ) + 2 Charm (50%). Khách bấm giảm Camera xuống 1.",
                "rule": "Hạn mức mới: 1 Charm 0đ + 2 Charm 50% + 1 Charm giá gốc 100%. Hệ thống tự động dịch chuyển món đắt nhất vào nhóm 0đ, tiếp theo vào nhóm 50% và món rẻ nhất về giá gốc.",
                "alt": "Giá đơn hàng cập nhật tức thì kèm thông báo lý do điều chỉnh số lượng ưu đãi.",
                "biz_question": "Quy tắc trượt tầng giá tự động này có đáp ứng đúng mong muốn vận hành của đội ngũ Kinh doanh không?"
            },
            {
                "br": "BR-05",
                "scenario": "Đóng gói & Giao nhận khi đơn hàng có nhiều mức giá khác nhau",
                "pre": "Đơn hàng hoàn tất gồm 1 Cam + 1 Charm 0đ + 2 Charm giảm 50%.",
                "rule": "Tất cả các sản phẩm được đóng chung trong CÙNG MỘT KIỆN HÀNG nếu xuất cùng một kho, không tách rời theo mức giá khuyến mãi.",
                "alt": "Hóa đơn và phiếu giao hàng ghi rõ từng dòng sản phẩm với đơn giá thực tế đã giảm để giao cho khách.",
                "biz_question": "Kho vận có yêu cầu dán tem phân biệt giữa phụ kiện tặng 0đ và phụ kiện bán lẻ giảm giá 50% không?"
            }
        ]
    },
    {
        "module": "4. Combo Booster (Bundle Play4 + Dòng khác)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua Combo đóng gói sẵn: Khách mua gói 'Combo An Ninh: Play 4 + IQ4S'",
                "pre": "Gian hàng mở bán mã Combo đóng gói sẵn có chứa 01 thiết bị Camera Play 4.",
                "rule": "Do trong Combo có thiết bị Play 4, khách vẫn được kích hoạt đúng 01 suất mua Charm 0đ như khi mua lẻ.",
                "alt": "Trang chi tiết của Combo hiển thị rõ: 'Tặng kèm 01 Charm Play 4 tự chọn trị giá 150.000đ'.",
                "biz_question": "Nếu mã Combo này đã được giảm giá sốc hơn 20%, Kinh doanh có muốn loại trừ quà tặng Charm 0đ không?"
            },
            {
                "br": "BR-02",
                "scenario": "Gom Combo mềm: Khách tự nhặt 1 Play 4 lẻ và 1 IQ4S lẻ vào giỏ",
                "pre": "Khách chọn riêng lẻ 1 Play 4 và 1 IQ4S vào giỏ hàng.",
                "rule": "Hệ thống tự động nhận diện cặp sản phẩm hợp lệ, áp dụng giá ưu đãi Combo (tiết kiệm thêm) và vẫn mở đầy đủ quyền nhận 01 Charm 0đ.",
                "alt": "Hiển thị thông báo: 'Đã tự động ghép Combo An Ninh - Tiết kiệm thêm 100k + Tặng 1 Charm 0đ'.",
                "biz_question": "Kinh doanh muốn hệ thống tự động ghép Combo để kích cầu hay bắt buộc khách phải chọn mua đúng link Combo mới được giảm giá?"
            },
            {
                "br": "BR-03",
                "scenario": "Phá vỡ Combo mềm: Khách xóa bớt IQ4S, chỉ giữ lại Play 4",
                "pre": "Đang có Combo mềm trong giỏ và đã chọn Charm 0đ. Khách xóa chiếc IQ4S.",
                "rule": "Combo bị hủy, Play 4 trở về giá bán lẻ thông thường. Quyền nhận 01 Charm 0đ theo Camera Play 4 vẫn ĐƯỢC GIỮ NGUYÊN.",
                "alt": "Thông báo: 'Combo an ninh đã hủy do giảm sản phẩm. Giá Play 4 quay về giá gốc. Ưu đãi 1 Charm 0đ vẫn được giữ'.",
                "biz_question": "Nếu sau này có loại Combo mà chỉ khi mua Combo mới có quà, Kinh doanh có muốn thu hồi quà khi khách xóa bớt món không?"
            },
            {
                "br": "BR-04",
                "scenario": "Mua kết hợp cả Combo lẫn mua lẻ: Mua 1 Combo (có 1 Play 4) VÀ thêm 2 Play 4 lẻ",
                "pre": "Giỏ có 1 Combo (chứa 1 Play 4) + 2 Camera Play 4 mua lẻ riêng.",
                "rule": "Cộng dồn quyền lợi: 1 Play 4 từ Combo + 2 Play 4 lẻ = Tổng cộng 3 Camera Play 4 → Cấp chính xác 3 suất nhận Charm 0đ.",
                "alt": "Giao diện hiển thị rõ: 'Bạn có 3 suất mua Charm 0đ (1 từ Combo An Ninh + 2 từ Camera mua lẻ)'.",
                "biz_question": "Có giới hạn số lượng tối đa khi khách vừa mua Combo vừa mua lẻ trong cùng một đơn hàng không?"
            }
        ]
    },
    {
        "module": "5. Dịch vụ bám kèm (Gắn với gói Cloud)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Điều kiện kép (Lệch số lượng): Mua 3 Camera Play 4 nhưng chỉ mua kèm 1 gói Cloud",
                "pre": "Chính sách yêu cầu điều kiện kép: Mua Camera Play 4 VÀ đăng ký gói Cloud mới được tặng Charm 0đ.",
                "rule": "Số lượng quà tính theo số nhỏ nhất (Hàm Min): 3 Camera nhưng chỉ có 1 Cloud → Chỉ được tặng đúng 01 Charm 0đ. 2 Camera còn lại không có Cloud thì không có quà 0đ.",
                "alt": "Hiển thị lời nhắc: 'Mua thêm 2 gói Cloud để nhận thêm 2 Charm 0đ cho 2 Camera còn lại [Chọn gói Cloud]'.",
                "biz_question": "Đối với 2 Camera không kèm Cloud, Kinh doanh có muốn cho phép khách mua Charm với giá giảm 50% để an ủi không?"
            },
            {
                "br": "BR-02",
                "scenario": "Thời hạn gói Cloud: Khách chọn gói Cloud 1 tháng thay vì gói 6 hoặc 12 tháng",
                "pre": "Chính sách quy định chỉ gói Cloud từ 6 tháng trở lên mới đủ điều kiện tặng Charm 0đ.",
                "rule": "Gói Cloud 1 tháng không đủ điều kiện nhận Charm 0đ. Chỉ khi chọn gói Cloud kỳ hạn >= 6 tháng mới mở suất Charm 0đ.",
                "alt": "Khi khách chọn gói 1 tháng: Hiển thị gợi ý 'Nâng cấp lên gói 6 tháng để nhận ngay Charm Play 4 trị giá 150.000đ hoàn toàn miễn phí'.",
                "biz_question": "Kỳ hạn gói Cloud tối thiểu để được tặng Charm 0đ chốt là 6 tháng hay 12 tháng?"
            },
            {
                "br": "BR-03",
                "scenario": "Hạ gói Cloud trong giỏ: Đang có 1 Cam + Cloud 6T (được 0đ), khách bấm đổi Cloud xuống 1T",
                "pre": "Đã có 1 Cam + Cloud 6T + Charm 0đ. Khách đổi thời hạn gói Cloud từ 6T xuống 1T.",
                "rule": "Hết điều kiện ưu đãi: Charm 0đ lập tức bị chuyển về giá bán lẻ gốc 150.000đ.",
                "alt": "Bảng thông báo xác nhận: 'Gói Cloud 1 tháng không đủ điều kiện nhận Charm 0đ. Phụ kiện Charm sẽ được chuyển về giá gốc 150.000đ. Bạn có muốn đổi không?'.",
                "biz_question": "Khi khách hạ gói dịch vụ, Kinh doanh muốn chuyển Charm về giá gốc hay tự động xóa Charm khỏi giỏ hàng?"
            },
            {
                "br": "BR-04",
                "scenario": "Hủy dịch vụ Cloud sau khi đã nhận quà / Hoàn cước Cloud",
                "pre": "Khách đã thanh toán đơn gồm Play 4 + Cloud 12T + Charm 0đ. Sau đó khách yêu cầu hủy gói Cloud.",
                "rule": "Khi khách hủy hợp đồng Cloud trước hạn: Số tiền hoàn cước sẽ bị KHẤU TRỪ giá trị niêm yết của Charm (150.000đ). Nếu tiền hoàn nhỏ hơn 150k thì hoàn 0đ.",
                "alt": "Nếu khách không đồng ý trừ tiền: Yêu cầu khách hoàn trả lại phụ kiện Charm còn nguyên hộp/nguyên seal về quầy giao dịch FPT.",
                "biz_question": "Kinh doanh có đồng ý đưa điều khoản ràng buộc này vào hợp đồng cung cấp dịch vụ Cloud để tránh tình trạng trục lợi quà tặng không?"
            }
        ]
    },
    {
        "module": "6. Gamification (Mốc mua sỉ 3 Cam)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Đạt mốc thưởng lớn: Đang có 2 Camera, khách bấm tăng lên 3 Camera",
                "pre": "Chính sách: Mua từ 3 Camera trở lên được tặng thêm 01 'Charm Bản Giới Hạn / Limited Edition 0đ'.",
                "rule": "Hệ thống tự động mở khóa và thêm ngay 01 Charm Limited Edition (0đ) vào giỏ hàng, đồng thời hạn mức Charm tiêu chuẩn tăng lên 3 chiếc.",
                "alt": "Hiển thị thông báo chúc mừng kèm hiệu ứng sinh động trên giỏ hàng để khách hào hứng.",
                "biz_question": "Nếu mẫu Charm Limited Edition bị hết hàng trong kho, Kinh doanh muốn thay thế bằng voucher dịch vụ Cloud hay nâng cấp quà tặng khác?"
            },
            {
                "br": "BR-02",
                "scenario": "Hụt mốc thưởng lớn: Đang có 3 Camera + Quà Limited, khách giảm Camera xuống 2",
                "pre": "Giỏ có 3 Camera + Quà tặng Charm Limited 0đ. Khách giảm số lượng Camera về 2.",
                "rule": "Không còn thỏa điều kiện: Hệ thống tự động thu hồi/xóa quà Charm Limited khỏi giỏ hàng (vì đây là phiên bản quà tặng độc quyền, không bán lẻ).",
                "alt": "Thông báo rõ: 'Số lượng Camera dưới 3, quà tặng Charm Limited Edition đã được tự động gỡ bỏ'.",
                "biz_question": "Có cần hiển thị cảnh báo trước khi khách bấm giảm không: 'Giảm số lượng sẽ làm mất quà tặng Limited độc quyền'?"
            },
            {
                "br": "BR-03",
                "scenario": "Hết quà Limited ngay lúc khách đang thanh toán",
                "pre": "Khách có 3 Camera + Charm Limited trong giỏ và bấm nút 'Thanh toán'. Kho vừa hết sạch quà Limited.",
                "rule": "Không chặn đơn hàng Camera của khách: Hệ thống xin lỗi và đề xuất gửi bù quà tặng sau 7 ngày làm việc hoặc cho phép đổi sang quà tặng khác tương đương.",
                "alt": "Bảng hỏi: 'Quà tặng Limited vừa hết hàng. Chúng tôi cam kết gửi bù quà miễn phí sau 7 ngày. Bạn có đồng ý tiếp tục đặt hàng không?'.",
                "biz_question": "Kinh doanh đồng ý giải pháp cam kết gửi bù quà sau để bảo vệ tỷ lệ chốt đơn bán Camera chính hay không?"
            },
            {
                "br": "BR-04",
                "scenario": "Chống đầu cơ gom hàng quà Limited",
                "pre": "Khách hàng hoặc đại lý tạo nhiều đơn hàng liên tục (mỗi đơn 3 Cam) để tích trữ quà Limited.",
                "rule": "Giới hạn tối đa: Mỗi tài khoản / Số điện thoại / Địa chỉ nhận hàng chỉ được nhận tối đa 02 Charm Limited trong toàn chiến dịch.",
                "alt": "Khi đã nhận đủ 2 quà Limited: Các đơn hàng sau mua 3 Cam chỉ nhận Charm tiêu chuẩn, không tặng thêm bản Limited.",
                "biz_question": "Kinh doanh muốn siết chặt giới hạn theo Số điện thoại hay Số CCCD/Tài khoản để đảm bảo quà đến tay người dùng thực tế?"
            }
        ]
    },
    {
        "module": "7. Kế toán & Nền tảng (Database & Vouchers)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Xuất hóa đơn điện tử VAT và ghi nhận chứng từ kế toán",
                "pre": "Đơn hàng thanh toán thành công gồm Camera Play 4 và Charm 0đ.",
                "rule": "Trên hóa đơn VAT và phiếu bán hàng thể hiện rõ: Charm Play 4 đơn giá 150.000đ - Tiền khuyến mại: -150.000đ - Thành tiền: 0đ theo đúng quy định đăng ký khuyến mại với Sở Công Thương.",
                "alt": "Hệ thống ghi nhận chi phí quà tặng vào ngân sách xúc tiến thương mại của bộ phận Marketing/Kinh doanh.",
                "biz_question": "Mẫu hóa đơn VAT điện tử gửi khách hàng đã được phòng Tài chính - Kế toán duyệt cách thể hiện dòng khuyến mại 0đ này chưa?"
            },
            {
                "br": "BR-02",
                "scenario": "Áp dụng kèm Mã giảm giá / Voucher toàn sàn (Ví dụ: Giảm 10% tổng đơn)",
                "pre": "Khách nhập mã Voucher 'GIAM10 - Giảm 10% tổng đơn' cho giỏ hàng có Camera và phụ kiện.",
                "rule": "Voucher giảm % chỉ áp dụng trên giá trị thực thu của Camera và khoản phụ thu (nếu có). Quà tặng 0đ không được tham gia tính giảm thêm.",
                "alt": "Hiển thị chi tiết: 'Voucher GIAM10 áp dụng giảm giá trên Camera Play 4 và phụ thu Charm'.",
                "biz_question": "Chương trình quà tặng Charm có được phép áp dụng chung với các voucher giảm giá/chiết khấu khác trên website không?"
            }
        ]
    },
    {
        "module": "8. Quản trị Tồn kho & Cạnh tranh giỏ hàng (Inventory Concurrency & OOS)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Hết hàng tức thời: Mẫu Charm đang chọn bị hết trong kho ngay trước lúc thanh toán",
                "pre": "Khách đang chọn Charm Mẫu A trong giỏ. Trong lúc chờ, khách khác đã mua hết tồn kho Mẫu A.",
                "rule": "Khi bấm 'Thanh toán', nếu mẫu A đã hết, hệ thống nhắc khách đổi sang mẫu Charm khác còn hàng. Không hủy đơn mua Camera của khách.",
                "alt": "Mẫu A bị làm mờ, gắn nhãn 'Vừa hết hàng'. Nổi bật nút 'Chọn mẫu khác thay thế'.",
                "biz_question": "Nếu tất cả các mẫu Charm đều hết hàng, Kinh doanh có đồng ý phát hành mã voucher trị giá 150k để khách mua phụ kiện ở đợt hàng sau không?"
            },
            {
                "br": "BR-02",
                "scenario": "Tồn kho không đủ số lượng mong muốn: Mua 3 Cam muốn 3 Charm A, nhưng kho chỉ còn 1 cái",
                "pre": "Kho còn 1 Charm A và nhiều Charm B, C. Khách muốn chọn cả 3 Charm Mẫu A.",
                "rule": "Giới hạn số lượng chọn tối đa của mỗi mẫu không vượt quá số lượng tồn kho thực tế. Mẫu A chỉ cho chọn tối đa 1 chiếc.",
                "alt": "Thông báo: 'Mẫu A chỉ còn 1 sản phẩm. Vui lòng chọn thêm 2 mẫu khác để nhận đủ 3 phần quà tặng'.",
                "biz_question": "Kinh doanh có đồng ý hiển thị số lượng tồn kho còn lại của từng mẫu phụ kiện để khách dễ dàng ra quyết định không?"
            },
            {
                "br": "BR-03",
                "scenario": "Để giỏ hàng quá lâu qua đêm (Chương trình khuyến mãi kết thúc)",
                "pre": "Khách bỏ Camera + Charm vào giỏ lúc đêm. Sáng hôm sau quay lại thanh toán thì chương trình tặng quà đã hết hạn.",
                "rule": "Quyền lợi và giá tiền được tính tại thời điểm bấm Đặt hàng. Khi chương trình kết thúc, giỏ hàng tự động cập nhật lại theo giá hiện hành.",
                "alt": "Thông báo rõ: 'Chương trình quà tặng Charm 0đ đã kết thúc. Giỏ hàng của bạn đã được cập nhật lại'.",
                "biz_question": "Có chính sách ngoại lệ nào gia hạn ưu đãi thêm vài giờ cho khách hàng đã lưu giỏ hàng trước thời điểm hết hạn không?"
            }
        ]
    },
    {
        "module": "9. Xung đột Khuyến mãi & Điểm thưởng FPT",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Camera Play 4 tham gia Flash Sale giá sốc",
                "pre": "Camera Play 4 giảm giá đặc biệt từ 800k còn 599k trong khung giờ Flash Sale.",
                "rule": "Theo cấu hình kinh doanh: Nếu Flash Sale giảm giá quá sâu, sản phẩm Flash Sale KHÔNG áp dụng kèm Charm 0đ.",
                "alt": "Trang Flash Sale ghi rõ: 'Giá sốc không áp dụng kèm quà tặng Charm 0đ'. Mua theo giá thường vẫn được tặng quà đầy đủ.",
                "biz_question": "Kinh doanh quyết định: Khi bán giá Flash Sale có kèm quà tặng Charm 0đ không, hay chỉ áp dụng khi bán giá niêm yết?"
            },
            {
                "br": "BR-02",
                "scenario": "Dùng Điểm thưởng FPT / Xu FPT Loyalty thanh toán phụ thu",
                "pre": "Khách có 50.000 điểm FPT Loyalty, muốn dùng điểm để cấn trừ khoản phụ thu 50k của Charm Premium.",
                "rule": "Cho phép dùng điểm thưởng FPT Loyalty để thanh toán các khoản phụ thu hoặc giá trị thanh toán thực tế (1 điểm = 1 VNĐ).",
                "alt": "Mục thanh toán hiển thị: '[x] Dùng 50.000 điểm FPT để thanh toán phụ thu (Số tiền cần trả: 0đ)'.",
                "biz_question": "Kinh doanh có đồng ý cho phép khách dùng điểm thưởng thành viên FPT Loyalty để trừ tiền phụ thu Charm Premium không?"
            }
        ]
    },
    {
        "module": "10. Vận chuyển & Giao nhận Đa kho",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Lệch kho hàng: Kho gần khách có Camera nhưng hết Charm (Charm ở kho khác)",
                "pre": "Kho gần khách (Hà Nội) có sẵn Camera nhưng hết Charm. Charm đang ở kho Đà Nẵng hoặc HCM.",
                "rule": "Hệ thống tự động tối ưu: Điều chuyển Charm về để giao chung 1 lần; HOẶC Tách làm 2 kiện giao riêng mà KHÔNG thu thêm bất kỳ phí vận chuyển nào của khách.",
                "alt": "Màn hình đặt hàng thông báo: 'Đơn hàng được chia làm 2 kiện do phụ kiện chuyển từ kho đặc biệt. Miễn phí vận chuyển cho phụ kiện quà tặng'.",
                "biz_question": "Kinh doanh chọn phương án nào: Tách làm 2 chuyến giao (FPT chịu ship phụ kiện) hay chờ gom đủ hàng mới giao một lần?"
            },
            {
                "br": "BR-02",
                "scenario": "Khách đặt Online và chọn nhận hàng tại Shop FPT gần nhà",
                "pre": "Khách đặt hàng trên web và chọn đến Shop FPT nhận hàng.",
                "rule": "Kiểm tra tồn kho tại Shop: Nếu Shop có sẵn Camera nhưng thiếu Charm, hệ thống báo thời gian điều chuyển Charm về Shop trước khi khách ra lấy.",
                "alt": "Thông báo: 'Cửa hàng có sẵn Camera. Phụ kiện Charm dự kiến có mặt tại Shop sau 24h. Chúng tôi sẽ gửi tin nhắn SMS khi trọn bộ sẵn sàng'.",
                "biz_question": "Khách có được phép lấy Camera trước tại quầy, còn quà tặng Charm sẽ gửi chuyển phát về tận nhà miễn phí sau không?"
            }
        ]
    },
    {
        "module": "11. Cổng thanh toán & Trạng thái đơn hàng",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Thanh toán Online thất bại hoặc Quá hạn chờ thanh toán (Quá 15 phút)",
                "pre": "Khách chọn thanh toán qua VNPAY/MoMo nhưng để quá 15 phút không hoàn tất.",
                "rule": "Hạn mức ưu đãi và tồn kho Charm được tạm giữ trong 15 phút. Sau 15 phút không thanh toán, đơn tự hủy và giải phóng tồn kho cho khách khác mua.",
                "alt": "Giao diện hiển thị: 'Giao dịch đã hết thời gian chờ thanh toán. Giỏ hàng của bạn đã được khôi phục để đặt lại'.",
                "biz_question": "Thời gian chờ thanh toán trực tuyến đối với đơn hàng có quà tặng nên là 15 phút hay 30 phút?"
            },
            {
                "br": "BR-02",
                "scenario": "Khách hủy đơn hàng thanh toán khi nhận hàng (COD) trước khi xuất kho",
                "pre": "Đơn hàng COD đang ở trạng thái 'Chờ xác nhận'. Khách bấm 'Hủy đơn hàng' trên web.",
                "rule": "Cho phép khách hủy đơn ngay lập tức nếu hàng chưa bàn giao cho shipper. Toàn bộ hạn mức mua quà và tồn kho phụ kiện được hoàn trả về hệ thống.",
                "alt": "Hiển thị danh sách lý do hủy đơn để khách phản hồi (Đổi ý, chọn nhầm mẫu Charm, muốn mua thêm Camera).",
                "biz_question": "Sau khi khách tự hủy đơn có quà tặng, có cần gửi tin nhắn kèm ưu đãi giữ chân khách hàng quay lại mua không?"
            }
        ]
    },
    {
        "module": "12. Đổi trả từng phần & Bảo hành (RMA & Warranty)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Bảo hành 1 đổi 1 Camera Play 4 do lỗi kỹ thuật của nhà sản xuất",
                "pre": "Camera bị lỗi phần cứng trong thời gian bảo hành chính hãng.",
                "rule": "Kỹ thuật viên / Cửa hàng đổi mới 01 Camera Play 4 tương đương cho khách. Khách KHÔNG phải nộp lại phụ kiện Charm đã tặng.",
                "alt": "Phiếu bảo hành ghi rõ: 'Đổi mới Camera Play 4 - Không thu hồi phụ kiện khuyến mại Charm'.",
                "biz_question": "Nếu phụ kiện Charm bị lỗi sản xuất (ví dụ gãy khớp nối), Kinh doanh có chính sách đổi mới phụ kiện trong vòng bao nhiêu ngày?"
            },
            {
                "br": "BR-02",
                "scenario": "Khách trả hàng Camera Play 4 để lấy lại tiền mặt",
                "pre": "Đơn hàng gồm 1 Cam (800k) + 1 Charm 0đ (giá niêm yết 150k). Sau 3 ngày khách yêu cầu trả Camera đòi lại tiền.",
                "rule": "Khách phải hoàn trả lại Camera kèm phụ kiện Charm còn nguyên seal/hộp. Nếu Charm đã bị mất hoặc hư hỏng, khấu trừ giá trị niêm yết của Charm (150.000đ) vào số tiền hoàn của Camera (Khách nhận lại 650.000đ).",
                "alt": "Charm Premium phụ thu 50k: Nếu chỉ trả Camera giữ Charm, hoàn tiền = 800k - (200k - 50k) = 650k.",
                "biz_question": "Kinh doanh chọn phương án nào: (A) Khấu trừ theo giá niêm yết 150k; (B) Khấu trừ theo giá vốn nhập hàng; hay (C) Bắt buộc trả đủ cả bộ mới cho hoàn tiền?"
            }
        ]
    },
    {
        "module": "13. Trải nghiệm Khách vãng lai & Đăng nhập tài khoản",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Khách vãng lai (chưa đăng nhập) chọn hàng rồi mới bấm Đăng nhập",
                "pre": "Khách chưa đăng nhập chọn 1 Cam + 1 Charm A (0đ). Sau đó bấm Đăng nhập. Tài khoản đã có sẵn 1 Cam từ trước.",
                "rule": "Hợp nhất giỏ hàng thông minh: Tổng số Camera = 1 (vãng lai) + 1 (tài khoản) = 2 Camera. Suất quà Charm 0đ tự động nâng lên 2. Giữ nguyên Charm A và mở thêm 1 ô quà thứ 2.",
                "alt": "Thông báo: 'Giỏ hàng đã được đồng bộ. Bạn hiện có 2 Camera và 2 suất nhận Charm 0đ! [Chọn thêm quà]'.",
                "biz_question": "Nếu giỏ hàng cũ trên tài khoản đã có sẵn Charm B, Kinh doanh muốn hệ thống tự gộp thành (Charm A + Charm B = 2 quà 0đ) luôn không?"
            },
            {
                "br": "BR-02",
                "scenario": "Khách đăng xuất tài khoản khi đang có giỏ hàng khuyến mãi",
                "pre": "Khách đang có giỏ hàng khuyến mãi Camera + Charm, sau đó bấm 'Đăng xuất'.",
                "rule": "Giỏ hàng khuyến mãi của tài khoản được lưu an toàn trên hệ thống. Trình duyệt công cộng được làm sạch giỏ hàng để bảo mật.",
                "alt": "Khi đăng nhập lại từ bất kỳ thiết bị nào, giỏ hàng cùng các quyền lợi ưu đãi quà tặng được phục hồi nguyên vẹn.",
                "biz_question": "Giỏ hàng khuyến mãi lưu trên tài khoản khách hàng nên được lưu giữ tối đa bao nhiêu ngày trước khi tự động làm mới?"
            }
        ]
    }
]

# Tạo Workbook Excel mới hoặc cập nhật vào file hiện tại
xlsx_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.xlsx"
tsv_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.tsv"
csv_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm_utf8.csv"
csv_std_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.csv"

wb = openpyxl.Workbook()
# Xóa sheet mặc định
ws_default = wb.active
wb.remove(ws_default)

# Đặt tên sheet chuẩn: Kich Ban Chuan - Tech Spec
ws = wb.create_sheet(title="Kich Ban Chuan - Tech Spec")

# Styles
font_title = Font(name="Times New Roman", size=16, bold=True, color="1B365D")
font_subtitle = Font(name="Times New Roman", size=12, italic=True, color="555555")
font_header = Font(name="Times New Roman", size=12, bold=True, color="FFFFFF")
font_section = Font(name="Times New Roman", size=13, bold=True, color="1B365D")
font_body = Font(name="Times New Roman", size=11, color="000000")
font_br = Font(name="Times New Roman", size=11, bold=True, color="004085")
font_q = Font(name="Times New Roman", size=11, italic=True, color="856404")

fill_header = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
fill_section = PatternFill(start_color="E8EEF5", end_color="E8EEF5", fill_type="solid")
fill_zebra = PatternFill(start_color="F8F9FA", end_color="F8F9FA", fill_type="solid")
fill_q = PatternFill(start_color="FFF3CD", end_color="FFF3CD", fill_type="solid")

thin_side = Side(style="thin", color="D0D7DE")
border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

# Tiêu đề bảng
ws.cell(1, 1, "BẢNG ĐẶC TẢ KỊCH BẢN GIỎ HÀNG - CHUẨN NGHIỆP VỤ & KINH DOANH (TECH SPEC)")
ws.cell(1, 1).font = font_title
ws.cell(2, 1, "Dự án: FPT Camera Play 4 & Phụ kiện Charm Promo Engine | Chuẩn hóa theo góc nhìn Senior BA & Product Owner")
ws.cell(2, 1).font = font_subtitle

headers = [
    "STT",
    "Mã Rule",
    "Nhóm Kịch Bản",
    "Tình Huống Mua Hàng (Customer Scenario)",
    "Điều Kiện Áp Dụng (Pre-conditions)",
    "Quy Tắc Nghiệp Vụ & Quyền Lợi KH (Business Logic & Pricing)",
    "Xử Lý Khi Có Thay Đổi (Alternative & Exception Flow)",
    "Câu Hỏi Khai Vấn & Mong Muốn Đội Kinh Doanh (Questions for Sales/Biz Team)"
]

header_row = 4
for col_idx, h in enumerate(headers, 1):
    c = ws.cell(header_row, col_idx, h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = border_cell
ws.row_dimensions[header_row].height = 42

current_row = 5
stt_counter = 1

tsv_rows = []
csv_rows = []

tsv_rows.append(headers)
csv_rows.append(headers)

for mod_idx, mod in enumerate(modules_biz, 1):
    # Dòng tiêu đề phân nhóm
    sec_cell = ws.cell(current_row, 1, f"PHẦN {mod_idx}: {mod['module'].upper()}")
    sec_cell.font = font_section
    sec_cell.fill = fill_section
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=len(headers))
    for c_i in range(1, len(headers) + 1):
        ws.cell(current_row, c_i).border = border_cell
        ws.cell(current_row, c_i).fill = fill_section
    ws.row_dimensions[current_row].height = 28
    current_row += 1
    
    for case in mod["cases"]:
        row_data = [
            stt_counter,
            case["br"],
            mod["module"],
            case["scenario"],
            case["pre"],
            case["rule"],
            case["alt"],
            case["biz_question"]
        ]
        
        tsv_rows.append(row_data)
        csv_rows.append(row_data)
        
        is_even = (stt_counter % 2 == 0)
        
        for col_idx, val in enumerate(row_data, 1):
            c = ws.cell(current_row, col_idx, val)
            c.font = font_body
            c.border = border_cell
            
            if is_even:
                c.fill = fill_zebra
                
            if col_idx == 1:
                c.alignment = Alignment(horizontal="center", vertical="top")
            elif col_idx == 2:
                c.alignment = Alignment(horizontal="center", vertical="top")
                c.font = font_br
            elif col_idx == 8:
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                c.font = font_q
                if not is_even:
                    c.fill = fill_q
            else:
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                
        ws.row_dimensions[current_row].height = 70
        current_row += 1
        stt_counter += 1

col_widths = {
    "A": 7,    # STT
    "B": 11,   # Mã Rule
    "C": 20,   # Nhóm Kịch Bản
    "D": 30,   # Tình Huống Mua Hàng
    "E": 26,   # Điều Kiện
    "F": 38,   # Quy Tắc Nghiệp Vụ
    "G": 32,   # Xử Lý Khi Có Thay Đổi
    "H": 36    # Câu Hỏi Khai Vấn Kinh Doanh
}

for col_letter, width in col_widths.items():
    ws.column_dimensions[col_letter].width = width

wb.save(xlsx_path)
print(f"Exported Excel to {xlsx_path} with sheet name: Kich Ban Chuan - Tech Spec")

with open(tsv_path, "w", encoding="utf-8") as f:
    for r in tsv_rows:
        cleaned = [str(cell).replace("\t", " ").replace("\r\n", " ").replace("\n", " ") for cell in r]
        f.write("\t".join(cleaned) + "\n")
print(f"Exported TSV to {tsv_path}")

with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    for r in csv_rows:
        writer.writerow(r)
print(f"Exported CSV UTF8 to {csv_path}")

with open(csv_std_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for r in csv_rows:
        writer.writerow(r)
print(f"Exported CSV to {csv_std_path}")

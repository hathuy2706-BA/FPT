# -*- coding: utf-8 -*-
"""
Script tạo bảng kịch bản chuẩn hóa bàn giao kỹ thuật (Tech Spec)
Dành cho tính năng Giỏ hàng Promotion: Camera Play4 & Phụ kiện Charm
Tuân thủ Rule 23: Mã Business Rule dạng BR-01, BR-02 reset theo từng tính năng
Font: Times New Roman, Căn chỉnh đẹp mắt, xuất ra XLSX, CSV và TSV
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import csv
import os

modules = [
    {
        "module": "1. Tổ hợp số lượng (Basic 1:1)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua 1 Cam Play4 và chọn +1 Charm Basic (Tỷ lệ 1:1 chuẩn)",
                "pre": "Giỏ hàng có 1 Camera Play4 (giá niêm yết). Kho còn hàng Charm Basic.",
                "rule": "1 Cam Play4 kích hoạt Quota mua 1 Charm Basic với giá 0đ. Hạn mức tối đa Charm 0đ = Số lượng Play4 trong giỏ hàng (Max_Free_Charm = Qty_Play4).",
                "backend": "Cart Engine tạo 2 line items: Line 1 = Cam Play4 (Price = P, is_main = true); Line 2 = Charm Basic (Price = 0, is_addon = true, parent_line_id = Line 1, promo_code = 'CHARM_0D').",
                "ui": "Block Extra Charm hiển thị tag 'Quà tặng 0đ (1/1)'. Nút [+] tại Charm Basic bị disable hoặc click tiếp sẽ hiển thị giá bán lẻ 150.000đ.",
                "exception": "Nếu Charm Basic hết hàng (OOS): Ẩn hoặc làm mờ variant đó, hiển thị nhãn 'Tạm hết hàng'."
            },
            {
                "br": "BR-02",
                "scenario": "Vượt hạn mức (M > N): Mua 1 Cam, khách chọn 2 Charm cùng Mẫu A",
                "pre": "Đã có 1 Play4 và 1 Charm A (0đ) trong giỏ. Khách nhấn [+] tiếp tại Charm A.",
                "rule": "Tách 2 Charm A thành 2 dòng riêng biệt: 01 chiếc tính giá 0đ (theo hạn mức Play4), 01 chiếc tính giá niêm yết gốc 150.000đ. Không tính giá trung bình cộng để đảm bảo tính pháp lý hóa đơn VAT.",
                "backend": "Tạo 2 line item trong Cart: Item 1: SKU Charm A, Qty = 1, Final_Price = 0đ (Linked to Cam). Item 2: SKU Charm A, Qty = 1, Final_Price = 150.000đ (Retail price, non-linked).",
                "ui": "Giỏ hàng hiển thị 2 dòng Charm A: Dòng 1 có badge 'Mua kèm Cam Play 4 - 0đ'; Dòng 2 có badge 'Mua thêm - 150.000đ'. Toast thông báo: 'Bạn đã dùng hết quota 0đ, sản phẩm thứ 2 áp dụng giá gốc'.",
                "exception": "Khách bấm [-] ở dòng nào thì trừ đúng dòng đó. Nếu xóa dòng 0đ, dòng 150k sẽ tự động chuyển thành dòng 0đ (Auto-promote)."
            },
            {
                "br": "BR-03",
                "scenario": "Vượt hạn mức (M > N): Mua 1 Cam, khách chọn 1 Charm A và 1 Charm B (Khác giá niêm yết)",
                "pre": "1 Cam Play4, khách tick chọn 1 Charm A (giá gốc 100k) và 1 Charm B (giá gốc 150k).",
                "rule": "Quy tắc Best-deal for Customer (Ưu tiên quyền lợi KH): Hệ thống tự động gán giá 0đ cho Charm có giá niêm yết cao nhất (Charm B - 150k), Charm còn lại (Charm A - 100k) tính giá gốc.",
                "backend": "Cart Pricing Engine sắp xếp mảng Add-on Charm theo Original_Price DESC: Gán discount 100% cho item đầu tiên trong hạn mức Quota. Item tiếp theo giữ nguyên giá bán lẻ.",
                "ui": "Charm B hiển thị 0đ (gạch ngang 150.000đ). Charm A hiển thị 100.000đ kèm ghi chú 'Giá bán lẻ'. Subtotal hiển thị rõ: Tiền Cam + 100.000đ.",
                "exception": "Nếu khách bỏ chọn Charm B, hệ thống tự động gán giá 0đ cho Charm A ngay lập tức (Real-time Re-calculate)."
            },
            {
                "br": "BR-04",
                "scenario": "Dưới hạn mức (M < N): Mua 3 Cam, chỉ chọn 1 Charm Mẫu A (M=1 < N=3)",
                "pre": "Giỏ hàng có 3 Play4 (Quota = 3), nhưng khách chỉ chọn 1 Charm A.",
                "rule": "Không ép buộc mua đủ Quota. Khách có quyền mua ít hơn hạn mức. Hệ thống hiển thị cảnh báo gợi ý (Nudge) nhưng vẫn cho phép tiếp tục thanh toán.",
                "backend": "Cart State: Total_Quota = 3, Used_Quota = 1, Remaining_Quota = 2. Cho phép Checkout bình thường mà không chặn validation.",
                "ui": "Hiển thị Banner nhắc nhở tinh tế tại Cart: 'Bạn còn 2 suất nhận Charm 0đ. [Chọn thêm quà]'. Nút 'Thanh toán' vẫn sáng rõ, không chặn luồng thanh toán của khách.",
                "exception": "Khách bỏ qua và thanh toán: Đơn hàng chỉ xuất 3 Cam + 1 Charm. Quyền lợi 2 Charm còn lại hết hiệu lực khi đơn hàng thanh toán thành công."
            },
            {
                "br": "BR-05",
                "scenario": "Dưới hạn mức (M = 0): Mua 2 Cam nhưng không chọn bất kỳ Charm nào",
                "pre": "2 Cam Play4 trong giỏ hàng, khách không tick vào bất kỳ phụ kiện Charm nào.",
                "rule": "Quyền mua Charm 0đ là ưu đãi 'Mua Kèm Ngay' (Instant Add-on), KHÔNG quy đổi thành tiền mặt, KHÔNG lưu thành Voucher bảo lưu cho đơn hàng sau.",
                "backend": "Cart không chứa line item Charm nào. Database đơn hàng lưu cờ 'has_claimed_charm = false'. Không phát sinh mã Voucher trong bảng Promo_User.",
                "ui": "Tại bước Checkout, hiển thị Popup xác nhận ngắn (Micro-modal): 'Bạn đang bỏ qua 2 Charm 0đ tặng kèm. Bạn có chắc muốn tiếp tục? [Tiếp tục thanh toán] [Chọn quà ngay]'.",
                "exception": "Nếu khách click 'Tiếp tục thanh toán', đóng modal và chuyển cổng thanh toán. Sau này khách liên hệ CSKH khiếu nại đòi quà sẽ xử lý theo quy chế CSKH đặc biệt."
            },
            {
                "br": "BR-06",
                "scenario": "Đồng bộ ngược (Sync Down): Đang có 2 Cam + 2 Charm A, giảm Cam xuống 1",
                "pre": "Giỏ có 2 Cam Play4 + 2 Charm A (cả 2 đều 0đ). Khách bấm [-] ở dòng Cam Play4.",
                "rule": "Quota giảm từ 2 xuống 1. Giữ nguyên 2 Charm A nhưng tự động chuyển chiếc thứ 2 thành giá niêm yết (150.000đ). KHÔNG tự ý xóa bớt sản phẩm của khách trừ khi hết hàng.",
                "backend": "Hệ thống gọi Event 'onUpdateCartQuantity': Cam Qty = 1 -> New_Quota = 1. Cart Engine split 2 Charm A thành: 1 Charm A (0đ) + 1 Charm A (150k). Cập nhật Subtotal.",
                "ui": "Cập nhật tức thì số tiền tổng đơn (+150k). Hiển thị Toast cảnh báo màu cam: 'Số lượng Camera giảm còn 1, chiếc Charm thứ 2 đã được chuyển về giá gốc 150.000đ'.",
                "exception": "Nếu cấu hình Biz chọn giải pháp 'Tự động giảm Charm theo Cam': Giảm Charm A về 1 và thông báo 'Hệ thống đã tự động điều chỉnh quà tặng tương ứng'."
            },
            {
                "br": "BR-07",
                "scenario": "Đồng bộ ngược: Đang có 2 Cam + 2 Charm khác mẫu (1 A, 1 B), giảm Cam xuống 1",
                "pre": "Giỏ có 2 Cam + 1 Charm A (0đ) + 1 Charm B (0đ). Khách giảm Cam xuống 1.",
                "rule": "Áp dụng nguyên tắc Giữ món giá trị nhất làm 0đ, món còn lại tính giá gốc. Nếu 2 món bằng giá, áp dụng FIFO (món chọn trước được 0đ, món chọn sau tính tiền) hoặc hiển thị Modal cho khách chọn.",
                "backend": "So sánh Original_Price(A) vs Original_Price(B): Nếu B > A, giữ B là 0đ, A tính tiền gốc. Nếu A == B, giữ món có added_timestamp nhỏ hơn làm 0đ.",
                "ui": "Hiển thị modal lựa chọn hoặc tự động áp dụng kèm thông báo rõ ràng: 'Bạn chỉ còn 1 suất Charm 0đ. Charm [Tên mẫu] được áp dụng 0đ, mẫu còn lại tính giá niêm yết'.",
                "exception": "Khách có thể click trực tiếp vào nút radio trên giao diện giỏ hàng để đảo quyền 0đ giữa Mẫu A và Mẫu B mà không cần xóa đi chọn lại."
            },
            {
                "br": "BR-08",
                "scenario": "Phân bổ mẫu số lượng lớn: Mua 10 Cam, chia Quota cho cả 3 mẫu A, B, C",
                "pre": "Khách mua số lượng lớn (N=10 Cam Play4, Quota = 10).",
                "rule": "Hỗ trợ nhập trực tiếp số lượng vào ô Textbox (Input Stepper) thay vì chỉ bấm nút [+]. Tổng số lượng Charm 0đ của các mẫu không được vượt quá 10.",
                "backend": "Validate tổng: Sum(Qty_Charm_0D) <= Qty_Play4. Nếu Sum > Qty_Play4, chặn submit hoặc tự động chuyển số dư dôi sang giá bán lẻ.",
                "ui": "Input field cho phép gõ số (type='number', min=0, max=10). Kèm thanh tiến trình trực quan: 'Đã phân bổ: 7/10 Charm 0đ' (Progress bar chuyển màu xanh khi đủ 10/10).",
                "exception": "Khách gõ số âm, ký tự chữ hoặc số thập phân: Input tự động validate về 0 hoặc làm tròn số nguyên gần nhất (Sanitize input)."
            },
            {
                "br": "BR-09",
                "scenario": "Đổi mẫu phụ kiện: Đang có 3 Cam + 3 Charm (1A, 1B, 1C), muốn đổi C thành A",
                "pre": "Đã chọn tối đa 3 Charm (1A, 1B, 1C). Quota 0đ khả dụng = 0.",
                "rule": "Nếu khách bấm [+] ở Mẫu A khi đã hết Quota: Cho phép tăng nhưng hiển thị giá 150k. Hoặc nếu khách bấm [-] ở Mẫu C về 0 rồi [+] Mẫu A thì Mẫu A được gán 0đ.",
                "backend": "Engine tính toán độc lập: Khi Charm C giảm về 0, Quota khả dụng tăng từ 0 lên 1. Khi Charm A tăng từ 1 lên 2, slot 0đ thứ 2 được gán cho Charm A.",
                "ui": "UI mượt mà, cập nhật giỏ hàng Real-time không cần reload trang. Icon [-] tại Mẫu C có tooltip 'Bỏ bớt để đổi sang mẫu khác'.",
                "exception": "Nếu Mẫu A vừa hết hàng trong lúc khách thao tác đổi: Báo lỗi 'Mẫu A vừa hết hàng, vui lòng giữ mẫu cũ hoặc chọn mẫu khác'."
            },
            {
                "br": "BR-10",
                "scenario": "Xóa sản phẩm chính: Đang có 1 Cam + 1 Charm 0đ, khách bấm Xóa Camera khỏi giỏ",
                "pre": "1 Cam Play4 + 1 Charm 0đ trong giỏ hàng. Khách nhấn nút 'Xóa' (Remove icon) tại dòng Cam.",
                "rule": "Quy tắc Ràng buộc chặt (Strict Binding): Charm 0đ không thể tồn tại độc lập trong giỏ. Xóa Cam sẽ đồng thời tự động xóa Charm 0đ, HOẶC bật xác nhận chuyển Charm sang giá bán lẻ.",
                "backend": "Cascade Delete: OnDelete(Parent_Play4_Line) -> Delete all child_lines where parent_line_id == Play4.LineID and is_promo == true.",
                "ui": "Hiển thị Modal cảnh báo: 'Xóa Camera Play4 sẽ đồng thời xóa quà tặng Charm 0đ đính kèm. Bạn có muốn giữ lại Charm với giá gốc 150.000đ không? [Xóa tất cả] [Giữ Charm giá gốc]'.",
                "exception": "Nếu khách bấm 'Xóa tất cả': Giỏ hàng trống rỗng. Nếu khách bấm 'Giữ Charm giá gốc': Giỏ giữ lại Charm với giá niêm yết 150.000đ."
            }
        ]
    },
    {
        "module": "2. Phụ thu nâng cấp (Charm Premium +50k)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Mua hỗn hợp Basic & Premium: Mua 2 Cam, chọn 1 Basic (0đ) + 1 Premium (+50k)",
                "pre": "2 Cam Play4 (Quota = 2). Kho còn cả mẫu Basic và mẫu Premium.",
                "rule": "1 Cam đổi được 1 Charm Basic 0đ HOẶC nâng cấp lên Charm Premium phụ thu +50.000đ/chiếc (thay vì giá gốc 200.000đ).",
                "backend": "Line 1: Cam Play4 x2; Line 2: Charm Basic (Price = 0đ, promo_type = 'FREE'); Line 3: Charm Premium (Price = 50.000đ, promo_type = 'UPGRADE_SURCHARGE', linked_parent = Cam).",
                "ui": "Hiển thị rõ ràng: Charm Basic: 0đ (Tiết kiệm 150.000đ); Charm Premium: 50.000đ (Tiết kiệm 150.000đ - Giá gốc 200.000đ). Phụ thu hiển thị thành dòng riêng trong bảng tóm tắt đơn.",
                "exception": "Kế toán: Khoản 50.000đ được hạch toán vào doanh thu của SKU Charm Premium (VAT 8% hoặc 10% theo quy định phụ kiện)."
            },
            {
                "br": "BR-02",
                "scenario": "Vượt Quota hỗn hợp: Mua 1 Cam, chọn 1 Basic + 1 Premium (M=2 > N=1)",
                "pre": "1 Cam Play4 (Quota = 1). Khách chọn cả 1 Basic và 1 Premium.",
                "rule": "Áp dụng công thức tối ưu hóa chiết khấu cho khách hàng: Áp dụng suất ưu đãi cho món có tỷ lệ/giá trị giảm cao nhất. Premium ưu đãi phụ thu 50k (giảm 150k), Basic tính giá gốc 150k; HOẶC Basic 0đ (giảm 150k), Premium tính giá gốc 200k. Tổng tiền như nhau (200k phụ kiện).",
                "backend": "Hệ thống gán Quota 1 cho Charm Basic (0đ) + Charm Premium tính giá gốc 200.000đ. Tổng tiền phụ kiện = 200.000đ.",
                "ui": "Hiển thị chi tiết: 'Charm Basic: 0đ (Theo Cam Play4)'; 'Charm Premium: 200.000đ (Giá bán lẻ)'. Kèm gợi ý: 'Mua thêm 1 Camera để được nâng cấp Charm Premium chỉ 50.000đ'.",
                "exception": "Nếu khách đổi ý muốn Premium là 50k và Basic là 150k, tổng tiền giỏ hàng vẫn bằng 200k, không làm sai lệch doanh thu."
            },
            {
                "br": "BR-03",
                "scenario": "Swap / Đổi mẫu: Đang có 1 Cam + 1 Basic (0đ), đổi sang Premium (+50k)",
                "pre": "Giỏ có 1 Cam + 1 Basic 0đ. Khách tick chọn sang mẫu Premium.",
                "rule": "Hệ thống tự động hủy chọn Basic và kích hoạt mức phụ thu 50.000đ cho Premium. Subtotal đơn hàng nhảy ngay lập tức (+50.000đ).",
                "backend": "API /cart/update-item: Xóa Line Basic 0đ, Insert Line Premium 50k. Re-calculate Tax, Shipping, Subtotal và trả về Cart JSON mới trong < 200ms.",
                "ui": "Animation chuyển đổi mượt mà. Số tiền tổng thanh toán nhảy số (Count-up animation) +50.000đ. Hiển thị tooltip: 'Đã nâng cấp lên phiên bản Charm Premium'.",
                "exception": "Mất kết nối mạng khi đang đổi: Hiển thị toast 'Chưa cập nhật được giỏ hàng, vui lòng thử lại', giữ nguyên trạng thái cũ."
            },
            {
                "br": "BR-04",
                "scenario": "Auto-sync Up: Đang có 1 Cam + 1 Premium (+50k), tăng Cam lên 2",
                "pre": "Giỏ có 1 Cam + 1 Premium (+50k). Khách bấm [+] tăng Cam lên 2.",
                "rule": "Giữ nguyên 1 Premium (+50k) và hiển thị thêm 01 Slot quà tặng trống (Empty Gift Slot) để khách tự chọn tiếp. KHÔNG tự động nhân đôi Premium thành +100k nếu khách chưa xác nhận.",
                "backend": "Play4 Qty = 2 -> Total_Quota = 2. Current_Used_Quota = 1 (Premium). Available_Quota = 1. Giữ nguyên Line Premium Qty = 1.",
                "ui": "Thẻ 'Phụ kiện mua kèm' hiển thị: 1 Premium (+50.000đ) và 1 ô 'Chọn thêm 1 Charm 0đ hoặc Premium [Chọn ngay]'.",
                "exception": "Nếu khách không chọn thêm slot thứ 2, đơn hàng chỉ có 1 Charm Premium + 50k, thanh toán bình thường."
            },
            {
                "br": "BR-05",
                "scenario": "Sync-down: Đang có 2 Cam + 1 Basic (0đ) + 1 Premium (+50k), giảm Cam xuống 1",
                "pre": "Giỏ có 2 Cam + 1 Basic + 1 Premium. Khách bấm [-] giảm Cam về 1.",
                "rule": "Bảo vệ quyền lợi khách hàng: Ưu tiên giữ lại suất Charm Basic 0đ, đẩy Charm Premium về giá niêm yết bán lẻ gốc (200.000đ). Hoặc mở popup cho khách tự quyết định giữ món nào.",
                "backend": "Quota rớt về 1: Line Basic giữ giá 0đ; Line Premium mất cờ promo, Price update từ 50.000đ lên 200.000đ.",
                "ui": "Popup thông báo nhanh: 'Số lượng Cam giảm còn 1. Ưu đãi 0đ được giữ cho Charm Basic. Charm Premium được tính theo giá bán lẻ 200.000đ. [Đồng ý] [Đổi sang ưu đãi Premium 50k]'.",
                "exception": "Khách chọn đổi sang Premium 50k: Hệ thống gán 50k cho Premium và xóa hoặc tính 150k cho Basic."
            },
            {
                "br": "BR-06",
                "scenario": "Chính sách trả hàng (Refund & RMA) có phụ thu nâng cấp",
                "pre": "Đơn hàng hoàn tất gồm 1 Cam Play4 (800k) + 1 Charm Premium (50k). Khách trả Cam, giữ Charm.",
                "rule": "Khách trả Cam Play4 nhưng giữ Charm Premium: Charm Premium không còn điều kiện mua kèm, bị tính theo giá bán lẻ gốc 200.000đ. Số tiền hoàn lại cho Cam = Giá Cam (800k) - Chênh lệch Charm (200k - 50k = 150k) = 650.000đ.",
                "backend": "Module RMA / Refund: Refund_Amount = Return_Item_Value - (Retail_Price_Kept_Addon - Paid_Price_Kept_Addon). Sinh biên bản cấn trừ tự động.",
                "ui": "Màn hình yêu cầu trả hàng hiển thị rõ chiết tính hoàn tiền để khách hiểu minh bạch trước khi nhấn xác nhận gửi yêu cầu.",
                "exception": "Nếu khách trả cả Cam và Charm Premium: Hoàn đủ 100% số tiền thực thu (850.000đ) vào tài khoản thanh toán ban đầu."
            }
        ]
    },
    {
        "module": "3. Bán chéo số lượng (Mua thêm Charm 2, 3 giảm 50%)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Xung đột giá: 1 Cam, chọn 3 Charm giá gốc khác nhau (100k, 150k, 200k)",
                "pre": "Chính sách: Mua 1 Cam được 1 Charm 0đ + tối đa 2 Charm tiếp theo giảm 50%. Khách chọn 3 Charm (100k, 150k, 200k).",
                "rule": "Thuật toán tham lam (Greedy Best-deal): Sắp xếp giá giảm dần (200k > 150k > 100k). Chiếc 200k áp dụng 0đ (giảm 200k). Chiếc 150k giảm 50% (còn 75k). Chiếc 100k giảm 50% (còn 50k). Tổng phụ kiện = 125k (Tiết kiệm tối đa 325k).",
                "backend": "Sort items by price DESC: Item[0].discount = 100%; Item[1].discount = 50%; Item[2].discount = 50%. Lưu các discount_amount tương ứng từng dòng.",
                "ui": "Hiển thị nhãn trực quan từng món: Charm 200k -> 'Tặng 0đ'; Charm 150k -> 'Giảm 50% còn 75k'; Charm 100k -> 'Giảm 50% còn 50k'. Kèm tổng tiết kiệm: 'Đã tiết kiệm 325.000đ'.",
                "exception": "Nếu doanh nghiệp muốn tối đa hóa doanh thu (Profit-protection): Đảo ngược lại (chiếc rẻ nhất 0đ). Rule này cần được khai báo linh hoạt qua biến cấu hình 'PROMO_DISCOUNT_STRATEGY = MAX_SAVING | MAX_REVENUE' tại QLCS."
            },
            {
                "br": "BR-02",
                "scenario": "Vượt trần ưu đãi (Over-limit): Mua 1 Cam, chọn 5 Charm",
                "pre": "1 Cam Play4. Hạn mức tối đa: 1 Charm 0đ + 2 Charm giảm 50%. Khách chọn tổng cộng 5 Charm.",
                "rule": "Chiếc thứ 1: 0đ. Chiếc thứ 2 và 3: Giảm 50%. Chiếc thứ 4 và thứ 5: Tính nguyên giá niêm yết 100%.",
                "backend": "Quota kiểm soát: Quota_Free = 1, Quota_Discount_50 = 2, Over_Items = Remaining. Phân bổ tuần tự theo giá giảm dần vào các nhóm quota.",
                "ui": "Nhóm Charm thứ 4, 5 hiển thị giá gốc không có badge giảm giá. Hiển thị thông báo nhỏ: 'Bạn đã đạt giới hạn tối đa 3 Charm ưu đãi. Sản phẩm thứ 4 trở đi áp dụng giá niêm yết'.",
                "exception": "Nếu khách mua thêm Cam thứ 2: Quota mở rộng thành 2 Charm 0đ + 4 Charm 50%, chiếc thứ 4 và 5 tự động chuyển sang hưởng giảm 50% ngay lập tức."
            },
            {
                "br": "BR-03",
                "scenario": "Xóa sản phẩm chính khi đang có Charm 0đ và Charm 50%",
                "pre": "Giỏ có 1 Cam + 1 Charm 0đ + 1 Charm 50%. Khách xóa Camera khỏi giỏ.",
                "rule": "Toàn bộ ưu đãi mua kèm bị vô hiệu lực ngay lập tức. Hệ thống hiển thị cảnh báo và chuyển toàn bộ các Charm về giá niêm yết 100% nếu khách muốn giữ giỏ, hoặc xóa toàn bộ.",
                "backend": "Trigger 'onRemoveParent': Reset toàn bộ promo_code liên kết, cập nhật unit_price của các Charm về base_price.",
                "ui": "Hiển thị Modal: 'Xóa Camera sẽ làm mất toàn bộ quyền mua Charm 0đ và giảm 50%. Bạn có muốn tiếp tục? [Đồng ý xóa hết] [Chuyển Charm về giá gốc]'.",
                "exception": "Nếu khách chọn 'Đồng ý xóa hết': Clear giỏ hàng sạch sẽ."
            },
            {
                "br": "BR-04",
                "scenario": "Dịch chuyển tầng giá (Shift-rule): Giảm Cam từ 2 xuống 1",
                "pre": "Giỏ có 2 Cam + 2 Charm (0đ) + 2 Charm (50%). Khách bấm giảm Cam xuống 1.",
                "rule": "Hạn mức mới: 1 Charm 0đ + 2 Charm 50% + 1 Charm giá gốc. Một chiếc Charm từ nhóm 0đ sẽ tự động dịch chuyển rơi xuống nhóm 50%, và một chiếc từ nhóm 50% sẽ dịch chuyển rơi về nhóm giá gốc 100%.",
                "backend": "Re-run pricing pipeline: Phân loại lại 4 món Charm theo thứ tự giá trị: 1 chiếc 0đ, 2 chiếc 50%, 1 chiếc 100%. Clear cache session giỏ hàng và lưu state mới.",
                "ui": "Thông báo toast nổi bật: 'Đã điều chỉnh lại ưu đãi phụ kiện theo số lượng Camera mới'. Giá tổng đơn cập nhật tức thì.",
                "exception": "Tránh giật lag giao diện (flickering): Sử dụng skeleton loading hoặc debounce 300ms khi người dùng nhấn nút tăng giảm số lượng liên tục."
            },
            {
                "br": "BR-05",
                "scenario": "Vận hành đóng gói & Kho (WMS) đối với đơn hàng đa chính sách giá",
                "pre": "Đơn hàng thanh toán thành công gồm 1 Cam + 1 Charm 0đ + 2 Charm 50%.",
                "rule": "Đơn hàng được đẩy xuống hệ thống Kho (WMS) dưới dạng CÙNG MỘT KIỆN HÀNG (Single Shipment) nếu các sản phẩm có cùng kho xuất, KHÔNG tách kiện theo chính sách giá.",
                "backend": "Order Management System (OMS) đóng gói payload gửi WMS: Mảng OrderLines chứa đủ 4 items, mỗi item có mã SKU thực tế và trường unit_price tương ứng để in phiếu xuất kho và hóa đơn.",
                "ui": "Trang theo dõi đơn hàng hiển thị 1 mã vận đơn duy nhất cho cả Camera và 3 phụ kiện Charm đi kèm.",
                "exception": "Nếu kho hết Charm tại địa điểm gần khách nhất: Hệ thống OMS kiểm tra phân bổ kho (Inventory Routing) trước khi quyết định gộp đơn hay điều chuyển nội bộ."
            }
        ]
    },
    {
        "module": "4. Combo Booster (Bundle Play4 + Dòng khác)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Nhận diện Bundle đóng gói sẵn (Hard Bundle): Mua Combo Play4 + IQ4S",
                "pre": "Gian hàng mở bán mã SKU Combo đóng gói sẵn 'Combo An Ninh: Play4 + IQ4S'.",
                "rule": "Trong SKU Combo có chứa 01 thiết bị Play4, do đó Combo này được kích hoạt đúng 01 Quota mua Charm 0đ (hoặc theo cấu hình khai báo của QLCS cho mã Combo này).",
                "backend": "Product Service phân rã BOM (Bill of Materials) của Combo: Detect component SKU == Play4 -> Tích lũy Quota Charm = 1.",
                "ui": "Trang chi tiết sản phẩm Combo hiển thị box 'Quà tặng kèm: Tặng 01 Charm Play4 tự chọn'. Vào giỏ hàng, hiển thị slot chọn Charm 0đ tương ứng.",
                "exception": "Nếu QLCS khai báo Combo này đã có khuyến mãi sâu khác và gắn flag 'exclude_charm_promo = true', hệ thống không cấp Quota Charm 0đ."
            },
            {
                "br": "BR-02",
                "scenario": "Gom Combo mềm (Soft Bundle): Khách thêm 1 Play4 lẻ + 1 IQ4S lẻ vào giỏ",
                "pre": "Khách thêm 1 Play4 lẻ và 1 IQ4S lẻ vào giỏ hàng riêng biệt.",
                "rule": "Auto-detect Bundle: Hệ thống tự động nhận diện cặp đôi sản phẩm hợp lệ, áp dụng giá ưu đãi Combo (nếu có) và unlock đầy đủ các quyền lợi quà tặng tương ứng của Combo.",
                "backend": "Promotion Engine quét rule Combo: Match Play4 + IQ4S -> Tự động gắn tag Virtual_Bundle_ID, cấp Quota Charm = 1.",
                "ui": "Hiển thị Badge nổi bật trong Cart: 'Đã tự động ghép Combo An Ninh - Tiết kiệm thêm 100k + Tặng 1 Charm 0đ'.",
                "exception": "Nếu khách không muốn ghép Combo (muốn áp dụng voucher lẻ khác): Cung cấp nút 'Tách Combo' trong giỏ hàng."
            },
            {
                "br": "BR-03",
                "scenario": "Phá vỡ Bundle (Un-bundle): Khách xóa bớt IQ4S khỏi Combo mềm",
                "pre": "Đang có Soft-bundle (Play4 + IQ4S) và đã chọn Charm 0đ. Khách xóa IQ4S.",
                "rule": "Combo bị phá vỡ, Play4 trở về trạng thái mua lẻ. Do Play4 mua lẻ vẫn có chính sách tặng 1 Charm 0đ nên quyền mua Charm 0đ vẫn ĐƯỢC GIỮ NGUYÊN.",
                "backend": "Virtual_Bundle_ID bị xóa. Line Play4 revert về đơn giá lẻ ban đầu. Quota Charm được re-evaluate theo rule Play4 lẻ: Quota = 1 (Không thay đổi).",
                "ui": "Thông báo: 'Combo an ninh đã bị hủy do xóa bớt sản phẩm. Giá Play4 quay về giá gốc. Ưu đãi 1 Charm 0đ theo Play4 vẫn được giữ'.",
                "exception": "Nếu Combo ban đầu là điều kiện duy nhất để tặng Charm: Khi phá combo, Charm 0đ lập tức bị thu hồi hoặc chuyển về giá gốc."
            },
            {
                "br": "BR-04",
                "scenario": "Tổ hợp số lượng Lẻ & Combo: Mua 1 Combo (Play4 + IQ4S) VÀ thêm 2 Play4 lẻ",
                "pre": "Giỏ có 1 Combo (có 1 Play4) + 2 Play4 mua lẻ riêng.",
                "rule": "Cộng dồn Quota: 1 Play4 từ Combo + 2 Play4 mua lẻ = Tổng cộng 3 Play4 -> Cấp chính xác 3 Quota mua Charm 0đ.",
                "backend": "Total_Quota = Quota(Combo) + Quota(Lẻ) = 1 + 2 = 3. Lưu biến tổng này trong Cart Context.",
                "ui": "Giao diện hiển thị rõ ràng: 'Bạn có 3 suất mua Charm 0đ (1 từ Combo An Ninh + 2 từ Camera Play4)'. Giúp khách không bị bối rối hoặc nghi ngờ sai sót.",
                "exception": "Xóa 2 Play4 lẻ: Quota rớt từ 3 xuống 1, kích hoạt luồng Sync-down giảm Charm tương ứng."
            }
        ]
    },
    {
        "module": "5. Dịch vụ bám kèm (Gắn với gói Cloud)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Lệch số lượng điều kiện kép: Mua 3 Cam Play4 nhưng chỉ mua kèm 1 gói Cloud",
                "pre": "Chương trình yêu cầu điều kiện kép: 'Mua Cam Play4 VÀ đăng ký gói Cloud mới được tặng Charm 0đ'.",
                "rule": "Lấy hàm MIN (Min-matching Rule): Quota Charm 0đ = MIN(Số lượng Play4, Số lượng gói Cloud) = MIN(3, 1) = 1 Charm 0đ. 2 Cam còn lại không có Cloud đi kèm nên không có Charm 0đ.",
                "backend": "Eligible_Quota = min(count(Play4), count(Eligible_Cloud_Subscriptions)). Kết quả = 1.",
                "ui": "Hiển thị: 'Bạn được nhận 1 Charm 0đ. Mua thêm 2 gói Cloud để nhận thêm 2 Charm 0đ cho 2 Camera còn lại [Chọn gói Cloud]'.",
                "exception": "Nếu 2 Cam còn lại muốn mua Charm theo chính sách bán chéo (giảm 50%): Hệ thống cho phép mua tối đa theo hạn mức bán chéo tương ứng."
            },
            {
                "br": "BR-02",
                "scenario": "Thay đổi điều kiện kỳ hạn dịch vụ Cloud: Cloud 1 tháng vs Cloud 6/12 tháng",
                "pre": "Chính sách quy định chỉ gói Cloud từ 6 tháng trở lên mới đủ điều kiện tặng Charm 0đ.",
                "rule": "Chỉ kích hoạt Quota Charm 0đ khi gói Cloud có duration >= 6 tháng. Gói Cloud 1 tháng không đủ điều kiện.",
                "backend": "Validate: Cloud_Item.duration_months >= 6. Return is_eligible = true/false.",
                "ui": "Khi khách chọn gói Cloud 1 tháng: Hiển thị tooltip 'Nâng cấp lên gói 6 tháng để nhận ngay Charm Play4 trị giá 150.000đ hoàn toàn miễn phí'.",
                "exception": "Khách chọn gói Cloud 1 tháng: Không có slot Charm 0đ, các Charm trong giỏ hiển thị giá bán lẻ bình thường."
            },
            {
                "br": "BR-03",
                "scenario": "Hạ gói Cloud: Đang có 1 Cam + Cloud 6T (được Charm 0đ), đổi Cloud xuống 1T",
                "pre": "Đã có 1 Cam + Cloud 6T + Charm 0đ. Khách click đổi kỳ hạn Cloud từ 6T xuống 1T.",
                "rule": "Tước quyền ưu đãi (Revoke Privilege): Charm 0đ lập tức không còn thỏa điều kiện, tự động chuyển về giá niêm yết 150.000đ.",
                "backend": "Trigger 'onSubscriptionPlanChange': Check validity -> Thấy không còn gói Cloud >= 6T -> Update Charm Line Item về full price 150k.",
                "ui": "Modal cảnh báo: 'Gói Cloud 1 tháng không đủ điều kiện nhận Charm 0đ. Phụ kiện Charm sẽ được chuyển về giá gốc 150.000đ. Bạn có muốn đổi không? [Xác nhận đổi] [Giữ gói 6 tháng]'.",
                "exception": "Nếu khách xác nhận đổi: Cập nhật Subtotal tăng 150k và đổi thời hạn Cloud."
            },
            {
                "br": "BR-04",
                "scenario": "Hủy dịch vụ Cloud sau thanh toán / Hoàn tiền Cloud",
                "pre": "Khách đã mua đơn hàng gồm Play4 + Cloud 12T + Charm 0đ và thanh toán xong.",
                "rule": "Khách yêu cầu hủy gói Cloud trong thời gian cam kết: Hệ thống xử lý hoàn cước Cloud theo chính sách nhà mạng FPT Telecom sau khi ĐÃ TRỪ giá trị niêm yết của quà tặng Charm (150.000đ).",
                "backend": "Billing & Subscription System: Refund_Cloud = Cloud_Remaining_Value - Charm_Original_Price. Nếu giá trị hoàn < 150k, số tiền hoàn = 0đ và khóa cước.",
                "ui": "CSKH Tool / Portal FPT: Hiển thị cảnh báo đơn hàng có kèm quà tặng Charm để nhân viên tư vấn giải thích điều khoản thu hồi cho khách.",
                "exception": "Khách không đồng ý trừ tiền: Chặn thao tác hủy gói Cloud hoặc yêu cầu khách hoàn trả phụ kiện Charm nguyên seal về quầy giao dịch."
            }
        ]
    },
    {
        "module": "6. Gamification (Mốc mua sỉ 3 Cam)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Đạt mốc sỉ (Hit Tier): Đang có 2 Cam, bấm tăng lên 3 Cam",
                "pre": "Chính sách: Mua từ 3 Cam trở lên được tặng thêm 01 'Charm Phiên Bản Giới Hạn / Limited Edition 0đ' bên cạnh Quota Basic.",
                "rule": "Auto-unlock & Auto-inject: Hệ thống tự động mở khóa và chèn thêm 01 SKU Charm Limited (giá 0đ) vào giỏ hàng, đồng thời Quota Basic tăng lên 3.",
                "backend": "Milestone Engine: If Qty_Play4 >= 3 and not_has_limited_charm -> Insert Line Item Charm_Limited, unit_price = 0, is_gift = true, non_removable_badge.",
                "ui": "Hiệu ứng ăn mừng (Confetti animation) trên giỏ hàng: 'Chúc mừng bạn đã mở khóa quà tặng độc quyền: 01 Charm Limited Edition (0đ)'.",
                "exception": "Nếu kho hết Charm Limited: Tự động chuyển đổi thành quà tặng thay thế tương đương (Ví dụ: Voucher dịch vụ Cloud 100k hoặc Charm Premium)."
            },
            {
                "br": "BR-02",
                "scenario": "Rớt mốc sỉ (Drop Tier): Đang có 3 Cam + Quà Limited, giảm Cam xuống 2",
                "pre": "Giỏ đang có 3 Cam + Quà tặng Charm Limited 0đ. Khách bấm [-] giảm Cam xuống 2.",
                "rule": "Thu hồi tự động (Clawback Rule): Không còn thỏa điều kiện mốc sỉ 3 Cam, hệ thống cưỡng chế xóa SKU Charm Limited khỏi giỏ hàng (vì đây là phiên bản quà tặng độc quyền, không bán lẻ).",
                "backend": "If Qty_Play4 < 3 -> Delete item where SKU == Charm_Limited. Quota Basic giảm từ 3 xuống 2.",
                "ui": "Toast thông báo màu đỏ: 'Số lượng Camera dưới 3, quà tặng Charm Limited Edition đã được tự động gỡ khỏi giỏ hàng'.",
                "exception": "Khách tăng lại lên 3 Cam: Tự động add lại quà Limited vào giỏ hàng."
            },
            {
                "br": "BR-03",
                "scenario": "Hết hàng Charm Limited (OOS) ngay lúc khách đang thanh toán",
                "pre": "Khách có 3 Cam + Charm Limited trong giỏ và nhấn nút 'Đặt hàng / Thanh toán'.",
                "rule": "Kho báo hết hàng Charm Limited trong lúc lock kho: Hệ thống KHÔNG chặn đứng việc mua Camera của khách, mà hiển thị thông báo xin lỗi và đề xuất quà thay thế hoặc giao bổ sung sau.",
                "backend": "Inventory Allocation Service: Return error 'ITEM_OOS: Charm_Limited'. Cart xử lý fallback sang giải pháp: Đính kèm 'Phiếu bảo lưu nhận Charm Limited đợt 2' hoặc 'Đổi quà tương đương'.",
                "ui": "Modal thông báo trang trọng: 'Rất tiếc, quà tặng Charm Limited vừa hết hàng trước ít phút. Chúng tôi sẽ gửi bù quà tặng cho bạn sau 7 ngày làm việc hoặc bạn có thể chọn đổi sang quà B. [Đồng ý gửi bù & Tiếp tục]'.",
                "exception": "Nếu khách không đồng ý: Khách có thể hủy bỏ đơn hàng không phát sinh phí."
            },
            {
                "br": "BR-04",
                "scenario": "Chống đầu cơ / Chống gom hàng quà Limited (Anti-fraud / Cap per User)",
                "pre": "Đại lý hoặc khách hàng mua nhiều đơn hàng liên tục 3 Cam để tích trữ quà Limited.",
                "rule": "Giới hạn tối đa (Cap per User): Mỗi tài khoản / Số điện thoại / Địa chỉ giao hàng chỉ được nhận tối đa 02 Charm Limited trong suốt toàn bộ chiến dịch.",
                "backend": "Order Validation API kiểm tra lịch sử mua hàng: Query Total_Claimed_Limited where user_id == CurrentUser or phone == ShippingPhone. If count >= 2 -> Không cấp thêm quà Limited.",
                "ui": "Khi đạt trần giới hạn: Ẩn quà Limited hoặc hiển thị thông báo: 'Bạn đã đạt số lượng tối đa 2 quà Limited cho mỗi khách hàng'. Các Cam vẫn được hưởng ưu đãi Basic bình thường.",
                "exception": "Đơn hàng của khách hàng doanh nghiệp (B2B): Cần kênh phê duyệt ngoại lệ từ Giám đốc kinh doanh qua Backoffice."
            }
        ]
    },
    {
        "module": "7. Kế toán & Nền tảng (Database & Vouchers)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Cấu trúc dữ liệu ghi nhận đơn hàng (Database Schema & Accounting)",
                "pre": "Đơn hàng thanh toán thành công gồm Cam Play4 và Charm 0đ.",
                "rule": "Ghi nhận chuẩn kế toán và xuất hóa đơn điện tử: Line Item Charm ghi nhận: Original_Price = 150.000đ; Discount_Amount = 150.000đ; Final_Amount = 0đ; Tax_Rate = 0% (hoặc theo quy định khuyến mãi đăng ký Sở Công Thương).",
                "backend": "Bảng Order_Items lưu đầy đủ: base_price=150000, discount=150000, amount=0, promotion_ref='PROMO_CHARM_0D'. Không lưu cứng giá gốc = 0đ để tránh mất dấu giá trị tài sản kho.",
                "ui": "Hóa đơn VAT và email xác nhận đơn hàng hiển thị: Charm Play 4: 150.000đ - Khuyến mại: -150.000đ - Thành tiền: 0đ.",
                "exception": "Khi tích hợp hệ thống ERP (SAP/Oracle): Đồng bộ đúng mã tài khoản chi phí khuyến mại của phòng Marketing."
            },
            {
                "br": "BR-02",
                "scenario": "Xung đột với Voucher toàn sàn (Cart-level Voucher)",
                "pre": "Khách nhập Voucher toàn sàn 'GIAM10 - Giảm 10% tổng giá trị đơn hàng' hoặc 'GIAM100K cho đơn từ 1.000.000đ'.",
                "rule": "Sản phẩm quà tặng 0đ không được tham gia tính chiết khấu giảm thêm. Giá trị phụ thu 50k (nếu có) được tính vào tổng thanh toán để xét điều kiện giá trị đơn hàng tối thiểu (Min Order Value).",
                "backend": "Voucher Engine: Cart_Subtotal_For_Voucher = Sum(Item.Final_Amount where item.is_gift == false). Voucher giảm 10% chỉ áp dụng trên giá trị sau khuyến mãi của các mặt hàng tính tiền.",
                "ui": "Hiển thị chi tiết dòng chiết khấu: 'Voucher GIAM10: -80.000đ (Áp dụng cho Camera Play4 và phụ thu Charm)'. Không gây hiểu lầm là giảm trên giá gốc quà tặng.",
                "exception": "Nếu Voucher quy định 'Không áp dụng chung với các chương trình khuyến mãi khác': Hệ thống thông báo rõ ràng lý do từ chối mã voucher."
            }
        ]
    },
    {
        "module": "8. Quản trị Tồn kho & Cạnh tranh giỏ hàng (Inventory Concurrency & OOS)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Tồn kho tức thời: Đang chọn Charm trong giỏ thì SKU Charm đó hết hàng trước lúc Checkout",
                "pre": "Khách đang chọn Charm Mẫu A trong giỏ. Trong lúc khách chuẩn bị thanh toán, khách hàng khác đã mua hết tồn kho Mẫu A.",
                "rule": "Soft Reservation vs Hard Reservation: Trong giỏ hàng chỉ giữ chỗ tạm (Soft lock). Khi bấm 'Thanh toán', hệ thống kiểm tra tồn kho thực tế (Real-time stock check). Nếu hết hàng, chặn thanh toán dòng đó và nhắc khách đổi mẫu.",
                "backend": "API /checkout/validate kiểm tra Inventory Service. Nếu available_stock < requested_qty -> Trả về mã lỗi 'ERR_STOCK_OOS', kèm danh sách variant Charm còn hàng thay thế.",
                "ui": "Dòng Charm A trong giỏ bị làm mờ, gắn badge đỏ 'Vừa hết hàng'. Nổi bật nút 'Đổi mẫu khác'. Nút 'Đặt hàng' bị tạm disable cho đến khi khách chọn lại mẫu có sẵn.",
                "exception": "Nếu tất cả các mẫu Charm đều hết hàng: Cho phép khách checkout đơn Cam Play4 và gửi kèm mã Voucher bù quà tặng cho lần mua sau."
            },
            {
                "br": "BR-02",
                "scenario": "Tồn kho không đủ số lượng: Mua 3 Cam muốn 3 Charm A, nhưng Mẫu A chỉ còn 1 cái",
                "pre": "Kho còn 1 Charm A, 5 Charm B, 10 Charm C. Khách nhập số lượng Charm A = 3.",
                "rule": "Giới hạn số lượng chọn tối đa của mỗi mẫu không vượt quá số lượng tồn kho khả dụng hiện tại (Max_Selectable = MIN(Quota, Stock_Qty)).",
                "backend": "Cart Controller validate: Qty_Input <= Product_Variant.stock_on_hand. Nếu vượt quá, trả lỗi hoặc tự động ép về số tồn tối đa.",
                "ui": "Nút [+] của Mẫu A bị disable khi số lượng đạt 1. Hiển thị thông báo nhỏ màu xám: 'Mẫu A chỉ còn 1 sản phẩm. Vui lòng chọn thêm 2 mẫu khác để nhận đủ quà'.",
                "exception": "Khách cố tình sửa request API để gửi số lượng 3: Backend chặn ngay lập tức và trả mã lỗi 400 Bad Request."
            },
            {
                "br": "BR-03",
                "scenario": "Quá hạn phiên giỏ hàng (Cart Session Expiration / Ngâm giỏ hàng qua đêm)",
                "pre": "Khách bỏ Cam + Charm vào giỏ lúc 23h hôm trước. Đến 9h sáng hôm sau mới quay lại bấm thanh toán, lúc này CTKM đã kết thúc.",
                "rule": "Chính sách giá và khuyến mại được tính lại tại thời điểm Submit đơn hàng (Point of Sale). Nếu CTKM hết hạn hoặc hết ngân sách, giỏ hàng tự động cập nhật lại quyền lợi.",
                "backend": "Check Campaign_Status: If status != 'ACTIVE' -> Remove promo discounts, update items to current active prices.",
                "ui": "Hiển thị thông báo Toast cảnh báo: 'Chương trình quà tặng Charm 0đ đã kết thúc lúc 00:00. Giỏ hàng của bạn đã được cập nhật lại theo giá hiện hành'.",
                "exception": "Khách hàng khiếu nại: Hệ thống CSKH tra cứu lịch sử log giỏ hàng để giải thích thỏa đáng cho khách."
            }
        ]
    },
    {
        "module": "9. Xung đột Khuyến mãi & Voucher đa tầng (Multi-tier Discount / Coupon Stacking)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Flash Sale trùng giờ: Camera Play4 đang tham gia Flash Sale giảm giá sốc",
                "pre": "Camera Play4 giảm giá từ 800k còn 599k trong khung giờ Flash Sale 12h-14h.",
                "rule": "Quy tắc Chồng khuyến mãi (Promo Stacking): Khai báo trên QLCS cho phép hoặc không cho phép kết hợp. Mặc định: Sản phẩm Flash Sale ĐƯỢC hưởng quà tặng Charm 0đ nếu chiến dịch cho phép, hoặc KHÔNG ĐƯỢC kèm quà nếu biên lợi nhuận không cho phép.",
                "backend": "Product Promotion Engine kiểm tra flag: 'is_flash_sale_combinable_with_charm'. Nếu False -> Vô hiệu hóa Quota Charm đối với các Cam mua trong khung giờ Flash Sale.",
                "ui": "Nếu không cho kết hợp: Tại trang Flash Sale hiển thị rõ nhãn 'Giá sốc không áp dụng kèm quà tặng Charm 0đ'.",
                "exception": "Nếu khách mua 1 Cam Flash Sale và 1 Cam giá thường: Chỉ Cam giá thường mới sinh Quota 1 Charm 0đ."
            },
            {
                "br": "BR-02",
                "scenario": "Thanh toán bằng Điểm thưởng FPT / Xu FPT Loyalty cho phụ thu Charm Premium",
                "pre": "Khách có 50.000 điểm FPT Loyalty trong tài khoản, muốn dùng để cấn trừ phụ thu 50k của Charm Premium.",
                "rule": "Cho phép sử dụng Điểm thưởng FPT để thanh toán các khoản phụ thu hoặc giá trị thanh toán thực tế của đơn hàng theo tỷ lệ quy đổi 1 điểm = 1 VNĐ.",
                "backend": "Payment Module: Total_Payable = Subtotal - Loyalty_Points_Redeemed. Gửi yêu cầu trừ điểm sang hệ thống FPT Loyalty Core qua API.",
                "ui": "Mục thanh toán hiển thị checkbox: '[x] Dùng 50.000 điểm FPT để thanh toán phụ thu (Số tiền cần trả: 0đ)'.",
                "exception": "Nếu giao dịch đặt hàng thất bại sau khi đã trừ điểm: Hệ thống tự động hoàn trả điểm thưởng (Rollback Points) trong vòng 5 phút."
            }
        ]
    },
    {
        "module": "10. Vận chuyển, Giao nhận & Đa kho (Shipping & Multi-location Fulfillment)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Lệch kho xuất hàng (Cross-docking / Multi-warehouse Split)",
                "pre": "Kho gần khách hàng nhất (Kho Hà Nội) có sẵn Camera Play4 nhưng hết phụ kiện Charm. Charm đang ở Kho Đà Nẵng hoặc Kho Tổng HCM.",
                "rule": "Quy tắc Điều phối Vận chuyển: Hệ thống OMS tối ưu hóa: Điều chuyển Charm về Kho Hà Nội để gom thành 1 kiện giao chung; HOẶC Tách thành 2 kiện hàng giao riêng (Split Delivery) mà KHÔNG thu thêm phí ship của khách hàng đối với kiện quà tặng.",
                "backend": "Order Routing Service: Tạo 2 Package ID: Package 1 (Play4 - Giao từ HN, tính phí ship chuẩn); Package 2 (Charm - Giao từ HCM, Shipping_Fee = 0đ do FPT chịu chi phí quà tặng).",
                "ui": "Màn hình Checkout hiển thị rõ ràng: 'Đơn hàng của bạn sẽ được chia thành 2 kiện do phụ kiện được điều chuyển từ kho đặc biệt. Miễn phí vận chuyển cho phụ kiện quà tặng'.",
                "exception": "Khách muốn nhận tất cả trong 1 lần: Cung cấp tùy chọn '[x] Giao chung khi đủ hàng (thời gian nhận có thể trễ hơn 1-2 ngày)'."
            },
            {
                "br": "BR-02",
                "scenario": "Nhận hàng tại quầy FPT Shop (BOPIS - Buy Online Pick-up In Store)",
                "pre": "Khách đặt mua online và chọn nhận hàng tại Shop FPT gần nhà.",
                "rule": "Kiểm tra tồn kho tức thời tại Shop đã chọn: Nếu Shop có Cam nhưng không có Charm, hệ thống tự động thông báo thời gian điều chuyển phụ kiện về Shop trước khi khách ra lấy.",
                "backend": "Check Store_Inventory(Store_ID, Play4_SKU, Charm_SKU). Nếu thiếu Charm, sinh phiếu chuyển kho nội bộ Store-Transfer.",
                "ui": "Hiển thị: 'Cửa hàng có sẵn Camera Play4. Phụ kiện Charm dự kiến có mặt tại cửa hàng sau 24h. Chúng tôi sẽ nhắn tin SMS khi toàn bộ đơn hàng sẵn sàng'.",
                "exception": "Khách cần gấp: Cho phép khách lấy Cam trước, Charm nhận sau hoặc gửi bưu điện về nhà miễn phí."
            }
        ]
    },
    {
        "module": "11. Cổng thanh toán & Trạng thái đơn (Payment Drop-off & Timeout)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Thanh toán Online thất bại hoặc Quá hạn chờ (Payment Pending Timeout)",
                "pre": "Khách chọn thanh toán qua VNPAY/MoMo, hệ thống tạo đơn hàng trạng thái 'Chờ thanh toán (Pending Payment)' với hạn chờ 15 phút.",
                "rule": "Trong 15 phút chờ: Kho và Quota Charm được tạm giữ (Holding). Nếu sau 15 phút khách không thanh toán hoặc bấm 'Hủy giao dịch', đơn hàng tự động chuyển sang 'Đã hủy (Cancelled)' và giải phóng tồn kho Charm ngay lập tức.",
                "backend": "Schedule Job / Cron Worker quét các đơn Pending quá 15 phút: Gọi InventoryService.releaseHold(Order_ID), cập nhật Order_Status = 'CANCELLED_TIMEOUT'.",
                "ui": "Khi hết hạn, nếu khách còn ở màn hình chờ: Hiển thị thông báo 'Giao dịch đã hết hạn chờ thanh toán. Giỏ hàng của bạn đã được hoàn lại. [Thanh toán lại]'.",
                "exception": "Trường hợp tiền đã trừ ở ngân hàng nhưng webhook VNPAY về trễ sau 15 phút: Hệ thống tự động kích hoạt luồng Reconciliation (Đối soát) để khôi phục đơn hàng hoặc tự động hoàn tiền tự động (Auto-refund) cho khách."
            },
            {
                "br": "BR-02",
                "scenario": "Khách hủy đơn hàng COD trước khi xuất kho",
                "pre": "Đơn hàng COD đang ở trạng thái 'Chờ xác nhận' hoặc 'Đang chuẩn bị hàng'. Khách bấm nút 'Hủy đơn hàng' trên App/Web.",
                "rule": "Cho phép khách hủy đơn ngay lập tức nếu chưa xuất kho. Toàn bộ hạn mức mua hàng và tồn kho phụ kiện Charm được hoàn trả vào kho khả dụng.",
                "backend": "API /order/cancel: Cập nhật trạng thái đơn = CANCELLED. Bắn event sang WMS hủy phiếu nhặt hàng và giải phóng tồn kho.",
                "ui": "Hiển thị lý do hủy đơn cho khách chọn (Đổi ý, chọn nhầm mẫu Charm, muốn mua thêm). Xác nhận hủy thành công ngay tức khắc.",
                "exception": "Đơn hàng đã bàn giao cho đơn vị vận chuyển: Không cho hủy trên web, hướng dẫn khách từ chối nhận hàng khi Shipper gọi."
            }
        ]
    },
    {
        "module": "12. Đổi trả từng phần & Bảo hành (RMA, Partial Return & Warranty)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Bảo hành 1 đổi 1 Camera Play4 do lỗi phần cứng kỹ thuật",
                "pre": "Khách sử dụng Camera trong 30 ngày bị lỗi phần cứng nhà sản xuất, đem đi bảo hành đổi mới.",
                "rule": "Bảo hành độc lập thiết bị chính: Kỹ thuật viên / Shop đổi mới 01 Camera Play4 tương đương cho khách. Khách KHÔNG cần phải nộp lại phụ kiện Charm đã tặng.",
                "backend": "Hệ thống Quản lý Bảo hành (Warranty Core): Tạo phiếu RMA đổi mã IMEI Camera mới, giữ nguyên thông tin sở hữu của Charm, không phát sinh chi phí.",
                "ui": "Biên nhận bảo hành ghi rõ: 'Đổi mới Camera Play4 - Không thu hồi phụ kiện khuyến mãi Charm'.",
                "exception": "Nếu phụ kiện Charm bị lỗi sản xuất: Áp dụng chính sách bảo hành phụ kiện riêng (Ví dụ: 1 đổi 1 trong 7 ngày nếu lỗi khớp gắn)."
            },
            {
                "br": "BR-02",
                "scenario": "Khách hàng trả hàng hoàn tiền (Return & Full/Partial Refund)",
                "pre": "Đơn hàng gồm 1 Cam Play4 (800k) + 1 Charm 0đ (Trị giá 150k). Sau 3 ngày khách yêu cầu trả Cam đòi tiền.",
                "rule": "Chính sách Thu hồi Quà tặng: Khi trả sản phẩm chính, khách phải hoàn trả kèm phụ kiện quà tặng Charm còn nguyên vẹn/chưa sử dụng. Nếu Charm đã bị mất hoặc hư hại, khấu trừ giá trị niêm yết của Charm (150.000đ) vào số tiền hoàn lại của Camera.",
                "backend": "Refund Calculator: If Gift_Returned == True: Refund = 800.000đ. If Gift_Returned == False: Refund = 800.000đ - 150.000đ = 650.000đ.",
                "ui": "Portal CSKH/App hiển thị điều khoản: 'Vui lòng hoàn trả Camera cùng đầy đủ hộp và quà tặng Charm đi kèm để nhận đủ 100% tiền hoàn'.",
                "exception": "Charm Premium phụ thu 50k: Nếu trả cả Cam và Charm Premium, hoàn đủ 850k. Nếu chỉ trả Cam giữ Charm, hoàn 800k - (200k - 50k) = 650k."
            }
        ]
    },
    {
        "module": "13. Đồng bộ Đa thiết bị & Tài khoản Ẩn danh (Guest vs Logged-in Cart Sync)",
        "cases": [
            {
                "br": "BR-01",
                "scenario": "Gộp giỏ hàng ẩn danh khi đăng nhập (Guest Cart Merging)",
                "pre": "Khách chưa đăng nhập (Guest) chọn 1 Cam + 1 Charm A (0đ). Sau đó bấm 'Đăng nhập'. Tài khoản của khách trước đó đã có sẵn 1 Cam Play4 trong giỏ.",
                "rule": "Quy tắc Hợp nhất giỏ hàng (Cart Merging Logic): Tổng số Cam sau khi đăng nhập = 1 (Guest) + 1 (Account) = 2 Cam. Quota Charm 0đ tự động nâng lên 2. Giữ lại Charm A đã chọn và cấp thêm 1 slot chọn Charm 0đ thứ 2.",
                "backend": "Cart Merge Service: OnUserLogin -> Aggregate items by SKU. Update Total_Play4 = 2 -> New_Quota = 2. Retain existing Charm A (Qty = 1) -> Remaining_Quota = 1.",
                "ui": "Toast thông báo sau đăng nhập: 'Giỏ hàng của bạn đã được đồng bộ. Hiện bạn có 2 Camera Play4 và 2 suất nhận Charm 0đ! [Chọn thêm quà]'.",
                "exception": "Xung đột nếu giỏ trên tài khoản đã có Charm B: Hệ thống gộp cả Charm A và Charm B thành 2 Charm 0đ hoàn hảo (1A + 1B = 2/2 Quota)."
            },
            {
                "br": "BR-02",
                "scenario": "Đăng xuất tài khoản khi đang có giỏ hàng khuyến mãi",
                "pre": "Khách đang đăng nhập có giỏ hàng Cam + Charm 0đ, sau đó nhấn 'Đăng xuất'.",
                "rule": "Bảo mật dữ liệu giỏ hàng: Giỏ hàng của tài khoản được lưu an toàn trên Cloud Database. Giỏ hàng ẩn danh hiện tại trên trình duyệt được làm sạch (Clear guest cart) để tránh lộ thông tin đơn hàng cho người dùng sau trên cùng máy tính.",
                "backend": "Session Destroy Event: Disassociate cart_id from browser session cookies, generate fresh empty anonymous cart.",
                "ui": "Badge giỏ hàng về số 0. Khi đăng nhập lại, giỏ hàng cũ tự động phục hồi nguyên vẹn.",
                "exception": "Khách tiếp tục mua với tư cách khách vãng lai: Tạo giỏ hàng mới độc lập hoàn toàn."
            }
        ]
    }
]

# Tạo file Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Kich_Ban_Ky_Thuat_Play4_Charm"

# Bật lưới hiển thị
ws.views.sheetView[0].showGridLines = True

# Định nghĩa Styles
font_title = Font(name="Times New Roman", size=16, bold=True, color="1F497D")
font_subtitle = Font(name="Times New Roman", size=12, italic=True, color="595959")
font_header = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
font_row = Font(name="Times New Roman", size=11, bold=False, color="000000")
font_br = Font(name="Times New Roman", size=11, bold=True, color="002060")
font_module = Font(name="Times New Roman", size=12, bold=True, color="FFFFFF")

fill_header = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
fill_module = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
fill_alt = PatternFill(start_color="F2F5F9", end_color="F2F5F9", fill_type="solid")
fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

thin_border_side = Side(style='thin', color='D9D9D9')
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
thick_bottom_side = Side(style='medium', color='1F497D')
header_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thick_bottom_side)

headers = [
    "STT",
    "Mã Rule",
    "Nhóm Kịch Bản",
    "Kịch Bản Thao Tác (Cart User Action)",
    "Điều Kiện Tiên Quyết (Pre-conditions)",
    "Quy Tắc Nghiệp Vụ (Business Logic & Pricing)",
    "Xử Lý Dữ Liệu Backend & Cart State",
    "Hành Vi UI/UX & Thông Báo",
    "Xử Lý Ngoại Lệ & Vận Hành (Exceptions & RMA)"
]

# Ghi Title
ws.merge_cells("A1:I1")
ws["A1"] = "BẢNG ĐẶC TẢ KỊCH BẢN GIỎ HÀNG BÀN GIAO KỸ THUẬT (TECH SPEC)"
ws["A1"].font = font_title
ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

ws.merge_cells("A2:I2")
ws["A2"] = "Dự án: FPT Camera Play4 & Phụ kiện Charm Promo Engine | Chuẩn hóa theo vai trò Senior BA & Product Owner"
ws["A2"].font = font_subtitle
ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

ws.row_dimensions[1].height = 30
ws.row_dimensions[2].height = 20
ws.row_dimensions[4].height = 32

# Ghi Headers
for col_idx, h in enumerate(headers, 1):
    cell = ws.cell(row=4, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = header_border

current_row = 5
stt_counter = 1

tsv_rows = []
tsv_headers = headers
tsv_rows.append(tsv_headers)

csv_rows = []
csv_rows.append(tsv_headers)

for mod_idx, mod in enumerate(modules, 1):
    # Ghi dòng phân cách Module
    ws.merge_cells(start_row=current_row, start_column=1, end_row=current_row, end_column=9)
    mod_cell = ws.cell(row=current_row, column=1, value=f"PHẦN {mod_idx}: {mod['module'].upper()}")
    mod_cell.font = font_module
    mod_cell.fill = fill_module
    mod_cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[current_row].height = 26
    current_row += 1
    
    for case in mod["cases"]:
        row_fill = fill_alt if stt_counter % 2 == 0 else fill_white
        
        row_data = [
            stt_counter,
            case["br"],
            mod["module"],
            case["scenario"],
            case["pre"],
            case["rule"],
            case["backend"],
            case["ui"],
            case["exception"]
        ]
        
        tsv_rows.append([str(x) for x in row_data])
        csv_rows.append(row_data)
        
        for c_idx, val in enumerate(row_data, 1):
            c = ws.cell(row=current_row, column=c_idx, value=val)
            c.font = font_br if c_idx == 2 else font_row
            c.fill = row_fill
            c.border = thin_border
            
            if c_idx in [1, 2]:
                c.alignment = Alignment(horizontal="center", vertical="top")
            else:
                c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
                
        ws.row_dimensions[current_row].height = 85
        current_row += 1
        stt_counter += 1

# Thiết lập độ rộng cột tối ưu
col_widths = {
    "A": 7,    # STT
    "B": 11,   # Mã Rule
    "C": 22,   # Nhóm Kịch Bản
    "D": 32,   # Kịch Bản Thao Tác
    "E": 28,   # Điều Kiện
    "F": 42,   # Quy Tắc Nghiệp Vụ
    "G": 40,   # Backend & State
    "H": 38,   # UI/UX & Thông Báo
    "I": 35    # Ngoại Lệ & Vận Hành
}

for col_letter, width in col_widths.items():
    ws.column_dimensions[col_letter].width = width

# Xuất ra file Excel
xlsx_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.xlsx"
wb.save(xlsx_path)
print(f"Exported Excel to {xlsx_path}")

# Xuất ra file TSV (Tab Separated Values để paste trực tiếp vào Google Sheets cực mượt)
tsv_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.tsv"
with open(tsv_path, "w", encoding="utf-8") as f:
    for r in tsv_rows:
        # Làm sạch newline bên trong cell để không bị gãy dòng khi paste vào Google Sheets
        cleaned = [str(cell).replace("\t", " ").replace("\r\n", "\n").replace("\n", " ") for cell in r]
        f.write("\t".join(cleaned) + "\n")
print(f"Exported TSV to {tsv_path}")

# Xuất ra file CSV
csv_path = "/Users/hathuy/Documents/FPT-1/thuyttdoc/Kich_Ban_Ky_Thuat_Play4_Charm.csv"
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for r in csv_rows:
        writer.writerow(r)
print(f"Exported CSV to {csv_path}")

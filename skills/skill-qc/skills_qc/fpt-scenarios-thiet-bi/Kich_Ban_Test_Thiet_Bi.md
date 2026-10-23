# KỊCH BẢN KIỂM THỬ & QUY TẮC NGHIỆP VỤ - PHÂN HỆ THIẾT BỊ

# C. QUY TẮC NGHIỆP VỤ VÀ KIỂM THỬ (BUSINESS RULES & TEST CASES)


## 1. Bảng Quy tắc Nghiệp vụ (Business Rules)


| Mã Rule | Tên Quy tắc | Mô tả chi tiết và Xử lý Hệ thống |
| :--- | :--- | :--- |
| BR-01 | Kiểm tra Điều kiện Bắt buộc | Các trường: Tên người nhận, SĐT liên hệ, Địa chỉ chi tiết (nhà/đường, phường, quận, tỉnh) là dữ liệu bắt buộc nhập. |
| BR-02 | Kiểm tra Tồn kho (Inventory Check) | Khi khách hàng thay đổi số lượng hoặc ấn Mua ngay, hệ thống phải call API OMS/Kho để check số lượng thực tế. Nếu số lượng trong kho < số lượng yêu cầu, chặn mua và thông báo: "Sản phẩm tạm hết hàng hoặc không đủ số lượng." |
| BR-03 | Đồng bộ chính sách Khách hàng hiện hữu | Nếu SĐT nhập vào đang là Khách hàng FPT (tra cứu qua API Contract), hệ thống tự động tính toán và apply Voucher/Mã giảm giá nội bộ (ví dụ: Miễn phí lắp đặt camera cho KH Internet). |



## 2. Bảng Tình huống Kiểm thử (Test Cases / Edge Cases)


| Mã TC | Kịch bản Ngoại lệ | Điều kiện kích hoạt (Condition) | Kết quả mong đợi (Expected Output) |
| :--- | :--- | :--- | :--- |
| TC-EX-01 | Giỏ hàng quá giới hạn | Khách hàng chọn số lượng mua > giới hạn tối đa cho phép trong 1 đơn (VD: > 10 thiết bị). | Báo lỗi: "Bạn chỉ được phép mua tối đa 10 sản phẩm cho mỗi đơn hàng." Auto set số lượng về 10. |
| TC-EX-02 | SĐT không hợp lệ | Nhập chữ cái hoặc ký tự đặc biệt vào trường SĐT. | Khóa bàn phím không cho nhập ký tự chữ, hoặc báo lỗi ngay lập tức dưới field. |


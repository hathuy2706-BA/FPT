# KỊCH BẢN KIỂM THỬ & QUY TẮC NGHIỆP VỤ - DỊCH VỤ SỐ STANDALONE (FPT PLAY)

# C. QUY TẮC NGHIỆP VỤ VÀ KIỂM THỬ (BUSINESS RULES & TEST CASES)


## 1. Bảng Quy tắc Nghiệp vụ (Business Rules)


| Mã Rule | Tên Quy tắc | Mô tả chi tiết và Xử lý Hệ thống |
| :--- | :--- | :--- |
| BR-01 | Không tra cứu hợp đồng CRM (No explicit CRM check) | Khách hàng không cần phải tra cứu thủ công qua màn hình. Hệ thống xử lý logic ngầm thông qua SĐT để phân luồng. |
| BR-02 | Check trùng gói FPT Play / Nâng cấp gói | (Test case: SĐT 0939536236)Hệ thống kiểm tra trực tiếp trạng thái SĐT trên hệ thống FPT Play.- Nếu SĐT đang sử dụng FPT Play (bất kể gói VVIP1/VVIP2 hay gói khác), hệ thống lập tức báo trùng lặp và không cho phép đăng ký mới đè lên tài khoản hiện hữu. |



## 2. Bảng Tình huống Kiểm thử (Test Cases / Edge Cases)


| Mã TC | Kịch bản Ngoại lệ | Điều kiện kích hoạt (Condition) | Kết quả mong đợi (Expected Output) |
| :--- | :--- | :--- | :--- |
| TC-EX-01 | Lỗi validate SĐT ngầm | Hệ thống kiểm tra ngầm phát hiện SĐT không đủ điều kiện đăng ký dịch vụ SA (tùy theo rule nội bộ). | Thông báo lỗi tinh tế: "Số điện thoại hiện chưa đủ điều kiện đăng ký dịch vụ này." Không chặn cứng luồng trải nghiệm. |


# KỊCH BẢN KIỂM THỬ NGOẠI LỆ - PHÂN HỆ INTERNET & TRUYỀN HÌNH COMBO

# C. KỊCH BẢN KIỂM THỬ NGOẠI LỆ (EDGE CASES)


| Mã TC | Kịch bản Ngoại lệ | Kết quả mong đợi (Expected Output) |
| :--- | :--- | :--- |
| TC-EX-01 | Khách hàng chọn địa chỉ Hết Port / Không có hạ tầng mạng (API Check Port trả về false) | Hệ thống bỏ qua block chọn gói DV và PTTT. Redirect thẳng đến Page Hoàn thành — kết thúc quy trình. Thông tin KH được đẩy vào tệp KHTN để nhân viên Sale tiếp nhận và tư vấn. |
| TC-EX-02 | Hủy giao dịch thanh toán trực tuyến (Drop off) | Khách hàng chuyển hướng sang cổng thanh toán (VNPay, Foxpay) nhưng bấm nút "Hủy". Hệ thống ghi nhận trạng thái KHTN là "Chờ thanh toán" để thực hiện gửi SMS nhắc nhở. |


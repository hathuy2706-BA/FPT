# Sơ đồ Sequence Diagram: Luồng Áp Dụng Voucher FPT.vn (Phase 1)

Dưới đây là sơ đồ trình tự tương tác giữa Khách hàng, Frontend FPT.vn, Backend Checkout và Product Hub / QLCS trong quá trình áp dụng voucher và thanh toán.

![Sơ đồ Sequence Diagram](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default' } }%%
sequenceDiagram
    autonumber
    actor Customer as Khách hàng
    participant FE as Frontend FPT.vn
    participant BE as Backend Checkout
    participant Hub as Product Hub & QLCS

    Note over Customer, Hub: Khởi động checkout & Lấy cấu hình cước / voucher
    Customer->>+FE: 1. Chọn sản phẩm (NET/Combo/Camera) và điền địa chỉ
    FE->>+BE: 2. Gửi request thông tin giỏ hàng & PTTT
    BE->>+Hub: 3. Lấy cấu hình gói cước, phí lắp đặt & danh sách Voucher
    Hub-->>-BE: 4. Trả về thông tin cấu hình (text nhỏ, phí) & list Voucher
    
    Note over BE: Sắp xếp voucher Active lên trên,<br/>Random voucher cùng cấp Active,<br/>Gắn tag "Sắp hết hạn" nếu HSD <= 3 ngày
    
    BE-->>-FE: 5. Trả về thông tin thanh toán chi tiết & danh sách Voucher đã xử lý
    FE-->>-Customer: 6. Hiển thị thông tin checkout & Nút "Chọn ưu đãi"

    Note over Customer, Hub: Khách hàng áp dụng ưu đãi
    Customer->>+FE: 7. Bấm "Chọn ưu đãi" và Chọn Voucher (hoặc Nhập mã thủ công)
    FE->>+BE: 8. Gửi yêu cầu áp dụng mã Voucher (Mã voucher, PTTT, SKU đơn hàng)
    
    Note over BE: Validate Voucher:<br/>- Kiểm tra PTTT tương thích (COD/Online)<br/>- Kiểm tra SKU tương thích (Voucher SKU)<br/>- Kiểm tra cơ cấu loại trừ (Exclusion)<br/>- Tính toán tiền giảm giá (Áp dụng Cap tối đa từ QLCS)
    
    alt Áp dụng thành công
        BE-->>FE: 9a. Trả về thông tin cước đã giảm giá & thông báo thành công (TH1a/TH2a)
        FE-->>Customer: 10a. Hiển thị số tiền cần thanh toán mới & Dòng chi tiết giảm giá
    else Thất bại / Bị khóa
        BE-->>FE: 9b. Trả về trạng thái lỗi (TH1b/TH2b)
        FE-->>Customer: 10b. Hiển thị thông điệp báo lỗi hoặc Voucher disabled kèm lý do (COD...)
    end
    deactivate BE
    deactivate FE

    Note over Customer, Hub: Khách hàng thanh toán & Thay đổi bối cảnh (nếu có)
    opt Khách hàng thay đổi PTTT hoặc Số lượng thiết bị (Context Change)
        Customer->>+FE: 11. Thay đổi thông tin PTTT (Ví dụ: từ VietQR sang COD)
        FE->>+BE: 12. Gửi request cập nhật giỏ hàng
        Note over BE: Validate lại điều kiện Voucher đang chọn
        alt Voucher không đạt điều kiện mới
            BE-->>FE: 13a. Trả về thông tin cước gốc & Thông báo lỗi TH3a (Voucher bị loại bỏ)
            FE-->>Customer: 14a. Thu hồi voucher về 0, hiển thị thông báo lỗi context
        else Voucher vẫn đạt điều kiện
            BE-->>FE: 13b. Trả về thông tin cước đã chiết khấu tương ứng
            FE-->>Customer: 14b. Cập nhật giao diện thanh toán bình thường
        end
        deactivate BE
        deactivate FE
    end

    Customer->>+FE: 15. Nhấn nút "Thanh toán"
    FE->>+BE: 16. Yêu cầu tạo đơn hàng và thanh toán
    BE->>+Hub: 17. Đánh dấu sử dụng Voucher & Tạo đơn hàng sang hệ thống SPF
    Hub-->>-BE: 18. Xác nhận tạo đơn hàng thành công
    BE-->>-FE: 19. Trả về thông tin hoàn tất đơn hàng
    FE-->>-Customer: 20. Hiển thị màn hình "Hoàn tất đơn hàng" (Mã đơn hàng, HĐĐT)
```

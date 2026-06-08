# Sơ đồ Flow Diagram: Luồng Nghiệp Vụ Áp Dụng Voucher FPT.vn (Phase 1)

Dưới đây là sơ đồ luồng hoạt động rẽ nhánh kiểm tra điều kiện áp dụng Voucher trên hệ thống FPT.vn.

![Sơ đồ Flow Diagram](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default' } }%%
flowchart TD
    Start([Khách hàng tại trang Checkout]) --> SelectVoucher{Chọn / Nhập mã Voucher}
    
    SelectVoucher -->|Chọn mã| CheckConditions[Backend Checkout kiểm tra điều kiện]
    
    CheckConditions --> CheckSKU{Đúng SKU / Gói cước?}
    CheckSKU -->|Không| DisableSKU[Khóa Voucher - Trạng thái Disabled<br/>Hiển thị lỗi: Lý do gói cước/thiết bị không đủ điều kiện] --> EndSelect([Quay lại danh sách ưu đãi])
    CheckSKU -->|Có| CheckPTTT{Đúng PTTT?}
    
    CheckPTTT -->|Không| DisablePTTT[Khóa Voucher - Trạng thái Disabled<br/>Hiển thị lỗi: Chỉ áp dụng cho PTTT...] --> EndSelect
    CheckPTTT -->|Có| CheckExclusion{Có bị loại trừ với<br/>mã đang chọn khác?}
    
    CheckExclusion -->|Có| DisableExcl[Khóa Voucher - Trạng thái Disabled<br/>Hiển thị lỗi: Không áp dụng đồng thời...] --> EndSelect
    CheckExclusion -->|Không| ApplySuccess[Áp dụng voucher thành công<br/>Tính tiền giảm cước & áp dụng Cap giảm tối đa]
    
    ApplySuccess --> UpdateCheckout[Cập nhật cước mới trên giao diện UI<br/>Hiển thị: Áp dụng mã ưu đãi thành công]
    
    UpdateCheckout --> CheckoutActive{Khách hàng thay đổi<br/>bối cảnh đơn hàng?}
    
    CheckoutActive -->|Đổi PTTT / đổi SKU / đổi chu kỳ cước| ReValidate[Backend tự động kiểm tra lại điều kiện]
    ReValidate --> ReCheckOK{Vẫn đủ điều kiện?}
    ReCheckOK -->|Không| RevokeVoucher[Thu hồi voucher, đưa số tiền giảm về 0<br/>Hiển thị lỗi: Ưu đãi đã chọn không đủ điều kiện áp dụng...] --> SelectVoucher
    ReCheckOK -->|Có| KeepVoucher[Giữ nguyên ưu đãi<br/>Tính lại cước theo bối cảnh mới] --> PayOrder
    
    CheckoutActive -->|Không thay đổi| PayOrder([Khách hàng bấm Thanh toán])
    
    PayOrder --> MarkUsed[Backend lưu đơn hàng và đánh dấu sử dụng Voucher]
    MarkUsed --> SuccessPage([Hiển thị màn hình Hoàn tất đơn hàng])
```

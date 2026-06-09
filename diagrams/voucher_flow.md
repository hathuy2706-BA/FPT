# Sơ đồ Flow Diagram: Luồng Nghiệp Vụ Áp Dụng Voucher FPT.vn (Phase 1)

Dưới đây là sơ đồ luồng hoạt động (Flow Diagram) thể hiện các bước rẽ nhánh và kiểm tra điều kiện áp dụng Voucher trên hệ thống FPT.vn.

![Sơ đồ Flow Diagram](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default', 'flowchart': { 'curve': 'stepAfter' } }%%
flowchart TD
    %% Định nghĩa các lớp style màu sắc chuẩn sơ đồ dự án
    classDef startClass fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff;
    classDef endClass fill:#F44336,stroke:#D32F2F,stroke-width:2px,color:#fff;
    classDef stepClass fill:#fff,stroke:#333,stroke-width:1.5px;
    classDef decisionClass fill:#fff,stroke:#333,stroke-width:1.5px;

    %% KHAI BÁO CÁC NODE THEO TIÊU CHUẨN HÌNH DẠNG VÀ PHÂN VAI TRÒ
    Node_Start((Start))
    Node_GetConfig[BE: Lấy cấu hình cước & voucher từ Product Hub]
    Node_ShowCheckout[FE: Hiển thị trang Checkout & nút Chọn ưu đãi]
    Node_SelectVoucher[KH: Chọn / Nhập mã Voucher]
    Node_ShowVouchers[FE: Hiển thị Popup Chọn ưu đãi]
    Node_Validate[BE: Kiểm tra điều kiện áp dụng]
    
    Node_CheckSKU{BE: Đơn hàng<br/>đúng SKU?}
    Node_CheckPTTT{BE: Đơn hàng<br/>đúng PTTT?}
    Node_CheckExcl{Voucher<br/>bị loại trừ?}
    
    Node_ShowError[FE: Hiển thị lỗi điều kiện voucher<br/>Lý do: COD / SKU / Loại trừ]
    Node_UpdateUI[FE: Cập nhật cước mới & Show thành công]
    
    Node_ChangeContext[KH: Thay đổi bối cảnh đơn hàng<br/>PTTT / SKU / Gói cước]
    Node_ReValidate[BE: Tự động kiểm tra lại điều kiện]
    Node_CheckReOK{BE: Vẫn đủ<br/>điều kiện?}
    Node_ShowContextError[FE: Hiển thị lỗi bối cảnh mới<br/>& thu hồi voucher về cước gốc]
    
    Node_Pay[KH: Nhấn nút Thanh toán]
    Node_MarkUsed[BE: Tạo đơn hàng SPF & Đánh dấu đã dùng mã]
    Node_SuccessPage((Kết thúc))

    %% Áp dụng style class cho các hình dạng node
    class Node_Start startClass;
    class Node_SuccessPage endClass;
    class Node_SelectVoucher,Node_ChangeContext,Node_Pay,Node_ShowCheckout,Node_ShowVouchers,Node_UpdateUI,Node_ShowError,Node_ShowContextError,Node_GetConfig,Node_Validate,Node_ReValidate,Node_MarkUsed stepClass;
    class Node_CheckSKU,Node_CheckPTTT,Node_CheckExcl,Node_CheckReOK decisionClass;

    %% LUỒNG LIÊN KẾT TUYẾN TÍNH THẲNG ĐỨNG VÀ GÓC VUÔNG CHUẨN
    Node_Start --> Node_GetConfig
    Node_GetConfig --> Node_ShowCheckout
    Node_ShowCheckout --> Node_SelectVoucher
    Node_SelectVoucher --> Node_ShowVouchers
    Node_ShowVouchers --> Node_Validate
    
    Node_Validate --> Node_CheckSKU
    
    %% Rẽ nhánh vuông góc kiểm tra điều kiện
    Node_CheckSKU -->|Không| Node_ShowError
    Node_CheckSKU -->|Có| Node_CheckPTTT
    
    Node_CheckPTTT -->|Không| Node_ShowError
    Node_CheckPTTT -->|Có| Node_CheckExcl
    
    Node_CheckExcl -->|Không| Node_UpdateUI
    Node_CheckExcl -->|Có| Node_ShowError
    
    %% Quay lại danh sách ưu đãi để chọn lại khi có lỗi
    Node_ShowError --> Node_SelectVoucher
    
    %% Tiếp tục thanh toán
    Node_UpdateUI --> Node_Pay
    Node_Pay --> Node_MarkUsed
    Node_MarkUsed --> Node_SuccessPage

    %% Luồng rẽ nhánh đổi bối cảnh (Context change)
    Node_UpdateUI --> Node_ChangeContext
    Node_ChangeContext --> Node_ReValidate
    Node_ReValidate --> Node_CheckReOK
    
    Node_CheckReOK -->|Không| Node_ShowContextError
    Node_CheckReOK -->|Có| Node_UpdateUI
    
    Node_ShowContextError --> Node_SelectVoucher
```

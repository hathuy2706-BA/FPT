# Sơ đồ Flow Diagram: Luồng Nghiệp Vụ Áp Dụng Voucher FPT.vn (Phase 1)

Dưới đây là sơ đồ luồng hoạt động phân làn (Swimlane Flowchart) thể hiện các bước rẽ nhánh và kiểm tra điều kiện áp dụng Voucher trên hệ thống FPT.vn.

![Sơ đồ Flow Diagram](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default', 'flowchart': { 'curve': 'stepAfter' } }%%
flowchart TD
    %% Định nghĩa các lớp style
    classDef startClass fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff;
    classDef endClass fill:#F44336,stroke:#D32F2F,stroke-width:2px,color:#fff;
    classDef stepClass fill:#fff,stroke:#333,stroke-width:1.5px;
    classDef decisionClass fill:#fff,stroke:#333,stroke-width:1.5px;

    subgraph L_KH[KHÁCH HÀNG]
        Node_Start((Start))
        Node_SelectVoucher[Chọn / Nhập mã Voucher]
        Node_ChangeContext[Thay đổi bối cảnh đơn hàng<br/>PTTT / SKU / Gói cước]
        Node_Pay[Nhấn nút Thanh toán]
    end

    subgraph L_FE[FRONTEND FPT.VN]
        Node_ShowCheckout[Hiển thị trang Checkout<br/>và nút Chọn ưu đãi]
        Node_ShowVouchers[Hiển thị Popup Chọn ưu đãi<br/>danh sách Voucher Active/Disabled]
        Node_UpdateUI[Cập nhật cước mới<br/>Hiển thị message thành công]
        Node_ShowError[Hiển thị lỗi điều kiện voucher<br/>Lý do: COD / SKU / Loại trừ]
        Node_ShowContextError[Hiển thị lỗi bối cảnh mới<br/>và thu hồi voucher về cước gốc]
        Node_SuccessPage((Kết thúc))
    end

    subgraph L_BE[BACKEND CHECKOUT & HỆ THỐNG]
        Node_GetConfig[Lấy cấu hình cước & voucher từ Product Hub]
        Node_Validate[Backend kiểm tra điều kiện áp dụng]
        Node_CheckSKU{Đơn hàng<br/>đúng SKU?}
        Node_CheckPTTT{Đơn hàng<br/>đúng PTTT?}
        Node_CheckExcl{Voucher<br/>bị loại trừ?}
        Node_ReValidate[Backend re-validate bối cảnh mới]
        Node_CheckReOK{Vẫn đủ<br/>điều kiện?}
        Node_MarkUsed[Tạo đơn hàng SPF & Đánh dấu đã dùng mã]
    end

    %% Áp dụng style class
    class Node_Start startClass;
    class Node_SuccessPage endClass;
    class Node_SelectVoucher,Node_ChangeContext,Node_Pay,Node_ShowCheckout,Node_ShowVouchers,Node_UpdateUI,Node_ShowError,Node_ShowContextError,Node_GetConfig,Node_Validate,Node_ReValidate,Node_MarkUsed stepClass;
    class Node_CheckSKU,Node_CheckPTTT,Node_CheckExcl,Node_CheckReOK decisionClass;

    %% Luồng kết nối giữa các node
    Node_Start --> Node_ShowCheckout
    Node_ShowCheckout --> Node_GetConfig
    Node_GetConfig --> Node_ShowCheckout
    
    Node_ShowCheckout --> Node_SelectVoucher
    Node_SelectVoucher --> Node_ShowVouchers
    Node_ShowVouchers --> Node_Validate
    
    Node_Validate --> Node_CheckSKU
    
    Node_CheckSKU -->|Không| Node_ShowError
    Node_CheckSKU -->|Có| Node_CheckPTTT
    
    Node_CheckPTTT -->|Không| Node_ShowError
    Node_CheckPTTT -->|Có| Node_CheckExcl
    
    Node_CheckExcl -->|Có| Node_ShowError
    Node_CheckExcl -->|Không| Node_UpdateUI
    
    Node_ShowError --> Node_ShowVouchers
    
    Node_UpdateUI --> Node_ChangeContext
    Node_UpdateUI --> Node_Pay
    
    Node_ChangeContext --> Node_ReValidate
    Node_ReValidate --> Node_CheckReOK
    
    Node_CheckReOK -->|Không| Node_ShowContextError
    Node_CheckReOK -->|Có| Node_UpdateUI
    
    Node_ShowContextError --> Node_SelectVoucher
    
    Node_Pay --> Node_MarkUsed
    Node_MarkUsed --> Node_SuccessPage
```

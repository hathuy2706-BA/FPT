# Sơ đồ Flow Diagram: Luồng Nghiệp Vụ Áp Dụng Voucher FPT.vn (Phase 1)

Dưới đây là sơ đồ luồng hoạt động (Flow Diagram) thể hiện các bước rẽ nhánh và kiểm tra điều kiện áp dụng Voucher trên hệ thống FPT.vn.

![Sơ đồ Flow Diagram](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default', 'flowchart': { 'curve': 'linear', 'nodeSpacing': 35, 'rankSpacing': 50 } } }%%
flowchart TD
    classDef startNode fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
    classDef endNode fill:#F44336,stroke:#D32F2F,stroke-width:2px,color:#fff
    classDef processNode fill:#FFFFFF,stroke:#424242,stroke-width:1.5px,color:#212121
    classDef decisionNode fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#212121
    classDef errorNode fill:#FFEBEE,stroke:#C62828,stroke-width:1.5px,color:#C62828
    classDef retryNode fill:#E3F2FD,stroke:#1565C0,stroke-width:1.5px,color:#0D47A1

    %% ═══════════════════════════════════════
    %% BLOCK 1: KHỞI TẠO & VÀO CHECKOUT
    %% ═══════════════════════════════════════
    A([Bắt đầu])
    B["BE: Lấy cấu hình cước & danh sách voucher\ntừ Product Hub"]
    C["FE: Hiển thị trang Checkout — nút 'Chọn ưu đãi'"]
    D["KH: Nhấn 'Chọn ưu đãi' hoặc nhập mã thủ công"]
    E["FE: Hiển thị Popup danh sách ưu đãi"]
    F["BE: Kiểm tra điều kiện áp dụng voucher"]

    %% ═══════════════════════════════════════
    %% BLOCK 2: KIỂM TRA ĐIỀU KIỆN
    %% ═══════════════════════════════════════
    G{"Đúng SKU\nyêu cầu?"}
    H{"Đúng PTTT\nyêu cầu?"}
    I{"Voucher\nbị loại trừ?"}

    %% ═══════════════════════════════════════
    %% BLOCK 3: XỬ LÝ LỖI (Nhánh phải)
    %% ═══════════════════════════════════════
    ERR_SKU["FE: Lỗi — Sai SKU / Gói cước\nkhông đáp ứng điều kiện voucher"]
    ERR_PTTT["FE: Lỗi — Sai PTTT / COD\nkhông được áp dụng voucher"]
    ERR_EXCL["FE: Lỗi — Voucher loại trừ nhau\nkhông thể áp dụng đồng thời"]
    RETRY["KH: Xem thông báo lỗi\nvà chọn lại ưu đãi phù hợp"]
    REENTER["KH: Nhập mã mới hoặc bỏ qua ưu đãi"]

    %% ═══════════════════════════════════════
    %% BLOCK 4: ÁP DỤNG THÀNH CÔNG
    %% ═══════════════════════════════════════
    J["FE: Cập nhật giá cước mới\n'Áp dụng mã ưu đãi thành công'"]

    %% ═══════════════════════════════════════
    %% BLOCK 5: THAY ĐỔI BỐI CẢNH
    %% ═══════════════════════════════════════
    L{"KH thay đổi\nbối cảnh đơn hàng\nPTTT / SKU / Gói cước?"}
    M["BE: Tự động kiểm tra lại\nđiều kiện voucher"]
    N{"Voucher\nvẫn hợp lệ?"}
    O["FE: Hiển thị lỗi bối cảnh mới\nThu hồi voucher — Hoàn về giá gốc"]
    P["KH: Xem lại ưu đãi\nvà chọn ưu đãi phù hợp với bối cảnh mới"]
    Q["KH: Nhập / Chọn mã mới\nhoặc tiếp tục không dùng ưu đãi"]

    %% ═══════════════════════════════════════
    %% BLOCK 6: THANH TOÁN & KẾT THÚC
    %% ═══════════════════════════════════════
    PAY["KH: Nhấn nút 'Thanh toán'"]
    DONE["BE: Tạo đơn hàng SPF\n& Đánh dấu mã voucher đã sử dụng"]
    R([Kết thúc])

    %% Gán style
    class A startNode
    class R endNode
    class B,C,D,E,F,J,M,O,P,PAY,DONE processNode
    class G,H,I,L,N decisionNode
    class ERR_SKU,ERR_PTTT,ERR_EXCL errorNode
    class RETRY,REENTER,Q retryNode

    %% ═══════════════════════════════════════
    %% LUỒNG CHÍNH
    %% ═══════════════════════════════════════
    A --> B --> C --> D --> E --> F

    F --> G
    G -->|Có| H
    H -->|Có| I
    I -->|Không| J

    %% Nhánh lỗi điều kiện
    G -->|Không| ERR_SKU --> RETRY
    H -->|Không| ERR_PTTT --> RETRY
    I -->|Có| ERR_EXCL --> RETRY
    RETRY --> REENTER --> F

    %% Luồng sau khi áp dụng
    J --> L
    L -->|Không thay đổi| PAY
    L -->|Có thay đổi| M
    M --> N
    N -->|Vẫn hợp lệ| J
    N -->|Không còn hợp lệ| O --> P --> Q --> F

    %% Kết thúc
    PAY --> DONE --> R
```

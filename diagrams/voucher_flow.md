# Sơ đồ Flow Diagram: Hành Trình Khách Hàng — Áp Dụng Voucher FPT.vn (Phase 1)

Sơ đồ mô tả trải nghiệm của **Khách hàng** khi áp dụng voucher ưu đãi trong luồng Checkout trên FPT.vn.

**Ký hiệu:**
- 🔵 Hình chữ nhật xanh dương → Hành động của Khách hàng
- 🟡 Hình thoi vàng → Điểm quyết định / rẽ nhánh
- 🟨 Hình bình hành vàng lá (nét đứt) → Note hệ thống — quy tắc vận hành ẩn
- 🔴 Hình chữ nhật đỏ → Thông báo lỗi / cảnh báo KH thấy
- 🟢 Hình chữ nhật xanh lá → Thông báo thành công KH thấy

![Sơ đồ Flow Diagram - Hành Trình KH Áp Dụng Voucher](./voucher_flow.png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'default', 'flowchart': { 'curve': 'linear', 'nodeSpacing': 45, 'rankSpacing': 55 } } }%%
flowchart TD

    classDef startEnd fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
    classDef stopEnd  fill:#F44336,stroke:#D32F2F,stroke-width:2px,color:#fff
    classDef khStep   fill:#E3F2FD,stroke:#1565C0,stroke-width:1.5px,color:#0D47A1
    classDef gate     fill:#FFF9C4,stroke:#F57F17,stroke-width:2px,color:#5D4037
    classDef noteBox  fill:#F9FBE7,stroke:#AFB42B,stroke-width:1px,color:#558B2F
    classDef errBox   fill:#FFEBEE,stroke:#C62828,stroke-width:1.5px,color:#C62828
    classDef okBox    fill:#E8F5E9,stroke:#2E7D32,stroke-width:1.5px,color:#1B5E20
    classDef warnBox  fill:#FFF3E0,stroke:#E65100,stroke-width:1.5px,color:#BF360C

    %% ═══════════════════════════════════
    %% BƯỚC 1: VÀO CHECKOUT
    %% ═══════════════════════════════════
    START([Bắt đầu])
    S1["KH truy cập trang Checkout"]
    N1[/"Note: Hệ thống GET danh sách voucher
    hợp lệ theo gói DV và PTTT mặc định
    của đơn hàng hiện tại"/]

    %% ═══════════════════════════════════
    %% BƯỚC 2: CHỌN ƯU ĐÃI
    %% ═══════════════════════════════════
    S2["KH nhấn Chọn ưu đãi"]

    CHK_EMPTY{"Có voucher
    khả dụng?"}

    EMPTY["Không có ưu đãi khả dụng
    cho đơn hàng này"]

    S3["KH xem danh sách voucher"]
    N3[/"Note: Hiển thị thông tin cơ bản mỗi voucher:
    Tên ưu đãi, Giá trị giảm, Hạn sử dụng
    Điều kiện áp dụng ngắn gọn
    Tag Sắp hết hạn nếu gần deadline"/]

    %% ═══════════════════════════════════
    %% BƯỚC 3: KH CHỌN VOUCHER
    %% ═══════════════════════════════════
    S4["KH tick chọn voucher"]

    CHK_EXCL{"Voucher bị loại trừ
    với voucher đã chọn?"}
    N4[/"Note: Kiểm tra ngay tại thời điểm
    KH tick chọn — hiển thị inline
    trong danh sách, không cần submit"/]

    WARN_EXCL["Cảnh báo inline:
    Không thể sử dụng với ưu đãi đã chọn khác"]

    %% ═══════════════════════════════════
    %% BƯỚC 4: HỆ THỐNG KIỂM TRA ĐIỀU KIỆN
    %% ═══════════════════════════════════
    S5["KH nhấn Xác nhận / Áp dụng mã"]

    CHK_COND{"Đơn hàng đáp ứng
    điều kiện voucher?"}
    N5[/"Note: BE kiểm tra điều kiện đơn hàng:
    Đúng gói DV hoặc SKU yêu cầu?
    Đúng phương thức thanh toán?
    FE chỉ nhận kết quả và hiển thị"/]

    WARN_COND["Cảnh báo điều kiện cụ thể
    VD: Ưu đãi chỉ áp dụng cho
    hình thức thanh toán Online"]

    %% ═══════════════════════════════════
    %% BƯỚC 5: ÁP DỤNG THÀNH CÔNG
    %% ═══════════════════════════════════
    OK["Thông báo: Áp dụng mã ưu đãi thành công!
    Giá cước được cập nhật trong đơn hàng"]
    N_OK[/"Note: BE tính giá trị giảm
    theo mức tối đa khai báo trong QLCS.
    FE nhận kết quả và cập nhật hiển thị"/]

    %% ═══════════════════════════════════
    %% BƯỚC 6: THANH TOÁN
    %% ═══════════════════════════════════
    PAY["KH xác nhận PTTT và nhấn Thanh toán"]
    N_PAY[/"Note: Hệ thống tạo đơn trên SPF
    và đánh dấu mã voucher đã sử dụng"/]

    DONE([Kết thúc])

    %% Gán style
    class START startEnd
    class DONE stopEnd
    class S1,S2,S3,S4,S5,PAY khStep
    class CHK_EMPTY,CHK_EXCL,CHK_COND gate
    class N1,N3,N4,N5,N_OK,N_PAY noteBox
    class EMPTY,WARN_COND errBox
    class WARN_EXCL warnBox
    class OK okBox

    %% ═══════════════════════════════════
    %% LUỒNG LIÊN KẾT
    %% ═══════════════════════════════════
    START --> S1
    S1 -. "GET voucher" .-> N1
    S1 --> S2 --> CHK_EMPTY

    CHK_EMPTY -->|Không có| EMPTY
    EMPTY --> S2

    CHK_EMPTY -->|Có voucher| S3
    S3 -. "Thông tin hiển thị" .-> N3
    S3 --> S4

    S4 --> CHK_EXCL
    CHK_EXCL -. "Kiểm tra inline" .-> N4

    CHK_EXCL -->|Có loại trừ| WARN_EXCL
    WARN_EXCL --> S3

    CHK_EXCL -->|Không loại trừ| S5

    S5 --> CHK_COND
    CHK_COND -. "Rule kiểm tra điều kiện" .-> N5

    CHK_COND -->|Không đáp ứng| WARN_COND
    WARN_COND --> S3

    CHK_COND -->|Đáp ứng| OK
    OK -. "Cập nhật giá" .-> N_OK

    OK --> PAY
    PAY -. "Xử lý đơn hàng" .-> N_PAY
    PAY --> DONE
```

## Bảng Hành Trình Khách Hàng (Customer Journey)

| # | Hành Động KH | KH Thấy Gì | Hệ Thống Xử Lý Ngầm |
|:---:|:---|:---|:---|
| 1 | Truy cập trang Checkout | Trang Checkout với nút "Chọn ưu đãi" | GET danh sách voucher hợp lệ theo gói DV, PTTT mặc định |
| 2 | Nhấn "Chọn ưu đãi" | Popup danh sách voucher / Empty state nếu không có | Lọc và sắp xếp danh sách voucher |
| 3 | Xem danh sách voucher | Tên, giá trị giảm, hạn dùng, điều kiện ngắn, tag "Sắp hết hạn" | — |
| 4 | Tick chọn voucher | Cảnh báo inline nếu voucher bị loại trừ nhau | Kiểm tra xung đột tức thì (real-time) |
| 5 | Nhấn "Xác nhận / Áp dụng" | Thành công hoặc cảnh báo điều kiện cụ thể | BE kiểm tra gói DV, SKU, PTTT |
| 6 | Nhấn "Thanh toán" | Trang xác nhận đơn hàng thành công | Tạo đơn SPF, đánh dấu mã đã dùng |

## Giải Thích Chi Tiết Các Trường Hợp (Cases)

### Case 1: Không có voucher khả dụng
Khi KH nhấn "Chọn ưu đãi" mà hệ thống không trả về voucher nào phù hợp với thông tin checkout hiện tại → Hiển thị **empty state** với nội dung: *"Không có ưu đãi khả dụng cho đơn hàng này"*. KH có thể nhập mã thủ công nếu có.

### Case 2: Voucher không áp dụng đồng thời (Loại trừ nhau)
Được kiểm tra **ngay khi KH tick chọn** voucher trong danh sách (không cần nhấn Xác nhận):
- Nếu Voucher A đang được chọn và Voucher B không được dùng đồng thời → Hiển thị **cảnh báo inline** ngay tại dòng Voucher B: *"Không thể sử dụng với ưu đãi đã chọn khác"*
- KH có thể bỏ chọn Voucher A để chọn Voucher B, hoặc giữ nguyên lựa chọn cũ

### Case 3: Voucher không đáp ứng điều kiện đơn hàng
Sau khi KH nhấn "Xác nhận", BE kiểm tra và trả về lỗi điều kiện **cụ thể**:
- Sai phương thức thanh toán → *"Ưu đãi chỉ áp dụng cho hình thức thanh toán Online"*
- Sai gói cước / SKU → *"Ưu đãi không áp dụng cho gói dịch vụ đang chọn"*
- KH có thể thay đổi điều kiện đơn hoặc chọn voucher khác

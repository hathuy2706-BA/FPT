---
name: diagram-drawer
description: Skill chuyên dụng để thiết kế và vẽ 3 loại sơ đồ nghiệp vụ: (1) BPMN swimlane dọc — luồng nghiệp vụ tổng quan cho URD, dùng Python SVG generator; (2) Sequence Diagram — tương tác kỹ thuật hệ thống, dùng Mermaid; (3) Flowchart Swimlane — luồng liên phòng ban, dùng Mermaid. Kích hoạt khi user yêu cầu vẽ sơ đồ, thiết kế luồng nghiệp vụ, cập nhật sơ đồ đã có, hoặc nhúng sơ đồ vào URD/SRS.
---

# Skill Vẽ Sơ Đồ Hệ Thống & Trực Quan Hóa (Diagram Drawer)

Skill này hướng dẫn chi tiết cách thiết kế sơ đồ dạng Mermaid (đặc biệt là Sequence Diagram) theo chuẩn giao diện nền tối (Dark Theme), xuất ra ảnh PNG/SVG chất lượng cao và trình bày tài liệu theo đúng cấu trúc template chuẩn của dự án.

---

## 1. Bộ Quy Tắc Ký Hiệu UML Sequence Diagram (Chuẩn draw.io / UML 2.5)

Dưới đây là **bảng tổng hợp đầy đủ** tất cả ký hiệu (notation) trong Sequence Diagram theo chuẩn UML 2.5 (giống draw.io), kèm theo cú pháp tương ứng trong Mermaid.

### A. Thành Phần Cốt Lõi (Core Elements)

| # | Ký hiệu UML | Hình dạng (Draw.io) | Ý nghĩa | Cú pháp Mermaid |
|---|-------------|---------------------|---------|-----------------|
| 1 | **Actor** | 🧍 Hình người que (stick figure) | Thực thể bên ngoài tương tác với hệ thống (người dùng, hệ thống ngoài) | `actor User as "Người dùng"` |
| 2 | **Participant (Object)** | 📦 Hộp chữ nhật bo góc | Đối tượng/thành phần tham gia luồng tương tác (class, service, module) | `participant System as "Hệ thống"` |
| 3 | **Lifeline** | ┆ Đường đứt nét dọc kéo xuống từ participant | Biểu thị sự tồn tại của đối tượng theo trục thời gian (đọc từ trên xuống) | Tự động sinh khi khai báo participant/actor |
| 4 | **Activation Box (Execution Specification)** | ▮ Hộp chữ nhật mỏng trên lifeline | Khoảng thời gian đối tượng đang **xử lý tích cực** (đang thực thi operation) | `activate A` / `deactivate A` hoặc ký hiệu `+`/`-` trên mũi tên |

#### Quy tắc chọn Actor vs Participant:
- **Dùng `actor`** khi thực thể là **con người hoặc hệ thống bên ngoài** (End-user, Admin, 3rd-party API)
- **Dùng `participant`** khi thực thể là **thành phần nội bộ hệ thống** (Service, Database, Module, Component)
- **Quy ước dự án**: Ưu tiên dùng `participant` cho tất cả để đảm bảo hiển thị đồng bộ hộp chữ nhật. Chỉ dùng `actor` khi muốn nhấn mạnh vai trò con người.

---

### B. Các Loại Tin Nhắn / Mũi Tên (Message Types)

Đây là phần **quan trọng nhất**, tương ứng với các mũi tên trong bảng ký hiệu draw.io:

| # | Loại Message | Ký hiệu Mũi tên | Mô tả | Cú pháp Mermaid |
|---|-------------|-----------------|-------|-----------------|
| 1 | **Synchronous (Đồng bộ)** | ──────▶ (Nét liền, đầu mũi tên **đặc/lấp đầy**) | Bên gửi **chờ** phản hồi trước khi tiếp tục. Ví dụ: gọi hàm, HTTP request chờ response | `A->>B: "Gọi API đồng bộ"` |
| 2 | **Asynchronous (Bất đồng bộ)** | ──────▷ (Nét liền, đầu mũi tên **mở/rỗng**) | Bên gửi **không chờ** phản hồi, tiếp tục xử lý ngay. Ví dụ: gửi event, push notification | `A-)B: "Gửi event bất đồng bộ"` |
| 3 | **Return (Phản hồi)** | ╌╌╌╌╌╌▷ (Nét **đứt**, đầu mũi tên mở) | Trả về kết quả/giá trị cho lời gọi trước đó | `B-->>A: "Trả về kết quả"` |
| 4 | **Self-Message (Tự gọi)** | ↻ Mũi tên vòng ngược lại chính mình | Đối tượng gọi method/xử lý nội bộ của chính nó | `A->>A: "Xử lý logic nội bộ"` |
| 5 | **Solid Line (Nét liền, không mũi tên)** | ────── (Nét liền, không có đầu) | Liên kết đơn giản, ít dùng trong sequence | `A->B: "Tin nhắn"` |
| 6 | **Dotted Line (Nét đứt, không mũi tên)** | ╌╌╌╌╌╌ (Nét đứt, không có đầu) | Liên kết phản hồi đơn giản | `A-->B: "Phản hồi"` |

#### Bảng Tra Cứu Nhanh Mũi Tên Mermaid:
```
Cú pháp Mermaid    │ Kiểu đường │ Kiểu đầu mũi tên    │ Dùng khi
───────────────────┼────────────┼──────────────────────┼─────────────────
  A->B             │ Nét liền   │ Không có đầu         │ Ít dùng
  A-->B            │ Nét đứt    │ Không có đầu         │ Ít dùng
  A->>B            │ Nét liền   │ Mũi tên đặc (▶)     │ ★ Gọi đồng bộ (sync call)
  A-->>B           │ Nét đứt    │ Mũi tên đặc (▶)     │ ★ Phản hồi (return)
  A-)B             │ Nét liền   │ Mũi tên mở (▷)      │ ★ Gọi bất đồng bộ (async)
  A--)B            │ Nét đứt    │ Mũi tên mở (▷)      │ Phản hồi bất đồng bộ
  A->>+B           │ Nét liền   │ Mũi tên đặc + Kích  │ ★ Gọi & kích hoạt (activate)
  B-->>-A          │ Nét đứt    │ Mũi tên đặc + Hủy   │ ★ Trả về & hủy kích hoạt
```

---

### C. Activation (Hộp Kích Hoạt / Execution Specification)

Activation Box biểu thị khoảng thời gian một đối tượng đang tích cực xử lý. Trong draw.io hiển thị là hộp chữ nhật mỏng nằm trên lifeline.

#### Cách 1: Ký hiệu viết tắt trên mũi tên (Khuyến nghị)
```mermaid
A->>+B: "Gọi API"        %% Mũi tên + dấu "+" → kích hoạt B
B-->>-A: "Trả kết quả"   %% Mũi tên + dấu "-" → hủy kích hoạt B
```

#### Cách 2: Khai báo tường minh
```mermaid
A->>B: "Gọi API"
activate B                 %% Bắt đầu hộp activation trên lifeline B
B->>B: "Xử lý nội bộ"
B-->>A: "Trả kết quả"
deactivate B               %% Kết thúc hộp activation
```

#### Activation lồng nhau (Nested Activation):
```mermaid
A->>+B: "Gọi B"
B->>+C: "B gọi tiếp C"    %% C được activate trong khi B vẫn active
C-->>-B: "C trả về"       %% Deactivate C
B-->>-A: "B trả về"       %% Deactivate B
```

---

### D. Tạo & Hủy Đối Tượng (Create & Destroy)

Trong draw.io: **Create** = mũi tên đứt nét chỉ tới hộp participant mới xuất hiện; **Destroy** = dấu ✕ (chữ X lớn) đặt ở cuối lifeline.

```mermaid
%% Tạo đối tượng mới giữa chừng
create participant Session as "Session"
A->>Session: "Khởi tạo session mới"

%% Hủy đối tượng
destroy Session
A-xSession: "Đóng và hủy session"
```

> **Lưu ý:** `create` và `destroy` là từ khóa Mermaid v10.9+. Kiểm tra phiên bản Mermaid khi sử dụng.

---

### E. Combined Fragments (Khung Logic Phức Hợp)

Combined Fragments trong draw.io là **khung hình chữ nhật lớn** bao quanh một nhóm tin nhắn, có nhãn loại ở góc trên-trái. Đây là công cụ mạnh nhất để biểu diễn logic điều kiện, lặp, song song.

| # | Fragment | Ký hiệu Draw.io | Ý nghĩa | Cú pháp Mermaid |
|---|----------|-----------------|---------|-----------------|
| 1 | **alt** | Khung chia đôi bằng nét đứt ngang, nhãn `alt` | Rẽ nhánh if-else: chỉ **1 nhánh** được thực thi | `alt ... else ... end` |
| 2 | **opt** | Khung đơn, nhãn `opt` | Tùy chọn (chỉ if, không else): thực thi nếu điều kiện đúng | `opt ... end` |
| 3 | **loop** | Khung đơn, nhãn `loop` | Lặp lại: thực thi nhiều lần theo điều kiện | `loop ... end` |
| 4 | **break** | Khung đơn, nhãn `break` | Ngoại lệ/thoát: nếu điều kiện đúng, thoát khỏi luồng bao ngoài | `break ... end` |
| 5 | **par** | Khung chia bằng nét đứt, nhãn `par` | Song song: các phân đoạn chạy **đồng thời** | `par ... and ... end` |
| 6 | **critical** | Khung đơn, nhãn `critical` | Vùng tới hạn: chỉ 1 thread được truy cập tại 1 thời điểm | `critical ... option ... end` |

#### Ví dụ đầy đủ các loại Fragment:

```mermaid
sequenceDiagram
    participant A as "Client"
    participant B as "Server"
    participant C as "Database"

    %% ═══ ALT: Rẽ nhánh if-else ═══
    alt Đăng nhập thành công
        B-->>A: "200 OK - Token JWT"
    else Sai mật khẩu
        B-->>A: "401 Unauthorized"
    else Tài khoản bị khóa
        B-->>A: "403 Forbidden"
    end

    %% ═══ OPT: Tùy chọn (chỉ thực hiện nếu điều kiện đúng) ═══
    opt Người dùng bật 2FA
        B->>A: "Yêu cầu nhập mã OTP"
        A->>B: "Gửi mã OTP"
    end

    %% ═══ LOOP: Vòng lặp ═══
    loop Mỗi 30 giây
        A->>B: "Heartbeat / Ping"
        B-->>A: "Pong"
    end

    %% ═══ BREAK: Ngoại lệ thoát ═══
    break Khi hệ thống quá tải
        B-->>A: "503 Service Unavailable"
    end

    %% ═══ PAR: Song song ═══
    par Gửi email thông báo
        B-)C: "Queue email job"
    and Ghi log audit
        B-)C: "Insert audit log"
    end

    %% ═══ CRITICAL: Vùng tới hạn ═══
    critical Trừ tiền tài khoản
        B->>C: "UPDATE balance SET amount = amount - 100"
    option Nếu số dư không đủ
        B-->>A: "Giao dịch thất bại - Insufficient balance"
    end
```

---

### F. Ghi Chú (Notes)

Ghi chú trong draw.io là hộp chữ nhật có góc gấp, nối tới lifeline bằng nét đứt.

```mermaid
%% Ghi chú bên trái participant
Note left of A: Ghi chú bên trái

%% Ghi chú bên phải participant
Note right of B: Ghi chú bên phải

%% Ghi chú trải ngang qua nhiều participant (dải phân cảnh)
Note over A, B: TIÊU ĐỀ PHÂN CẢNH
```

> **⚠️ BẮT BUỘC:** Luôn có **dấu cách sau dấu phẩy** trong `Note over A, B` (ĐÚNG) thay vì `Note over A,B` (SAI - gây lỗi biên dịch).

---

### G. Vùng Đánh Dấu / Highlight (rect)

Dùng `rect` để tô nền nhóm tin nhắn, giúp nhấn mạnh một phần trong sơ đồ.

```mermaid
rect rgb(40, 40, 80)
    A->>B: "Bước quan trọng được highlight"
    B-->>A: "Phản hồi"
end

rect rgba(255, 165, 0, 0.15)
    Note over A, B: Khu vực cảnh báo
    A->>B: "Hành động cần chú ý"
end
```

---

### H. Bảng Tổng Hợp Mapping: Ký Hiệu Draw.io → Mermaid Syntax

Bảng tham chiếu nhanh cho toàn bộ ký hiệu:

| Ký hiệu Draw.io | Hình | Mermaid Syntax | Ghi chú |
|:---|:---:|:---|:---|
| Actor | 🧍 | `actor X as "Tên"` | Hình người que |
| Object / Participant | 📦 | `participant X as "Tên"` | Hộp chữ nhật |
| Lifeline | ┆ | *(tự động)* | Đường đứt dọc |
| Activation Box | ▮ | `activate X` / `deactivate X` hoặc `+`/`-` | Hộp mỏng trên lifeline |
| Synchronous Message | ──▶ | `A->>B: "msg"` | Nét liền, đầu đặc |
| Asynchronous Message | ──▷ | `A-)B: "msg"` | Nét liền, đầu mở |
| Return Message | ╌╌▷ | `A-->>B: "msg"` | Nét đứt, phản hồi |
| Self-Message | ↻ | `A->>A: "msg"` | Tự gọi chính mình |
| Create | ╌╌▷📦 | `create participant X` | Tạo đối tượng mới |
| Destroy | ✕ | `destroy X` | Hủy đối tượng |
| Cross Message | ──✕ | `A-xB: "msg"` | Mũi tên có X ở đầu |
| Note | 📝 | `Note left/right/over ...` | Hộp ghi chú |
| alt Fragment | [alt] | `alt ... else ... end` | Rẽ nhánh điều kiện |
| opt Fragment | [opt] | `opt ... end` | Tùy chọn |
| loop Fragment | [loop] | `loop ... end` | Vòng lặp |
| break Fragment | [break] | `break ... end` | Ngoại lệ/thoát |
| par Fragment | [par] | `par ... and ... end` | Song song |
| critical Fragment | [critical] | `critical ... option ... end` | Vùng tới hạn |
| Highlight Area | 🟦 | `rect rgb(...) ... end` | Tô nền highlight |

---

## 2. Nguyên Tắc Thiết Kế Sơ Đồ Mermaid

Khi viết code Mermaid cho Sequence Diagram, luôn tuân thủ các quy tắc sau để đảm bảo sơ đồ trực quan và không bị lỗi biên dịch:

### A. Cấu Hình Theme Tối (Dark Theme)
Luôn đặt chỉ thị cấu hình theme tối ở ngay dòng đầu tiên của khối code Mermaid:
```mermaid
%%{init: { 'theme': 'dark' } }%%
```

### B. Khai Báo Participant / Actor
- **`participant`**: Hiển thị dạng hộp chữ nhật bo góc — dùng cho thành phần nội bộ hệ thống
- **`actor`**: Hiển thị dạng hình người que — dùng cho người dùng hoặc hệ thống bên ngoài
- **Quy ước dự án**: Mặc định dùng `participant` cho tất cả. Chỉ dùng `actor` khi cần nhấn mạnh rõ ràng đây là con người.

```mermaid
participant Customer as "Khách hàng"
participant Portal as "CMS Portal"
```

### C. Dấu Cách Trong Phân Cảnh (Note over)
Cú pháp `Note over` để vẽ các dải phân cảnh nằm ngang kéo dài bắt buộc phải có **dấu cách (space) sau dấu phẩy** ngăn cách giữa 2 thực thể:
- **ĐÚNG:** `Note over Admin, Customer: TIÊU ĐỀ PHÂN CẢNH`
- **SAI:** `Note over Admin,Customer: TIÊU ĐỀ PHÂN CẢNH` (Không có dấu cách sẽ gây lỗi biên dịch *Unknown diagram error*).

### D. Sử Dụng Dấu Ngoặc Kép Cho Nội Dung Tin Nhắn
Để tránh lỗi phân tích cú pháp khi nội dung tin nhắn chứa ký tự đặc biệt hoặc tiếng Việt, hãy luôn bọc các mô tả tin nhắn trong dấu ngoặc kép `""`:
```mermaid
Admin->>Portal: "1. Tạo/Sửa bài viết (Gán tag: 'camera')"
```

### E. Sử Dụng `autonumber` Cho Đánh Số Tự Động
Luôn thêm `autonumber` ngay sau `sequenceDiagram` để Mermaid tự đánh số thứ tự tin nhắn:
```mermaid
sequenceDiagram
    autonumber
```

---

## 3. Template Cấu Trúc File Trình Bày Sơ Đồ

Mỗi sơ đồ khi tạo ra sẽ chỉ bao gồm **2 file duy nhất** nằm trong thư mục `diagrams/`:
1.  **File tài liệu Markdown (`[tên-sơ-đồ].md`):** File trình bày, chứa cả mã nguồn Mermaid (trong khối code block) và hình ảnh hiển thị kèm mô tả nghiệp vụ chi tiết.
2.  **File ảnh PNG (`[tên-sơ-đồ].png`):** File ảnh được biên dịch ra từ khối code Mermaid nằm trong file Markdown để nhúng hiển thị trực tiếp.

Tuyệt đối **KHÔNG** tạo thêm các file nguồn riêng lẻ `.mermaid`, file vector `.svg` hoặc script `.ps1` riêng cho từng sơ đồ để tránh làm rác thư mục.

### Template File `.md` chuẩn (`diagrams/[tên-sơ-đồ].md`)
```markdown
# Sơ đồ Sequence Diagram: [TÊN SƠ ĐỒ]

Dưới đây là sơ đồ trực quan luồng [MÔ TẢ NGẮN GỌN LUỒNG HOẠT ĐỘNG].

![Sơ đồ Sequence Diagram](./[tên-sơ-đồ].png)

## Mã nguồn Mermaid (Dùng để render ảnh)
```mermaid
%%{init: { 'theme': 'dark' } }%%
sequenceDiagram
    autonumber
    participant [Thực thể 1] as "[Tên hiển thị 1]"
    participant [Thực thể 2] as "[Tên hiển thị 2]"

    Note over [Thực thể 1], [Thực thể 2]: [TÊN PHÂN CẢNH]
    [Thực thể 1]->>+[Thực thể 2]: "1. [Mô tả hành động]"
    [Thực thể 2]-->>[Thực thể 1]: "2. [Mô tả phản hồi]"
    deactivate [Thực thể 2]
```

## Bảng ký hiệu sử dụng trong sơ đồ

| Ký hiệu | Ý nghĩa |
|----------|---------|
| `participant` | Thành phần hệ thống (hộp chữ nhật) |
| `actor` | Người dùng bên ngoài (hình người) |
| `──▶` (`->>`) | Gọi đồng bộ (chờ phản hồi) |
| `╌╌▶` (`-->>`) | Phản hồi / Return |
| `──▷` (`-)`) | Gọi bất đồng bộ |
| `↻` (`A->>A`) | Tự gọi nội bộ |
| `▮ activate/deactivate` | Hộp kích hoạt (đang xử lý) |
| `alt/else/end` | Rẽ nhánh điều kiện |
| `opt/end` | Xử lý tùy chọn |
| `loop/end` | Vòng lặp |
| `par/and/end` | Xử lý song song |
| `Note over` | Dải phân cảnh / Ghi chú |
| `rect` | Highlight vùng quan trọng |

## Giải thích luồng nghiệp vụ chi tiết

### 1. [Phân đoạn nghiệp vụ 1]
*   **Bước 1 - N:** [Giải thích chi tiết hoạt động của các bước]

### 2. [Phân đoạn nghiệp vụ 2]
*   **Bước N+1 - M:** [Giải thích chi tiết hoạt động của các bước]
```

---

## 4. Phương Pháp Phân Tích Nghiệp Vụ & Thiết Kế Luồng Cho BA

Khi phân tích một yêu cầu nghiệp vụ để trực quan hóa thành sơ đồ, BA cần tuân thủ quy trình phân tích và chuyển hóa sau:

### A. Phân tích để vẽ Flow Diagram (Swimlane Flowchart)
Áp dụng khi cần mô tả **luồng công việc liên phòng ban (Cross-functional)** hoặc các hoạt động có sự tham gia của cả con người và hệ thống tự động.
1. **Xác định Đối tượng (Who/What)**: Liệt kê tất cả các bộ phận tham gia (ví dụ: PO, MKT, Khách hàng, DVKH, Hệ thống, Kỹ thuật viên). Mỗi đối tượng sẽ tương ứng với một `subgraph` (làn) trong Mermaid.
2. **Xác định các sự kiện Tự động hóa**: Phân biệt rõ các tác vụ thủ công (do con người làm) và các tác vụ tự động (hệ thống tự duyệt hợp đồng, tự tạo phiếu thi công, tự gạch nợ, tự phát hành hóa đơn). Các node tự động nên được gom vào làn `HỆ THỐNG`.
3. **Mẫu phân tích**: Sử dụng file [flowchart-swimlane-template.md](file:///Users/hathuy/Documents/FPT-1/.agent/skills/diagram-drawer/templates/flowchart-swimlane-template.md) để bắt đầu.

### B. Phân tích để vẽ Sequence Diagram
Áp dụng khi cần mô tả **tương tác kỹ thuật chi tiết giữa các hệ thống (System Interaction)**, các cuộc gọi API, và xử lý logic của Back-end.
1. **Xác định Actor & Participants**: Actor là con người hoặc hệ thống bên ngoài. Participants là các thành phần hệ thống nội bộ (FE, BE Gateway, Microservices như PIM, OMS, Bảo hành APP, v.v.).
2. **Xác định Logic rẽ nhánh (Decision Logic)**: Thể hiện rõ các kịch bản kiểm tra điều kiện (ví dụ: Kiểm tra IMEI có ngày xuất bán > 7 ngày thì báo lỗi, <= 7 ngày thì đề xuất gói bảo hành). Sử dụng các khối `alt/else` trong Mermaid.
3. **Mẫu phân tích**: Sử dụng file [sequence-ba-template.md](file:///Users/hathuy/Documents/FPT-1/.agent/skills/diagram-drawer/templates/sequence-ba-template.md) để bắt đầu.

---

## 5. Quy Trình Tự Động Biên Dịch Mermaid sang PNG từ file MD

Để tạo ra file ảnh PNG có nền tối solid màu `#121212` trực tiếp từ khối code Mermaid trong file Markdown, sử dụng lệnh PowerShell sau:

### Lệnh PowerShell biên dịch nhanh:
```powershell
$name = "[tên-sơ-đồ]"; $md = Get-Content -Path "diagrams/$name.md" -Raw -Encoding UTF8; if ($md -match '(?s)```mermaid\s*\r?\n(.*?)\r?\n```') { $code = $Matches[1].Trim(); $bytes = [System.Text.Encoding]::UTF8.GetBytes($code); $b64 = [Convert]::ToBase64String($bytes).Replace('+', '-').Replace('/', '_').Replace('=', ''); Invoke-WebRequest -Uri "https://mermaid.ink/img/${b64}?bgColor=121212&type=png" -OutFile "diagrams/$name.png" -UserAgent "Mozilla/5.0" }
```

Hoặc bạn có thể chạy file script PowerShell dùng chung [generate_images.ps1](file:///c:/Users/Admin/OneDrive/Desktop/FPT/diagrams/generate_images.ps1) (nếu có) bằng cách truyền tên sơ đồ làm tham số.

---

## 6. Thư Mục Templates & Case Studies Cho BA

Skill này đi kèm thư mục `templates/` chứa các file mẫu sẵn sàng dùng ngay:

### 🔷 BPMN Swimlane (Python SVG Generator — chuẩn URD FPT)
> Dùng cho: sơ đồ luồng nghiệp vụ tổng quan, Customer Journey, nhúng vào URD Word

| File | Mô tả |
|------|--------|
| [bpmn_template/SKILL.md](templates/bpmn_template/SKILL.md) | **Hướng dẫn đầy đủ** BPMN: ký hiệu, quy trình 5 bước, cấu trúc node, điều chỉnh layout, checklist. |
| [bpmn_template/gen_bpmn_template.py](templates/bpmn_template/gen_bpmn_template.py) | **Generator template** — copy → `diagrams/gen_[tên]_bpmn.py`, thay placeholder, chạy ngay. |

**Quy trình nhanh:**
```bash
# 1. Copy template
cp .agent/skills/diagram-drawer/templates/bpmn_template/gen_bpmn_template.py \
   diagrams/gen_[module]_bpmn.py

# 2. Chỉnh sửa node/edge/annotation trong file vừa copy
# 3. Chạy generator
python3 diagrams/gen_[module]_bpmn.py          # → diagrams/[module]_bpmn.svg

# 4. Xuất PNG sắc nét (cần: brew install librsvg)
rsvg-convert -w 1600 diagrams/[module]_bpmn.svg -o diagrams/[module]_bpmn.png

# 5. Nhúng vào URD: xem ba-senior/templates/urd-template.md PHẦN 5
```

**Ví dụ thực tế đã kiểm chứng:** [`diagrams/gen_cart_bpmn.py`](../../../../diagrams/gen_cart_bpmn.py) (URD Giỏ hàng & Checkout đa SP)

---

### 🔶 Sequence Diagram & Flowchart (Mermaid)
> Dùng cho: tương tác API chi tiết (Sequence), luồng liên phòng ban (Flowchart)

| File | Mô tả |
|------|--------|
| [sequence-template.md](templates/sequence-template.md) | Mẫu file Markdown kèm khối Mermaid + chỗ nhúng ảnh PNG. |
| [flowchart-swimlane-template.md](templates/flowchart-swimlane-template.md) | Template Flow Diagram phân làn nghiệp vụ bằng Mermaid. |
| [sequence-ba-template.md](templates/sequence-ba-template.md) | Template Sequence Diagram tương tác hệ thống chi tiết. |
| [example-related-articles.md](templates/example-related-articles.md) | Ví dụ thực tế hoàn chỉnh (sơ đồ "Thông tin hay theo Tag SP"). |

**Quy trình tạo sơ đồ Mermaid:**
1. Copy file template tương ứng → `diagrams/[tên-mới].md`
2. Điền nội dung vào khối ` ```mermaid ``` ` cùng mô tả chi tiết
3. Chạy PowerShell biên dịch nhanh ở Mục 5 để sinh `diagrams/[tên-mới].png`
4. Kiểm tra hiển thị trong file Markdown mới tạo

---

### Bảng chọn loại sơ đồ

| Yêu cầu | Loại sơ đồ | Template |
|---|---|---|
| Luồng nghiệp vụ tổng quan cho URD, Customer Journey, ai làm gì | **BPMN Swimlane** | `bpmn_template/gen_bpmn_template.py` |
| Tương tác API giữa các hệ thống, call sequence kỹ thuật | **Sequence Diagram** | `sequence-ba-template.md` |
| Luồng công việc liên phòng ban, quy trình nghiệp vụ nội bộ | **Flowchart Swimlane** | `flowchart-swimlane-template.md` |


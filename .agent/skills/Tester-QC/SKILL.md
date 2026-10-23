---
name: Tester-QC
description: Chuyên gia kiểm thử phần mềm (Tester/QC) và Quản lý nghiệm thu người dùng (UAT) chuẩn quốc tế ISTQB & FPT Telecom. Hỗ trợ thiết kế kịch bản test (Test Scenarios/Test Cases), phân tích ca kiểm thử Happy/Unhappy/Cross-system, vận hành quy trình UAT nhiều vòng (Round 1, 2, 3), phân loại lỗi (Defect/Severity), và tự động tạo/xuất Template UAT Excel chuẩn nhận diện 3 màu FPT (Xanh dương, Cam, Xanh lá).
---

# KỸ NĂNG TESTER & QUALITY CONTROL (TESTER-QC)

> **Mã hiệu tài liệu chuẩn**: `4.0-BM/PM/HDCV/FTEL`  
> **Phiên bản**: `1.0`  
> **Đơn vị ban hành**: FPT Telecom  
> **Font chuẩn tài liệu**: `Times New Roman` (Tiêu chuẩn hành chính FPT)  
> **Hệ thống màu chủ đạo**: 3 màu nhận diện thương hiệu Logo FPT (Xanh dương `#0054A6` · Cam `#F26522` · Xanh lá `#009E49`)

---

## MỤC LỤC TỔNG QUAN
1. [Mục I: Template UAT Chuẩn Dự Án FPT (Nguyên Bản & Quy Cách)](#mục-i-template-uat-chuẩn-dự-án-fpt)
2. [Mục II: Bộ Kỹ Năng QC Chuẩn Quốc Tế (ISTQB & ISO/IEC/IEEE 29119)](#mục-ii-bộ-kỹ-năng-qc-chuẩn-quốc-tế)
3. [Mục III: Ứng Dụng Skill Designer & Bộ Nhận Diện Thương Hiệu 3 Màu FPT](#mục-iii-ứng-dụng-skill-designer--nhận-diện-thương-hiệu-3-màu-fpt)
4. [Mục IV: Quy Trình Triển Khai UAT Step-by-Step](#mục-iv-quy-trình-triển-khai-uat-step-by-step)
5. [Mục V: Hướng Dẫn Tự Động Sinh & Quản Lý Template Excel](#mục-v-hướng-dẫn-tự-động-sinh--quản-lý-template-excel)

---

# MỤC I: TEMPLATE UAT CHUẨN DỰ ÁN FPT

Template UAT chuẩn được lưu trữ nguyên bản tại:
- File mẫu gốc dự án: `templates/uat_template_raw.xlsx` (Trích xuất từ Google Sheets ID: `1hg36S76ZU3-Z-v2LGbTqL7ahYsVnWRNSvzbcIJ2UQrs`)
- File mẫu chuẩn hóa Designer FPT: `templates/uat_template_fpt_standard.xlsx`

Toàn bộ file gồm 4 sheet cốt lõi được giữ nguyên cấu trúc:

```
UAT_Template.xlsx
├── 1. Cover      (Trang bìa định danh tài liệu chuẩn ISO FTEL)
├── 2. Summary    (Tổng hợp thông tin dự án, danh sách module & quyết định nghiệm thu PO)
├── 3. Report     (Dashboard thống kê & Bảng kịch bản test chi tiết đa vòng Round 1-2-3)
└── 4. Guideline  (Quy chuẩn hướng dẫn phạm vi, Happy/Unhappy case, lưu trữ QA)
```

---

### 1. Sheet `Cover` (Trang Bìa)
- **Tiêu đề trung tâm**: `USER ACCEPTANCE TEST - UAT` (Font: Times New Roman, Size 24pt, Bold, Màu Cam FPT `#F26522`).
- **Khung thông tin định danh**:
  - `Mã hiệu`: **4.0-BM/PM/HDCV/FTEL**
  - `Phiên bản`: **1.0**
  - Merge ô chuẩn: `B10:O10` (Tiêu đề), `F12:H12` & `I12:K12` (Mã hiệu), `F13:H13` & `I13:K13` (Phiên bản).

---

### 2. Sheet `Summary` (Tổng Hợp Dự Án & Nghiệm Thu)
- **Tiêu đề**: `UAT SUMMARY` (Ô D1, Font: Times New Roman, Size 20pt, Bold, Màu Cam FPT `#F26522`).
- **Khung thông tin dự án (Metadata)**:
  - `Project name`: FPT.VN (Cột C3 - D3)
  - `Version`: 1.0 (Cột C4 - D4)
  - `PO - Product Owner`: ThuyTT104 (Cột C5 - D5)
  - `PM - Project Manager`: [Tên PM phụ trách] (Cột C6 - D6)
  - `Testing start date`: [Ngày bắt đầu kiểm thử] (Cột E3 - F3)
  - `Testing end date`: [Ngày kết thúc kiểm thử] (Cột E4 - F4)
  - `Account Test - Division`: ISC / Đơn vị kiểm thử (Cột E5 - F5)
- **Bảng tổng kết trạng thái Module**:
  - Các cột: `NO.` | `MODULE` | `STATUS` | `COMMENTS`
  - Đánh số thứ tự chuẩn: `1.0`, `2.0`, `3.0`...

---

### 3. Sheet `Report` (Dashboard & Chi Tiết Kịch Bản Test)
Sheet `Report` là trái tim của đợt UAT, phục vụ ghi nhận kết quả và phản hồi lỗi giữa Đơn vị Test và ISC/Dev Team qua 3 vòng kiểm thử (Rounds).

#### A. Dashboard Thống Kê Tiến Độ Vòng Test (Dòng 3 - 5)
Bảng tổng hợp động sử dụng công thức tự động:
- Cột: `NO.` | `ROUND` | `TOTAL` | `PASSED` | `FAILED` | `PENDING` | `N/A`
- **Công thức tính dòng ROUND 1 (Row 4)**:
  - `TOTAL`: `=SUM($E4:$H4)`
  - `PASSED`: `=COUNTIF($J$10:$J$50,"PASSED")`
  - `FAILED`: `=COUNTIF($J$10:$J$50,"FAILED")`
  - `PENDING`: `=COUNTIF($J$10:$J$50,"PENDING")`
  - `N/A`: `=COUNTIF($J$10:$J$50,"N/A")`
- **Công thức dòng TOTAL (Row 5)**:
  - `=SUM(D4)`, `=SUM(E4)`, `=SUM(F4)`, `=SUM(G4)`, `=SUM(H4)`

#### B. Khung Thời Gian & Phân Quyền Vòng Test (Dòng 7 - 8)
- **Row 7 (Khung thời gian)**:
  - `ROUND 1 - FROM [20/10/2026] TO [27/10/2026]` (Cột J7:M7 - Nền Xanh dương sẫm)
  - `ROUND 2 - FROM [  /  /    ] TO [  /  /    ]` (Cột N7:Q7)
  - `ROUND 3 - FROM [  /  /    ] TO [  /  /    ]` (Cột R7:U7)
- **Row 8 (Phân trách nhiệm kết quả & Phản hồi)**:
  - `TEST RESULT (Đơn vị tham gia Test thông báo kết quả)`: Áp dụng cho Cột J-K, N-O, R-S (Nền Xanh dương FPT `#0054A6`, chữ trắng).
  - `ISC FEEDBACK (Đội phát triển phản hồi xử lý)`: Áp dụng cho Cột L-M, P-Q, T-U (Nền Xanh lá FPT `#009E49`, chữ trắng).

#### C. Chi Tiết Các Cột Nghiệp Vụ (Dòng 9)
| Cột | Tên Cột | Chiều rộng | Định dạng & Hướng dẫn |
|:---:|:---|:---:|:---|
| **B** | `NO.` | 7 | Căn giữa, in đậm màu Xanh dương FPT (`VD`, `1.0`, `2.0`...) |
| **C** | `MODULE`<br>*(Màn hình/Chức năng)* | 30 | Tên module hoặc tính năng được kiểm thử |
| **D - F** | `STEPS TO EXECUTE`<br>*(Mô tả các bước thực hiện)* | 45 *(Merged)* | Các bước thao tác tuần tự step-by-step rõ ràng (1, 2, 3...) |
| **G - I** | `EXPECTED RESULT`<br>*(Kết quả mong đợi)* | 45 *(Merged)* | Kết quả hệ thống phải trả về theo URD/SRS |
| **J** | `STATUS` (R1) | 15 | Dropdown: `PASSED`, `FAILED`, `PENDING`, `N/A` |
| **K** | `DESCRIPTION` (R1) | 35 | Mô tả lỗi thực tế, đính kèm mã lỗi hoặc link evidence |
| **L** | `ACTION` (R1) | 16 | Dropdown ISC: `DONE`, `DOING`, `CANCELLED`, `NEXT PLAN` |
| **M** | `NOTE` (R1) | 35 | Ghi chú phản hồi từ Dev/ISC |
| **N - Q**| `ROUND 2` | 15/35/16/35 | STATUS, MÔ TẢ LỖI, ACTION, NOTE vòng 2 |
| **R - U**| `ROUND 3` | 15/35/16/35 | STATUS, MÔ TẢ LỖI, ACTION, NOTE vòng 3 |

#### D. Dòng Dữ Liệu Mẫu Chuẩn (Row 10 - Ví dụ mẫu FPT)
- **NO.**: `VD`
- **MODULE**: `Gửi và xác thực mã OTP`
- **STEPS TO EXECUTE**:
  ```text
  1. Truy cập trang fpt.vn/nang-cap.
  2. Nhập số điện thoại hợp lệ (10 số, bắt đầu 03, 05, 07, 08, 09).
  3. Bấm 'Xác nhận'.
  ```
- **EXPECTED RESULT**:
  ```text
  1. Hệ thống gọi API gửi SMS OTP.
  2. Hiển thị popup nhập OTP với thời gian đếm ngược (05:00).
  ```
- **TEST RESULT**:
  - `STATUS`: `PASSED`
  - `DESCRIPTION`: `OTP nhận đúng trong 5s, countdown hiển thị chuẩn`
- **ISC FEEDBACK**:
  - `ACTION`: `DONE`
  - `NOTE`: `Đã verify trên môi trường Staging`

---

### 4. Sheet `Guideline` (Hướng Dẫn Sử Dụng & Quy Chuẩn UAT)
Nội dung chuẩn 100% theo quy định ban hành của dự án:
1. **Phạm vi áp dụng**:
   - Áp dụng cho các dự án mới / nâng cấp có mức độ ảnh hưởng từ Medium trở lên (Medium / High).
   - Áp dụng cho PO, User UAT, Tester, BA.
2. **Cấu trúc file**:
   - `Cover`: Thông tin chung template.
   - `Summary`: Tổng hợp kết quả và xác nhận UAT cuối cùng của PO.
   - `Report 1_Module`: Mẫu UAT khi tổ chức theo Module/Chức năng.
   - `Report 2_Process`: Mẫu UAT khi tổ chức theo Quy trình end-to-end (luồng nghiệp vụ xuyên suốt hoặc dự án ad-hoc/biz demand cần đáp ứng nhanh).
3. **Cách sử dụng & Thiết kế UAT theo Nghiệp Vụ & Hệ Thống**:
   - Thống nhất với PO chọn Report 1 hoặc Report 2.
   - Ưu tiên thiết kế case theo **nghiệp vụ & ý nghĩa hệ thống**, không chỉ theo màn hình đơn lẻ.
   - **Cross-system**: Bắt buộc phải có cả **Happy case** và **Unhappy case** (data sai, timeout, lỗi tích hợp API...) để kiểm tra toàn vẹn ràng buộc hệ thống.
   - Khi có nhiều PO theo hệ thống: PO từng hệ thống xác nhận bảng *“PO UAT Decision by System”*; Lead PO / Business Owner cập nhật *“Overall UAT Decision”*.
4. **Xác nhận & Lưu trữ**:
   - Hoàn tất UAT: PO confirm kết quả tại sheet `Summary` (khớp với latest update của sheet `Report`) và gửi email đính kèm file/link.
   - QA/PIC phụ trách lưu trữ tài liệu vào Thư mục dự án.

---

# MỤC II: BỘ KỸ NĂNG QC CHUẨN QUỐC TẾ (ISTQB & ISO/IEC/IEEE 29119)

Vận dụng kiến thức kiểm thử chuẩn mực quốc tế từ **ISTQB (International Software Testing Qualifications Board)** và **ISO/IEC/IEEE 29119**:

```
                  ┌────────────────────────────────────────┐
                  │        Agile Testing Pyramid           │
                  │                                        │
                  │               /  UAT  \   <-- Acceptance
                  │              /---------\               │
                  │             /    SIT    \  <-- Integration
                  │            /-------------\             │
                  │           /   Component   \            │
                  │          /-----------------\           │
                  │         /     Unit Test     \          │
                  └────────────────────────────────────────┘
```

### 1. Phân Biệt Các Cấp Độ Kiểm Thử & Vai Trò UAT
| Tiêu chí | SIT (System Integration Testing) | UAT (User Acceptance Testing) |
|:---|:---|:---|
| **Mục tiêu** | Tìm lỗi kỹ thuật, lỗi tích hợp API, DB, giao thức | Xác nhận hệ thống đáp ứng đúng nhu cầu nghiệp vụ thực tế của người dùng |
| **Người thực hiện** | QC / Tester chuyên trách | PO, Key Users, Business Stakeholders, End-users |
| **Tiêu chí đánh giá** | Khớp 100% với SRS/Kỹ thuật chi tiết | Khớp với Business Requirements (URD), luồng công việc thực tế, UX |
| **Môi trường** | Test / SIT Environment | Staging / Pre-Production (Dữ liệu mô phỏng thực tế) |

---

### 2. Các Kỹ Thuật Thiết Kế Kịch Bản Test (Test Design Techniques)

Tester/QC bắt buộc phải vận dụng 6 kỹ thuật chuẩn quốc tế sau khi viết Test Case:

#### 1. Phân Vùng Tương Đương (Equivalence Partitioning - EP)
- Chia tập dữ liệu đầu vào thành các nhóm hợp lệ (Valid) và không hợp lệ (Invalid).
- *Ví dụ*: Ô nhập số điện thoại FPT Telecom (10 số, đầu 03, 05, 07, 08, 09):
  - Phân vùng hợp lệ: Chuỗi 10 chữ số bắt đầu bằng đầu số viễn thông Việt Nam hợp lệ (VD: `0901234567`).
  - Phân vùng không hợp lệ: Ít hơn 10 ký tự, nhiều hơn 10 ký tự, chứa chữ/ký tự đặc biệt, đầu số không tồn tại (`01...`, `02...`).

#### 2. Phân Tích Giá Trị Biên (Boundary Value Analysis - BVA)
- Lỗi phần mềm thường xuất hiện nhiều nhất tại các điểm biên (Boundary).
- Kiểm tra các giá trị: `Min - 1`, `Min`, `Min + 1`, `Max - 1`, `Max`, `Max + 1`.
- *Ví dụ*: Số lượng gói cước F-Safe mua kèm trong đơn hàng (Từ 1 đến 5 gói):
  - Giá trị biên cần test: `0` (dưới min), `1` (min), `2` (trên min), `4` (dưới max), `5` (max), `6` (vượt max).

#### 3. Bảng Quyết Định (Decision Table Testing)
- Dùng cho các luồng nghiệp vụ phức tạp chứa nhiều điều kiện kết hợp (Business Rules đa chiều).
- *Ví dụ*: Quy tắc áp dụng khuyến mãi nâng cấp băng thông:
  - Điều kiện 1: Khách hàng hiện hữu FPT Telecom (Y/N)
  - Điều kiện 2: Trả trước từ 6 tháng trở lên (Y/N)
  - Điều kiện 3: Thuộc khu vực Hà Nội / TP.HCM (Y/N)
  - Hành động: Giảm 20% + Tặng 1 tháng + Miễn phí lắp đặt thiết bị Wi-Fi 6.

#### 4. Kiểm Thử Chuyển Đổi Trạng Thái (State Transition Testing)
- Kiểm tra vòng đời của thực thể qua từng sự kiện tác động.
- *Ví dụ vòng đời Hợp đồng/Đơn hàng*:  
  `Mới tạo (Draft)` ──(Bấm đặt hàng)──► `Chờ thanh toán (Pending Payment)` ──(Cổng thanh toán thành công)──► `Đã thanh toán (Paid)` ──(ISC kích hoạt)──► `Hoàn tất (Completed)`.
  - Phải test cả trạng thái chuyển tiếp không hợp lệ: Từ `Đã hủy (Cancelled)` không thể chuyển sang `Đã thanh toán (Paid)`.

#### 5. Kiểm Thử Kịch Bản Nghiệp Vụ (Use Case / End-to-End Business Flow)
- Đảm bảo một quy trình kinh doanh hoàn chỉnh chạy mượt mà từ đầu đến cuối:
  - Khách vào web fpt.vn ➔ Chọn gói Internet F-Game ➔ Thêm dịch vụ bán kèm F-Safe ➔ Xác thực OTP ➔ Điền địa chỉ lắp đặt ➔ Thanh toán qua VNPay QR ➔ Nhận email xác nhận & SMS hợp đồng điện tử ➔ Đơn hàng đồng bộ sang CRM & Billing FTEL.

#### 6. Dự Đoán Lỗi (Error Guessing) & Kiểm Thử Thăm Dò (Exploratory Testing)
- Dựa trên kinh nghiệm của Senior QC để bắt các lỗi tiềm ẩn:
  - Người dùng bấm nút "Thanh toán" liên tục nhiều lần (Double Click / Spam Request).
  - Mất kết nối mạng giữa chừng khi đang gọi API thanh toán.
  - Back/Forward trình duyệt hoặc F5 Refresh tại bước nhập OTP.

---

### 3. Phân Loại Happy Path, Unhappy Path & Cross-System

Mọi bộ Test Suite của dự án FPT Telecom bắt buộc phải có đầy đủ 3 nhóm ca kiểm thử:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CẤU TRÚC TEST SUITE UAT                         │
├───────────────────────────┬────────────────────────────────────────────┤
│ 1. Happy Path (60%)       │ Các luồng chuẩn thành công, dữ liệu đúng   │
├───────────────────────────┼────────────────────────────────────────────┤
│ 2. Unhappy Path (25%)     │ Dữ liệu sai, vượt biên, từ chối, hết hạn   │
├───────────────────────────┼────────────────────────────────────────────┤
│ 3. Cross-System (15%)     │ Đồng bộ CRM, Billing, ERP, Timeout, Mock   │
└───────────────────────────┴────────────────────────────────────────────┘
```

- **Happy Path**: Dữ liệu đúng chuẩn, người dùng thao tác tuần tự, giao dịch thành công.
- **Unhappy Path**:
  - Nhập sai mã OTP quá 5 lần.
  - Mã OTP hết hạn sau 5 phút.
  - Thẻ ngân hàng không đủ số dư.
  - Địa chỉ nằm ngoài vùng phủ hạ tầng FPT.
- **Cross-System Integration Cases**:
  - Web fpt.vn gọi API sang CRM tạo Lead nhưng CRM bị timeout (Xử lý retry và lưu queue ra sao?).
  - Thanh toán thành công tại Cổng thanh toán (VNPay/MoMo) nhưng IPN webhook trả lời chậm.
  - Giao dịch hoàn tiền (Refund) giữa hệ thống Billing và Cổng thanh toán.

---

### 4. Quản Lý Vòng Đời Lỗi (Defect Life Cycle & Severity)

Khi ghi nhận lỗi tại cột `DESCRIPTION` (Report), Tester/QC phải phân loại theo chuẩn:

| Mức độ (Severity) | Tên gọi | Định nghĩa & Tác động | Yêu cầu xử lý |
|:---:|:---|:---|:---|
| **S1** | **Blocker / Critical** | Hệ thống sập, treo cứng màn hình, lộ lỗ hổng bảo mật, không thể thanh toán, chặn đứng toàn bộ luồng UAT tiếp theo | Sửa ngay lập tức trong 2-4h, hoãn Go-Live |
| **S2** | **Major** | Tính năng chính bị lỗi sai logic (tính sai tiền, không gửi OTP), không có phương án tạm thời (No Workaround) | Sửa trong vòng 24h trước khi chốt UAT |
| **S3** | **Medium** | Lỗi chức năng phụ, hoặc có phương án thay thế tạm thời (Workaround) | Sửa trong đợt release tiếp theo |
| **S4** | **Minor / Trivial** | Lỗi hiển thị UI, lệch font, lỗi chính tả, căn lề chưa chuẩn | Sửa khi hoàn tất các chức năng chính |

---

# MỤC III: ỨNG DỤNG SKILL DESIGNER & NHẬN DIỆN THƯƠNG HIỆU 3 MÀU FPT

Dựa trên tiêu chuẩn Design System từ `.agent/skills/designer/design_md_CMS_VI.md`, bảng tính Excel UAT được thiết kế đạt đẳng cấp Enterprise UI, tối ưu trải nghiệm người dùng (UX) và phân cấp thị giác rõ ràng:

### 1. Bảng Màu 3 Màu Logo FPT (FPT Brand Trio)
| Màu sắc | Mã Hex | RGB | Tỷ lệ & Ý nghĩa | Ứng dụng trong Template Excel |
|:---|:---:|:---:|:---|:---|
| **FPT Blue (Xanh dương)** | `#0054A6` | (0, 84, 166) | **Chủ đạo (60%)**<br>Công nghệ, chuẩn mực, tin cậy, vững bền | Header chính các bảng tính (`NO`, `MODULE`, `STEPS`, `EXPECTED RESULT`), Khung viền Section, Mã hiệu tài liệu |
| **FPT Orange (Cam)** | `#F26522` | (242, 101, 34) | **Điểm nhấn (20%)**<br>Nhiệt huyết, sáng tạo, nổi bật | Tiêu đề lớn (`USER ACCEPTANCE TEST`, `UAT REPORT`), Nhãn số hiệu ví dụ (`VD`), Trạng thái cần chú ý |
| **FPT Green (Xanh lá)** | `#009E49` | (0, 158, 73) | **Điểm nhấn (20%)**<br>Sức sống, tăng trưởng, thành công | Header cột `ISC FEEDBACK`, Trạng thái `PASSED`, Trạng thái `DONE`, Dấu hiệu nghiệm thu thành công |

### 2. Nguyên Tắc Thiết Kế Trực Quan (Designer Principles)
1. **Phân cấp thị giác rõ ràng (Visual Hierarchy)**:
   - Cấp 1 (Title): Size 20 - 24pt Bold, màu Cam FPT `#F26522`.
   - Cấp 2 (Header bảng): Size 11 - 12pt Bold, màu Xanh dương FPT `#0054A6` với chữ trắng tương phản cao.
   - Cấp 3 (Dữ liệu hàng): Size 10 - 11pt Regular, màu xám sẫm `Slate 800` (`#1E293B`) dễ đọc, không gây chói mắt.
2. **Kỹ thuật Zebra Striping (Dòng chẵn/lẻ)**:
   - Các dòng test case xen kẽ giữa nền trắng (`#FFFFFF`) và nền xám xanh siêu nhẹ (`#F8FAFC`). Giúp mắt của Tester và PO không bị mỏi hay nhìn lệch dòng khi duyệt bảng có hàng trăm test case.
3. **Màu trạng thái Semantic (Chuẩn WCAG AA)**:
   - Không dùng màu quá chói lọi. Sử dụng kỹ thuật: **Nền màu nhạt (Soft Pastel Tint) + Chữ màu sẫm đậm (Dark Saturated Text)**:
     - `PASSED`: Nền `#D1FAE5` + Chữ `#065F46` (Xanh lục bảo)
     - `FAILED`: Nền `#FEE2E2` + Chữ `#991B1B` (Đỏ sẫm)
     - `PENDING`: Nền `#FEF3C7` + Chữ `#92400E` (Hổ phách)
     - `N/A`: Nền `#F1F5F9` + Chữ `#475569` (Xám Slate)
4. **Cố định cấu trúc & Độ rộng cột (Layout Constrained)**:
   - Tuân thủ User Rule 21: Toàn bộ bảng tính được cấu hình sẵn độ rộng cột (Column Widths), tự động bật thuộc tính xuống dòng `wrap_text=True`, không bị tràn viền màn hình khi mở trên các độ phân giải khác nhau.

---

# MỤC IV: QUY TRÌNH TRIỂN KHAI UAT STEP-BY-STEP

Quy trình 5 bước chuẩn hóa dành cho Tester, BA và PO:

```
[Bước 1: Chuẩn bị] ──► [Bước 2: Thiết kế Case] ──► [Bước 3: Chạy Round 1] ──► [Bước 4: Re-test Round 2/3] ──► [Bước 5: Ký Duyệt Sign-off]
```

### Bước 1: Chuẩn Bị & Xác Định Tiêu Chí Đầu Vào (UAT Entry Criteria)
- Đảm bảo các điều kiện tiên quyết trước khi mở UAT:
  - 100% test case SIT đã được execute và Pass.
  - 0 lỗi mức độ Blocker (S1) hoặc Critical (S2) còn tồn đọng.
  - Môi trường UAT/Staging ổn định, đã nạp đầy đủ Master Data và tài khoản test thử nghiệm.
- Điền đầy đủ thông tin tại sheet `Summary` (Project name, PO, PM, Thời gian bắt đầu).

### Bước 2: Thiết Kế Test Scenarios & Test Cases
- Thống nhất chọn dạng `Report 1_Module` hoặc `Report 2_Process`.
- BA/Tester viết kịch bản test tại sheet `Report`:
  - Cột `STEPS TO EXECUTE`: Đánh số 1, 2, 3 rõ ràng, ghi rõ dữ liệu test cần nhập.
  - Cột `EXPECTED RESULT`: Mô tả chi tiết hành vi hiển thị trên giao diện và kết quả nghiệp vụ hệ thống.
  - Đảm bảo tối thiểu 1 Happy case và 1 Unhappy case cho mỗi tính năng.

### Bước 3: Thực Hiện Kiểm Thử Vòng 1 (Execution Round 1)
- User/PO thao tác kiểm thử thực tế trên hệ thống.
- Cập nhật kết quả tại cột J-K:
  - Chọn `STATUS`: `PASSED`, `FAILED`, hoặc `PENDING`.
  - Nếu FAILED: Mô tả chi tiết tại cột `DESCRIPTION` (kèm URL ảnh chụp lỗi/log).
- Đội phát triển (ISC) theo dõi các ca FAILED, xử lý lỗi và cập nhật tại cột L-M:
  - Chọn `ACTION`: `DONE`, `DOING`, hoặc `CANCELLED`.
  - Điền `NOTE`: Giải pháp xử lý hoặc mã bản vá (commit/build).

### Bước 4: Kiểm Thử Lại (Regression Test Round 2 & 3)
- Sau khi ISC hoàn tất sửa lỗi (`ACTION` = `DONE`), Tester/PO thực hiện kiểm tra lại các ca từng bị Fail.
- Ghi nhận kết quả vào cột Round 2 (N, O, P, Q). Nếu vẫn chưa đạt, chuyển sang Round 3 (R, S, T, U).

### Bước 5: Đánh Giá Tiêu Chí Kết Thúc & Nghiệm Thu (UAT Exit Criteria & Sign-off)
- Điều kiện nghiệm thu thành công:
  - 100% Happy Path Pass.
  - 0 lỗi S1/S2 chưa giải quyết.
  - Các lỗi Minor còn lại được PO đồng ý chấp thuận dời sang đợt bảo trì tiếp theo.
- PO ký xác nhận nghiệm thu tại sheet `Summary` và thông báo qua Email chính thức kèm file/link UAT.

---

# MỤC V: HƯỚNG DẪN TỰ ĐỘNG SINH & QUẢN LÝ TEMPLATE EXCEL

Skill này tích hợp sẵn bộ script Python tự động hóa hoàn toàn việc tạo file Excel UAT chuẩn FPT.

### 1. Cấu Trúc Thư Mục Skill
```
.agent/skills/Tester-QC/
├── SKILL.md                                 # Tài liệu định nghĩa toàn diện kỹ năng Tester-QC
├── templates/
│   ├── uat_template_raw.xlsx                # File gốc nguyên bản từ Google Sheets dự án
│   └── uat_template_fpt_standard.xlsx       # File chuẩn hóa 3 màu FPT + công thức + validation
└── scripts/
    └── generate_uat_template.py             # Script Python sinh file Excel chuẩn tự động
```

### 2. Lệnh Tự Động Sinh File Excel Mẫu Mới
Bất cứ khi nào bắt đầu một dự án mới hoặc cần một file UAT trắng chuẩn mực, chỉ cần chạy lệnh sau từ Terminal:

```bash
python3 .agent/skills/Tester-QC/scripts/generate_uat_template.py [đường_dẫn_file_ra.xlsx]
```

*Ví dụ tạo file UAT cho dự án FPT.VN Nâng Cấp:*
```bash
python3 .agent/skills/Tester-QC/scripts/generate_uat_template.py docs/UAT_FPT_VN_NangCap.xlsx
```

Script sẽ tự động:
1. Tạo đầy đủ 4 sheet (`Cover`, `Summary`, `Report`, `Guideline`).
2. Định dạng font `Times New Roman` và phối màu chuẩn 3 màu FPT (Xanh dương, Cam, Xanh lá).
3. Thiết lập sẵn công thức thống kê tự động `=SUM(...)` và `=COUNTIF(...)`.
4. Cài đặt sẵn Dropdown Data Validation cho cột `STATUS` và `ACTION`.
5. Thiết lập Conditional Formatting tự động highlight màu khi người dùng chọn kết quả test.

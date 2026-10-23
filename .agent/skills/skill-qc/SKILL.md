---
name: skill-qc
description: Chuyên gia kiểm thử phần mềm (Tester/QC) và Quản lý nghiệm thu người dùng (UAT) chuẩn quốc tế ISTQB & FPT Telecom. Hỗ trợ thiết kế kịch bản test (Test Scenarios/Test Cases), phân tích ca kiểm thử Happy/Unhappy/Cross-system, vận hành quy trình UAT nhiều vòng (Round 1, 2, 3), phân loại lỗi (Defect/Severity), tích hợp bộ 14 kỹ năng QE-AI nâng cao (Automation, E2E, Bug/Log Analysis, Test Data, Seed Data, Visual Sweep, Quality Audit), và tự động tạo/xuất Template UAT Excel chuẩn nhận diện 3 màu FPT (Xanh dương, Cam, Xanh lá).
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
6. [Mục VI: Ma Trận 14 Kỹ Năng QE-AI Chuyên Sâu (QE-AI Skills Matrix)](#mục-vi-ma-trận-14-kỹ-năng-qe-ai-chuyên-sâu)

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
├── scripts/
│   └── generate_uat_template.py             # Script Python sinh file Excel chuẩn tự động
└── skills/                               # 14 Kỹ năng QE-AI chuyên sâu tích hợp từ repo QE-AI
    ├── analyzing-bugs-and-logs/
    ├── auditing-test-quality/
    ├── building-test-tools-with-api/
    ├── capturing-ui-sweep/
    ├── coaching-qe-learners/
    ├── designing-test-strategy/
    ├── generating-test-cases/
    ├── generating-test-data/
    ├── managing-seed-data/
    ├── planning-e2e-coverage/
    ├── prompting-for-qe/
    ├── writing-automation-tests/
    ├── writing-e2e-tests/
    └── writing-skills/
```


### 3. Kho Kịch Bản Kiểm Thử & Nghiệp Vụ Thực Tế FPT (Trong thư mục skills_qc/)
Toàn bộ kịch bản test case và nghiệp vụ kiểm thử của dự án FPT-1 đã được đưa về tập trung tại :
- **[Cẩm nang Master Test Cases FPT](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/FPT_TEST_CASES_MASTER_BOOK.md)**: Tra cứu nhanh toàn bộ test case & business rule 4 phân hệ.
- **[Kịch bản Camera Play 4 & Charm](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/fpt-scenarios-camera-charm/Kich_Ban_Ky_Thuat_Play4_Charm.xlsx)**: 40+ kịch bản test mua kèm tỷ lệ 1:1, tách dòng, best-deal.
- **[Kịch bản Internet & Truyền hình Combo](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/fpt-scenarios-internet-combo/Kich_Ban_Test_Internet_Combo.md)**: Các test cases ngoại lệ (Hết port, drop-off, đổi địa chỉ).
- **[Kịch bản Mua Bán Thiết Bị](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/fpt-scenarios-thiet-bi/Kich_Ban_Test_Thiet_Bi.md)**: Giới hạn giỏ hàng, hết tồn kho, phí vận chuyển.
- **[Kịch bản Dịch Vụ Số Standalone](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/fpt-scenarios-dich-vu-so-sa/Kich_Ban_Test_Dich_Vu_So_SA.md)**: Validate SĐT ngầm, tài khoản FPT Play hiện hữu, OTP retry.
- **[Script chuẩn hóa kịch bản](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/fpt-test-scripts/update_kich_ban_chuan_biz.py)**: Script tự động validate và cập nhật kịch bản test.

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

---

# MỤC VI: MA TRẬN 14 KỸ NĂNG QE-AI CHUYÊN SÂU

Bộ 14 kỹ năng QE-AI cao cấp được kế thừa từ repository chuẩn [QE-AI](https://github.com/huyphan13189/QE-AI/tree/main/.claude/skills) và được tổ chức nằm ngay trong thư mục `skills/` của `Tester-QC`. Bộ kỹ năng này hỗ trợ đắc lực cho Tester/QC và PO trong mọi công đoạn từ thiết kế, sinh test case, tự động hóa, phân tích log lỗi đến nghiệm thu:

```
                               ┌────────────────────────────────────────────────┐
                               │           HỆ THỐNG NĂNG LỰC QE-AI              │
                               └──────────────────────┬─────────────────────────┘
                                                      │
         ┌───────────────────┬────────────────────────┼────────────────────────┬───────────────────┐
         ▼                   ▼                        ▼                        ▼                   ▼
┌─────────────────┐ ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐ ┌─────────────────┐
│  1. CHIẾN LƯỢC  │ │ 2. SINH CASE    │      │ 3. TEST TỰ ĐỘNG │      │ 4. PHÂN TÍCH    │ │ 5. CÔNG CỤ &    │
│  & HOẠCH ĐỊNH   │ │ & DỮ LIỆU TEST  │      │ & VISUAL SWEEP  │      │ LỖI & AUDIT     │ │ ĐÀO TẠO QE      │
├─────────────────┤ ├─────────────────┤      ├─────────────────┤      ├─────────────────┤ ├─────────────────┤
│• test-strategy  │ │• gen-test-cases │      │• write-auto-test│      │• bug-and-log    │ │• prompting-qe   │
│• e2e-coverage   │ │• gen-test-data  │      │• write-e2e-tests│      │• audit-quality  │ │• build-test-tool│
│                 │ │• seed-data      │      │• ui-sweep       │      │                 │ │• coach-learners │
│                 │ │                 │      │                 │      │                 │ │• write-skills│
└─────────────────┘ └─────────────────┘      └─────────────────┘      └─────────────────┘ └─────────────────┘
```

---

### TRỤ CỘT 1: CHIẾN LƯỢC & HOẠCH ĐỊNH KIỂM THỬ (STRATEGY & PLANNING)

#### 1. [`designing-test-strategy`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/designing-test-strategy/SKILL.md) — Hoạch Định Chiến Lược Kiểm Thử
- **Mục đích**: Lập chiến lược kiểm thử cho một tính năng lớn, Epic hoặc đợt phát hành mới; xây dựng **Test Charter** cho các buổi kiểm thử thăm dò (Exploratory Testing Session); xác định ma trận ưu tiên: *Những gì bắt buộc phải test sâu, những gì chỉ cần smoke test, và những gì có thể bỏ qua*.
- **Cách áp dụng trong UAT FPT**:
  - Dùng khi bắt đầu dự án mới hoặc tính năng lớn (Impact High/Medium) để xác định rõ phạm vi cần đưa vào UAT.
  - Ngăn ngừa tình trạng: *"Viết dàn trải hàng trăm test case vụn vặt nhưng bỏ sót các rủi ro chết người liên quan đến tiền bạc, thanh toán và dữ liệu hợp đồng"*.

#### 2. [`planning-e2e-coverage`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/planning-e2e-coverage/SKILL.md) — Hoạch Định Độ Bao Phủ End-to-End
- **Mục đích**: Quyết định hệ thống cần bao nhiêu ca kiểm thử E2E; phân tầng độ bao phủ (Tier 1: High/P0 - Golden Journeys; Tier 2: Medium/P1 - Branching Journeys; Tier 3: Low/P2 - Edge Cases); đánh giá độ bao phủ thực tế của bộ test hiện có so với toàn bộ luồng nghiệp vụ.
- **Cách áp dụng trong UAT FPT**:
  - Lập bản đồ các luồng mua hàng và thanh toán trên fpt.vn (Ví dụ: Mua mới Internet, Nâng cấp băng thông, Mua kèm F-Safe/Camera).
  - Đảm bảo 100% Golden Path của FPT có mặt trong danh sách UAT trước khi chốt lịch kiểm thử với PO.

---

### TRỤ CỘT 2: SINH KỊCH BẢN & QUẢN TRỊ DỮ LIỆU KIỂM THỬ (TEST GENERATION & DATA)

#### 3. [`generating-test-cases`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/generating-test-cases/SKILL.md) — Sinh Test Case Chuẩn Xác Bằng AI
- **Mục đích**: Biến tài liệu yêu cầu (URD, PRD, User Story, Acceptance Criteria, API Specs) thành bộ kịch bản test case chuẩn mực với sự trợ giúp của AI.
- **Cách áp dụng trong UAT FPT**:
  - Sinh trực tiếp các dòng test case để điền vào sheet `Report` theo đúng chuẩn cột: `NO.`, `MODULE`, `STEPS TO EXECUTE`, `EXPECTED RESULT`.
  - Ép cấu trúc sinh đầy đủ 3 nhóm: Happy path, Unhappy path (biên, lỗi người dùng) và Cross-system integration (gọi CRM, Billing, Gateway).
  - Tránh bẫy AI ảo giác: Mọi bước kiểm thử đều bám sát đúng quy tắc nghiệp vụ (BR) của dự án.

#### 4. [`generating-test-data`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/generating-test-data/SKILL.md) — Sinh Dữ Liệu Kiểm Thử Đa Dạng
- **Mục đích**: Sinh dữ liệu test giả lập có tính đại diện cao (Synthetic test data) cho UI, API, DB tests, bulk load datasets.
- **Cách áp dụng trong UAT FPT**:
  - Sinh danh sách số điện thoại viễn thông Việt Nam hợp lệ (đầu 03, 05, 07, 08, 09) và không hợp lệ.
  - Sinh số CCCD/CMND chuẩn 12 số, email, địa chỉ lắp đặt theo 63 tỉnh thành Việt Nam.
  - Sinh dữ liệu ký tự Unicode tiếng Việt có dấu, khoảng trắng thừa, chuỗi XSS/SQL Injection để kiểm tra tính bảo mật của form nhập liệu fpt.vn.

#### 5. [`managing-seed-data`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/managing-seed-data/SKILL.md) — Quản Trị Dữ Liệu Khởi Tạo (Seed Data) Idempotent
- **Mục đích**: Quản lý thư viện fixture/seed data cục bộ dùng chung cho môi trường dev và E2E; đảm bảo nguyên tắc **Idempotency** (chạy lại nhiều lần không sinh rác dữ liệu, không làm phình bảng dữ liệu, không trùng lặp khóa chính).
- **Cách áp dụng trong UAT FPT**:
  - Tạo sẵn các gói cước Internet (Giga, Sky, Meta, F-Game), các dịch vụ gia tăng (F-Safe, FPT Play, Cloud Camera) trên môi trường Staging/UAT để mọi vòng test (Round 1, 2, 3) đều có dữ liệu chuẩn sẵn sàng mà không cần nhập tay lại từ đầu.

---

### TRỤ CỘT 3: KIỂM THỬ TỰ ĐỘNG & VISUAL QA (AUTOMATION & VISUAL SWEEP)

#### 6. [`writing-automation-tests`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/writing-automation-tests/SKILL.md) — Viết Kịch Bản Test Tự Động (API & UI)
- **Mục đích**: Xây dựng bộ khung test tự động (Playwright, Cypress, Postman, Jest), chuyển đổi test case thủ công (Manual) thành kịch bản tự động hóa; kiểm thử API endpoints và hợp đồng dữ liệu.
- **Cách áp dụng trong UAT FPT**:
  - Tự động hóa các API cốt lõi: API gửi SMS OTP, API xác thực số điện thoại, API tính cước khuyến mãi, API tạo Lead sang CRM.
  - Chạy regression tự động trước mỗi vòng UAT để phát hiện sớm các lỗi kỹ thuật trước khi bàn giao cho PO kiểm thử chấp nhận.

#### 7. [`writing-e2e-tests`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/writing-e2e-tests/SKILL.md) — Viết Kịch Bản Kiểm Thử E2E Trực Thực
- **Mục đích**: Viết các kịch bản End-to-End điều khiển trình duyệt thật (Real Browser) tương tác với backend và cơ sở dữ liệu thật; xử lý cơ chế bypass authentication, deep-link, xử lý triệt để bài toán **Flaky Test** (test lúc pass lúc fail do mạng hoặc timing).
- **Cách áp dụng trong UAT FPT**:
  - Xây dựng kịch bản Golden Path E2E: Từ trang chủ fpt.vn ➔ Chọn gói cước ➔ Thêm dịch vụ bán kèm ➔ Nhập OTP ➔ Điền địa chỉ ➔ Thanh toán qua cổng thanh toán Sandbox ➔ Xác nhận đơn hàng thành công trên hệ thống.

#### 8. [`capturing-ui-sweep`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/capturing-ui-sweep/SKILL.md) — Quét & Kiểm Tra Giao Diện Toàn Diện (Visual QA Sweep)
- **Mục đích**: Tự động chụp ảnh toàn bộ các màn hình của ứng dụng theo nhóm tính năng; sử dụng AI để quét và phát hiện các lỗi thị giác: vỡ layout, lệch hàng, tràn khung, text bị cắt xén, ảnh broken, empty-state xấu xí, sai lệch so với Design System.
- **Cách áp dụng trong UAT FPT**:
  - Chụp toàn bộ luồng mua hàng và đăng ký dịch vụ trên cả 2 phiên bản Desktop và Mobile.
  - Đối chiếu với tiêu chuẩn Design System FPT (3 màu nhận diện, font Times New Roman, khoảng cách padding, độ tương phản WCAG AA) trước khi trình PO nghiệm thu giao diện.

---

### TRỤ CỘT 4: PHÂN TÍCH LỖI, NHẬT KÝ & THẨM ĐỊNH CHẤT LƯỢNG (DEFECT ANALYSIS & AUDIT)

#### 9. [`analyzing-bugs-and-logs`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/analyzing-bugs-and-logs/SKILL.md) — Phân Tích Lỗi, Stack Trace & Nhật Ký Hệ Thống
- **Mục đích**: Đọc và phân tích error logs, stack trace, mã lỗi 500/502/504; truy vết nguyên nhân gốc rễ (Root Cause Analysis - RCA); xác định chính xác file, hàm và điều kiện gây lỗi; viết Bug Report chuẩn mực có đầy đủ bước tái hiện (Reproduction Steps) và bằng chứng (Evidence).
- **Cách áp dụng trong UAT FPT**:
  - Khi một test case bị `FAILED` tại cột `STATUS` (Sheet `Report`), kỹ năng này giúp Tester không chỉ ghi nhận *"Tính năng bị lỗi"* mà cung cấp chính xác: *"API `/api/v1/otp/verify` trả về 500 do NullPointerException tại hàm validatePhonePrefix với đầu số 05"*.
  - Giúp đội phát triển (ISC) nắm bắt ngay nguyên nhân và cập nhật cột `ACTION` = `DONE` nhanh chóng.

#### 10. [`auditing-test-quality`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/auditing-test-quality/SKILL.md) — Thẩm Định Chất Lượng Bộ Test
- **Mục đích**: Đánh giá và kiểm toán chất lượng thực chất của một bộ test suite; vạch trần các ca test vô nghĩa (*Assertionless tests* - test chạy xanh lè nhưng không assert kết quả thực tế); phát hiện các lỗ hổng logic kiểm thử còn thiếu sót.
- **Cách áp dụng trong UAT FPT**:
  - Kiểm toán lại toàn bộ sheet `Report` trước khi gửi cho PO: Đảm bảo không có dòng test case nào ghi chung chung kiểu *"Kiểm tra màn hình hoạt động bình thường"*, mà phải có điều kiện kiểm tra rõ ràng, có số liệu cụ thể.

---

### TRỤ CỘT 5: CÔNG CỤ AI, PROMPTING & ĐÀO TẠO QE (AI TOOLING & COACHING)

#### 11. [`prompting-for-qe`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/prompting-for-qe/SKILL.md) — Kỹ Thuật Viết Prompt Chuyên Biệt Cho QE/Tester
- **Mục đích**: Kỹ thuật xây dựng câu lệnh (Prompt Construction) chuẩn xác dành riêng cho các tác vụ kiểm thử phần mềm; chống lan man, chống bịa đặt dữ liệu, ép đầu ra theo bảng biểu có cấu trúc.
- **Cách áp dụng trong UAT FPT**:
  - Dùng để tương tác với AI khi cần phân tích URD phức tạp và chuyển đổi thành bảng test case FPT: Cung cấp đầy đủ Role, Context, Constraints, Few-shot Examples và Output Format chuẩn Sheet `Report`.

#### 12. [`building-test-tools-with-api`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/building-test-tools-with-api/SKILL.md) — Xây Dựng Công Cụ Kiểm Thử Tự Động Hóa Với API
- **Mục đích**: Viết các script tự động hóa gọi API mô hình ngôn ngữ lớn (LLM API) từ mã nguồn để tự động phân tích tài liệu yêu cầu, sinh checklist kiểm thử hoặc triage logs số lượng lớn trong CI/CD pipeline.
- **Cách áp dụng trong UAT FPT**:
  - Kết hợp với script `generate_uat_template.py` để tạo tool đọc file URD `.doc` trong thư mục `thuyttdoc/` và tự động điền sẵn các kịch bản test vào file Excel UAT Template chuẩn FPT.

#### 13. [`coaching-qe-learners`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/coaching-qe-learners/SKILL.md) — Đào Tạo & Nâng Cao Năng Lực Đội Ngũ Tester/QC
- **Mục đích**: Huấn luyện đội ngũ theo lộ trình đào tạo chuẩn; thực hiện phỏng vấn thử (Mock Interview) đánh giá năng lực theo từng cấp bậc (Level Gate); chấm bài dựa trên bằng chứng thực tế theo nguyên tắc nghiêm ngặt: *"Luật không làm hộ"*.
- **Cách áp dụng trong UAT FPT**:
  - Đào tạo nội bộ cho Tester mới tham gia dự án FPT: Nắm vững quy trình UAT, cách dùng template, cách log bug và văn hóa phối hợp giữa PO - BA - Tester - Dev.

#### 14. [`writing-skills`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/Tester-QC/skills_qc/writing-skills/SKILL.md) — Đóng Gói & Chuẩn Hóa Kỹ Năng Mới
- **Mục đích**: Quy trình chuẩn hóa và đóng gói một kỹ thuật kiểm thử thực tế lặp đi lặp lại thành một skill có thể tái sử dụng cho toàn bộ tổ chức hoặc dự án.
- **Cách áp dụng trong UAT FPT**:
  - Khi phát sinh một quy trình kiểm thử mới (ví dụ: Quy trình UAT thanh toán sinh trắc học FacePay FPT), kỹ năng này giúp đóng gói thành module chuẩn mực đưa vào bộ kỹ năng dùng chung.

---

## TỔNG KẾT BẢNG ÁNH XẠ NHIỆM VỤ THỰC TẾ

| Nhiệm vụ thực tế của Tester / PO | Kỹ năng QE-AI được triệu hồi | Sản phẩm đầu ra |
|:---|:---|:---|
| **Lập kế hoạch UAT cho đợt release mới** | `designing-test-strategy`<br>`planning-e2e-coverage` | Test Charter, Ma trận phạm vi UAT |
| **Sinh kịch bản test từ URD/User Story** | `generating-test-cases`<br>`prompting-for-qe` | Danh sách test case điền vào Sheet `Report` |
| **Chuẩn bị dữ liệu tài khoản, gói cước test** | `generating-test-data`<br>`managing-seed-data` | Tập dữ liệu kiểm thử (Số ĐT, CCCD, Gói cước) |
| **Chạy kiểm tra giao diện trước đợt UAT** | `capturing-ui-sweep` | Báo cáo kiểm tra Visual layout & Design system |
| **Phát hiện lỗi 500, lỗi API trong lúc UAT** | `analyzing-bugs-and-logs` | Bug report chuẩn có stack trace và file/hàm lỗi |
| **Rà soát lại bộ test case trước khi trình PO** | `auditing-test-quality` | Báo cáo thẩm định chất lượng bộ test |
| **Xuất file Excel UAT Template chuẩn FPT** | `generate_uat_template.py` | File `.xlsx` chuẩn 4 sheet, 3 màu FPT, công thức tự động |
| **Chạy kiểm thử hồi quy tự động** | `writing-automation-tests`<br>`writing-e2e-tests` | Bộ kịch bản E2E Playwright/Cypress tự động |

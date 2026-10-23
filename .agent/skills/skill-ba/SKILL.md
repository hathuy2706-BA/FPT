---
name: skill-ba
description: Bộ kỹ năng toàn diện dành cho Business Analyst (BA) chuyên nghiệp tại FPT Telecom. Hợp nhất các năng lực cốt lõi: Khám phá & Đặc tả yêu cầu (URD/SRS/BRD), Viết User Story & Acceptance Criteria chuẩn INVEST/Gherkin, Thiết kế sơ đồ luồng nghiệp vụ chuẩn nền trắng (Flowchart, BPMN, Sequence), và Xuất sơ đồ sang Figma board (figma-bpmn-exporter).
---

# BỘ KỸ NĂNG BUSINESS ANALYST (SKILL-BA)

> **Mã hiệu vai trò**: `BA-CORE-FTEL`  
> **Dự án**: Hệ sinh thái FPT Telecom (fpt.vn, CRM, Billing, Customer Portal)  
> **Font chuẩn tài liệu**: `Times New Roman` (Tiêu chuẩn hành chính FPT)  
> **Bộ nhận diện chuẩn**: 3 màu logo FPT (Xanh dương `#0054A6` · Cam `#F26522` · Xanh lá `#009E49`)

---

## 1. CẤU TRÚC PHÂN LOẠI NĂNG LỰC TRONG `skill-ba`

Toàn bộ các kỹ năng nghiệp vụ BA được gom tập trung và phân loại ngăn nắp tại thư mục này:

```
skill-ba/
├── SKILL.md                          # Tài liệu cổng điều phối toàn diện vai trò BA
├── ba-senior/                        # Kỹ năng BA Senior: Khám phá bài toán, URD, SRS, giải pháp
│   ├── SKILL.md
│   ├── templates/                    # Mẫu URD, US template, PRD template
│   └── skillfow/
├── user-story-ac-writer/             # Viết User Story chuẩn INVEST & AC chuẩn Gherkin Given-When-Then
│   ├── SKILL.md
│   ├── templates/
│   └── _ checklists/
├── diagram-drawer/                   # Vẽ sơ đồ luồng Flowchart, BPMN, Sequence diagram chuẩn nền trắng
│   ├── SKILL.md
│   └── templates/
├── figma-bpmn-exporter/              # Xuất sơ đồ BPMN từ SVG sang vector native trên Figma board
│   ├── SKILL.md
│   ├── plugin/
│   └── scripts/
```

---

## 2. BẢN ĐỒ KỸ NĂNG & QUY TRÌNH BA STEP-BY-STEP

```
[1. Khám Phá & Phỏng Vấn] ──► [2. Viết URD/SRS] ──► [3. Vẽ Sơ Đồ BPMN/Flow] ──► [4. Viết User Story & AC] ──► [5. Xuất Sơ Đồ Figma]
        (ba-senior)               (ba-senior)            (diagram-drawer)           (user-story-ac-writer)        (figma-bpmn-exporter)
```

### Bước 1: Khám Phá Bài Toán & Đặc Tả Nghiệp Vụ (`ba-senior`)
- **Tài liệu hướng dẫn**: [`ba-senior/SKILL.md`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-ba/ba-senior/SKILL.md)
- **Nội dung thực thi**:
  - Khám phá vấn đề kinh doanh thực sự (Root Cause), không chỉ nghe theo yêu cầu bề nổi.
  - Viết tài liệu URD (User Requirements Document) chuẩn hành chính FPT:
    - Bìa chuẩn logo FPT Telecom dạng base64 `docs/images/logoftel.png`.
    - Đánh số quy tắc nghiệp vụ: Bắt đầu mỗi phân hệ/tính năng mới là reset từ `BR-01`, `BR-02` (Tuân thủ User Rule 23).
    - Toàn bộ nội dung sử dụng font `Times New Roman` (Tiêu đề 1 size 16 Bold, Tiêu đề 2 size 15 Bold, Tiêu đề 3 size 14 Bold, Nội dung size 13 Regular) theo User Rule 19.
    - Cố định bảng và mục lục trong sườn tài liệu, không tràn viền (User Rule 21).

### Bước 2: Thiết Kế Sơ Đồ Nghiệp Vụ (`diagram-drawer`)
- **Tài liệu hướng dẫn**: [`diagram-drawer/SKILL.md`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-ba/diagram-drawer/SKILL.md)
- **Quy chuẩn bắt buộc (User Rule 16)**:
  - Tất cả các sơ đồ (Flowchart, BPMN 2.0, Sequence Diagram, State Machine) **bắt buộc phải sử dụng nền trắng (White background)**.
  - Phân định rõ các Swimlane (Khách hàng, Frontend fpt.vn, Backend API, CRM, Billing, Cổng thanh toán).

### Bước 3: Xuất Sơ Đồ Lên Figma Board (`figma-bpmn-exporter`)
- **Tài liệu hướng dẫn**: [`figma-bpmn-exporter/SKILL.md`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-ba/figma-bpmn-exporter/SKILL.md)
- **Nội dung thực thi**:
  - Chạy script: `python3 .agent/skills/skill-ba/figma-bpmn-exporter/scripts/build_plugin.py`
  - Load plugin vào Figma Desktop để chuyển đổi file SVG thành vector native editable trực tiếp trên Figma board của dự án.

### Bước 4: Viết User Story & Acceptance Criteria (`user-story-ac-writer`)
- **Tài liệu hướng dẫn**: [`user-story-ac-writer/SKILL.md`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-ba/user-story-ac-writer/SKILL.md)
- **Quy chuẩn bắt buộc**:
  - Đảm bảo 6 tiêu chí **INVEST**: Independent (Độc lập), Negotiable (Có thể thương lượng), Valuable (Có giá trị), Estimable (Ước lượng được), Small (Vừa vặn trong sprint), Testable (Kiểm thử được).
  - Format Acceptance Criteria theo cú pháp Gherkin: `Given - When - Then` rõ ràng, có đầy đủ Happy Path, Edge Cases và Error Handling.

---

## 3. BẢNG TRA CỨU TÀI LIỆU & TEMPLATES DÙNG CHUNG CỦA BA
- **Template URD mẫu**: `skill-ba/ba-senior/templates/urd-template.md`
- **Template User Story**: `skill-ba/ba-senior/templates/templateus.doc`
- **Template PRD chuẩn**: `skill-ba/ba-senior/templates/prd_new.docx`

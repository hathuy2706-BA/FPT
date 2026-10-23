---
name: skill-designer
description: Bộ kỹ năng toàn diện dành cho UI/UX Designer tại FPT Telecom. Hợp nhất các chuẩn mực thiết kế giao diện doanh nghiệp (Enterprise SaaS & E-Commerce): Untitled UI PRO VARIABLES (v5.0), Bộ nhận diện thương hiệu 3 màu FPT (Xanh dương, Cam, Xanh lá), Hệ thống Design Tokens, Typography Times New Roman & Inter, Responsive Grid 1920px/Desktop/Mobile, và Chuẩn tiếp cận WCAG AA.
---

# BỘ KỸ NĂNG UI/UX DESIGNER (SKILL-DESIGNER)

> **Mã hiệu vai trò**: `DESIGN-CORE-FTEL`  
> **Dự án**: FPT.VN E-Commerce & Customer Journey Design System  
> **Hệ thống màu chủ đạo**: 3 màu nhận diện thương hiệu Logo FPT (Xanh dương `#0054A6` · Cam `#F26522` · Xanh lá `#009E49`)

---

## 1. CẤU TRÚC THƯ MỤC TRONG `skill-designer`

```
skill-designer/
├── SKILL.md                          # Tài liệu cổng điều phối vai trò UI/UX Designer
└── core-designer/                    # Tài liệu đặc tả Design System chuẩn hóa tiếng Việt
    └── design_md_CMS_VI.md           # Hướng dẫn chi tiết Untitled UI PRO VARIABLES (v5.0)
```

---

## 2. NGUYÊN TẮC THIẾT KẾ & BỘ NHẬN DIỆN THƯƠNG HIỆU FPT

### A. Triết Lý Thiết Kế Cốt Lõi
1. **Clarity First (Rõ Ràng Là Số 1)**: Giao diện phải truyền tải thứ bậc thông tin (Visual Hierarchy) ngay tức thì. Không để người dùng phải đoán.
2. **Scalable Systems (Khả Năng Mở Rộng)**: Mọi thuộc tính màu sắc, khoảng cách, bo góc đều phải được chuẩn hóa thành **Design Tokens** và có thể tái sử dụng.
3. **Accessibility by Default (Dễ Tiếp Cận Chuẩn WCAG AA)**: Độ tương phản an toàn, typography rõ ràng, không gây mỏi mắt.
4. **Minimal but Expressive (Tối Giản Nhưng Đậm Nét)**: Dùng khoảng trắng (Whitespace) tinh tế, điểm nhấn màu sắc có chủ đích.

### B. Bảng Màu 3 Màu Logo FPT (FPT Brand Trio)
- **FPT Blue (Xanh dương - `#0054A6`)**: Chiếm 60% diện tích Header. Đại diện cho công nghệ, độ tin cậy và chuẩn mực kỹ thuật.
- **FPT Orange (Cam - `#F26522`)**: Chiếm 20% điểm nhấn thị giác. Đại diện cho năng động, nhiệt huyết và sáng tạo.
- **FPT Green (Xanh lá - `#009E49`)**: Chiếm 20% điểm nhấn thành công. Đại diện cho tăng trưởng, phản hồi tích cực và hoàn tất thành công.

### C. Quy Chuẩn Typography & Spacing
- **Typography**: 
  - Tài liệu hành chính / URD / Báo cáo: Sử dụng font `Times New Roman` (User Rule 19).
  - Ứng dụng Web / Dashboard: Sử dụng font `Inter`.
- **Spacing System**: Hệ thống khoảng cách bội số 4px / 8px:
  - 4px (Spacing 1), 8px (Spacing 2), 12px (Spacing 3), 16px (Spacing 4), 24px (Spacing 6), 32px (Spacing 8), 48px (Spacing 12).
- **Radius System**:
  - Buttons: `radius-md` (8px)
  - Cards / Panels: `radius-lg` (12px)
  - Modals: `radius-xl` (16px)
  - Pills / Status Badges: `radius-full` (9999px)

---

## 3. TÀI LIỆU CHI TIẾT THAM KHẢO
- Xem tài liệu đặc tả đầy đủ các Components (Buttons, Inputs, Badges, Tables, Cards, Modals, Responsive Strategy 1920px) tại: [`core-designer/design_md_CMS_VI.md`](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-designer/core-designer/design_md_CMS_VI.md).

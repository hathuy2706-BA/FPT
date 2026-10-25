---
name: skill-po
description: Bộ kỹ năng toàn diện dành cho Product Owner (PO) chuyên nghiệp tại FPT Telecom. Hợp nhất các năng lực cốt lõi: Định hình Tầm nhìn Sản phẩm (Product Vision & Strategy), Quản trị & Ưu tiên Product Backlog (Value-driven Prioritization), Thiết kế Product Roadmap Pixel-Perfect & Luồng Đồng Bộ Tự Động Data (Roadmap & Realtime Sync Engine), Định nghĩa Tiêu chí Chấp nhận Kinh doanh, và Ký duyệt Nghiệm thu Chấp thuận Người dùng (Overall UAT Decision).
---

# BỘ KỸ NĂNG PRODUCT OWNER (SKILL-PO)

> **Mã hiệu vai trò**: `PO-CORE-FTEL`  
> **Dự án**: FPT.VN & Hệ sinh thái số FPT Telecom  
> **Vai trò**: Đại diện tiếng nói kinh doanh và người dùng, tối đa hóa giá trị sản phẩm

---

## 1. CẤU TRÚC THƯ MỤC TRONG `skill-po`

```
skill-po/
├── SKILL.md                          # Tài liệu cổng điều phối vai trò PO
├── core-po/                          # Kỹ năng Product Owner cốt lõi (Chiến lược, Backlog, Prioritization)
│   └── SKILL.md
└── roadmap/                          # Kỹ năng chuyên sâu: Thiết kế Roadmap Pixel-Perfect & Luồng Đồng Bộ Realtime
    ├── SKILL.md
    ├── scripts/                      # Script Google Apps Script mẫu chuẩn
    ├── templates/                    # Đặc tả kỹ thuật Google Sheets (12 cột, 1.740px)
    └── references/                   # Bảng ma trận 8 mốc trạng thái & màu sắc
```

---

### ⚠️ QUY CHUẨN LƯU TRỮ HÌNH ẢNH NGHIỆP VỤ PO
- **Thư mục lưu trữ duy nhất**: Toàn bộ hình ảnh, biểu đồ liên quan đến nghiệp vụ PO (Roadmap, Backlog Chart, Milestone, Release Timeline) sau này khi tạo mới **BẮT BUỘC PHẢI LƯU VÀO THƯ MỤC `docs/images/po/`**.
- Không lưu ảnh rải rác ngoài thư mục gốc hay thư mục khác.

## 2. NĂNG LỰC CỐT LÕI CỦA PRODUCT OWNER FPT

### A. Tầm Nhìn Sản Phẩm & Chiến Lược Kinh Doanh (Product Vision)
- Định nghĩa rõ mục tiêu sản phẩm, chân dung khách hàng mục tiêu (Target Persona), bài toán kinh doanh cần giải quyết.
- Thiết lập hệ thống chỉ số thành công (KPIs / OKRs): Tỷ lệ chuyển đổi đơn hàng (Conversion Rate), Giá trị đơn hàng trung bình (AOV), Thời gian hoàn tất mua hàng (Drop-off rate).

### B. Ưu Tiên Hóa Backlog Theo Giá Trị (Value-Driven Prioritization)
- Áp dụng các ma trận ưu tiên chuẩn quốc tế:
  - **MoSCoW**: Must have (bắt buộc), Should have (nên có), Could have (có thể có), Won't have (chưa làm).
  - **RICE Score**: Reach (Độ phủ) × Impact (Tác động) × Confidence (Độ tin cậy) / Effort (Công sức).
  - **WSJF (Weighted Shortest Job First)**: Ưu tiên tính năng mang lại giá trị nhanh nhất với chi phí trì hoãn cao nhất.

### C. Quản Trị Roadmap & Điều Phối Release
- Lập lộ trình phát triển sản phẩm theo quý/năm (Quarterly Product Roadmap).
- Phân tách phạm vi MVP (Minimum Viable Product) để Go-Live nhanh chóng theo từng giai đoạn, đáp ứng các chiến dịch kinh doanh ad-hoc / biz demand.

### D. Ký Duyệt & Nghiệm Thu Sản Phẩm (UAT Sign-off)
- Phối hợp chặt chẽ với team Tester/QC trong các đợt UAT:
  - Xác nhận điều kiện mở UAT (Entry Criteria).
  - Xác nhận kết quả kiểm thử tại Sheet `Summary` của Template UAT FPT.
  - Phê duyệt bảng *“PO UAT Decision by System”* cho từng phân hệ và ký chốt *“Overall UAT Decision”* để phát hành sản phẩm.

### E. Thiết Kế Product Roadmap & Luồng Đồng Bộ Tự Động Data (Roadmap & Sync Engine)
- Chi tiết quy chuẩn và mã nguồn xem tại module: [skill-po/roadmap](file:///Users/hathuy/Documents/FPT-1/.agent/skills/skill-po/roadmap/SKILL.md).
- **Quy chuẩn thiết kế Pixel-Perfect**: Banner Cam FPT (`#F37021`), Logo FPT Telecom chuẩn tỷ lệ, Lưới 12 cột (1.740px), Cấu trúc thẻ 2 dòng (Thân thẻ Pastel & Thanh đáy Accent 6px theo 8 mốc trạng thái).
- **Thiết lập Google Apps Script Realtime Engine**: Đồng bộ tự động 100% dữ liệu từ Product Backlog gốc sang Roadmap Timeline, tự động tối ưu diện tích thẻ hiển thị trọn vẹn Acceptance Criteria không bị cắt chữ, hỗ trợ 3 chế độ đồng bộ (OnEdit, Daily Timer 7:00 AM, 1-Click Menu).


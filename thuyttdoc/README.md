# THƯ MỤC TÀI NGUYÊN & TÀI LIỆU DỰ ÁN (`thuyttdoc`)

> **Quy chuẩn quy hoạch**: Thư mục `thuyttdoc` được phân chia thành các thư mục chuyên biệt theo đúng vai trò và mục đích nghiệp vụ, đảm bảo chuẩn hóa, ngăn nắp và dễ quản trị.

---

## 1. Cấu Trúc Phân Hệ Thư Mục

```
thuyttdoc/
├── doc/       # Tập trung toàn bộ tài liệu đặc tả nghiệp vụ BA (BRD, PRD, URD, Tech Spec)
├── uat/       # Chuyên biệt cho việc thực hiện kiểm thử UAT (File Excel UAT, tool đồng bộ)
├── roadmap/   # Quản lý toàn bộ tài liệu, bảng tính Backlog, Roadmap và tool đồng bộ của PO
├── pic-ba/    # Sơ đồ & Flow nghiệp vụ BA (BPMN, Flowchart, Sequence - chuẩn nền trắng)
└── pic-po/    # Hình ảnh chiến lược PO (Biểu đồ Roadmap, Backlog - chuẩn nhận diện FPT)
```

---

## 2. Chi Tiết Các Phân Vùng Chức Năng

| Thư mục | Đối tượng sử dụng | Nội dung chứa | Quy tắc lưu trữ |
|:---|:---|:---|:---|
| **`doc/`** | Business Analyst (BA) | Toàn bộ tài liệu văn bản: `BRD_*.doc`, `prd_*.doc`, `urd_*.doc`, User Stories, Tech Spec (`Kich_Ban_Ky_Thuat_*.xlsx`) | Tuân thủ Global Rule 19: Font Times New Roman 13pt, tiêu đề in đậm tăng dần, bảng căn vừa trang. |
| **`uat/`** | PO, BA, QC/Tester | File Excel thực hiện UAT (`UAT_GioHang_FPT_VN.xlsx`) và script sync UAT (`sync_uat.py`) | **Chỉ chứa các file để thực hiện UAT**. Không lưu tài liệu đặc tả hay ảnh sơ đồ tại đây. |
| **`roadmap/`** | Product Owner (PO) | Bảng tính tiến độ Roadmap & Backlog (`Roadmap_Website_CMS_Q4_2026.xlsx`), script đồng bộ (`sync_roadmap_cli.py`, `google_apps_script_*.js`), snapshot HTML/PNG | Tập trung toàn bộ tài liệu và công cụ quản trị lộ trình, tồn đọng sản phẩm (Backlog) của PO. |
| **`pic-ba/`** | Business Analyst (BA) | Sơ đồ luồng BPMN, Flowchart, Sequence (`.svg`, `.png`) | Bắt buộc nền trắng (`bgcolor="white"` - Global Rule 16), độ phân giải cao hoặc vector SVG. |
| **`pic-po/`** | Product Owner (PO) | Biểu đồ lộ trình Roadmap, Backlog, Release timeline (`.png`) | Đúng bảng màu nhận diện thương hiệu FPT (Xanh dương, Cam, Xanh lá). |

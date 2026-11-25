# THƯ MỤC TÀI LIỆU PHÂN TÍCH NGHIỆP VỤ BA (`doc`)

> **Quy chuẩn lưu trữ**: Bắt buộc toàn bộ tài liệu đặc tả nghiệp vụ của Business Analyst (BA) bao gồm: BRD (Business Requirements Document), PRD (Product Requirements Document), URD (User Requirements Document), User Stories và Tech Spec quy tắc nghiệp vụ **phải lưu trực tiếp vào thư mục này**.

---

## 1. Mục Đích & Phạm Vi Áp Dụng
- Thư mục tập trung duy nhất cho toàn bộ tài liệu văn bản phân tích nghiệp vụ (BA) trong dự án FPT Telecom (đặc biệt là luồng Giỏ hàng & Bán hàng FPT.vn).
- Tránh việc lưu trữ tài liệu rải rác ngoài thư mục gốc `thuyttdoc/`, giúp quản trị phiên bản và truy xuất tài liệu một cách chuẩn hóa, chuyên nghiệp.

---

## 2. Cấu Trúc Phân Loại Tài Liệu Trong Thư Mục

| Loại tài liệu | Tiền tố / Quy tắc đặt tên | Mô tả chi tiết |
|:---|:---|:---|
| **BRD** (Business Requirements) | `brd_<tên_nghiệp_vụ>.doc` / `BRD_<Tên>.doc` | Yêu cầu nghiệp vụ cấp cao từ khối kinh doanh / dịch vụ (Combo Internet, Thiết bị, Camera, FPT Play, Ultra Fast,...) |
| **PRD** (Product Requirements) | `prd_<tên_sản_phẩm>.doc` (VD: `prd_cart.doc`) | Tài liệu đặc tả yêu cầu sản phẩm chi tiết (Luồng giỏ hàng, Mini-cart, Checkout,...) |
| **URD** (User Requirements) | `urd_<tên_chức_năng>.doc` | Đặc tả yêu cầu người dùng theo từng giai đoạn và chức năng cụ thể |
| **User Stories & Tech Spec** | `user_stories_*.doc`, `Kich_Ban_Ky_Thuat_*.xlsx` | Danh sách User Stories & kịch bản kỹ thuật chi tiết cùng quy tắc nghiệp vụ (BR) |

---

## 3. Quy Chuẩn Định Dạng Tài Liệu BA (Theo Global Rules)
1. **Font chữ & Kích thước**: Toàn bộ nội dung tài liệu sử dụng font chữ **Times New Roman**, cỡ chữ **13pt** cho phần nội dung (detail). Các tiêu đề in đậm (Bold), tăng dần kích thước: Tiêu đề 1 size 16, tiêu đề 2 size 15, tiêu đề 3 size 14.
2. **Quy tắc nghiệp vụ**: Đánh số theo chuẩn `BR-01, BR-02,...`, reset lại từ `BR-01` khi bắt đầu bảng quy tắc nghiệp vụ của từng tính năng mới.
3. **Bảng biểu & Căn lề**: Các bảng biểu phải được căn lề đồng đều trong khổ trang tài liệu, cố định vừa vặn trong sườn văn bản, không được tràn lề hay thụt lệch.
4. **Hình ảnh & Sơ đồ nhúng**: Tất cả sơ đồ luồng (BPMN, Flowchart, Sequence) nhúng trong tài liệu phải được lấy từ thư mục `thuyttdoc/pic-ba/` (chuẩn nền trắng).

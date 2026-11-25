# THƯ MỤC QUẢN LÝ LỘ TRÌNH ROADMAP & BACKLOG PO (`roadmap`)

> **Quy chuẩn lưu trữ**: Thư mục này tập trung toàn bộ tài liệu bảng tính, kịch bản đồng bộ, mã nguồn Google Apps Script và dữ liệu liên quan đến **Lộ trình sản phẩm (Product Roadmap)** và **Phạm vi tồn đọng sản phẩm (Product Backlog)** thuộc trách nhiệm của Product Owner (PO).

---

## 1. Mục Đích & Phạm Vi Áp Dụng
- Tập trung duy nhất và có hệ thống toàn bộ file dữ liệu số, bảng tính theo dõi tiến độ sprint/quý, công cụ đồng bộ dữ liệu Realtime từ Google Sheets về hệ thống.
- Tách biệt rõ ràng với tài liệu phân tích nghiệp vụ của BA (`doc/`), kịch bản kiểm thử nghiệm thu (`uat/`), và kho hình ảnh sơ đồ (`pic-ba/`, `pic-po/`).

---

## 2. Danh Mục Các File Trong Thư Mục

| Tên File | Định dạng | Vai trò & Mục đích sử dụng |
|:---|:---|:---|
| `Roadmap_Website_CMS_Q4_2026.xlsx` | Excel (.xlsx) | Bảng tính theo dõi tiến độ tổng thể với 2 sheet nòng cốt: <br>1. **`Roadmap_Timeline_Q4`**: Biểu đồ Gantt thác nước theo dõi mốc tiến độ theo tuần/tháng. <br>2. **`Chi_Tiet_Backlog_Scope`**: Danh mục toàn bộ User Stories, Epic, độ ưu tiên (P1-P4) và trạng thái phân bổ. |
| `Roadmap_Website_CMS_Q4_2026.png` | Ảnh PNG | Bản snapshot biểu đồ lộ trình Roadmap Q4 xuất bản để nhúng báo cáo hoặc trình bày cho Stakeholders. |
| `roadmap_q4_2026.html` | HTML View | Giao diện HTML render trực quan bảng lộ trình Roadmap và ma trận tiến độ. |
| `sync_roadmap_cli.py` | Python Script (.py) | Công cụ CLI chạy trực tiếp trên máy để đồng bộ 2 chiều dữ liệu Backlog và Timeline từ Google Sheets qua Google Sheets API. |
| `google_apps_script_roadmap_sync.js` | JavaScript (.js) | Bộ mã nguồn thuật toán xử lý logic phân tầng tiến độ, tô màu Gantt thác nước, freeze header và chống đè dữ liệu trên Google Sheets. |
| `google_apps_script_auto_loader.js` | JavaScript (.js) | Script auto-loader gắn vào Google Sheet Apps Script để luôn tự động nạp phiên bản code xử lý mới nhất từ GitHub. |
| `backup_apps_script_old.json` | JSON (.json) | Bản backup cấu hình & phiên bản script cũ để truy vết lịch sử khi cần thiết. |
| `crop_header.png` | Ảnh PNG | Header mẫu hỗ trợ căn chỉnh tỷ lệ khung hình khi xuất biểu đồ Roadmap. |

---

## 3. Hướng Dẫn Vận Hành Đồng Bộ Dành Cho PO

### Cách 1: Đồng bộ trực tiếp trên Google Sheets (Khuyên dùng)
1. Mở file Google Sheets Roadmap online.
2. Tại thanh Menu điều khiển, chọn: **🚀 PRODUCT ROADMAP** -> **📈 Đồng Bộ Thác Nước Gantt (Bản mới nhất từ GitHub)**.
3. Script auto-loader sẽ tự động kéo logic mới nhất từ GitHub về thực thi mà không cần chỉnh sửa code thủ công.

### Cách 2: Chạy đồng bộ qua dòng lệnh Terminal
```bash
python3 thuyttdoc/roadmap/sync_roadmap_cli.py
```
Script sẽ tự động refresh token OAuth2 và đồng bộ cập nhật cấu trúc Waterfall Gantt lên Spreadsheet.

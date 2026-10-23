# THƯ MỤC HÌNH ẢNH SƠ ĐỒ & FLOW NGHIỆP VỤ BA (`pic-ba`)

> **Quy chuẩn lưu trữ**: Bắt buộc mọi sơ đồ, luồng nghiệp vụ (Flowchart, BPMN 2.0, Sequence Diagram, State Machine, Mockup) do BA tạo ra hoặc AI render tự động đều **phải lưu trực tiếp vào thư mục này**.

---

## 1. Mục Đích & Phạm Vi Áp Dụng
- Thư mục tập trung duy nhất cho toàn bộ hình ảnh nghiệp vụ của Business Analyst (BA) trong dự án FPT Telecom.
- Nghiêm cấm lưu trữ hình ảnh sơ đồ rải rác ngoài thư mục gốc, thư mục `diagrams/` hay các thư mục khác.
- Sau này, bất kỳ công cụ hoặc script nào (Graphviz, PlantUML, Mermaid, draw.io, figma exporter) khi xuất file ảnh (.png, .svg) đều phải trỏ đường dẫn output về `thuyttdoc/pic-ba/`.

---

## 2. Tiêu Chuẩn Hình Ảnh Sơ Đồ BA
1. **Nền Trắng (White Background - User Rule 16)**: Toàn bộ sơ đồ bắt buộc phải sử dụng nền màu trắng (`bgcolor="white"`), không dùng nền đen hay nền trong suốt gây khó nhìn khi in ấn hoặc nhúng vào tài liệu Word/URD.
2. **Quy tắc đặt tên file (Naming Convention)**:
   - Sơ đồ BPMN: `bpmn_<tên_chức_năng>.png` và `bpmn_<tên_chức_năng>.svg`
   - Sơ đồ Flowchart: `flow_<tên_luồng>.png`
   - Sơ đồ Sequence: `seq_<tên_kịch_bản>.png`
   - Sơ đồ State Machine: `state_<tên_thực_thể>.png`
3. **Độ phân giải & Tỷ lệ**: Render ở mật độ DPI tối thiểu 300dpi hoặc xuất định dạng vector `.svg` kèm theo để đảm bảo độ sắc nét cao nhất.

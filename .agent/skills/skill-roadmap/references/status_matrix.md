# MA TRẬN 8 MỐC TRẠNG THÁI & MÀU SẮC CHUẨN FPT TELECOM (ROADMAP ENGINE)

Tài liệu quy chuẩn dành cho **Product Owner (PO)**, **Tech Lead** và **Scrum Master** khi thiết lập và quản trị tiến độ trên Product Roadmap Google Sheets.

---

## 1. BẢNG MÃ MÀU VÀ TIẾN ĐỘ THEO TRẠNG THÁI (STATUS MATRIX)

| STT | Trạng thái nghiệp vụ | Tỷ lệ % tiến độ | Màu thân thẻ (Pastel Cấp 100) | Màu thanh tiến trình (Accent Đáy 6px) | Màu Badge Chip | Icon nhận diện | Ý nghĩa nghiệp vụ PO |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **0** | **Pending / On Hold** | `0%` | `#F3F4F6` (Xám nhạt) | `#9CA3AF` (Xám trung bình) | `#6B7280` | ⏸️ | Tạm hoãn, chờ làm rõ yêu cầu từ Business / Stakeholders |
| **1** | **Chưa tiếp nhận** | `12.5%` | `#F1F5F9` (Xám phấn nhạt) | `#94A3B8` (Xám Slate) | `#475569` | ⚪ | Đầu mục mới ghi nhận vào Backlog, chưa gán Sprint |
| **2** | **Đã tiếp nhận yêu cầu** | `25.0%` | `#DBEAFE` (Xanh baby dịu) | `#3B82F6` (Xanh dương FPT) | `#1D4ED8` | 🔵 | PO đã tiếp nhận, đưa vào danh sách phân tích của Quý |
| **3** | **Đang phân tích / Document** | `37.5%` | `#FFEDD5` (Cam đào dịu mắt) | `#F97316` (Cam rực rỡ) | `#C2410C` | 🟠 | BA đang viết URD / BRD / SRS, thiết kế UI/UX luồng |
| **4** | **Transfer DEV / PO reviewed** | `50.0%` | `#DCFCE7` (Xanh lá non dịu) | `#22C55E` (Xanh lá nhận diện) | `#15803D` | 🟢 | PO đã review URD, bàn giao requirement và kickoff cùng DEV |
| **5** | **DEV In Progress** | `62.5%` | `#FEF9C3` (Vàng bơ phấn dịu) | `#EAB308` (Vàng nghệ đậm) | `#A16207` | 🟡 | Đội ngũ lập trình đang triển khai code frontend / backend / API |
| **6** | **UAT** | `75.0%` | `#F3E8FF` (Tím pastel dịu) | `#A855F7` (Tím đậm nổi bật) | `#6B21A8` | 🟣 | Bàn giao môi trường Staging, Tester & PO thực hiện nghiệm thu |
| **7** | **Done** | `100.0%` | `#D1FAE5` (Xanh ngọc bích nhạt)| `#10B981` (Xanh ngọc bích full)| `#047857` | ✅ | Tính năng đã Deploy Production thành công, đóng task |

---

## 2. QUY CHUẨN THIẾT KẾ THẺ TASK 2 TẦNG (2-ROW CARD ARCHITECTURE)

Mỗi task trên Roadmap được thiết kế gồm **2 dòng liên kết chặt chẽ**:
1. **Dòng 1: Thân thẻ Task (Chiều cao chuẩn 36px)**
   - Nền mang màu **Pastel cấp độ 100** dịu mắt, không gây chói hay mỏi mắt khi nhìn bảng tổng thể.
   - Text gồm 2 dòng RichText:
     - Dòng trên: `[Hệ thống] Tên Task` (Font Times New Roman 10pt Bold, màu đen `#1E293B`).
     - Dòng dưới: `Acceptance Criteria / Detail` (Font Times New Roman 8.5pt Italic, màu xám xanh `#475569`).
   - Badge bên phải: Phân hạng ưu tiên `[P1] / [P2]` và Nhãn trạng thái `[DEV In Progress] / [UAT]`.
   - Độ rộng hiển thị text: Tận dụng trọn vẹn diện tích (Task 1 tháng: 85 ký tự; Task 2 tháng: 170 ký tự, không bị cắt dấu `...`).

2. **Dòng 2: Thanh tiến trình đáy thẻ (Chiều cao cố định 6px)**
   - Tỷ lệ màu chia theo đúng cột W1-W4 của tháng.
   - Các cột thuộc tỷ lệ hoàn thành mang màu **Accent đậm rực rỡ** của trạng thái tương ứng.
   - Các cột còn lại mang màu nền Canvas `#F8FAFC` để thể hiện rõ ràng đoạn đường còn phải đi.
   - **CHỈ DUY NHẤT TRẠNG THÁI `Done`** mới hiển thị full 100% màu toàn bộ cây task.

# ĐẶC TẢ KỸ THUẬT GOOGLE SHEETS PRODUCT ROADMAP (PIXEL-PERFECT SPEC)

Tài liệu quy định chi tiết kích thước, tỷ lệ, kiểu chữ và bố cục lưới Google Sheets để đạt độ hoàn thiện **Pixel-Perfect 1.740px** vừa vặn màn hình tiêu chuẩn ở mức thu phóng 100%.

---

## 1. THÔNG SỐ LƯỚI & ĐỘ RỘNG CỘT (GRID SPECIFICATION)

| Tham số | Giá trị chuẩn | Diễn giải kỹ thuật |
|:---|:---:|:---|
| **Tổng số cột** | **12 Cột** (Từ Cột A đến Cột L) | Tương ứng 3 Tháng trong Quý (Tháng 10, Tháng 11, Tháng 12). |
| **Phân bổ theo tháng** | 4 Cột / Tháng | Mỗi tháng tương ứng 4 Tuần (W1, W2, W3, W4). |
| **Độ rộng mỗi cột** | **145 px** | `roadmapSheet.setColumnWidth(col, 145);` |
| **Tổng bề rộng bảng** | **1.740 px** | $12 \times 145\text{px} = 1.740\text{px}$ (Vừa khít màn hình Desktop tiêu chuẩn). |
| **Xóa cột thừa** | Cột 13 trở đi | Tự động xóa từ cột 13 đến hết sheet để tạo khung đóng kín, không bị dư viền. |

---

## 2. THÔNG SỐ CHIỀU CAO DÒNG (ROW HEIGHT SPECIFICATION)

| Dòng | Nội dung | Chiều cao (px) | Kiểu dáng & Màu sắc nhận diện FPT |
|:---:|:---|:---:|:---|
| **Dòng 1** | **Banner Tiêu Đề Bảng** | **32 px** | Nền **Màu Cam FPT Telecom (`#F37021`)**, chữ Trắng (`#FFFFFF`) 14pt Bold Times New Roman căn giữa. Góc trái chèn **Logo FPT Telecom** tỷ lệ 76px × 24px lọt lòng. |
| **Dòng 2** | Ghi chú Hot Request | **20 px** | Nền Trắng, chữ Đỏ (`#DC2626`) 9pt Italic Times New Roman căn giữa. |
| **Dòng 3** | Tiêu đề Tháng (M10, M11, M12) | **26 px** | Nền 3 màu nhận diện: Tháng 10 (Xanh dương `#1E40AF`), Tháng 11 (Tím `#6B21A8`), Tháng 12 (Xanh lá `#047857`). Chữ Trắng 11pt Bold. |
| **Dòng chẵn (4, 7, 10...)** | **Thân Thẻ Task (Dòng 1)** | **36 px** | Nền màu Pastel cấp độ 100 theo trạng thái. Dòng trên 10pt Bold đen, dòng dưới 8.5pt Italic xám. |
| **Dòng lẻ (5, 8, 11...)** | **Thanh Tiến Trình (Dòng 2)** | **6 px** | Màu Accent rực rỡ chạy theo tỷ lệ % trạng thái (chỉ Done mới full 100%). |
| **Dòng ngăn cách (6, 9, 12...)**| Khoảng cách giữa các thẻ | **8 px** | Nền trống màu Canvas `#FFFFFF` / `#F8FAFC`, không có viền. |
| **Dòng cuối cùng** | Footer Nguồn dữ liệu | **24 px** | Chữ nghiêng 9pt: `Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)`. |

---

## 3. QUY TẮC FONT CHỮ TOÀN BẢNG (TYPOGRAPHY)
* **Font Family duy nhất**: `Times New Roman` (Quy định bắt buộc theo User Rule 19 cho toàn bộ tài liệu và bảng biểu FPT Telecom).
* **Quy chuẩn Font Size**:
  - Tiêu đề Banner Dòng 1: `14pt - Bold`
  - Tiêu đề Tháng Dòng 3: `11pt - Bold`
  - Tên Hệ thống & Tên Task: `10pt - Bold`
  - Detail (Acceptance Criteria): `8.5pt - Italic`
  - Badge trạng thái & Priority: `8.5pt - Bold`
  - Ghi chú & Footer: `9pt - Italic`

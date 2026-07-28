# Canva Content Pack — Product Roadmap FCP
Nguồn: po/prod/roadmap.html · Sync gần nhất: 27/07/2026 (đã kiểm tra lại đúng sheet 📌 Product Backlog FCP)
Link Canva: https://www.canva.com/design/DAHQk_G9-rg/7NJCqk87D9UMQDaxp618Sw/edit

---

## ⚠️ Điều chỉnh so với bản trước
- **Bỏ mọi nhắc đến "Camera / T5"**: hạng mục Camera không thuộc sheet 📌 Product Backlog FCP — bị lấy nhầm từ tab khác ở lần sync trước.
- **Thêm cột "Chưa phân loại"**: 1 hạng mục mới trên sheet (chatbot Daisy) chưa được gán Epic/PIC/Trạng thái.

---

## 1. Bảng màu FPT Design System (dùng cho fill/border trong Canva)

### Màu thương hiệu FPT (dải màu chủ đạo — dùng cho header/stripe)
| Tên | Hex |
|---|---|
| Cam FPT | #F58220 |
| Xanh lá FPT | #00954F |
| Xanh dương FPT | #005BAA |

### Màu Epic (dùng cho thanh màu bên trái mỗi card + chip nhãn)
| Epic | Màu chữ / thanh | Màu nền chip |
|---|---|---|
| CMS | #2A78D6 | #EAF2FC |
| Web | #EB6834 | #FDEEE7 |
| Cart | #1BAF7A | #E6F7F0 |
| Chưa gán | #5B5850 | #EEECE7 |

### Màu trạng thái (status pill)
| Trạng thái | Màu chữ | Màu nền |
|---|---|---|
| ● Hoàn thành | #0CA30C | #E5F6E5 |
| ● Đang phân tích | #2A78D6 | #EAF2FC |
| ● Đã tiếp nhận | #B8860B | #FBF1DA |
| ● Chưa tiếp nhận / Chưa gán | #898781 | #EFEEEA |

**Gợi ý dựng trong Canva:** tìm template có sẵn theo từ khoá "Kanban board" hoặc "Project roadmap timeline" trong thư viện Canva, sau đó recolor từng cột/card bằng bảng màu trên (dùng tính năng "Edit colors" hoặc đổi màu shape trực tiếp).

**Card gọn (compact) — mỗi card chỉ 3 dòng để dễ bổ sung task:**
- Dòng 1: chip Epic + chip Trạng thái (đặt cạnh nhau, cùng 1 hàng)
- Dòng 2: Tiêu đề hạng mục (in đậm)
- Dòng 3 (chỉ khi có): PIC · Phụ thuộc (gộp chung 1 dòng nhỏ, màu xám, in nghiêng phần phụ thuộc)

---

## 2. Header trang

**Eyebrow:** FPT Telecom · FCP
**Tiêu đề:** Product Roadmap theo tháng — Product Backlog FCP

> Header chỉ còn eyebrow + tiêu đề — đã bỏ dòng mô tả, callout cảnh báo và dòng nguồn/sync để tập trung vào nội dung board. Footer (mục 5) chỉ còn 1 câu ngắn.

**4 stat tile:**
- 15 — Tổng số hạng mục
- 10 — Đang phân tích
- 4 — Tháng trong lộ trình (T8–T11)
- 1 — Mới, chưa phân loại

---

## 3. Legend (chú thích màu — đặt ngay trên board)

Epic: ● CMS · ● Web · ● Cart · ● Chưa gán
Trạng thái: ● Hoàn thành · ● Đang phân tích · ● Đã tiếp nhận · ● Chưa tiếp nhận / Chưa gán

---

## 4. Board theo tháng (mỗi cột = 1 khối trong Canva, mỗi card = 1 shape con)

### 🔵 Tháng 8/2026 — Nền tảng Cart & Checkout (4 hạng mục)

**Card 1** [Web]
Luồng giỏ hàng — add-on nhiều SP/SKU/SA
Trạng thái: ● Đang phân tích · PIC: ThuyTT104

**Card 2** [Cart]
[BE] Luồng giỏ hàng — nhu cầu FE theo kênh
Trạng thái: ● Đang phân tích · PIC: Yennt122

**Card 3** [Cart]
[BE] Luồng giỏ hàng — phân tích chi tiết
Trạng thái: ● Đang phân tích · PIC: Thanhvt58

**Card 4** [CMS]
Cấu hình hiển thị checkout theo kênh
Trạng thái: ● Đang phân tích · PIC: LongNH156

---

### 🔵 Tháng 9/2026 — Thanh toán & Voucher (4 hạng mục)

**Card 1** [CMS]
Phương thức thanh toán — bật/tắt theo kênh
Trạng thái: ● Đang phân tích · PIC: LongNH156

**Card 2** [CMS]
Cấu hình nội dung Gói bán / Combo / SA
Trạng thái: ● Đang phân tích · PIC: LongNH156

**Card 3** [Web]
Rule ưu tiên/loại trừ & cấu hình chi tiết Voucher
Trạng thái: ● Đang phân tích · PIC: ThuyTT104
Phụ thuộc: Luồng giỏ hàng (T8) hoàn tất

**Card 4** [CMS]
Quản lý bài viết của tác giả (tin tức)
Trạng thái: ● Đã tiếp nhận · PIC: LongNH156

---

### 🔵 Tháng 10/2026 — Trải nghiệm tìm/so sánh SP (4 hạng mục)

**Card 1** [CMS]
Trang phòng giao dịch — UI tìm kiếm mới
Trạng thái: ● Đang phân tích · PIC: SonLN11

**Card 2** [Web]
Tính năng tìm kiếm sản phẩm trên website
Trạng thái: ● Đang phân tích

**Card 3** [Web]
Tính năng so sánh sản phẩm (PLP/PDP)
Trạng thái: ● Đang phân tích

**Card 4** [CMS]
Quản lý ID cho banner page Tin tức
Trạng thái: ● Chưa tiếp nhận · PIC: LongNH156

---

### ⚪ Tháng 11/2026 — Combo & Referral (GTBB) (2 hạng mục)

**Card 1** [Web]
Add Combo Camera tại PDP Camera Only
Trạng thái: ● Chưa tiếp nhận · PIC: SonLN11, ThuyTT104
Phụ thuộc: Cấu hình Combo/SA (T9) hoàn tất

**Card 2** [Web]
CS tặng thiết bị cho GTBB (referral)
Trạng thái: ● Chưa tiếp nhận
Phụ thuộc: Rule Voucher (T9) hoàn tất

---

### ⚫ Chưa phân loại — cần grooming (1 hạng mục)

**Card 1** [Chưa gán]
Thêm điểm chạm cho chat bot Daisy trên HomePage
Trạng thái: ● Chưa gán
Cần gán Epic/PIC/Trạng thái

---

## 5. Footer note

Ghi chú: Lộ trình ước tính, chưa phải mốc cam kết chính thức. Chi tiết: xem po/doc.

---

## 6. Hướng dẫn dựng nhanh trong Canva

1. Mở link Canva → search template "Kanban" hoặc "Roadmap timeline" trong thanh Elements/Templates.
2. Tạo 5 cột (frame/group): T8 · T9 · T10 · T11 · Chưa phân loại (theo thứ tự trên).
3. Mỗi card trong cột = 1 rectangle bo góc + text box, thanh màu trái theo Epic (mục 1), chip trạng thái theo màu status (mục 1).
4. Copy nội dung từng card ở mục 4 vào text box tương ứng.
5. Header/stripe trên cùng dùng 3 màu thương hiệu FPT (cam/xanh lá/xanh dương) chia 3 dải ngang mỏng, giống dải màu nhận diện FPT.
6. Legend đặt ngay dưới header, dùng dot tròn nhỏ + label như liệt kê ở mục 3.

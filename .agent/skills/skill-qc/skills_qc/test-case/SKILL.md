---
name: test-case
description: >-
  Skill bắt buộc khi viết, tạo, review, hoặc rà soát test case / testcase / kịch bản kiểm thử.
  Auto-triggers whenever the prompt involves: test case, testcase, test scenario, QA, kiểm thử,
  acceptance criteria, happy path, negative case, edge case, idempotent test, UI test, API test,
  test coverage, test matrix, viết TC, bảng test case, QC.
  Tự động kích hoạt khi prompt tiếng Việt liên quan đến: viết test case, tạo testcase, viết kịch bản kiểm thử,
  liệt kê test case, review test case, bổ sung case còn thiếu, cover happy path / negative / edge case,
  sinh test case từ Confluence, từ Jira ticket, hoặc từ summary ticket.
  Agent MUST read this SKILL.md và tuân theo template + quy tắc trước khi sinh bất kỳ test case nào.
  Agent MUST luôn xuất kết quả test case cuối cùng ra một file .md trong thư mục docs/.
---

# Skill Viết Testcase

## ⚠️ Quy tắc bắt buộc về đầu ra (Output)

**Kết quả cuối cùng BẮT BUỘC phải được ghi ra một file `.md` trong thư mục `docs/`.**

- Đường dẫn: `docs/test-case-<ten-tinh-nang-hoac-ma-ticket>.md`
  - Ví dụ: `docs/test-case-xac-thuc-vneid.md`, `docs/test-case-PAYMENT-1234.md`
  - Tên file dùng chữ thường, không dấu, nối bằng dấu `-` (kebab-case).
- Nếu thư mục `docs/` chưa tồn tại thì tạo mới.
- Nếu file đã tồn tại: hỏi người dùng muốn ghi đè hay tạo file mới với hậu tố `-v2`, `-v3`...
- KHÔNG chỉ in bảng test case ra chat rồi dừng lại. Việc tạo file `.md` là bước hoàn thành bắt buộc.
- Sau khi tạo file, báo lại cho người dùng đường dẫn file đã xuất.

### Cấu trúc file .md cần có

```markdown
# Test Case — <Tên tính năng / Mã ticket>

- **Nguồn**: <Confluence / Jira ticket / Summary>
- **Ngày tạo**: <yyyy-mm-dd>
- **Người tạo**: AI Agent

## Bảng Test Case

| TC Name | Expected | Note |
|---------|----------|------|
| ... | ... | ... |
```

Nếu có nhiều nhóm scenario, chia thành nhiều mục `## <Tên nhóm>` riêng, mỗi mục một bảng.

## Template

| TC Name | Expected | Note |
|---------|----------|------|
| | | |

## Quy tắc viết testcase

- **TC Name**: Luôn bắt đầu bằng **"Kiểm tra"** + mô tả scenario. Ví dụ: `Kiểm tra KH không thuộc KH Sim FPT truy cập xác thực`
- **Expected**: Kết quả mong đợi sau khi thực hiện
- **Note**: Ghi chú thêm nếu cần (edge case, điều kiện đặc biệt, cần confirm BA)

## Nguồn để viết testcase

1. **Từ Confluence** — đọc phần Mô tả UI / Acceptance Criteria
2. **Từ Jira ticket** — đọc Description (Steps, Expected, Actual)
3. **Từ Summary ticket** — suy luận các case happy path + negative

## Các loại testcase cần cover

- ✅ Happy path — luồng thành công
- ❌ Negative — luồng thất bại, lỗi
- 🔄 Edge case — giá trị biên, dữ liệu đặc biệt
- 🔁 Idempotent — thực hiện nhiều lần kết quả không đổi
- 📱 UI — hiển thị đúng design, ẩn/hiện đúng điều kiện
- 🔌 API — payload đúng, response đúng

## Ví dụ thực tế

### Từ Confluence — Xác thực thuê bao VNeid

| TC Name | Expected | Note |
|---------|----------|------|
| KH không thuộc KH Sim FPT truy cập xác thực | Hiển thị popup yêu cầu đăng nhập tài khoản FPT | |
| KH Sim FPT không thuộc đối tượng cần xác thực | Hiển thị thông báo không thuộc đối tượng cần xác thực | Cần confirm lại flow với BA |
| KH chọn phương thức VNeid | Hiển thị danh sách phương thức, chọn được VNeid | Phương thức hiển thị theo config CMS |
| Nhập CCCD đúng định dạng | Chuyển sang màn xác nhận chia sẻ thông tin VNeid | |
| Nhập CCCD sai định dạng | Hiển thị thông báo lỗi, không cho tiếp tục | |
| KH xác nhận chia sẻ thông tin VNeid | Gọi API chia sẻ thành công, chuyển sang bước liveness | |
| KH từ chối chia sẻ thông tin VNeid | Quay lại màn chọn phương thức xác thực | |
| Liveness thành công | Chụp ảnh thành công, chuyển sang bước so sánh CSDLQG | |
| Liveness thất bại | Hiển thị thông báo lỗi, cho phép thử lại | ánh sáng kém, che mặt, ảnh giả |
| So sánh ảnh khớp CSDLQG | Hiển thị trạng thái cập nhật thuê bao thành công | |
| So sánh ảnh không khớp CSDLQG | Hiển thị trạng thái thất bại, hướng dẫn thử lại | |
| CMS tắt phương thức VNeid | Phương thức VNeid không hiển thị trong danh sách | |

### Từ Jira ticket — Loyalty điểm khi login app

| TC Name | Expected | Note |
|---------|----------|------|
| Login web, chưa login app, chưa follow Zalo OA → Login app | isAppFptShop = TRUE, isZaloFptShop = FALSE | Chỉ truyền isAppFptShop = TRUE |
| Login web, chưa login app, đã follow Zalo OA → Login app | isAppFptShop = TRUE, isZaloFptShop = TRUE (giữ nguyên) | Login app không reset isZaloFptShop |
| Login app thành công → Kiểm tra dùng điểm Loyalty | Cho phép sử dụng điểm Loyalty | isAppFptShop = TRUE là điều kiện đủ |
| Chưa login app, chưa follow Zalo OA → Dùng điểm | Không cho phép sử dụng điểm | |
| Login app nhiều lần liên tiếp | Trạng thái không thay đổi, vẫn cho phép dùng điểm | Idempotent |

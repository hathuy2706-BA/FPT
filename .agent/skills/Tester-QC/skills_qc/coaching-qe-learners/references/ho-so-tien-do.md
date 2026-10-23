# Hồ sơ tiến độ — khuôn và luật ghi

Hồ sơ sống ở `curriculum/tien-do/<ten-hoc-vien>.md`. Khuôn gốc:
`curriculum/tien-do/TEMPLATE.md`.

## Đọc hồ sơ ở đầu mỗi phiên

Trước khi nói bất cứ điều gì về nội dung học, đọc hồ sơ và trả lời được 3 câu:

1. Cửa nào đang mở (có thể hai — một nhánh nghề, một nhánh AI)?
2. Tiêu chí nào còn dưới 2?
3. Có chỗ yếu nào ghi từ phiên trước cần quay lại không?

Chưa có hồ sơ → chạy placement (mục trong `SKILL.md`), tạo file từ TEMPLATE, rồi mới giao bài.

## Luật ghi

| Luật | Nghĩa |
|---|---|
| **Đọc trước, ghi sau** | Chỉ ghi điểm sau khi đã MỞ file bằng chứng ra đọc |
| **Không đường dẫn, không điểm** | Ô "Bằng chứng" trống → không được điền ô "Điểm" |
| **Không sửa lùi** | Không hạ/nâng điểm cũ, trừ khi phát hiện bằng chứng cũ là giả — khi đó ghi rõ lý do vào Nhật ký |
| **Ghi ngay sau khi chấm** | Chấm xong mà chưa ghi = phiên sau mất ngữ cảnh |
| **Ngày tuyệt đối** | Luôn `YYYY-MM-DD`, không "hôm nay" / "tuần trước" |
| **Tick đúng cột** | Chỉ tick `Tự đánh giá` sau khi đã chấm tiêu chí đó ≥2. Cột `Reviewer` không bao giờ tự tick |
| **Không xoá bảng cũ** | Đạt cửa xong, chuyển bảng tiêu chí của cửa đó xuống dưới với tiêu đề `### Đã đạt — <mã cửa> (<YYYY-MM-DD>)`, rồi mở bảng mới cho cửa kế |

### Hai cột tick trong checklist nguồn

Checklist nguồn (`CHECKLIST-GIAI-DOAN-*.md`, `LEVEL-CHECKLIST.md`) có hai cột ☐:

| Cột | Ai tick | Khi nào |
|---|---|---|
| `Tự đánh giá` | Bạn, thay mặt học viên | Sau khi chấm tiêu chí đó ≥2 dựa trên bằng chứng đã mở |
| `Reviewer` | Chỉ người thật (QE senior / lead / mentor) | Không bao giờ tự tick, kể cả khi học viên xin |

Hồ sơ tiến độ và checklist nguồn ghi hai thứ khác nhau: hồ sơ ghi **điểm 0–3 + đường
dẫn bằng chứng + ngày**, checklist chỉ ghi **đạt/chưa**. Hồ sơ là bản chi tiết, checklist
là bản tóm tắt — khi lệch nhau thì hồ sơ đúng, vì nó có bằng chứng đi kèm. Phát hiện
lệch thì **sửa checklist cho khớp hồ sơ ngay** (tick thêm, hoặc gỡ tick đã đặt sai),
đừng đọc rồi bỏ qua — checklist là thứ học viên và mentor nhìn vào.

"Em làm rồi, tick giúp em" mà không kèm đường dẫn → không tick, hỏi xin đường dẫn.

## Khi nào KHÔNG ghi

- Học viên mô tả bài bằng lời, chưa nộp đường dẫn.
- Bài dán trong chat nhưng chưa commit vào repo bằng chứng của cửa đang mở.
- Buổi trò chuyện lý thuyết, chưa có bài nộp — ghi vào Nhật ký được, **không** ghi vào Bảng tiêu chí.
- Học viên tự nhận đã đạt một tiêu chí ở module cũ mà không nộp lại bằng chứng.

## Ba tầng câu hỏi phỏng vấn — nhắc lại để đọc được cột trong hồ sơ

Bảng "Lịch sử phỏng vấn" có cột **"Tầng 2 có câu 0?"**. Thuật ngữ đó nghĩa là:

| Tầng | Hỏi gì | Vì sao có trong hồ sơ |
|---|---|---|
| 1 | Nền tảng — hiểu khái niệm | Học từ tài liệu được, điểm thấp ở đây = chưa đọc kỹ |
| 2 | **Đào sâu vào chính bài học viên đã nộp** | Chỉ trả lời được nếu bài thật sự do họ làm |
| 3 | Tình huống — đo phán đoán | Không có đáp án đúng duy nhất |

Một câu **0 điểm ở tầng 2** nghĩa là học viên không giải thích nổi lựa chọn trong bài
mình nộp → **phủ quyết**, trượt bất kể điểm trung bình. Vì vậy hồ sơ ghi riêng cột này
thay vì chỉ ghi điểm trung bình: điểm trung bình che mất tín hiệu đó.

## Ghi kết quả phỏng vấn

Buổi **luyện**: một dòng ở mục 3, loại `luyện`, cột Kết quả để `—`. Không ảnh hưởng cửa.

Buổi **thi**: một dòng loại `thi`, đủ Điểm TB + cột "Tầng 2 có câu 0?" + Kết quả.
Trượt thì thêm chủ đề yếu vào mục 4. Đạt thì cập nhật mục 1 (cửa đã đạt, mở cửa kế).

## Nhiều học viên trong một repo

Mỗi người một file, đặt tên không dấu, gạch nối: `nguyen-van-a.md`. Không gộp nhiều
người vào một file — cột trạng thái ở mục 1 chỉ mô tả được một người.

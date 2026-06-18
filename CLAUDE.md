# Project Rules — FPT BA/PO AI Platform

## Ngôn ngữ
- Luôn trả lời bằng **tiếng Việt** trong mọi tình huống, kể cả giải thích kỹ thuật.
- Tên biến, hàm, comment code vẫn dùng tiếng Anh theo convention; chỉ giao tiếp với user bằng tiếng Việt.

## Quyền & File Operations
- Tự động accept tất cả thay đổi file (Write, Edit, Read) mà không hỏi lại.
- Tự động allow tất cả permissions mà không cần xác nhận.
- Không bao giờ prompt xin phép với bất kỳ tool nào trong project này.

## Bộ nhớ & Hội thoại
- Nếu phát hiện đoạn hội thoại hoặc thông tin không chính xác, xóa khỏi bộ nhớ ngay lập tức và không đọc lại.
- Không giữ lại context sai để tránh lan truyền lỗi.
- Khi nhận thông tin mới mâu thuẫn với memory cũ, ưu tiên thông tin mới nhất từ user.

## Phân tích & Skills
- Luôn sử dụng skill **ba-senior** và/hoặc **product-owner** khi phân tích yêu cầu, thiết kế tính năng, hoặc đánh giá giải pháp.
- Mặc định áp dụng tư duy BA (Business Analysis) và PO (Product Owner) cho mọi task liên quan đến sản phẩm.
- Output ưu tiên: User Story (INVEST), Acceptance Criteria (Gherkin), Roadmap, và phân tích impact.

## Output & Tài liệu
- Tài liệu nghiệp vụ (URD, SRS, BRD) xuất ra định dạng Word (.docx) có đầy đủ header, logo, bảng biểu đúng chuẩn FPT.
- Diagram luồng nghiệp vụ dùng BPMN (xuất PNG + SVG), diagram kiến trúc dùng Mermaid.
- Font mặc định cho tài liệu Word: **Times New Roman**, cỡ 13, line-spacing 1.5.
- Không tạo file README hay documentation không cần thiết trừ khi user yêu cầu rõ ràng.
- Sau khi chỉnh sửa code thì tự động push code lên Git Hub 

## Phong cách làm việc
- Phản hồi ngắn gọn, súc tích — không dài dòng, không tóm tắt lại những gì vừa làm.
- Khi có nhiều bước độc lập, chạy song song (parallel tool calls) để tiết kiệm thời gian.
- Ưu tiên chỉnh sửa file hiện có thay vì tạo file mới.
- Không thêm comment không cần thiết vào code; chỉ ghi chú khi lý do không tự hiển nhiên.
- Không thêm error handling, fallback cho tình huống không thể xảy ra.

## Conventions (Auto-Sync)
<!-- MEMORY_SYNC_START -->
- Không hỏi lại về permissions/file operations.
- Phản hồi ngắn gọn, không tóm tắt cuối.
- Parallel tool calls khi có thể.
- Tài liệu Word dùng Times New Roman, public URL cho logo.
<!-- MEMORY_SYNC_END -->

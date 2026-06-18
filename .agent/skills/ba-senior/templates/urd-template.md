# URD TEMPLATE — TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (FPT TELECOM CHUẨN)

> **Hướng dẫn sử dụng template này:**
> - File output là `.doc` (HTML-based, mở được bằng MS Word)
> - Thay toàn bộ `[PLACEHOLDER]` bằng nội dung thực tế
> - Logo: nhúng dạng base64 Data URI (`data:image/png;base64,...`) để tránh broken link khi mở trên máy khác
> - Mỗi đầu mục lớn (MỤC LỤC, A, B, C, D, E) PHẢI xuống trang mới
> - Sơ đồ flow: dùng skill `diagram-drawer`, xuất PNG nền trắng, nhúng bằng thẻ `<img class="diagram-img">`

---

## PHẦN 1 — HTML SHELL (Copy toàn bộ vào file .doc)

```html
<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>FPT.VN URD - [TÊN HỆ THỐNG]</title>
<style>
    /* ===== TYPOGRAPHY ===== */
    body { font-family: 'Times New Roman', Times, serif; line-height: 1.5; color: #000000; font-size: 12pt; }

    /* ===== ĐÁNH SỐ TRANG (MS WORD) — bắt buộc ===== */
    /* Footer field PAGE/NUMPAGES tự đánh số trang khi mở bằng Word.
       Phải bọc toàn bộ thân tài liệu trong div.Section1 và đặt div footer id=f1 (mso-element:footer) ở cuối. */
    @page Section1 {
        size: 21.0cm 29.7cm;          /* A4 dọc */
        margin: 2.0cm 2.0cm 2.0cm 2.0cm;
        mso-header-margin: 1.0cm;
        mso-footer-margin: 1.0cm;
        mso-paper-source: 0;
        mso-footer: f1;
    }
    div.Section1 { page: Section1; }
    p.MsoFooter, p.MsoHeader { margin: 0; font-family: 'Times New Roman', serif; font-size: 9pt; color: #666666; }

    /* ===== TRANG BÌA ===== */
    .cover-container {
        border: 4px double #1f4e78;
        padding: 50px 40px;
        margin: 10px;
        min-height: 800px;
        position: relative;
    }
    .cover-logo-box { text-align: left; margin-bottom: 30px; }
    /* Logo FPT Telecom: kích thước chuẩn 4cm x 1.4cm, góc trái trên (dùng đơn vị cm để in đúng) */
    .cover-logo { width: 4cm; height: 1.4cm; display: block; margin: 0; }
    .cover-badge { display: inline-block; border: 1.5px solid #c00000; color: #c00000; font-family: 'Arial', sans-serif; font-size: 9.5pt; font-weight: bold; letter-spacing: 0.5px; padding: 4px 12px; }
    .cover-org { font-family: 'Arial', sans-serif; color: #808080; font-size: 10.5pt; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 18px; }
    .cover-title-en { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 13pt; font-style: italic; margin-top: -6px; margin-bottom: 26px; }
    .cover-scope { font-family: 'Arial', sans-serif; color: #595959; font-size: 11pt; margin-top: 8px; }
    .cover-copyright { border-top: 1px solid #d0d0d0; margin-top: 28px; padding-top: 10px; text-align: center; font-family: 'Arial', sans-serif; font-size: 9pt; color: #808080; }
    .cover-title-box { text-align: center; margin-top: 40px; margin-bottom: 60px; }
    .cover-title-main {
        font-family: 'Arial', sans-serif;
        color: #1f4e78;
        font-size: 24pt;
        font-weight: bold;
        text-transform: uppercase;
        line-height: 1.4;
        margin-bottom: 20px;
    }
    .cover-title-sub {
        font-family: 'Arial', sans-serif;
        color: #e37222;
        font-size: 14pt;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 10px;
        letter-spacing: 0.5px;
    }
    .cover-meta-box {
        margin-top: 60px;
        width: 100%;
        border-top: 2px solid #1f4e78;
        padding-top: 20px;
    }
    .cover-meta-table { width: 100%; border-collapse: collapse; border: none; }
    .cover-meta-table td { border: none; padding: 6px 0; font-size: 11pt; color: #333333; }
    .cover-meta-label { font-weight: bold; color: #1f4e78; width: 140px; }

    /* ===== HEADINGS ===== */
    /* LƯU Ý: h1 có page-break-before để đầu mục lớn luôn xuống trang mới */
    h1 { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 18pt; font-weight: bold; text-transform: uppercase; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #1f4e78; padding-bottom: 5px; page-break-before: always; mso-page-break-before: always; }
    h2 { font-family: 'Arial', sans-serif; color: #2e75b6; font-size: 14pt; font-weight: bold; margin-top: 24px; margin-bottom: 12px; border-bottom: 1px solid #2e75b6; padding-bottom: 3px; }
    h3 { font-family: 'Arial', sans-serif; color: #5b9bd5; font-size: 12pt; font-weight: bold; margin-top: 18px; margin-bottom: 8px; }
    h4 { font-family: 'Arial', sans-serif; color: #000000; font-size: 12pt; font-weight: bold; margin-top: 14px; margin-bottom: 6px; }

    /* ===== BẢNG DỮ LIỆU ===== */
    table.data-table { border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 15px; table-layout: auto; word-wrap: break-word; }
    table.data-table th, table.data-table td { border: 1px solid #000000; padding: 6px 8px; text-align: left; vertical-align: top; font-size: 11pt; }
    table.data-table th { background-color: #d9e1f2; font-weight: bold; color: #1f4e78; font-size: 10.5pt; }

    /* ===== BẢNG USE CASE ===== */
    table.usecase-table { border-collapse: collapse; width: 100%; margin-top: 8px; margin-bottom: 12px; }
    table.usecase-table td { border: 1px solid #000000; padding: 8px; vertical-align: top; }
    table.usecase-table td.label { background-color: #f2f2f2; font-weight: bold; width: 150px; }

    /* ===== MỤC LỤC — WORD CLASSIC STYLE ===== */
    .toc-title { page-break-before: always; mso-page-break-before: always; font-family: 'Times New Roman', Times, serif; font-size: 16pt; font-weight: bold; text-align: center; color: #000000; text-transform: uppercase; margin-bottom: 18px; letter-spacing: 0; padding-bottom: 0; border-bottom: none; }
    .toc-list { width: 100%; margin-bottom: 2px; }
    p.toc-entry { font-family: 'Times New Roman', Times, serif; color: #000000; font-size: 12pt; line-height: 1.25; margin-top: 0; margin-bottom: 6px; text-align: left; white-space: normal; overflow-wrap: normal; word-break: normal; mso-tab-count: 1; }
    p.toc-l1 { font-weight: bold; margin-left: 0; text-indent: 0; tab-stops: right dotted 16.8cm; }
    p.toc-l2 { font-weight: normal; margin-left: 0.75cm; text-indent: 0; tab-stops: right dotted 16.8cm; }
    p.toc-l3 { font-weight: normal; margin-left: 1.5cm; text-indent: 0; tab-stops: right dotted 16.8cm; }
    .toc-tab { mso-tab-count: 1 dotted; }

    /* ===== TIỆN ÍCH ===== */
    ul, ol { margin-top: 5px; margin-bottom: 10px; padding-left: 20px; }
    li { margin-bottom: 4px; }
    p { margin-top: 0; margin-bottom: 8px; text-align: justify; }
    .page-break { page-break-before: always; mso-page-break-before: always; }
    .code-block { font-family: 'Courier New', Courier, monospace; background-color: #f4f4f4; border: 1px solid #ddd; padding: 12px; white-space: pre-wrap; font-size: 10pt; margin-top: 5px; margin-bottom: 10px; line-height: 1.2; }
    .alert-box { background-color: #fce4d6; border-left: 6px solid #ed7d31; padding: 10px; margin-top: 10px; margin-bottom: 10px; }
    .error-inline { color: #c00000; font-size: 10pt; font-style: italic; font-weight: bold; margin-top: 3px; }
    .success-inline { color: #385723; font-size: 10pt; font-weight: bold; }
    .diagram-img { max-width: 100%; height: auto; display: block; margin: 15px auto; border: 1px solid #ccc; padding: 5px; background: #fff; }
    .note-box { background-color: #fcf8e3; border: 1px solid #faebcc; color: #8a6d3b; padding: 12px; margin-bottom: 15px; border-radius: 4px; }
    .figma-comment { background-color: #e2f0d9; border: 1px solid #a9d08e; color: #375623; padding: 10px; font-size: 10.5pt; margin-bottom: 10px; }
</style>
</head>
<body>

<!-- ⚠️ BẮT BUỘC: bọc toàn bộ thân tài liệu trong div.Section1 để áp footer đánh số trang -->
<div class="Section1">

<!-- ============================================================ -->
<!-- TRANG BÌA (chuẩn URD)                                         -->
<!-- Ghi chú:                                                      -->
<!--  - Logo nhúng base64, kích thước 110×39px (≈3cm×1cm)          -->
<!--  - Dùng width/height px thay cm — Word HTML bỏ qua đơn vị cm  -->
<!--  - table-layout:fixed + max-width ô logo để logo không giãn   -->
<!--  - Revision History nằm trên trang bìa (KHÔNG tách thành h2)  -->
<!-- ============================================================ -->

<!-- Bảng 1: Header tài liệu -->
<table style="width:100%; border-collapse:collapse; border:2px solid #000000; margin:0; table-layout:fixed;">
    <tr>
        <td style="border-right:1.5px solid #000000; border-bottom:1.5px solid #000000; padding:12px 16px; width:120px; max-width:120px; overflow:hidden; text-align:center; vertical-align:middle;">
            <!-- Thay [LOGO_BASE64] bằng chuỗi data:image/png;base64,... -->
            <!-- Lệnh lấy base64: python3 -c "import base64; print('data:image/png;base64,'+base64.b64encode(open('docs/images/logoftel.png','rb').read()).decode())" -->
            <img src="[LOGO_BASE64]" width="110" height="39" style="width:110px; height:39px; max-width:110px; display:block; margin:auto;" alt="FPT Telecom">
        </td>
        <td style="border-bottom:1.5px solid #000000; padding:20px 24px; text-align:center; vertical-align:middle;">
            <div style="font-family:'Arial', sans-serif; font-size:16pt; font-weight:bold; color:#000000; text-transform:uppercase; line-height:1.35;">FPT.VN URD &ndash; USER REQUIREMENTS DOCUMENT</div>
        </td>
    </tr>
    <tr>
        <td colspan="2" style="padding:10px 20px;">
            <span style="font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold;">Mã hiệu:</span>
            <span style="font-family:'Times New Roman', serif; font-size:11pt;"> FPT-URD-[MODULE]-[SỐ]-01</span>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <span style="font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold;">Phiên bản:</span>
            <span style="font-family:'Times New Roman', serif; font-size:11pt;"> V1.0</span>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <span style="font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold;">Ngày:</span>
            <span style="font-family:'Times New Roman', serif; font-size:11pt;"> [DD/MM/YYYY]</span>
        </td>
    </tr>
</table>

<!-- Bảng 2: Revision History — cách bảng header 2cm -->
<div style="margin-top:2cm;">
    <p style="font-family:'Arial', sans-serif; font-size:13pt; font-weight:bold; color:#1f4e78; margin:0 0 4px 0; text-transform:uppercase; letter-spacing:0.5px;">Revision History</p>
    <hr style="border:none; border-top:1.5px solid #1f4e78; margin:0 0 10px 0;">
    <p style="font-family:'Times New Roman', serif; font-size:10pt; font-style:italic; color:#333333; margin:0 0 10px 0;">
        [A]: Add &ndash; <u>Thêm mới</u> &nbsp;|&nbsp; [U]: Update &ndash; <u>Cập nhật, thay đổi</u> &nbsp;|&nbsp; [D]: Delete &ndash; <u>Xóa</u>
    </p>
    <table style="width:100%; border-collapse:collapse; table-layout:fixed;">
        <thead>
            <tr>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center; width:90px;">Date</th>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center; width:75px;">Version</th>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center; width:110px;">Author</th>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center; width:110px;">Reviewer</th>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center; width:110px;">Approver</th>
                <th style="border:1px solid #000000; padding:8px 10px; font-family:'Arial', sans-serif; font-size:11pt; font-weight:bold; background-color:#dae3f3; text-align:center;">Change Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt; text-align:center;">[DD/MM/YYYY]</td>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt; text-align:center;">V1.0</td>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt; text-align:center;">[Tên tác giả]</td>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt; text-align:center;">[Reviewer]</td>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt; text-align:center;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:8px 10px; font-family:'Times New Roman', serif; font-size:11pt;">[A] Khởi tạo tài liệu URD [Tên hệ thống]</td>
            </tr>
            <tr>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
                <td style="border:1px solid #000000; padding:20px 10px;">&nbsp;</td>
            </tr>
        </tbody>
    </table>
</div>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<!-- ============================================================ -->
<!-- PHÊ DUYỆT TÀI LIỆU (Document Sign-off) — chuẩn URD           -->
<!-- ============================================================ -->
<h2>PHÊ DUYỆT TÀI LIỆU (DOCUMENT SIGN-OFF)</h2>
<p><em>Tài liệu chỉ có hiệu lực làm cơ sở triển khai sau khi được các bên liên quan rà soát và phê duyệt đầy đủ.</em></p>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 22%;">Vai trò</th>
            <th style="width: 22%;">Họ và tên</th>
            <th style="width: 26%;">Chức danh / Bộ phận</th>
            <th style="width: 13%; text-align: center;">Ngày</th>
            <th style="width: 17%; text-align: center;">Chữ ký</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>Người lập</strong> (Prepared by)</td><td>[Tên tác giả]</td><td>Business Analyst</td><td style="text-align: center;">[DD/MM/YYYY]</td><td>&nbsp;</td></tr>
        <tr><td><strong>Người rà soát</strong> (Reviewed by)</td><td>&nbsp;</td><td>Product Owner</td><td style="text-align: center;">&nbsp;</td><td>&nbsp;</td></tr>
        <tr><td><strong>Người phê duyệt</strong> (Approved by)</td><td>&nbsp;</td><td>Trưởng bộ phận Sản phẩm / QLCS</td><td style="text-align: center;">&nbsp;</td><td>&nbsp;</td></tr>
    </tbody>
</table>

<!-- ============================================================ -->
<!-- MỤC LỤC — class toc-title đã có page-break-before: always   -->
<!-- ⚠️ Dùng paragraph + tab leader kiểu Word Classic:
     - Level 1 sát lề, bold
     - Level 2 thụt 0.75cm
     - Level 3 thụt 1.5cm
     - Tất cả level dùng cùng tab stop phải 16.8cm để số trang thẳng cột
     - Dòng dài được phép xuống dòng để không tràn viền
     Render bản A4 bằng Word rồi thay "X" bằng số trang thực.             -->
<!-- ============================================================ -->
<div class="toc-title" style="page-break-before: always; mso-page-break-before: always;">MỤC LỤC</div>
<div class="toc-list">
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">A. GIỚI THIỆU<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Mục đích tài liệu<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Thông tin chung &amp; Hiện trạng (AS-IS vs TO-BE)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Thuật ngữ và viết tắt<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">B. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Sơ đồ luồng nghiệp vụ tổng quan (Flow Diagram)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Danh sách các chức năng chính<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Ma trận phân quyền sử dụng<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">C. ĐẶC TẢ CHI TIẾT CÁC CHỨC NĂNG NGHIỆP VỤ<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">I. [Luồng 1]<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Quy trình nghiệp vụ từng bước (Step-by-Step)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Quy tắc cấu hình &amp; Business Rules<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Mô tả giao diện &amp; Ràng buộc trường<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">II. [Luồng 2] (nếu có)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">III. Đặc tả điều kiện &amp; Edge Cases<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">IV. Bảng thông điệp báo lỗi (Error Messages)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">D. YÊU CẦU PHI CHỨC NĂNG<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">E. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO<span style="mso-tab-count:1 dotted">	</span>X</p>
</div>

<!-- ============================================================ -->
<!-- A. GIỚI THIỆU — h1 tự xuống trang do page-break-before       -->
<!-- ============================================================ -->
<h1>A. GIỚI THIỆU</h1>

<h3>1. Mục đích tài liệu</h3>
<p>Tài liệu này đặc tả các yêu cầu người dùng cuối đối với [Tên hệ thống/tính năng]. Tài liệu đóng vai trò làm cơ sở nghiệp vụ để đội ngũ phát triển Frontend (FE), Backend (BE), Quản lý chính sách (QLCS), Product Hub và đội ngũ Kiểm thử (QA/QC) xây dựng giải pháp kỹ thuật và kịch bản UAT.</p>

<h3>2. Thông tin chung &amp; Hiện trạng (AS-IS vs TO-BE)</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 8%; text-align: center;">STT</th>
            <th style="width: 25%;">Hạng mục</th>
            <th style="width: 67%;">Mô tả chi tiết</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">1</td>
            <td><b>Giới thiệu tổng quan</b></td>
            <td>[Mô tả ngắn gọn bối cảnh dự án, tính năng mới hoặc hệ thống sắp xây dựng]</td>
        </tr>
        <tr>
            <td style="text-align: center;">2</td>
            <td><b>Hiện trạng (AS-IS)</b></td>
            <td>[Mô tả quy trình hiện tại, bất cập cần giải quyết]</td>
        </tr>
        <tr>
            <td style="text-align: center;">3</td>
            <td><b>Mục tiêu (TO-BE)</b></td>
            <td>[Mục tiêu cụ thể, KPI hoặc hiệu quả mong muốn sau triển khai]</td>
        </tr>
        <tr>
            <td style="text-align: center;">4</td>
            <td><b>Phạm vi triển khai</b></td>
            <td><b>Kỹ thuật:</b> [Web / App / Backend / CMS...]<br><b>Nghiệp vụ:</b> [Các luồng quy trình được bao phủ]<br><b>Tổ chức:</b> [Phòng ban, đối tượng người dùng]</td>
        </tr>
    </tbody>
</table>

<h3>3. Thuật ngữ và viết tắt</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 8%; text-align: center;">STT</th>
            <th style="width: 15%;">Thuật ngữ</th>
            <th style="width: 30%;">Tên đầy đủ</th>
            <th style="width: 47%;">Mô tả ý nghĩa</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="text-align: center;">1</td><td>URD</td><td>User Requirements Document</td><td>Tài liệu yêu cầu người dùng</td></tr>
        <tr><td style="text-align: center;">2</td><td>SKU</td><td>Stock Keeping Unit</td><td>Đơn vị phân loại hàng hóa/dịch vụ</td></tr>
        <tr><td style="text-align: center;">3</td><td>COD</td><td>Cash On Delivery</td><td>Thanh toán trực tiếp khi nhận hàng</td></tr>
        <tr><td style="text-align: center;">4</td><td>PTTT</td><td>Phương Thức Thanh Toán</td><td>Hình thức thanh toán KH lựa chọn</td></tr>
        <tr><td style="text-align: center;">5</td><td>BE</td><td>Backend</td><td>Hệ thống xử lý logic phía máy chủ</td></tr>
        <tr><td style="text-align: center;">6</td><td>FE</td><td>Frontend</td><td>Giao diện hiển thị phía người dùng</td></tr>
        <tr><td style="text-align: center;">7</td><td>SPF</td><td>Hệ thống Phê duyệt &amp; Quản lý đơn hàng FPT</td><td>Hệ thống tạo &amp; quản lý đơn hàng nội bộ</td></tr>
        <tr><td style="text-align: center;">8</td><td>[Thuật ngữ]</td><td>[Tên đầy đủ]</td><td>[Giải thích]</td></tr>
    </tbody>
</table>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<!-- ============================================================ -->
<!-- B. TỔNG QUAN HỆ THỐNG                                        -->
<!-- ============================================================ -->
<h1>B. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI</h1>

<h3>1. Sơ đồ luồng nghiệp vụ tổng quan (BPMN)</h3>
<!-- ⚠️ KHÔNG đặt text/bullet mô tả TRƯỚC <img>. Sơ đồ đặt ngay sau heading.   -->
<!-- Sơ đồ phải theo CHUẨN BPMN: swimlane/pool theo tác nhân; Start/End Event   -->
<!-- là vòng tròn (mảnh/đậm); Task = chữ nhật bo góc; Exclusive Gateway = hình  -->
<!-- thoi gắn ký hiệu ×; Text Annotation = khối nét đứt gắn mã [MODULE-BR-xx];  -->
<!-- Sequence Flow = mũi tên liền, luồng quay lui = mũi tên nét đứt.            -->
<!-- Cách tạo: viết generator SVG (3 lane dọc KH/FE/BE) → rsvg-convert -z 2     -->
<!-- → PNG → nhúng base64 (xem PHẦN 5).                                         -->
<img src="[ĐƯỜNG_DẪN_HOẶC_BASE64]" class="diagram-img" alt="Sơ đồ BPMN [Tên hệ thống]">
<div class="note-box">
    <strong>Cách đọc sơ đồ (BPMN):</strong> Sơ đồ dùng [N] làn trách nhiệm (swimlane): <strong>Khách hàng</strong> – thao tác trên giao diện; <strong>Website/Frontend</strong> – hiển thị &amp; điều phối; <strong>Backend &amp; Tích hợp</strong> – xử lý nghiệp vụ &amp; tích hợp hệ thống. Ký hiệu: vòng tròn mảnh = Start Event; vòng tròn đậm = End Event; chữ nhật bo góc = Task; hình thoi × = Exclusive Gateway; khối nét đứt = chú thích Business Rule; mũi tên liền = luồng tuần tự; mũi tên nét đứt = luồng quay lui.
</div>
<p><b>Nguyên tắc vận hành xuyên suốt:</b></p>
<ul>
    <li>[Nguyên tắc 1 — Ví dụ: BE xử lý toàn bộ tính toán, FE chỉ nhận kết quả và hiển thị real-time]</li>
    <li>[Nguyên tắc 2 — Ví dụ: Mọi ngưỡng cấu hình (giá, phí, giới hạn SL, PTTT...) nạp động từ QLCS/Product Hub, không hardcode trên FE]</li>
    <li>[Nguyên tắc 3 — Ví dụ: Mọi thay đổi điều kiện đơn hàng trigger re-validate tự động]</li>
</ul>

<h3>2. Danh sách các chức năng chính</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 8%; text-align: center;">STT</th>
            <th style="width: 25%;">Module / Chức năng</th>
            <th style="width: 12%; text-align: center;">Phiên bản</th>
            <th style="width: 15%; text-align: center;">Phân loại</th>
            <th style="width: 40%;">Mô tả tóm tắt hành vi hệ thống</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">1</td>
            <td>[Tên chức năng 1]</td>
            <td style="text-align: center;">1.0</td>
            <td style="text-align: center;">Thêm mới</td>
            <td>[Mô tả ngắn chức năng 1]</td>
        </tr>
        <tr>
            <td style="text-align: center;">2</td>
            <td>[Tên chức năng 2]</td>
            <td style="text-align: center;">1.0</td>
            <td style="text-align: center;">Thêm mới</td>
            <td>[Mô tả ngắn chức năng 2]</td>
        </tr>
    </tbody>
</table>

<h3>3. Ma trận phân quyền sử dụng</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 8%; text-align: center;">STT</th>
            <th style="width: 42%;">Chức năng / Module</th>
            <th style="width: 15%; text-align: center;">Khách hàng</th>
            <th style="width: 15%; text-align: center;">Admin QLCS</th>
            <th style="width: 20%;">Ghi chú</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">1</td>
            <td>[Tên chức năng]</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td>[Ghi chú]</td>
        </tr>
        <tr>
            <td style="text-align: center;">2</td>
            <td>[Cấu hình hệ thống]</td>
            <td style="text-align: center; color: red; font-weight: bold;">Không</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td>Admin cấu hình tại Product Hub / QLCS</td>
        </tr>
    </tbody>
</table>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<!-- ============================================================ -->
<!-- C. ĐẶC TẢ CHI TIẾT CÁC CHỨC NĂNG NGHIỆP VỤ                  -->
<!-- ============================================================ -->
<h1>C. ĐẶC TẢ CHI TIẾT CÁC CHỨC NĂNG NGHIỆP VỤ</h1>

<h2>I. [TÊN LUỒNG 1]</h2>

<h3>1. Quy trình nghiệp vụ từng bước (Step-by-Step)</h3>
<table class="usecase-table">
    <tr>
        <td class="label">Tác nhân tham gia</td>
        <td>[Ví dụ: Khách hàng (Cá nhân/Doanh nghiệp) mua sắm trên FPT.vn]</td>
    </tr>
    <tr>
        <td class="label">Điều kiện bắt đầu (Pre-conditions)</td>
        <td>[Ví dụ: Khách hàng đã chọn gói dịch vụ và chuyển tới trang Checkout]</td>
    </tr>
    <tr>
        <td class="label">Luồng xử lý chính</td>
        <td>
            <b>Bước 1: [Tên bước]</b>
            <br>- [Mô tả hành động KH]
            <br>- [Mô tả phản hồi hệ thống]
            <br>
            <b>Bước 2: [Tên bước]</b>
            <br>- [Mô tả hành động KH]
            <br>- [Mô tả phản hồi hệ thống]
            <br>
            <!-- Thêm bước theo từng luồng -->
        </td>
    </tr>
    <tr>
        <td class="label">Điều kiện kết thúc (Post-conditions)</td>
        <td>[Ví dụ: Đơn hàng tạo thành công trên SPF, KH nhận xác nhận qua SMS/Email]</td>
    </tr>
    <tr>
        <td class="label">Luồng thay thế / Ngoại lệ</td>
        <td>
            <b>Alt 1: [Tên ngoại lệ]</b><br>
            [Điều kiện xảy ra] → [Hành vi hệ thống / thông báo hiển thị]
            <br><br>
            <b>Alt 2: [Tên ngoại lệ]</b><br>
            [Điều kiện xảy ra] → [Hành vi hệ thống / thông báo hiển thị]
        </td>
    </tr>
</table>

<h3>2. Quy tắc cấu hình từ Product Hub và Quản lý chính sách</h3>
<div class="alert-box">
    <b>[[MODULE]-BR-01] [Tên Business Rule]:</b>
    <br>- [Mô tả quy tắc 1]
    <br>- [Mô tả quy tắc 2]
</div>
<div class="alert-box">
    <b>[[MODULE]-BR-02] [Tên Business Rule]:</b>
    <br>- [Mô tả quy tắc]
</div>

<h3>3. Mô tả giao diện &amp; Ràng buộc trường (Screen Description)</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 8%; text-align: center;">STT</th>
            <th style="width: 20%;">Field / Element</th>
            <th style="width: 15%;">Kiểu dữ liệu</th>
            <th style="width: 25%;">Ràng buộc / Validation</th>
            <th style="width: 32%;">Thao tác &amp; Phản hồi hệ thống</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">1</td>
            <td><b>[Tên field]</b></td>
            <td>Textbox / Dropdown / Checkbox...</td>
            <td>- Bắt buộc (Required)<br>- [Ràng buộc khác]</td>
            <td>- KH: [Hành động]<br>- Hệ thống: [Phản hồi]</td>
        </tr>
    </tbody>
</table>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<h2>II. [TÊN LUỒNG 2] (nếu có)</h2>
<!-- Lặp lại cấu trúc như Luồng I -->

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<h2>III. ĐẶC TẢ CÁC ĐIỀU KIỆN VÀ EDGE CASES</h2>

<!-- ✅ PATTERN CHO EDGE CASE: Mỗi case gồm (1) mô tả tổng quan + (2) bảng chi tiết -->
<div class="alert-box">
    <b>[[MODULE]-CASE-BR-00] Tổng hợp các trường hợp ngoại lệ:</b>
    <br><b>Case 1 — [Tên case]:</b> [Mô tả ngắn gọn điều kiện và hành vi]
    <br><b>Case 2 — [Tên case]:</b> [Mô tả ngắn gọn điều kiện và hành vi]
    <br><b>Case 3 — [Tên case]:</b> [Mô tả ngắn gọn điều kiện và hành vi]
</div>

<h3>Chi tiết Case 1: [Tên]</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 25%;">Điều kiện xảy ra</th>
            <th style="width: 35%;">Hành vi hiển thị</th>
            <th style="width: 20%;">Message hiển thị</th>
            <th style="width: 20%;">Hành động KH</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[Điều kiện]</td>
            <td>[Mô tả hành vi UI]</td>
            <td style="color: #c00000; font-style: italic; font-weight: bold;">[Text thông báo chính xác]</td>
            <td>[KH có thể làm gì tiếp theo]</td>
        </tr>
    </tbody>
</table>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<h2>IV. BẢNG THÔNG ĐIỆP BÁO LỖI (ERROR MESSAGES)</h2>
<p>Bảng quy định chính xác nội dung thông điệp hệ thống hiển thị cho KH trong từng trường hợp:</p>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 25%;">Trường Hợp Nghiệp Vụ</th>
            <th style="width: 15%;">Trạng Thái</th>
            <th style="width: 40%;">Nội dung Message hiển thị chính xác</th>
            <th style="width: 20%;">Hành vi Hệ thống &amp; Giao diện</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>TH1: [Tên trường hợp]</b><br>([Mô tả ngắn điều kiện xảy ra])</td>
            <td style="color: green; font-weight: bold;">Thành công</td>
            <td style="color: #385723; font-weight: bold;">[Text thông báo thành công chính xác]</td>
            <td>[Hành vi UI sau thành công]</td>
        </tr>
        <tr>
            <td></td>
            <td style="color: red; font-weight: bold;">Thất bại</td>
            <td style="color: #c00000; font-style: italic; font-weight: bold;">[Text thông báo lỗi chính xác]</td>
            <td>[Hành vi UI sau lỗi]</td>
        </tr>
    </tbody>
</table>

<!-- ============================================================ -->
<!-- D. YÊU CẦU PHI CHỨC NĂNG                                     -->
<!-- ============================================================ -->
<h1>D. YÊU CẦU PHI CHỨC NĂNG</h1>

<h3>1. Hiệu năng hệ thống (Performance)</h3>
<ul>
    <li><b>Tốc độ xử lý tính toán:</b> Thời gian Backend nhận dữ liệu, validate và phản hồi kết quả cho Frontend không được vượt quá <b>0.5 giây</b> trong điều kiện mạng bình thường.</li>
    <li><b>Tự động đồng bộ:</b> Trạng thái [đối tượng] phải được cập nhật thời gian thực ngay khi giao dịch hoàn tất, tránh sử dụng lại dữ liệu cũ.</li>
    <li><b>Tải đồng thời:</b> Hệ thống đáp ứng tối thiểu [1.000] giao dịch đồng thời không bị nghẽn.</li>
</ul>

<h3>2. Thiết kế trải nghiệm người dùng (UI/UX)</h3>
<ul>
    <li><b>Responsive Design:</b> Giao diện phải hiển thị hoàn hảo trên cả Desktop (Web) và Mobile (Responsive/App). Nút bấm và popup đảm bảo thao tác ngón tay trên điện thoại.</li>
    <li><b>Thông báo lỗi cụ thể:</b> Mọi thông báo lỗi phải nêu <b>cụ thể điều kiện</b> không đáp ứng, không dùng message generic. KH phải biết cần thay đổi gì để tiếp tục.</li>
    <li><b>Cấu hình động:</b> Toàn bộ text nhỏ dưới gói cước, thông tin hiển thị trong popup, và các điều kiện áp dụng đều được cấu hình từ Product Hub — không hardcode trên FE.</li>
    <li><b>Phản hồi tức thì:</b> Các kiểm tra có thể thực hiện phía client (định dạng số điện thoại, điều kiện loại trừ...) phải được xử lý real-time, không chờ submit.</li>
</ul>

<h3>3. Bảo mật &amp; An toàn thông tin (Security)</h3>
<ul>
    <li><b>Mã hóa thông tin:</b> Mọi dữ liệu truyền tải trong luồng thanh toán phải được mã hóa qua HTTPS (TLS 1.3).</li>
    <li><b>Che dấu dữ liệu nhạy cảm:</b> Số điện thoại hiển thị dạng masking (VD: <code>098***1234</code>). Thông tin thẻ không lưu tại DB hệ thống, ủy quyền cho cổng thanh toán PCI-DSS.</li>
</ul>

<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>

<!-- ============================================================ -->
<!-- E. PHỤ LỤC                                                   -->
<!-- ============================================================ -->
<h1>E. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO</h1>
<ul>
    <li>Tài liệu thiết kế UI/UX (Figma): [Chèn link Figma tại đây]</li>
    <li>Tài liệu đặc tả API tích hợp: [Chèn link tài liệu API]</li>
    <li>Sơ đồ BPMN: [Đường dẫn file diagrams/...]</li>
    <li>[Tài liệu tham khảo khác]</li>
</ul>

<!-- ============================================================ -->
<!-- FOOTER ĐÁNH SỐ TRANG (MS WORD) — field PAGE / NUMPAGES        -->
<!-- Đặt ở CUỐI, BÊN TRONG div.Section1. Word tự render số trang;  -->
<!-- Chrome bỏ qua phần trong <!--[if supportFields]-->.          -->
<!-- ============================================================ -->
<div style='mso-element:footer' id="f1">
    <p class="MsoFooter" align="center" style="text-align:center; font-family:'Times New Roman', serif; font-size:9pt; color:#666666;">
        Trang <!--[if supportFields]><span style='mso-element:field-begin'></span><span style='mso-spacerun:yes'> </span>PAGE <span style='mso-element:field-separator'></span><![endif]--><span>1</span><!--[if supportFields]><span style='mso-element:field-end'></span><![endif]--> / <!--[if supportFields]><span style='mso-element:field-begin'></span><span style='mso-spacerun:yes'> </span>NUMPAGES <span style='mso-element:field-separator'></span><![endif]--><span>1</span><!--[if supportFields]><span style='mso-element:field-end'></span><![endif]-->&nbsp;&nbsp;|&nbsp;&nbsp;FPT-URD-[MODULE]-[SỐ THỨ TỰ]-01 &middot; [VERSION]
    </p>
</div>

</div><!-- /Section1 -->

</body>
</html>
```

---

## PHẦN 2 — CHECKLIST TRƯỚC KHI SUBMIT URD

### ✅ Trang bìa (chuẩn URD)
- [ ] **Bảng 1** — Header: Logo FPT (ô trái, `width:120px`) | Tiêu đề "FPT.VN URD – USER REQUIREMENTS DOCUMENT" (ô phải, in hoa); Row 2: Mã hiệu · Phiên bản · Ngày inline
- [ ] Logo nhúng **base64 Data URI**, kích thước **`width="110" height="39"`** (px, không dùng cm — Word bỏ qua cm); `table-layout:fixed` + `max-width:120px` trên ô logo
- [ ] **Bảng 2** — Revision History: tiêu đề "REVISION HISTORY" màu `#1f4e78`, đường kẻ ngang, chú thích `[A]/[U]/[D]`, bảng 6 cột (Date · Version · Author · Reviewer · Approver · Change Description), header nền `#dae3f3`
- [ ] ⚠️ **Phiên bản ở Bảng 1 = phiên bản mới nhất trong Bảng 2** (đồng bộ, không lệch)
- [ ] Cách 2 bảng **2cm** (`margin-top:2cm` trên div bọc Bảng 2)
- [ ] Kết thúc trang bìa bằng `<div style="page-break-before: always;">&nbsp;</div>`

### ✅ Phê duyệt tài liệu (Sign-off)
- [ ] Có bảng **PHÊ DUYỆT TÀI LIỆU** ngay sau bìa: Người lập / Người rà soát / Người phê duyệt (Vai trò · Họ tên · Chức danh · Ngày · Chữ ký)

### ✅ Đánh số trang (MS Word)
- [ ] Toàn bộ thân tài liệu bọc trong `<div class="Section1">`
- [ ] Có `@page Section1 { mso-footer: f1; }` + `<div id="f1" style="mso-element:footer">` với field `PAGE`/`NUMPAGES`
- [ ] Footer hiển thị "Trang X / Y | Mã hiệu · Version"

### ✅ Page Break
- [ ] MỤC LỤC xuống trang mới (class `toc-title` đã có `page-break-before: always`)
- [ ] Mỗi `<h1>` (A, B, C, D, E...) xuống trang mới (CSS `h1` đã có `page-break-before: always`)
- [ ] Dùng `<div style="page-break-before: always; mso-page-break-before: always;">&nbsp;</div>` trước các `<h2>` phân luồng lớn (I, II, III, IV)

### ✅ Mục lục (TOC)
- [ ] **Điền số trang thực** vào ký tự `X` cuối từng dòng `<p class="toc-entry ...">` sau `<span style="mso-tab-count:1 dotted">	</span>` — render bản A4 bằng Word rồi dò trang từng heading. KHÔNG để "X"/"—"
- [ ] Số trang khớp với các đầu mục đã ép page-break

### ✅ Sơ đồ BPMN (thay flowchart cũ)
- [ ] Theo **chuẩn BPMN**: swimlane/pool theo tác nhân (KH / FE / BE & Tích hợp)
- [ ] **Start Event** = vòng tròn mảnh; **End Event** = vòng tròn đậm
- [ ] **Task** = chữ nhật bo góc; **Exclusive Gateway** = hình thoi gắn ký hiệu **×**
- [ ] **Text Annotation** = khối nét đứt gắn mã `[MODULE-BR-xx]`; **Sequence Flow** liền, luồng quay lui nét đứt
- [ ] ⚠️ KHÔNG đặt text/bullet TRƯỚC `<img>`; ghi chú "cách đọc" + nguyên tắc vận hành đặt SAU ảnh
- [ ] Lưu nguồn tại `diagrams/[tên_flow].svg` + PNG `@2x`, nhúng base64 bằng `<img class="diagram-img">` (xem PHẦN 5)

### ✅ Luồng nghiệp vụ
- [ ] Góc nhìn **Customer Journey** — KH làm gì, KH thấy gì
- [ ] Quy tắc hệ thống viết dưới dạng **note/BR** không phải step chính
- [ ] Có đầy đủ: Pre-conditions, Luồng chính, Post-conditions, Luồng ngoại lệ (Alt)
- [ ] Các ngưỡng cấu hình (giá, **biểu phí**, **giới hạn SL**, **PTTT**, bậc dịch vụ...) ghi rõ **do QLCS/Product Hub khai báo động**, không hardcode; không gài chương trình ưu đãi/khuyến mãi nếu thực tế chưa có

### ✅ Edge Cases & Error Messages
- [ ] Mỗi case có: điều kiện xảy ra, hành vi UI, message chính xác, hướng dẫn KH
- [ ] Message lỗi **cụ thể** theo loại điều kiện (ERR_PTTT, ERR_SKU...) — không generic
- [ ] Message thành công viết màu xanh lá (`success-inline`)
- [ ] Message lỗi viết màu đỏ (`error-inline`)

### ✅ Business Rules & Revision History
- [ ] Mã BR **liên tục, không gãy số** (BR-01 → BR-0n); cập nhật mọi cross-reference khi thêm/xóa rule
- [ ] Cập nhật version + ngày + tác giả + mô tả chi tiết thay đổi sau mỗi lần sửa

---

## PHẦN 3 — LỆNH LẤY BASE64 LOGO

```bash
# Chạy trong thư mục project để lấy base64 của logo
python3 -c "
import base64
with open('docs/images/logoftel.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
print('data:image/png;base64,' + b64)
"
```

> Copy toàn bộ chuỗi output (bắt đầu bằng `data:image/png;base64,...`) vào thuộc tính `src` của thẻ `<img>` trong trang bìa.

---

## PHẦN 4 — CHUẨN CANH CHỈNH CỘT BẢNG (% WIDTH)

> **Nguyên tắc cốt lõi:** Cột chứa **nội dung mô tả / chi tiết** luôn chiếm tỷ lệ lớn nhất. Cột ID/Code/Flag giữ nhỏ để nhường không gian cho dữ liệu thực chất.

### Quy tắc chung
- Dùng **`%` (phần trăm)** thay vì `px` cứng để bảng co giãn đúng trong Word và trình duyệt
- Tổng các cột phải bằng **100%**
- `table-layout: auto` kết hợp `%` = Word tự điều chỉnh theo tỷ lệ
- Cột cuối cùng (detail) có thể để `auto` hoặc đặt % lớn nhất

### Bảng tỷ lệ chuẩn theo từng loại bảng

#### 1. Revision History (Lịch sử thay đổi)
```html
<th style="width: 9%;">Ngày</th>           <!-- Ngắn: DD/MM/YYYY -->
<th style="width: 6%; text-align:center">Ver.</th>   <!-- Ngắn: V1.0 -->
<th style="width: 12%;">Tác giả</th>       <!-- Vừa: Tên người -->
<th style="width: 7%; text-align:center">HĐ</th>     <!-- Ngắn: [A]/[U] -->
<th style="width: 18%;">Mô tả chung</th>   <!-- Vừa -->
<th style="width: 48%;">Nội dung chi tiết</th> <!-- ★ LỚN NHẤT -->
```

#### 2. Thông tin chung / Giới thiệu (3 cột)
```html
<th style="width: 5%; text-align:center">STT</th>   <!-- Nhỏ -->
<th style="width: 22%;">Hạng mục</th>               <!-- Vừa -->
<th style="width: 73%;">Mô tả chi tiết</th>         <!-- ★ LỚN NHẤT -->
```

#### 3. Thuật ngữ / Định nghĩa (4 cột)
```html
<th style="width: 5%; text-align:center">STT</th>   <!-- Nhỏ -->
<th style="width: 13%;">Thuật ngữ</th>              <!-- Vừa -->
<th style="width: 25%;">Nghĩa tiếng Anh</th>        <!-- Vừa -->
<th style="width: 57%;">Mô tả ý nghĩa</th>          <!-- ★ LỚN NHẤT -->
```

#### 4. Functional List / Danh sách chức năng (5 cột)
```html
<th style="width: 5%; text-align:center">STT</th>   <!-- Nhỏ -->
<th style="width: 25%;">Module / Chức năng</th>     <!-- Vừa -->
<th style="width: 7%; text-align:center">Ver.</th>  <!-- Nhỏ -->
<th style="width: 8%; text-align:center">Loại</th>  <!-- Nhỏ -->
<th style="width: 55%;">Mô tả hành vi hệ thống</th> <!-- ★ LỚN NHẤT -->
```

#### 5. Permission Matrix / Phân quyền (6 cột)
```html
<th style="width: 5%; text-align:center">STT</th>   <!-- Nhỏ -->
<th style="width: 55%;">Tên Chức năng / Module</th> <!-- ★ LỚN NHẤT -->
<th style="width: 10%; text-align:center">KH vãng lai</th>    <!-- Role -->
<th style="width: 10%; text-align:center">KH đăng nhập</th>   <!-- Role -->
<th style="width: 10%; text-align:center">Telesales/CSKH</th> <!-- Role -->
<th style="width: 10%; text-align:center">Admin (CMS)</th>    <!-- Role -->
```

#### 6. Cart Items / Sản phẩm giỏ hàng (6 cột)
```html
<th style="width: 4%; text-align:center">Chọn</th>          <!-- Checkbox -->
<th style="width: 40%;">Tên sản phẩm & Đặc tính DV</th>    <!-- ★ LỚN NHẤT -->
<th style="width: 13%; text-align:center">Đơn giá TB</th>   <!-- Số tiền -->
<th style="width: 12%; text-align:center">Giá Cloud</th>    <!-- Số tiền -->
<th style="width: 7%; text-align:center">SL</th>            <!-- Số lượng -->
<th style="width: 14%; text-align:center">Thành tiền</th>   <!-- Tổng -->
```

#### 7. Business Rules / Quy tắc nghiệp vụ (3 cột)
```html
<th style="width: 12%; text-align:center">Mã Rule</th>      <!-- Ngắn: BR-01 -->
<th style="width: 22%;">Tên Quy tắc</th>                   <!-- Vừa -->
<th style="width: 66%;">Nội dung quy tắc & Logic hệ thống</th> <!-- ★ LỚN NHẤT -->
```

#### 8. Screen Description / Đặc tả màn hình (4 cột)
```html
<th style="width: 18%;">Phần tử giao diện</th>  <!-- Tên element -->
<th style="width: 13%;">Kiểu hiển thị</th>      <!-- Input/Button... -->
<th style="width: 8%; text-align:center">Bắt buộc</th> <!-- Y/N -->
<th style="width: 61%;">Mô tả hành vi, ràng buộc & UI/UX</th> <!-- ★ LỚN NHẤT -->
```

### Lưu ý khi tạo bảng mới
| Loại cột | Tỷ lệ gợi ý | Ví dụ |
|---|---|---|
| ID / STT / Mã code | 4–7% | STT, Mã Rule, Mã lỗi |
| Cột cờ (Flag/Status) | 6–10% | Bắt buộc, Loại, HĐ |
| Tên ngắn / Nhãn | 10–25% | Thuật ngữ, Module, Tác giả |
| Mô tả vừa | 20–30% | Tên Quy tắc, Hạng mục |
| **Mô tả chi tiết / Logic** | **40–73%** | Nội dung rule, Hành vi UI |


---

## PHẦN 5 — TẠO SƠ ĐỒ BPMN (SWIMLANE) & NHÚNG VÀO URD

> **Tại sao tự sinh SVG?** Flowchart tự do khó đạt chuẩn BPMN (thiếu pool/lane, event tròn, gateway có ký hiệu). Cách ổn định nhất: viết một generator sinh **SVG swimlane dọc** rồi convert sang PNG nét cao và nhúng base64.

### Quy ước ký hiệu BPMN bắt buộc
| Thành phần | Ký hiệu | Ghi chú |
|---|---|---|
| Start Event | Vòng tròn **mảnh** (xanh) | Điểm bắt đầu |
| End Event | Vòng tròn **đậm** (đỏ) | Mỗi kết cục một end riêng |
| Task / Activity | Chữ nhật **bo góc** | Một hành động |
| Exclusive Gateway | Hình **thoi** gắn ký hiệu **×** | Rẽ nhánh loại trừ (Yes/No) |
| Text Annotation | Khối **nét đứt** | Gắn mã `[MODULE-BR-xx]` cạnh bước liên quan |
| Sequence Flow | Mũi tên **liền** | Luồng tuần tự |
| Back / Retry flow | Mũi tên **nét đứt** | Quay về điều chỉnh / thử lại |
| Pool / Lane | Băng dọc có tiêu đề | 1 lane / tác nhân (KH · FE · BE & Tích hợp) |

### Quy trình 4 bước
```bash
# 1) Viết generator (Python sinh SVG): mỗi node gán (lane, row, kind, label).
#    Lane = cột dọc; row = bước thời gian; vẽ rect/circle/diamond + connector L.
python3 diagrams/gen_bpmn.py            # -> diagrams/[flow].svg

# 2) Convert SVG -> PNG @2x cho nét khi in (cần: brew install librsvg)
rsvg-convert -z 2 -o diagrams/[flow].png diagrams/[flow].svg

# 3) Nhúng base64 vào URD (thay đúng thẻ class="diagram-img")
python3 - <<'PY'
import re, base64
p='thuyttdoc/[urd_file].doc'; html=open(p,encoding='utf-8').read()
b64='data:image/png;base64,'+base64.b64encode(open('diagrams/[flow].png','rb').read()).decode()
html=re.sub(r'(<img src=")data:image/png;base64,[^"]*(" class="diagram-img")', r'\g<1>'+b64+r'\g<2>', html, count=1)
open(p,'w',encoding='utf-8').write(html)
PY

# 4) Verify: render .doc -> PDF, soi trang chứa sơ đồ
#    (macOS) /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
#      --headless=new --disable-gpu --print-to-pdf=out.pdf "file://$PWD/thuyttdoc/[urd_file].doc"
```

### Khung luồng tham chiếu (Checkout TMĐT FPT) — tái dùng & tinh chỉnh
- **Lane KH:** Bắt đầu → Chọn cấu hình trên PDP → Thêm giỏ → Điều chỉnh giỏ → Tiếp tục → Nhập SĐT → Chọn hình thức triển khai → Nhập địa chỉ/Voucher/PTTT → Xác nhận & Thanh toán → (End A / End B).
- **Lane FE:** Tạo/cập nhật dòng giỏ (tách dòng/combo) → Lưu & hiển thị giỏ → GW "Có ≥1 dòng chọn?" → Hiển thị Checkout → GW "Hình thức?" → Thank You (A/B).
- **Lane BE & Tích hợp:** Tra cứu hợp đồng CRM → GW (đề xuất liên kết) → GW "Thanh toán thành công?" → Tạo đơn SPF & đẩy cước.
- **Annotation gắn rule:** tách dòng `Line_Key = SKU + Loại Cloud + Chu kỳ`; lưu giỏ theo trạng thái đăng nhập; phí lắp đặt theo biểu phí QLCS (KHÔNG ưu đãi nếu chưa có chương trình); PTTT do QLCS khai báo (COD khóa ở vùng cấm giao vận).

### Lưu ý quan trọng
- **Lề & lane co giãn:** chừa lề trái/phải đủ cho Text Annotation, tránh tràn canvas.
- **Tiêu đề & chú giải (legend)** đặt riêng (đỉnh + đáy), không đè lên lane.
- File `.doc` (HTML-based) bị tool đọc nhầm là binary do dòng quá dài — chỉnh sửa bằng **Python (đọc/ghi UTF-8)**, không Read trực tiếp; mọi replace nên có `assert count == kỳ vọng`.

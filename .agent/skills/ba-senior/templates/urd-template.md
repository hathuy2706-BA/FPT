# URD TEMPLATE — TÀI LIỆU YÊU CẦU NGƯỜI DÙNG (FPT TELECOM CHUẨN)

> **Hướng dẫn sử dụng template này:**
> - File output là `.doc` (HTML-based, mở được bằng MS Word)
> - Thay toàn bộ `[PLACEHOLDER]` bằng nội dung thực tế
> - Logo: nhúng dạng base64 Data URI (`data:image/png;base64,...`) để tránh broken link khi mở trên máy khác
> - Mỗi đầu mục lớn (A, B, C, D, E, F) PHẢI xuống trang mới (`h1` đã có `page-break-before: always`)
> - Mỗi `h2` (luồng trong mục C) cũng PHẢI xuống trang mới (`h2` đã có `page-break-before: always`)
> - Sơ đồ flow: dùng skill `diagram-drawer`, xuất PNG nền trắng, nhúng bằng thẻ `<img class="diagram-img">` KHÔNG có border/padding
> - BR (Business Rules) viết dạng **bảng 3 cột** (Mã | Tên quy tắc | Nội dung), KHÔNG dùng alert-box
> - Mỗi luồng trong mục C gồm **4 phần cố định**: x.1 Đặc tả chi tiết · x.2 Quy tắc nghiệp vụ · x.3 Đặc tả giao diện · x.4 Edge cases & Mã lỗi

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

    /* ===== ĐÁNH SỐ TRANG (MS WORD) ===== */
    @page Section1 {
        size: 21.0cm 29.7cm;
        margin: 2.0cm 2.0cm 2.0cm 2.0cm;
        mso-header-margin: 1.0cm;
        mso-footer-margin: 1.0cm;
        mso-paper-source: 0;
        mso-footer: f1;
    }
    div.Section1 { page: Section1; }
    p.MsoFooter, p.MsoHeader { margin: 0; font-family: 'Times New Roman', serif; font-size: 9pt; color: #666666; }

    /* ===== TRANG BÌA ===== */
    .cover-container { border: 4px double #1f4e78; padding: 50px 40px; margin: 10px; min-height: 800px; position: relative; }
    .cover-logo { width: 4cm; height: 1.4cm; display: block; margin: 0; }
    .cover-badge { display: inline-block; border: 1.5px solid #c00000; color: #c00000; font-family: 'Arial', sans-serif; font-size: 9.5pt; font-weight: bold; letter-spacing: 0.5px; padding: 4px 12px; }
    .cover-org { font-family: 'Arial', sans-serif; color: #808080; font-size: 10.5pt; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 18px; }
    .cover-title-en { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 13pt; font-style: italic; margin-top: -6px; margin-bottom: 26px; }
    .cover-scope { font-family: 'Arial', sans-serif; color: #595959; font-size: 11pt; margin-top: 8px; }
    .cover-copyright { border-top: 1px solid #d0d0d0; margin-top: 28px; padding-top: 10px; text-align: center; font-family: 'Arial', sans-serif; font-size: 9pt; color: #808080; }
    .cover-title-box { text-align: center; margin-top: 40px; margin-bottom: 60px; }
    .cover-title-main { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 24pt; font-weight: bold; text-transform: uppercase; line-height: 1.4; margin-bottom: 20px; }
    .cover-title-sub { font-family: 'Arial', sans-serif; color: #e37222; font-size: 14pt; font-weight: bold; text-transform: uppercase; margin-top: 10px; letter-spacing: 0.5px; }
    .cover-meta-box { margin-top: 60px; width: 100%; border-top: 2px solid #1f4e78; padding-top: 20px; }
    .cover-meta-table { width: 100%; border-collapse: collapse; border: none; }
    .cover-meta-table td { border: none; padding: 6px 0; font-size: 11pt; color: #333333; }
    .cover-meta-label { font-weight: bold; color: #1f4e78; width: 140px; }

    /* ===== HEADINGS ===== */
    /* h1 và h2 đều có page-break-before để xuống trang mới */
    h1 { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 18pt; font-weight: bold; text-transform: uppercase; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #1f4e78; padding-bottom: 5px; page-break-before: always; mso-page-break-before: always; }
    h2 { font-family: 'Arial', sans-serif; color: #2e75b6; font-size: 14pt; font-weight: bold; margin-top: 24px; margin-bottom: 12px; border-bottom: 1px solid #2e75b6; padding-bottom: 3px; page-break-before: always; mso-page-break-before: always; }
    h3 { font-family: 'Arial', sans-serif; color: #5b9bd5; font-size: 12pt; font-weight: bold; margin-top: 18px; margin-bottom: 8px; }
    h4 { font-family: 'Arial', sans-serif; color: #000000; font-size: 12pt; font-weight: bold; margin-top: 14px; margin-bottom: 6px; }

    /* ===== BẢNG — ép co giãn đúng trong Word ===== */
    table { max-width: 100%; box-sizing: border-box; }
    th, td { box-sizing: border-box; word-wrap: break-word; overflow-wrap: anywhere; word-break: break-word; }
    table.data-table { border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 15px; table-layout: fixed; mso-table-layout-alt: fixed; word-wrap: break-word; }
    table.data-table th, table.data-table td { border: 1px solid #000000; padding: 6px 8px; text-align: left; vertical-align: top; font-size: 11pt; overflow-wrap: anywhere; word-break: break-word; }
    table.data-table th { background-color: #d9e1f2; font-weight: bold; color: #1f4e78; font-size: 10.5pt; }

    /* ===== BẢNG USE CASE ===== */
    table.usecase-table { border-collapse: collapse; width: 100%; margin-top: 8px; margin-bottom: 12px; table-layout: fixed; mso-table-layout-alt: fixed; }
    table.usecase-table td { border: 1px solid #000000; padding: 8px; vertical-align: top; font-size: 11pt; overflow-wrap: anywhere; word-break: break-word; }
    table.usecase-table td.label { background-color: #f2f2f2; font-weight: bold; width: 170px; }

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
    li { margin-bottom: 4px; overflow-wrap: anywhere; word-break: break-word; }
    p { margin-top: 0; margin-bottom: 8px; text-align: justify; overflow-wrap: anywhere; word-break: break-word; }
    .page-break { page-break-before: always; mso-page-break-before: always; }
    .alert-box { background-color: #fce4d6; border-left: 6px solid #ed7d31; padding: 10px; margin-top: 10px; margin-bottom: 10px; }
    .error-inline { color: #c00000; font-size: 10pt; font-style: italic; font-weight: bold; }
    .success-inline { color: #385723; font-size: 10pt; font-weight: bold; }
    /* diagram-img: KHÔNG có border, padding — kích thước cố định 16cm */
    .diagram-img { width: 16.0cm; height: auto; display: block; margin: 10px auto; border: none; padding: 0; background: #fff; mso-style-priority: 100; }
    .note-box { background-color: #fcf8e3; border: 1px solid #faebcc; color: #8a6d3b; padding: 12px; margin-bottom: 15px; }
    /* flow-band: nhãn loại luồng hiển thị đầu mỗi h2 luồng */
    .flow-band { background-color: #1f4e78; color: #ffffff; font-family: 'Arial', sans-serif; font-weight: bold; padding: 3px 8px; font-size: 10pt; border-radius: 3px; }
</style>
</head>
<body>

<!-- ⚠️ BẮT BUỘC: bọc toàn bộ thân tài liệu trong div.Section1 -->
<div class="Section1">

<!-- ============================================================ -->
<!-- TRANG BÌA                                                     -->
<!-- ============================================================ -->

<!-- Bảng 1: Header tài liệu -->
<table style="width:100%; border-collapse:collapse; border:2px solid #000000; margin:0; table-layout:fixed;">
    <tr>
        <td style="border-right:1.5px solid #000000; border-bottom:1.5px solid #000000; padding:12px 16px; width:120px; max-width:120px; overflow:hidden; text-align:center; vertical-align:middle;">
            <!-- Logo base64: python3 -c "import base64; print('data:image/png;base64,'+base64.b64encode(open('docs/images/logoftel.png','rb').read()).decode())" -->
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

<!-- ============================================================ -->
<!-- MỤC LỤC — class toc-title đã có page-break-before: always   -->
<!-- Điền số trang thực sau khi render bằng Word (thay "X")       -->
<!-- ============================================================ -->
<div class="toc-title" style="page-break-before: always; mso-page-break-before: always;">MỤC LỤC</div>
<div class="toc-list">
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">A. GIỚI THIỆU<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Mục đích tài liệu<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Thông tin chung &amp; Hiện trạng (AS-IS vs TO-BE)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Thuật ngữ và viết tắt<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">B. TỔNG QUAN HỆ THỐNG &amp; PHẠM VI<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Sơ đồ luồng nghiệp vụ tổng quan (BPMN)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Phân loại nhóm luồng &amp; sơ đồ luồng chính<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Danh sách chức năng &amp; Ma trận phân quyền<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">4. Đặc tả giao diện dùng chung &amp; trạng thái hệ thống<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">C. ĐẶC TẢ CHI TIẾT CÁC LUỒNG NGHIỆP VỤ<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. [Tên Luồng 1]<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1.1 Đặc tả chi tiết<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1.2 Quy tắc nghiệp vụ<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1.3 Đặc tả giao diện<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l3" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 1.5cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1.4 Edge cases &amp; Mã lỗi<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. [Tên Luồng 2] (nếu có)<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">D. TRƯỜNG HỢP LỖI &amp; THÔNG BÁO HỆ THỐNG<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">1. Nguyên tắc hiển thị lỗi &amp; retry<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">2. Trạng thái lỗi dùng chung<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l2" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:normal; margin:0 0 6px 0.75cm; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">3. Bảng mã lỗi dùng chung<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">E. YÊU CẦU PHI CHỨC NĂNG<span style="mso-tab-count:1 dotted">	</span>X</p>
    <p class="toc-entry toc-l1" style="font-family:'Times New Roman', Times, serif; font-size:12pt; font-weight:bold; margin:0 0 6px 0; line-height:1.25; text-align:left; tab-stops:right dotted 16.8cm;">F. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO<span style="mso-tab-count:1 dotted">	</span>X</p>
</div>

<!-- ============================================================ -->
<!-- A. GIỚI THIỆU                                                 -->
<!-- ============================================================ -->
<h1>A. GIỚI THIỆU</h1>

<h3>1. Mục đích tài liệu</h3>
<p>Tài liệu này đặc tả các yêu cầu người dùng cuối đối với <b>[Tên hệ thống/tính năng]</b> trên [Kênh: Website FPT.vn / App...]. [Mô tả ngắn phạm vi tài liệu — số luồng, loại sản phẩm/dịch vụ bao phủ].</p>
<p>Tài liệu làm cơ sở nghiệp vụ để FE, BE, QLCS, Product Hub và QA/QC xây dựng giải pháp kỹ thuật và kịch bản UAT. Mỗi luồng được trình bày như một <b>mục lớn tự chứa</b>, gồm 4 phần: đặc tả chi tiết, quy tắc nghiệp vụ, đặc tả giao diện &amp; ràng buộc trường, edge cases &amp; bảng mã lỗi.</p>

<h3>2. Thông tin chung &amp; Hiện trạng (AS-IS vs TO-BE)</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 5%; text-align: center;">STT</th>
            <th style="width: 22%;">Hạng mục</th>
            <th style="width: 73%;">Mô tả chi tiết</th>
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
            <th style="width: 5%; text-align: center;">STT</th>
            <th style="width: 14%;">Thuật ngữ</th>
            <th style="width: 26%;">Tên đầy đủ</th>
            <th style="width: 55%;">Mô tả ý nghĩa</th>
        </tr>
    </thead>
    <tbody>
        <tr><td style="text-align: center;">1</td><td>URD</td><td>User Requirements Document</td><td>Tài liệu yêu cầu người dùng</td></tr>
        <tr><td style="text-align: center;">2</td><td>SKU</td><td>Stock Keeping Unit (Thiết bị)</td><td>Sản phẩm thiết bị bán lẻ: Camera, Access Point, TV...</td></tr>
        <tr><td style="text-align: center;">3</td><td>SA</td><td>Dịch vụ (Service)</td><td>Sản phẩm dịch vụ: FPT Play, Cloud, Ultrafast...</td></tr>
        <tr><td style="text-align: center;">4</td><td>SPF</td><td>Hệ thống đơn hàng FPT</td><td>Hệ thống tạo &amp; quản lý đơn hàng nội bộ</td></tr>
        <tr><td style="text-align: center;">5</td><td>QLCS / Product Hub</td><td>Quản lý Chính sách / Trung tâm SP</td><td>Nguồn khai báo động giá, biểu phí, PTTT, chu kỳ, ưu đãi</td></tr>
        <tr><td style="text-align: center;">6</td><td>PTTT / COD</td><td>Phương thức thanh toán / Cash On Delivery</td><td>VietQR, Ví MoMo/ZaloPay, Thẻ ATM/Visa, COD (thu khi nhận)</td></tr>
        <tr><td style="text-align: center;">7</td><td>BE / FE</td><td>Backend / Frontend</td><td>Hệ thống xử lý server / Giao diện người dùng</td></tr>
        <tr><td style="text-align: center;">8</td><td>[Thuật ngữ]</td><td>[Tên đầy đủ]</td><td>[Giải thích]</td></tr>
    </tbody>
</table>

<!-- ============================================================ -->
<!-- B. TỔNG QUAN HỆ THỐNG & PHẠM VI                              -->
<!-- ============================================================ -->
<h1>B. TỔNG QUAN HỆ THỐNG &amp; PHẠM VI</h1>

<h3>1. Sơ đồ luồng nghiệp vụ tổng quan (BPMN)</h3>
<!-- ⚠️ KHÔNG đặt text/bullet TRƯỚC <img>. Sơ đồ đặt ngay sau heading.        -->
<!-- Chuẩn BPMN: swimlane/pool theo tác nhân; Start/End = vòng tròn mảnh/đậm;  -->
<!-- Task = chữ nhật bo góc; Exclusive Gateway = hình thoi ×;                   -->
<!-- Text Annotation = khối nét đứt; Sequence Flow = mũi tên liền.              -->
<div style="text-align:center; page-break-inside:avoid; margin:10px 0; overflow:hidden;">
<img class="diagram-img" width="605" height="493" style="width:16.0cm; height:auto; display:block; margin:0 auto; border:none; padding:0; mso-width-source:userset; mso-height-source:userset;" src="[LOGO_BASE64_DIAGRAM_TỔNG_QUAN]">
</div>
<div class="note-box">
    <strong>Cách đọc sơ đồ (BPMN):</strong> [N] làn trách nhiệm (swimlane): <strong>Khách hàng</strong> – thao tác giao diện; <strong>Website/Frontend</strong> – hiển thị &amp; điều phối; <strong>Backend &amp; Tích hợp</strong> – xử lý nghiệp vụ &amp; tích hợp SPF/CRM/Payment/Product Hub. Ký hiệu: vòng tròn mảnh = Start; vòng tròn đậm = End; chữ nhật bo góc = Task; hình thoi &times; = Exclusive Gateway; khối nét đứt = chú thích Business Rule; mũi tên liền = luồng tuần tự; mũi tên nét đứt = luồng quay lui.
</div>
<p><b>Nguyên tắc vận hành xuyên suốt (áp dụng cho mọi luồng tại Mục C):</b></p>
<ul>
    <li>BE xử lý toàn bộ tính toán (thành tiền, tạm tính, ưu đãi, cần thanh toán); FE chỉ nhận kết quả &amp; hiển thị real-time.</li>
    <li>Mọi ngưỡng cấu hình (giá, biểu phí, giới hạn SL, chu kỳ, PTTT, ưu đãi) nạp động từ QLCS / Product Hub — không hardcode FE; không gài ưu đãi nếu thực tế chưa khai báo.</li>
    <li>Mọi thay đổi điều kiện đơn (đổi chu kỳ/SL/thuộc tính, áp/huỷ ưu đãi, đổi PTTT) trigger BE re-validate giá &amp; điều kiện trước thanh toán.</li>
    <li>[Nguyên tắc đặc thù khác của hệ thống này]</li>
</ul>

<h3>2. Phân loại nhóm luồng &amp; sơ đồ luồng chính</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 24%;">Nhóm luồng</th>
            <th style="width: 38%;">Mô tả</th>
            <th style="width: 38%;">Áp dụng cho</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Nhóm 1 — [Tên nhóm]</b></td>
            <td>[Mô tả đặc điểm chung nhóm này]</td>
            <td>[Danh sách luồng thuộc nhóm]</td>
        </tr>
        <tr>
            <td><b>Nhóm 2 — [Tên nhóm]</b> (nếu có)</td>
            <td>[Mô tả đặc điểm chung]</td>
            <td>[Danh sách luồng]</td>
        </tr>
    </tbody>
</table>

<!-- Sơ đồ luồng nhóm 1 -->
<h4>2.1. Sơ đồ luồng [Tên nhóm 1]</h4>
<div style="text-align:center; page-break-inside:avoid; margin:10px 0; overflow:hidden;">
<img class="diagram-img" width="605" height="493" style="width:16.0cm; height:auto; display:block; margin:0 auto; border:none; padding:0; mso-width-source:userset; mso-height-source:userset;" src="[LOGO_BASE64_DIAGRAM_NHÓM1]">
</div>

<!-- Sơ đồ luồng nhóm 2 (nếu có) -->
<h4>2.2. Sơ đồ luồng [Tên nhóm 2]</h4>
<div style="text-align:center; page-break-inside:avoid; margin:10px 0; overflow:hidden;">
<img class="diagram-img" width="605" height="464" style="width:16.0cm; height:auto; display:block; margin:0 auto; border:none; padding:0; mso-width-source:userset; mso-height-source:userset;" src="[LOGO_BASE64_DIAGRAM_NHÓM2]">
</div>
<div class="note-box"><strong>Lưu ý:</strong> [Ghi chú về cách dùng sơ đồ và phần đặc thù từng luồng ở Mục C]</div>

<h3>3. Danh sách chức năng &amp; Ma trận phân quyền</h3>
<!-- Bảng danh sách chức năng / luồng -->
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 5%; text-align: center;">STT</th>
            <th style="width: 33%;">Luồng / Chức năng</th>
            <th style="width: 14%; text-align: center;">Loại / Nhóm</th>
            <th style="width: 48%;">Mô tả tóm tắt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;">1</td>
            <td>[Tên luồng 1]</td>
            <td style="text-align: center;">[Loại] / [Nhóm]</td>
            <td>[Mô tả ngắn]</td>
        </tr>
        <tr>
            <td style="text-align: center;">2</td>
            <td>[Tên luồng 2]</td>
            <td style="text-align: center;">[Loại] / [Nhóm]</td>
            <td>[Mô tả ngắn]</td>
        </tr>
    </tbody>
</table>
<div style="height:18px; line-height:18px;">&nbsp;</div>
<!-- Bảng ma trận phân quyền -->
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 40%;">Chức năng / Module</th>
            <th style="width: 15%; text-align: center;">KH vãng lai</th>
            <th style="width: 15%; text-align: center;">KH đăng nhập</th>
            <th style="width: 15%; text-align: center;">Telesales/CSKH</th>
            <th style="width: 15%; text-align: center;">Admin QLCS</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[Chức năng 1]</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
            <td style="text-align: center; color: red; font-weight: bold;">Không</td>
        </tr>
        <tr>
            <td>[Cấu hình giá/biểu phí/PTTT]</td>
            <td style="text-align: center; color: red; font-weight: bold;">Không</td>
            <td style="text-align: center; color: red; font-weight: bold;">Không</td>
            <td style="text-align: center; color: red; font-weight: bold;">Không</td>
            <td style="text-align: center; color: green; font-weight: bold;">Có</td>
        </tr>
    </tbody>
</table>

<h3>4. Đặc tả giao diện dùng chung &amp; trạng thái hệ thống</h3>
<!-- Bảng mô tả các trạng thái/thành phần dùng chung trên mọi luồng -->
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 18%;">Thành phần / Trạng thái</th>
            <th style="width: 16%;">Màn hình áp dụng</th>
            <th style="width: 12%; text-align: center;">Bắt buộc</th>
            <th style="width: 54%;">Yêu cầu hiển thị &amp; hành vi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>[Thành phần dùng chung 1]</b></td>
            <td>[Màn hình]</td>
            <td style="text-align: center;">Có / Không</td>
            <td>[Mô tả hành vi, message, CTA]</td>
        </tr>
        <tr>
            <td><b>Lỗi tải / tính giá</b></td>
            <td>[Màn hình] / Checkout</td>
            <td style="text-align: center;">Có nếu lỗi chặn</td>
            <td>Khi API lỗi/timeout, giữ KH tại màn hiện tại, bảo toàn dữ liệu đã nhập; hiển thị <span class="error-inline">"Chưa thể cập nhật thông tin. Vui lòng thử lại."</span>; CTA <b>Thử lại</b>; chặn thanh toán khi tổng tiền chưa xác thực.</td>
        </tr>
        <tr>
            <td><b>QLCS không trả PTTT</b></td>
            <td>Checkout / Thanh toán</td>
            <td style="text-align: center;">Có</td>
            <td>Hiển thị <span class="error-inline">"Hiện chưa có phương thức thanh toán khả dụng. Vui lòng thử lại hoặc liên hệ 1900 6600."</span>; disable nút đặt hàng; CTA <b>Tải lại phương thức thanh toán</b>.</td>
        </tr>
    </tbody>
</table>
<div class="note-box"><strong>Nguyên tắc chung cho trạng thái lỗi:</strong>
    <ul>
        <li>Lỗi làm sai tổng tiền, phí, PTTT hoặc consent bắt buộc phải chặn đặt hàng/thanh toán đến khi dữ liệu hợp lệ.</li>
        <li>CTA retry gọi lại đúng API đang lỗi; không xóa giỏ, không xóa dữ liệu KH chưa có xác nhận.</li>
        <li>Message hiển thị cho KH dùng copy nghiệp vụ rõ ràng; mã lỗi kỹ thuật chỉ dùng cho log &amp; CSKH.</li>
    </ul>
</div>

<!-- ============================================================ -->
<!-- C. ĐẶC TẢ CHI TIẾT CÁC LUỒNG NGHIỆP VỤ                      -->
<!-- ============================================================ -->
<h1>C. ĐẶC TẢ CHI TIẾT CÁC LUỒNG NGHIỆP VỤ</h1>
<p>Mỗi luồng là một mục lớn tự chứa, gồm <b>4 phần</b>: <b>.1</b> Đặc tả chi tiết (quy trình từng bước); <b>.2</b> Quy tắc nghiệp vụ; <b>.3</b> Đặc tả giao diện &amp; ràng buộc trường; <b>.4</b> Edge cases &amp; Bảng mã lỗi. Các nguyên tắc vận hành chung tại Mục B áp dụng cho mọi luồng.</p>

<!-- ===== LUỒNG 1 ===== -->
<!-- h2 tự xuống trang mới do CSS page-break-before: always -->
<h2>1. [Tên Luồng 1]</h2>
<p><span class="flow-band">Loại: [SKU / SA / SKU+SA] &middot; [Giỏ lẻ / Gộp giỏ]</span> &nbsp; [Mô tả ngắn một dòng về luồng này]</p>

<h3>1.1 Đặc tả chi tiết (Quy trình từng bước)</h3>
<table class="usecase-table">
    <tr>
        <td class="label">Tác nhân</td>
        <td>[Ví dụ: Khách hàng mua [sản phẩm] trên FPT.vn]</td>
    </tr>
    <tr>
        <td class="label">Điều kiện bắt đầu</td>
        <td>[Ví dụ: KH đang ở trang PDP / giỏ hàng]</td>
    </tr>
    <tr>
        <td class="label">Luồng xử lý chính</td>
        <td>
            <b>B1:</b> [Hành động KH] &rarr; [Phản hồi hệ thống].<br>
            <b>B2:</b> [Hành động KH] &rarr; [Phản hồi hệ thống].<br>
            <b>B3:</b> [Hành động KH] &rarr; [Phản hồi hệ thống].<br>
            <b>B4:</b> Xác nhận &amp; thanh toán &rarr; BE tạo đơn SPF &rarr; Hoàn tất (mã đơn).
        </td>
    </tr>
    <tr>
        <td class="label">Điều kiện kết thúc</td>
        <td>[Ví dụ: Đơn tạo thành công, KH nhận mã đơn / mã kích hoạt]</td>
    </tr>
    <tr>
        <td class="label">Luồng thay thế / Ngoại lệ</td>
        <td>
            <b>Alt 1 — [Tên ngoại lệ]:</b> [Điều kiện xảy ra] &rarr; [Hành vi hệ thống].<br><br>
            <b>Alt 2 — [Tên ngoại lệ]:</b> [Điều kiện xảy ra] &rarr; [Hành vi hệ thống].
        </td>
    </tr>
</table>

<!-- Kịch bản đặc thù (nếu có) -->
<h4>1.1.1 Kịch bản nghiệp vụ đặc thù</h4>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 18%;">Kịch bản</th>
            <th style="width: 42%;">Mô tả</th>
            <th style="width: 40%;">Hành vi bắt buộc</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Case 1 — [Tên]</b></td>
            <td>[Điều kiện và mô tả nghiệp vụ]</td>
            <td>[Hành vi hệ thống bắt buộc]</td>
        </tr>
        <tr>
            <td><b>Case 2 — [Tên]</b></td>
            <td>[Điều kiện và mô tả nghiệp vụ]</td>
            <td>[Hành vi hệ thống bắt buộc]</td>
        </tr>
    </tbody>
</table>

<h3>1.2 Quy tắc nghiệp vụ</h3>
<!-- BR viết dạng bảng 3 cột — KHÔNG dùng alert-box -->
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 14%; text-align:center;">Mã</th>
            <th style="width: 24%;">Tên quy tắc</th>
            <th style="width: 62%;">Nội dung &amp; Logic hệ thống</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center;">[MÔ-ĐUN]-BR-01</td>
            <td>[Tên quy tắc 1]</td>
            <td>[Mô tả chi tiết logic, điều kiện, nguồn cấu hình]</td>
        </tr>
        <tr>
            <td style="text-align:center;">[MÔ-ĐUN]-BR-02</td>
            <td>[Tên quy tắc 2]</td>
            <td>[Mô tả chi tiết logic]</td>
        </tr>
        <tr>
            <td style="text-align:center;">[MÔ-ĐUN]-BR-03</td>
            <td>PTTT động &amp; COD vùng cấm</td>
            <td>Danh sách PTTT do QLCS/Backend khai báo; FE render theo dữ liệu trả về. COD ẩn/disable nếu địa chỉ thuộc vùng không hỗ trợ thu hộ.</td>
        </tr>
    </tbody>
</table>

<h3>1.3 Đặc tả giao diện &amp; ràng buộc trường</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 20%;">Phần tử</th>
            <th style="width: 16%;">Màn hình</th>
            <th style="width: 8%; text-align:center;">Bắt buộc</th>
            <th style="width: 56%;">Ràng buộc &amp; hành vi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>[Tên phần tử / field]</b></td>
            <td>[Màn hình: PDP / Giỏ / Checkout]</td>
            <td style="text-align:center;">Có / Không</td>
            <td>[Mô tả ràng buộc, validation, phản hồi hệ thống]</td>
        </tr>
        <tr>
            <td><b>Phương thức thanh toán</b></td>
            <td>Checkout</td>
            <td style="text-align:center;">Có</td>
            <td>Danh sách động từ QLCS; COD ẩn ở vùng cấm ([MÔ-ĐUN]-BR-03).</td>
        </tr>
        <tr>
            <td><b>Hoàn tất đơn hàng</b></td>
            <td>Hoàn tất</td>
            <td style="text-align:center;">&ndash;</td>
            <td>Hiển thị mã đơn, tổng tiền, PTTT, trạng thái tiếp nhận; CTA <b>Theo dõi đơn hàng</b>.</td>
        </tr>
    </tbody>
</table>

<h3>1.4 Edge cases &amp; Bảng mã lỗi</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 16%;">Mã lỗi</th>
            <th style="width: 26%;">Trường hợp</th>
            <th style="width: 36%;">Message hiển thị</th>
            <th style="width: 22%;">Hành vi hệ thống</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ERR_[MÔ-ĐUN]_01</td>
            <td>[Tên trường hợp 1]</td>
            <td><span class="error-inline">"[Message lỗi chính xác]"</span></td>
            <td>[Hành vi UI / CTA]</td>
        </tr>
        <tr>
            <td>ERR_[MÔ-ĐUN]_02</td>
            <td>[Tên trường hợp 2]</td>
            <td><span class="error-inline">"[Message lỗi chính xác]"</span></td>
            <td>[Hành vi UI / CTA]</td>
        </tr>
        <tr>
            <td>MSG_[MÔ-ĐUN]_OK</td>
            <td>Thanh toán thành công</td>
            <td><span class="success-inline">"Thanh toán thành công! Cảm ơn quý khách đã đăng ký sử dụng dịch vụ của FPT Telecom."</span></td>
            <td>Chuyển trang Hoàn tất; hiển thị mã đơn.</td>
        </tr>
    </tbody>
</table>

<!-- ===== LUỒNG 2 (nếu có) ===== -->
<h2>2. [Tên Luồng 2]</h2>
<p><span class="flow-band">Loại: [SKU / SA] &middot; [Nhóm]</span> &nbsp; [Mô tả ngắn]</p>

<h3>2.1 Đặc tả chi tiết (Quy trình từng bước)</h3>
<!-- Lặp lại cấu trúc usecase-table như Luồng 1 -->

<h3>2.2 Quy tắc nghiệp vụ</h3>
<!-- Lặp lại cấu trúc bảng BR như Luồng 1 -->

<h3>2.3 Đặc tả giao diện &amp; ràng buộc trường</h3>
<!-- Lặp lại cấu trúc bảng giao diện như Luồng 1 -->

<h3>2.4 Edge cases &amp; Bảng mã lỗi</h3>
<!-- Lặp lại cấu trúc bảng mã lỗi như Luồng 1 -->

<!-- ============================================================ -->
<!-- D. TRƯỜNG HỢP LỖI & THÔNG BÁO HỆ THỐNG                       -->
<!-- ============================================================ -->
<h1>D. TRƯỜNG HỢP LỖI &amp; THÔNG BÁO HỆ THỐNG</h1>

<h3>1. Nguyên tắc hiển thị lỗi &amp; retry</h3>
<ul>
    <li><b>Ưu tiên thông điệp nghiệp vụ:</b> KH chỉ nhìn thấy message dễ hiểu và CTA xử lý tiếp theo; mã lỗi kỹ thuật dùng cho log, tracking và CSKH.</li>
    <li><b>Không cho thanh toán khi dữ liệu chưa hợp lệ:</b> Các lỗi tính giá, phí, PTTT, consent bắt buộc hoặc tồn kho phải disable CTA đặt hàng/thanh toán.</li>
    <li><b>Bảo toàn dữ liệu KH:</b> Khi retry, hệ thống giữ nguyên giỏ hàng, thông tin KH, voucher đã nhập; chỉ cập nhật lại phần dữ liệu từ API sau khi retry thành công.</li>
    <li><b>Retry đúng nguồn lỗi:</b> CTA <b>Thử lại</b>/<b>Áp dụng lại</b>/<b>Tải lại</b> gọi lại đúng API tương ứng và ghi nhận log thời điểm, mã lỗi, request ID nếu có.</li>
</ul>

<h3>2. Trạng thái lỗi dùng chung</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 18%;">Trạng thái</th>
            <th style="width: 22%;">Điều kiện kích hoạt</th>
            <th style="width: 34%;">Message hiển thị</th>
            <th style="width: 26%;">Hành vi / CTA</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Không tải được dữ liệu</b></td>
            <td>API lấy dữ liệu lỗi, timeout hoặc trả dữ liệu không hợp lệ.</td>
            <td><span class="error-inline">"Chưa thể tải thông tin. Vui lòng thử lại."</span></td>
            <td>CTA <b>Thử lại</b>; không cho tiếp tục khi chưa có dữ liệu hợp lệ.</td>
        </tr>
        <tr>
            <td><b>Không cập nhật được tổng tiền</b></td>
            <td>API tính giá/biểu phí/voucher lỗi hoặc timeout.</td>
            <td><span class="error-inline">"Chưa thể cập nhật giá và tổng tiền. Vui lòng thử lại."</span></td>
            <td>Đánh dấu tổng tiền chưa xác thực; disable CTA thanh toán; CTA <b>Thử lại</b>.</td>
        </tr>
        <tr>
            <td><b>Không có PTTT</b></td>
            <td>QLCS không trả danh sách PTTT phù hợp với giỏ/khu vực/chính sách.</td>
            <td><span class="error-inline">"Hiện chưa có phương thức thanh toán khả dụng. Vui lòng thử lại hoặc liên hệ 1900 6600."</span></td>
            <td>Disable đặt hàng/thanh toán; CTA <b>Tải lại phương thức thanh toán</b>.</td>
        </tr>
        <tr>
            <td><b>Voucher không hợp lệ</b></td>
            <td>Voucher không tồn tại, hết hạn hoặc không thỏa điều kiện giỏ.</td>
            <td><span class="error-inline">"Mã khuyến mãi không hợp lệ hoặc đã hết hạn. Vui lòng kiểm tra lại."</span></td>
            <td>Không áp dụng giảm giá; giữ mã KH đã nhập.</td>
        </tr>
        <tr>
            <td><b>[Trạng thái lỗi đặc thù]</b></td>
            <td>[Điều kiện kích hoạt]</td>
            <td><span class="error-inline">"[Message]"</span></td>
            <td>[Hành vi / CTA]</td>
        </tr>
    </tbody>
</table>

<h3>3. Bảng mã lỗi dùng chung</h3>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 15%;">Mã lỗi</th>
            <th style="width: 18%;">Màn hình</th>
            <th style="width: 25%;">Điều kiện</th>
            <th style="width: 28%;">Message thông báo</th>
            <th style="width: 14%;">Hành động</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CART_EMPTY</td>
            <td>[Màn hình]</td>
            <td>Không có dòng hợp lệ.</td>
            <td><span class="error-inline">"[Tên màn hình] của bạn đang trống. Vui lòng chọn sản phẩm/dịch vụ để tiếp tục."</span></td>
            <td>Tiếp tục mua sắm</td>
        </tr>
        <tr>
            <td>PRICE_CALC_FAILED</td>
            <td>[Màn hình] / Checkout</td>
            <td>API tính giá, phí hoặc tổng tiền trả lỗi.</td>
            <td><span class="error-inline">"Chưa thể cập nhật giá và tổng tiền. Vui lòng thử lại."</span></td>
            <td>Thử lại; chặn thanh toán</td>
        </tr>
        <tr>
            <td>VOUCHER_TIMEOUT</td>
            <td>[Màn hình] / Checkout</td>
            <td>API kiểm tra voucher timeout.</td>
            <td><span class="error-inline">"Chưa thể kiểm tra mã khuyến mãi. Vui lòng thử lại sau ít phút."</span></td>
            <td>Áp dụng lại</td>
        </tr>
        <tr>
            <td>PAYMENT_METHOD_EMPTY</td>
            <td>Checkout / Thanh toán</td>
            <td>QLCS không trả PTTT khả dụng.</td>
            <td><span class="error-inline">"Hiện chưa có phương thức thanh toán khả dụng. Vui lòng thử lại hoặc liên hệ 1900 6600."</span></td>
            <td>Tải lại PTTT; chặn đặt hàng</td>
        </tr>
        <tr>
            <td>API_SESSION_EXPIRED</td>
            <td>[Màn hình] / Checkout</td>
            <td>Phiên hết hạn hoặc token không hợp lệ.</td>
            <td><span class="error-inline">"Phiên làm việc đã hết hạn. Vui lòng tải lại để tiếp tục."</span></td>
            <td>Tải lại</td>
        </tr>
        <tr>
            <td>CONSENT_REQUIRED</td>
            <td>Nhập thông tin KH / Checkout</td>
            <td>KH chưa xác nhận mục đích xử lý dữ liệu cá nhân bắt buộc.</td>
            <td><span class="error-inline">"Vui lòng xác nhận đồng ý xử lý dữ liệu cá nhân để tiếp tục."</span></td>
            <td>Highlight khối consent; chặn submit</td>
        </tr>
        <tr>
            <td>ERR_[MÔ-ĐUN]_XX</td>
            <td>[Màn hình]</td>
            <td>[Điều kiện đặc thù của hệ thống]</td>
            <td><span class="error-inline">"[Message lỗi]"</span></td>
            <td>[Hành động]</td>
        </tr>
    </tbody>
</table>

<!-- ============================================================ -->
<!-- E. YÊU CẦU PHI CHỨC NĂNG                                     -->
<!-- ============================================================ -->
<h1>E. YÊU CẦU PHI CHỨC NĂNG</h1>

<h3>1. Hiệu năng hệ thống (Performance)</h3>
<ul>
    <li><b>Tốc độ xử lý tính toán:</b> BE nhận dữ liệu, validate &amp; phản hồi kết quả cho FE không quá <b>0.5 giây</b> trong điều kiện mạng bình thường.</li>
    <li><b>Đồng bộ real-time:</b> Trạng thái [đối tượng] cập nhật ngay khi giao dịch hoàn tất, tránh dùng lại dữ liệu cũ.</li>
    <li><b>Tải đồng thời:</b> Hệ thống đáp ứng tối thiểu <b>1.000</b> giao dịch đồng thời không nghẽn.</li>
</ul>

<h3>2. Bảo mật &amp; An toàn thông tin (Security)</h3>
<ul>
    <li><b>Mã hóa:</b> Mọi dữ liệu truyền tải trong luồng thanh toán mã hóa qua HTTPS (TLS 1.3).</li>
    <li><b>Che dấu dữ liệu nhạy cảm:</b> SĐT &amp; mã hợp đồng hiển thị masking (VD: 098***1234); thông tin thẻ không lưu tại DB, ủy quyền cổng thanh toán PCI-DSS.</li>
    <li><b>Phân quyền:</b> Cấu hình giá/biểu phí/PTTT/ưu đãi chỉ Admin QLCS; KH không truy cập.</li>
    <li><b>Ghi nhận consent:</b> Lưu phiên bản chính sách, mã mục đích, thời điểm, kênh, trạng thái đồng ý và định danh phiên/đơn hàng; nội dung chính sách lấy từ cấu hình, không hardcode FE.</li>
</ul>

<h3>3. Trải nghiệm người dùng &amp; Mobile responsive (UI/UX)</h3>
<ul>
    <li><b>Responsive:</b> Hiển thị hoàn hảo trên Desktop &amp; Mobile; nút/popup/stepper thao tác tốt bằng ngón tay.</li>
    <li><b>Thông báo cụ thể:</b> Mọi lỗi nêu rõ điều kiện không đáp ứng, không dùng message generic; KH biết cần làm gì để tiếp tục.</li>
    <li><b>Cấu hình động:</b> Giá, chu kỳ, ưu đãi, PTTT, text điều khoản cấu hình từ Product Hub/QLCS — không hardcode FE.</li>
    <li><b>Phản hồi tức thì:</b> Kiểm tra phía client (định dạng SĐT/email, chọn dòng, tính tạm tính) xử lý real-time, không chờ submit.</li>
</ul>

<!-- ============================================================ -->
<!-- F. PHỤ LỤC & TÀI LIỆU THAM KHẢO                             -->
<!-- ============================================================ -->
<h1>F. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO</h1>
<ul>
    <li>Taxonomy sản phẩm: [Mô tả ngắn các loại sản phẩm/dịch vụ trong phạm vi tài liệu]</li>
    <li>Tài liệu thiết kế UI/UX (Figma): [Chèn link Figma tại đây]</li>
    <li>Sơ đồ BPMN: diagrams/[tên_flow]_bpmn.svg (generator: diagrams/gen_[tên]_bpmn.py)</li>
    <li>URD liên quan: [Danh sách các URD khác cùng hệ thống]</li>
    <li>Tài liệu đặc tả API tích hợp (SPF / CRM / Payment / Product Hub): [Chèn link]</li>
    <li>Quy ước mã: BR theo luồng ([PREFIX]-BR-nn); mã lỗi ERR_{LUỒNG}_{NN}; thông điệp thành công MSG_{LUỒNG}_OK</li>
</ul>

<!-- ============================================================ -->
<!-- FOOTER ĐÁNH SỐ TRANG (MS WORD)                               -->
<!-- ============================================================ -->
<div style='mso-element:footer' id="f1">
    <p class="MsoFooter" align="center" style="text-align:center; font-family:'Times New Roman', serif; font-size:9pt; color:#666666;">
        Trang <!--[if supportFields]><span style='mso-element:field-begin'></span><span style='mso-spacerun:yes'> </span>PAGE <span style='mso-element:field-separator'></span><![endif]--><span>1</span><!--[if supportFields]><span style='mso-element:field-end'></span><![endif]--> / <!--[if supportFields]><span style='mso-element:field-begin'></span><span style='mso-spacerun:yes'> </span>NUMPAGES <span style='mso-element:field-separator'></span><![endif]--><span>1</span><!--[if supportFields]><span style='mso-element:field-end'></span><![endif]-->&nbsp;&nbsp;|&nbsp;&nbsp;FPT-URD-[MODULE]-[SỐ]-01 &middot; [VERSION]
    </p>
</div>

</div><!-- /Section1 -->

</body>
</html>
```

---

## PHẦN 2 — CHECKLIST TRƯỚC KHI SUBMIT URD

### ✅ Trang bìa
- [ ] **Bảng 1** — Logo FPT (ô trái, `width:120px`, `table-layout:fixed`) | Tiêu đề "FPT.VN URD – USER REQUIREMENTS DOCUMENT" (ô phải, in hoa)
- [ ] Row 2 của Bảng 1: Mã hiệu · Phiên bản · Ngày inline
- [ ] Logo nhúng **base64 Data URI**, `width="110" height="39"` (px, không dùng cm)
- [ ] **Bảng 2** — Revision History: tiêu đề màu `#1f4e78`, đường kẻ ngang `#1f4e78`, chú thích `[A]/[U]/[D]`, bảng 6 cột (Date · Version · Author · Reviewer · Approver · Change Description), header nền `#dae3f3`
- [ ] ⚠️ **Phiên bản ở Bảng 1 = phiên bản mới nhất trong Bảng 2** (đồng bộ)
- [ ] Cách 2 bảng **2cm** (`margin-top:2cm` trên div bọc Bảng 2)
- [ ] Kết thúc trang bìa bằng `<div style="page-break-before: always;">&nbsp;</div>` (class `toc-title` tự xử lý)

### ✅ Đánh số trang (MS Word)
- [ ] Toàn bộ thân tài liệu bọc trong `<div class="Section1">`
- [ ] `@page Section1 { mso-footer: f1; }` + `<div id="f1" style="mso-element:footer">` với field `PAGE`/`NUMPAGES`
- [ ] Footer: "Trang X / Y | Mã hiệu · Version"

### ✅ Page Break
- [ ] MỤC LỤC có `class="toc-title"` (đã tích hợp `page-break-before: always`)
- [ ] Mỗi `<h1>` (A, B, C, D, E, F) xuống trang mới (CSS đã có `page-break-before: always`)
- [ ] Mỗi `<h2>` (luồng trong mục C) xuống trang mới (CSS đã có `page-break-before: always`)

### ✅ Mục lục (TOC)
- [ ] **Điền số trang thực** vào ký tự `X` sau khi render bằng Word — KHÔNG để "X"/"—"
- [ ] Số trang khớp với các đầu mục đã page-break
- [ ] Level 1 bold sát lề, level 2 thụt 0.75cm, level 3 thụt 1.5cm; tab stop phải 16.8cm

### ✅ Sơ đồ BPMN
- [ ] Chuẩn BPMN: swimlane/pool theo tác nhân (KH / FE / BE & Tích hợp)
- [ ] Start Event = vòng tròn mảnh; End Event = vòng tròn đậm; Task = chữ nhật bo góc; Exclusive Gateway = hình thoi **×**; Text Annotation = khối nét đứt; Sequence Flow liền; luồng quay lui nét đứt
- [ ] `<img>` phải có `width="[PX_W]" height="[PX_H]"` (px thực của PNG) + inline style `width:16.0cm; height:auto; border:none; padding:0; mso-width-source:userset; mso-height-source:userset;`
- [ ] KHÔNG có `border`, `padding`, `alt` trên ảnh sơ đồ; KHÔNG dùng class `diagram-img` cũ có border
- [ ] Bọc trong `<div style="text-align:center; page-break-inside:avoid; margin:10px 0; overflow:hidden;">`
- [ ] ⚠️ KHÔNG đặt text/bullet TRƯỚC `<img>`; ghi chú "cách đọc" + nguyên tắc vận hành đặt SAU ảnh
- [ ] Nguồn SVG lưu tại `diagrams/[tên_flow]_bpmn.svg`; PNG nhúng base64

### ✅ Mục C — Cấu trúc luồng
- [ ] Mỗi luồng là một `<h2>` (tự xuống trang mới)
- [ ] Ngay dưới `<h2>` có `<p><span class="flow-band">Loại: ... · Nhóm: ...</span> &nbsp; [Mô tả]</p>`
- [ ] Mỗi luồng có đủ **4 phần**: x.1 Đặc tả chi tiết · x.2 Quy tắc nghiệp vụ · x.3 Đặc tả giao diện · x.4 Edge cases & Mã lỗi
- [ ] Góc nhìn **Customer Journey** — KH làm gì, KH thấy gì
- [ ] Pre-conditions, Luồng chính (B1, B2...), Post-conditions, Luồng thay thế (Alt 1, Alt 2...)
- [ ] Có kịch bản đặc thù (`h4`) nếu luồng có nhiều case phức tạp

### ✅ Business Rules
- [ ] BR viết dạng **bảng 3 cột** (Mã | Tên quy tắc | Nội dung) — KHÔNG dùng `alert-box`
- [ ] Mã BR theo prefix luồng: `[PREFIX]-BR-01`, `[PREFIX]-BR-02`... liên tục không gãy số
- [ ] Cập nhật mọi cross-reference khi thêm/xóa rule

### ✅ Edge Cases & Mã lỗi
- [ ] Bảng mã lỗi 4 cột: Mã lỗi | Trường hợp | Message hiển thị | Hành vi hệ thống
- [ ] Message lỗi dùng `<span class="error-inline">"..."</span>` — màu đỏ `#c00000`, italic, bold
- [ ] Message thành công dùng `<span class="success-inline">"..."</span>` — màu xanh lá `#385723`
- [ ] Quy ước mã: `ERR_{LUỒNG}_{NN}` cho lỗi; `MSG_{LUỒNG}_OK` cho thành công
- [ ] Mục D có bảng mã lỗi **dùng chung** (5 cột: Mã | Màn hình | Điều kiện | Message | Hành động)

### ✅ Bảng B.3 — Phân quyền
- [ ] Bảng chức năng: 4 cột (STT | Luồng/Chức năng | Loại/Nhóm | Mô tả)
- [ ] Bảng phân quyền: cột role gồm KH vãng lai / KH đăng nhập / Telesales-CSKH / Admin QLCS
- [ ] Cách nhau bằng `<div style="height:18px; line-height:18px;">&nbsp;</div>`

### ✅ Bảng B.4 — Giao diện dùng chung
- [ ] 4 cột: Thành phần/Trạng thái | Màn hình áp dụng | Bắt buộc | Yêu cầu hiển thị & hành vi
- [ ] Bao gồm các trạng thái lỗi hệ thống dùng chung (load fail, tính giá fail, PTTT empty, consent)

### ✅ Revision History & Mã hiệu
- [ ] Version Bảng 1 = version mới nhất trong Bảng 2
- [ ] Cập nhật ngày + tác giả + mô tả thay đổi sau mỗi lần sửa
- [ ] Mã hiệu format: `FPT-URD-[MODULE]-[SỐ]-01`

---

## PHẦN 3 — LỆNH LẤY BASE64 LOGO

```bash
python3 -c "
import base64
with open('docs/images/logoftel.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
print('data:image/png;base64,' + b64)
"
```

> Copy toàn bộ chuỗi output (bắt đầu bằng `data:image/png;base64,...`) vào `src` của thẻ `<img>` logo trang bìa.

---

## PHẦN 4 — CHUẨN CANH CHỈNH CỘT BẢNG (% WIDTH)

> **Nguyên tắc cốt lõi:** Cột **mô tả chi tiết / logic** luôn chiếm tỷ lệ lớn nhất. Dùng `%` thay `px` cứng. Tổng cột = 100%.

### Bảng tỷ lệ chuẩn theo từng loại

#### 1. Revision History (6 cột)
```html
<th style="width:90px;">Date</th>
<th style="width:75px;">Version</th>
<th style="width:110px;">Author</th>
<th style="width:110px;">Reviewer</th>
<th style="width:110px;">Approver</th>
<th>Change Description</th>   <!-- chiếm phần còn lại -->
```

#### 2. Thông tin chung / AS-IS vs TO-BE (3 cột)
```html
<th style="width: 5%; text-align:center">STT</th>
<th style="width: 22%;">Hạng mục</th>
<th style="width: 73%;">Mô tả chi tiết</th>   <!-- ★ LỚN NHẤT -->
```

#### 3. Thuật ngữ / Định nghĩa (4 cột)
```html
<th style="width: 5%; text-align:center">STT</th>
<th style="width: 14%;">Thuật ngữ</th>
<th style="width: 26%;">Tên đầy đủ</th>
<th style="width: 55%;">Mô tả ý nghĩa</th>   <!-- ★ LỚN NHẤT -->
```

#### 4. Danh sách chức năng / Luồng (4 cột)
```html
<th style="width: 5%; text-align:center">STT</th>
<th style="width: 33%;">Luồng / Chức năng</th>
<th style="width: 14%; text-align:center">Loại / Nhóm</th>
<th style="width: 48%;">Mô tả tóm tắt</th>   <!-- ★ LỚN NHẤT -->
```

#### 5. Ma trận phân quyền (5 cột)
```html
<th style="width: 40%;">Chức năng / Module</th>   <!-- ★ LỚN NHẤT -->
<th style="width: 15%; text-align:center">KH vãng lai</th>
<th style="width: 15%; text-align:center">KH đăng nhập</th>
<th style="width: 15%; text-align:center">Telesales/CSKH</th>
<th style="width: 15%; text-align:center">Admin QLCS</th>
```

#### 6. Giao diện dùng chung B.4 (4 cột)
```html
<th style="width: 18%;">Thành phần / Trạng thái</th>
<th style="width: 16%;">Màn hình áp dụng</th>
<th style="width: 12%; text-align:center">Bắt buộc</th>
<th style="width: 54%;">Yêu cầu hiển thị &amp; hành vi</th>   <!-- ★ LỚN NHẤT -->
```

#### 7. Business Rules — bảng 3 cột (KHÔNG alert-box)
```html
<th style="width: 14%; text-align:center">Mã</th>
<th style="width: 24%;">Tên quy tắc</th>
<th style="width: 62%;">Nội dung &amp; Logic hệ thống</th>   <!-- ★ LỚN NHẤT -->
```

#### 8. Đặc tả giao diện — 4 cột
```html
<th style="width: 20%;">Phần tử</th>
<th style="width: 16%;">Màn hình</th>
<th style="width: 8%; text-align:center">Bắt buộc</th>
<th style="width: 56%;">Ràng buộc &amp; hành vi</th>   <!-- ★ LỚN NHẤT -->
```

#### 9. Edge cases — bảng mã lỗi 4 cột
```html
<th style="width: 16%;">Mã lỗi</th>
<th style="width: 26%;">Trường hợp</th>
<th style="width: 36%;">Message hiển thị</th>   <!-- ★ LỚN NHẤT -->
<th style="width: 22%;">Hành vi hệ thống</th>
```

#### 10. Bảng mã lỗi dùng chung D.3 — 5 cột
```html
<th style="width: 15%;">Mã lỗi</th>
<th style="width: 18%;">Màn hình</th>
<th style="width: 25%;">Điều kiện</th>
<th style="width: 28%;">Message thông báo</th>   <!-- ★ LỚN NHẤT -->
<th style="width: 14%;">Hành động</th>
```

#### 11. Kịch bản đặc thù — 3 cột
```html
<th style="width: 18%;">Kịch bản</th>
<th style="width: 42%;">Mô tả</th>
<th style="width: 40%;">Hành vi bắt buộc</th>
```

### Quy tắc chung
| Loại cột | Tỷ lệ gợi ý |
|---|---|
| ID / STT / Mã lỗi | 5–16% |
| Cột cờ (Bắt buộc, Loại) | 8–14% |
| Tên ngắn / Nhãn | 14–26% |
| Mô tả vừa | 20–33% |
| **Mô tả chi tiết / Logic / Message** | **40–73%** |

---

## PHẦN 5 — TẠO SƠ ĐỒ BPMN & NHÚNG VÀO URD

### Quy ước ký hiệu BPMN bắt buộc
| Thành phần | Ký hiệu | Ghi chú |
|---|---|---|
| Start Event | Vòng tròn **mảnh** (xanh) | Điểm bắt đầu |
| End Event | Vòng tròn **đậm** (đỏ) | Mỗi kết cục một end riêng |
| Task / Activity | Chữ nhật **bo góc** | Một hành động |
| Exclusive Gateway | Hình **thoi** gắn ký hiệu **×** | Rẽ nhánh loại trừ (Yes/No) |
| Text Annotation | Khối **nét đứt** | Gắn mã `[PREFIX-BR-nn]` cạnh bước liên quan |
| Sequence Flow | Mũi tên **liền** | Luồng tuần tự |
| Back / Retry flow | Mũi tên **nét đứt** | Quay về điều chỉnh / thử lại |
| Pool / Lane | Băng dọc có tiêu đề | 1 lane / tác nhân: KH · FE · BE & Tích hợp |

### Quy trình 4 bước
```bash
# 1) Viết generator Python sinh SVG swimlane dọc: mỗi node gán (lane, row, kind, label).
python3 diagrams/gen_[tên]_bpmn.py          # -> diagrams/[tên]_bpmn.svg

# 2) Convert SVG -> PNG @2x (cần: brew install librsvg)
rsvg-convert -z 2 -o diagrams/[tên]_bpmn.png diagrams/[tên]_bpmn.svg

# 3) Nhúng base64 vào URD
python3 - <<'PY'
import re, base64
p='thuyttdoc/[urd_file].doc'
html = open(p, encoding='utf-8').read()
b64 = 'data:image/png;base64,' + base64.b64encode(open('diagrams/[tên]_bpmn.png','rb').read()).decode()
# Thay ảnh tổng quan (diagram-img đầu tiên)
html = re.sub(r'(<img class="diagram-img"[^>]*src=")[^"]*(")', r'\g<1>' + b64 + r'\g<2>', html, count=1)
open(p, 'w', encoding='utf-8').write(html)
print('Done')
PY

# 4) Verify: render .doc -> PDF, kiểm tra sơ đồ
# macOS: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
#   --headless=new --disable-gpu --print-to-pdf=out.pdf "file://$PWD/thuyttdoc/[urd_file].doc"
```

### Nhúng img chuẩn (lấy W×H px từ rsvg-convert để điền vào width/height)
```html
<div style="text-align:center; page-break-inside:avoid; margin:10px 0; overflow:hidden;">
<img class="diagram-img" width="605" height="493" style="width:16.0cm; height:auto; display:block; margin:0 auto; border:none; padding:0; mso-width-source:userset; mso-height-source:userset;" src="data:image/png;base64,...">
</div>
```
> `width` và `height` (px) điền theo kích thước thực của PNG xuất ra (dùng `file diagrams/[tên].png` hoặc Python `PIL`). `mso-width-source:userset; mso-height-source:userset;` bắt buộc để Word không tự scale sai tỷ lệ khi in A4. KHÔNG dùng `alt` trên ảnh sơ đồ.

### Script lấy kích thước PNG (điền vào width/height px)
```bash
# Cách 1: dùng Python Pillow
python3 -c "from PIL import Image; im=Image.open('diagrams/[tên].png'); print(im.size)"
# Output: (605, 493)

# Cách 2: dùng file command
file diagrams/[tên].png
# Output: PNG image data, 605 x 493, ...
```

### Script nhúng tất cả ảnh base64 vào URD (thay theo thứ tự)
```python
import re, base64

p = 'thuyttdoc/[urd_file].doc'
html = open(p, encoding='utf-8').read()

diagrams = [
    'diagrams/[tên_overview]_bpmn.png',   # sơ đồ tổng quan B.1
    'diagrams/[tên_nhom1]_bpmn.png',      # sơ đồ nhóm 1 B.2.1
    'diagrams/[tên_nhom2]_bpmn.png',      # sơ đồ nhóm 2 B.2.2 (nếu có)
]

def b64(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path,'rb').read()).decode()

# Thay từng src theo thứ tự xuất hiện trong file
for i, path in enumerate(diagrams):
    html = re.sub(
        r'(<img class="diagram-img"[^>]*src=")[^"]*(")',
        lambda m, b=b64(path): m.group(1) + b + m.group(2),
        html, count=1
    )

open(p, 'w', encoding='utf-8').write(html)
print('Done —', len(diagrams), 'diagrams embedded')
```

### Lưu ý quan trọng
- **File `.doc` (HTML-based)** bị tool đọc nhầm là binary do dòng quá dài — chỉnh sửa bằng **Python (đọc/ghi UTF-8)**, không Read trực tiếp.
- **`width/height` px**: PHẢI khớp với kích thước thực PNG — nếu để sai, Word scale ảnh lệch tỷ lệ khi in.
- **`mso-width-source:userset`**: bắt buộc để Word tôn trọng `width:16.0cm` trong CSS thay vì tính lại từ px.
- **Lề & lane**: chừa lề trái/phải đủ cho Text Annotation, tránh tràn canvas.
- **Tiêu đề & chú giải (legend)**: đặt riêng ở đỉnh/đáy, không đè lên lane.
- **Mọi replace** nên có `count=1` hoặc xác nhận số lần thay để tránh replace sai vị trí.

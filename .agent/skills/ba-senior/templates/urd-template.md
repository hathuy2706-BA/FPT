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

    /* ===== TRANG BÌA ===== */
    .cover-container {
        border: 4px double #1f4e78;
        padding: 50px 40px;
        margin: 10px;
        min-height: 800px;
        position: relative;
    }
    .cover-logo-box { text-align: left; margin-bottom: 30px; }
    .cover-logo { width: 90px; height: auto; }
    .cover-title-box { text-align: center; margin-top: 60px; margin-bottom: 80px; }
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
    h1 { font-family: 'Arial', sans-serif; color: #1f4e78; font-size: 18pt; font-weight: bold; text-transform: uppercase; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #1f4e78; padding-bottom: 5px; page-break-before: always; }
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

    /* ===== MỤC LỤC ===== */
    /* page-break-before: always đảm bảo MỤC LỤC luôn xuống trang mới */
    .toc-title {
        page-break-before: always;
        font-family: 'Arial', sans-serif;
        font-size: 16pt;
        font-weight: bold;
        text-align: center;
        color: #1f4e78;
        text-transform: uppercase;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }
    table.toc-table { width: 100%; border-collapse: collapse; border: none; }
    table.toc-table td { border: none; padding: 5px 0; vertical-align: bottom; }
    .toc-dots { border-bottom: 1px dotted #555555; }
    .toc-l1 { font-family: 'Arial', sans-serif; font-weight: bold; color: #1f4e78; font-size: 11.5pt; text-transform: uppercase; }
    .toc-l2 { padding-left: 20px; font-size: 11pt; color: #000000; }
    .toc-l3 { padding-left: 40px; font-size: 10.5pt; font-style: italic; color: #555555; }
    .toc-page { text-align: right; font-family: 'Arial', sans-serif; font-size: 11pt; width: 40px; font-weight: bold; }

    /* ===== TIỆN ÍCH ===== */
    ul, ol { margin-top: 5px; margin-bottom: 10px; padding-left: 20px; }
    li { margin-bottom: 4px; }
    p { margin-top: 0; margin-bottom: 8px; text-align: justify; }
    .page-break { page-break-before: always; }
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

<!-- ============================================================ -->
<!-- TRANG BÌA                                                     -->
<!-- Ghi chú: Logo nhúng dạng base64 - không bị vỡ khi copy file -->
<!-- ============================================================ -->
<div class="cover-container">
    <div class="cover-logo-box">
        <!-- Thay [LOGO_BASE64] bằng chuỗi base64 của logoftel.png -->
        <!-- Lệnh lấy base64: python3 -c "import base64; print('data:image/png;base64,'+base64.b64encode(open('docs/images/logoftel.png','rb').read()).decode())" -->
        <img src="[LOGO_BASE64]" class="cover-logo" alt="FPT Telecom Logo">
    </div>

    <div class="cover-title-box">
        <div class="cover-title-main">Tài Liệu Yêu Cầu Người Dùng<br>(User Requirements Document - URD)</div>
        <div class="cover-title-sub">[TÊN HỆ THỐNG / TÍNH NĂNG]<br>[KÊNH / PHASE]</div>
    </div>

    <div class="cover-meta-box">
        <table class="cover-meta-table">
            <!-- BỎ dòng "Dự án" theo yêu cầu chuẩn hóa -->
            <tr>
                <td class="cover-meta-label">Mã hiệu:</td>
                <td>FPT-URD-[MODULE]-[SỐ THỨ TỰ]-01</td>
            </tr>
            <tr>
                <td class="cover-meta-label">Phiên bản:</td>
                <td>V1.0</td>
            </tr>
            <tr>
                <td class="cover-meta-label">Tác giả:</td>
                <td>[Tên tác giả — VD: ThuyTT104]</td>
            </tr>
            <tr>
                <td class="cover-meta-label">Ngày lập:</td>
                <td>[DD/MM/YYYY]</td>
            </tr>
            <tr>
                <td class="cover-meta-label">Ngày cập nhật:</td>
                <td>[DD/MM/YYYY]</td>
            </tr>
        </table>
    </div>
</div>

<div class="page-break"></div>

<!-- ============================================================ -->
<!-- LỊCH SỬ THAY ĐỔI                                             -->
<!-- ============================================================ -->
<h2>REVISION HISTORY (LỊCH SỬ THAY ĐỔI)</h2>
<p><i>Ký hiệu hành động: [A]: Add – Thêm mới | [U]: Update – Cập nhật, thay đổi | [D]: Delete - Xóa</i></p>
<table class="data-table">
    <thead>
        <tr>
            <th style="width: 15%;">Ngày</th>
            <th style="width: 10%;">Version</th>
            <th style="width: 20%;">Tác giả</th>
            <th style="width: 10%;">Hành động</th>
            <th style="width: 45%;">Mô tả chi tiết thay đổi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>[DD/MM/YYYY]</td>
            <td>V1.0</td>
            <td>[Tên tác giả]</td>
            <td style="text-align: center;">[A]</td>
            <td>Khởi tạo tài liệu URD [Tên hệ thống]. Mô tả chi tiết [Mô tả ngắn].</td>
        </tr>
    </tbody>
</table>

<!-- ============================================================ -->
<!-- MỤC LỤC — class toc-title đã có page-break-before: always   -->
<!-- ============================================================ -->
<div class="toc-title">MỤC LỤC</div>
<table class="toc-table">
    <tr>
        <td class="toc-l1">A. GIỚI THIỆU</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">1. Mục đích tài liệu</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">2. Thông tin chung &amp; Hiện trạng (AS-IS vs TO-BE)</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">3. Thuật ngữ và viết tắt</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l1">B. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">1. Sơ đồ luồng nghiệp vụ tổng quan (Flow Diagram)</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">2. Danh sách các chức năng chính</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">3. Ma trận phân quyền sử dụng</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l1">C. ĐẶC TẢ CHI TIẾT CÁC CHỨC NĂNG NGHIỆP VỤ</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">I. [Luồng 1]</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l3">1. Quy trình nghiệp vụ từng bước (Step-by-Step)</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l3">2. Quy tắc cấu hình &amp; Business Rules</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l3">3. Mô tả giao diện &amp; Ràng buộc trường</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">II. [Luồng 2] (nếu có)</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">III. Đặc tả điều kiện &amp; Edge Cases</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l2">IV. Bảng thông điệp báo lỗi (Error Messages)</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l1">D. YÊU CẦU PHI CHỨC NĂNG</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
    <tr>
        <td class="toc-l1">E. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO</td>
        <td class="toc-dots"></td>
        <td class="toc-page">X</td>
    </tr>
</table>

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

<div class="page-break"></div>

<!-- ============================================================ -->
<!-- B. TỔNG QUAN HỆ THỐNG                                        -->
<!-- ============================================================ -->
<h1>B. TỔNG QUAN HỆ THỐNG VÀ PHẠM VI</h1>

<h3>1. Sơ đồ luồng nghiệp vụ tổng quan (Flow Diagram)</h3>
<p>Dưới đây là sơ đồ luồng <b>hành trình khách hàng (Customer Journey)</b> khi sử dụng [Tên hệ thống]. Sơ đồ thể hiện từng bước hành động của KH, các điểm quyết định và quy tắc hệ thống vận hành ngầm.</p>
<p><b>Nguyên tắc vận hành:</b></p>
<ul>
    <li>[Nguyên tắc 1 — Ví dụ: BE xử lý toàn bộ tính toán, FE chỉ nhận kết quả và hiển thị]</li>
    <li>[Nguyên tắc 2 — Ví dụ: Cấu hình text động từ Product Hub, không hardcode trên FE]</li>
    <li>[Nguyên tắc 3 — Ví dụ: Mọi thay đổi điều kiện đơn hàng trigger re-validate tự động]</li>
</ul>
<!-- Sơ đồ flow: xuất PNG nền trắng bằng skill diagram-drawer, nhúng vào đây -->
<img src="[ĐƯỜNG_DẪN_HOẶC_BASE64]" class="diagram-img" alt="Sơ đồ Flow Diagram [Tên hệ thống]">

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

<div class="page-break"></div>

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

<div class="page-break"></div>

<h2>II. [TÊN LUỒNG 2] (nếu có)</h2>
<!-- Lặp lại cấu trúc như Luồng I -->

<div class="page-break"></div>

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

<div class="page-break"></div>

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

<div class="page-break"></div>

<!-- ============================================================ -->
<!-- E. PHỤ LỤC                                                   -->
<!-- ============================================================ -->
<h1>E. PHỤ LỤC &amp; TÀI LIỆU THAM KHẢO</h1>
<ul>
    <li>Tài liệu thiết kế UI/UX (Figma): [Chèn link Figma tại đây]</li>
    <li>Tài liệu đặc tả API tích hợp: [Chèn link tài liệu API]</li>
    <li>Sơ đồ Flow Diagram: [Đường dẫn file diagrams/...]</li>
    <li>[Tài liệu tham khảo khác]</li>
</ul>

</body>
</html>
```

---

## PHẦN 2 — CHECKLIST TRƯỚC KHI SUBMIT URD

### ✅ Trang bìa
- [ ] Logo FPT Telecom nhúng dạng **base64 Data URI** (không dùng đường dẫn file)
- [ ] Tác giả điền tên thực (VD: ThuyTT104)
- [ ] **BỎ dòng "Dự án"** theo chuẩn mới
- [ ] Có đầy đủ: Mã hiệu, Phiên bản, Ngày lập, Ngày cập nhật

### ✅ Page Break
- [ ] MỤC LỤC xuống trang mới (class `toc-title` đã có `page-break-before: always`)
- [ ] Mỗi `<h1>` (A, B, C, D, E) xuống trang mới (CSS `h1` đã có `page-break-before: always`)
- [ ] Dùng `<div class="page-break"></div>` trước các `<h2>` phân luồng lớn (I, II, III, IV)

### ✅ Sơ đồ Flow Diagram
- [ ] Dùng skill `diagram-drawer` để vẽ — nền trắng, đường thẳng/vuông góc
- [ ] Hình tròn: Bắt đầu / Kết thúc
- [ ] Hình chữ nhật: Tác vụ (hành động KH)
- [ ] Hình thoi: Điểm quyết định (YES/NO)
- [ ] Hình bình hành / Note box: Quy tắc hệ thống ẩn (note đi kèm step)
- [ ] Lưu PNG tại `diagrams/[tên_flow].png`
- [ ] Nhúng vào URD bằng `<img class="diagram-img">`

### ✅ Luồng nghiệp vụ
- [ ] Góc nhìn **Customer Journey** — KH làm gì, KH thấy gì
- [ ] Quy tắc hệ thống viết dưới dạng **note/BR** không phải step chính
- [ ] Có đầy đủ: Pre-conditions, Luồng chính, Post-conditions, Luồng ngoại lệ (Alt)

### ✅ Edge Cases & Error Messages
- [ ] Mỗi case có: điều kiện xảy ra, hành vi UI, message chính xác, hướng dẫn KH
- [ ] Message lỗi **cụ thể** theo loại điều kiện (ERR_PTTT, ERR_SKU...) — không generic
- [ ] Message thành công viết màu xanh lá (`success-inline`)
- [ ] Message lỗi viết màu đỏ (`error-inline`)

### ✅ Revision History
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


import re
import os

template_file = '/Users/hathuy/Documents/FPT-1/thuyttdoc/brd_sdt_fpl.doc'
out_files = {
    'BRD_Internet_Combo.doc': {
        'title': 'FPT.VN BRD - ĐĂNG KÝ COMBO INTERNET VÀ TRUYỀN HÌNH',
        'code': 'FPT-BRD-REG-01-01',
        'content': '''<h1>A. GIỚI THIỆU</h1>
<h2>1. Mục đích tài liệu</h2>
<p>Tài liệu này mô tả các yêu cầu nghiệp vụ cho luồng đăng ký mua Internet và Combo Internet trên trang beta.fpt.vn.</p>

<h1>B. LUỒNG NGHIỆP VỤ</h1>
<h2>1. Step-by-step Luồng Khách hàng</h2>
<table class="data-table">
    <tr>
        <th style="width: 10%">STT</th>
        <th style="width: 30%">Bước thực hiện</th>
        <th style="width: 60%">Hành vi hệ thống (UI/UX)</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Khách hàng bấm "Đăng ký ngay" / "Mua ngay" tại gói cước Internet/Combo.</td>
        <td>Hệ thống hiển thị popup form nhập thông tin.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Khách hàng nhập thông tin (SĐT, Họ tên, Địa chỉ) và xác nhận.</td>
        <td>Kiểm tra rule validation và chính sách địa chỉ.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Khách hàng chuyển sang bước thanh toán.</td>
        <td>Hoàn tất quá trình đăng ký.</td>
    </tr>
</table>

<h1>C. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)</h1>
<table class="data-table">
    <tr>
        <th style="width: 10%">Mã Rule</th>
        <th style="width: 24%">Tên Quy tắc</th>
        <th style="width: 66%">Mô tả chi tiết</th>
    </tr>
    <tr>
        <td>BR-01</td>
        <td>Kiểm tra định dạng SĐT</td>
        <td>SĐT phải đúng định dạng 10 số, bắt đầu bằng 0. Validate theo các đầu số nhà mạng hợp lệ tại VN. <span class="error-inline">Thông báo lỗi: SĐT không hợp lệ</span></td>
    </tr>
    <tr>
        <td>BR-02</td>
        <td>Kiểm tra trùng tài khoản FPT Play</td>
        <td>Khi nhập SĐT (ví dụ: 0939536236) để mua combo, hệ thống check qua API FPT Play. Nếu SĐT đã có tài khoản, hiển thị cảnh báo/thông báo đồng bộ tài khoản.</td>
    </tr>
    <tr>
        <td>BR-03</td>
        <td>Xử lý gói VVIP1/2</td>
        <td>Nếu khách hàng chọn gói VVIP1/VVIP2, áp dụng rule block hoặc yêu cầu nâng cấp nếu tài khoản hiện tại không đủ điều kiện.</td>
    </tr>
    <tr>
        <td>BR-04</td>
        <td>Kiểm tra hạ tầng địa chỉ</td>
        <td>Call API check hạ tầng theo Phường/Xã/Quận/Huyện. Nếu không có hạ tầng, chặn đăng ký và báo lỗi.</td>
    </tr>
</table>

<h1>D. TRƯỜNG HỢP NGOẠI LỆ (EDGE CASES)</h1>
<table class="data-table">
    <tr>
        <th style="width: 20%">Trường hợp (Case)</th>
        <th style="width: 40%">Điều kiện</th>
        <th style="width: 40%">Hành vi hệ thống</th>
    </tr>
    <tr>
        <td>SĐT đã tồn tại nhưng tài khoản bị khóa</td>
        <td>API FPT Play trả về status khóa đối với SĐT.</td>
        <td><span class="error-inline">Báo lỗi "Tài khoản FPT Play của bạn đang bị khóa".</span></td>
    </tr>
    <tr>
        <td>Khu vực hết port</td>
        <td>Check API hạ tầng trả về hết port.</td>
        <td>Chuyển sang form lưu thông tin chờ.</td>
    </tr>
</table>
'''
    },
    'BRD_ThietBi.doc': {
        'title': 'FPT.VN BRD - MUA THIẾT BỊ',
        'code': 'FPT-BRD-REG-01-02',
        'content': '''<h1>A. GIỚI THIỆU</h1>
<h2>1. Mục đích tài liệu</h2>
<p>Tài liệu này mô tả các yêu cầu nghiệp vụ cho luồng mua thiết bị (Camera, AP, Smart TV, SmartHome) trên trang beta.fpt.vn.</p>

<h1>B. LUỒNG NGHIỆP VỤ</h1>
<h2>1. Step-by-step Luồng Khách hàng</h2>
<table class="data-table">
    <tr>
        <th style="width: 10%">STT</th>
        <th style="width: 30%">Bước thực hiện</th>
        <th style="width: 60%">Hành vi hệ thống (UI/UX)</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Khách hàng chọn thiết bị (Camera, AP...) và bấm "Mua ngay".</td>
        <td>Hiển thị popup/trang giỏ hàng yêu cầu số lượng.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Khách hàng nhập thông tin giao hàng (Họ tên, SĐT, Địa chỉ).</td>
        <td>Kiểm tra điều kiện bắt buộc và SĐT.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Chọn phương thức thanh toán.</td>
        <td>Kiểm tra tồn kho và chuyển qua thanh toán.</td>
    </tr>
</table>

<h1>C. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)</h1>
<table class="data-table">
    <tr>
        <th style="width: 10%">Mã Rule</th>
        <th style="width: 24%">Tên Quy tắc</th>
        <th style="width: 66%">Mô tả chi tiết</th>
    </tr>
    <tr>
        <td>BR-01</td>
        <td>Kiểm tra điều kiện bắt buộc</td>
        <td>Các trường Tên, SĐT, Địa chỉ chi tiết là bắt buộc nhập (mandatory).</td>
    </tr>
    <tr>
        <td>BR-02</td>
        <td>Kiểm tra SĐT hợp lệ</td>
        <td>Chỉ chấp nhận số điện thoại 10 số mạng VN. Báo lỗi <span class="error-inline">"SĐT không hợp lệ"</span> nếu sai định dạng.</td>
    </tr>
    <tr>
        <td>BR-03</td>
        <td>Kiểm tra tồn kho</td>
        <td>Trước khi qua bước thanh toán, call API kho để giữ hàng (hold). Nếu hết hàng, thông báo <span class="error-inline">"Sản phẩm tạm hết hàng"</span>.</td>
    </tr>
    <tr>
        <td>BR-04</td>
        <td>Chính sách khách hàng hiện hữu</td>
        <td>Nếu SĐT đang dùng mạng FPT, tự động apply voucher/chiết khấu nếu có.</td>
    </tr>
</table>
'''
    },
    'BRD_DichVu_SA.doc': {
        'title': 'FPT.VN BRD - DỊCH VỤ SA',
        'code': 'FPT-BRD-REG-01-03',
        'content': '''<h1>A. GIỚI THIỆU</h1>
<h2>1. Mục đích tài liệu</h2>
<p>Tài liệu này mô tả yêu cầu nghiệp vụ cho các dịch vụ giá trị gia tăng (SA) gồm FPT Play, Ultrafast, HyperFast.</p>

<h1>B. LUỒNG NGHIỆP VỤ</h1>
<h2>1. Step-by-step Luồng Khách hàng</h2>
<table class="data-table">
    <tr>
        <th style="width: 10%">STT</th>
        <th style="width: 30%">Bước thực hiện</th>
        <th style="width: 60%">Hành vi hệ thống (UI/UX)</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Khách hàng chọn gói dịch vụ (ví dụ: Ultrafast) và chọn "Đăng ký ngay".</td>
        <td>Hệ thống hiển thị yêu cầu nhập Mã Hợp Đồng hoặc SĐT.</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Khách hàng nhập Mã Hợp Đồng hoặc SĐT.</td>
        <td>Hệ thống tra cứu thông tin Hợp đồng Internet FPT.</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Xác nhận thông tin gói và tiến hành thanh toán.</td>
        <td>Kích hoạt dịch vụ thành công <span class="success-inline">"Đăng ký thành công"</span>.</td>
    </tr>
</table>

<h1>C. QUY TẮC NGHIỆP VỤ (BUSINESS RULES)</h1>
<table class="data-table">
    <tr>
        <th style="width: 10%">Mã Rule</th>
        <th style="width: 24%">Tên Quy tắc</th>
        <th style="width: 66%">Mô tả chi tiết</th>
    </tr>
    <tr>
        <td>BR-01</td>
        <td>Điều kiện đăng ký SA</td>
        <td>Dịch vụ Ultrafast/HyperFast chỉ áp dụng cho khách hàng đang sử dụng đường truyền Internet FPT. Phải check tồn tại HĐ.</td>
    </tr>
    <tr>
        <td>BR-02</td>
        <td>Kiểm tra trùng gói FPT Play</td>
        <td>Test case SĐT 0939536236: Nếu tài khoản FPT Play đã có gói VVIP, không cho phép mua đè gói thấp hơn, hoặc cảnh báo cộng dồn thời gian.</td>
    </tr>
    <tr>
        <td>BR-03</td>
        <td>Validate SĐT</td>
        <td>Validate 10 số theo Regex chuẩn. Không chứa ký tự đặc biệt.</td>
    </tr>
</table>
'''
    }
}

with open(template_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lấy template header từ dòng 1 đến trước <h1>A. GIỚI THIỆU</h1> (khoảng dòng 186)
header_lines = []
for line in lines:
    if "<h1>A. GIỚI THIỆU</h1>" in line or "<!-- A. GIỚI THIỆU" in line:
        break
    header_lines.append(line)

header_content = "".join(header_lines)
footer_content = "\n</div>\n</body>\n</html>"

for filename, data in out_files.items():
    # Replace title
    content = header_content.replace('FPT.VN BRD &ndash; BUSINESS REQUIREMENTS DOCUMENT', data['title'])
    content = content.replace('FPT.VN BRD - ĐĂNG KÝ COMBO INTERNET VÀ TRUYỀN HÌNH', data['title'])
    content = content.replace('FPT-BRD-REG-01-01', data['code'])
    
    # Append specific content
    content += data['content'] + footer_content
    
    # Write to file
    with open(f'/Users/hathuy/Documents/FPT-1/thuyttdoc/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Successfully generated all BRD files using template.")

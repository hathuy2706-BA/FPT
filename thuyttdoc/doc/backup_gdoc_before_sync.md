

**TÊN DỰ ÁN**

***PRD – Product Requirements Document***


| **Mã hiệu** | **1.0-BM/PM/HDCV/FTEL** |
| :---: | :---: |
| Mã hiệu | FPT-PRD-CART-001 |
| Phiên bản | 1.5 (Dự án: Xây dựng luồng giỏ hàng trên website) |



REVISION HISTORY

*\[A\]: Add – Thêm mới    \[U\]: Update – Cập nhật, thay đổi    \[D\]: Delete – Xóa*

| **Date** | **Version** | **Author** | **Reviewer** | **Approver** | **Change Description** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 06/10/2026 | 1.0 | ThuyTT104 · BA | ThuyTT104 - PO Team | PM Team | Phát hành PRD cho Dự án "Xây dựng luồng giỏ hàng trên website" |
|  |  |  |  |  |  |
|  |  |  |  |  |  |




**MỤC LỤC TÀI LIỆU**




# PART A — BUSINESS CONTEXT & RATIONALE

1. EXECUTIVE SUMMARY – TỔNG QUAN SẢN PHẨM


| **Product/Project Name** | **Xây dựng luồng giỏ hàng trên website** |
| --- | --- |
| **PO/Sponsor** | THuyTT104 |
| **Description** | Dự án "Xây dựng luồng giỏ hàng trên website" nhằm thiết lập trải nghiệm checkout hợp nhất cho phép Khách hàng chọn mua gộp nhiều thiết bị (SKU) và dịch vụ số (SA) trên FPT.vn, tự động nhận diện giỏ hàng, ẩn/hiện biểu mẫu địa chỉ nhận hàng, tự động phân luồng kích hoạt SA Instant/Pending. |
| **Business Need** | Hiện tại việc bán lẻ thiết bị và dịch vụ bị tách rời, buộc Khách hàng phải thanh toán nhiều lần gây gián đoạn trải nghiệm và làm tăng tỷ lệ bỏ giỏ (Drop-off Rate \~45%). Cần giỏ hàng gộp để tăng Average Order Value (AOV) và tự động hóa điều phối đơn hàng. |
| **Expected Outcomes** | 1. Tăng AOV thêm +15% trong Q4/2026.2. Giảm Drop-off Rate tại bước Checkout từ 45% xuống < 25%.3. Tự động hóa 100% việc điều phối đơn hàng SKU/SA và phân luồng kích hoạt dịch vụ. |
| **Target Users/Customers** | Khách hàng vãng lai (Guest Checkout) và Khách hàng đăng nhập thực hiện luồng Mua mới (Line mạng mới / Tài khoản mới) trên FPT.vn (Chưa áp dụng cho tệp KH nâng cấp HĐ cũ). |
| **In-scope / High-level Scope** | Giỏ hàng & Checkout các SPDV website bán gồm: • Camera Combo: Gói đóng gói sẵn do Kinh doanh ban hành, gồm số lượng Camera nhất định hoặc mix các loại Camera với nhau (ví dụ: Combo 2 mắt Cam, Combo Mix 1 Indoor + 1 Outdoor) kèm theo gói lưu trữ Cloud sử dụng trong combo; • Camera Only: Thiết bị Camera bán lẻ từng chiếc (có tùy chọn mua kèm gói Cloud); • Dịch vụ truyền hình FPT Play (Gói dịch vụ số SA: V.VIP 1, V.VIP 2); • Dịch vụ gia tốc mạng UltraFast (Gói cước gia tăng SA - bán mã kích hoạt); • Thiết bị phát Wi-Fi 6 Access Point AX8000C (SKU phần cứng); • Thiết bị FPT Smart Home (Ổ cắm thông minh - SKU phần cứng); • Smart TV Samsung (SKU phần cứng bán lẻ - đối tác giao hàng trực tiếp, hệ thống không kiểm tra vùng phủ giao hàng); • Luồng gộp Combo nhiều dịch vụ số (Combo SA + SA: FPT Play V.VIP & UltraFast); • Luồng gộp Combo Thiết bị + Dịch vụ số (Mix SKU + SA) cho Khách hàng vãng lai & Khách hàng đăng nhập Mua Mới. |
| **Out of Scope** | 1. Tệp Khách hàng nâng cấp Hợp đồng cũ (luồng fpt.vn/nang-cap chưa áp dụng trong giai đoạn này). 2. Gói cước Cloud Camera lẻ (Dịch vụ lưu trữ Cloud lẻ thuộc luồng nâng cấp hợp đồng hiện hữu trên fpt.vn/nang-cap, Out of Scope của giỏ hàng bán mới; không hiển thị trên website bán mới). 3. Dịch vụ Internet & Combo Internet đơn lẻ (sử dụng luồng bán hàng riêng, không áp dụng trên giỏ hàng này). 4. Gói cước HyperFast (Đã chính thức ngưng kinh doanh trên toàn hệ thống; riêng gói cước UltraFast vẫn kinh doanh và bán bình thường). 5. Giỏ hàng B2B / Khách hàng Doanh nghiệp. 6. Đổi/trả hàng trực tiếp trên giao diện Giỏ hàng. |
| **Impact if Not Done** | Khách hàng tiếp tục gặp trải nghiệm rời rạc, bỏ giỏ hàng cao, thất thoát cơ hội bán chéo (Cross-sell) thiết bị và dịch vụ số. |

1. GOALS & SUCCESS METRICS – MỤC TIÊU SẢN PHẨM/DỰ ÁN

#### **2.1 Mục tiêu cụ thể (đo được)**


| **ID** | **Goal Type** | **Goals** | **Success Metrics/KPI** | **Baseline** | **Timeframe** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| G-01 | Business Goal | Tăng doanh thu bán chéo SKU + SA | Tăng Average Order Value (AOV) thêm +15% trong Q4/2026 | AOV hiện tại | Q4/2026 |
| G-02 | Business Goal | Giảm tỷ lệ bỏ giỏ (Drop-off Rate) | Giảm Drop-off Rate tại bước Checkout từ 45% xuống < 25% | 45% drop-off | Q4/2026 |
| G-03 | Product/UX Goal | Tối ưu hóa hành trình Checkout động | Ẩn 100% Form Địa chỉ nhận hàng đối với giỏ 100% dịch vụ số SA | Phải điền địa chỉ cho mọi đơn | Ngay khi Release |
| G-04 | Ops Goal | Tự động phân luồng Kích hoạt & Thi công | Tự động phân luồng SA Instant (Online) và SA Pending (COD), giảm 30% ticket hỗ trợ | Tạo đơn thủ công | Ngay khi Release |



#### **2.2 Thuật ngữ, từ ngữ viết tắt**

| **ID** | **Thuật ngữ** | **Mô tả** |
| :---: | :---: | :---: |
| 1 | URD / PRD | Tài liệu Yêu cầu Người dùng & Đặc tả Sản phẩm chuẩn |
| 2 | SKU | Stock Keeping Unit - Thiết bị phần cứng bán lẻ (Camera, AP AX8000C, Ổ cắm Smart Home, TV Samsung) |
| 3 | SA | Service Agreement - Dịch vụ số/gói cước (FPT Play, UltraFast) |
| 4 | Cloud Camera | Dịch vụ lưu trữ đám mây đi kèm Camera (được đóng gói sẵn trong gói Camera Combo hoặc bán kèm tùy chọn khi mua Camera Only) |
| 5 | FPT Play | Dịch vụ truyền hình & giải trí trực tuyến FPT Play |
| 6 | UltraFast / HyperFast | Gói cước gia tốc UltraFast vẫn kinh doanh và bán bình thường (Chỉ riêng gói cũ HyperFast đã chính thức ngừng kinh doanh) |
| 7 | Access Point AX8000C | Thiết bị phát Wi-Fi 6 tốc độ cao |
| 8 | Smart Home Plug | Thiết bị ổ cắm thông minh IoT kết nối Wi-Fi |
| 9 | TV Samsung | Thiết bị TV Samsung bán lẻ, đối tác giao hàng trực tiếp (không kiểm tra vùng phủ giao hàng) |
| 10 | Guest Checkout | Luồng thanh toán cho Khách hàng vãng lai (không cần đăng nhập tài khoản HĐ FPT cũ) |
| 11 | FID | Hệ thống Định danh FPT ID (lưu session giỏ hàng khi KH có đăng nhập; nếu KH không đăng nhập thì lưu session trên trình duyệt/browser) |
| 12 | SPF | Smart Platform Foundation - Hệ thống quản lý đơn hàng và thanh toán tập trung của FPT (tạo đơn chính thức sau khi hoàn tất giao dịch) |
| 13 | FCP / CMS | FCP: Hệ thống Quản lý Danh mục Sản phẩm & Bảng giá tập trung (Product & Pricing Catalog). CMS: Hệ thống Quản trị & Cập nhật Nội dung (Content Management System) trên website. |
| 14 | HiFPT | Ứng dụng/Hệ thống Quản lý Khách hàng & Biên bản điện tử |
| 15 | Instant SA | Trạng thái dịch vụ số được tự động kích hoạt ngay lập tức sau khi thanh toán thành công (VNPAY) |
| 16 | Pending SA | Trạng thái dịch vụ số chờ kích hoạt (chờ KTV hoàn tất thu tiền COD cho SKU mua kèm) |
| 17 | Geolocation Check | Không áp dụng kiểm tra vùng phủ giao hàng cồng kềnh trên website (Đối tác tiếp nhận địa chỉ và giao hàng trực tiếp) |








## PART B — USERS, SCOPE & REQUIREMENTS

1. PERSONAS

| **Persona** | **Description** | **Business Goals** | **Pain Points** | **Key Activities** | **Frequency** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Khách hàng vãng lai | Khách truy cập FPT.vn chưa đăng nhập/chưa có HĐ FPT | Mua nhanh thiết bị/dịch vụ số không qua thủ tục phức tạp | Phải nhập đi nhập lại địa chỉ dù chỉ mua dịch vụ số | Chọn SP -> Thêm giỏ -> Checkout -> Thanh toán | Hàng ngày |
| Khách hàng đăng nhập (Mua mới) | Khách đã đăng nhập tài khoản FPT, thực hiện luồng Mua Mới (tài khoản/line cước mới), KHÔNG dùng nâng cấp HĐ cũ | Mua mới thiết bị/dịch vụ số gắn với tài khoản cá nhân | Chưa áp dụng cho tệp KH nâng cấp Hợp đồng cũ | Đăng nhập -> Chọn SP -> Checkout Mua mới | Thường xuyên |
| Telesales / CSKH | Nhân viên hỗ trợ tạo đơn giùm Khách hàng | Tạo đơn nhanh cho Khách qua điện thoại/Chatbot | Giao diện rườm rà, thiếu công cụ tra cứu mã lỗi | Tiếp nhận yêu cầu -> Chọn SP -> Nhập info KH -> Submit | Hàng ngày |

1. SCOPES


| **In-scope / High-level Scope** | Danh mục sản phẩm & dịch vụ (SPDV) nằm trong phạm vi luồng giỏ hàng website bán mới (FPT.vn) bao gồm: 1. Camera Combo: Gói đóng gói sẵn do Kinh doanh ban hành, gồm số lượng Camera nhất định hoặc mix các loại Camera với nhau (ví dụ: Combo 2 mắt Cam, Combo Mix 1 Indoor + 1 Outdoor) kèm theo gói lưu trữ Cloud sử dụng trong combo; 2. Camera Only: Thiết bị Camera bán lẻ từng chiếc (có tùy chọn mua kèm gói Cloud); 3. Dịch vụ truyền hình FPT Play: Gói dịch vụ số SA (V.VIP 1, V.VIP 2); 4. Dịch vụ gia tốc mạng UltraFast: Gói cước gia tăng SA (bán mã kích hoạt); 5. Thiết bị Access Point AX8000C: Thiết bị phát Wi-Fi 6 (SKU phần cứng); 6. Thiết bị FPT Smart Home: Ổ cắm thông minh Wi-Fi (SKU phần cứng); 7. Smart TV Samsung: Thiết bị phần cứng bán lẻ (đối tác giao hàng trực tiếp); 8. Các luồng mua gộp Combo giữa các SPDV trên:    • Combo dịch vụ số (Combo SA + SA: FPT Play V.VIP & UltraFast),    • Combo Thiết bị + Dịch vụ số (Combo Mix SKU + SA). (Ghi chú: Toàn bộ các quy tắc nghiệp vụ chi tiết, cơ chế tự động nhận diện giỏ hàng, phân luồng kích hoạt dịch vụ số SA, hình thức triển khai giao vận, kiểm soát số lượng tối đa SL\_Max, ràng buộc chống xung đột sản phẩm trong cùng một đơn hàng, cơ chế tick chọn sản phẩm, xóa sản phẩm và xóa sản phẩm đã tạo đơn được quy định và đặc tả đầy đủ tại Mục 5 - User Stories, Mục 6 - Acceptance Criteria và Mục 8 - Feature Detail Business Rules). |
| --- | --- |
| **Out of Scope** | 1. Tệp Khách hàng nâng cấp Hợp đồng cũ (luồng fpt.vn/nang-cap chưa áp dụng trong giai đoạn này). 2. Gói cước Cloud Camera lẻ (Dịch vụ lưu trữ Cloud lẻ thuộc luồng nâng cấp hợp đồng hiện hữu trên fpt.vn/nang-cap, Out of Scope của giỏ hàng bán mới; không hiển thị trên website bán mới). 3. Dịch vụ Internet & Combo Internet đơn lẻ (sử dụng luồng bán hàng riêng, không áp dụng trên giỏ hàng này). 4. Gói cước HyperFast (Đã chính thức ngưng kinh doanh trên toàn hệ thống; riêng gói UltraFast vẫn bán bình thường). 5. Giỏ hàng B2B / Khách hàng Doanh nghiệp. 6. Đổi/trả hàng trực tiếp trên giao diện Giỏ hàng. |
| **Tích hợp với các hệ thống khác** | - FID: Hệ thống Định danh FPT ID (chỉ lưu session giỏ hàng khi KH có đăng nhập; nếu chưa đăng nhập thì lưu trên trình duyệt/browser).- SPF: Smart Platform Foundation (API Create\_Order & Core Billing).- FCP / CMS: FCP: Hệ thống Quản lý Danh mục Sản phẩm & Bảng giá tập trung (Product & Pricing Catalog). CMS: Hệ thống Quản trị & Cập nhật Nội dung (Content Management System) trên website..- HiFPT: Hệ thống Quản lý Khách hàng & Biên bản điện tử.- Radius Server: Hệ thống kích hoạt gói cước Booster Ultrafast. |
| **Đơn vị chủ trì / phối hợp** | - Đơn vị chủ trì: Khối E-Commerce (ECOM).- Đơn vị phối hợp: ISC, FTQ, DVKH, CEM, FCM, CSOC, HiFPT. |











1. BUSINESS PROCESS


| ID | Step Name | Actor | Hành động/Mô tả thao tác | Kết quả |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Khách hàng thêm SP vào Giỏ | Khách vãng lai & KH Mua Mới | Khách hàng lựa chọn sản phẩm và bấm "Thêm vào giỏ" tại Trang chủ, Trang danh mục hoặc Trang chi tiết. | UI trang hiện tại KHÔNG thay đổi (không reload trang). Icon Giỏ hàng trên thanh Header tự động tăng số lượng hiển thị, đồng thời bung thông báo (Toast) "Thêm giỏ hàng thành công". Dữ liệu sản phẩm được lưu vào giỏ hàng phiên làm việc. |
| S-02 | Step 2: Vào Giỏ hàng & Điều chỉnh sản phẩm (/cart) | Front-End & FID Service | Khách hàng click vào Icon giỏ hàng trên Header chuyển đến /cart. Khách điều chỉnh giỏ: Tăng/giảm SL, chọn lại đặc tính sản phẩm, chọn mua thêm SP đi kèm. Sau đó tick chọn các SP cần mua để xác nhận đặt hàng và bấm "Tiếp tục". - Kiểm soát Số lượng: Khóa nút (+) khi đạt SL\_Max theo chính sách; nếu nhập vượt quá SL\_Max, khi blur (bấm ra ngoài) hệ thống tự động đưa về SL\_Max. - Ràng buộc chống xung đột: Khách hàng không thể tick chọn cùng lúc 2 sản phẩm cùng loại Camera (khác chu kỳ/khác Cloud) hoặc trùng gói cước dịch vụ khác chu kỳ; nếu tick sản phẩm thứ 2 sẽ hiển thị cảnh báo ngay tại dòng sản phẩm và tự động bỏ tick. | Hệ thống tự động tính lại tổng tiền tạm tính theo các sản phẩm được tick chọn. Chỉ chuyển tiếp các sản phẩm được tick sang Step 3. |
| S-03 | Step 3: Xem lại SP, Chọn PTTT, Ưu đãi & SP đi kèm (/checkout) | Front-End | Màn hình /checkout hiển thị danh sách SP đã tick chọn. Khách hàng xem lại sản phẩm; Chọn Phương thức thanh toán (Hệ thống hỗ trợ đa dạng: Thẻ tín dụng, ATM, ZaloPay, Apple Pay trên iOS, MoMo, VietQR, COD. Nếu giỏ hàng có SP không hỗ trợ COD ➔ Tự động ẩn COD); Chọn mã ưu đãi (Voucher/khuyến mãi); Chọn mua thêm SP đi kèm tại bước checkout. Bấm "Xác nhận đặt hàng". | Hệ thống khởi tạo Mã đơn hàng Checkout (ID Checkout) để quản lý phiên giao dịch (chưa tạo đơn hàng chính thức trên SPF). Điều hướng sang cổng thanh toán trực tuyến hoặc xác nhận đơn COD. |
| S-04 | Step 4: Thanh toán qua cổng & Trang hoàn tất (Thank You Page) | Khách hàng | Khách hàng thực hiện thanh toán qua cổng trực tuyến VNPAY (hoặc hoàn tất xác nhận đơn COD). Điều hướng tới trang hoàn thành đơn hàng. | Hiển thị trang hoàn tất giao dịch (Thành công / Thất bại). Chỉ khi giao dịch HOÀN TẤT THÀNH CÔNG, hệ thống Checkout mới gửi dữ liệu sang SPF để tạo Đơn hàng chính thức (Order ID) và phân luồng điều phối giao hàng / kích hoạt dịch vụ số SA. |
| S-05 | S-NAV-01: Điều hướng Mua Ngay (Trang chủ & Trang chi tiết) | Front-End & SPF Core | 1. Tại Trang chủ: Khách hàng bấm 'Mua ngay' ➔ Điều hướng vào Trang chi tiết sản phẩm (PDP). 2. Tại Trang chi tiết sản phẩm (PDP): Khách hàng bấm 'Mua ngay' ➔ Bỏ qua Step 2 (Giỏ hàng), đưa Khách hàng đi thẳng đến Step 3 (Checkout) ➔ Step 4. | Tối ưu trải nghiệm đặt hàng nhanh (Fast Checkout) đối với khách hàng đã có quyết định mua nhanh tại trang chi tiết sản phẩm. |
| S-06 | S-NAV-02: Cơ chế Back từ Checkout về Giỏ hàng & Quy tắc Checkbox | SPF & KTV & SA Engine | Khách hàng đang ở Màn hình Checkout (Step 3 - khi đi từ 'Mua ngay' tại PDP) bấm nút 'Quay lại' (Back to Cart) về Giỏ hàng (Step 2). Hệ thống tự động thêm sản phẩm vừa bấm 'Mua ngay' vào Giỏ hàng. QUY TẮC CHECKBOX: Tự động tick sẵn duy nhất sản phẩm vừa bấm 'Mua ngay'; toàn bộ các sản phẩm khác đã có trong giỏ trước đó sẽ ở trạng thái BỎ TICK (UNCHECK). Khách hàng có thể tick chọn thêm các sản phẩm khác để tiếp tục đi tiếp luồng giỏ hàng (Step 2 ➔ Step 3 ➔ Step 4). | Hiển thị trang Thank You, gửi SMS xác nhận đơn hàng |
| S-NAV-04 | S-NAV-04: Kiểm soát Số lượng tối đa (SL\_Max) | Front-End & Policy Engine | Đối với các sản phẩm phần cứng/thiết bị có quy định số lượng tối đa (SL\_Max) từ Chính sách kinh doanh FCP: 1) Hệ thống tự động khóa (disable) nút (+) khi số lượng trong giỏ đạt SL\_Max. 2) Nếu Khách hàng trực tiếp nhập số lượng lớn hơn SL\_Max vào ô input: Khi blur (click/tap ra ngoài vùng nhập liệu), hệ thống tự động đưa số lượng về giá trị SL\_Max và KHÔNG hiển thị thông báo Toast. | Bảo vệ giỏ hàng tuân thủ đúng định mức chính sách bán hàng của từng SPDV, ngăn chặn nhập vượt định mức. |
| S-NAV-05 | S-NAV-05: Xung đột cùng loại Camera khác chu kỳ / khác Cloud | Front-End & Giỏ Hàng Rule Engine | Tại màn hình Giỏ hàng (Step 2), nếu trong giỏ đã có 1 sản phẩm Camera Combo (ví dụ IQ4S Cloud 6T) và Khách hàng tick chọn thêm sản phẩm Camera thứ 2 cùng loại nhưng khác chu kỳ hoặc khác gói Cloud (ví dụ IQ4S Cloud 12T): Hệ thống kích hoạt quy tắc chống xung đột, lập tức hiển thị cảnh báo (Warning) ngay tại dòng sản phẩm thứ 2 vừa tick và tự động bỏ tick sản phẩm này (không cho phép chọn cả 2 vào cùng 1 đơn). | Ngăn ngừa lỗi xung đột kích hoạt hợp đồng Cloud và gói cước trên cùng một loại thiết bị trong một đơn hàng. |
| S-NAV-06 | S-NAV-06: Xung đột trùng gói cước dịch vụ khác chu kỳ | Front-End & Giỏ Hàng Rule Engine | Tại màn hình Giỏ hàng (Step 2), nếu Khách hàng đã chọn một gói cước dịch vụ SA (ví dụ FPT Play V.VIP 6 Tháng) và tiếp tục tick chọn thêm gói cước cùng loại nhưng khác chu kỳ (ví dụ FPT Play V.VIP 12 Tháng): Hệ thống hiển thị thông báo cảnh báo ngay tại line sản phẩm mới vừa tick thêm và tự động bỏ tick sản phẩm đó (uncheck), yêu cầu khách hàng chỉ chọn 01 chu kỳ duy nhất cho mỗi gói dịch vụ trên một đơn hàng. | Bảo đảm dữ liệu đơn hàng dịch vụ SA duy nhất 01 chu kỳ cước trên một tài khoản/đơn thanh toán. |



1. USER STORIES & ACCEPTANCE CRITERIA

*Mỗi User Story phải trace được tới ít nhất 1 Acceptance Criteria. Mọi AC ví dụ minh họa trong template này đều được ánh xạ ngược về đúng US tương ứng — KHÔNG để tồn tại AC không thuộc US nào, và ngược lại.*


#### **6.0 Quy ước ID — AC ID Convention (bắt buộc tuân thủ)**

*Đây là quy ước áp dụng thống nhất cho toàn bộ ISC — không tự đặt format khác khi dùng template này.*

| Thành phần | Cấu trúc quy ước & Giải thích chi tiết |
| :---: | :---: |
| User Story (US) | Định dạng: US-\[STT\] (Ví dụ: US-01, US-02... US-12). Định danh duy nhất cho từng kịch bản câu chuyện người dùng. |
| Acceptance Criteria (AC) | Định dạng: AC-\[Mã\_US\].\[STT\_Kịch\_bản\] (Ví dụ: AC-01.1.01, AC-04.1.02). Định danh tiêu chí nghiệm thu bám sát 1-1 với từng US. |
| Business Rule (BR) | Định dạng: BR-\[STT\] (Ví dụ: BR-01, BR-02). Quy tắc nghiệp vụ cố định (Reset BR-01 theo từng phân hệ tính năng FR). |
| Non-Functional Req (NFR) | Định dạng: NFR-\[STT\] (Ví dụ: NFR-01, NFR-02). Yêu cầu phi chức năng về hiệu năng, bảo mật, khả dụng. |



#### **6.1 Primary user stories**

| ID | Priority (MoSCoW) | As a... | I want to... | So that... | AC liên quan |
| :---: | :---: | :---: | :---: | :---: | :---: |
| US-01 | **Must Have** | Khách hàng mua lẻ | Tôi muốn chọn mua thiết bị phần cứng lẻ (Camera IQ4S/Play 4, AP AX8000C, SmartHome, Smart TV) trên FPT.vn | Để thêm vào giỏ hàng và xem đơn giá, số lượng rõ ràng | AC-01.1.01AC-01.1.02 |
| US-02 | **Must Have** | Khách hàng cá nhân | Tôi muốn đăng ký gói cước FPT Play V.VIP, lựa chọn phương thức kích hoạt tại giỏ hàng (Tự động kích hoạt ngay vào SĐT hoặc Nhận mã kích hoạt qua SMS để tự kích hoạt), và tùy chọn điền Form địa chỉ (không bắt buộc) | Để sử dụng dịch vụ theo nhu cầu cá nhân hoặc tặng mã cho người khác, đồng thời thanh toán trực tuyến thuận tiện | AC-02.1.01, AC-02.1.02, AC-02.1.05 |
| US-03 | **Must Have** | Khách hàng hộ gia đình | Tôi muốn đăng ký gộp nhiều dịch vụ số SA trong cùng 1 giỏ hàng (FPT Play V.VIP & UltraFast) | Để hệ thống tự động gộp chung vào một giao dịch thanh toán trực tuyến tinh gọn và phân luồng kích hoạt độc lập | AC-03.1.01, AC-03.1.02 |
| US-04 | **Must Have** | Khách hàng cá nhân | Tôi muốn chọn mua Camera Combo (gói đóng sẵn gồm số lượng Camera nhất định hoặc mix các loại Camera + gói Cloud sử dụng trong combo) hoặc Camera Only (thiết bị Camera có bán kèm gói Cloud) | Để tự động liên kết thiết bị với dịch vụ lưu trữ Cloud trong cùng một đơn hàng | AC-04.1.01, AC-04.1.02 |
| US-05 | **Should Have** | Khách hàng mua nhiều thiết bị | Tôi muốn chọn mua nhiều thiết bị phần cứng khác chủng loại (2x Indoor Camera + 1x Mesh AP AX8000C + 2x SmartHome) | Để gom chung 1 đơn hàng phần cứng duy nhất | AC-05.1.01AC-05.1.02 |
| US-06 | **Must Have** | Khách hàng mua trọn gói | Tôi muốn mua Combo kết hợp gồm Gói FPT Play V.VIP + Camera kèm gói lưu trữ Cloud + Thiết bị phát Wi-Fi AX8000C | Để giỏ hàng tự động phân luồng xử lý kỹ thuật nhưng giữ chung một lượt thanh toán trực tuyến | AC-06.1.01, AC-06.1.02 |
| US-07 | **Should Have** | Khách hàng xem giỏ hàng | Tôi muốn nhận được các gợi ý bán kèm tự động phù hợp với thiết bị đã chọn (Gói Cloud cho Camera; Bộ điều khiển cho công tắc; Thiết bị phát Wi-Fi AX8000C) | Để bấm thêm ngay 1-click vào giỏ hàng mà không cần tìm kiếm | AC-07.1.01AC-07.1.02 |
| US-08 | **Must Have** | Khách hàng mua sắm | Tôi muốn nhập mã giảm giá (Voucher code) hoặc áp dụng khuyến mãi tự động | Để hưởng ưu đãi giảm tiền mặt, %, tặng cước hoặc miễn phí vận chuyển | AC-08.1.01AC-08.1.02 |
| US-09 | **Must Have** | Khách hàng theo khu vực | Tôi muốn chọn mua thiết bị Smart TV Samsung và nhập địa chỉ nhận hàng để đối tác/đơn vị vận chuyển giao hàng tận nơi (hệ thống không kiểm tra ràng buộc vùng phủ hàng cồng kềnh trên website) | Để mua sắm thiết bị tiện lợi, nhanh chóng và nhận hàng tại nhà | AC-09.1.01AC-09.1.02 |
| US-10 | **Must Have** | Khách hàng vãng lai | Tôi muốn giỏ hàng được lưu trữ tạm thời trên trình duyệt (Guest Cookie) và tự động đồng bộ khi Đăng nhập FPT ID | Để không bị mất sản phẩm đã chọn khi tiến hành đăng nhập | AC-10.1.01AC-10.1.02 |
| US-11 | **Must Have** | Khách hàng thao tác giỏ hàng | Tôi muốn hệ thống kiểm soát số lượng tối đa (SL\_Max: khóa nút (+) khi đạt Max và tự động chuyển về SL\_Max khi nhập số lượng lớn hơn Max rồi bấm ra ngoài) | Để đảm bảo đơn hàng tuân thủ đúng hạn mức chính sách FCP trước khi thanh toán | AC-11.1.01, AC-11.1.02 |
| US-12 | **Must Have** | Khách hàng sẵn sàng mua | Tôi muốn hệ thống kiểm tra quy tắc chống xung đột tại màn hình giỏ hàng (chặn tick cùng loại Cam+Cloud khác chu kỳ/khác gói Cloud; chặn tick trùng gói cước khác chu kỳ kèm cảnh báo ngay tại line sản phẩm vừa tick) và khởi tạo ID Checkout khi bấm Tiếp tục | Để đảm bảo các sản phẩm trong cùng một đơn hàng không bị xung đột trước khi sang bước Checkout | AC-12.1.01, AC-12.1.02, AC-12.1.03, AC-12.1.04, AC-12.1.05 |
| US-13 | **Must Have** | Khách hàng mua sắm | Tôi muốn bấm 'Mua ngay' tại Trang chủ thì được chuyển vào Trang chi tiết; còn bấm 'Mua ngay' tại Trang chi tiết thì được đưa thẳng sang Bước 3 (Checkout) | Để rút ngắn thời gian mua sắm và thanh toán nhanh chóng mà không cần qua trang giỏ hàng trung gian | AC-13.1.01 AC-13.1.02 |
| US-14 | **Must Have** | Khách hàng tại Checkout | Khi tôi bấm quay lại (Back) từ Bước 3 (Checkout) về Giỏ hàng (Bước 2), tôi muốn sản phẩm vừa 'Mua ngay' tự động được lưu vào giỏ và tự động tick chọn duy nhất sản phẩm đó (các sản phẩm khác uncheck) | Để tôi có thể linh hoạt tick chọn thêm các sản phẩm khác muốn mua kèm hoặc điều chỉnh số lượng trước khi tiếp tục đặt hàng | AC-14.1.01 |
| US-15 | **Must Have** | Khách hàng tại Checkout | Tôi muốn hệ thống hiển thị đúng các phương thức thanh toán khả dụng cho giỏ hàng của tôi tùy thuộc vào từng sản phẩm (Ví dụ: Thẻ tín dụng, ATM, Ví điện tử, QR Code, COD nếu hỗ trợ...), và tự động ẩn phương thức COD nếu trong giỏ có sản phẩm không hỗ trợ COD | Để tôi lựa chọn phương thức thanh toán phù hợp và thanh toán đơn hàng thành công | AC-15.1.01 AC-15.1.02 |
| US-16 | **Must Have** | Khách hàng xem giỏ hàng | Tôi muốn bấm vào icon giỏ hàng trên thanh Header hoặc truy cập trang /cart để xem đầy đủ danh sách sản phẩm đã thêm hoặc thông báo khi giỏ hàng trống | Để tôi kiểm tra danh sách sản phẩm, số lượng, đơn giá, tùy chọn gói cước kèm theo, tổng tiền thanh toán tạm tính và thực hiện lựa chọn đặt hàng | AC-16.1.01, AC-16.1.02 |
| US-17 | **Must Have** | Khách hàng mua sắm | Tôi muốn nhận được thông báo giải thích rõ ràng và xử lý phù hợp khi thao tác thêm sản phẩm vào giỏ hàng không thể thực hiện | Để tôi hiểu lý do không thể thêm sản phẩm (đạt số lượng tối đa, xung đột sản phẩm, hết hàng hoặc lỗi kết nối) và biết hướng điều chỉnh đơn hàng phù hợp | AC-17.1.01, AC-17.1.02, AC-17.1.03 |
| US-18 | **Must Have** | Khách hàng tại giỏ hàng | Tôi muốn bấm icon Xóa tại một dòng sản phẩm để loại bỏ sản phẩm đó ra khỏi giỏ hàng | Để loại bỏ sản phẩm không còn nhu cầu mua, hệ thống tự động trừ số lượng sản phẩm trong giỏ hàng, cập nhật lại tổng số lượng hiển thị và đồng bộ ngay lập tức số lượng trên badge icon giỏ hàng ở thanh Header | AC-18.1.01, AC-18.1.02, AC-18.1.03 |
| US-19 | **Must Have** | Khách hàng tại giỏ hàng | Tôi muốn chủ động tick chọn 1, nhiều hoặc tất cả các sản phẩm muốn mua trong đợt này | Để tôi có thể phân chia mua từng nhóm sản phẩm theo nhu cầu tài chính, đồng thời hệ thống tự động kiểm tra ngay các quy tắc chống xung đột (trùng gói cước khác chu kỳ, trùng model Camera khác gói Cloud) để đảm bảo đơn hàng hợp lệ trước khi tiến hành thanh toán | AC-19.1.01, AC-19.1.02, AC-19.1.03 |
| US-20 | **Must Have** | Khách hàng thanh toán | Tôi muốn sau khi hoàn tất quá trình tạo đơn hàng (bao gồm cả trường hợp thanh toán thành công hoặc thanh toán thất bại/hoàn tất phiên tạo đơn SPF), hệ thống sẽ tự động xóa các sản phẩm của đơn đó khỏi giỏ hàng, và giữ nguyên các sản phẩm tôi chưa tick chọn | Để giỏ hàng của tôi không bị lưu trùng các sản phẩm đã xử lý đơn, đồng thời các sản phẩm còn lại chưa mua vẫn được lưu giữ nguyên vẹn để tôi tiếp tục mua sắm cho các lần sau mà không phải tìm kiếm lại | AC-20.1.01, AC-20.1.02, AC-20.1.03 |
| US-21 | **Must Have** | Quản trị viên (CMS) & Khách hàng | Tôi muốn hệ thống hỗ trợ cấu hình động từ CMS và hiển thị icon Tooltip mô tả chi tiết cạnh từng Hình thức triển khai (giao hàng/lắp đặt...) và từng Hình thức kích hoạt (tự động/nhận mã SMS) tại giỏ hàng | Để khách hàng hiểu rõ quy trình thực hiện, thời gian bàn giao và điều kiện áp dụng của từng hình thức mà không cần rời giỏ hàng, giảm tải CSKH và tối ưu tỷ lệ hoàn tất đơn | AC-21.1.01, AC-21.1.02 |
| US-22 | **Must Have** | Khách hàng tại giỏ hàng | Tôi muốn nhấp vào nút '< Quay lại' trên giao diện giỏ hàng để quay trở về đúng trang duyệt web liền trước (Trang chủ, Danh mục hoặc Chi tiết sản phẩm) hoặc fallback về Trang chủ an toàn | Để tôi có thể tiếp tục tìm kiếm và chọn thêm các sản phẩm, gói dịch vụ khác một cách thuận tiện mà không bị mất dữ liệu hay trạng thái của các sản phẩm đang có trong giỏ hàng | AC-22.1.01, AC-22.1.02 |
| US-23 | **Must Have** | Khách hàng tại giỏ hàng | Tôi muốn nhấp vào checkbox 'Chọn tất cả' ở đầu danh sách sản phẩm để chọn nhanh hoặc bỏ chọn nhanh toàn bộ sản phẩm trong giỏ hàng, đồng thời hệ thống tự động kiểm tra quy tắc xung đột | Để tôi có thể linh hoạt quyết định mua sắm toàn bộ giỏ hàng hoặc hủy chọn nhanh chóng, đảm bảo đơn hàng không bị xung đột sản phẩm hay phương thức triển khai | AC-23.1.01, AC-23.1.02, AC-23.1.03 |
| US-24 | **Must Have** | Khách hàng mua sắm | Tôi muốn khi vừa bấm 'Thêm vào giỏ hàng' thành công từ Trang chủ, Trang danh mục hoặc Trang chi tiết (PDP) và chuyển sang 'Xem giỏ hàng', sản phẩm mới thêm đó sẽ được tự động tick chọn sẵn và hiển thị đúng số lượng đã chọn | Để tôi không phải tìm kiếm và tick chọn lại sản phẩm mình vừa chủ đích muốn mua, tổng tiền tạm tính phản ánh ngay giá trị sản phẩm mới thêm và sẵn sàng cho việc tiến hành đặt hàng | AC-24.1.01, AC-24.1.02, AC-24.1.03 |
| US-25 | **Must Have** | Khách hàng mua sắm | Tôi muốn khi nhấn 'Thêm vào giỏ hàng' tại thẻ sản phẩm, trên Desktop sẽ hiển thị Side Drawer (Mini Cart) trượt từ phải sang trái, trên Mobile sẽ đẩy Modal Bottom Sheet từ dưới lên để tôi xác nhận/chọn thuộc tính sản phẩm và có thanh CTA cố định đáy màn hình | Để tôi xem nhanh tóm tắt giỏ hàng, chọn phân loại linh hoạt và quyết định đi tiếp thanh toán hoặc tiếp tục mua sắm mà không làm gián đoạn việc xem trang | AC-25.1.01, AC-25.1.02, AC-25.1.03 |
| US-26 | **Must Have** | Khách hàng mua sắm | Tôi muốn khi gặp sự cố gián đoạn kết nối, rớt mạng hoặc hết hạn phiên thanh toán (màn hình Đứt gãy luồng), hệ thống vẫn bảo toàn nguyên vẹn toàn bộ sản phẩm trong giỏ hàng và cung cấp nút CTA 'Quay lại Giỏ hàng để thử lại' | Để tôi có thể dễ dàng phục hồi giỏ hàng và hoàn tất đơn hàng nhanh chóng mà không phải tìm kiếm và chọn lại từng sản phẩm từ đầu | AC-26.1.01, AC-26.1.02 |
| US-27 | **Must Have** | Khách hàng mua sắm đơn hàng hỗn hợp | Tôi muốn tại màn hình hoàn tất đơn hàng (Step 4) hệ thống hiển thị đúng loại Form thông báo hoàn tất chính (Form 1 có ký BBĐT hoặc Form 2 cảm ơn & tổng đài 1900 6600) cùng các block chuyên biệt cho dịch vụ cấp mã code kích hoạt (UltraFast), block FPT Play kèm nút tải App FPT Play, và block phân tách hình thức triển khai | Để tôi nắm bắt rõ ràng trạng thái pháp lý hợp đồng, thực hiện kích hoạt dịch vụ số ngay tại chỗ hoặc tải ứng dụng trải nghiệm tức thì mà không gặp bất kỳ vướng mắc nào | AC-27.1.01 |


#### **6.2 Acceptance Criteria**

| AC-01.1.01 | ✅ Mua lẻ Camera Only (Happy Path) |
| :---: | --- |
| Given | Khách vãng lai chọn 1 Camera IQ trên FPT.vn và bấm 'Thêm vào giỏ'. |
| When | Hệ thống gọi API AddToCart. |
| Then | UI trang hiện tại không thay đổi (không reload trang). Icon Giỏ hàng trên thanh Header tự động tăng số lượng hiển thị, đồng thời bung thông báo (Toast) "Thêm giỏ hàng thành công". |


| AC-01.1.02 | ❌ Kiểm soát số lượng Camera vượt quá giới hạn tối đa (SL\_Max) |
| :---: | --- |
| Given | Sản phẩm Camera trong giỏ hàng có giới hạn số lượng mua tối đa theo chính sách FCP (SL\_Max = 5 thiết bị). |
| When | 1. Khách hàng bấm nút tăng (+) khi số lượng đã đạt 5; HOẶC 2. Khách hàng gõ trực tiếp số lượng lớn hơn 5 (ví dụ nhập 6) vào ô input và click/tap ra ngoài màn hình (onBlur). |
| Then | 1. Tại số lượng = 5: Hệ thống tự động khóa (disable) nút (+); 2. Khi khách hàng nhập số lượng > 5 (ví dụ nhập 6) và blur ra ngoài: Hệ thống tự động chuyển đổi giá trị về đúng số lượng tối đa (SL\_Max = 5) và KHÔNG hiển thị thông báo Toast. |


| AC-02.1.01 | ✅ Đăng ký FPT Play V.VIP & Lựa chọn phương thức kích hoạt tại Giỏ hàng |
| :---: | --- |
| Given | Khách hàng chọn gói cước FPT Play (V.VIP 1 hoặc V.VIP 2). |
| When | Khách hàng vào giỏ hàng, lựa chọn Phương thức kích hoạt: (1) Hệ thống tự động kích hoạt; HOẶC (2) Nhận mã tự kích hoạt; tùy chọn điền hoặc bỏ qua Form Địa chỉ nhận hàng và tiến hành thanh toán. |
| Then | Gói cước có số lượng cố định = 1; Form Địa chỉ hiển thị cho nhập nhưng không bắt buộc (Optional); Sau khi thanh toán thành công: Nếu chọn Tự động kích hoạt -> Hệ thống tự động kích hoạt ngay vào SĐT mua đơn; Nếu chọn Nhận mã -> Hệ thống gửi SMS mã kích hoạt cho KH tự kích hoạt (KH không cần thao tác kích hoạt tại Step 4). |


| AC-02.1.02 | ❌ Chọn trùng gói cước dịch vụ số chỉ khác chu kỳ trong cùng đơn hàng |
| :---: | --- |
| Given | Tại màn hình Giỏ hàng (Step 2), khách hàng đã tick chọn 01 gói FPT Play V.VIP (ví dụ chu kỳ 6 Tháng). |
| When | Khách hàng tick chọn thêm 01 gói FPT Play V.VIP cùng loại nhưng khác chu kỳ (ví dụ chu kỳ 12 Tháng). |
| Then | Hệ thống kiểm tra rule xung đột đơn hàng, hiển thị thông báo cảnh báo (warning) ngay tại dòng sản phẩm vừa tick thêm: 'Gói cước đã có trong giỏ hàng. Mỗi đơn hàng chỉ chọn 01 chu kỳ cước cho mỗi gói dịch vụ.' và tự động bỏ tick sản phẩm đó (uncheck). |


| AC-02.1.03 | ⚠️ Xử lý kiểm tra SĐT đang sử dụng FPT Play tại Checkout & Bật Popup báo lỗi (Nhập SĐT khác / Xóa sản phẩm) |
| --- | --- |
| Given | Khách hàng chọn gói cước FPT Play SA và đến màn hình Checkout (/checkout - Step 3), nhập Số điện thoại. |
| When | Hệ thống gọi API kiểm tra trạng thái thuê bao và phát hiện SĐT này ĐANG SỬ DỤNG dịch vụ FPT Play. |
| Then | Hệ thống hiển thị Popup Modal báo lỗi: "Quý khách đã có tài khoản FPT Play theo số {SĐT} vui lòng nhập số điện thoại khác để tiếp tục đăng ký dịch vụ online" với 2 nút hành động rõ ràng: \[Nhập SĐT khác\] (tắt popup để nhập lại SĐT) và \[Xóa sản phẩm\] (kích hoạt kiểm tra đơn hàng). Nếu SĐT không có dịch vụ FPT Play: Hệ thống cho phép đi tiếp bình thường. |


| AC-02.1.04 | ✅ Xử lý nút \[Xóa sản phẩm\] tại Popup báo lỗi tài khoản FPT Play: Phân nhánh đơn 1 SP vs đơn nhiều SP & Đẩy KHTN sang CRM |
| --- | --- |
| Given | Popup Modal báo lỗi SĐT đã có tài khoản FPT Play đang hiển thị trên màn hình Checkout. |
| When | Khách hàng bấm vào nút hành động \[Xóa sản phẩm\]. |
| Then | Hệ thống kiểm tra danh sách sản phẩm trong đơn hàng: (1) Đơn hàng KHÔNG còn sản phẩm nào khác: Hệ thống điều hướng khách hàng về Màn hình đứt gãy luồng, đồng thời tự động đẩy dữ liệu Khách hàng tiềm năng (KHTN: SĐT + Dịch vụ FPT Play) sang CRM/Telesales để liên hệ hỗ trợ; (2) Đơn hàng CÒN sản phẩm khác: Hệ thống tự động Clear gói FPT Play khỏi đơn hàng và giỏ hàng, đóng Popup Modal; khách hàng kiểm tra lại đơn hàng và tiếp tục luồng thanh toán cho các sản phẩm còn lại bình thường; đồng thời hệ thống tự động đẩy thông tin KHTN (SĐT + Dịch vụ FPT Play) sang CRM. |


| **AC-02.1.05** | **⚠️ Cảnh báo xung đột khi chọn đồng thời 2 gói FPT Play V.VIP cùng hình thức 'Tự kích hoạt'** |
| --- | --- |
| **Given** | Khách hàng có gói FPT Play V.VIP thứ nhất đã chọn hình thức 'Tự kích hoạt' và đang được tick chọn mua trong giỏ hàng. |
| **When** | Khách hàng tick chọn thêm gói FPT Play V.VIP thứ hai cũng với hình thức 'Tự kích hoạt'. |
| **Then** | Hệ thống hiển thị cảnh báo Warning (Banner/Inline tại dòng gói cước thứ hai): 'Số điện thoại của Quý khách chỉ có thể kích hoạt 01 dịch vụ FPT Play tại một thời điểm. Quý khách vui lòng chọn lại hình thức kích hoạt "Nhận mã" để lấy mã code gửi tặng cho người thân/bạn bè sử dụng.'. Đồng thời cung cấp nút chọn nhanh để chuyển hình thức sang 'Nhận mã' cho gói cước thứ hai; khi chuyển sang 'Nhận mã', cảnh báo tự động ẩn và khách hàng có thể bấm 'Tiếp tục' để thanh toán đơn hàng bình thường. |


| AC-03.1.01 | ✅ Gộp nhiều dịch vụ số SA trong cùng giỏ hàng (FPT Play V.VIP & UltraFast) |
| :---: | --- |
| Given | Khách hàng chọn gói FPT Play V.VIP và chọn tiếp gói UltraFast. |
| When | Tick chọn cả 2 dịch vụ tại trang Giỏ hàng (/cart) và tiến hành đặt hàng. |
| Then | Hệ thống tự động nhận diện luồng Combo SA + SA (FPT Play V.VIP & UltraFast), hiển thị gộp trong 1 đơn hàng, ẩn COD (chỉ thanh toán online). Form địa chỉ nhận hàng hiển thị dạng không bắt buộc (Optional) do có FPT Play (để Biz khai thác thêm thông tin) và dùng chung 01 số điện thoại đại diện. Sau khi thanh toán thành công, FPT Play xử lý kích hoạt theo đúng Phương thức kích hoạt đã lựa chọn tại Giỏ hàng (Tự động kích hoạt ngay vào SĐT hoặc Gửi SMS mã kích hoạt); UltraFast sinh mã kích hoạt tại màn hình Hoàn tất (Step 4) kèm 02 Next Actions (Sao chép mã / Kích hoạt trực tiếp theo HĐ FTEL). |


| AC-03.1.02 | Đăng ký Gói cước UltraFast (Mã kích hoạt & 2 Next Actions tại Step 4) |
| :---: | --- |
| Given | Khách hàng có nhu cầu mua gói gia tốc UltraFast (bán dưới dạng mã kích hoạt). |
| When | Khách hàng chọn gói cước UltraFast (chu kỳ 1T, 6T, 12T) -> Nhập SĐT liên hệ -> Tiến hành thanh toán. |
| Then | Hệ thống cấp mã kích hoạt UltraFast tại màn hình Hoàn tất (Step 4) mà KHÔNG cần kiểm tra SĐT có Hợp đồng Internet trước đó hay không. Không tăng/giảm số lượng (luôn = 1), ẩn 100% Form Địa chỉ giao hàng. Tại màn hình hoàn tất (Step 4) cung cấp 2 Next Actions: (1) Sao chép mã kích hoạt để gửi tặng hoặc kích hoạt sau trên FPT ID/Hi FPT; (2) Kích hoạt ngay: hệ thống kiểm tra SĐT mua hàng và lọc danh sách Hợp đồng Internet thỏa mãn ĐỒNG THỜI 3 điều kiện: (1) Là HĐ billing; (2) Đang hoạt động bình thường (Status Active/In-service); (3) Là HĐ tại FTEL (FPT Telecom). Nếu có 1 HĐ hợp lệ -> kích hoạt ngay; nếu có nhiều HĐ hợp lệ -> hiển thị danh sách cho KH chọn HĐ muốn kích hoạt; nếu không có HĐ hợp lệ -> hiển thị thông báo không tìm thấy Hợp đồng FTEL phù hợp (hướng dẫn sao chép mã để kích hoạt sau qua Hi FPT). |


| AC-03.1.03 | ✅ Modal chờ kích hoạt / chờ lấy mã UltraFast không thể đóng (Unclosable Polling Modal) |
| --- | --- |
| Given | Khách hàng vừa hoàn tất giao dịch thanh toán trực tuyến thành công cho đơn hàng dịch vụ số UltraFast trên cổng SPF. |
| When | Hệ thống điều hướng về màn hình hoàn tất và bắt đầu tiến trình kích hoạt / khởi tạo mã code. |
| Then | Hệ thống hiển thị Modal 'Chờ hệ thống kích hoạt / khởi tạo mã code' kèm Spinner hiệu ứng xoay. Modal này BẮT BUỘC KHÔNG CÓ nút đóng \[X\], người dùng click ra ngoài vùng nền mờ (backdrop) hoặc nhấn phím ESC đều BỊ CHẶN HOÀN TOÀN. Frontend thực hiện Polling API kích hoạt với chu kỳ 2s/lần (tối đa 30s) đến khi nhận được kết quả trả về. |


| AC-03.1.04 | ✅ Cơ chế Fallback thông báo gửi SMS khi Polling kích hoạt UltraFast quá hạn (Timeout) |
| --- | --- |
| Given | Modal chờ kích hoạt UltraFast đang thực hiện Polling nhưng sau 30 giây hệ thống Backend vẫn chưa trả về kết quả hoặc phản hồi mã lỗi hệ thống tạm thời. |
| When | Hết thời gian chờ (Timeout 30s) hoặc nhận mã lỗi hệ thống. |
| Then | Hệ thống tự động đóng Modal chờ và hiển thị Pop-up thông báo thân thiện: 'Hệ thống chưa thể lấy mã kích hoạt ngay lúc này. Mã kích hoạt sẽ được gửi tự động qua tin nhắn SMS tới số điện thoại \[SĐT\] của quý khách trong vòng 5 phút. Tổng đài 1900 6600 luôn sẵn sàng hỗ trợ.' Đơn hàng được ghi nhận hoàn tất an toàn. |


| AC-04.1.01 | ✅ Thêm Camera Combo đóng sẵn vào giỏ hàng (số lượng Cam/mix Cam + Cloud) |
| :---: | --- |
| Given | Khách hàng chọn gói Camera Combo trên website (gói đóng sẵn số lượng Camera nhất định hoặc mix nhiều Camera kèm gói Cloud). |
| When | Bấm 'Thêm vào giỏ hàng'. |
| Then | Giỏ hàng hiển thị đúng gói Camera Combo với đầy đủ thành phần thiết bị Camera và gói Cloud đi kèm với đơn giá Combo trọn gói đã áp chiết khấu. |


| AC-04.1.02 | ❌ Xóa thiết bị Camera tự động bóc tách gói Cloud kèm theo |
| :---: | --- |
| Given | Giỏ hàng đang có Combo Camera IQ + Cloud Storage. |
| When | Khách hàng bấm Xóa Camera IQ khỏi giỏ hàng. |
| Then | Hệ thống tự động xóa gói Cloud Storage kèm theo (do Cloud không hiển thị card riêng và không thể tồn tại độc lập mà không có Camera) và thông báo cho người dùng. |


| AC-05.1.01 | ✅ Mua nhiều thiết bị SKU khác loại |
| :---: | --- |
| Given | Khách hàng thêm 2x Camera IQ, 1x Mesh AP AX8000C, 2x SmartHome. |
| When | Xem trang Giỏ hàng. |
| Then | Tất cả 5 thiết bị được liệt kê rõ ràng từng dòng, hỗ trợ điều chỉnh số lượng/xóa riêng từng item. |


| AC-05.1.02 | ❌ Mua thiết bị vượt quá số lượng tối đa 10 |
| --- | --- |
| Given | Giỏ hàng có 10 Camera IQ. |
| When | Khách hàng bấm tăng số lượng. |
| Then | Hệ thống khóa nút (+) khi đạt SL\_Max; nếu nhập vượt SL\_Max, khi blur ra ngoài hệ thống tự động đưa về SL\_Max. |


| AC-06.1.01 | ✅ Mua Combo trọn gói |
| --- | --- |
| Given | Khách hàng chọn FPT Play V.VIP, Camera kèm gói lưu trữ Cloud và Access Point AX8000C. |
| When | Bấm Thêm vào giỏ hàng. |
| Then | Hệ thống gộp thành 1 giỏ hàng chung. |


| AC-06.1.02 | ✅ Mua chung Camera Combo và Camera Only trong cùng 1 đơn hàng |
| --- | --- |
| Given | Trong giỏ hàng có cả sản phẩm Camera Combo và Camera Only. |
| When | Khách hàng tick chọn cả hai loại để thanh toán trong cùng một đơn hàng. |
| Then | Hệ thống tiếp nhận đơn hàng bình thường, không chặn tách đơn, hiển thị Form địa chỉ nhận hàng và tạo đơn hàng thanh toán gộp chung một lượt. |


| AC-07.1.01 | ✅ Gợi ý bán kèm tự động |
| --- | --- |
| Given | Khách hàng chọn 01 thiết bị phần cứng (Camera IQ4S hoặc SmartHome) có cấu hình sản phẩm bán kèm từ hệ thống. |
| When | Hiển thị trang giỏ hàng. |
| Then | Hệ thống hiển thị gợi ý bán kèm sản phẩm phù hợp đã được khai báo từ hệ thống (ví dụ: thiết bị phát Wi-Fi AP AX8000C hoặc phụ kiện đi kèm). |


| AC-07.1.02 | ✅ Bỏ qua gợi ý |
| --- | --- |
| Given | Hệ thống gợi ý sản phẩm. |
| When | Khách không chọn thêm. |
| Then | Tiếp tục thanh toán với giỏ hàng cũ. |


| AC-08.1.01 | ✅ Áp dụng mã giảm giá hợp lệ |
| --- | --- |
| Given | Khách nhập mã voucher hợp lệ. |
| When | Bấm Áp dụng. |
| Then | Giảm trừ tổng tiền và hiển thị chi tiết giảm giá. |


| AC-08.1.02 | ❌ Nhập mã giảm giá hết hạn |
| --- | --- |
| Given | Khách nhập mã voucher hết hạn. |
| When | Bấm Áp dụng. |
| Then | Hệ thống hiển thị lỗi 'Mã giảm giá không hợp lệ'. |


| AC-09.1.02 | ❌ Bỏ trống thông tin địa chỉ nhận hàng bắt buộc khi mua Smart TV |
| --- | --- |
| Given | Trong giỏ hàng có thiết bị Smart TV Samsung (SKU phần cứng). |
| When | Nhập địa chỉ nhà. |
| Then | Hệ thống hiển thị cảnh báo validation yêu cầu điền đầy đủ Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà trước khi tiếp tục. |


| AC-10.1.01 | ✅ Đồng bộ giỏ hàng khi đăng nhập |
| --- | --- |
| Given | Khách thêm hàng dưới danh nghĩa Guest. |
| When | Khách đăng nhập FPT ID. |
| Then | Giỏ hàng Guest được đồng bộ vào tài khoản. |


| AC-10.1.02 | ✅ Xóa session khi hết hạn |
| --- | --- |
| Given | Giỏ hàng của khách hàng (Guest / Local) được lưu trữ tùy thuộc vào trình duyệt (Browser LocalStorage / Cookie). |
| When | Trình duyệt tự động xóa (clear) dữ liệu / cookie sau 30 ngày (hoặc khách hàng chủ động xóa dữ liệu duyệt web). |
| Then | Giỏ hàng tự động bị làm mới (trống) theo đúng cơ chế lưu trữ của trình duyệt. |


| AC-11.1.01 | ✅ Kiểm soát Số lượng mua tối đa (SL\_Max) từ Chính sách FCP |
| --- | --- |
| Given | Sản phẩm phần cứng có giới hạn số lượng tối đa được khai báo từ Chính sách FCP (SL\_Max). |
| When | Khách hàng tăng số lượng hoặc nhập số lượng vào ô input. |
| Then | Khóa nút (+) khi đạt SL\_Max; nếu nhập số lượng > SL\_Max, khi blur (bấm ra ngoài) hệ thống tự động đưa về mức SL\_Max. |


| AC-11.1.02 | ❌ Khóa điều chỉnh số lượng đối với Camera Combo và Dịch vụ số SA |
| --- | --- |
| Given | Trong giỏ hàng có sản phẩm Camera Combo hoặc Dịch vụ số SA (FPT Play, UltraFast). |
| When | Khách hàng xem sản phẩm tại màn hình giỏ hàng (/cart). |
| Then | Hệ thống cố định số lượng = 1, khóa hoàn toàn nút (+) và (-) hoặc ẩn ô điều chỉnh số lượng, không cho phép khách hàng thay đổi số lượng đối với Camera Combo và Dịch vụ số SA. |


| AC-12.1.01 | ✅ Khởi tạo Draft Order khi Checkout |
| --- | --- |
| Given | Giỏ hàng hợp lệ. |
| When | Bấm Tiến hành thanh toán. |
| Then | Hệ thống tạo Checkout ID. |


| AC-12.1.02 | ✅ Khôi phục giỏ hàng khi quay lại từ Checkout |
| --- | --- |
| Given | Khách từ trang Checkout. |
| When | Bấm Quay lại giỏ hàng. |
| Then | Hệ thống tự động thêm sản phẩm vừa bấm 'Mua ngay' vào Giỏ hàng. Tự động tick sẵn duy nhất sản phẩm vừa bấm 'Mua ngay', toàn bộ các sản phẩm khác đã có trong giỏ hàng trước đó sẽ bỏ tick (uncheck). Khách hàng có thể tick chọn thêm các sản phẩm khác để tiếp tục luồng giỏ hàng (Step 2 ➔ Step 3 ➔ Step 4). |


| AC-12.1.03 | ❌ Ràng buộc chống xung đột cùng model Camera khác chu kỳ / khác Cloud |
| --- | --- |
| Given | Trong giỏ hàng đã có 1 Camera Combo (ví dụ IQ4S kèm Cloud 6 Tháng). |
| When | Khách hàng tick chọn thêm sản phẩm Camera thứ 2 cùng loại nhưng khác chu kỳ hoặc khác gói Cloud (ví dụ IQ4S kèm Cloud 12 Tháng). |
| Then | Hệ thống kích hoạt quy tắc xung đột giỏ hàng, hiển thị thông báo cảnh báo (warning) ngay tại dòng sản phẩm thứ 2 vừa tick và tự động bỏ tick sản phẩm đó (uncheck), không cho phép chọn cả 2 vào cùng 1 đơn hàng. |


| AC-12.1.04 | ❌ Ràng buộc chống xung đột trùng gói cước dịch vụ khác chu kỳ |
| --- | --- |
| Given | Trong giỏ hàng đã có 1 gói cước dịch vụ SA (ví dụ FPT Play V.VIP 6 Tháng). |
| When | Khách hàng tiếp tục tick chọn thêm gói cước cùng loại nhưng khác chu kỳ (ví dụ FPT Play V.VIP 12 Tháng). |
| Then | Hệ thống hiển thị cảnh báo ngay tại line sản phẩm mới vừa tick thêm và tự động bỏ tick sản phẩm đó (uncheck), yêu cầu khách hàng chỉ chọn 01 chu kỳ duy nhất cho mỗi gói dịch vụ trên một đơn hàng. |


| AC-12.1.05 | ✅ Kiểm soát Số lượng tối đa (SL\_Max) và tự động đưa về SL\_Max khi blur |
| --- | --- |
| Given | Khách hàng đang ở màn hình Giỏ hàng (Step 2) với sản phẩm thiết bị/phần cứng có giới hạn số lượng tối đa (SL\_Max = 5 theo chính sách). |
| When | Khách hàng tăng số lượng đạt SL\_Max = 5 hoặc cố tình nhập số lượng lớn hơn SL\_Max (ví dụ nhập 6) vào ô input và click/tap ra ngoài (onBlur). |
| Then | 1) Nút (+) tự động khóa (disable) khi số lượng đạt SL\_Max. 2) Khi blur ra ngoài, hệ thống tự động đưa số lượng về giá trị SL\_Max (= 5) và hiển thị thông báo giải thích cho khách hàng. |


| AC-13.1.01 | ✅ Bấm 'Mua ngay' tại Trang chủ/Danh mục điều hướng sang Trang chi tiết (PDP) |
| --- | --- |
| Given | Khách hàng đang ở Trang chủ hoặc Trang danh mục sản phẩm của FPT.vn. |
| When | Khách hàng bấm nút 'Mua ngay' tại một thẻ sản phẩm bất kỳ. |
| Then | Hệ thống điều hướng người dùng chuyển sang Trang chi tiết sản phẩm (PDP) tương ứng để khách hàng lựa chọn cấu hình, màu sắc hoặc gói dịch vụ đi kèm. |


| AC-13.1.02 | ✅ Bấm 'Mua ngay' tại Trang chi tiết đưa thẳng sang Bước 3 (Checkout) |
| --- | --- |
| Given | Khách hàng đang ở Trang chi tiết sản phẩm (PDP) và đã chọn cấu hình sản phẩm phù hợp. |
| When | Khách hàng bấm nút 'Mua ngay'. |
| Then | Hệ thống khởi tạo ID Checkout tạm thời và đưa người dùng đi thẳng sang màn hình Checkout (Step 3) với duy nhất sản phẩm vừa chọn mà không cần qua trang Giỏ hàng trung gian. |


| AC-14.1.01 | ✅ Quay lại từ Checkout về Giỏ hàng tự động lưu sản phẩm 'Mua ngay' và tick duy nhất sản phẩm đó |
| --- | --- |
| Given | Khách hàng đang ở Màn hình Checkout (Step 3) vào từ nút 'Mua ngay' tại Trang chi tiết. |
| When | Khách hàng bấm nút 'Quay lại' (Back to Cart) về Giỏ hàng (Step 2). |
| Then | Hệ thống tự động lưu sản phẩm vừa 'Mua ngay' vào Giỏ hàng, tự động tick sẵn duy nhất sản phẩm đó (toàn bộ sản phẩm khác bỏ tick), khách hàng có thể tick thêm sản phẩm khác nếu muốn gộp đơn. |


| AC-15.1.01 | ✅ Hiển thị danh sách phương thức thanh toán phù hợp và ẩn COD khi có dịch vụ số |
| --- | --- |
| Given | Khách hàng tiến hành đặt hàng tại màn hình Checkout. |
| When | Hệ thống kiểm tra danh mục sản phẩm trong đơn hàng. |
| Then | Nếu trong đơn có sản phẩm Dịch vụ số SA (FPT Play, UltraFast), hệ thống tự động ẩn hoàn toàn phương thức COD; chỉ hiển thị các cổng thanh toán trực tuyến trả trước (Ví dụ: Thẻ ATM, Thẻ tín dụng, Ví điện tử, QR Code...). Nếu đơn thuần phần cứng (SKU) có hỗ trợ COD thì hiển thị thêm lựa chọn COD. |


| AC-15.1.02 | ✅ Cảnh báo khi người dùng chưa chọn phương thức thanh toán khả dụng |
| --- | --- |
| Given | Khách hàng ở bước thanh toán nhưng chưa click chọn bất kỳ phương thức thanh toán nào. |
| When | Khách hàng bấm nút 'Xác nhận thanh toán / Đặt hàng'. |
| Then | Hệ thống hiển thị cảnh báo yêu cầu người dùng chọn phương thức thanh toán hợp lệ trước khi tiếp tục. |


| AC-16.1.01 | ✅ Xem chi tiết danh sách sản phẩm trong giỏ hàng và tổng tiền tạm tính |
| --- | --- |
| Given | Khách hàng đã thêm ít nhất 01 sản phẩm vào giỏ hàng và truy cập trang Giỏ hàng (/cart). |
| When | Màn hình giỏ hàng tải thành công. |
| Then | Hệ thống hiển thị đầy đủ danh sách sản phẩm: Checkbox chọn mua, Hình ảnh, Tên sản phẩm, Phân loại/chu kỳ, Đơn giá, Bộ chỉnh số lượng (hoặc cố định SL=1), Thành tiền, Nút xóa. Khối Order Summary hiển thị Tổng tiền tạm tính của các sản phẩm được tick chọn và nút CTA 'Tiếp tục' sáng (enabled). |


| AC-16.1.02 | ✅ Xem giỏ hàng ở trạng thái rỗng (Empty Cart View) và điều hướng tiếp tục mua sắm |
| --- | --- |
| Given | Khách hàng chưa có sản phẩm nào hoặc đã xóa hết sản phẩm khỏi giỏ hàng (count(items) == 0). |
| When | Khách hàng bấm vào icon giỏ hàng trên Header hoặc truy cập /cart. |
| Then | Hệ thống hiển thị giao diện Giỏ hàng trống với hình minh họa, thông điệp 'Giỏ hàng của bạn đang trống' và nút CTA 'Khám phá sản phẩm ngay' điều hướng về trang chủ / danh mục FPT.vn. Badge Header ẩn hoàn toàn. |


| AC-17.1.01 | ❌ Thêm sản phẩm thất bại do đạt giới hạn số lượng tối đa (SL\_Max) |
| --- | --- |
| Given | Sản phẩm trong giỏ hàng đã đạt mức số lượng tối đa cho phép mua (SL\_Max theo chính sách FCP). |
| When | Khách hàng tiếp tục bấm nút 'Thêm vào giỏ hàng' tại trang chi tiết sản phẩm hoặc danh mục. |
| Then | Hệ thống không tăng số lượng vào giỏ, hiển thị Toast cảnh báo: 'Sản phẩm đã đạt số lượng mua tối đa cho phép ({SL\_Max} sản phẩm). Quý khách không thể thêm thêm số lượng.', giữ nguyên giỏ hàng và badge Header. |


| AC-17.1.02 | ❌ Thêm sản phẩm thất bại do xung đột gói cước / model trong cùng đơn hàng |
| --- | --- |
| Given | Giỏ hàng đã có Camera kèm Cloud chu kỳ A (hoặc gói SA chu kỳ A). |
| When | Khách hàng chọn cùng model Camera với Cloud chu kỳ B (hoặc cùng gói SA chu kỳ B) và bấm 'Thêm vào giỏ'. |
| Then | Hệ thống không thêm vào giỏ, hiển thị cảnh báo: 'Không thể chọn mua cùng một loại sản phẩm khác gói cước/chu kỳ trong cùng một đơn hàng. Quý khách vui lòng chọn 1 chu kỳ phù hợp hoặc tách thành đơn hàng khác.', giữ nguyên giỏ hàng. |


| AC-17.1.03 | ❌ Thêm sản phẩm thất bại do sản phẩm hết hàng hoặc lỗi kết nối hệ thống |
| --- | --- |
| Given | Sản phẩm khách hàng muốn mua đang ngừng kinh doanh / hết hàng, hoặc lỗi timeout kết nối API giỏ hàng. |
| When | Khách hàng bấm 'Thêm vào giỏ hàng'. |
| Then | Hệ thống không thêm sản phẩm vào giỏ, hiển thị thông báo lỗi thân thiện: 'Sản phẩm hiện đang tạm hết hàng' hoặc 'Không thể kết nối đến hệ thống giỏ hàng, quý khách vui lòng thử lại sau giây lát', không làm sai lệch badge Header. |


| AC-18.1.01 | ✅ Xóa sản phẩm thành công & trừ tổng SL giỏ hàng, cập nhật badge icon Header |
| --- | --- |
| Given | Khách hàng đang ở màn hình Giỏ hàng (/cart), giỏ có N sản phẩm, badge Header hiển thị số N. |
| When | Khách hàng bấm icon Xóa (thùng rác) tại 1 dòng sản phẩm (trên Desktop) HOẶC thực hiện thao tác vuốt ngang dòng sản phẩm từ phải sang trái (Swipe left) trên Mobile để lộ nút \[Xóa\] và nhấn nút \[Xóa\]. |
| Then | Hệ thống loại bỏ sản phẩm khỏi giỏ hàng; Tổng số lượng hiển thị giảm tương ứng; Badge icon Header lập tức cập nhật lại; Tổng tiền tạm tính tự động tính lại; hiển thị Toast 'Đã xóa sản phẩm khỏi giỏ hàng'. |


| AC-18.1.02 | ✅ Xóa sản phẩm cuối cùng đưa giỏ hàng về trạng thái rỗng và xóa badge icon Header |
| --- | --- |
| Given | Giỏ hàng chỉ còn duy nhất 01 sản phẩm cuối cùng (count(items) == 1), badge Header hiển thị số 1. |
| When | Khách hàng bấm Xóa sản phẩm đó và xác nhận. |
| Then | Hệ thống xóa sản phẩm khỏi session; badge icon Header tự động ẩn (hoặc hiển thị 0); màn hình giỏ hàng tự động chuyển sang giao diện Empty Cart hiển thị thông điệp 'Giỏ hàng của bạn đang trống', nút CTA 'Tiếp tục mua sắm' và Khối sản phẩm gợi ý đã xem (Recently Viewed Products) hiển thị 4 - 6 sản phẩm khách hàng từng xem gần nhất trên website kèm nút 'Thêm vào giỏ' nhanh. |


| AC-18.1.03 | ✅ Xóa thiết bị Camera tự động bóc tách xóa gói Cloud kèm theo và trừ đúng tổng số lượng |
| --- | --- |
| Given | Giỏ hàng có thiết bị Camera kèm gói Cloud Storage đi kèm (hoặc Camera Combo). |
| When | Khách hàng bấm Xóa thiết bị Camera đó. |
| Then | Hệ thống tự động xóa thiết bị Camera và gói Cloud gắn kèm, trừ đúng số lượng của cả 2 thành phần và cập nhật badge icon Header đồng bộ. |


| AC-18.1.04 | ✅ Quy chuẩn giao diện Pop-up Xác nhận Xóa sản phẩm (Trái: Xóa, Phải: Đóng) |
| --- | --- |
| Given | Khách hàng đang ở màn hình Giỏ hàng và nhấp vào icon Thùng rác \[Xóa\] tại một dòng sản phẩm (Desktop) hoặc vuốt ngang line sản phẩm sang trái và bấm nút \[Xóa\] (Mobile). |
| When | Hệ thống mở Pop-up Modal xác nhận xóa sản phẩm. |
| Then | Giao diện Modal tuân thủ nghiêm ngặt quy cách: Tiêu đề 'Xác nhận xóa sản phẩm'; Nội dung 'Quý khách có chắc chắn muốn xóa sản phẩm này khỏi giỏ hàng?'; Thứ tự nút hành động hiển thị: Nút bên TRÁI là nút CTA chính màu đỏ/cam 'Xóa' (bấm vào sẽ xóa SP và đóng popup); Nút bên PHẢI là nút phụ viền xám 'Đóng' (bấm vào sẽ giữ nguyên giỏ hàng và đóng popup). |


| AC-19.1.01 | ✅ Tick chọn 1, nhiều hoặc tất cả sản phẩm muốn mua và cập nhật tổng tiền thanh toán tạm tính |
| --- | --- |
| Given | Khách hàng có nhiều sản phẩm trong giỏ hàng. |
| When | Khách hàng click checkbox tại 1 dòng sản phẩm, hoặc tick nhiều dòng, hoặc click 'Chọn tất cả'. |
| Then | Hệ thống ghi nhận trạng thái đã chọn; Khối tổng tiền thanh toán tạm tính lập tức cập nhật lại CHỈ TÍNH TIỀN CHO CÁC SẢN PHẨM ĐƯỢC TICK CHỌN; Nút CTA 'Tiếp tục' sáng (enabled) kèm số lượng chọn. |


| AC-19.1.02 | ❌ Kiểm tra ràng buộc chống xung đột khi tick chọn sản phẩm (Real-time Conflict Validation) |
| --- | --- |
| Given | Khách hàng đã tick chọn một sản phẩm A trong giỏ hàng (ví dụ: Cam IQ4S + Cloud 6T, hoặc FPT Play 6T). |
| When | Khách hàng click tick chọn thêm sản phẩm thứ 2 bị xung đột nghiệp vụ (cùng model Cam IQ4S + Cloud 12T, hoặc FPT Play 12T). |
| Then | Hệ thống hiển thị cảnh báo Warning inline ngay tại dòng sản phẩm thứ 2 vừa tick: 'Không thể chọn mua cùng một loại sản phẩm khác gói cước/chu kỳ trong cùng một đơn hàng. Quý khách vui lòng chọn 1 gói phù hợp hoặc tách thành đơn hàng khác.', đồng thời TỰ ĐỘNG BỎ TICK sản phẩm thứ 2 và giữ nguyên các sản phẩm đã chọn trước đó. |


| AC-19.1.03 | ❌ Không tick chọn sản phẩm nào trong giỏ hàng (Zero Selection - Vô hiệu hóa nút Đặt hàng) |
| --- | --- |
| Given | Giỏ hàng có sản phẩm nhưng tất cả checkbox sản phẩm đều ở trạng thái bỏ chọn (unticked). |
| When | Khách hàng xem màn hình giỏ hàng. |
| Then | Tổng tiền thanh toán tạm tính hiển thị là 0 đ; Nút CTA 'Tiếp tục' bị vô hiệu hóa (disabled), hiển thị chú thích 'Vui lòng chọn ít nhất 01 sản phẩm để tiến hành thanh toán'. |


| AC-20.1.01 | ✅ Xóa sản phẩm đã chọn khi thanh toán thành công & giữ nguyên sản phẩm chưa tick |
| --- | --- |
| Given | Giỏ hàng có 4 sản phẩm (A, B, C, D). Khách hàng chỉ tick chọn sản phẩm A và B để đặt hàng (C và D không tick chọn). |
| When | Khách hàng hoàn tất thanh toán thành công tại cổng thanh toán (hoặc xác nhận tạo đơn thành công trên SPF) và sang màn hình Hoàn tất (Step 4). |
| Then | Hệ thống tự động xóa hoàn toàn sản phẩm A và B khỏi session giỏ hàng (cả trên Browser và FID); Sản phẩm C và D vẫn ĐƯỢC GIỮ NGUYÊN VẸN trong giỏ hàng; Tổng số lượng trong giỏ và badge Header được cập nhật lại theo số lượng sản phẩm còn lại (C, D). |


| AC-20.1.02 | ✅ Xóa sản phẩm đã chọn khi tạo đơn thất bại / gián đoạn thanh toán & giữ nguyên sản phẩm chưa tick |
| --- | --- |
| Given | Khách hàng đã tick chọn sản phẩm A và B để tạo đơn hàng sang SPF. |
| When | Đơn hàng đã được khởi tạo ID Checkout/Order trên SPF nhưng thanh toán trực tuyến thất bại/hủy bỏ và kết thúc phiên đặt hàng đó. |
| Then | Hệ thống xóa các sản phẩm A và B đã đưa vào đơn hàng đó khỏi giỏ hàng (tránh lưu đúp đơn); các sản phẩm C và D không tick chọn ban đầu vẫn được giữ nguyên vẹn trong giỏ hàng. |


| AC-20.1.03 | ✅ Bảo toàn nguyên vẹn giỏ hàng khi người dùng chủ động bấm Back từ Checkout về Giỏ hàng |
| --- | --- |
| Given | Khách hàng tick chọn sản phẩm A và B, bấm 'Tiếp tục' sang màn hình Checkout nhưng chưa bấm nút thanh toán/chưa hoàn tất tạo đơn SPF. |
| When | Khách hàng bấm nút 'Quay lại' (Back) về Giỏ hàng (/cart). |
| Then | Hệ thống bảo toàn nguyên vẹn toàn bộ sản phẩm A, B, C, D trong giỏ hàng; trạng thái checkbox của A và B vẫn được tick chọn sẵn như trước khi chuyển bước. |


| AC-21.1.01 | ✅ Tooltip mô tả Hình thức triển khai cấu hình động từ CMS |
| --- | --- |
| Given | Khách hàng đang tại màn hình Giỏ hàng, có sản phẩm vật lý (Thiết bị, Phụ kiện, Camera Combo...) cho phép chọn hình thức triển khai (Giao hàng tận nơi, Kỹ thuật viên lắp đặt tại nhà, Nhận tại quầy giao dịch). |
| When | Khách hàng di chuột (Hover trên Desktop) hoặc chạm nhẹ (Tap/Click trên Mobile) vào icon Tooltip \[(i)\] cạnh tên Hình thức triển khai. |
| Then | Hệ thống hiển thị popover/tooltip chứa nội dung mô tả chi tiết (ví dụ: thời gian cam kết bàn giao, phạm vi hỗ trợ kỹ thuật, chi phí dịch vụ nếu có). Toàn bộ nội dung văn bản này được lấy động từ cấu hình CMS của FPT Telecom theo mã hình thức (fulfillment\_method\_code), hỗ trợ rich text và đa ngôn ngữ, không hardcode trên giao diện. |


| AC-21.1.02 | ✅ Tooltip mô tả Hình thức kích hoạt dịch vụ số SA cấu hình động từ CMS |
| --- | --- |
| Given | Khách hàng có sản phẩm dịch vụ số SA (FPT Play, Ultra Fast...) trong giỏ hàng và đang lựa chọn Phương thức kích hoạt (Hệ thống tự động kích hoạt theo SĐT mua hàng, Nhận SMS mã kích hoạt). |
| When | Khách hàng hover hoặc tap vào icon Tooltip \[(i)\] bên cạnh tên Phương thức kích hoạt. |
| Then | Hệ thống hiển thị tooltip giải thích quy trình thực hiện (ví dụ: "Hệ thống tự động kích hoạt tài khoản ngay sau khi thanh toán thành công theo SĐT mua hàng" hoặc "Mã kích hoạt gồm 10 ký tự sẽ gửi qua tin nhắn SMS trong vòng 5 phút sau khi thanh toán thành công"). Nội dung được đồng bộ thời gian thực từ cấu hình CMS của phân hệ SA (activation\_method\_code). |


| AC-22.1.01 | ✅ Nút "Quay lại" điều hướng về đúng trang trước đó (Referrer Navigation) |
| --- | --- |
| Given | Khách hàng đang ở màn hình Giỏ hàng sau khi chuyển từ một trang duyệt web (Trang chủ, Trang danh mục sản phẩm, hoặc Trang chi tiết PDP). |
| When | Khách hàng nhấn vào nút/icon "< Quay lại" (Back) ở góc trên bên trái thanh tiêu đề giỏ hàng hoặc breadcrumb. |
| Then | Trình duyệt điều hướng người dùng quay trở lại đúng URL của trang trước đó (document.referrer trong cùng domain fpt.vn), toàn bộ vị trí cuộn trang (scroll position) và trạng thái session giỏ hàng được bảo lưu trọn vẹn, không làm mất dữ liệu sản phẩm trong giỏ. |


| AC-22.1.02 | ✅ Fallback điều hướng an toàn khi không có trang trước đó (No Referrer Fallback) |
| --- | --- |
| Given | Khách hàng truy cập trực tiếp vào link Giỏ hàng (fpt.vn/gio-hang) từ bookmark, link chia sẻ bên ngoài hoặc tab mới mà không có lịch sử điều hướng nội bộ (document.referrer rỗng hoặc ngoài domain fpt.vn). |
| When | Khách hàng nhấn nút "< Quay lại" tại màn hình Giỏ hàng. |
| Then | Hệ thống tự động fallback điều hướng khách hàng về Trang chủ (https://fpt.vn) hoặc Trang danh mục thiết bị/dịch vụ mặc định, đảm bảo trải nghiệm liền mạch và không bị lỗi 404 hoặc kẹt trang. |


| AC-23.1.01 | ✅ Tick chọn "Chọn tất cả" (Select All) danh sách sản phẩm trong giỏ hàng |
| --- | --- |
| Given | Giỏ hàng có từ 2 sản phẩm trở lên và hiện tại checkbox "Chọn tất cả" đang ở trạng thái Unchecked. |
| When | Khách hàng nhấp vào checkbox "Chọn tất cả" tại thanh header danh sách sản phẩm. |
| Then | Toàn bộ checkbox của các sản phẩm hợp lệ trong giỏ hàng đồng loạt chuyển sang trạng thái Checked; Khối Tổng tiền tạm tính và Nút "Tiếp tục" tự động tính toán lại tổng giá trị của toàn bộ các sản phẩm này. |


| AC-23.1.02 | ✅ Kiểm tra và xử lý xung đột sản phẩm khi thực hiện "Chọn tất cả" |
| --- | --- |
| Given | Giỏ hàng chứa các sản phẩm có ràng buộc xung đột nghiệp vụ (ví dụ: cùng model Camera nhưng khác gói Cloud/chu kỳ, hoặc trùng gói SA khác chu kỳ). |
| When | Khách hàng nhấp vào checkbox "Chọn tất cả". |
| Then | Hệ thống ưu tiên tick chọn các sản phẩm hợp lệ và sản phẩm đầu tiên được thêm vào; đối với sản phẩm bị xung đột, hệ thống tự động giữ trạng thái Unchecked (hoặc bỏ tick) đồng thời hiển thị thông báo cảnh báo inline: "Sản phẩm A và B không thể thanh toán cùng lúc. Vui lòng tách đơn hoặc chọn 1 trong 2", đảm bảo đơn hàng không rơi vào trạng thái lỗi thanh toán. |


| AC-23.1.03 | ✅ Thao tác "Bỏ chọn tất cả" (Deselect All) |
| --- | --- |
| Given | Checkbox "Chọn tất cả" đang ở trạng thái Checked (toàn bộ sản phẩm đang được chọn). |
| When | Khách hàng nhấp vào checkbox "Chọn tất cả" để bỏ chọn (Uncheck). |
| Then | Toàn bộ checkbox của từng sản phẩm trong giỏ hàng chuyển sang Unchecked; Khối Tổng tiền tạm tính hiển thị về 0 đ; Nút "Tiếp tục" chuyển sang trạng thái Disable (vô hiệu hóa) kèm gợi ý "Vui lòng chọn ít nhất 1 sản phẩm để thanh toán". |


| AC-23.1.04 | ⚠️ Cảnh báo khi tick chọn các sản phẩm khác Hình thức giao hàng (Tự tắt sau 7s, vẫn cho chọn bình thường) |
| --- | --- |
| Given | Giỏ hàng chứa nhiều sản phẩm có hình thức giao hàng/triển khai khác nhau (ví dụ: Sản phẩm A là thiết bị phần cứng giao tận nơi/KTV lắp đặt và Sản phẩm B là dịch vụ số kích hoạt trực tuyến). Sản phẩm A hiện đang ở trạng thái Checked. |
| When | Khách hàng nhấp vào checkbox để tick chọn thêm Sản phẩm B. |
| Then | Hệ thống VẪN CHO PHÉP tick chọn thành công Sản phẩm B (checkbox Sản phẩm B chuyển sang trạng thái Checked = True); Khối Tổng tiền tạm tính lập tức cập nhật cộng dồn giá trị của cả hai sản phẩm; Nút CTA 'Tiếp tục' sáng (enabled) cho phép đi tiếp. Đồng thời, hệ thống hiển thị thông báo cảnh báo Warning (Toast Notification / Banner màu vàng cam): 'Đơn hàng của Quý khách bao gồm các sản phẩm có hình thức giao hàng khác nhau. Quý khách vẫn có thể tiếp tục đặt hàng bình thường.'. Thông báo cảnh báo này tự động tắt (auto-dismiss) sau khoảng 7 giây (7s), hoặc khách hàng có thể chủ động bấm dấu 'x' để đóng sớm. |


| AC-24.1.01 | ✅ Tự động tick chọn sản phẩm vừa mới thêm khi chuyển vào Giỏ hàng |
| --- | --- |
| Given | Khách hàng đang ở Trang chủ, Trang danh mục hoặc Trang chi tiết sản phẩm (PDP), thực hiện nhấn nút "Thêm vào giỏ hàng" thành công. |
| When | Khách hàng nhấn nút "Xem giỏ hàng" trên Toast thông báo thành công, Popup xác nhận hoặc trên Mini-cart Header. |
| Then | Khi trang Giỏ hàng được tải, sản phẩm vừa được thêm mới BẮT BUỘC được hệ thống tự động tick chọn sẵn (Checked = True), bất kể các sản phẩm cũ trước đó đang ở trạng thái nào (nếu không có xung đột nghiệp vụ). |


| AC-24.1.02 | ✅ Đồng bộ và hiển thị chính xác số lượng đã chọn từ màn hình trước |
| --- | --- |
| Given | Khách hàng tại trang PDP chọn số lượng sản phẩm là N (N >= 1, hợp lệ theo tồn kho và hạn mức) và bấm Thêm vào giỏ hàng. |
| When | Khách hàng chuyển sang màn hình Giỏ hàng. |
| Then | Ô nhập số lượng (Stepper Counter) của sản phẩm đó tại giỏ hàng hiển thị chính xác giá trị N; nếu sản phẩm đã tồn tại từ trước trong giỏ thì số lượng được cộng dồn (Cũ + N) và hiển thị giá trị mới tương ứng. |


| AC-24.1.03 | ✅ Tự động cập nhật Khối Tổng tiền tạm tính cho sản phẩm mới tick |
| --- | --- |
| Given | Sản phẩm mới thêm vào giỏ hàng được hệ thống tự động tick chọn sẵn theo AC-24.1.01. |
| When | Trang Giỏ hàng hoàn tất tải (Page Load Complete). |
| Then | Khối "Tổng tiền tạm tính" ở cột bên phải lập tức tính toán bao gồm Thành tiền của sản phẩm mới thêm (Số lượng x Đơn giá khuyến mãi/gốc), đồng thời Nút "Tiếp tục" ở trạng thái Active cho phép khách hàng nhấn đi tiếp ngay lập tức. |


| AC-25.1.01 | ✅ Hiển thị Side Drawer (Mini Cart) trượt từ phải sang trái trên giao diện Desktop |
| --- | --- |
| Given | Khách hàng đang ở màn hình Desktop (viewport >= 1024px) tại Trang chủ hoặc Trang danh mục sản phẩm của FPT.vn. |
| When | Khách hàng nhấn nút 'Thêm vào giỏ' tại một thẻ sản phẩm bất kỳ. |
| Then | Hệ thống hiển thị thanh Side Drawer (Mini Cart) trượt êm ái từ mép phải sang trái màn hình (độ rộng chuẩn 400px, có lớp phủ mờ overlay phía sau). Drawer hiển thị hình ảnh, tên sản phẩm vừa thêm, số lượng, đơn giá, tổng tiền tạm tính hiện tại của giỏ hàng và 2 nút CTA: 'Xem giỏ hàng' (chuyển sang /cart) và 'Tiếp tục' (chuyển sang Checkout). |


| **AC-25.1.02** | **✅ Hiển thị Modal Bottom Sheet trượt từ dưới lên trên giao diện Mobile** |
| --- | --- |
| **Given** | Khách hàng đang ở màn hình Mobile (viewport < 1024px) tại Trang chủ hoặc Danh mục sản phẩm. |
| **When** | Khách hàng nhấn nút 'Thêm vào giỏ' hoặc 'Mua ngay' tại thẻ sản phẩm. |
| **Then** | Hệ thống đẩy Modal Bottom Sheet từ dưới đáy màn hình lên trên, cho phép khách hàng chọn nhanh các thuộc tính sản phẩm (màu sắc, cấu hình, gói Cloud đi kèm nếu có, số lượng) kèm nút xác nhận 'Thêm vào giỏ hàng' hoặc 'Mua ngay' tiện lợi. |


| **AC-25.1.03** | **✅ Thanh điều khiển cố định đáy màn hình Mobile (Sticky Bottom Bar)** |
| --- | --- |
| **Given** | Khách hàng đang duyệt xem trang chi tiết sản phẩm hoặc Modal Bottom Sheet trên thiết bị di động. |
| **When** | Khách hàng cuộn trang xem nội dung mô tả chi tiết sản phẩm. |
| **Then** | Khối nút hành động CTA (Thêm vào giỏ hàng, Mua ngay) luôn được cố định chắc chắn ở mép dưới cùng màn hình (Sticky Bottom Bar), không bị che khuất bởi nội dung cuộn, giúp thao tác một chạm dễ dàng. |


| **AC-26.1.01** | **✅ Hiển thị màn hình Đứt gãy luồng khi phiên thanh toán timeout hoặc mất kết nối mạng** |
| --- | --- |
| **Given** | Khách hàng đang trong quá trình chuyển tiếp từ Giỏ hàng sang Thanh toán hoặc đang ở phiên thanh toán trên SPF nhưng bị rớt mạng, lỗi kết nối hoặc phiên hết hạn (Timeout sau 15 phút không thanh toán). |
| **When** | Khách hàng quay lại trình duyệt hoặc hệ thống phát hiện phiên gián đoạn. |
| **Then** | Hệ thống điều hướng sang Màn hình 'Đứt gãy luồng' (Drop-off Screen) với hình ảnh minh họa gián đoạn, tiêu đề 'Giao dịch của quý khách đang bị gián đoạn' kèm thông điệp trấn an 'Toàn bộ sản phẩm quý khách đã chọn vẫn được lưu giữ an toàn trong giỏ hàng.' |


| **AC-26.1.02** | **✅ Cơ chế bảo toàn và phục hồi trạng thái giỏ hàng từ màn hình Đứt gãy** |
| --- | --- |
| **Given** | Khách hàng đang ở màn hình Đứt gãy luồng. |
| **When** | Khách hàng nhấn nút CTA chính '\[Quay lại Giỏ hàng để thử lại\]'. |
| **Then** | Hệ thống điều hướng khách hàng quay trở lại trang Giỏ hàng (/cart); toàn bộ các sản phẩm trong phiên đặt hàng dở dang được tự động tick chọn sẵn (Checked = True) và giữ nguyên số lượng, tổng tiền tạm tính sẵn sàng để khách hàng bấm 'Tiếp tục' thanh toán lại ngay lập tức. Nếu bấm '\[Về Trang chủ\]', hệ thống đưa về https://fpt.vn. |


| **AC-27.1.01** | **✅ Quy chuẩn hiển thị Form thông báo hoàn tất chính (Form 1 ký BBĐT vs Form 2 cảm ơn), Block kích hoạt mã code, Block FPT Play kèm nút Tải App, và Block phân tách triển khai tại Step 4** |
| --- | --- |
| **Given** | Khách hàng đã hoàn tất đặt hàng / thanh toán thành công cho đơn hàng trên hệ thống fpt.vn. |
| **When** | Hệ thống điều hướng khách hàng đến màn hình Hoàn tất đơn hàng (Step 4 / Thank You Page). |
| **Then** | Màn hình Step 4 hiển thị phân tầng trực quan tuân thủ nghiêm ngặt các quy tắc: (1) Khung thông báo hoàn tất chính:   • Nếu đơn hàng có sản phẩm cần ký BBĐT (gói cước/dịch vụ cam kết): Hiển thị Form 1 (Thông báo chúc mừng + Khung xác nhận Hợp đồng điện tử: Số HĐĐT, thông báo mã OTP ký số qua SMS, nút CTA \[Xem & Ký Hợp Đồng Điện Tử Ngay\]). KHÔNG hiển thị Form 2.   • Nếu đơn hàng chỉ gồm sản phẩm mua đứt không cần ký BBĐT: Hiển thị Form 2 (Thông điệp cảm ơn 'Cảm ơn Quý khách đã mua sắm tại FPT Telecom!', mã đơn hàng, trạng thái thanh toán thành công, và hướng dẫn liên hệ Tổng đài 1900 6600 nếu có bất kỳ nhu cầu nào cần hỗ trợ). (2) Các Block bổ sung hiển thị ngay dưới Form thông báo hoàn tất chính:   • Nếu có sản phẩm cấp mã code (UltraFast, Code SA): Hiển thị Block cấp mã kích hoạt (Code) kèm nút 'Sao chép mã' và tác vụ kích hoạt ngay trực tiếp (input nhập Số HĐ Internet và nút 'Kích hoạt ngay' gọi API tức thì).   • Nếu có dịch vụ FPT Play SA: Hiển thị Block thông báo FPT Play kèm thông tin tài khoản và nút CTA nổi bật \[Tải App FPT Play\] (hoặc mã QR scan tải app cho Smartphone/Smart TV).   • Nếu là đơn hàng hỗn hợp nhiều hình thức triển khai: Bổ sung Block phân tách hình thức triển khai (Nhóm Giao hàng tận nơi hiển thị địa chỉ 4 cấp và thời gian giao dự kiến; Nhóm Kích hoạt trực tuyến). |






1. FEATURE CATALOGUE  – DANH SÁCH CHỨC NĂNG

*Liệt kê danh mục toàn bộ tính năng ở mức tổng quan, phân loại theo trạng thái (🆕 Mới / 🔄 Cập nhật / ✅ Giữ nguyên) để đội Dev ưu tiên nguồn lực. Bảng này KHÔNG mô tả chi tiết field/UI (thuộc chương 9).*


#### **7.1 Sơ đồ tổng quan**



#### **7.2 Feature & Requirement Traceability**

| **US**  **liên quan** | **Feature** | **Mô tả** | **Ghi chú** |
| :---: | :---: | :---: | :---: |
| US01, US02 | Luồng Giỏ Hàng Camera | Hỗ trợ Camera Combo (gói đóng sẵn số lượng Cam hoặc mix các loại Cam + gói Cloud) và Camera Only (bán lẻ từng thiết bị có bán kèm Cloud). Hiển thị Form Địa chỉ . Kiểm soát SL\_Max (khóa nút +, onBlur tự chuyển về Max). Chống xung đột cùng loại Cam khác chu kỳ/khác Cloud (warning inline tại SP thứ 2 & tự bỏ tick). | Tích hợp Cloud API |
| US03 | Luồng Giỏ Hàng FPT Play | Dịch vụ số SA 100% (V.VIP 1, V.VIP 2). Ẩn Form Địa chỉ & ẩn COD. Nhập SĐT kích hoạt. Chống chọn trùng gói cước khác chu kỳ (warning inline ngay tại line SP vừa tick thêm & tự bỏ tick). | Tích hợp FPT Play Core |
| US04 | Luồng Giỏ Hàng Mix SKU+SA | Hỗ trợ Combo SA+SA (FPT Play V.VIP & UltraFast) và Mix SKU+SA. Tự động ẩn COD khi có dịch vụ SA. UltraFast mua mã code không cần check HĐ trước, cung cấp 2 Next Actions tại Step 4 (Sao chép mã / Kích hoạt theo 3 nhánh: 1 HĐ, nhiều HĐ, 0 HĐ). | Logic Pending SA |
| US05 | Luồng Giỏ Hàng Smart TV Samsung | Thiết bị SKU (AX8000C, Ổ cắm Smart Home, Smart TV Samsung). Kiểm soát SL\_Max (khóa nút +, onBlur tự đưa về SL\_Max). Tiếp nhận địa chỉ giao hàng bình thường, không kiểm tra vùng phủ giao hàng. | Đơn vị vận chuyển / Đối tác giao hàng |
| US-16, US-17, US-18, US-19, US-20 | Quy Tắc Nền Tảng Giỏ Hàng & Vòng Đời Đơn Hàng | Xem giỏ hàng, Empty state; Thêm vào giỏ không thành công; Xóa sản phẩm và cập nhật tổng SL/badge Header; Tick chọn SP và check rule trùng thời gian thực; Xóa sản phẩm đã tạo đơn (thành công/thất bại) & giữ nguyên sản phẩm chưa tick. | Frontend Cart Core & Session Engine |
| US-21, US-22, US-23, US-24 | Điều Hướng, Lựa Chọn & Cấu Hình CMS Giỏ Hàng | Cấu hình CMS động cho Tooltip Hình thức triển khai & Hình thức kích hoạt; Cơ chế Back về Referrer page an toàn; Checkbox Chọn tất cả/Bỏ chọn tất cả & kiểm soát xung đột; Tự động tick chọn và giữ số lượng khi thêm mới từ PDP/Home/Danh mục. | CMS Tooltip & Cart Interaction Engine |
| US-25, US-26 | Trải Nghiệm Mua Hàng & Khôi Phục Luồng | Drawer/Bottom sheet, Chặn fulfillment mismatch, Unclosable Polling Modal, Đứt gãy luồng | Figma Cart 1.0 Design Sync |



#### **7.3 Ma trận phân quyền**

*x = Full access — được quyền thực hiện tất cả.   x\* = Phân quyền theo nhóm quyền hoặc quyền dự án.*

| **KH Đăng nhập Mua Mới** | **Telesales / CSKH** | **Admin / ECOM** |
| :---: | :---: | :---: |
| Cho phép (Account Session Mua Mới) | Cho phép (Tạo đơn thay KH) | Cho phép |
| Cho phép (Max 10/item) | Cho phép (Max 10/item) | Cho phép |
| Cho phép (Pre-fill info mới) | Cho phép (Nhập info KH) | Cho phép |
| Cho phép (Tạo đơn KH Mua Mới) | Cho phép (Tạo đơn Sales) | Cho phép (Cấu hình Rule) |







1. FEATURE DETAIL - ĐẶC TẢ CHỨC NĂNG CHI TIẾT

#### 8.00 FR00 — Quy Tắc Nền Tảng Giỏ Hàng (Cart Mechanics, Selection, Deletion & Order Completion)

Mô tả nghiệp vụ: Đặc tả các quy tắc vận hành cốt lõi của Giỏ hàng website FPT.vn xuyên suốt vòng đời phiên mua sắm: Cơ chế hiển thị danh sách giỏ hàng và trạng thái giỏ rỗng (Empty State); Xử lý các trường hợp thêm vào giỏ không thành công; Cơ chế xóa sản phẩm và tự động cập nhật giảm số lượng tổng trong giỏ hàng cùng badge icon trên thanh Header; Cơ chế linh hoạt tick chọn sản phẩm muốn mua (1, nhiều hoặc tất cả) kèm kiểm tra ràng buộc chống xung đột thời gian thực; và Cơ chế tự động xóa các sản phẩm đã hoàn tất tạo đơn (thành công hoặc thất bại) khỏi giỏ hàng đồng thời bảo toàn các sản phẩm không tick chọn.



##### 8.00.1 Quy tắc nghiệp vụ (Business Rules)


| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| --- | --- | --- |
| BR-01 | Cơ Chế Hiển Thị Giỏ Hàng & Badge Icon Header | Khách hàng truy cập /cart hoặc click icon giỏ hàng trên thanh Header để xem danh sách sản phẩm. Badge icon trên Header hiển thị tổng số lượng sản phẩm hiện có trong giỏ hàng (total\_quantity = sum(quantity)). Khi giỏ hàng về 0 sản phẩm, badge trên Header tự động ẩn (hoặc hiển thị 0) và màn hình giỏ hàng chuyển sang giao diện Empty Cart với thông điệp 'Giỏ hàng của bạn đang trống' kèm nút CTA 'Tiếp tục mua sắm' và Khối gợi ý sản phẩm đã xem (Recently Viewed Products): Tự động trích xuất lịch sử duyệt sản phẩm của khách hàng trên website fpt.vn (từ LocalStorage / Cookie phiên duyệt web hoặc theo tài khoản FID) để hiển thị danh sách từ 4 - 6 sản phẩm mà khách hàng đã từng xem gần đây (Camera, AP, SmartHome, Smart TV, FPT Play...). Mỗi thẻ sản phẩm hiển thị đầy đủ hình ảnh, tên sản phẩm, đơn giá/giá ưu đãi và nút CTA nhanh 'Thêm vào giỏ' hoặc 'Xem chi tiết' giúp khách hàng dễ dàng tiếp tục mua sắm. |
| BR-02 | Cơ Chế Xóa Sản Phẩm Khỏi Giỏ Hàng & Trừ Số Lượng Tổng | Khi khách hàng xóa 1 dòng sản phẩm (bấm icon thùng rác trên Desktop hoặc thực hiện thao tác vuốt ngang line sản phẩm từ phải sang trái - Swipe Left trên Mobile để hiển thị nút \[Xóa\] màu đỏ và xác nhận), hệ thống loại bỏ dòng sản phẩm đó khỏi giỏ hàng, tự động trừ số lượng sản phẩm tương ứng, cập nhật lại Tổng số lượng hiển thị và đồng bộ ngay lập tức badge icon trên thanh Header. Quy chuẩn trải nghiệm UX trên Mobile (Viewport < 768px): Hỗ trợ cử chỉ vuốt chạm bản địa (Swipe-to-Reveal Action): Khách hàng có thể vuốt ngang line sản phẩm từ phải sang trái (Swipe Left). Khi vuốt vượt ngưỡng 40px (threshold), line sản phẩm trượt mượt mà sang trái khoảng 80px để lộ nút hành động \[Xóa\] màu đỏ thương hiệu FPT với icon thùng rác. Khách hàng bấm vào nút \[Xóa\] này để mở Pop-up Modal xác nhận xóa sản phẩm (với nút Xóa bên Trái, nút Đóng bên Phải theo đúng quy chuẩn giao diện). Nếu khách hàng vuốt ngược lại sang phải hoặc chạm ra ngoài line sản phẩm, line sản phẩm tự động trượt đóng về vị trí ban đầu. Nếu xóa Camera có gói Cloud kèm theo (hoặc Camera Combo), hệ thống tự động bóc tách xóa luôn gói Cloud đi kèm và trừ đúng số lượng của cả hai thành phần. |
| BR-03 | Cơ Chế Xử Lý Thêm Vào Giỏ Hàng Không Thành Công | Hệ thống từ chối thêm sản phẩm vào giỏ hàng và hiển thị cảnh báo tương ứng khi: (1) Số lượng trong giỏ đã đạt SL\_Max theo chính sách FCP (hệ thống xử lý trực tiếp trên UI: khóa nút (+) khi đạt SL\_Max và tự động clamp về SL\_Max trên sự kiện onBlur nếu nhập tay > SL\_Max, không hiển thị Toast thông báo); (2) Xung đột sản phẩm trong cùng đơn hàng: cùng model Camera khác gói Cloud/chu kỳ hoặc trùng gói SA khác chu kỳ (cảnh báo inline xung đột); (3) Sản phẩm hết hàng hoặc mất kết nối API giỏ hàng (thông báo lỗi thân thiện). Trong mọi trường hợp thất bại, giỏ hàng và badge Header giữ nguyên trạng thái hợp lệ trước đó. |
| BR-04 | Cơ Chế Tick Chọn Sản Phẩm & Kiểm Tra Xung Đột Thời Gian Thực | Khách hàng có thể tick chọn 1, nhiều hoặc tất cả sản phẩm muốn mua bằng checkbox từng dòng hoặc checkbox 'Chọn tất cả'. Tổng tiền thanh toán tạm tính chỉ tính trên các sản phẩm đang ĐƯỢC TICK CHỌN. Khi khách hàng tick chọn thêm một sản phẩm bị xung đột nghiệp vụ (cùng model Camera khác gói Cloud/chu kỳ hoặc trùng gói SA khác chu kỳ với sản phẩm đã tick trước đó), hệ thống lập tức hiển thị cảnh báo Warning inline ngay tại dòng sản phẩm vừa tick và TỰ ĐỘNG BỎ TICK (untick). Nút CTA 'Tiếp tục' chỉ kích hoạt khi count(selected\_items) >= 1. |
| BR-05 | Cơ Chế Xóa Sản Phẩm Đã Tạo Đơn & Bảo Toàn Sản Phẩm Chưa Chọn | Khi khách hàng tick chọn một tập hợp con sản phẩm (ví dụ A, B trong giỏ gồm A, B, C, D) để tiến hành Checkout và hoàn tất quá trình tạo đơn trên SPF (bao gồm cả trường hợp thanh toán trực tuyến thành công hoặc thanh toán thất bại/hủy giao dịch đã ghi nhận hoàn tất flow SPF): hệ thống tự động XÓA (CLEAR) các sản phẩm đã tạo đơn (A, B) khỏi session giỏ hàng; toàn bộ các sản phẩm không tick chọn (C, D) vẫn ĐƯỢC GIỮ NGUYÊN VẸN trong giỏ hàng. Badge icon Header cập nhật lại theo số lượng của các sản phẩm còn lại (C, D). Nếu khách hàng chủ động bấm Back từ Checkout về Giỏ hàng (chưa hoàn tất tạo đơn), toàn bộ sản phẩm A, B, C, D được giữ nguyên vẹn và giữ nguyên trạng thái tick chọn sẵn của A, B. |
| BR-06 | Cơ Chế Tooltip Mô Tả Hình Thức Triển Khai & Cấu Hình CMS | Hệ thống hỗ trợ cấu hình động nội dung tooltip (tiêu đề, mô tả chi tiết quy trình giao nhận, thời gian bàn giao dự kiến, lưu ý) cho từng Hình thức triển khai trên hệ thống CMS theo mã định danh (fulfillment\_method\_code). Trên giao diện Giỏ hàng, cạnh mỗi tùy chọn hình thức triển khai hiển thị icon tooltip \[ (i) \]; khi khách hàng hover (desktop) hoặc tap (mobile), hệ thống hiển thị popover thông tin chi tiết. Khi quản trị viên cập nhật nội dung trên CMS, thông tin phản ánh ngay lập tức trên UI giỏ hàng mà không cần triển khai lại mã nguồn frontend. |
| BR-07 | Cơ Chế Tooltip Mô Tả Hình Thức Kích Hoạt Dịch Vụ Số & Cấu Hình CMS | Tương tự như hình thức triển khai, các Phương thức kích hoạt dịch vụ số SA (như: Hệ thống tự động kích hoạt theo SĐT mua hàng, Nhận tin nhắn SMS mã kích hoạt) đều có icon tooltip \[ (i) \] cạnh tên phương thức. Nội dung giải thích quy trình kích hoạt được cấu hình động trên hệ thống CMS của phân hệ SA theo mã định danh (activation\_method\_code) và hiển thị trực quan dạng popover khi khách hàng tương tác. Mọi thay đổi về chính sách kích hoạt đều được cập nhật linh hoạt từ CMS. |
| BR-08 | Cơ Chế Điều Hướng Quay Lại Trang Trước Đó (Back to Referrer) Từ Giỏ Hàng | Khi khách hàng nhấn vào nút/icon '< Quay lại' (Back) tại màn hình Giỏ hàng, hệ thống kiểm tra URL của trang duyệt web liền trước (document.referrer nội bộ trong cùng domain fpt.vn). Nếu tồn tại referrer hợp lệ (ví dụ: Trang chủ, Trang danh mục thiết bị/dịch vụ, Trang chi tiết sản phẩm PDP), hệ thống điều hướng đưa khách hàng quay trở lại đúng trang đó, bảo toàn vị trí scroll và trạng thái dữ liệu giỏ hàng. Nếu không có referrer (truy cập trực tiếp URL giỏ hàng, bookmark, mở tab mới, hoặc chuyển hướng từ domain bên ngoài), hệ thống tự động fallback đưa về Trang chủ (https://fpt.vn) hoặc Trang danh mục chính an toàn. |
| BR-09 | Cơ Chế Checkbox Chọn Tất Cả / Bỏ Chọn Tất Cả & Kiểm Tra Xung Đột Đồng Loạt | Khách hàng có thể tick chọn hoặc bỏ chọn toàn bộ sản phẩm bằng checkbox 'Chọn tất cả' tại header danh sách sản phẩm giỏ hàng. Khi tick 'Chọn tất cả': hệ thống tiến hành kiểm tra xung đột thời gian thực; nếu phát hiện các sản phẩm có xung đột nghiệp vụ (cùng model Camera khác gói Cloud/chu kỳ hoặc trùng gói SA khác chu kỳ), hệ thống ưu tiên giữ tick các sản phẩm hợp lệ và sản phẩm đầu tiên được thêm vào, tự động bỏ tick sản phẩm xung đột đồng thời hiển thị thông báo cảnh báo inline rõ ràng. Tổng tiền thanh toán tạm tính được tính toán lại theo đúng các sản phẩm đang được tick. Khi bỏ tick 'Chọn tất cả': toàn bộ sản phẩm chuyển về Unchecked, tổng tiền tạm tính = 0 đ và vô hiệu hóa nút 'Tiếp tục'. |
| BR-10 | Cơ Chế Tự Động Tick Chọn & Giữ Nguyên Số Lượng Khi Thêm Mới Vào Giỏ Hàng | Khi khách hàng thực hiện 'Thêm vào giỏ hàng' thành công từ Trang chủ, Trang danh mục hoặc Trang chi tiết sản phẩm (PDP) và nhấn 'Xem giỏ hàng', sản phẩm vừa mới thêm BẮT BUỘC ĐƯỢC TỰ ĐỘNG TICK CHỌN SẴN (Checked = True) khi vào giỏ hàng. Đồng thời, bộ đếm số lượng (Quantity Stepper Counter) của sản phẩm đó trong giỏ hàng hiển thị chính xác số lượng đã chọn ở màn hình trước đó (hoặc cộng dồn nếu sản phẩm đã có sẵn trong giỏ). Khối Tổng tiền tạm tính tự động tính gộp thành tiền của sản phẩm mới này và Nút 'Tiếp tục' ở trạng thái kích hoạt sẵn sàng để khách hàng tiến hành thanh toán ngay lập tức. |
| BR-11 | Cơ Chế Cảnh Báo Khi Chọn Sản Phẩm Khác Hình Thức Giao Hàng (Tự Tắt Sau 7s) | Khi giỏ hàng có nhiều sản phẩm với hình thức giao hàng/triển khai khác nhau (ví dụ: sản phẩm phần cứng giao tận nơi và sản phẩm dịch vụ số kích hoạt trực tuyến): Khi khách hàng đã tick chọn sản phẩm thứ nhất và tiếp tục tick chọn thêm sản phẩm thứ hai có hình thức giao hàng khác loại, hệ thống VẪN CHO PHÉP tick chọn bình thường (checkbox sản phẩm thứ hai ghi nhận trạng thái Checked = True, tính gộp thành tiền vào Tổng tạm tính). Đồng thời, hệ thống hiển thị thông báo cảnh báo Warning (Toast Notification / Banner màu vàng cam) thông báo cho khách hàng biết về việc đơn hàng gồm các hình thức giao hàng khác nhau; thông báo cảnh báo này tự động tắt (auto-dismiss) sau khoảng 7 giây (7s) hoặc khách hàng có thể bấm đóng chủ động. Nút CTA 'Tiếp tục' vẫn ở trạng thái kích hoạt (enabled) cho phép đi tiếp sang bước thanh toán. |
| BR-12 | Cơ Chế Hiển Thị Khung Hoàn Tất Chính & Các Khối Chức Năng Bổ Sung Tại Step 4 Màn Hình Hoàn Tất | Tại màn hình hoàn tất đơn hàng (Step 4 - Order Confirmation / Thank You Page), hệ thống quy định cấu trúc hiển thị phân tầng chuyên biệt như sau: (1) Hai loại Form thông báo hoàn tất chính (Hiển thị có điều kiện loại trừ lẫn nhau - Exclusive): • Form 1 (Có sản phẩm cần ký kết Hợp đồng / Biên bản điện tử - BBĐT): Áp dụng khi đơn hàng có chứa ít nhất 01 sản phẩm/dịch vụ yêu cầu ký kết pháp lý BBĐT (ví dụ: gói cước Internet, gói combo thiết bị cam kết, hoặc dịch vụ có hợp đồng cung cấp dịch vụ viễn thông). Giao diện hiển thị: Tiêu đề chúc mừng đặt hàng thành công + Khung thông báo xác nhận hợp đồng điện tử: Số HĐĐT, thông báo mã OTP ký số đã gửi về SĐT của khách hàng, nút CTA trực tiếp \[Xem & Ký Hợp Đồng Điện Tử Ngay\] hoặc hướng dẫn ký qua SMS/Zalo OA. QUY TẮC ƯU TIÊN TUYỆT ĐỐI: Nếu đơn hàng có bất kỳ sản phẩm nào cần ký hợp đồng thì BẮT BUỘC hiển thị Form 1, TUYỆT ĐỐI KHÔNG hiển thị Form 2. • Form 2 (Thông báo hoàn tất thông thường - Không có ký BBĐT): Áp dụng khi đơn hàng CHỈ gồm các sản phẩm mua đứt không yêu cầu ký hợp đồng (Camera Only, AP AX8000C, Ổ cắm SmartHome, Smart TV Samsung, hoặc mã code dịch vụ số thông thường). Giao diện hiển thị: Thông điệp cảm ơn khách hàng đã tin tưởng lựa chọn mua sắm tại FPT Telecom ('Cảm ơn Quý khách đã mua sắm tại FPT Telecom!'), mã đơn hàng, trạng thái thanh toán thành công, và Hướng dẫn khách hàng liên hệ Tổng đài hỗ trợ CSKH 24/7 (1900 6600) nếu có bất kỳ nhu cầu nào cần hỗ trợ. (2) Các Block bổ sung hiển thị ngay dưới Form thông báo hoàn tất chính: • Block Dịch vụ cấp mã code & Tác vụ kích hoạt điện tử (VD: UltraFast, Code SA): Hiển thị khi đơn hàng có sản phẩm dịch vụ số cấp mã kích hoạt. Hiển thị mã Code kèm nút \[Sao chép mã\], thời hạn sử dụng và Tác vụ kích hoạt trực tiếp ngay tại trang (Input nhập Số hợp đồng Internet / Tài khoản và nút CTA \[Kích hoạt ngay\] không cần rời màn hình). • Block Dịch vụ FPT Play SA & Nút Tải App FPT Play: Hiển thị khi đơn hàng có sản phẩm FPT Play (V.VIP 1, V.VIP 2). Hiển thị thông tin tài khoản FPT Play, thông điệp sẵn sàng trải nghiệm và nút CTA nổi bật \[Tải App FPT Play\] (hoặc mã QR scan tải ứng dụng trên Smartphone/Smart TV) kèm nút \[Trải nghiệm ngay trên Web\]. • Block Phân tách hình thức triển khai: Đối với các đơn hàng gộp từ 2 sản phẩm trở lên có hình thức triển khai khác nhau, hệ thống hiển thị riêng biệt từng Block tương ứng (Block Giao hàng tận nơi hiển thị địa chỉ 4 cấp và thời gian giao dự kiến; Block Dịch vụ số hiển thị trạng thái kích hoạt). |



##### 8.00.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)

Sơ đồ luồng nghiệp vụ quy định vòng đời quản lý sản phẩm trong giỏ hàng: Duyệt sản phẩm -> Thêm vào giỏ (thành công/thất bại) -> Xem giỏ hàng & badge Header -> Tick chọn sản phẩm & kiểm tra xung đột thời gian thực -> Xóa sản phẩm & trừ số lượng -> Checkout & Hoàn tất tạo đơn -> Xóa sản phẩm đã tạo đơn và bảo toàn sản phẩm chưa chọn.



##### 8.00.3 Các bước thực hiện chi tiết


| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| --- | --- | --- | --- | --- |
| S-01 | Xem Giỏ Hàng & Kiểm Tra Số Lượng | Khách hàng & Front-End | Khách bấm icon Giỏ hàng trên Header hoặc truy cập /cart | Hiển thị danh sách sản phẩm hoặc giao diện Empty State nếu giỏ rỗng; hiển thị đúng badge Header. |
| S-02 | Tick Chọn Sản Phẩm Muốn Mua | Khách hàng & Front-End | Khách hàng click checkbox từng dòng hoặc checkbox 'Chọn tất cả' | Hệ thống kiểm tra rule xung đột; nếu xung đột -> warning inline & untick; nếu hợp lệ -> cập nhật Tổng tiền tạm tính. |
| S-03 | Xóa Sản Phẩm Ra Khỏi Giỏ | Khách hàng & Front-End | Khách hàng bấm icon Xóa (thùng rác) và xác nhận | Loại bỏ item khỏi giỏ hàng, trừ tổng số lượng và cập nhật badge icon Header; nếu giỏ về 0 chuyển sang Empty State. |
| S-04 | Tiến Hành Đặt Hàng (Checkout) | Khách hàng & Front-End | Khách bấm 'Tiếp tục' khi có >= 1 sản phẩm được tick | Khởi tạo ID Checkout, điều hướng sang Step 3 Checkout kèm danh sách sản phẩm được chọn; nếu bấm Back giữ nguyên giỏ hàng. |
| S-05 | Hoàn Tất Tạo Đơn & Clear Giỏ Hàng | SPF & Front-End | Khách hoàn tất thanh toán thành công hoặc kết thúc phiên tạo đơn SPF thất bại | Hệ thống xóa toàn bộ sản phẩm đã tạo đơn khỏi giỏ hàng, bảo toàn các sản phẩm chưa tick chọn, cập nhật badge Header. |
| S-00.06 | Tương tác Tooltip Hình thức triển khai & Kích hoạt | Người dùng / Frontend | Người dùng hover hoặc tap vào icon (i) cạnh Hình thức triển khai hoặc Hình thức kích hoạt; Frontend đọc tooltip\_content cấu hình từ CMS và hiển thị popover thông tin chi tiết. | Popover hiển thị đúng nội dung CMS |
| S-00.07 | Nhấn nút '< Quay lại' từ Giỏ hàng | Người dùng / Frontend | Khách hàng bấm nút Quay lại; Frontend kiểm tra document.referrer nội bộ. Nếu hợp lệ điều hướng về trang trước, nếu không có referrer tự động fallback về Trang chủ fpt.vn. | Người dùng quay về trang trước đó |
| S-00.08 | Thao tác Checkbox 'Chọn tất cả' | Người dùng / Cart Engine | Khách hàng tick hoặc bỏ tick 'Chọn tất cả'; Hệ thống cập nhật hàng loạt checkbox sản phẩm, kiểm tra xung đột nghiệp vụ, tính lại tổng tiền tạm tính và cập nhật nút Đặt hàng. | Toàn bộ SP hợp lệ được chọn / bỏ chọn |
| S-00.09 | Tự động tick chọn và giữ số lượng khi thêm mới | Hệ thống Giỏ hàng | Khách hàng thêm SP từ PDP/Home/Listing và bấm 'Xem giỏ hàng'; Hệ thống mở giỏ hàng, tự động tick chọn sản phẩm vừa thêm, hiển thị đúng số lượng đã chọn và cộng tiền tạm tính. | Sản phẩm mới thêm được tick sẵn & count đúng SL |



##### 8.00.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)


| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| --- | --- | --- | --- |
| Checkbox chọn sản phẩm | Optional | Checkbox | Mặc định tick chọn khi thêm mới; cho phép khách hàng bỏ chọn hoặc tick chọn lại. |
| Checkbox 'Chọn tất cả' | Optional | Checkbox | Tick/bỏ tick đồng loạt tất cả các sản phẩm hợp lệ trong giỏ hàng. |
| Icon Xóa sản phẩm (Thùng rác) | Enabled | Action Button | Hiển thị modal xác nhận xóa; sau khi xóa, trừ số lượng và cập nhật badge Header. |
| Badge Counter trên Header | Dynamic | Badge Tag | Hiển thị tổng số lượng sản phẩm trong giỏ; tự động ẩn khi giỏ hàng về 0. |
| Nút CTA 'Tiếp tục' | Dynamic | Button CTA | Chỉ sáng (enabled) khi có ít nhất 1 sản phẩm được tick chọn; hiển thị số lượng chọn. |
| Tooltip Hình thức triển khai | Hiển thị | Icon Tooltip \[ (i) \] | Di chuột hoặc chạm vào icon (i) cạnh tùy chọn triển khai để mở popover giải thích quy trình giao hàng/lắp đặt. Nội dung đồng bộ từ CMS (fulfillment\_method\_code). |
| Tooltip Hình thức kích hoạt | Hiển thị | Icon Tooltip \[ (i) \] | Di chuột hoặc chạm vào icon (i) cạnh tùy chọn kích hoạt SA để mở popover giải thích quy trình tự động/SMS mã kích hoạt. Nội dung đồng bộ từ CMS (activation\_method\_code). |
| Nút Điều Hướng Quay Lại | Bắt buộc | Button \[< Quay lại\] | Đặt ở góc trên bên trái màn hình giỏ hàng; click để quay lại trang duyệt web trước đó (referrer) hoặc fallback về Trang chủ fpt.vn nếu không có referrer. |
| Checkbox 'Chọn tất cả' | Tùy chọn | Master Checkbox | Đặt tại thanh tiêu đề danh sách giỏ hàng; hỗ trợ 3 trạng thái (Checked / Unchecked / Indeterminate). Tick để chọn toàn bộ SP hợp lệ; bỏ tick để hủy chọn toàn bộ. |
| Stepper Số Lượng SP Mới | Bắt buộc | Quantity Counter \[-\] N \[+\] | Tự động đồng bộ số lượng N đã chọn từ PDP; hiển thị sẵn và hỗ trợ tăng/giảm trong hạn mức quy định của sản phẩm. |
| Pop-up Xác nhận Xóa sản phẩm | Bắt buộc | Dialog Pop-up Modal | Hiển thị khi click icon Thùng rác. Gồm tiêu đề "Xác nhận xóa sản phẩm", nội dung "Bạn có chắc chắn muốn xóa sản phẩm này khỏi giỏ hàng?", 2 nút hành động: Nút "\[Xóa\]" bên TRÁI (màu đỏ/cam), Nút "\[Đóng\]" bên PHẢI (viền xám). Click ra ngoài hoặc bấm ESC tương đương đóng popup mà không xóa. |
| Side Drawer Thêm Giỏ Hàng (Desktop) | Tùy chọn | Right Drawer (Mini Cart) | Kích hoạt khi click "Thêm vào giỏ" tại card SP trên Desktop (viewport >= 1024px). Độ rộng cố định 400px trượt từ mép phải sang trái, kèm lớp nền mờ overlay. Hiển thị SP vừa thêm, số lượng, đơn giá, tổng tiền giỏ hàng, nút "\[Xem giỏ hàng\]" và "\[Tiếp tục\]". |
| Bottom Sheet Thêm Giỏ Hàng (Mobile) | Tùy chọn | Bottom Sheet Modal | Kích hoạt khi click "Thêm vào giỏ" tại card SP trên Mobile (viewport < 1024px). Đẩy từ dưới đáy màn hình lên, hiển thị SP vừa thêm, cấu hình phân loại, số lượng và nút CTA "\[Xem giỏ hàng\]". |
| Thanh điều hướng cố định chân trang (Sticky Bottom Bar) | Bắt buộc | Fixed Bar (Bottom Nav) | Thanh cố định sát mép dưới màn hình (Mobile & Desktop khi cuộn trang) hiển thị tổng tiền tạm tính và nút CTA "\[Tiếp tục\]" để đảm bảo khách hàng luôn nhìn thấy hành động chuyển bước thanh toán. |



##### 8.00.5 Edge Cases & Bảng mã lỗi chi tiết


| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| --- | --- | --- | --- |
| ERR-01 | Đạt hoặc nhập số lượng vượt quá số lượng mua tối đa cho phép (SL\_Max) | Không hiển thị Toast thông báo. Hệ thống xử lý trực tiếp trên UI (Silent control): Khóa nút (+) khi đạt SL\_Max và tự động clamp về SL\_Max trên sự kiện onBlur khi khách hàng nhập tay > SL\_Max. | Khóa (disable) nút (+) khi đạt SL\_Max. Nếu khách hàng nhập số lượng > SL\_Max vào ô input, khi click ra ngoài (sự kiện onBlur), hệ thống tự động gán giá trị về lại SL\_Max và cập nhật lại thành tiền tương ứng, không bung bất kỳ thông báo Toast nào. |
| WRN-01 | Tick chọn sản phẩm bị xung đột nghiệp vụ (cùng Cam khác Cloud, trùng SA khác chu kỳ) | Warning inline: 'Không thể chọn mua cùng một loại sản phẩm khác gói cước/chu kỳ trong cùng một đơn hàng. Quý khách vui lòng chọn 1 gói phù hợp hoặc tách thành đơn hàng khác.' | Tự động bỏ tick (untick) sản phẩm vừa chọn và giữ nguyên các sản phẩm đã tick trước đó. |
| ERR-02 | Lỗi kết nối API giỏ hàng hoặc session gián đoạn | Toast: 'Không thể cập nhật giỏ hàng lúc này, vui lòng kiểm tra kết nối mạng và thử lại sau giây lát.' | Giữ nguyên dữ liệu giỏ hàng trên local cache, không làm sai lệch số lượng. |
| ERR-03 | Không xác định được trang trước đó (Direct access / No Referrer) | Hệ thống tự động fallback điều hướng người dùng về Trang chủ fpt.vn an toàn khi bấm nút Quay lại, không báo lỗi 404. | Khách hàng mở trực tiếp link giỏ hàng hoặc từ ứng dụng ngoài không có referrer nội bộ fpt.vn. |
| WRN-02 | Xung đột sản phẩm khi tick 'Chọn tất cả' | Hệ thống ưu tiên tick SP hợp lệ đầu tiên, tự động bỏ tick SP xung đột và hiển thị thông báo cảnh báo inline giải thích lý do. | Giỏ hàng có các sản phẩm xung đột nghiệp vụ thanh toán cùng lúc (Camera khác gói Cloud, SA khác chu kỳ). |
| ERR-04 | Lỗi tải dữ liệu Tooltip từ CMS (Timeout / Network Error) | Frontend tự động fallback hiển thị nội dung mô tả mặc định (Fallback text) nhúng sẵn trong client, không làm gián đoạn tương tác người dùng. | Kết nối tới CMS API cấu hình tooltip bị gián đoạn hoặc phản hồi chậm quá 1.5s. |
| ERR-05 | Mất kết nối mạng / Timeout phiên thanh toán (Đứt gãy luồng) | Màn hình "Đứt gãy luồng" (Drop-off Recovery): "Đã xảy ra gián đoạn kết nối trong quá trình đặt hàng. Đơn hàng của bạn đã được lưu lại." | Hiển thị 2 nút CTA: Nút chính "\[Quay lại Giỏ hàng để thử lại\]" (chuyển về /cart, tự động tick chọn lại 100% các sản phẩm của đơn hàng dở dang, bảo toàn số lượng và tổng tiền), Nút phụ "\[Về Trang chủ\]" (chuyển về https://fpt.vn). Không làm mất giỏ hàng của khách hàng. |




#### **8.01 FR01 — Luồng Giỏ Hàng Camera (Lẻ, Combo Cloud & Mix Camera)**

Mô tả nghiệp vụ: Đặc tả chi tiết trải nghiệm chọn mua Camera Indoor/Outdoor, Camera Combo Cloud (6T/12T) hoặc Mix Camera. Luồng yêu cầu điền địa chỉ nhận hàng để giao hàng/lắp đặt.

##### 8.01.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| --- | --- | :---: |
| BR-01 | Hiển thị Form Địa chỉ | Khi giỏ hàng có chứa sản phẩm Camera (SKU), bắt buộc hiển thị Form Địa chỉ nhận hàng (Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà/Đường). |
| BR-02 | Logic Tải giá Cloud | Hỗ trợ 2 phân loại bán mới trên giỏ hàng: (1) Camera Combo: Gói đóng gói sẵn do Kinh doanh cấu hình, gồm số lượng Camera nhất định hoặc mix các loại Camera với nhau (ví dụ: Combo 2 mắt Cam, Combo Mix 1 Indoor + 1 Outdoor) kèm theo gói lưu trữ Cloud sử dụng trong combo; (2) Camera Only: Thiết bị Camera bán lẻ từng chiếc, có tùy chọn mua kèm gói Cloud. Khi chọn/đổi gói Cloud kèm thiết bị, hệ thống tự động tính toán và cập nhật lại tổng tiền tạm tính. |
| BR-03 | Không Quản Lý Phân Tách Nội Bộ SPF | Hệ thống Giỏ hàng/Website không quản lý logic phân tách đơn hàng hay bóc tách kỹ thuật nội bộ của hệ thống SPF. Giỏ hàng có trách nhiệm truyền nhận đầy đủ, chính xác toàn bộ dữ liệu đơn hàng (SKU phần cứng, gói Camera Combo, dịch vụ số SA, thông tin khách hàng) sang SPF; việc phân tách, điều phối và xử lý đơn hàng nội bộ hoàn toàn do hệ thống SPF tự động quản lý theo nghiệp vụ backend. |
| BR-04 | Giới Hạn Số Lượng Camera | Số lượng từng mẫu Camera không quá SL\_Max (theo chính sách FCP). Khóa nút (+) khi đạt SL\_Max; nếu nhập vượt SL\_Max, khi blur (bấm ra ngoài) hệ thống tự động đưa về SL\_Max. |
| BR-05 | Không Tăng Giảm SL Camera Combo | Gói Camera Combo được Kinh doanh đóng gói cố định về số lượng thiết bị và gói Cloud thành phần (khách hàng không tách lẻ từng thiết bị bên trong Combo). Hệ thống cố định số lượng = 1 đối với Camera Combo và Dịch vụ số SA, khóa hoàn toàn nút (+) và (-) không cho phép tăng giảm số lượng; nếu thêm lần 2 cùng gói đã tồn tại, hệ thống cảnh báo “Sản phẩm đã tồn tại trong giỏ hàng”. |
| BR-06 | Hỗ Trợ Thanh Toán Chung Camera Combo và Camera Only | Hệ thống cho phép khách hàng mua và thanh toán chung Camera Combo cùng Camera Only trong 1 đơn hàng. Khi tạo đơn hàng sang SPF/Core Billing, hệ thống tự động bóc tách đầy đủ các dòng SKU phần cứng Camera và các dòng SA Cloud tương ứng của cả hai loại. |
| BR-07 | Ràng Buộc Trùng Loại Camera Khác Chu Kỳ / Khác Cloud | Khách hàng không thể tick chọn cùng lúc 2 sản phẩm cùng loại Camera (khác chu kỳ hoặc khác gói Cloud). Nếu tick chọn sản phẩm thứ 2, hệ thống hiển thị cảnh báo ngay tại dòng sản phẩm và tự động bỏ tick. |



##### 8.01.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.01.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| --- | --- | :---: | :---: | :---: |
| S-01 | Chọn thiết bị | Khách hàng | Chọn mẫu Camera (IQ4S, Play 4) theo Combo Cloud billing / Cam Only kèm Cloud / Cam Only -> Click 'Thêm vào giỏ' | Lưu vào Session giỏ hàng (Browser LocalStorage nếu chưa đăng nhập; đồng bộ DB FID nếu đã đăng nhập) |
| S-02 | Tải giỏ hàng | Front-End | FE gọi API Get\_Cart\_Metadata, đếm count(SKU) >= 1 | Render Form Địa chỉ nhận hàng |
| S-03 | Nhập địa chỉ | Khách hàng | Nhập SĐT, Họ tên, Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà | Validate địa chỉ giao hàng hợp lệ |
| S-04 | Submit Đơn hàng | Khách hàng & SPF | Chọn PTTT VNPAY/COD -> Click 'Đặt hàng' | Tạo Order ID trên SPF, chuyển đơn tới KTV giao lắp |



##### 8.01.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Form Địa chỉ Giao hàng | Required | Address Form | Yêu cầu đủ 4 cấp: Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà/Đường. |
| Input Số lượng Camera | Required | Numeric Box (+/-) | Lựa chọn gói Cloud theo loại: Combo Cloud billing, Cam Only kèm Cloud, Cam SA (chọn sau). Khóa nút (+) khi đạt SL\_Max; tự động đưa về SL\_Max khi blur. |
| Dropdown Gói Cloud | Optional | Select Box | Lựa chọn Không Cloud, Gói 6 Tháng, Gói 12 Tháng. |



##### 8.01.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Vượt quá số lượng tối đa (SL\_Max) | Không hiển thị Toast thông báo. Xử lý trực tiếp trên UI: Khóa nút (+) khi đạt SL\_Max và tự động đưa về SL\_Max khi blur. | Khóa nút (+); tự động đưa về SL\_Max khi blur. tăng số lượng. |
| ERR-02 | Bỏ trống địa chỉ nhận hàng | Hiển thị Error inline 'Vui lòng chọn đầy đủ Tỉnh/Thành, Quận/Huyện, Phường/Xã.' | Yêu cầu nhập đầy đủ 4 cấp hành chính. |
| ERR-03 | Lỗi API gọi giá Cloud | Hiển thị Cảnh báo 'Không thể lấy giá gói Cloud, hệ thống mặc định gói 6 tháng.' | Mặc định chọn gói Cloud 6T. |
| WRN-01 | Tick chọn cùng loại Camera khác chu kỳ/Cloud | Cảnh báo: 'Sản phẩm cùng loại Camera đã có trong đơn hàng. Vui lòng bỏ chọn sản phẩm trước đó nếu muốn đổi sang gói này.' | Tự động bỏ tick sản phẩm thứ 2 vừa chọn và hiển thị cảnh báo inline. |



#### **8.02 FR02 — Luồng Giỏ Hàng FPT Play (Dịch vụ SA)**

Mô tả nghiệp vụ: Đặc tả luồng mua lẻ dịch vụ số FPT Play (V.VIP 1, V.VIP 2). Tại Giỏ hàng, khách hàng lựa chọn Phương thức kích hoạt: (1) Hệ thống tự động kích hoạt ngay vào SĐT mua đơn; hoặc (2) Nhận mã kích hoạt qua SMS để tự kích hoạt sau (hoặc đem tặng). Form Địa chỉ nhận hàng vẫn hiển thị nhưng ở trạng thái Không bắt buộc (Optional - KH có thể nhập hoặc bỏ qua) phục vụ Biz khai thác thêm thông tin. Khách hàng không thao tác kích hoạt tại màn hình Hoàn tất.

##### 8.02.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Hiển Thị Form Địa Chỉ Không Bắt Buộc (Optional) | Đối với luồng mua FPT Play, hệ thống vẫn hiển thị Form Địa chỉ nhận hàng nhưng ở trạng thái Không bắt buộc (Optional - không có dấu \*). Khách hàng có thể nhập hoặc không nhập (phục vụ mục đích Kinh doanh khai thác thêm dữ liệu khách hàng). Nếu bỏ trống, hệ thống vẫn cho phép chuyển bước và thanh toán bình thường. |
| BR-02 | Lựa Chọn Phương Thức Kích Hoạt Tại Giỏ Hàng | Tại màn hình Giỏ hàng (Step 2), khách hàng lựa chọn 01 trong 02 Phương thức kích hoạt: (1) Hệ thống tự động kích hoạt ngay vào SĐT mua đơn sau khi thanh toán thành công; (2) Nhận mã kích hoạt qua SMS để tự kích hoạt sau. Khách hàng không thao tác kích hoạt tại màn hình hoàn tất mà hệ thống tự động xử lý theo đúng phương thức đã chọn từ trước tại Giỏ hàng. SĐT mua đơn được kiểm tra định dạng Regex hợp lệ. |
| BR-03 | Kiểm Soát Kích Hoạt Đồng Thời Trên Cùng Số Điện Thoại & Gợi Ý Chuyển Sang Nhận Mã | Mỗi số điện thoại của khách hàng chỉ có thể kích hoạt 01 dịch vụ FPT Play hoạt động tại một thời điểm. Trường hợp trong giỏ hàng đã có gói FPT Play V.VIP (1) được chọn hình thức 'Tự kích hoạt' và tick chọn mua, nếu khách hàng tiếp tục tick chọn thêm gói FPT Play V.VIP (2) cũng với hình thức 'Tự kích hoạt', hệ thống lập tức hiển thị thông báo cảnh báo Warning (Banner/Inline tại dòng sản phẩm thứ hai): 'Số điện thoại của Quý khách chỉ có thể kích hoạt 01 dịch vụ FPT Play tại một thời điểm. Quý khách vui lòng chọn lại hình thức kích hoạt "Nhận mã" để lấy mã code gửi tặng cho người thân/bạn bè sử dụng.'. Đồng thời, hệ thống cung cấp nút tùy chọn nhanh cho phép khách hàng chuyển đổi hình thức nhận của gói thứ hai sang 'Nhận mã' ngay tại giỏ hàng. Khi khách hàng bấm nút CTA 'Tiếp tục' để sang bước thanh toán, hệ thống yêu cầu ít nhất 1 trong 2 gói phải ở hình thức 'Nhận mã' để đảm bảo không bị xung đột kích hoạt thuê bao. |
| BR-04 | Xử Lý Sau Thanh Toán Theo Phương Thức Kích Hoạt | Sau khi thanh toán trực tuyến thành công: (1) Nếu khách hàng chọn 'Hệ thống tự động kích hoạt': Hệ thống kích hoạt dịch vụ tức thì vào SĐT mua đơn và gửi SMS xác nhận kèm tài khoản/mật khẩu; (2) Nếu khách hàng chọn 'Nhận mã tự kích hoạt': Hệ thống gửi SMS chứa mã kích hoạt tới SĐT mua đơn để khách hàng tự kích hoạt sau. Đồng thời, tại màn hình hoàn tất đơn hàng (Step 4), hệ thống phát sinh thêm Block thông báo dành riêng cho FPT Play hiển thị thông tin tài khoản/mã code và nút CTA nổi bật \[Tải App FPT Play\] (hoặc mã QR scan tải ứng dụng cho Smartphone/Smart TV) giúp khách hàng tải app và trải nghiệm ngay tức thì. |
| BR-05 | Dịch Vụ SA Không Tăng Giảm Số Lượng | Gói cước FPT Play (V.Vip 1, V.Vip 2) không hỗ trợ tăng/giảm số lượng (mặc định số lượng = 1). Khách hàng chỉ chọn chu kỳ (1 Tháng, 6 Tháng, 12 Tháng). Khi chọn chu kỳ mới sẽ tự động ghi đè chu kỳ cũ trong giỏ. |
| BR-06 | Kiểm Tra Trạng Thái SĐT Đang Sử Dụng Dịch Vụ FPT Play Tại Màn Hình Checkout | Khi khách hàng chọn gói cước FPT Play SA đến màn hình Checkout (/checkout - Step 3) và nhập Số điện thoại: Hệ thống gọi API kiểm tra trạng thái thuê bao xem SĐT này có đang sử dụng dịch vụ FPT Play hay không: (1) Nếu KHÔNG đang sử dụng dịch vụ FPT Play: Hệ thống cho phép khách hàng chuyển tiếp sang bước tiếp theo (chọn phương thức thanh toán và hoàn tất đơn hàng bình thường). (2) Nếu ĐANG SỬ DỤNG dịch vụ FPT Play: Hệ thống lập tức hiển thị Popup Modal báo lỗi: • Tiêu đề: Thông Báo Dịch Vụ FPT Play (hoặc Tài Khoản Đã Tồn Tại) • Nội dung báo lỗi: "Quý khách đã có tài khoản FPT Play theo số {SĐT} vui lòng nhập số điện thoại khác để tiếp tục đăng ký dịch vụ online" • Cung cấp 02 nút hành động (Buttons) trực quan:   - Nút \[Nhập SĐT khác\]: Tắt popup modal để khách hàng thao tác nhập lại Số điện thoại khác ngay tại form Checkout.   - Nút \[Xóa sản phẩm\]: Hệ thống kiểm tra giỏ hàng/đơn hàng Checkout của khách hàng:     + Nhánh 2.1 (Nếu đơn hàng KHÔNG còn sản phẩm nào khác ngoài gói FPT Play SA): Hệ thống tự động điều hướng khách hàng về Màn hình đứt gãy luồng (Drop-off Page), đồng thời tự động đẩy thông tin Khách hàng tiềm năng (KHTN / Lead) gồm SĐT khách hàng vừa nhập + Dịch vụ FPT Play quan tâm sang hệ thống CRM/Telesales để nhân viên liên hệ tư vấn, hỗ trợ sau.     + Nhánh 2.2 (Nếu đơn hàng CÒN sản phẩm khác): Hệ thống tự động Clear (Xóa bỏ) gói FPT Play SA ra khỏi đơn hàng Checkout và Giỏ hàng, đóng Popup Modal; khách hàng kiểm tra lại thông tin đơn hàng đã cập nhật và tiếp tục đi tiếp luồng mua sắm/thanh toán cho các sản phẩm còn lại bình thường; đồng thời hệ thống tự động đẩy thông tin KHTN (SĐT + Dịch vụ FPT Play) sang CRM/Telesales để hỗ trợ riêng. |



##### 8.02.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.02.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Chọn gói cước FPT Play | Khách hàng | Chọn gói cước FPT Play (V.Vip 1, V.Vip 2) -> Click 'Thêm vào giỏ' | Lưu gói SA vào giỏ hàng |
| S-02 | Tick chọn tại Giỏ & Chọn PT Kích Hoạt | Front-End | Khách hàng tick chọn gói FPT Play tại Giỏ hàng và lựa chọn Phương thức kích hoạt: (1) Tự động kích hoạt ngay; hoặc (2) Nhận mã tự kích hoạt (nếu tick thêm gói cùng loại khác chu kỳ -> cảnh báo inline và tự động bỏ tick). Hệ thống hiển thị Form Địa chỉ ở trạng thái Optional. | Ghi nhận Phương thức kích hoạt & Hiển thị Form Địa chỉ Optional (Ẩn COD) |
| S-03 | Nhập SĐT Key Account | Khách hàng | Nhập SĐT liên hệ nhận thông tin/mã kích hoạt & Tùy chọn điền Form Địa chỉ nhận hàng (không bắt buộc, KH có thể bỏ qua). | Validate Regex SĐT hợp lệ. Hệ thống gọi API kiểm tra SĐT có đang sử dụng FPT Play hay không: Nếu không -> Chuyển bước chọn PTTT; Nếu có -> Bật Popup Modal báo lỗi "Quý khách đã có tài khoản FPT Play theo số {SĐT}..." với 2 nút \[Nhập SĐT khác\] và \[Xóa sản phẩm\] (xử lý phân nhánh đứt gãy hoặc clear SP tiếp tục thanh toán + đẩy KHTN sang CRM). |
| S-04 | Thanh toán Online & Active | Khách hàng & SPF | Khởi tạo ID Checkout -> Khách hàng hoàn tất thanh toán trực tuyến thành công. | Hệ thống Checkout gửi thông tin sang SPF tạo Đơn hàng chính thức; Dịch vụ FPT Play được tự động kích hoạt ngay vào SĐT mua đơn (nếu chọn phương thức 1) hoặc gửi SMS mã kích hoạt cho KH tự kích hoạt (nếu chọn phương thức 2). |



##### 8.02.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Input SĐT Key Account | Required | Text Input | Bắt buộc. Field duy nhất thu thập danh tính ngoài tên. Red outline nếu sai Regex. |
| Block Địa chỉ giao hàng | N/A | Hidden Component | Display: Block (Hiển thị cho nhập, placeholder hướng dẫn, không validate bắt buộc địa chỉ). |



##### 8.02.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | SĐT nhập tại Checkout đang sử dụng dịch vụ FPT Play | Popup Modal: "Quý khách đã có tài khoản FPT Play theo số {SĐT} vui lòng nhập số điện thoại khác để tiếp tục đăng ký dịch vụ online" | Hiển thị Popup Modal với 2 button: (1) \[Nhập SĐT khác\]: Tắt popup để KH nhập lại SĐT khác; (2) \[Xóa sản phẩm\]: Kiểm tra đơn hàng còn SP khác không. Nếu không: Đưa KH về màn hình đứt gãy và đẩy thông tin KHTN (SĐT + Dịch vụ FPT Play) sang CRM; Nếu có: Tự động clear gói FPT Play khỏi đơn, tắt popup, cho phép KH kiểm tra lại và đi tiếp luồng thanh toán cho các SP còn lại, đồng thời đẩy KHTN sang CRM. |
| ERR-02 | SĐT sai định dạng Regex | Hiển thị Error inline 'Số điện thoại không hợp lệ, vui lòng kiểm tra lại.' | Yêu cầu nhập đầy đủ 4 cấp hành chính. |
| ERR-03 | Lỗi Server Kích Hoạt FPT Play | Hiển thị Modal 'Kích hoạt dịch vụ gián đoạn. Đơn hàng đã ghi nhận và sẽ kích hoạt trong 15p.' | Đẩy job retry kích hoạt tự động. |
| WRN-01 | Tick chọn cùng gói FPT Play khác chu kỳ | Cảnh báo: 'Gói cước đã có trong giỏ hàng. Mỗi đơn hàng chỉ chọn 01 chu kỳ cước cho mỗi gói dịch vụ.' | Tự động bỏ tick gói cước vừa chọn và hiển thị cảnh báo inline. |



#### **8.03 FR03 — Luồng Giỏ Hàng Access Point AX8000C (Thiết bị SKU)**

Mô tả nghiệp vụ: Đặc tả luồng bán lẻ thiết bị phát Wi-Fi 6 AX8000C. Yêu cầu địa chỉ giao hàng. 

##### 8.03.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Yêu Cầu Địa Chỉ Giao Hàng | Access Point AX8000C là SKU phần cứng, bắt buộc phải điền địa chỉ giao hàng. |
| BR-02 | Tùy Chọn Lắp Đặt Hỗ Trợ | Hình thức triển khai: TIN Giao hàng (tự lắp đặt) hoặc đăng ký KTV lắp đặt tại nhà. Phí thi công lắp đặt chuẩn: 300.000 VNĐ/lần theo biểu phí FCP. |
| BR-03 | Tiếp Nhận Địa Chỉ Giao Hàng & Không Kiểm Tra Vùng Phủ | Hệ thống tiếp nhận và lưu thông tin địa chỉ nhận hàng của khách hàng (Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà/Tên đường) để chuyển sang đơn vị vận chuyển giao tận nơi. Hệ thống website KHÔNG gọi API kiểm tra vùng phủ giao hàng và KHÔNG đặt lịch hẹn. |
| BR-04 | Kiểm Soát Số Lượng Tối Đa (SL\_Max) | Số lượng mua tối đa tuân thủ chính sách FCP. Hệ thống tự động khóa nút (+) khi đạt SL\_Max; nếu nhập số lượng > SL\_Max, khi blur (bấm ra ngoài) hệ thống tự động đưa về SL\_Max. |



##### 8.03.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.03.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Chọn thiết bị AX8000C | Khách hàng | Chọn số lượng -> Click 'Thêm vào giỏ' | Lưu item SKU vào giỏ |
| S-02 | Nhập Địa chỉ nhận hàng | Khách hàng | Điền Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà | Lưu địa chỉ nhận hàng của đơn hàng |
| S-03 | Tích chọn Hỗ trợ KTV | Khách hàng | Chọn Tự lắp hoặc Nhờ KTV (+50k) | Cập nhật tổng tiền đơn hàng |
| S-04 | Submit & Xuất đơn | Khách hàng & Logistics | Chọn PTTT -> Click 'Đặt hàng' | Tạo phiếu giao hàng Logistics |



##### 8.03.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Checkbox Hỗ trợ KTV Lắp đặt | Optional | Checkbox | Tích chọn sẽ tự động bổ sung line item 'Phí hỗ trợ lắp đặt: 50.000đ'. |
| Form Địa chỉ Giao hàng | Required | Address Form | Yêu cầu điền đủ 4 cấp hành chính. |



##### 8.03.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Vượt quá số lượng mua tối đa | Không hiển thị Toast thông báo. Xử lý trực tiếp trên UI: Khóa nút (+) khi đạt SL\_Max và tự động đưa về SL\_Max khi blur. | Khóa nút (+); tự động đưa về SL\_Max khi blur. |
| ERR-02 | Địa chỉ nhận hàng không hợp lệ | Hiển thị Error inline 'Địa chỉ nhận hàng không hợp lệ hoặc thiếu thông tin.' | Yêu cầu đổi địa chỉ giao hàng. |



#### **8.04 FR04 — Luồng Giỏ Hàng Ổ Cắm Thông Minh FPT Smart Home (Thiết bị IoT SKU)**

Mô tả nghiệp vụ: Đặc tả luồng bán lẻ ổ cắm Wi-Fi thông minh. Yêu cầu nhập địa chỉ giao hàng.

##### 8.04.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Ràng Buộc Địa Chỉ Giao Hàng | Bắt buộc điền địa chỉ giao hàng. |
| BR-02 | Giới Hạn Số Lượng Tối Đa 5 Thiết Bị | Giới hạn tối đa 5 ổ cắm/đơn (SL\_Max = 5). Khóa nút (+) khi đạt 5; nếu nhập > 5 thì khi blur tự động đưa về 5. |
| BR-03 | Ghi Chú Kỹ Thuật Đơn Hàng | Tự động kẹp tag `IoT\_SmartPlug` trong thông tin đơn để bộ phận giao vận/KTV chuẩn bị vật tư thi công. |
| BR-04 | Sản Phẩm Đối Tác & Cảnh Báo Giao Hàng | Sản phẩm Đối tác (Smart Home/IoT) do Đối tác xử lý & giao hàng tận nơi. KHÔNG tạo phiếu thi công/giao hàng của FPT. Hệ thống hiển thị thông báo: “Ftel sẽ sớm giao hàng đến bạn (Đối tác Giao hàng)”. |



##### 8.04.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.04.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Chọn Ổ cắm Smart Home | Khách hàng | Chọn số lượng (Max 5) -> Click 'Thêm giỏ' | Lưu item IoT vào giỏ |
| S-02 | Nhập Địa chỉ nhận hàng | Khách hàng | Nhập Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà | Validate địa chỉ giao hàng |
| S-03 | Thanh toán & Submit | Khách hàng & SPF | Chọn PTTT VNPAY/COD -> Click 'Đặt hàng' | Tạo phiếu giao hàng IoT |



##### 8.04.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Input Số lượng Ổ cắm | Required | Numeric Box (+/-) | Giới hạn từ 1 đến 5 ổ cắm/đơn. |
| Form Địa chỉ Giao hàng | Required | Address Form | Yêu cầu điền đầy đủ 4 cấp địa chỉ. |



##### 8.04.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Vượt quá 5 ổ cắm thông minh | Không hiển thị Toast thông báo. Xử lý trực tiếp trên UI: Khóa nút (+) khi số lượng = 5 và tự động đưa về 5 khi blur. | g.Khóa nút (+); tự động đưa về SL\_Max khi blur. tăng số lượn |
| ERR-02 | Lỗi cập nhật số lượng thiết bị | Hiển thị Toast 'Không thể cập nhật số lượng ổ cắm, vui lòng thử lại.' | Gợi ý chọn sản phẩm khác. |



#### **8.05 FR05 — Luồng Giỏ Hàng Smart TV Samsung (Thiết bị Phần Cứng Do Đối Tác Giao Hàng)**

Mô tả nghiệp vụ: Đặc tả trải nghiệm chọn mua thiết bị Smart TV Samsung. Khách hàng nhập địa chỉ nhận hàng để đối tác/đơn vị vận chuyển giao hàng trực tiếp. Hệ thống KHÔNG kiểm tra vùng phủ giao hàng đối với hàng cồng kềnh trên website. Không có bước chọn lịch hẹn giao.

##### 8.05.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Yêu Cầu Địa Chỉ Giao Hàng & Không Check Vùng Phủ Cồng Kềnh | Khách hàng mua Smart TV Samsung bắt buộc nhập đầy đủ địa chỉ nhận hàng (Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà/Đường). Hệ thống KHÔNG kiểm tra vùng phủ hay ràng buộc địa lý đối với hàng cồng kềnh (không gọi API Geolocation check). |
| BR-02 | Hình Thức Triển Khai Do Đối Tác Giao Hàng | Smart TV Samsung là sản phẩm do Đối tác phân phối xử lý đơn và giao hàng trực tiếp tận nơi. Hệ thống không tạo phiếu thi công KTV FPT. |
| BR-03 | Đơn Hàng Gộp Cùng Thiết Bị & Dịch Vụ Khác | Cho phép mua Smart TV cùng với các thiết bị phần cứng khác (Camera, AP AX8000C, SmartHome) hoặc dịch vụ số SA trong cùng 1 đơn hàng mà không bị giới hạn địa lý. |
| BR-04 | Hình Thức Triển Khai Đối Tác | Smart TV Samsung là sản phẩm Đối tác xử lý & giao hàng tận nơi. Không tạo phiếu giao hàng của FPT. Smart TV Samsung do Đối tác phân phối xử lý đơn và giao hàng trực tiếp. |
| BR-05 | Kiểm Soát Số Lượng Tối Đa TV (SL\_Max) | Tuân thủ số lượng mua tối đa Smart TV theo chính sách FCP. Hệ thống tự động khóa nút (+) khi đạt SL\_Max; nếu nhập > SL\_Max, khi blur ra ngoài hệ thống tự động đưa về SL\_Max. |



##### 8.05.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.05.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Chọn mẫu Smart TV Samsung | Khách hàng | Chọn kích thước TV -> Click 'Thêm vào giỏ' | Lưu item TV vào giỏ |
| S-02 | Nhập Địa chỉ nhận hàng | Khách hàng & FE | Chọn Tỉnh -> Huyện -> Phường/Xã | Lưu địa chỉ vào Session FID (không kiểm tra vùng phủ) |
| S-03 | Xác nhận Đơn hàng & Chuyển Checkout | Hệ thống | Kiểm tra thông tin địa chỉ đầy đủ | Kiểm tra thông tin địa chỉ đầy đủ và chuyển tiếp sang bước Checkout |
| S-04 | Submit Đơn giao TV | Khách hàng & Logistics | Chọn PTTT -> Click 'Đặt hàng' | Tạo vận đơn giao Smart TV do đối tác thực hiện |



##### 8.05.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Dropdown Phường/Xã | Required | Select Box | Chọn Phường/Xã theo Quận/Huyện. Hệ thống lưu địa chỉ nhận hàng, không gọi API kiểm tra vùng phủ cồng kềnh. |
| Form Địa chỉ nhận hàng | N/A | Modal Dialog | Bắt buộc nhập đầy đủ Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà/Tên đường trước khi chuyển sang bước đặt hàng. |



##### 8.05.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Thiếu thông tin địa chỉ nhận hàng | Hiển thị cảnh báo: 'Vui lòng điền đầy đủ địa chỉ nhận hàng (Tỉnh/Thành, Quận/Huyện, Phường/Xã, Số nhà) để đối tác giao Smart TV.' | Yêu cầu nhập đầy đủ 4 cấp hành chính. |
| ERR-02 | Lỗi Đơn vị vận chuyển / Đối tác giao hàng Check | Hệ thống không gọi API kiểm tra vùng phủ cồng kềnh; đơn được tiếp nhận bình thường. | Cho phép Khách thử lại. |



#### **8.06 FR06 — Luồng Giỏ Hàng UltraFast (Dịch vụ gia tăng SA)**

Mô tả nghiệp vụ: Luồng mua mã kích hoạt gói cước gia tốc UltraFast (Lưu ý: Gói cước UltraFast vẫn kinh doanh và bán bình thường; riêng gói cũ HyperFast đã chính thức ngừng kinh doanh). Khách hàng mua mã kích hoạt bình thường mà KHÔNG cần kiểm tra trước SĐT đã có hợp đồng hay chưa. Ẩn 100% Form địa chỉ nhận hàng. Sau khi thanh toán thành công, tại màn hình hoàn tất (Step 4) cung cấp 2 Next Actions: 1) Sao chép mã kích hoạt (để tặng cho người khác hoặc kích hoạt sau trên FPT ID/Hi FPT); 2) Bấm "Kích hoạt ngay" để hệ thống kiểm tra SĐT mua hàng có hợp đồng Internet FPT hay không (nếu có 1 HĐ -> kích hoạt ngay; nếu có nhiều HĐ -> chọn HĐ muốn kích hoạt; nếu không có HĐ -> thông báo không tìm thấy HĐ).

##### 8.06.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Ẩn Form Địa Chỉ | Giỏ hàng chỉ có UltraFast -> Ẩn 100% Form Địa chỉ giao hàng. |
| BR-02 | Mua Mã Kích Hoạt (Code) | Khách hàng mua gói UltraFast dưới dạng mã kích hoạt (Code) bình thường mà KHÔNG cần kiểm tra trước SĐT đã có hợp đồng hay chưa. |
| BR-03 | Hai Hành Động Sau Thanh Toán Tại Step 4 | Sau khi thanh toán trực tuyến thành công, tại màn hình hoàn tất (Step 4), hệ thống hiển thị Block cấp mã kích hoạt điện tử (Activation Code) kèm tác vụ kích hoạt ngay trực tiếp đặt ngay dưới Form thông báo hoàn tất chính, cung cấp 2 Next Actions rõ ràng: (1) Nút 'Sao chép mã' kèm thông báo thời hạn sử dụng mã; (2) Ô nhập Số hợp đồng Internet kèm nút CTA 'Kích hoạt ngay' (hệ thống gọi API kích hoạt tức thì mà không cần rời màn hình). |
| BR-04 | Không Tăng Giảm SL & Ghi Đè Chu Kỳ | Gói UltraFast không hỗ trợ tăng giảm số lượng (luôn = 1). Chỉ chọn chu kỳ cước (1T, 6T, 12T). Khi chọn chu kỳ mới hệ thống tự động cập nhật vào line item hiện tại. Nếu tick chọn thêm gói cùng loại khác chu kỳ, hệ thống cảnh báo ngay tại dòng sản phẩm và tự động bỏ tick. |
| BR-05 | Modal Chờ Kích Hoạt Dịch Vụ Số SA (Unclosable Polling Modal) | Tại màn hình hoàn tất (Step 4), khi khách hàng chọn phương thức Kích hoạt trực tiếp hoặc Lấy mã code: Hệ thống hiển thị Modal "Hệ thống đang xử lý kích hoạt / cấp mã..." không có nút Đóng (X), chặn click ra ngoài và chặn phím ESC (Unclosable). Hệ thống thực hiện Polling kiểm tra trạng thái mỗi 2 giây (tối đa 30 giây). Nếu quá 30 giây mà hệ thống core chưa trả kết quả thành công, tự động fallback: Đóng Modal và hiển thị thông báo: "Mã kích hoạt đang được khởi tạo và sẽ gửi qua tin nhắn SMS tới số \[SĐT\] trong vòng 5 phút". |



##### 8.06.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.06.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Chọn gói UltraFast | Khách hàng | Chọn gói 1T/6T/12T -> Click 'Thêm giỏ' | Lưu item SA vào giỏ |
| S-02 | Nhập SĐT Internet FPT | Khách hàng | Nhập SĐT nhận mã kích hoạt và thông tin xác nhận đơn hàng | Khởi tạo đơn hàng mua mã kích hoạt |
| S-03 | Thanh toán & Lựa chọn hành động tại Step 4 | Khách hàng & Radius | Khởi tạo ID Checkout -> Khách hàng hoàn tất thanh toán trực tuyến thành công. | Mã kích hoạt hiển thị + Kết quả kích hoạt dịch vụ nếu chọn Kích hoạt ngay |



##### 8.06.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Mã kích hoạt & Nút Sao chép (Step 4) | Required | Text Input | Hiển thị mã kích hoạt dạng text kèm nút Copy nhanh (sao chép vào clipboard để tặng hoặc kích hoạt sau trên FPT ID/Hi FPT). |
| Nút Kích hoạt ngay & Modal chọn HĐ | Required | CTA Button + Modal List | Bấm "Kích hoạt ngay": Nếu có 1 HĐ -> kích hoạt ngay; Nếu có nhiều HĐ -> mở modal chọn HĐ; Nếu không có HĐ -> hiển thị thông báo không tìm thấy HĐ. |



##### 8.06.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Không tìm thấy HĐ Internet khi bấm Kích hoạt ngay | Hiển thị thông báo: "Không tìm thấy hợp đồng Internet FPT liên kết với số điện thoại này. Bạn có thể sao chép mã kích hoạt để gửi tặng hoặc kích hoạt trên hợp đồng khác qua Hi FPT/FPT ID." | Giữ mã kích hoạt hiển thị, hướng dẫn khách hàng lưu mã hoặc kích hoạt trên tài khoản khác. |
| ERR-02 | Hợp đồng đã có gói UltraFast đang hiệu lực | Hiển thị cảnh báo: "Hợp đồng đã chọn hiện đang có gói UltraFast đang hoạt động. Vui lòng chọn hợp đồng khác hoặc gia hạn sau khi gói cũ hết hiệu lực." | Yêu cầu nhập đầy đủ 4 cấp hành chính. |
| WRN-01 | Tick chọn cùng gói UltraFast khác chu kỳ | Cảnh báo: 'Gói cước UltraFast đã có trong giỏ hàng. Mỗi đơn hàng chỉ chọn 01 chu kỳ cước.' | Tự động bỏ tick gói cước vừa chọn và hiển thị cảnh báo inline. |



#### **8.07 FR07 — Luồng Giỏ Hàng Gộp Nhiều Dịch Vụ SA (SA + SA)**

Mô tả nghiệp vụ: Mua gộp các dịch vụ số SA (ví dụ tiêu biểu: FPT Play V.VIP & UltraFast) trong cùng 1 giỏ hàng. Ẩn COD (chỉ thanh toán trực tuyến). Biểu mẫu địa chỉ giao hàng hiển thị dạng không bắt buộc (Optional) nếu giỏ hàng có FPT Play (để Biz khai thác thêm thông tin vùng miền của KH) hoặc ẩn 100% nếu giỏ hàng toàn bộ là SA khác. Dùng chung 01 SĐT đại diện làm thông tin liên hệ. Dịch vụ FPT Play xử lý kích hoạt theo đúng Phương thức kích hoạt đã chọn tại Giỏ hàng; UltraFast sinh mã tại Step 4.

##### 8.07.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Xử Lý Form Địa Chỉ Cho Giỏ SA+SA | Đếm `count(SKU) == 0`: Nếu giỏ hàng có dịch vụ FPT Play -> Hiển thị Form địa chỉ nhận hàng ở trạng thái Không bắt buộc (Optional, không có dấu \*) để phục vụ Biz khai thác thêm thông tin; nếu giỏ hàng chỉ gồm các dịch vụ số khác (như UltraFast) -> Ẩn 100% Form địa chỉ. |
| BR-02 | SĐT Đại Diện Duy Nhất | Sử dụng 01 Số điện thoại duy nhất làm Key kích hoạt cho tất cả các gói SA trong giỏ. |
| BR-03 | Phân Luồng Kích Hoạt Độc Lập (FPT Play & UltraFast) | Sau khi thanh toán trực tuyến thành công: Dịch vụ FPT Play xử lý theo đúng Phương thức kích hoạt khách hàng đã lựa chọn tại Giỏ hàng (Tự động kích hoạt ngay tức thì vào SĐT đại diện và gửi SMS tài khoản/mật khẩu HOẶC Gửi SMS mã kích hoạt điện tử để khách hàng tự kích hoạt sau). Dịch vụ UltraFast sinh mã kích hoạt điện tử hiển thị tại màn hình Hoàn tất Step 4 kèm 02 Next Actions (Sao chép mã / Kích hoạt trực tiếp theo 3 nhánh HĐ billing đang hoạt động bình thường tại FTEL). Hai luồng kích hoạt hoạt động hoàn toàn độc lập, kết quả kích hoạt của dịch vụ này không làm ảnh hưởng đến dịch vụ kia. |
| BR-04 | Chống Chọn Trùng Gói Cước Khác Chu Kỳ | Tại màn hình Giỏ hàng (Step 2), khách hàng có thể tick chọn gộp các dịch vụ số khác nhau (FPT Play V.VIP + UltraFast), nhưng nếu tick chọn trùng cùng 1 gói cước chỉ khác chu kỳ thì hệ thống hiển thị cảnh báo (warning) ngay tại line sản phẩm vừa tick thêm và tự động bỏ tick. |

##### 8.07.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.07.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Gộp các gói SA vào Giỏ | Khách hàng | Thêm FPT Play V.VIP & Gói cước gia tốc UltraFast vào giỏ | Lưu danh sách SA item |
| S-02 | Kiểm tra Giỏ & Hiện Form SĐT | Front-End | Xác nhận count(SKU) == 0 | Hiện form SĐT liên hệ, Form địa chỉ hiển thị Optional nếu có FPT Play (hoặc ẩn nếu không có) |
| S-03 | Thanh toán & Active gộp | Khách hàng & SA Engine | Khởi tạo ID Checkout -> Khách hàng hoàn tất thanh toán trực tuyến thành công. | FPT Play kích hoạt theo đúng Phương thức đã chọn tại Giỏ hàng; UltraFast sinh mã kích hoạt tại Step 4 kèm 2 Next Actions. |



##### 8.07.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Input SĐT Đại Diện | Required | Text Input | Bắt buộc. Dùng làm tài khoản chung cho các gói SA. |
| Summary List SA Items | ReadOnly | List Table | Hiển thị chi tiết các gói SA gộp trong đơn. |



##### 8.07.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Lỗi kích hoạt 1 trong 2 SA | Hiển thị Cảnh báo: "FPT Play đã xử lý kích hoạt theo đúng Phương thức đã chọn tại Giỏ hàng. Gói UltraFast đã tạo mã thành công nhưng chưa kích hoạt vào hợp đồng (khách hàng có thể sao chép mã để kích hoạt sau)." | Tự động tạo ticket kỹ thuật. |
| WRN-01 | Chọn trùng gói SA khác chu kỳ trong Combo SA+SA | Cảnh báo: 'Gói cước đã có trong giỏ hàng. Mỗi đơn hàng chỉ chọn 01 chu kỳ cước cho mỗi gói dịch vụ.' | Tự động bỏ tick gói cước vừa chọn và giữ nguyên gói cước đã chọn trước đó. |



#### **8.08 FR08 — Luồng Giỏ Hàng Gộp Hỗn Hợp Thiết Bị + Dịch Vụ (SKU + SA)**

Mô tả nghiệp vụ: Luồng mua gộp Camera (SKU) + FPT Play (SA). Bắt buộc hiển thị Form Địa chỉ nhận hàng (bắt buộc theo SKU phần cứng). Tự động ẩn hoàn toàn phương thức COD do trong giỏ có dịch vụ số SA. Dịch vụ FPT Play được kích hoạt theo đúng Phương thức kích hoạt khách hàng đã chọn tại Giỏ hàng (Tự động kích hoạt ngay hoặc Nhận mã qua SMS).

##### 8.08.1 Quy tắc nghiệp vụ (Business Rules)

| **Mã Rule** | **Tên Quy Tắc** | **Nội dung & Logic Hệ Thống Chi Tiết** |
| :---: | :---: | :---: |
| BR-01 | Bắt Buộc Hiện Form Địa Chỉ | `count(SKU) >= 1` -> Bắt buộc hiển thị Form Địa chỉ nhận hàng. |
| BR-02 | Chính Sách Kích Hoạt Dịch Vụ Số | Khi khách hàng thanh toán trực tuyến thành công (Ví dụ: Thẻ, Ví điện tử, QR Code...), dịch vụ FPT Play được xử lý kích hoạt theo đúng Phương thức kích hoạt khách hàng đã lựa chọn tại Giỏ hàng (Tự động kích hoạt ngay vào SĐT hoặc Gửi SMS mã kích hoạt điện tử); UltraFast sinh mã tại Step 4. |
| BR-03 | Chính Sách Ẩn COD Đơn Mix SKU+SA | Do gói Dịch vụ số SA (như FPT Play, UltraFast) không hỗ trợ phương thức COD, nên khi Khách hàng mua gộp Thiết bị SKU + Dịch vụ số SA, hệ thống TỰ ĐỘNG ẨN HOÀN TOÀN phương thức COD. Khách hàng lựa chọn các phương thức thanh toán trực tuyến trả trước được hỗ trợ cho sản phẩm (Ví dụ: Thẻ tín dụng, Thẻ ATM, Ví điện tử, QR Code...). |
| BR-04 | Hiển Thị Danh Sách Cổng Thanh Toán Trực Tuyến | Giao diện Checkout hiển thị danh mục các phương thức thanh toán trực tuyến trả trước phù hợp với sản phẩm (Ví dụ: Thẻ tín dụng, Thẻ ATM, Ví điện tử, Apple Pay, QR Code...) kèm hướng dẫn thanh toán. |



##### 8.08.2 Quy trình luồng nghiệp vụ BPMN (Business Workflow)



##### 8.08.3 Các bước thực hiện chi tiết

| **Mã Bước** | **Tên Bước Thao Tác** | **Tác Nhân** | **Thao Tác / Hành Động Chi Tiết** | **Kết Quả Đầu Ra (Output)** |
| :---: | :---: | :---: | :---: | :---: |
| S-01 | Gộp SKU + SA vào Giỏ | Khách hàng | Thêm Camera & FPT Play vào giỏ | Lưu item hỗn hợp |
| S-02 | Nhập Địa chỉ & Chọn PTTT | Khách hàng | Điền địa chỉ nhận hàng -> Chọn PTTT | COD tự động ẩn do có SA, chỉ hiển thị các PTTT online |
| S-03 | Submit Đơn sang SPF | Front-End & SPF | Click 'Đặt hàng' -> Gửi payload kẹp Flag | SPF tạo đơn & điều phối SA Engine |



##### 8.08.4 Đặc tả giao diện & ràng buộc trường (UI Field Spec)

| **Phần tử / Component UI** | **Trạng Thái** | **Loại Control** | **Ràng buộc & Hành vi Chi tiết** |
| :---: | :---: | :---: | :---: |
| Radio Box COD | Optional | Radio Button | Tự động ẩn hoàn toàn phương thức COD khi trong giỏ hàng có dịch vụ số SA (FPT Play, UltraFast). |
| Form Địa chỉ Giao hàng | Required | Address Form | Yêu cầu đủ 4 cấp địa chỉ nhận hàng. |



##### 8.08.5 Edge Cases & Bảng mã lỗi chi tiết

| **Mã Lỗi** | **Điều Kiện / Trường Hợp Gặp Lỗi** | **Message Thông Báo Hiển Thị Chi Tiết** | **Hành Vi Hệ Thống & Hướng Xử Lý** |
| :---: | :---: | :---: | :---: |
| ERR-01 | Tick chọn sản phẩm xung đột trong giỏ hỗn hợp (cùng model Camera khác gói Cloud hoặc trùng gói SA khác chu kỳ) | Cảnh báo Warning inline: 'Không thể chọn mua cùng model Camera khác gói Cloud hoặc trùng dịch vụ số khác chu kỳ trong cùng một đơn hàng.' | Hệ thống tự động bỏ tick (untick) sản phẩm vừa chọn, giữ nguyên sản phẩm hợp lệ đã tick trước đó. |
| ERR-02 | Lỗi kết nối cổng thanh toán trực tuyến VNPAY / SPF Gateway | Hiển thị Error Toast / Modal: 'Giao dịch thanh toán trực tuyến tạm thời gián đoạn. Quý khách vui lòng thử lại hoặc chọn phương thức thanh toán trực tuyến khác.' | Giữ nguyên toàn bộ giỏ hàng và dữ liệu form địa chỉ nhận hàng, cho phép khách hàng bấm thử lại mà không phải nhập lại thông tin. |





### PART C — NON-FUNCTIONAL REQUIREMENTS & GOVERNANCE

#### 9. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - NFR)

Danh mục tham khảo — team dự án bổ sung/loại bỏ dòng theo đặc thù dự án.



| **Mã NFR** | **Hạng mục** | **Yêu cầu chi tiết** | **Phương pháp đo lường** |
| --- | --- | --- | --- |
| NFR-01 | Performance | Thuật toán đếm local count(SKU) và count(SA) phản hồi < 50ms. Thời gian tải giỏ hàng < 1.5s. | Lighthouse / APM Profiling |
| NFR-02 | Security | Bảo vệ Price Tampering: Cấm 100% truyền Sub-total từ Client. Server tự tính giá từ SKU List. HTTPS & Token CSRF bắt buộc. | CSOC Pentest giả lập |
| NFR-03 | Availability | Nếu SPF downtime, Session giỏ hàng vẫn được lưu giữ an toàn (trên Browser LocalStorage cho khách vãng lai hoặc DB FID khi khách đã đăng nhập). Không làm crash UI của khách. Hiện thông báo giao dịch đang xử lý. | Chaos Engineering Test |
| NFR-04 | Scalability | Cấu hình động bảng giá, chính sách triển khai & biểu phí từ hệ thống FCP, không gán cố định trên giao diện. | Code Review Audit |




#### 10. TÀI LIỆU THAM KHẢO & LIÊN KẾT (ARTIFACT REFERENCE)

Đảm bảo truy vết giữa yêu cầu nghiệp vụ và thiết kế giao diện. Nếu dự án không phải làm UI thì ghi "N/A — Backend only".



| **Hạng mục** | **Mô tả** | **Link / Vị trí lưu trữ** |
| --- | --- | --- |
| Tài liệu BRD/PRD | Tài liệu Đặc tả Yêu cầu Sản phẩm Giỏ hàng | thuyttdoc/prd\_cart.doc |
| Sơ đồ BPMN | Bộ sơ đồ luồng nghiệp vụ BPMN nền trắng (FR01 -> FR08) | thuyttdoc/pic-ba/ |
| UI/UX Design | Thiết kế giao diện Giỏ hàng & Checkout trên Figma | Figma FPT Ecom Board |
| API Specs | Tài liệu tích hợp kỹ thuật giữa FID, SPF, FCP, HiFPT | Swagger Docs FPT.vn |



#### 11. TIÊU CHÍ NGHIỆM THU DỰ ÁN (DEFINITION OF DONE - DOD)

Dự án được coi là hoàn thành khi đáp ứng ĐẦY ĐỦ các tiêu chí sau.



| **STT** | **Tiêu chí nghiệm thu (Definition of Done)** | **Owner** | **Kết quả** |
| --- | --- | --- | --- |
| 1 | Hoàn tất rà soát và phê duyệt tài liệu PRD & Sơ đồ BPMN | BA & QA | Pass |
| 2 | Hoàn tất phát triển đầy đủ các quy tắc giỏ hàng (SL\_Max, Chống xung đột, Phân luồng kích hoạt SA, Cho phép bán chung Cam Combo & Cam Only) | Dev Team | Pass |
| 3 | Kiểm thử nghiệm thu UAT đạt 100% các kịch bản Acceptance Criteria (AC) | QC Team | Pass |
| 4 | Kiểm tra bảo mật Price Tampering & Penetration Test đạt chuẩn CSOC | Security Team | Pass |





## PART D — TEMPLATE META & USAGE

1. HƯỚNG DẪN SỬ DỤNG TEMPLATE
- Các team dự án được phép customize (thêm/bớt cột, đổi tên cột/mục) miễn đảm bảo truy vết được: yêu cầu → chức năng.
- Khi nội dung KHÔNG áp dụng cho dự án, phải ghi rõ "N/A" và nêu ngắn gọn lý do.
- Sau khi "Make a copy" template cho dự án, BA/PIC xóa: (a) các đoạn hướng dẫn màu cam, (b) toàn bộ nội dung Ví dụ minh họa, (c) mục Part D này.
- Quy ước ID AC (mục 7.0) là bắt buộc và áp dụng thống nhất toàn ISC — không tự đặt format khác.
- PRD là artifact bắt buộc trước Gate Design theo ISC SDLC Process v1.7 — không bỏ qua bước phê duyệt PO ở mục 12.




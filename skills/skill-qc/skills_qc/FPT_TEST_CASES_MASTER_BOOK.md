# CẨM NANG TEST CASES & NGHIỆP VỤ KIỂM THỬ DỰ ÁN FPT (MASTER BOOK)

> **Mã hiệu tài liệu**: `4.0-BM/PM/HDCV/FTEL-TC`  
> **Dự án**: FPT.VN E-Commerce & Customer Journey Ecosystem  
> **Áp dụng cho**: Tester, QC, Business Analyst (BA), Product Owner (PO), Dev Team (ISC)  
> **Định dạng chuẩn**: Font Times New Roman, tuân thủ bảng mã quy tắc nghiệp vụ BR-01..BR-n theo từng phân hệ.

---

## MỤC LỤC
1. [Tổng Quan Ma Trận Kiểm Thử Dự Án FPT-1](#1-tổng-quan-ma-trận-kiểm-thử-dự-án-fpt-1)
2. [Phân Hệ 1: Giỏ Hàng Mua Kèm Camera Play 4 & Phụ Kiện Charm](#2-phân-hệ-1-giỏ-hàng-mua-kèm-camera-play-4--phụ-kiện-charm)
3. [Phân Hệ 2: Kịch Bản Ngoại Lệ Internet & Truyền Hình Combo](#3-phân-hệ-2-kịch-bản-ngoại-lệ-internet--truyền-hình-combo)
4. [Phân Hệ 3: Quy Tắc Nghiệp Vụ & Test Cases Mua Thiết Bị](#4-phân-hệ-3-quy-tắc-nghiệp-vụ--test-cases-mua-thiết-bị)
5. [Phân Hệ 4: Dịch Vụ Số Standalone (FPT Play OTT) & Xác Thực SĐT](#5-phân-hệ-4-dịch-vụ-số-standalone-fpt-play-ott--xác-thực-sđt)
6. [Quy Chuẩn Log Lỗi, Bằng Chứng Kiểm Thử & Nghiệm Thu UAT](#6-quy-chuẩn-log-lỗi-bằng-chứng-kiểm-thử--nghiệm-thu-uat)

---

## 1. TỔNG QUAN MA TRẬN KIỂM THỬ DỰ ÁN FPT-1

Hệ thống bán hàng và chăm sóc khách hàng FPT.VN bao gồm 4 phân hệ nghiệp vụ cốt lõi:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG PHÂN HỆ KIỂM THỬ FPT-1                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. CAMERA & CHARM ENGINE  │ Mua kèm có điều kiện, tỷ lệ 1:1, best-deal │
├───────────────────────────┼────────────────────────────────────────────┤
│ 2. INTERNET & COMBO       │ Khảo sát hạ tầng, check port, địa chỉ      │
├───────────────────────────┼────────────────────────────────────────────┤
│ 3. THIẾT BỊ PHỤ KIỆN      │ Giỏ hàng, tồn kho, thiết bị Wi-Fi 6        │
├───────────────────────────┼────────────────────────────────────────────┤
│ 4. DỊCH VỤ SỐ (FPT PLAY)  │ Validate SĐT ngầm, chống đè tài khoản      │
└───────────────────────────┴────────────────────────────────────────────┘
```

---

## 2. PHÂN HỆ 1: GIỎ HÀNG MUA KÈM CAMERA PLAY 4 & PHỤ KIỆN CHARM

*Tài liệu gốc đính kèm: `fpt-scenarios-camera-charm/Kich_Ban_Ky_Thuat_Play4_Charm.xlsx`*

### A. Nguyên Tắc Cốt Lõi (Core Pricing Logic)
- **Hạn mức mua kèm ưu đãi (Add-on Allowance)**: Mỗi 01 Camera Play 4 trong giỏ hàng kích hoạt 01 suất mua kèm 01 Charm với giá ưu đãi (hiện tại là 0đ).
- **Quy tắc tách dòng (Split Line Items)**: Khi số lượng phụ kiện vượt hạn mức, hệ thống tách thành 2 dòng: dòng hưởng giá ưu đãi và dòng tính giá bán lẻ gốc (150.000đ).
- **Quy tắc Best-Deal**: Khách chọn nhiều mẫu có giá bán lẻ khác nhau, ưu đãi 0đ tự động gán cho mẫu có giá trị cao nhất.

### B. Bảng Kịch Bản Test Case Mẫu (Trích đoạn từ Bộ 40+ Rules)
| STT | Mã Rule | Tình Huống Mua Hàng | Điều Kiện Áp Dụng | Quy Tắc Nghiệp Vụ & Kết Quả Mong Đợi (Expected Output) |
|:---:|:---:|:---|:---|:---|
| 1 | **BR-01** | Mua đúng tỷ lệ 1:1 (1 Cam + 1 Charm) | Giỏ hàng có 1 Cam Play 4. Kho còn Charm. | 1 Cam kích hoạt 1 suất Charm 0đ. Giỏ hàng hiển thị đúng 0đ cho Charm. |
| 2 | **BR-02** | Vượt hạn mức (1 Cam + 2 Charm cùng mẫu A) | Đã có 1 Cam + 1 Charm A (0đ). Bấm thêm 1 Charm A. | Tách thành 2 dòng: 1 chiếc Charm A giá 0đ, 1 chiếc Charm A tính giá gốc 150k. |
| 3 | **BR-03** | Vượt hạn mức (1 Cam + 1 Charm A 100k + 1 Charm B 150k) | 1 Cam, chọn 1 Charm 100k và 1 Charm 150k. | Best-deal: Charm B (150k) được áp dụng giá 0đ, Charm A tính giá 100k. |
| 4 | **BR-04** | Dưới hạn mức (Mua 3 Cam nhưng chỉ chọn 1 Charm) | Giỏ có 3 Cam, chỉ chọn 1 Charm. | Không chặn luồng, hiển thị nhắc nhở nhẹ còn 2 suất ưu đãi chưa chọn. |
| 5 | **BR-05** | Giảm số lượng Cam (2 Cam + 2 Charm ➔ giảm Cam xuống 1) | Giỏ đang có 2 Cam + 2 Charm 0đ, khách giảm Cam xuống 1. | Hạn mức giảm còn 1. Giữ 2 Charm nhưng chiếc thứ 2 chuyển thành giá gốc 150k. |
| 6 | **BR-06** | Xóa hoàn toàn Camera khỏi giỏ hàng | Khách bấm xóa sản phẩm Camera Play 4. | Hạn mức ưu đãi về 0. Toàn bộ Charm chuyển thành tính giá bán lẻ gốc, kèm popup cảnh báo. |

---

## 3. PHÂN HỆ 2: KỊCH BẢN NGOẠI LỆ INTERNET & TRUYỀN HÌNH COMBO

*Tài liệu gốc đính kèm: `fpt-scenarios-internet-combo/Kich_Ban_Test_Internet_Combo.md`*

### Bảng Kịch Bản Kiểm Thử Ngoại Lệ (Edge Cases)
| Mã TC | Kịch bản Ngoại lệ | Điều kiện kích hoạt | Kết quả mong đợi (Expected Output) |
|:---:|:---|:---|:---|
| **TC-EX-01** | Hết Port / Không có hạ tầng mạng | API Check Port trả về `false` tại địa chỉ khách chọn. | Hệ thống bỏ qua bước chọn gói và thanh toán; chuyển thẳng đến Page Hoàn thành; thông tin tự động đẩy sang CRM Lead KHTN cho Sales liên hệ khảo sát hạ tầng. |
| **TC-EX-02** | Hủy giao dịch thanh toán trực tuyến (Drop-off) | Khách sang cổng VNPay/Foxpay nhưng bấm "Hủy giao dịch" hoặc đóng tab. | Chuyển hướng về trang Đặt hàng thành công nhưng ở trạng thái "Chờ thanh toán"; ghi nhận hình thức Thu sau (COD); bắn SMS/Email kèm link thanh toán lại. |
| **TC-EX-03** | Khách hàng thay đổi địa chỉ lắp đặt ở bước cuối | Tại bước Xác nhận, khách bấm quay lại đổi địa chỉ sang Tỉnh/TP khác. | Hệ thống lập tức xóa các khuyến mãi địa phương cũ, gọi lại API tính cước theo vùng giá mới và cảnh báo người dùng xác nhận lại. |
| **TC-EX-04** | Số điện thoại đã có hợp đồng FPT đang nợ cước | Khách nhập SĐT đang có nợ cước trên hệ thống Billing. | Chặn luồng thanh toán trả trước mới; hiển thị thông báo hướng dẫn khách thanh toán nợ cước cũ hoặc liên hệ tổng đài 1900 6600. |

---

## 4. PHÂN HỆ 3: QUY TẮC NGHIỆP VỤ & TEST CASES MUA THIẾT BỊ

*Tài liệu gốc đính kèm: `fpt-scenarios-thiet-bi/Kich_Ban_Test_Thiet_Bi.md`*

### A. Bảng Quy Tắc Nghiệp Vụ (Business Rules)
| Mã Rule | Tên Quy Tắc | Mô Tả Chi Tiết & Ràng Buộc |
|:---:|:---|:---|
| **BR-01** | Giới hạn số lượng mua thiết bị | Mỗi đơn hàng không được đặt quá 05 thiết bị cùng loại (Access Point Wi-Fi 6, IP Camera) nhằm chống đầu cơ. |
| **BR-02** | Ràng buộc tồn kho chi nhánh | Địa chỉ giao hàng thuộc Quận/Huyện nào thì phải kiểm tra tồn kho tại Kho Vận phụ trách khu vực đó. |
| **BR-03** | Phí vận chuyển thiết bị | Đơn hàng thiết bị từ 500.000đ trở lên được miễn phí vận chuyển toàn quốc. Dưới 500.000đ tính phí cố định 30.000đ. |

### B. Bảng Tình Huống Kiểm Thử (Test Cases / Edge Cases)
| Mã TC | Kịch bản Ngoại lệ | Điều kiện kích hoạt | Kết quả mong đợi (Expected Output) |
|:---:|:---|:---|:---|
| **TC-EX-01** | Giỏ hàng quá giới hạn cho phép | Khách nhập số lượng thiết bị là 6 chiếc (vượt max 5). | Hệ thống báo lỗi ngay tại ô input: *"Số lượng tối đa cho mỗi đơn hàng là 5 thiết bị"*, vô hiệu hóa nút Tiếp tục. |
| **TC-EX-02** | Sản phẩm hết hàng trong lúc đang đặt | Khách đang ở bước thanh toán thì sản phẩm bị người khác mua hết tồn kho. | Cổng thanh toán chặn trừ tiền, popup hiển thị: *"Sản phẩm đã hết hàng, vui lòng chọn sản phẩm khác hoặc quay lại sau"*. |

---

## 5. PHÂN HỆ 4: DỊCH VỤ SỐ STANDALONE (FPT PLAY OTT) & XÁC THỰC SĐT

*Tài liệu gốc đính kèm: `fpt-scenarios-dich-vu-so-sa/Kich_Ban_Test_Dich_Vu_So_SA.md`*

### A. Bảng Quy Tắc Nghiệp Vụ (Business Rules)
| Mã Rule | Tên Quy Tắc | Mô Tả Chi Tiết & Ràng Buộc |
|:---:|:---|:---|
| **BR-01** | Kiểm tra trạng thái SĐT FPT Play ngầm | Hệ thống phải gọi API sang hệ thống FPT Play kiểm tra xem SĐT đăng ký đã có tài khoản hay chưa trước khi gửi OTP. |
| **BR-02** | Chống đè tài khoản hiện hữu | Nếu SĐT đang có gói FPT Play còn hạn sử dụng, hệ thống không cho phép đăng ký đè gói mới cùng loại mà hướng dẫn gia hạn. |

### B. Bảng Tình Huống Kiểm Thử (Test Cases / Edge Cases)
| Mã TC | Tình huống kiểm thử | Điều kiện kích hoạt | Kết quả mong đợi (Expected Output) |
|:---:|:---|:---|:---|
| **TC-EX-01** | SĐT đã kích hoạt tài khoản FPT Play trước đó | Nhập SĐT `0939536236` (đã có gói VVIP đang hoạt động). | Hệ thống phát hiện tài khoản hiện hữu, hiển thị thông báo: *"Số điện thoại này đã có gói dịch vụ FPT Play, vui lòng đăng nhập để gia hạn"*. |
| **TC-EX-02** | Nhập sai mã OTP quá 5 lần liên tiếp | Người dùng nhập sai OTP 5 lần trong vòng 5 phút. | Khóa tính năng gửi OTP trong 15 phút, hiển thị đếm ngược thời gian chờ để chống brute-force SMS. |
| **TC-EX-03** | Khách hàng đổi số điện thoại ở bước OTP | Khách bấm "Đổi số điện thoại" tại popup OTP. | Hủy mã OTP cũ, giải phóng session, cho phép nhập lại SĐT mới và reset số lần gửi OTP. |

---

## 6. QUY CHUẨN LOG LỖI, BẰNG CHỨNG KIỂM THỬ & NGHIỆM THU UAT

Khi thực hiện kiểm thử trên Template Excel UAT chuẩn FPT (`templates/uat_template_fpt_standard.xlsx`):
1. **Ghi nhận tại Sheet `Report`**:
   - Nếu `PASSED`: Ghi rõ thiết bị test, OS, Version.
   - Nếu `FAILED`: Cột `DESCRIPTION` bắt buộc phải có:
     - [Bước tái hiện]: 1, 2, 3...
     - [Kết quả thực tế]: Hệ thống báo lỗi gì, mã lỗi HTTP (400, 500), response body.
     - [Evidence]: Link ảnh chụp màn hình hoặc log console.
2. **Quy định phân loại lỗi**:
   - `S1 - Blocker`: Chặn đứng thanh toán, sập web, sai lệch số tiền thanh toán ➔ Fix ngay trong 2h.
   - `S2 - Major`: Lỗi tính toán ưu đãi sai, không nhận được OTP ➔ Fix trong 24h.
   - `S3 - Medium`: Lỗi hiển thị, sai câu chữ thông báo, chậm phản hồi ➔ Dời sang đợt bảo trì tiếp theo.
3. **Nghiệm thu ký duyệt (Sign-off)**:
   - 100% Happy Path Pass.
   - 0 lỗi S1/S2 tồn đọng.
   - PO xác nhận tại Sheet `Summary`.

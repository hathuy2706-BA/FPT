# THƯ MỤC THỰC HIỆN KIỂM THỬ CHẤP NHẬN NGƯỜI DÙNG (`uat`)

> **Quy chuẩn lưu trữ**: Thư mục này **CHỈ CHỨA DUY NHẤT** các file phục vụ trực tiếp cho quá trình thực hiện kiểm thử UAT (User Acceptance Testing) của Product Owner (PO), Business Analyst (BA) và QC Team. Tuyệt đối không lưu tài liệu đặc tả (BRD/PRD/URD) hay hình ảnh sơ đồ vào thư mục này.

---

## 1. Mục Đích & Phạm Vi Áp Dụng
- Tập trung các file kịch bản kiểm thử UAT, kết quả nghiệm thu, và công cụ đồng bộ dữ liệu nghiệm thu thực tế của dự án.
- Tách biệt hoàn toàn giữa **Tài liệu đặc tả (Doc)** và **File thực thi kiểm thử nghiệm thu (UAT)**.

---

## 2. Danh Mục File Trong Thư Mục

| Tên File | Định dạng | Mục đích sử dụng |
|:---|:---|:---|
| `UAT_GioHang_FPT_VN.xlsx` | Excel (.xlsx) | File Excel kịch bản kiểm thử UAT chi tiết (chuẩn form mẫu FPT Telecom: 4.0-BM/PM/HDCV/FTEL). PO/Tester mở trực tiếp file này để thực hiện test và ghi nhận kết quả (Pass/Fail/Untested). |
| `sync_uat.py` | Python Script (.py) | Tool hỗ trợ đồng bộ 2 chiều (Bidirectional Sync) giữa file Excel local và Google Sheets UAT Online. |

---

## 3. Quy Trình Vận Hành UAT Dành Cho PO / Tester
1. **Thực hiện kiểm thử**: Mở file `UAT_GioHang_FPT_VN.xlsx`, kiểm tra theo từng bước và điều kiện mong muốn, ghi nhận kết quả tại các cột tương ứng.
2. **Đồng bộ kết quả**:
   - Đẩy kết quả local lên Google Sheet online:
     ```bash
     python3 thuyttdoc/uat/sync_uat.py --push
     ```
   - Kéo kết quả mới nhất từ Google Sheet về máy:
     ```bash
     python3 thuyttdoc/uat/sync_uat.py --pull
     ```
3. **Giữ sạch thư mục**: Không tạo thêm các file rác, file nháp hay tài liệu đặc tả ngoài phạm vi UAT vào thư mục này.

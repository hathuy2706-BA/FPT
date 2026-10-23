# Lưu ý khi vẽ sơ đồ BPMN (Best Practices)

Dựa trên các phản hồi từ việc tinh chỉnh sơ đồ, dưới đây là các ghi chú quan trọng cần tuân thủ khi thiết kế và tạo sơ đồ BPMN trong tương lai:

## 1. Yêu cầu thẩm mỹ và bố cục
- **Chuẩn thẩm mỹ**: Các đường nét (lines) và mũi tên phải là **đường thẳng** hoặc **vuông góc** rõ ràng, tuyệt đối tránh các đường chéo nhau lộn xộn hoặc các đường thẳng bị vẽ tùy tiện.
- **Routing**: Sử dụng các thuộc tính định tuyến (routing hints) như `"VH"` (Vertical-Horizontal) hoặc `"HV"` (Horizontal-Vertical) để điều hướng các đường nét sao cho có các khúc cua vuông góc thay vì các đường chéo trực tiếp gây vướng víu.
- **Rẽ nhánh**: Với các luồng (flow) rẽ ngang, quay lui, hoặc trỏ đến đích (end event), cần phải thiết kế luồng vẽ vuông góc mạch lạc. Không chỉa mũi tên thẳng qua các block hoặc cắt ngang không cần thiết.

## 2. Xử lý khoảng trống và tránh chồng chéo (Overlaps)
- **Tuyệt đối không để chồng text lên đường kẻ hoặc hình khối**. Việc chồng chéo làm sơ đồ không thể đọc được.
- **Di chuyển vị trí label (Label Position - `lp`)**:
  - Đối với các hình thoi (Gateway), hãy chuyển text sang các vị trí trống (ví dụ: đưa sang **phía bên phải** của hình thoi) để không bị đè vào các đường kết nối ở trên/dưới/trái.
  - Đối với nút "Kết thúc" (End Event), nếu mũi tên đi vào từ bên cạnh hoặc phía trên, hãy dời label (ví dụ chữ "Kết thúc") xuống **phía dưới** (`"lp": "b"`) hoặc góc khác thích hợp.
  - Khi có luồng như "Mũi tên từ thanh toán sang hình thoi 'SPDV CÓ KÍCH HOẠT?'", cần kiểm tra kỹ và tách biệt text của đường kẻ với khối hình và các luồng khác.

## 3. Kiến trúc sinh code (Generator Engine)
- Sử dụng công cụ (Python generator như `gen_prd_cart_bpmn.py`) có khả năng điều khiển tuyệt đối (absolute control) đối với tọa độ (grid placement) và định tuyến (routing) thay vì dựa vào tự động bố cục (như `splines=ortho` thô của Graphviz) dễ gây rối.
- Tách biệt logic định tuyến tại các cổng rẽ nhánh (gateway) hoặc các điểm kết thúc để đảm bảo các đường không đi ra/đi vào cùng một phía đang chứa text.

*Ghi chú này sẽ được tham chiếu và áp dụng tự động cho các yêu cầu vẽ/sửa sơ đồ về sau.*

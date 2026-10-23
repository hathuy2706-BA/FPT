# Skill: BPMN Diagram Drawer — Chuẩn FPT Telecom

> **Khi nào dùng skill này:** User yêu cầu vẽ sơ đồ BPMN swimlane, luồng nghiệp vụ (business process), Customer Journey cho tài liệu URD/SRS, hoặc update lại sơ đồ đã có.
>
> **Phân biệt với Sequence/Flowchart:** BPMN dùng cho **luồng nghiệp vụ tổng quan** (ai làm gì, theo lane tác nhân). Sequence dùng cho **tương tác kỹ thuật API chi tiết** (hệ thống nào gọi hệ thống nào).

---

## 1. Ký hiệu BPMN bắt buộc

| Thành phần | Ký hiệu SVG | kind= | Ghi chú |
|---|---|---|---|
| **Start Event** | Vòng tròn mảnh, nền xanh lá | `"start"` | Điểm bắt đầu duy nhất |
| **End Event** | Vòng tròn đậm, nền đỏ nhạt | `"end"` | Mỗi kết cục 1 end riêng |
| **Task / Activity** | Chữ nhật bo góc | `"task"` | 1 hành động đơn |
| **Exclusive Gateway** | Hình thoi + ký hiệu **×** | `"gw"` | Rẽ nhánh loại trừ (Yes/No) |
| **Text Annotation** | Hộp nét đứt màu vàng | `ANNOT` | Gắn mã `[MODULE-BR-nn]` |
| **Sequence Flow** | Mũi tên liền `→` | `E` | Luồng tuần tự giữa node |
| **Back / Retry Flow** | Mũi tên đứt đỏ `⤶` | `BACK` | Quay lại điều chỉnh / thử lại |
| **Swimlane / Pool** | Băng dọc có header | `LANES` | 1 lane = 1 tác nhân |

### Màu chuẩn 3 lane FPT
| Lane | Màu viền | Màu nền | Vai trò |
|---|---|---|---|
| 0 — Khách hàng | `#1f4e78` | `#eef3fb` | Hành động người dùng cuối |
| 1 — Website / FE | `#2e75b6` | `#eef7fd` | Hiển thị & điều phối FE |
| 2 — Backend & Tích hợp | `#7030a0` | `#f6f0fb` | Xử lý nghiệp vụ, API, SPF/CRM |

> Có thể thêm lane 3+ bằng cách mở rộng `LANES`, `LANE_X`, `LANE_COLOR` trong `gen_bpmn_template.py`.

---

## 2. Quy trình tạo sơ đồ BPMN (5 bước)

### Bước 1 — Copy & đặt tên generator
```bash
cp .agent/skills/diagram-drawer/templates/bpmn_template/gen_bpmn_template.py \
   diagrams/gen_[tên_module]_bpmn.py
```

### Bước 2 — Khai báo nodes, edges, back-edges, annotations
Chỉnh sửa file `diagrams/gen_[tên]_bpmn.py`:

```python
# Cấu trúc node: "id": (lane, row, half, kind, label)
N1 = {
    "start":  (0, 0, "c", "start", "Bắt đầu\nMua sắm"),
    "k1":     (0, 1, "c", "task",  "Chọn sản phẩm\ntrên PDP"),
    "f1":     (1, 2, "c", "task",  "Tạo dòng giỏ\ntheo Line_Key"),
    "g_dup":  (1, 3, "c", "gw",    "Trùng\nLine_Key?"),
    "f2":     (1, 4, "l", "task",  "Cộng dồn\nsố lượng"),
    "f3":     (1, 4, "r", "task",  "Tạo dòng\nmới riêng"),
    "end":    (0, 5, "c", "end",   "Hoàn tất"),
}

# Sequence flows
E1 = [
    ("start", "k1",    "",    0),
    ("k1",    "f1",    "",    0),
    ("f1",    "g_dup", "",    0),
    ("g_dup", "f2",    "Có",  0),
    ("g_dup", "f3",    "Không", 0),
    ("f2",    "end",   "",    0),
    ("f3",    "end",   "",    0),
]

# Back / retry
BACK1 = [("g_dup", "k1", "Lỗi → thử lại")]

# Text Annotation (Business Rules)
ANNOT1 = [
    ("[CART-BR-01] Line_Key = SKU + Thuộc tính + Chu kỳ.\nTrùng → cộng dồn SL; khác → tách dòng.", "f1", "r"),
]

build(
    title="SƠ ĐỒ BPMN TỔNG QUAN — GIỎ HÀNG (FPT.VN)",
    N=N1, E=E1, BACK=BACK1, ANNOT=ANNOT1,
    nrows=6,
    outfile="diagrams/cart_overview_bpmn.svg",
)
```

### Bước 3 — Chạy generator
```bash
python3 diagrams/gen_[tên]_bpmn.py
# Output: diagrams/[tên]_bpmn.svg  (kích thước: ~1960 × H px)
```

### Bước 4 — Convert SVG → PNG (cần `brew install librsvg`)
```bash
# -w 1600: đủ sắc nét khi in A4 Word (~250 DPI), file nhỏ gọn
rsvg-convert -w 1600 diagrams/[tên]_bpmn.svg -o diagrams/[tên]_bpmn.png

# Lấy kích thước thực để điền vào HTML attribute
python3 -c "
import struct
with open('diagrams/[tên]_bpmn.png','rb') as f:
    f.read(8); f.read(4); f.read(4)
    w = struct.unpack('>I', f.read(4))[0]
    h = struct.unpack('>I', f.read(4))[0]
dw = 605; dh = round(605 * h / w)
print(f'width={dw} height={dh}')
"
```

### Bước 5 — Nhúng vào URD (.doc HTML-based)
```python
import base64, struct, re

def get_dims(path):
    with open(path, 'rb') as f:
        f.read(8); f.read(4); f.read(4)
        w = struct.unpack('>I', f.read(4))[0]
        h = struct.unpack('>I', f.read(4))[0]
    return w, h

def b64img(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path,'rb').read()).decode()

p = 'thuyttdoc/[urd_file].doc'
lines = open(p, encoding='utf-8').read().split('\n')

# Danh sách ảnh theo thứ tự xuất hiện trong file
diagrams = [
    'diagrams/[tên]_overview_bpmn.png',
    'diagrams/[tên]_group1_bpmn.png',   # nếu có
]

img_indices = [i for i, l in enumerate(lines) if re.match(r'\s*<img class="diagram-img"', l)]
assert len(img_indices) == len(diagrams)

for line_num, path in zip(img_indices, diagrams):
    w, h = get_dims(path)
    dw, dh = 605, round(605 * h / w)
    lines[line_num] = (
        f'<img class="diagram-img" width="{dw}" height="{dh}" '
        f'style="width:16.0cm; height:auto; display:block; margin:0 auto; '
        f'border:none; padding:0; mso-width-source:userset; mso-height-source:userset;" '
        f'src="{b64img(path)}">'
    )

open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('Done')
```

---

## 3. Cấu trúc node — tham số chi tiết

### Format
```python
"id": (lane, row, half, kind, label)
```

| Tham số | Kiểu | Giá trị | Ghi chú |
|---|---|---|---|
| `lane` | int | `0` / `1` / `2` | 0=Khách hàng · 1=FE · 2=BE |
| `row` | int | `0` → `N` | Hàng dọc 0-based từ trên xuống |
| `half` | str | `"c"` / `"l"` / `"r"` | Vị trí ngang trong lane; `"l"`/`"r"` → NARROW box |
| `kind` | str | `"start"` / `"end"` / `"task"` / `"gw"` | Loại ký hiệu BPMN |
| `label` | str | text, `\n` xuống dòng | ≤ 3 dòng, ≤ 30 ký tự/dòng |

### Quy ước đặt id
| Tiền tố | Dùng cho |
|---|---|
| `start` / `end` | Điểm đầu/cuối |
| `k1`, `k2`... | Bước của **K**hách hàng (lane 0) |
| `f1`, `f2`... | Bước của **F**rontend (lane 1) |
| `b1`, `b2`... | Bước của **B**ackend (lane 2) |
| `g_<tên>` | **G**ateway (rẽ nhánh) |

---

## 4. Điều chỉnh layout khi sơ đồ bị lệch / tràn

| Triệu chứng | Điều chỉnh trong file gen_*.py |
|---|---|
| Node chồng lên nhau | Tăng `ROW_H`: 94 → 104 |
| Label bị cắt | Giảm `fs` trong `tspans()`: 9.6 → 8.5 |
| Text Annotation tràn canvas | Tăng `LEFT_PAD`/`RIGHT_PAD`: 290 → 340 |
| Lane quá chật | Tăng `LANE_W`: 460 → 510 |
| Back-edge đè lên nội dung | Tăng `LEFT_PAD`: 290 → 360 |
| Sơ đồ quá cao | Giảm `ROW_H` hoặc gộp node ít quan trọng |
| Text Annotation bị nhỏ | Tăng `bh` (chiều cao hộp) và `fs` trong `draw_annot()` |

---

## 5. Checklist trước khi nhúng vào URD

- [ ] SVG mở trong browser — không có node chồng nhau, không tràn viền canvas
- [ ] Text Annotation hiển thị đủ nội dung, không bị cắt
- [ ] Back-edge nét đứt đỏ đi đúng từ gateway → node quay lại
- [ ] Legend ở đáy hiển thị đầy đủ ký hiệu
- [ ] PNG xuất từ `rsvg-convert -w 1600` — kiểm tra kích thước bằng `struct.unpack`
- [ ] `width`/`height` px trong HTML khớp đúng tỉ lệ PNG thực
- [ ] Trong Word: sơ đồ không tràn lề, không bị blur, không bị cắt trang

---

## 6. File trong thư mục này

| File | Mục đích |
|---|---|
| `SKILL.md` | Hướng dẫn skill BPMN (file này) |
| `gen_bpmn_template.py` | Generator template đầy đủ — copy để bắt đầu sơ đồ mới |

**Xem thêm:**
- Generator thực tế đã kiểm chứng: [`diagrams/gen_cart_bpmn.py`](../../../../diagrams/gen_cart_bpmn.py)
- Quy trình nhúng vào URD: [`ba-senior/templates/urd-template.md`](../../../ba-senior/templates/urd-template.md) → PHẦN 5 & 6

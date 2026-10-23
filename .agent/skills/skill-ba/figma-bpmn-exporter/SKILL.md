---
name: figma-bpmn-exporter
description: Xuất sơ đồ BPMN/SVG từ thư mục diagrams/ lên Figma board dưới dạng vector native editable. Kích hoạt khi user yêu cầu đưa sơ đồ vào Figma, cập nhật sơ đồ trên Figma, hoặc sync diagram từ repo lên board BA.
---

# Skill: Figma BPMN Exporter

Skill này tự động hoá quy trình đưa sơ đồ SVG BPMN từ repo vào Figma board dưới dạng **vector native** — có thể chỉnh sửa màu, shape, text trực tiếp trong Figma mà không cần redraw.

---

## Kiến trúc

```
.agent/skills/figma-bpmn-exporter/
├── SKILL.md               ← file này
├── plugin/
│   ├── manifest.json      ← Figma plugin metadata (static)
│   └── code.js            ← Plugin logic (static, dùng createNodeFromSvg)
└── scripts/
    └── build_plugin.py    ← Sinh ui.html với SVG embedded, chạy mỗi lần export
```

**Nguồn SVG**: `diagrams/*.svg` trong project root  
**Output Figma**: Native FrameNode với vector paths — fully editable

---

## Quy trình sử dụng

### Bước 1 — Build plugin UI

Chạy script để nhúng SVG mới nhất vào plugin:

```bash
python3 .agent/skills/figma-bpmn-exporter/scripts/build_plugin.py
```

Script tự động:
- Quét tất cả `diagrams/*.svg`
- Sinh `plugin/ui.html` với SVG embedded sẵn
- In ra danh sách sơ đồ sẽ được export

Để chỉ export một số sơ đồ cụ thể:

```bash
python3 .agent/skills/figma-bpmn-exporter/scripts/build_plugin.py \
  --include cart_overview_bpmn cart_single_bpmn cart_merge_bpmn
```

### Bước 2 — Load plugin vào Figma Desktop

1. Mở **Figma Desktop App**
2. Mở board target (VD: board PO/BA)
3. Menu **Plugins** → **Development** → **Import plugin from manifest...**
4. Chọn file: `.agent/skills/figma-bpmn-exporter/plugin/manifest.json`

> Plugin chỉ cần import **một lần**. Các lần sau dùng **Reload** (Ctrl+Alt+P).

### Bước 3 — Chạy plugin

1. **Plugins** → **Development** → **BPMN → Figma Exporter**
2. Chọn sơ đồ muốn thêm (checkbox)
3. Click **"Thêm vào Figma Board"**
4. Plugin tạo các Frame chứa vector paths, tự scroll/zoom đến vị trí vừa tạo

### Bước 4 — Edit sơ đồ trên Figma

Sau khi import, mỗi sơ đồ là một **Frame** chứa:
- Vector paths (shape BPMN: pool, task, gateway, arrow)
- Text layers (label của từng node)
- Có thể double-click vào bất kỳ element nào để edit

---

## Khi cập nhật sơ đồ trong repo

Mỗi khi SVG trong `diagrams/` thay đổi:

```bash
# 1. Rebuild plugin UI
python3 .agent/skills/figma-bpmn-exporter/scripts/build_plugin.py

# 2. Trong Figma: Ctrl+Alt+P (Reload Plugin)
# 3. Xóa frame cũ trên board (nếu cần)
# 4. Chạy lại plugin → chọn sơ đồ đã update
```

---

## Yêu cầu

- **Figma Desktop App** (Web app không load plugin development)
- SVG files phải nằm trong `diagrams/` và có định dạng BPMN chuẩn
- Python 3.x (để chạy build script)

---

## Nguyên tắc kỹ thuật

Plugin dùng `figma.createNodeFromSvg(svgString)` — API native của Figma SDK:
- Input: SVG string
- Output: `FrameNode` chứa toàn bộ vector paths, groups, text từ SVG
- Kết quả **không phải image** — là các Figma node thực sự, edit được

Không cần Figma API token. Không gọi external API. Chạy hoàn toàn trong sandbox của Figma plugin.

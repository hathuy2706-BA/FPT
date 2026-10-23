# -*- coding: utf-8 -*-
"""
BPMN Generator Template — Chuẩn FPT Telecom
============================================
Nguồn gốc: chuẩn hoá từ diagrams/gen_cart_bpmn.py (URD Giỏ hàng & Checkout đa SP).

Cách dùng:
  1. Copy file này → diagrams/gen_[tên]_bpmn.py
  2. Thay [PLACEHOLDER] theo luồng nghiệp vụ cụ thể
  3. Chạy: python3 diagrams/gen_[tên]_bpmn.py
  4. Convert SVG → PNG: rsvg-convert -w 1600 diagrams/[tên].svg -o diagrams/[tên].png
  5. Nhúng vào URD: xem hướng dẫn trong ba-senior/templates/urd-template.md PHẦN 5

Yêu cầu: Python 3.x (stdlib only, không cần thư viện ngoài)
"""

ESC = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ============================================================
# BƯỚC 1 — CẤU HÌNH LAYOUT
# Điều chỉnh khi thêm/bớt lane hoặc cần nhiều không gian hơn
# ============================================================
LEFT_PAD  = 290   # px lề trái  (chứa back-edge nét đứt + Text Annotation bên trái)
RIGHT_PAD = 290   # px lề phải (chứa Text Annotation bên phải)
LANE_W    = 460   # px chiều rộng mỗi lane  (tăng nếu label quá dài)
LANE_X    = {0: LEFT_PAD, 1: LEFT_PAD + LANE_W, 2: LEFT_PAD + 2 * LANE_W}

# Định nghĩa các lane (tác nhân) — thay tên và màu theo đặc thù luồng
# Format: (tên_hiển_thị, x_bắt_đầu, chiều_rộng, màu_viền, màu_nền)
LANES = [
    ("[LANE 0 — VD: KHÁCH HÀNG (CUSTOMER)]",
     LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("[LANE 1 — VD: WEBSITE FPT.VN (FRONTEND)]",
     LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("[LANE 2 — VD: BACKEND & TÍCH HỢP (SPF · CRM · Payment · Product Hub)]",
     LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
LANE_COLOR = {0: "#1f4e78", 1: "#2e75b6", 2: "#7030a0"}  # màu viền node khớp lane

HEADER_H = 46    # px chiều cao dải tiêu đề lane
ROW_H    = 94    # px khoảng cách dọc mỗi hàng (tăng → 104+ nếu label 3 dòng)
TOP      = 84    # px khoảng từ đỉnh SVG đến top lane (chứa tiêu đề sơ đồ)
BOXW     = 270   # px chiều rộng Task box khi half="c"
BOXH     = 62    # px chiều cao Task box
NARROW   = 206   # px chiều rộng Task box khi half="l" hoặc "r" (2 nhánh song song)


# ============================================================
# ENGINE — KHÔNG CẦN THAY ĐỔI PHẦN NÀY
# ============================================================
def lane_cx(l, half="c"):
    """Tâm ngang trong lane l: 'c'=giữa, 'l'=28% từ trái, 'r'=72% từ trái."""
    x = LANE_X[l]
    if half == "c": return x + LANE_W / 2
    if half == "l": return x + LANE_W * 0.28
    return x + LANE_W * 0.72


def row_y(r):
    """Tâm dọc của hàng r (0-based từ trên xuống)."""
    return TOP + HEADER_H + r * ROW_H + ROW_H / 2


def build(title, N, E, BACK, ANNOT, nrows, outfile):
    """
    Sinh file SVG cho 1 sơ đồ BPMN swimlane dọc.

    Tham số
    -------
    title   str   Tiêu đề hiển thị ở đỉnh sơ đồ
    N       dict  Node definitions:
                    { "id": (lane, row, half, kind, label) }
                    lane : 0 / 1 / 2
                    row  : int 0-based (hàng dọc từ trên xuống)
                    half : "c" | "l" | "r"
                    kind : "start" | "end" | "task" | "gw"
                    label: str — dùng '\\n' để xuống dòng (tối đa 3 dòng)
    E       list  Sequence flows:
                    [ (from_id, to_id, label, dashed) ]
                    dashed: 0=liền, 1=nét đứt
    BACK    list  Back / retry flows (vẽ vòng ngoài bên trái):
                    [ (from_id, to_id, label) ]
    ANNOT   list  Text Annotation (Business Rule):
                    [ (text, anchor_node_id, side) ]
                    side: "r"=phải lane | "l"=trái lane
    nrows   int   Tổng số hàng = max(row trong N) + 1
    outfile str   Đường dẫn file SVG xuất ra
    """
    def npos(nid):
        l, r, half, kind, label = N[nid][:5]
        return lane_cx(l, half), row_y(r), kind, label, l

    W = LANE_X[2] + LANE_W + RIGHT_PAD
    H = TOP + HEADER_H + nrows * ROW_H + 56

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
               f'viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">')
    out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
    out.append(f'<text x="{W/2}" y="34" font-size="20" font-weight="bold" '
               f'fill="#1f4e78" text-anchor="middle">{ESC(title)}</text>')
    out.append('<defs>'
               '<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" '
               'orient="auto" markerUnits="strokeWidth">'
               '<path d="M0,0 L7,3 L0,6 Z" fill="#444"/></marker>'
               '</defs>')

    # ── Lanes ──
    laneTop, laneBot = TOP, H - 22
    for name, x, w, c, fill in LANES:
        out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{laneBot-laneTop}" '
                   f'fill="{fill}" stroke="{c}" stroke-width="1.4"/>')
        out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{HEADER_H}" fill="{c}"/>')
        out.append(f'<text x="{x+w/2}" y="{laneTop+HEADER_H/2+5}" font-size="12.5" '
                   f'font-weight="bold" fill="#ffffff" text-anchor="middle">{ESC(name)}</text>')

    # ── Helper: render text đa dòng ──
    def tspans(label, cx, cy, fs=10, fill="#000", weight="normal"):
        lines = label.split("\n")
        y0 = cy - (len(lines) - 1) * fs * 0.62
        s = (f'<text x="{cx}" y="{y0+fs*0.35}" font-size="{fs}" '
             f'fill="{fill}" font-weight="{weight}" text-anchor="middle">')
        for j, ln in enumerate(lines):
            s += f'<tspan x="{cx}" dy="{0 if j == 0 else fs*1.24}">{ESC(ln)}</tspan>'
        return s + '</text>'

    # ── Helper: điểm neo cạnh node ──
    def anchor(nid, where):
        cx, cy, kind, label, l = npos(nid)
        if kind == "gw":              h = w = 70
        elif kind in ("start","end"): h = w = 52
        else: h = BOXH; w = NARROW if N[nid][2] != "c" else BOXW
        if where == "b": return cx, cy + h / 2
        if where == "t": return cx, cy - h / 2
        if where == "l": return cx - w / 2, cy
        return cx + w / 2, cy  # "r"

    # ── Sequence Flow (vẽ trước — nằm dưới node) ──
    def draw_edge(a, b, label, dashed):
        ax, ay = anchor(a, "b")
        bx, by = anchor(b, "t")
        dash = ' stroke-dasharray="6,4"' if dashed else ''
        if abs(ax - bx) < 2:
            d = f'M{ax},{ay} L{bx},{by}'
            lx, ly = ax + 8, (ay + by) / 2
        else:
            midy = ay + (by - ay) * 0.5
            d = f'M{ax},{ay} L{ax},{midy} L{bx},{midy} L{bx},{by}'
            lx, ly = (ax + bx) / 2, midy - 5
        out.append(f'<path d="{d}" fill="none" stroke="#444" stroke-width="1.5"'
                   f'{dash} marker-end="url(#arr)"/>')
        if label:
            wlbl = len(label) * 6.2 + 8
            out.append(f'<rect x="{lx-wlbl/2}" y="{ly-9}" width="{wlbl}" height="15" '
                       f'fill="#ffffff" opacity="0.92"/>')
            out.append(f'<text x="{lx}" y="{ly+3}" font-size="9.5" fill="#333" '
                       f'text-anchor="middle">{ESC(label)}</text>')

    for a, b, lbl, dsh in E:
        draw_edge(a, b, lbl, dsh)

    # ── Back / Retry Flow (vòng ngoài bên trái, nét đứt đỏ) ──
    def draw_back(a, b, label, xx):
        ax, ay = anchor(a, "l")
        bx, by = anchor(b, "l")
        d = f'M{ax},{ay} L{xx},{ay} L{xx},{by} L{bx},{by}'
        out.append(f'<path d="{d}" fill="none" stroke="#c62828" stroke-width="1.4" '
                   f'stroke-dasharray="6,4" marker-end="url(#arr)"/>')
        out.append(f'<text x="{xx+4}" y="{(ay+by)/2}" font-size="9.5" fill="#c62828" '
                   f'text-anchor="start" transform="rotate(-90 {xx+4} {(ay+by)/2})">'
                   f'{ESC(label)}</text>')

    for i, (a, b, lbl) in enumerate(BACK):
        xx = LEFT_PAD - 250 if i == 0 else LANE_X[1] - 24
        draw_back(a, b, lbl, xx)

    # ── Text Annotation — Business Rule ──
    def draw_annot(text, nid, side):
        cx, cy, kind, label, l = npos(nid)
        bw, bh = 252, 50
        if side == "r":
            ax = LANE_X[l] + LANE_W; bxs = ax + 18; endx = bxs
        else:
            ax = LANE_X[l]; bxs = ax - 18 - bw; endx = bxs + bw
        by_ = cy - bh / 2
        out.append(f'<path d="M{ax},{cy} L{endx},{cy}" stroke="#bf8f00" '
                   f'stroke-width="1.1" stroke-dasharray="3,3"/>')
        out.append(f'<rect x="{bxs}" y="{by_}" width="{bw}" height="{bh}" '
                   f'fill="#fffaf0" stroke="#bf8f00" stroke-width="1.1" '
                   f'stroke-dasharray="5,3" rx="3"/>')
        out.append(tspans(text, bxs + bw / 2, cy, fs=8.2, fill="#7a5b00"))

    for t, nid, side in ANNOT:
        draw_annot(t, nid, side)

    # ── Nodes (vẽ sau — nằm trên cùng) ──
    for nid in N:
        cx, cy, kind, label, l = npos(nid)
        col = LANE_COLOR[l]
        if kind == "start":
            out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#e8f5e9" '
                       f'stroke="#2e7d32" stroke-width="2"/>')
            out.append(tspans(label, cx, cy, fs=9, fill="#1b5e20", weight="bold"))
        elif kind == "end":
            out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#ffebee" '
                       f'stroke="#c62828" stroke-width="3.4"/>')
            out.append(tspans(label, cx, cy, fs=8.5, fill="#b71c1c", weight="bold"))
        elif kind == "gw":
            r = 35
            out.append(f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" '
                       f'fill="#fff2cc" stroke="#bf8f00" stroke-width="1.8"/>')
            out.append(f'<text x="{cx}" y="{cy-r-6}" font-size="15" font-weight="bold" '
                       f'fill="#bf8f00" text-anchor="middle">\xd7</text>')
            out.append(tspans(label, cx, cy, fs=8.8, fill="#5b4500", weight="bold"))
        else:  # task
            w = NARROW if N[nid][2] != "c" else BOXW
            out.append(f'<rect x="{cx-w/2}" y="{cy-BOXH/2}" width="{w}" height="{BOXH}" '
                       f'rx="9" fill="#ffffff" stroke="{col}" stroke-width="1.7"/>')
            out.append(tspans(label, cx, cy, fs=9.6, fill="#1a1a1a"))

    # ── Legend ──
    out.append(
        f'<text x="{W/2}" y="{H-15}" font-size="11" fill="#555" text-anchor="middle">'
        'K\xed hiệu BPMN: '
        '◯ Start Event  '
        '◉ End Event  '
        '▭ Task  '
        '◇\xd7 Exclusive Gateway  '
        '╌╌ Text Annotation  '
        '—▸ Sequence Flow  '
        '╌▸ Luồng quay lại'
        '</text>'
    )
    out.append('</svg>')

    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"OK  {outfile}  ({W}x{H})")


# ============================================================
# BƯỚC 2 — KHAI BÁO SƠ ĐỒ
# Mỗi sơ đồ = 1 khối N / E / BACK / ANNOT + 1 lần gọi build()
# ============================================================

# ──────────────────────────────────────────────────────────────
# SƠ ĐỒ 1 — TỔNG QUAN (bắt buộc có trong mọi URD)
# ──────────────────────────────────────────────────────────────
# Quy ước đặt id:
#   start / end        — điểm đầu / cuối
#   k1, k2, k3 ...     — bước của Khách hàng (lane 0)
#   f1, f2, f3 ...     — bước của Frontend   (lane 1)
#   b1, b2, b3 ...     — bước của Backend    (lane 2)
#   g_<tên> ...        — Exclusive Gateway

N1 = {
    # id           lane  row  half  kind     label
    "start":      (0,    0,   "c",  "start", "Bắt đầu\n[Điểm khởi đầu]"),
    "k1":         (0,    1,   "c",  "task",  "[Hành động KH 1]\n[Chi tiết nếu cần]"),
    "f1":         (1,    2,   "c",  "task",  "[Hành động FE 1]\n[Chi tiết]"),
    "b1":         (2,    3,   "c",  "task",  "[Xử lý BE / Tích hợp]\n[Hệ thống liên quan]"),
    "g_check":    (2,    4,   "c",  "gw",    "[Điều kiện\nrẽ nhánh?]"),
    "k2":         (0,    5,   "c",  "task",  "[Hành động KH 2]\n[Sau rẽ nhánh]"),
    "f2":         (1,    6,   "c",  "task",  "[Hiển thị kết quả\nFE]"),
    "b2":         (2,    7,   "c",  "task",  "[Tạo đơn / Kích hoạt\ntrên SPF]"),
    "f3":         (1,    8,   "c",  "task",  "Thank You / Xác nhận\n[Mã đơn · Trạng thái]"),
    "end":        (0,    9,   "c",  "end",   "Hoàn tất\n[Mô tả kết thúc]"),
}

E1 = [
    # from         to          label_mũi_tên      dashed
    ("start",      "k1",       "",                0),
    ("k1",         "f1",       "",                0),
    ("f1",         "b1",       "",                0),
    ("b1",         "g_check",  "",                0),
    ("g_check",    "k2",       "Có",              0),
    ("k2",         "f2",       "",                0),
    ("f2",         "b2",       "",                0),
    ("b2",         "f3",       "",                0),
    ("f3",         "end",      "",                0),
]

BACK1 = [
    # from          to       label_dọc (xoay -90°)
    ("g_check",    "k1",    "[Không] → thử lại / điều chỉnh"),
]

ANNOT1 = [
    # text_annotation                                              anchor      side
    ("[MODULE-BR-01] [Mô tả quy tắc nghiệp vụ 1].\n[Điều kiện áp dụng].",  "f1",  "r"),
    ("[MODULE-BR-02] [Mô tả quy tắc nghiệp vụ 2].\n[Nguồn cấu hình].",     "b1",  "r"),
    ("[MODULE-BR-03] [Quy tắc đặc thù luồng này].\n[Logic BE xử lý].",      "b2",  "r"),
]

build(
    title="SƠ ĐỒ BPMN TỔNG QUAN — [TÊN MODULE / LUỒNG NGHIỆP VỤ] (FPT.VN)",
    N=N1, E=E1, BACK=BACK1, ANNOT=ANNOT1,
    nrows=10,   # = max(row trong N1) + 1
    outfile="diagrams/[tên]_overview_bpmn.svg",
)


# ──────────────────────────────────────────────────────────────
# SƠ ĐỒ 2 — LUỒNG CHI TIẾT NHÓM 1 (bỏ comment khi cần)
# ──────────────────────────────────────────────────────────────
# N2 = {
#     "start": (0, 0, "c", "start", "Bắt đầu\n[Nhóm 1]"),
#     # ... thêm node
#     "end":   (0, X, "c", "end",   "Hoàn tất"),
# }
# E2 = [ ... ]
# BACK2 = [ ... ]
# ANNOT2 = [ ... ]
# build(
#     title="SƠ ĐỒ BPMN — [TÊN NHÓM 1]",
#     N=N2, E=E2, BACK=BACK2, ANNOT=ANNOT2,
#     nrows=...,
#     outfile="diagrams/[tên]_group1_bpmn.svg",
# )


# ──────────────────────────────────────────────────────────────
# SƠ ĐỒ 3 — LUỒNG CHI TIẾT NHÓM 2 (bỏ comment khi cần)
# ──────────────────────────────────────────────────────────────
# N3 = { ... }
# E3 = [ ... ]
# BACK3 = [ ... ]
# ANNOT3 = [ ... ]
# build(
#     title="SƠ ĐỒ BPMN — [TÊN NHÓM 2]",
#     N=N3, E=E3, BACK=BACK3, ANNOT=ANNOT3,
#     nrows=...,
#     outfile="diagrams/[tên]_group2_bpmn.svg",
# )

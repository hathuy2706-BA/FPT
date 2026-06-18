# -*- coding: utf-8 -*-
"""BPMN Swimlane – Luồng Voucher Phase 2 (Internet/Combo & SKU/Camera) – v2 clean routing."""

ESC = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

LEFT_PAD   = 50
RIGHT_PAD  = 170    # khoảng trống bên phải cho BACK arrow
LANE_W     = 440
LANE_X     = {0: LEFT_PAD, 1: LEFT_PAD + LANE_W, 2: LEFT_PAD + 2 * LANE_W}
LANES = [
    ("KHÁCH HÀNG",                              LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("WEBSITE FPT.VN  (FRONTEND)",              LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("BACKEND  &  ECP  (VOUCHER ENGINE)",       LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
LANE_COLOR = {0: "#1f4e78", 1: "#2e75b6", 2: "#7030a0"}

HEADER_H = 46
ROW_H    = 92
TOP      = 72
BOXW     = 286
BOXH     = 62
GW_R     = 34     # gateway half-size

def lane_cx(l):
    return LANE_X[l] + LANE_W / 2

def row_cy(r):
    return TOP + HEADER_H + r * ROW_H + ROW_H / 2

# ── Node table: id → (lane, row, kind, label) ──────────────────────────────
# kind: start | end | task | gw
N = {
    "start": (0,  0, "start", "Bat dau"),
    "k1":    (0,  1, "task",  "Vao trang Checkout\n(Internet/Combo)\nhoac Gio hang (SKU/Camera)"),
    "f1":    (1,  2, "task",  "Hien thi section\n\"Ma giam gia\"\nhoac \"Uu dai\""),
    "k2":    (0,  3, "task",  "Click \"Chon uu dai\"\nhoac nhap ma tay"),
    "f2":    (1,  4, "task",  "Goi ECP API\nlay danh sach voucher KH"),
    "c1":    (2,  4, "task",  "Tra danh sach voucher\n(ten / mo ta / anh tu CMS)"),
    "f3":    (1,  5, "task",  "Hien thi Popup uu dai:\n- Active len dau  -  Label D-3\n- Scroll khi noi dung > 452px"),
    "k3":    (0,  6, "task",  "Chon voucher tu popup\nhoac nhap ma tay\n->  Bam \"Ap dung\""),
    "f4":    (1,  6, "task",  "Gui validate request\n(ma  .  PTTT  .  don  .  dia chi)"),
    "c2":    (2,  6, "task",  "Validate voucher:\n- PTTT  -  Don toi thieu\n- SL SP  -  Khu vuc  -  Loai tru"),
    "gw":    (2,  7, "gw",    "Voucher\nhop le?"),
    "c3":    (2,  8, "task",  "Tinh so tien giam\n->  Tra ket qua hop le"),
    "f5":    (1,  8, "task",  "Cap nhat tong tien\n\"1 uu dai dang ap dung\"\n->  Dong popup"),
    "k4":    (0,  8, "task",  "Xac nhan don hang\n&  Thanh toan"),
    "c5":    (2,  9, "task",  "Final check voucher\n->  Tao don SPF"),
    "end":   (0, 10, "end",   "Don hang\nhoan tat"),
}

# ── Forward edges: (src, dst, label) ─────────────────────────────────────
# Routing auto-detected: same row -> horizontal; cross-row -> L-shape orthogonal
EDGES = [
    ("start", "k1",  ""),
    ("k1",    "f1",  ""),
    ("f1",    "k2",  ""),
    ("k2",    "f2",  ""),
    ("f2",    "c1",  ""),
    ("c1",    "f3",  ""),
    ("f3",    "k3",  ""),
    ("k3",    "f4",  ""),
    ("f4",    "c2",  ""),
    ("c2",    "gw",  ""),
    ("gw",    "c3",  "Hop le"),
    ("c3",    "f5",  ""),
    ("f5",    "k4",  ""),
    ("k4",    "c5",  ""),
    ("c5",    "end", ""),
]

# ── Backward (retry) arrows: (src, dst, label) ────────────────────────────
# Routed via RIGHT side of diagram (outside BE lane)
BACK = [
    ("gw", "k3", "Loi: FE hien thi\nthong bao inline/toast\nKH thu lai"),
]

# ── Annotations (text boxes): (nid, side, text) ──────────────────────────
ANNOT = [
    ("f3", "l", "BR01\nTen/mo ta/anh voucher\ndo CMS (ECP) cau hinh"),
    ("c2", "r", "BR02\nCo cau loai tru:\nExclusion Group tai ECP"),
]

# ──────────────────────────────────────────────────────────────────────────
# SVG builder
# ──────────────────────────────────────────────────────────────────────────

def build_svg():
    nrows   = max(v[1] for v in N.values()) + 1
    TOTAL_W = LEFT_PAD + 3 * LANE_W + RIGHT_PAD
    TOTAL_H = TOP + HEADER_H + nrows * ROW_H + 48

    def npos(nid):
        l, r, kind, label = N[nid]
        return lane_cx(l), row_cy(r), kind, label, l

    def anchor(nid, where):
        cx, cy, kind, label, l = npos(nid)
        if kind == "gw":
            hw = GW_R
            ww = GW_R
        elif kind in ("start", "end"):
            hw = 24
            ww = 24
        else:
            hw = BOXH / 2
            ww = BOXW / 2
        if where == "b": return cx, cy + hw
        if where == "t": return cx, cy - hw
        if where == "l": return cx - ww, cy
        if where == "r": return cx + ww, cy

    def same_row(a, b):
        return N[a][1] == N[b][1]

    def tspans(label, cx, cy, fs=10, fill="#111", weight="normal"):
        lines = label.split("\n")
        lh = fs * 1.28
        y0 = cy - (len(lines) - 1) * lh / 2
        s = '<text x="%.1f" y="%.1f" font-size="%s" fill="%s" font-weight="%s" text-anchor="middle">' % (cx, y0, fs, fill, weight)
        for i, ln in enumerate(lines):
            dy = "" if i == 0 else ' dy="%.1f"' % lh
            s += '<tspan x="%.1f"%s>%s</tspan>' % (cx, dy, ESC(ln))
        return s + "</text>"

    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" font-family="Arial, sans-serif">' % (TOTAL_W, TOTAL_H, TOTAL_W, TOTAL_H),
        '<rect width="%d" height="%d" fill="#ffffff"/>' % (TOTAL_W, TOTAL_H),
        '<defs>'
        '<marker id="arr" markerWidth="9" markerHeight="7" refX="7" refY="3.5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L7,3.5 L0,7 Z" fill="#444"/></marker>'
        '<marker id="arr_red" markerWidth="9" markerHeight="7" refX="7" refY="3.5" orient="auto" markerUnits="strokeWidth">'
        '<path d="M0,0 L7,3.5 L0,7 Z" fill="#c62828"/></marker></defs>',
    ]

    # Title
    out.append('<text x="%.1f" y="44" font-size="17" font-weight="bold" fill="#1f4e78" text-anchor="middle">SO DO BPMN -- LUONG CHON &amp; AP DUNG VOUCHER (PHASE 2)</text>' % (TOTAL_W / 2))

    # Swimlane backgrounds & headers
    lane_top = TOP
    lane_h   = HEADER_H + nrows * ROW_H
    for name, x, w, col, bg in LANES:
        out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="#c8d4e0" stroke-width="1.2"/>' % (x, lane_top, w, lane_h, bg))
        out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (x, lane_top, w, HEADER_H, col))
        out.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">%s</text>' % (x + w/2, lane_top + HEADER_H/2 + 5, ESC(name)))
        # Row guide lines
        for r in range(1, nrows):
            gy = TOP + HEADER_H + r * ROW_H
            out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#dde8f0" stroke-width="0.5"/>' % (x, gy, x+w, gy))

    # Pool border
    out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="#7a9abc" stroke-width="2" rx="4"/>' % (LEFT_PAD, lane_top, 3*LANE_W, lane_h))

    # ── Forward edges ────────────────────────────────────────────────────
    def draw_edge(a, b, label):
        if same_row(a, b):
            ax, ay = anchor(a, "r")
            bx, by = anchor(b, "l")
            d = "M%.1f,%.1f L%.1f,%.1f" % (ax, ay, bx, by)
            lx = (ax + bx) / 2
            ly = ay - 7
        else:
            ax, ay = anchor(a, "b")
            bx, by = anchor(b, "t")
            midy = (ay + by) / 2
            d = "M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" % (ax, ay, ax, midy, bx, midy, bx, by)
            lx = (ax + bx) / 2
            ly = midy - 5
        out.append('<path d="%s" fill="none" stroke="#444" stroke-width="1.6" marker-end="url(#arr)"/>' % d)
        if label:
            wl = len(label) * 6 + 10
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="14" fill="#ffffff" opacity="0.9" rx="2"/>' % (lx - wl/2, ly - 10, wl))
            out.append('<text x="%.1f" y="%.1f" font-size="9" fill="#1f4e78" text-anchor="middle" font-weight="bold">%s</text>' % (lx, ly + 1, ESC(label)))

    for a, b, lbl in EDGES:
        draw_edge(a, b, lbl)

    # ── Backward (BACK) arrows via right side ────────────────────────────
    xx_back = LEFT_PAD + 3 * LANE_W + 60
    for a, b, lbl in BACK:
        ax, ay = anchor(a, "r")
        bx, by = anchor(b, "r")
        d = "M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" % (ax, ay, xx_back, ay, xx_back, by, bx, by)
        out.append('<path d="%s" fill="none" stroke="#c62828" stroke-width="1.5" stroke-dasharray="7,4" marker-end="url(#arr_red)"/>' % d)
        if lbl:
            mid_y = (ay + by) / 2
            lines = lbl.split("\n")
            for i, ln in enumerate(lines):
                dy_val = i * 10 - len(lines) * 4
                out.append('<text x="%.1f" y="%.1f" font-size="8.5" fill="#c62828" text-anchor="middle">%s</text>' % (xx_back + 8, mid_y + dy_val, ESC(ln)))

    # ── Annotations ──────────────────────────────────────────────────────
    for nid, side, text in ANNOT:
        cx, cy, kind, label, l = npos(nid)
        bw, bh = 230, 50
        if side == "r":
            ax0 = LANE_X[l] + LANE_W
            bxs = ax0 + 14
            endx = bxs
        else:
            ax0 = LANE_X[l]
            bxs = ax0 - 14 - bw
            endx = bxs + bw
        by0 = cy - bh / 2
        out.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="#bf8f00" stroke-width="1" stroke-dasharray="3,3"/>' % (ax0, cy, endx, cy))
        out.append('<rect x="%.1f" y="%.1f" width="%s" height="%s" fill="#fffaf0" stroke="#bf8f00" stroke-width="1.1" stroke-dasharray="5,3" rx="3"/>' % (bxs, by0, bw, bh))
        lines = text.split("\n")
        lh = 12
        ty = cy - (len(lines) - 1) * lh / 2
        for i, ln in enumerate(lines):
            out.append('<text x="%.1f" y="%.1f" font-size="8.2" fill="#7a5b00" text-anchor="middle" dominant-baseline="middle">%s</text>' % (bxs + bw/2, ty + i*lh, ESC(ln)))

    # ── Draw nodes (on top of edges) ────────────────────────────────────
    for nid, (l, r, kind, label) in N.items():
        cx = lane_cx(l)
        cy = row_cy(r)
        col = LANE_COLOR[l]
        if kind == "start":
            out.append('<circle cx="%.1f" cy="%.1f" r="24" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2.2"/>' % (cx, cy))
            out.append(tspans(label, cx, cy, fs=9.5, fill="#1b5e20", weight="bold"))
        elif kind == "end":
            out.append('<circle cx="%.1f" cy="%.1f" r="24" fill="#ffebee" stroke="#c62828" stroke-width="3.5"/>' % (cx, cy))
            out.append(tspans(label, cx, cy, fs=9, fill="#b71c1c", weight="bold"))
        elif kind == "gw":
            gpts = "%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" % (cx, cy-GW_R, cx+GW_R, cy, cx, cy+GW_R, cx-GW_R, cy)
            out.append('<polygon points="%s" fill="#fff2cc" stroke="#bf8f00" stroke-width="1.8"/>' % gpts)
            out.append('<text x="%.1f" y="%.1f" font-size="14" font-weight="bold" fill="#bf8f00" text-anchor="middle">x</text>' % (cx, cy - GW_R - 5))
            out.append(tspans(label, cx, cy, fs=9, fill="#5b4500", weight="bold"))
        else:
            out.append('<rect x="%.1f" y="%.1f" width="%s" height="%s" rx="9" fill="#ffffff" stroke="%s" stroke-width="1.8"/>' % (cx - BOXW/2, cy - BOXH/2, BOXW, BOXH, col))
            out.append(tspans(label, cx, cy, fs=9.6, fill="#1a1a1a"))

    # ── Legend ───────────────────────────────────────────────────────────
    legend_y = TOP + HEADER_H + nrows * ROW_H + 14
    out.append('<text x="%.1f" y="%s" font-size="10" fill="#555" text-anchor="middle">Ky hieu BPMN:  O Start Event   End Event (double ring)   Task/Activity   Diamond Exclusive Gateway   -- Sequence Flow   -- Luong quay lui/retry</text>' % (TOTAL_W / 2, legend_y + 16))

    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    import os
    svg = build_svg()
    os.makedirs("diagrams", exist_ok=True)
    with open("diagrams/voucher_bpmn.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("OK diagrams/voucher_bpmn.svg")

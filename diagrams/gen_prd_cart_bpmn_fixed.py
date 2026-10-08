# -*- coding: utf-8 -*-
"""
BPMN swimlane generator — PRD Giỏ hàng (thuyttdoc/prd_cart.doc)
Dựa trên skill diagram-drawer/templates/bpmn_template, nâng cấp:
  - Routing trực giao (V / HV / VH / Z / U) tránh đè node
  - Badge mã bước S-xx trên Task -> liên kết bảng "Các bước thực hiện"
  - Text Annotation BR-xx / ERR-xx ở cột phải -> liên kết bảng BR & mã lỗi
  - Start/End ghi rõ điểm nối về sơ đồ Tổng quan (mục 5.1)
Chạy: python3 diagrams/gen_prd_cart_bpmn.py  -> diagrams/prd_cart_*.svg + .png
"""
import subprocess, textwrap, os

ESC = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Layout ──
ML, MR = 14, 12
LANE_W = 460
GAP = 16
ANNOT_W = 236
TOP = 80
HEADER_H = 40
ROW_H = 65
BOXW, BOXH, NARROW = 270, 62, 206
GW_R = 27
EV_R = 18
FS_TASK = 13.2

C_KH, C_FE, C_BE = "#1f4e78", "#2e75b6", "#7030a0"
LANE_DEF = [("KHÁCH HÀNG (CUSTOMER)", C_KH, "#eef3fb"),
            ("WEBSITE FPT.VN (FRONT-END)", C_FE, "#eef7fd"),
            ("HỆ THỐNG XỬ LÝ", C_BE, "#f6f0fb")]
LANE_X = {i: ML + i * LANE_W for i in range(3)}
ANNOT_X = ML + 3 * LANE_W + GAP
W = ML + 3 * LANE_W + 30


def cx_of(l, half):
    x = LANE_X[l]
    return x + {"c": 0.5, "l": 0.26, "r": 0.74}[half] * LANE_W


def cy_of(r):
    return TOP + HEADER_H + 8 + r * ROW_H + ROW_H / 2


def tspans(label, cx, cy, fs, fill="#1a1a1a", weight="normal", anchor="middle"):
    lines = label.split("\n")
    lh = fs * 1.22
    y0 = cy - (len(lines) - 1) * lh / 2 + fs * 0.36
    s = (f'<text x="{cx:.1f}" y="{y0:.1f}" font-size="{fs}" fill="{fill}" '
         f'font-weight="{weight}" text-anchor="{anchor}">')
    for j, ln in enumerate(lines):
        s += f'<tspan x="{cx:.1f}" dy="{0 if j == 0 else lh:.1f}">{ESC(ln)}</tspan>'
    return s + "</text>"


def build(key, title, subtitle, lane2, N, E, ANNOT, nrows):
    lanes = [LANE_DEF[0], LANE_DEF[1], (lane2, C_BE, "#f6f0fb")]
    lane_bot = cy_of(nrows - 1) + ROW_H / 2 + 6
    H = lane_bot + 58
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H:.0f}" '
             f'viewBox="0 0 {W} {H:.0f}" font-family="Arial, Helvetica, sans-serif">')
    o.append(f'<rect width="{W}" height="{H:.0f}" fill="#ffffff"/>')
    o.append('<defs>'
             '<marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
             '<path d="M0,0 L9,4 L0,8 Z" fill="#3a3a3a"/></marker>'
             '<marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse">'
             '<path d="M0,0 L9,4 L0,8 Z" fill="#c62828"/></marker></defs>')
    o.append(f'<text x="{W/2}" y="32" font-size="19" font-weight="bold" fill="#1f4e78" '
             f'text-anchor="middle">{ESC(title)}</text>')
    o.append(f'<text x="{W/2}" y="56" font-size="12" fill="#595959" font-style="italic" '
             f'text-anchor="middle">{ESC(subtitle)}</text>')

    # lanes
    for i, (name, c, fill) in enumerate(lanes):
        x = LANE_X[i]
        o.append(f'<rect x="{x}" y="{TOP}" width="{LANE_W}" height="{lane_bot-TOP:.0f}" '
                 f'fill="{fill}" stroke="{c}" stroke-width="1.3"/>')
        o.append(f'<rect x="{x}" y="{TOP}" width="{LANE_W}" height="{HEADER_H}" fill="{c}"/>')
        o.append(f'<text x="{x+LANE_W/2}" y="{TOP+HEADER_H/2+4.5}" font-size="13" font-weight="bold" '
                 f'fill="#fff" text-anchor="middle">{ESC(name)}</text>')
    # annotation column header
    

    def info(nid):
        n = N[nid]
        l, r, half, kind, label = n[:5]
        opt = n[5] if len(n) > 5 else {}
        return cx_of(l, half), cy_of(r), kind, label, l, half, opt

    def size(nid):
        cx, cy, kind, label, l, half, opt = info(nid)
        if kind in ("gw", "pgw"):
            return GW_R * 2, GW_R * 2
        if kind in ("start", "end"):
            return EV_R * 2, EV_R * 2
        return (BOXW if half == "c" else NARROW), BOXH

    def anc(nid, side):
        cx, cy, *_ = info(nid)
        w, h = size(nid)
        return {"t": (cx, cy - h / 2), "b": (cx, cy + h / 2),
                "l": (cx - w / 2, cy), "r": (cx + w / 2, cy)}[side]

    def label_at(x, y, text, anchor, color):
        if not text:
            return
        wl = len(text) * 6.4 + 8
        rx = x - wl / 2 if anchor == "middle" else (x - 4 if anchor == "start" else x - wl + 4)
        o.append(f'<rect x="{rx:.1f}" y="{y-11:.1f}" width="{wl:.1f}" height="15" fill="#ffffff" opacity="0.95" rx="2"/>')
        o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="11.8" font-weight="bold" fill="{color}" '
                 f'text-anchor="{anchor}">{ESC(text)}</text>')

    # edges
    labels = []
    for e in E:
        a, b, lbl = e[0], e[1], e[2]
        route = e[3] if len(e) > 3 else "auto"
        style = e[4] if len(e) > 4 else "seq"
        color = "#c62828" if style == "back" else "#3a3a3a"
        mk = "ar" if style == "back" else "a"
        dash = ' stroke-dasharray="7,4"' if style == "back" else ""
        ax_, ay_, *_ = info(a)
        bx_, by_, *_ = info(b)
        if route == "auto":
            if abs(ax_ - bx_) < 2 and by_ > ay_:
                route = "V"
            elif abs(ay_ - by_) < 2:
                route = "H"
            else:
                route = "HV"
        if route == "V":
            p0, p1 = anc(a, "b"), anc(b, "t")
            pts = [p0, p1]
            lab = (p0[0] + 7, p0[1] + 15, "start")
        elif route == "H":
            s1, s2 = ("r", "l") if bx_ > ax_ else ("l", "r")
            p0, p1 = anc(a, s1), anc(b, s2)
            pts = [p0, p1]
            lab = ((p0[0] + p1[0]) / 2, p0[1] - 6, "middle")
        elif route == "HV":
            s1 = "r" if bx_ > ax_ else "l"
            p0 = anc(a, s1); p1 = anc(b, "t")
            pts = [p0, (p1[0], p0[1]), p1]
            lab = (p0[0] + (10 if s1 == "r" else -10), p0[1] - 6, "start" if s1 == "r" else "end")
        elif route == "VH":
            s2 = "l" if ax_ < bx_ else "r"
            p0 = anc(a, "b"); p1 = anc(b, s2)
            pts = [p0, (p0[0], p1[1]), p1]
            lab = (p0[0] + 7, p0[1] + 15, "start")
        elif route == "Z":
            p0 = anc(a, "b"); p1 = anc(b, "t")
            my = p0[1] + (p1[1] - p0[1]) * 0.45
            pts = [p0, (p0[0], my), (p1[0], my), p1]
            lab = (p0[0] + 7, p0[1] + 15, "start")
        else:  # ("U", side, xoff_lane, dx)
            _, side, lane, dx = route
            xx = LANE_X[lane] + dx
            p0 = anc(a, side); p1 = anc(b, side)
            pts = [p0, (xx, p0[1]), (xx, p1[1]), p1]
            if style == "back":
                lab = ("rot", xx, (p0[1] + p1[1]) / 2)
            else:
                lab = (p0[0] + (10 if side == "r" else -10), p0[1] - 6, "start" if side == "r" else "end")
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        o.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6"{dash} marker-end="url(#{mk})"/>')
        labels.append((lab, lbl, color))

    # nodes
    for nid in N:
        cx, cy, kind, label, l, half, opt = info(nid)
        col = [C_KH, C_FE, C_BE][l]
        if kind in ("start", "end"):
            if kind == "start":
                o.append(f'<circle cx="{cx}" cy="{cy}" r="{EV_R}" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>')
                fc = "#1b5e20"
            else:
                o.append(f'<circle cx="{cx}" cy="{cy}" r="{EV_R}" fill="#ffebee" stroke="#c62828" stroke-width="4"/>')
                fc = "#b71c1c"
            lp = opt.get("lp", "r")
            if lp == "r":
                o.append(tspans(label, cx + EV_R + 8, cy, 12, fc, "bold", "start"))
            elif lp == "l":
                o.append(tspans(label, cx - EV_R - 8, cy, 12, fc, "bold", "end"))
            else:
                o.append(tspans(label, cx, cy + EV_R + 20, 12, fc, "bold"))
        elif kind in ("gw", "pgw"):
            r = GW_R
            o.append(f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" '
                     f'fill="#fff2cc" stroke="#bf8f00" stroke-width="2"/>')
            if kind == "gw":
                k = 8
                o.append(f'<path d="M{cx-k},{cy-k} L{cx+k},{cy+k} M{cx+k},{cy-k} L{cx-k},{cy+k}" '
                         f'stroke="#7a5b00" stroke-width="3.2" stroke-linecap="round"/>')
            else:
                k = 11
                o.append(f'<path d="M{cx-k},{cy} L{cx+k},{cy} M{cx},{cy-k} L{cx},{cy+k}" '
                         f'stroke="#7a5b00" stroke-width="3.2" stroke-linecap="round"/>')
            if label:
                lp = opt.get("lp", "tr")
                nl = label.count("\n") + 1
                ly = cy - r / 2 - 4 - (nl - 1) * 7.5
                if lp == "tr":
                    o.append(tspans(label, cx + r * 0.7, ly, 12, "#5b4500", "bold", "start"))
                else:
                    o.append(tspans(label, cx - r * 0.7, ly, 12, "#5b4500", "bold", "end"))
        else:
            w = BOXW if half == "c" else NARROW
            o.append(f'<rect x="{cx-w/2}" y="{cy-BOXH/2}" width="{w}" height="{BOXH}" rx="9" '
                     f'fill="#ffffff" stroke="{col}" stroke-width="1.8"/>')
            o.append(tspans(label, cx, cy + (2 if opt.get("step") else 0), FS_TASK))
            st = opt.get("step")
            if st:
                bw = len(st) * 7 + 10
                bx = cx - w / 2 + 6
                by = cy - BOXH / 2 - 8
                o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="15" rx="7" fill="{col}"/>')
                o.append(f'<text x="{bx+bw/2}" y="{by+11}" font-size="10.5" font-weight="bold" '
                         f'fill="#fff" text-anchor="middle">{ESC(st)}</text>')

    # edge labels on top
    for lab, txt, color in labels:
        if not txt:
            continue
        if lab[0] == "rot":
            _, xx, yy = lab
            wl = len(txt) * 6.3 + 8
            o.append(f'<g transform="rotate(-90 {xx:.1f} {yy:.1f})">'
                     f'<rect x="{xx-wl/2:.1f}" y="{yy-9:.1f}" width="{wl:.1f}" height="15" fill="#fff" opacity="0.95" rx="2"/>'
                     f'<text x="{xx:.1f}" y="{yy+2.5:.1f}" font-size="11.3" font-weight="bold" fill="{color}" '
                     f'text-anchor="middle">{ESC(txt)}</text></g>')
        else:
            label_at(lab[0], lab[1], txt, lab[2], color)

    # legend
    ly = H - 26
    items_l = [("start", "Start Event"), ("end", "End Event"), ("task", "Task"),
               ("step", "Mã bước (S-xx)"), ("gw", "Exclusive Gateway"), ("pgw", "Parallel Gateway"),
               ("seq", "Sequence Flow"), ("back", "Luồng quay lại / lỗi"), ("ann", "Text Annotation")]
    x = ML + 6
    o.append(f'<line x1="{ML}" y1="{ly-20}" x2="{W-MR}" y2="{ly-20}" stroke="#d0d0d0"/>')
    for k, t in items_l:
        if k == "start":
            o.append(f'<circle cx="{x+8}" cy="{ly}" r="8" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.6"/>'); x += 22
        elif k == "end":
            o.append(f'<circle cx="{x+8}" cy="{ly}" r="8" fill="#ffebee" stroke="#c62828" stroke-width="3"/>'); x += 22
        elif k == "task":
            o.append(f'<rect x="{x}" y="{ly-8}" width="26" height="16" rx="4" fill="#fff" stroke="#2e75b6" stroke-width="1.5"/>'); x += 32
        elif k == "step":
            o.append(f'<rect x="{x}" y="{ly-7}" width="30" height="14" rx="7" fill="#2e75b6"/>'
                     f'<text x="{x+15}" y="{ly+4}" font-size="9" font-weight="bold" fill="#fff" text-anchor="middle">S-01</text>'); x += 36
        elif k in ("gw", "pgw"):
            o.append(f'<polygon points="{x+9},{ly-9} {x+18},{ly} {x+9},{ly+9} {x},{ly}" fill="#fff2cc" stroke="#bf8f00" stroke-width="1.5"/>')
            sym = "×" if k == "gw" else "+"
            o.append(f'<text x="{x+9}" y="{ly+4.5}" font-size="12" font-weight="bold" fill="#7a5b00" text-anchor="middle">{sym}</text>'); x += 24
        elif k == "seq":
            o.append(f'<path d="M{x},{ly} L{x+26},{ly}" stroke="#3a3a3a" stroke-width="1.6" marker-end="url(#a)"/>'); x += 34
        elif k == "back":
            o.append(f'<path d="M{x},{ly} L{x+26},{ly}" stroke="#c62828" stroke-width="1.6" stroke-dasharray="5,3" marker-end="url(#ar)"/>'); x += 34
        else:
            o.append(f'<path d="M{x+8},{ly-8} L{x},{ly-8} L{x},{ly+8} L{x+8},{ly+8}" fill="none" stroke="#bf8f00" stroke-width="1.6"/>'); x += 14
        o.append(f'<text x="{x}" y="{ly+4}" font-size="11.5" fill="#444">{ESC(t)}</text>')
        x += len(t) * 6.3 + 16
    o.append("</svg>")

    svg = os.path.join(OUT_DIR, f"prd_cart_{key}_bpmn.svg")
    png = os.path.join(OUT_DIR, f"prd_cart_{key}_bpmn.png")
    with open(svg, "w", encoding="utf-8") as f:
        f.write("\n".join(o))
    subprocess.run(["rsvg-convert", "-w", str(W * 2), svg, "-o", png], check=True)
    print(f"OK {key}: {W}x{H:.0f}")


U_KH = lambda dx=40: ("U", "l", 0, dx)     # luồng quay lại theo mép trái lane Khách hàng
END_LINK = "Kết thúc\n(→ Tổng quan S-06)"
START_LINK = "Bắt đầu\n(Tổng quan S-01)"

# ═════════════ 0. TỔNG QUAN — mục 5.1 / 5.2 ═════════════
build("overview",
      "SƠ ĐỒ BPMN TỔNG QUAN — LUỒNG GIỎ HÀNG & CHECKOUT FPT.VN",
      "Liên kết: Bảng 5.2 (S-01 → S-06) · Rẽ nhánh tới sơ đồ chi tiết FR01 → FR08 (mục 8)",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", "Khách truy cập FPT.vn\n(Vãng lai / Mua mới)"),
          "k1": (0, 1, "c", "task", "Chọn SP tại trang chi tiết\n→ 'Thêm vào giỏ'", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu giỏ hàng\n(Đồng bộ hệ thống)", {"step": "S-01"}),
          "k2": (0, 3, "c", "task", "Truy cập trang /cart", {"step": "S-02"}),
          "f1": (1, 4, "c", "task", "Phân tích thành phần\ngiỏ hàng (SP/Dịch vụ)", {"step": "S-02"}),
          "b2": (2, 4, "c", "task", "Hệ thống xác nhận\nthông tin & giá tạm tính", {"step": "S-02"}),
          "g1": (1, 5, "c", "gw", "count(SKU) ≥ 1 ?", {"lp": "tl"}),
          "f2": (1, 6, "l", "task", "Ẩn Form Địa chỉ\n& Lịch KTV\n→ FR02 · FR06 · FR07", {"step": "S-03"}),
          "f3": (1, 6, "r", "task", "Render Form\nĐịa chỉ nhận hàng\n→ FR01·03·04·05·08", {"step": "S-03"}),
          "k3": (0, 7, "c", "task", "Nhập SĐT (bắt buộc), Họ tên,\nĐịa chỉ (nếu có SKU)", {"step": "S-04"}),
          "g2": (1, 8, "c", "gw", "Form hợp lệ?"),
          "k4": (0, 9, "c", "task", "Chọn PTTT VNPAY / COD\n(giỏ Mix + COD → cảnh báo)", {"step": "S-04"}),
          "f4": (1, 10, "c", "task", "Bấm 'Đặt hàng'\n→ POST /order/submit", {"step": "S-05"}),
          "b3": (2, 11, "c", "task", "Hệ thống tạo đơn hàng\n& khởi tạo thanh toán", {"step": "S-05"}),
          "g3": (2, 12, "c", "gw", "PTTT ?"),
          "b4": (2, 13, "l", "task", "VNPAY thành công\n→ Instant SA active\n+ KTV book lịch SKU", {"step": "S-06"}),
          "b5": (2, 13, "r", "task", "COD → Pending SA\nKTV thu tiền xong\nmới active SA", {"step": "S-06"}),
          "g4": (2, 14, "c", "gw", ""),
          "f5": (1, 15, "c", "task", "Trang Thank You\n+ gửi SMS xác nhận đơn", {"step": "S-06"}),
          "end": (0, 16, "c", "end", "Hoàn tất\nđơn hàng"),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "k2", ""), ("k2", "f1", ""),
          ("f1", "b2", "", "H"), ("b2", "g1", "", "Z"),
          ("g1", "f2", "Không (100% SA)"), ("g1", "f3", "Có (SKU / Mix)"),
          ("f2", "k3", ""), ("f3", "k3", "", "VH"),
          ("k3", "g2", ""), ("g2", "k4", "Hợp lệ", "VH"),
          ("g2", "k3", "Không → báo lỗi inline", U_KH(), "back"),
          ("k4", "f4", ""), ("f4", "b3", ""), ("b3", "g3", ""),
          ("g3", "b4", "VNPAY"), ("g3", "b5", "COD"),
          ("b4", "g4", "", "VH"), ("b5", "g4", "", "VH"),
          ("g4", "f5", "", "VH"), ("f5", "end", ""),
      ],
      [
          ("Dynamic Checkout UI: count(SKU)=0 → giỏ 100% SA (ẩn địa chỉ); count(SKU)≥1 → giỏ SKU / Mix (hiện địa chỉ).", "g1"),
          ("Validate SĐT Regex VN, Họ tên, địa chỉ 4 cấp (nếu có SKU). Lỗi hiển thị inline, chặn Đặt hàng.", "g2"),
          ("SPF nhận payload kèm SA_Activation_Flag: INSTANT (VNPAY) / PENDING (COD).", "b3"),
          ("Instant SA kích hoạt ngay sau VNPAY; Pending SA chỉ kích hoạt khi KTV thu tiền COD.", "g3"),
      ],
      17)

# ═════════════ FR01 — CAMERA ═════════════
build("fr01",
      "SƠ ĐỒ BPMN — FR01 · LUỒNG GIỎ HÀNG CAMERA (LẺ · COMBO CLOUD · MIX CAMERA)",
      "Liên kết: 5.1 Tổng quan (S-01 → S-06) · 8.01.1 Business Rules · 8.01.3 Các bước · 8.01.5 Mã lỗi ERR-CAM",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn Camera Indoor/Outdoor\n+ Gói Cloud (Không/6T/12T)\n→ 'Thêm vào giỏ'", {"step": "S-01"}),
          "g1": (1, 2, "c", "gw", "Số lượng ≤ 10?"),
          "b1": (2, 3, "c", "task", "Lưu thông tin giỏ hàng", {"step": "S-01"}),
          "f1": (1, 4, "c", "task", "Vào giỏ hàng → Hệ thống\nnhận diện có SP vật lý", {"step": "S-02"}),
          "b2": (2, 5, "c", "task", "Tự động cập nhật giá\nkhi thay đổi gói Cloud"),
          "f2": (1, 6, "c", "task", "Render Form Địa chỉ nhận hàng\n(KHÔNG Lịch KTV) + Sub-total", {"step": "S-02"}),
          "k2": (0, 7, "c", "task", "Nhập SĐT, Họ tên,\nđịa chỉ đủ 4 cấp", {"step": "S-03"}),
          "g2": (1, 8, "c", "gw", "Địa chỉ hợp lệ?"),
          "k3": (0, 9, "c", "task", "Chọn PTTT VNPAY / COD\n→ 'Đặt hàng'", {"step": "S-04"}),
          "b3": (2, 10, "c", "task", "Tạo đơn hàng (Tách tự động\nThiết bị & Dịch vụ)", {"step": "S-04"}),
          "b4": (2, 11, "c", "task", "Chuyển đơn tới\nKTV giao lắp", {"step": "S-04"}),
          "end": (0, 12, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "g1", ""),
          ("g1", "b1", "Có"), ("g1", "k1", "Không · ERR-CAM-01", U_KH(), "back"),
          ("b1", "f1", "", "VH"), ("f1", "b2", "Đổi gói Cloud"), ("b2", "f2", "", "VH"),
          ("f2", "k2", ""), ("k2", "g2", ""),
          ("g2", "k3", "Hợp lệ", "VH"), ("g2", "k2", "Không · ERR-CAM-02", U_KH(), "back"),
          ("k3", "b3", ""), ("b3", "b4", ""), ("b4", "end", ""),
      ],
      [
          ("BR-04: Tối đa 10 Camera/mẫu/đơn. ERR-CAM-01: Toast vượt 10, disable nút (+).", "g1"),
          ("BR-02: Đổi gói Cloud → Get_Price reload Sub-total. ERR-CAM-03: lỗi API → mặc định Cloud 6T.", "b2"),
          ("BR-01: Có SKU Camera → bắt buộc Form Địa chỉ, KHÔNG hiển thị Lịch KTV.", "f2"),
          ("ERR-CAM-02: Bỏ trống địa chỉ → lỗi inline, disable nút Thanh toán.", "g2"),
          ("BR-03: Tự động tách 1 Camera Combo thành 1 dòng SKU + 1 dòng SA Cloud trong payload SPF.", "b3"),
      ],
      13)

# ═════════════ FR02 — FPT PLAY ═════════════
build("fr02",
      "SƠ ĐỒ BPMN — FR02 · LUỒNG GIỎ HÀNG FPT PLAY (DỊCH VỤ SA)",
      "Liên kết: 5.1 Tổng quan (nhánh 100% SA) · 8.02.1 Business Rules · 8.02.3 Các bước · 8.02.5 Mã lỗi ERR-FPL",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn gói FPT Play\n(iZi / VIP / MAX) → 'Thêm vào giỏ'", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu gói dịch vụ vào giỏ", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "count(SKU) == 0 → Ẩn Form\nĐịa chỉ & Lịch KTV khỏi DOM", {"step": "S-02"}),
          "k2": (0, 4, "c", "task", "Nhập SĐT chính chủ\n& Họ tên", {"step": "S-03"}),
          "g1": (1, 5, "c", "gw", "SĐT đúng Regex?"),
          "b2": (2, 6, "c", "task", "Kiểm tra SĐT đã có tài khoản\n& trùng gói cùng loại"),
          "g2": (2, 7, "c", "gw", "Đã có TK /\ntrùng gói?"),
          "k3": (0, 8, "c", "task", "Thanh toán online VNPAY", {"step": "S-04"}),
          "g3": (2, 9, "c", "gw", "Thanh toán\nthành công?"),
          "b3": (2, 10, "c", "task", "Kích hoạt tức thì FPT Play\n& Gửi SMS Tài khoản", {"step": "S-04"}),
          "f2": (1, 11, "c", "task", "Trang Thank You\nxác nhận đơn hàng"),
          "end": (0, 12, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "g1", ""), ("g1", "b2", "Đúng"),
          ("g1", "k2", "Sai · ERR-FPL-02", U_KH(16), "back"),
          ("b2", "g2", ""), ("g2", "k3", "Không", "VH"),
          ("g2", "k2", "Có · ERR-FPL-01", U_KH(34), "back"),
          ("k3", "g3", ""), ("g3", "b3", "Có"),
          ("g3", "k3", "Không → thử lại", U_KH(16), "back"),
          ("b3", "f2", "", "VH"), ("f2", "end", ""),
      ],
      [
          ("BR-01: Giỏ 100% dịch vụ số (count(SKU)=0) → ẩn 100% Form Địa chỉ & Lịch KTV.", "f1"),
          ("BR-02: SĐT là Key Account kích hoạt. ERR-FPL-02: sai Regex → lỗi inline, disable Thanh toán.", "g1"),
          ("BR-03: 1 SĐT chỉ mua 01 gói cùng loại/đơn. ERR-FPL-01: SĐT đã có TK → gợi ý nâng cấp / SĐT khác.", "g2"),
          ("BR-04: VNPAY thành công → Instant SA + SMS. ERR-FPL-03: lỗi server → job retry tự động 15p.", "b3"),
      ],
      13)

# ═════════════ FR03 — AX8000C ═════════════
build("fr03",
      "SƠ ĐỒ BPMN — FR03 · LUỒNG GIỎ HÀNG ACCESS POINT AX8000C (THIẾT BỊ SKU)",
      "Liên kết: 5.1 Tổng quan (nhánh có SKU) · 8.03.1 Business Rules · 8.03.3 Các bước · 8.03.5 Mã lỗi ERR-AX",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn AX8000C + số lượng\n→ 'Thêm vào giỏ'", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu sản phẩm vào giỏ", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "Render Form Địa chỉ giao hàng\n(KHÔNG lịch hẹn thi công)"),
          "k2": (0, 4, "c", "task", "Nhập Tỉnh/Thành, Quận/Huyện,\nPhường/Xã, Số nhà", {"step": "S-02"}),
          "b2": (2, 5, "c", "task", "Kiểm tra tồn kho\ntại khu vực Khách hàng", {"step": "S-02"}),
          "g1": (2, 6, "c", "gw", "Còn hàng &\ntrong vùng phủ?"),
          "k3": (0, 7, "c", "task", "Chọn Tự lắp (miễn phí) hoặc\n'Hỗ trợ KTV lắp đặt' (+50.000đ)", {"step": "S-03"}),
          "f2": (1, 8, "c", "task", "Cập nhật tổng tiền\n(+ line 'Phí hỗ trợ lắp đặt')", {"step": "S-03"}),
          "k4": (0, 9, "c", "task", "Chọn PTTT → 'Đặt hàng'", {"step": "S-04"}),
          "b3": (2, 10, "c", "task", "Tạo đơn hàng &\nchuyển yêu cầu giao vận", {"step": "S-04"}),
          "end": (0, 11, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "b2", ""), ("b2", "g1", ""),
          ("g1", "k3", "Đạt", "VH"),
          ("g1", "k2", "Không · ERR-AX-01/02", U_KH(), "back"),
          ("k3", "f2", ""), ("f2", "k4", ""), ("k4", "b3", ""), ("b3", "end", ""),
      ],
      [
          ("BR-01: AX8000C là SKU phần cứng → bắt buộc địa chỉ giao hàng, không có lịch hẹn thi công.", "f1"),
          ("BR-03: Tự động gửi Quận/Huyện sang API FCP kiểm tra tồn kho kho gần nhất.", "b2"),
          ("ERR-AX-01: Hết hàng khu vực → gợi ý nhận thông báo. ERR-AX-02: ngoài vùng phủ kho → yêu cầu đổi địa chỉ.", "g1"),
          ("BR-02: Tự lắp (miễn phí) hoặc tích 'Hỗ trợ KTV lắp đặt' (+50.000đ phí dịch vụ).", "f2"),
      ],
      12)

# ═════════════ FR04 — SMART HOME PLUG ═════════════
build("fr04",
      "SƠ ĐỒ BPMN — FR04 · LUỒNG GIỎ HÀNG Ổ CẮM THÔNG MINH FPT SMART HOME (IoT SKU)",
      "Liên kết: 5.1 Tổng quan (nhánh có SKU) · 8.04.1 Business Rules · 8.04.3 Các bước · 8.04.5 Mã lỗi ERR-SH",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn Ổ cắm Smart Home\n+ số lượng → 'Thêm giỏ'", {"step": "S-01"}),
          "g1": (1, 2, "c", "gw", "Số lượng ≤ 5?"),
          "b1": (2, 3, "c", "task", "Kiểm tra tồn kho &\nlưu item IoT vào giỏ", {"step": "S-01"}),
          "g2": (2, 4, "c", "gw", "Còn hàng?"),
          "f1": (1, 5, "c", "task", "Render Form Địa chỉ giao hàng\n(KHÔNG lịch hẹn giao / lắp)"),
          "k2": (0, 6, "c", "task", "Nhập Tỉnh/Thành, Quận/Huyện,\nPhường/Xã, Số nhà", {"step": "S-02"}),
          "g3": (1, 7, "c", "gw", "Địa chỉ hợp lệ?"),
          "k3": (0, 8, "c", "task", "Chọn PTTT VNPAY / COD\n→ 'Đặt hàng'", {"step": "S-03"}),
          "b2": (2, 9, "c", "task", "Tạo đơn hàng &\nphân loại sản phẩm IoT", {"step": "S-03"}),
          "b3": (2, 10, "c", "task", "Tạo phiếu giao hàng IoT\n(Logistics / KTV chuẩn bị vật tư)", {"step": "S-03"}),
          "end": (0, 11, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "g1", ""),
          ("g1", "b1", "Có"), ("g1", "k1", "Không · ERR-SH-01", U_KH(16), "back"),
          ("b1", "g2", ""), ("g2", "f1", "Có", "VH"),
          ("g2", "k1", "Hết hàng · ERR-SH-02", U_KH(34), "back"),
          ("f1", "k2", ""), ("k2", "g3", ""),
          ("g3", "k3", "Hợp lệ", "VH"), ("g3", "k2", "Không", U_KH(16), "back"),
          ("k3", "b2", ""), ("b2", "b3", ""), ("b3", "end", ""),
      ],
      [
          ("BR-02: Tối đa 5 ổ cắm/đơn. ERR-SH-01: vượt 5 → lỗi inline, disable nút tăng số lượng.", "g1"),
          ("ERR-SH-02: Tạm hết hàng ổ cắm IoT → Toast, gợi ý chọn sản phẩm khác.", "g2"),
          ("BR-01: Bắt buộc địa chỉ giao hàng; KHÔNG hiển thị bước chọn lịch hẹn giao / lắp đặt.", "f1"),
          ("BR-03: Tự động kẹp tag IoT_SmartPlug để giao vận / KTV chuẩn bị vật tư.", "b2"),
      ],
      12)

# ═════════════ FR05 — SMART TV SAMSUNG ═════════════
build("fr05",
      "SƠ ĐỒ BPMN — FR05 · LUỒNG GIỎ HÀNG SMART TV SAMSUNG (CỒNG KỀNH · RÀNG BUỘC ĐỊA LÝ)",
      "Liên kết: 5.1 Tổng quan (nhánh có SKU) · 8.05.1 Business Rules · 8.05.3 Các bước · 8.05.5 Mã lỗi ERR-TV",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn mẫu / kích thước TV\n→ 'Thêm vào giỏ'", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu sản phẩm vào giỏ", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "Render Form Địa chỉ giao hàng\n(KHÔNG lịch hẹn)"),
          "k2": (0, 4, "c", "task", "Chọn Tỉnh → Quận/Huyện\n→ Phường/Xã", {"step": "S-02"}),
          "f2": (1, 5, "c", "task", "Hệ thống tự động kiểm tra\nvùng phủ giao hàng cồng kềnh", {"step": "S-02"}),
          "b2": (2, 6, "c", "task", "Xác nhận khả năng\ngiao hàng tại địa chỉ", {"step": "S-03"}),
          "g1": (1, 7, "c", "gw", "is_supported\n== true?"),
          "k3": (0, 8, "c", "task", "Chọn PTTT → 'Đặt hàng'", {"step": "S-04"}),
          "b3": (2, 9, "c", "task", "Tạo đơn hàng &\nvận đơn giao hàng cồng kềnh", {"step": "S-04"}),
          "end": (0, 10, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "f2", ""), ("f2", "b2", ""), ("b2", "g1", "", "VH"),
          ("g1", "k3", "True", "VH"),
          ("g1", "k2", "False · Popup ERR-TV-01", U_KH(), "back"),
          ("k3", "b3", ""), ("b3", "end", ""),
      ],
      [
          ("BR-01: Chọn xong Phường/Xã → gọi GET /location/check_oversized xác thực vùng phủ.", "f2"),
          ("ERR-TV-02: Lỗi API Geolocation → Toast lỗi, cho phép Khách thử lại.", "b2"),
          ("BR-02: is_supported = false → Popup từ chối, disable 'Đặt hàng' (CTA Đổi địa chỉ / Xóa TV). BR-03: giỏ Mix TV + Camera → xóa TV mới thanh toán tiếp.", "g1"),
      ],
      11)

# ═════════════ FR06 — ULTRAFAST / HYPERFAST ═════════════
build("fr06",
      "SƠ ĐỒ BPMN — FR06 · LUỒNG GIỎ HÀNG ULTRAFAST / HYPERFAST (DỊCH VỤ GIA TĂNG SA)",
      "Liên kết: 5.1 Tổng quan (nhánh 100% SA) · 8.06.1 Business Rules · 8.06.3 Các bước · 8.06.5 Mã lỗi ERR-UF",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Chọn gói UltraFast\n(1T / 6T / 12T) → 'Thêm giỏ'", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu gói dịch vụ vào giỏ", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "count(SKU) == 0\n→ Ẩn 100% Form Địa chỉ"),
          "k2": (0, 4, "c", "task", "Nhập SĐT đường truyền\nInternet FPT", {"step": "S-02"}),
          "b2": (2, 5, "c", "task", "Kiểm tra điều kiện SĐT\n(Đã có Internet FPT?)", {"step": "S-02"}),
          "g1": (2, 6, "c", "gw", "SĐT hợp lệ &\nchưa có gói?"),
          "k3": (0, 7, "c", "task", "Thanh toán online VNPAY", {"step": "S-03"}),
          "g2": (2, 8, "c", "gw", "Thanh toán\nthành công?"),
          "b3": (2, 9, "c", "task", "Kích hoạt tự động\ngói UltraFast", {"step": "S-03"}),
          "f2": (1, 10, "c", "task", "Trang Thank You\nxác nhận đơn hàng"),
          "end": (0, 11, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "b2", ""), ("b2", "g1", ""),
          ("g1", "k3", "Có", "VH"),
          ("g1", "k2", "Không · ERR-UF-01/02", U_KH(), "back"),
          ("k3", "g2", ""), ("g2", "b3", "Có"),
          ("g2", "k3", "Không → thử lại", U_KH(), "back"),
          ("b3", "f2", "", "VH"), ("f2", "end", ""),
      ],
      [
          ("BR-01: Giỏ chỉ có UltraFast → ẩn 100% Form Địa chỉ giao hàng.", "f1"),
          ("BR-02: SĐT phải là SĐT đăng ký đường truyền Internet FPT hiện hữu.", "b2"),
          ("ERR-UF-01: SĐT không dùng Internet FPT → gợi ý đăng ký. ERR-UF-02: đã có gói → disable Thanh toán.", "g1"),
          ("BR-03: VNPAY thành công → gọi API Activate_Booster tới Radius Server mở rộng băng thông.", "b3"),
      ],
      12)

# ═════════════ FR07 — SA + SA ═════════════
build("fr07",
      "SƠ ĐỒ BPMN — FR07 · LUỒNG GIỎ HÀNG GỘP NHIỀU DỊCH VỤ SA (FPT PLAY + ULTRAFAST)",
      "Liên kết: 5.1 Tổng quan (nhánh 100% SA) · 8.07.1 Business Rules · 8.07.3 Các bước · 8.07.5 Mã lỗi ERR-SASA",
      "HỆ THỐNG (XỬ LÝ ĐƠN & DỊCH VỤ)",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Thêm FPT Play & UltraFast\nvào giỏ hàng", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu thông tin các dịch vụ", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "count(SKU) == 0 → Ẩn Form\nĐịa chỉ, hiện Form SĐT", {"step": "S-02"}),
          "k2": (0, 4, "c", "task", "Nhập 01 SĐT đại diện\n(Key Account)", {"step": "S-02"}),
          "g1": (1, 5, "c", "gw", "SĐT hợp lệ?"),
          "k3": (0, 6, "c", "task", "Thanh toán online VNPAY", {"step": "S-03"}),
          "b2": (2, 7, "c", "task", "Hệ thống xử lý kích hoạt\nđộc lập từng dịch vụ", {"step": "S-03"}),
          "p1": (2, 8, "c", "pgw", ""),
          "b3": (2, 9, "l", "task", "Kích hoạt\nFPT Play"),
          "b4": (2, 9, "r", "task", "Kích hoạt\nUltraFast"),
          "p2": (2, 10, "c", "pgw", ""),
          "g2": (2, 11, "c", "gw", "Cả 2 SA\nthành công?"),
          "f2": (1, 12, "l", "task", "Thank You\n+ SMS kích hoạt"),
          "f3": (1, 12, "r", "task", "Cảnh báo 1 SA lỗi\n+ tạo ticket KT"),
          "end": (0, 13, "c", "end", END_LINK),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "g1", ""), ("g1", "k3", "Hợp lệ", "VH"),
          ("g1", "k2", "Không", U_KH(), "back"),
          ("k3", "b2", ""), ("b2", "p1", ""),
          ("p1", "b3", ""), ("p1", "b4", ""),
          ("b3", "p2", "", "VH"), ("b4", "p2", "", "VH"),
          ("p2", "g2", ""), ("g2", "f2", "Có"), ("g2", "f3", "Không", "VH"),
          ("f2", "end", ""), ("f3", "end", "", "VH"),
      ],
      [
          ("BR-01: Giỏ SA + SA (count(SKU)=0) → ẩn 100% Form Địa chỉ giao hàng.", "f1"),
          ("BR-02: Dùng 01 SĐT duy nhất làm Key kích hoạt cho tất cả gói SA trong giỏ.", "g1"),
          ("BR-03: Gửi 2 payload kích hoạt riêng biệt; 1 bên lỗi, bên còn lại vẫn hoạt động bình thường.", "p1"),
          ("ERR-SASA-01: 1 trong 2 SA lỗi → cảnh báo 'hỗ trợ trong 15p' + tự động tạo ticket kỹ thuật.", "g2"),
      ],
      14)

# ═════════════ FR08 — MIX SKU + SA ═════════════
build("fr08",
      "SƠ ĐỒ BPMN — FR08 · LUỒNG GIỎ HÀNG GỘP HỖN HỢP THIẾT BỊ + DỊCH VỤ (SKU + SA)",
      "Liên kết: 5.1 Tổng quan (nhánh Mix) · 8.08.1 Business Rules · 8.08.3 Các bước · 8.08.5 Mã lỗi ERR-MIX",
      "HỆ THỐNG & VẬN HÀNH",
      {
          "start": (0, 0, "c", "start", START_LINK),
          "k1": (0, 1, "c", "task", "Thêm Camera (SKU)\n+ FPT Play (SA) vào giỏ", {"step": "S-01"}),
          "b1": (2, 2, "c", "task", "Lưu thông tin giỏ hàng", {"step": "S-01"}),
          "f1": (1, 3, "c", "task", "count(SKU) ≥ 1 → Hiện Form\nĐịa chỉ (KHÔNG Lịch KTV)"),
          "k2": (0, 4, "c", "task", "Nhập địa chỉ nhận hàng\n→ Chọn PTTT", {"step": "S-02"}),
          "g1": (1, 5, "c", "gw", "PTTT ?", {"lp": "tl"}),
          "f2": (1, 6, "c", "task", "Bung Alert vàng: SA chỉ kích\nhoạt sau khi KTV thu tiền", {"step": "S-02"}),
          "f3": (1, 7, "c", "task", "'Đặt hàng' → Gửi yêu cầu\ntới hệ thống", {"step": "S-03"}),
          "b2": (2, 8, "c", "task", "Tạo đơn hàng &\nđiều phối dịch vụ", {"step": "S-03"}),
          "g2": (2, 9, "c", "gw", "SA_Activation_Flag ?"),
          "b4": (2, 10, "l", "task", "PENDING: KTV\ngiao lắp & thu\ntiền COD"),
          "b3": (2, 10, "r", "task", "INSTANT: VNPAY OK\n→ FPT Play active\n+ SMS mật khẩu"),
          "g3": (2, 11, "l", "gw", "Thu tiền\nthành công?", {"lp": "tr"}),
          "b5": (2, 12, "l", "task", "Xác nhận thu tiền\\n& Kích hoạt dịch vụ"),
          "f4": (1, 12, "c", "task", "Huỷ đơn & Hỗ trợ\\nkhách hàng"),
          "end": (1, 14, "c", "end", "Hoàn tất\\nđơn hàng"),
      },
      [
          ("start", "k1", ""), ("k1", "b1", ""), ("b1", "f1", "", "VH"), ("f1", "k2", ""),
          ("k2", "g1", ""), ("g1", "f2", "COD"),
          ("g1", "f3", "VNPAY", ("U", "r", 1, 312)),
          ("f2", "f3", ""), ("f3", "b2", ""), ("b2", "g2", ""),
          ("g2", "b4", "PENDING"), ("g2", "b3", "INSTANT"),
          ("b3", "end", "", "VH"), ("b4", "g3", ""),
          ("g3", "b5", "Có"), ("g3", "f4", "Không"),
          ("b5", "end", "", "VH"), ("f4", "end", ""),
      ],
      [
          ("BR-01: count(SKU) ≥ 1 → bắt buộc Form Địa chỉ nhận hàng, KHÔNG hiển thị Lịch hẹn KTV.", "f1"),
          ("BR-04: Chọn COD cho đơn Mix SKU+SA → bung Alert box màu vàng cảnh báo thời gian kích hoạt SA.", "f2"),
          ("BR-02: VNPAY → SA_Activation_Flag = INSTANT. BR-03: COD → SA_Activation_Flag = PENDING.", "g2"),
          ("ERR-MIX-02: Lỗi gateway VNPAY → báo lỗi, giữ nguyên giỏ hàng cho khách thử lại.", "b3"),
          ("ERR-MIX-01: Khách hủy đơn COD → cảnh báo tạm dừng, cập nhật trạng thái Cancelled.", "g3"),
      ],
      14)

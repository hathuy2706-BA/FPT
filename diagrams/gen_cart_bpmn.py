# -*- coding: utf-8 -*-
"""Sinh 3 sơ đồ BPMN swimlane dọc cho URD Giỏ hàng & Checkout đa sản phẩm (CART):
   1) Tổng quan toàn trình   2) Luồng giỏ lẻ (1 SP)   3) Luồng đi cùng / gộp giỏ (đa SP)."""

ESC = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

LEFT_PAD = 290
RIGHT_PAD = 290
LANE_W = 460
LANE_X = {0: LEFT_PAD, 1: LEFT_PAD + LANE_W, 2: LEFT_PAD + 2 * LANE_W}
LANES = [
    ("KHÁCH HÀNG (CUSTOMER)",                               LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("WEBSITE FPT.VN (FRONTEND)",                           LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("BACKEND & TÍCH HỢP (SPF · CRM · Payment · Product Hub)", LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
HEADER_H = 46
ROW_H = 94
TOP = 84
BOXW, BOXH = 270, 62
NARROW = 206
LANE_COLOR = {0: "#1f4e78", 1: "#2e75b6", 2: "#7030a0"}


def lane_cx(l, half="c"):
    x = LANE_X[l]
    return x + LANE_W / 2 if half == "c" else (x + LANE_W * 0.28 if half == "l" else x + LANE_W * 0.72)


def row_y(r):
    return TOP + HEADER_H + r * ROW_H + ROW_H / 2


def build(title, N, E, BACK, ANNOT, nrows, outfile):
    def npos(nid):
        l, r, half, kind, label = N[nid][:5]
        return lane_cx(l, half), row_y(r), kind, label, l

    W = LANE_X[2] + LANE_W + RIGHT_PAD
    H = TOP + HEADER_H + nrows * ROW_H + 56
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">']
    out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
    out.append(f'<text x="{W/2}" y="34" font-size="20" font-weight="bold" fill="#1f4e78" text-anchor="middle">{ESC(title)}</text>')
    out.append('<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="#444"/></marker></defs>')

    laneTop, laneBot = TOP, H - 22
    for name, x, w, c, fill in LANES:
        out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{laneBot-laneTop}" fill="{fill}" stroke="{c}" stroke-width="1.4"/>')
        out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{HEADER_H}" fill="{c}"/>')
        out.append(f'<text x="{x+w/2}" y="{laneTop+HEADER_H/2+5}" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{ESC(name)}</text>')

    def tspans(label, cx, cy, fs=10, fill="#000", weight="normal"):
        lines = label.split("\n")
        y0 = cy - (len(lines) - 1) * fs * 0.62
        s = f'<text x="{cx}" y="{y0+fs*0.35}" font-size="{fs}" fill="{fill}" font-weight="{weight}" text-anchor="middle">'
        for j, ln in enumerate(lines):
            s += f'<tspan x="{cx}" dy="{0 if j==0 else fs*1.24}">{ESC(ln)}</tspan>'
        return s + '</text>'

    def anchor(nid, where):
        cx, cy, kind, label, l = npos(nid)
        if kind == "gw": h = w = 70
        elif kind in ("start", "end"): h = w = 52
        else: h = BOXH; w = (NARROW if N[nid][2] != "c" else BOXW)
        if where == "b": return cx, cy + h / 2
        if where == "t": return cx, cy - h / 2
        if where == "l": return cx - w / 2, cy
        if where == "r": return cx + w / 2, cy

    def draw_edge(a, b, label, dashed):
        ax, ay = anchor(a, "b"); bx, by = anchor(b, "t")
        dash = ' stroke-dasharray="6,4"' if dashed else ''
        if abs(ax - bx) < 2:
            d = f'M{ax},{ay} L{bx},{by}'; lx, ly = ax + 8, (ay + by) / 2
        else:
            midy = ay + (by - ay) * 0.5
            d = f'M{ax},{ay} L{ax},{midy} L{bx},{midy} L{bx},{by}'; lx, ly = (ax + bx) / 2, midy - 5
        out.append(f'<path d="{d}" fill="none" stroke="#444" stroke-width="1.5"{dash} marker-end="url(#arr)"/>')
        if label:
            wlbl = len(label) * 6.2 + 8
            out.append(f'<rect x="{lx-wlbl/2}" y="{ly-9}" width="{wlbl}" height="15" fill="#ffffff" opacity="0.92"/>')
            out.append(f'<text x="{lx}" y="{ly+3}" font-size="9.5" fill="#333" text-anchor="middle">{ESC(label)}</text>')

    for a, b, lbl, dsh in E:
        draw_edge(a, b, lbl, dsh)

    def draw_back(a, b, label, xx):
        ax, ay = anchor(a, "l"); bx, by = anchor(b, "l")
        d = f'M{ax},{ay} L{xx},{ay} L{xx},{by} L{bx},{by}'
        out.append(f'<path d="{d}" fill="none" stroke="#c62828" stroke-width="1.4" stroke-dasharray="6,4" marker-end="url(#arr)"/>')
        out.append(f'<text x="{xx+4}" y="{(ay+by)/2}" font-size="9.5" fill="#c62828" text-anchor="start" transform="rotate(-90 {xx+4} {(ay+by)/2})">{ESC(label)}</text>')

    for i, (a, b, lbl) in enumerate(BACK):
        draw_back(a, b, lbl, LEFT_PAD - 250 if i == 0 else LANE_X[1] - 24)

    def draw_annot(text, nid, side):
        cx, cy, kind, label, l = npos(nid)
        bw, bh = 252, 50
        if side == "r":
            ax = LANE_X[l] + LANE_W; bxs = ax + 18; ex = ax
        else:
            ax = LANE_X[l]; bxs = ax - 18 - bw; ex = ax
        by = cy - bh / 2
        endx = (bxs + bw) if side == "l" else bxs
        out.append(f'<path d="M{ex},{cy} L{endx},{cy}" stroke="#bf8f00" stroke-width="1.1" stroke-dasharray="3,3"/>')
        out.append(f'<rect x="{bxs}" y="{by}" width="{bw}" height="{bh}" fill="#fffaf0" stroke="#bf8f00" stroke-width="1.1" stroke-dasharray="5,3" rx="3"/>')
        out.append(tspans(text, bxs + bw / 2, cy, fs=8.2, fill="#7a5b00"))

    for t, nid, side in ANNOT:
        draw_annot(t, nid, side)

    for nid in N:
        cx, cy, kind, label, l = npos(nid)
        col = LANE_COLOR[l]
        if kind == "start":
            out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>')
            out.append(tspans(label, cx, cy, fs=9, fill="#1b5e20", weight="bold"))
        elif kind == "end":
            out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#ffebee" stroke="#c62828" stroke-width="3.4"/>')
            out.append(tspans(label, cx, cy, fs=8.5, fill="#b71c1c", weight="bold"))
        elif kind == "gw":
            r = 35
            out.append(f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="#fff2cc" stroke="#bf8f00" stroke-width="1.8"/>')
            out.append(f'<text x="{cx}" y="{cy-r-6}" font-size="15" font-weight="bold" fill="#bf8f00" text-anchor="middle">×</text>')
            out.append(tspans(label, cx, cy, fs=8.8, fill="#5b4500", weight="bold"))
        else:
            w = NARROW if N[nid][2] != "c" else BOXW
            out.append(f'<rect x="{cx-w/2}" y="{cy-BOXH/2}" width="{w}" height="{BOXH}" rx="9" fill="#ffffff" stroke="{col}" stroke-width="1.7"/>')
            out.append(tspans(label, cx, cy, fs=9.6, fill="#1a1a1a"))

    out.append(f'<text x="{W/2}" y="{H-15}" font-size="11" fill="#555" text-anchor="middle">Ký hiệu BPMN:  ◯ Start Event   ◉ End Event   ▭ Task   ◇× Exclusive Gateway   ┄┄ Text Annotation   — ▸ Sequence Flow   ┄▸ Luồng quay lui</text>')
    out.append('</svg>')
    open(outfile, "w", encoding="utf-8").write("\n".join(out))
    print("OK", outfile, W, H)


# ============================ DIAGRAM 1 — TỔNG QUAN ============================
N1 = {
 "start": (0, 0, "c", "start", "Bắt đầu\nChọn SP trên PDP"),
 "k1": (0, 1, "c", "task", "Chọn cấu hình SP\n(SL · Chu kỳ · Cloud/Gói)\nbấm 'Thêm vào giỏ hàng'"),
 "f1": (1, 2, "c", "task", "Tạo / cập nhật dòng giỏ\n(theo Line_Key)"),
 "f2": (1, 3, "c", "task", "Lưu giỏ & hiển thị\nmàn Giỏ hàng"),
 "k2": (0, 4, "c", "task", "Điều chỉnh giỏ\n(Tick · +/- SL · Đổi thuộc tính · Xóa)"),
 "gsel": (1, 5, "c", "gw", "Có ≥ 1 dòng\nđược chọn?"),
 "k3": (0, 6, "c", "task", "Bấm 'Tiếp tục'"),
 "f3": (1, 7, "c", "task", "Hiển thị màn Checkout\n(B1 Thông tin → B2 Thanh toán)"),
 "k4": (0, 8, "c", "task", "Nhập SĐT (bắt buộc) &\nthông tin nhận hàng / hóa đơn"),
 "b1": (2, 9, "c", "task", "Tra cứu hợp đồng CRM &\nvalidate giá (Product Hub)"),
 "k5": (0, 10, "c", "task", "Chọn triển khai · Ưu đãi · PTTT\n→ Xác nhận & Thanh toán"),
 "gpay": (2, 11, "c", "gw", "Thanh toán\nthành công?"),
 "b2": (2, 12, "c", "task", "Tạo đơn trên SPF &\nKích hoạt / Giao hàng"),
 "f4": (1, 13, "c", "task", "Thank You Page\n(Mã đơn · Theo dõi ĐH)"),
 "end": (0, 14, "c", "end", "Hoàn tất\nđơn hàng"),
}
E1 = [("start","k1","",0),("k1","f1","",0),("f1","f2","",0),("f2","k2","",0),("k2","gsel","",0),
      ("gsel","k3","Có",0),("k3","f3","",0),("f3","k4","",0),("k4","b1","",0),("b1","k5","",0),
      ("k5","gpay","",0),("gpay","b2","Thành công",0),("b2","f4","",0),("f4","end","",0)]
BACK1 = [("gsel","k2","Không → nút 'Tiếp tục' mờ"),("gpay","k5","Thất bại → thử lại / đổi PTTT")]
ANNOT1 = [
 ("[CART-BR-01] Line_Key = SKU/Gói + Thuộc tính + Chu kỳ. Trùng → cộng dồn SL; khác → tách dòng.", "f1", "r"),
 ("[CART-BR-04] Giá · chu kỳ · PTTT · biểu phí nạp động từ Product Hub / QLCS, không hardcode FE.", "f2", "r"),
 ("[CART-BR-07] Tra cứu hợp đồng dịch vụ FPT trên CRM → đề xuất gộp / liên kết hợp đồng.", "b1", "r"),
 ("[CART-BR-05] Tick 'Nhận hóa đơn' → bắt buộc Họ tên · Email · Địa chỉ đầy đủ.", "k4", "l"),
 ("[CART-BR-08] Mọi thay đổi đơn → BE re-validate giá & điều kiện trước thanh toán.", "k5", "l"),
]
build("SƠ ĐỒ BPMN TỔNG QUAN — GIỎ HÀNG & CHECKOUT ĐA SẢN PHẨM (FPT.VN)", N1, E1, BACK1, ANNOT1, 15,
      "/Users/hathuy/Documents/FPT-1/diagrams/cart_overview_bpmn.svg")

# ============================ DIAGRAM 2 — GIỎ LẺ ============================
N2 = {
 "start": (0, 0, "c", "start", "Bắt đầu\nMua 1 sản phẩm"),
 "k1": (0, 1, "c", "task", "Trên PDP chọn thuộc tính\n(Cloud / Gói · Chu kỳ · Số lượng)"),
 "k2": (0, 2, "c", "task", "Bấm 'Thêm vào giỏ hàng'"),
 "f1": (1, 3, "c", "task", "Tạo dòng giỏ theo Line_Key\n(SKU/Gói + Thuộc tính + Chu kỳ)"),
 "gdup": (1, 4, "c", "gw", "Trùng Line_Key\ndòng có sẵn?"),
 "f2": (1, 5, "l", "task", "Cộng dồn số lượng\ndòng trùng"),
 "f3": (1, 5, "r", "task", "Tách dòng sản phẩm\nmới riêng biệt"),
 "f4": (1, 6, "c", "task", "Hiển thị Giỏ hàng\n(tạm tính real-time)"),
 "k3": (0, 7, "c", "task", "Tick chọn dòng · Bấm 'Tiếp tục'"),
 "f5": (1, 8, "c", "task", "Màn Checkout"),
 "k4": (0, 9, "c", "task", "Nhập SĐT · Hình thức triển khai\n(KTV / Tự lắp) hoặc Kích hoạt · PTTT"),
 "b1": (2, 10, "c", "task", "Validate giá & khởi tạo\ngiao dịch thanh toán"),
 "gpay": (2, 11, "c", "gw", "Thanh toán\nthành công?"),
 "b2": (2, 12, "c", "task", "Tạo đơn SPF &\nKích hoạt / Giao thiết bị"),
 "f6": (1, 13, "c", "task", "Thank You Page\n(Mã đơn hàng)"),
 "enda": (0, 14, "l", "end", "Hoàn tất\n(KTV lắp / Kích hoạt tự động)"),
 "endb": (0, 14, "r", "end", "Hoàn tất\n(Tự lắp / KH tự kích hoạt)"),
}
E2 = [("start","k1","",0),("k1","k2","",0),("k2","f1","",0),("f1","gdup","",0),
      ("gdup","f2","Có",0),("gdup","f3","Không",0),("f2","f4","",0),("f3","f4","",0),
      ("f4","k3","",0),("k3","f5","",0),("f5","k4","",0),("k4","b1","",0),("b1","gpay","",0),
      ("gpay","b2","Thành công",0),("b2","f6","",0),("f6","enda","",0),("f6","endb","",0)]
BACK2 = [("gpay","k4","Thất bại → thử lại")]
ANNOT2 = [
 ("[CART-BR-13] Thiết bị có Cloud (Camera) bắt buộc gắn 01 gói Cloud, trừ khi KH tick 'đã có Cloud'.", "k1", "l"),
 ("[CART-BR-06] Phí lắp đặt theo biểu phí QLCS; tự lắp → giao qua đối tác VC, không phí thi công.", "k4", "l"),
 ("[CART-BR-09] PTTT do QLCS khai báo; COD khóa ở vùng sâu/xa/hải đảo không hỗ trợ thu hộ.", "b1", "r"),
]
build("SƠ ĐỒ BPMN — LUỒNG GIỎ LẺ (THÊM TỪNG SẢN PHẨM)", N2, E2, BACK2, ANNOT2, 15,
      "/Users/hathuy/Documents/FPT-1/diagrams/cart_single_bpmn.svg")

# ============================ DIAGRAM 3 — ĐI CÙNG / GỘP GIỎ ============================
N3 = {
 "start": (0, 0, "c", "start", "Bắt đầu\nChọn nhiều sản phẩm"),
 "k1": (0, 1, "c", "task", "Thêm lần lượt từng SP vào giỏ\n(SKU thiết bị · SA dịch vụ: Cloud/FPT Play/Ultrafast)"),
 "glog": (1, 2, "c", "gw", "KH đã\nđăng nhập?"),
 "f1": (1, 3, "l", "task", "Lưu giỏ theo tài khoản\n(đồng bộ đa thiết bị)"),
 "f2": (1, 3, "r", "task", "Lưu giỏ tạm\ntrên trình duyệt"),
 "f3": (1, 4, "r", "task", "Hợp nhất giỏ tạm vào\ngiỏ tài khoản khi đăng nhập"),
 "f4": (1, 5, "c", "task", "Hiển thị giỏ đa dòng\n(mỗi SP 1 dòng theo Line_Key)"),
 "k2": (0, 6, "c", "task", "Tick chọn các dòng · Bấm 'Tiếp tục'"),
 "f5": (1, 7, "c", "task", "Checkout — panel 'Thông tin thanh toán'\nliệt kê từng dòng + 'Cần thanh toán'"),
 "k3": (0, 8, "c", "task", "Nhập SĐT · chọn triển khai/kích hoạt\ncho từng nhóm SP · Ưu đãi · PTTT"),
 "b1": (2, 9, "c", "task", "Tra cứu hợp đồng CRM ·\nvalidate & gộp tính tiền toàn giỏ"),
 "gpay": (2, 10, "c", "gw", "Thanh toán\nthành công?"),
 "b2": (2, 11, "c", "task", "Tạo 1 đơn tổng hợp trên SPF\n(tách hạng mục thiết bị & dịch vụ)"),
 "f6": (1, 12, "c", "task", "Thank You Page\n(1 mã đơn cho toàn giỏ)"),
 "end": (0, 13, "c", "end", "Hoàn tất\nđơn gộp"),
}
E3 = [("start","k1","",0),("k1","glog","",0),("glog","f1","Đã ĐN",0),("glog","f2","Chưa ĐN",0),
      ("f1","f4","",0),("f2","f3","",0),("f3","f4","",0),("f4","k2","",0),("k2","f5","",0),
      ("f5","k3","",0),("k3","b1","",0),("b1","gpay","",0),("gpay","b2","Thành công",0),
      ("b2","f6","",0),("f6","end","",0)]
BACK3 = [("gpay","k3","Thất bại → thử lại")]
ANNOT3 = [
 ("[CART-BR-03] Mỗi SP khác loại = 1 dòng độc lập theo Line_Key; thiết bị & dịch vụ tách riêng SL.", "f4", "r"),
 ("[CART-BR-02] Lưu & hợp nhất giỏ guest ↔ tài khoản khi đăng nhập (đồng bộ đa thiết bị).", "f3", "r"),
 ("[CART-BR-11] 'Cần thanh toán' = Σ thành tiền dòng tick − ưu đãi; BE tính, FE hiển thị real-time.", "f5", "l"),
 ("[CART-BR-10] Gộp nhiều SP khác loại → 1 đơn SPF, 1 lần thanh toán, VAT gộp theo quy định.", "b2", "r"),
]
build("SƠ ĐỒ BPMN — LUỒNG ĐI CÙNG / GỘP GIỎ (ĐA SẢN PHẨM TRONG 1 GIỎ)", N3, E3, BACK3, ANNOT3, 14,
      "/Users/hathuy/Documents/FPT-1/diagrams/cart_merge_bpmn.svg")

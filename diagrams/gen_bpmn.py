# -*- coding: utf-8 -*-
"""Sinh sơ đồ BPMN chuẩn (swimlane dọc) cho luồng Giỏ hàng & Checkout Camera FPT."""

ESC = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---------- Cấu hình lane ----------
LEFT_PAD = 280
LANE_W = 430
LANE_X = {0: LEFT_PAD, 1: LEFT_PAD+LANE_W, 2: LEFT_PAD+2*LANE_W}   # mép trái mỗi lane
LANES = [
    ("KHÁCH HÀNG (CUSTOMER)",                                  LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("WEBSITE FPT.VN (FRONTEND)",                             LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("HỆ THỐNG BACKEND & TÍCH HỢP (SPF · CRM · Payment)",     LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
HEADER_H = 46
ROW_H = 92
TOP = 84
BOXW, BOXH = 250, 60
NARROW = 196

def lane_cx(l, half="c"):
    x = LANE_X[l]
    if half == "c": return x + LANE_W/2
    if half == "l": return x + LANE_W*0.28
    if half == "r": return x + LANE_W*0.72

def row_y(r): return TOP + HEADER_H + r*ROW_H + ROW_H/2

# ---------- Khai báo node ----------
# id: (lane, row, half, kind, label, color)
LANE_COLOR = {0:"#1f4e78", 1:"#2e75b6", 2:"#7030a0"}
N = {
 "start":(0,0,"c","start","Bắt đầu\nmua sắm"),
 "k1":(0,1,"c","task","Duyệt SP & chọn cấu hình trên PDP:\nMàu sắc · Loại Cloud · Chu kỳ"),
 "k2":(0,2,"c","task","Bấm 'Thêm vào giỏ hàng'"),
 "f1":(1,3,"c","task","Tạo / cập nhật dòng giỏ hàng\n(Tách dòng · Gộp Combo)"),
 "f2":(1,4,"c","task","Lưu giỏ hàng &\nhiển thị màn Giỏ hàng"),
 "k3":(0,5,"c","task","Điều chỉnh giỏ hàng\n(Tick chọn · +/- SL · Đổi chu kỳ · Xóa)"),
 "gsel":(1,6,"c","gw","Có ≥ 1 dòng\nđược chọn?"),
 "k4":(0,7,"c","task","Bấm 'Tiếp tục thanh toán'"),
 "f3":(1,8,"c","task","Hiển thị màn Checkout"),
 "k5":(0,9,"c","task","Nhập SĐT nhận hàng"),
 "b1":(2,10,"c","task","Tra cứu hợp đồng Internet\n(CRM) theo SĐT"),
 "gnet":(2,11,"c","gw","Có hợp đồng\nInternet FPT?"),
 "bnoi":(2,12,"l","task","Đề xuất gộp hóa đơn\n& liên kết hợp đồng"),
 "bngoai":(2,12,"r","task","Bỏ qua đề xuất\n(tiếp tục đặt hàng)"),
 "k6":(0,13,"c","task","Chọn hình thức triển khai"),
 "ginstall":(1,14,"c","gw","Hình thức\ntriển khai?"),
 "f4":(1,15,"l","task","Lịch hẹn KTV & phí lắp đặt\n(theo biểu phí QLCS)"),
 "f5":(1,15,"r","task","Tự lắp: giao hàng tận nơi\n(không phí thi công)"),
 "k7":(0,16,"c","task","Nhập địa chỉ · Voucher ·\nChọn phương thức thanh toán"),
 "k8":(0,17,"c","task","Xác nhận & Thanh toán"),
 "gpay":(2,18,"c","gw","Thanh toán\nthành công?"),
 "b2":(2,19,"c","task","Tạo đơn hàng trên SPF\n& đẩy cấu hình cước Cloud"),
 "gthanks":(1,20,"c","gw","Hình thức\ntriển khai?"),
 "f6":(1,21,"l","task","Thank You Page\n(Lịch hẹn KTV + Wifi)"),
 "f7":(1,21,"r","task","Thank You Page\n(Vận đơn + Hub tự lắp)"),
 "end_a":(0,22,"l","end","Hoàn tất\n(KTV lắp đặt)"),
 "end_b":(0,22,"r","end","Hoàn tất\n(Tự lắp đặt)"),
}

def npos(nid):
    l,r,half,kind,label = N[nid][:5]
    return lane_cx(l,half), row_y(r), kind, label, l

# ---------- Edges: (from, to, label, dashed, route) ----------
# route: 'v' vertical/L, 'down' = simple, 'back' = quay lui bên trái
E = [
 ("start","k1","",0),
 ("k1","k2","",0),
 ("k2","f1","",0),
 ("f1","f2","",0),
 ("f2","k3","",0),
 ("k3","gsel","",0),
 ("gsel","k4","Có",0),
 ("k4","f3","",0),
 ("f3","k5","",0),
 ("k5","b1","",0),
 ("b1","gnet","",0),
 ("gnet","bnoi","Có",0),
 ("gnet","bngoai","Không",0),
 ("bnoi","k6","",0),
 ("bngoai","k6","",0),
 ("k6","ginstall","",0),
 ("ginstall","f4","KTV FPT",0),
 ("ginstall","f5","Tự lắp",0),
 ("f4","k7","",0),
 ("f5","k7","",0),
 ("k7","k8","",0),
 ("k8","gpay","",0),
 ("gpay","b2","Thành công",0),
 ("b2","gthanks","",0),
 ("gthanks","f6","KTV FPT",0),
 ("gthanks","f7","Tự lắp",0),
 ("f6","end_a","",0),
 ("f7","end_b","",0),
]
# back edges (dashed, đi vòng bên trái)
BACK = [
 ("gsel","k3","Không → nút mờ"),
 ("gpay","k8","Thất bại → thử lại"),
]
# annotations: (text, anchor_node, side)
ANNOT = [
 ("[BR-01] Line_Key = SKU + Loại Cloud + Chu kỳ.\nTrùng → cộng dồn SL; khác → tách dòng.","f1","r"),
 ("[BR-07] Chưa login → lưu cache trình duyệt.\nĐã login → lưu theo tài khoản KH.","f2","r"),
 ("[BR-05] Phí lắp đặt theo biểu phí QLCS.\nKhông ưu đãi/miễn phí lắp đặt.","f4","l"),
 ("[BR-06] PTTT do QLCS khai báo;\nCOD khóa ở vùng cấm giao vận.","k7","l"),
]

W = LANE_X[2] + LANE_W + 40
H = TOP + HEADER_H + 23*ROW_H + 50

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">')
out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
# title
out.append(f'<text x="{W/2}" y="34" font-size="20" font-weight="bold" fill="#1f4e78" text-anchor="middle">SƠ ĐỒ BPMN — LUỒNG GIỎ HÀNG &amp; CHECKOUT CAMERA FPT</text>')

# defs: arrow markers
out.append('<defs>')
out.append('<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="#444"/></marker>')
out.append('<marker id="arrd" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="#bf8f00"/></marker>')
out.append('</defs>')

# lanes
laneTop = TOP
laneBot = H-20
for i,(name,x,w,c,fill) in enumerate(LANES):
    out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{laneBot-laneTop}" fill="{fill}" stroke="{c}" stroke-width="1.4"/>')
    out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{HEADER_H}" fill="{c}"/>')
    out.append(f'<text x="{x+w/2}" y="{laneTop+HEADER_H/2+5}" font-size="13.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{ESC(name)}</text>')

def tspans(label, cx, cy, fs=11, fill="#000", weight="normal"):
    lines = label.split("\n")
    total = len(lines)
    y0 = cy - (total-1)*fs*0.62
    s = f'<text x="{cx}" y="{y0+fs*0.35}" font-size="{fs}" fill="{fill}" font-weight="{weight}" text-anchor="middle">'
    for j,ln in enumerate(lines):
        dy = 0 if j==0 else fs*1.24
        s += f'<tspan x="{cx}" dy="{dy}">{ESC(ln)}</tspan>'
    s += '</text>'
    return s

# draw edges first (under nodes)
def anchor(nid, where):
    cx,cy,kind,label,l = npos(nid)
    if kind=="gw": h=70; w=70
    elif kind in("start","end"): h=52; w=52
    else: h=BOXH; w=(NARROW if N[nid][2]!="c" else BOXW)
    if where=="b": return cx, cy+h/2
    if where=="t": return cx, cy-h/2
    if where=="l": return cx-w/2, cy
    if where=="r": return cx+w/2, cy

def draw_edge(a,b,label,dashed):
    ax,ay = anchor(a,"b")
    bx,by = anchor(b,"t")
    dash = ' stroke-dasharray="6,4"' if dashed else ''
    col = "#444"
    if abs(ax-bx) < 2:
        d = f'M{ax},{ay} L{bx},{by}'
        lx,ly = ax+8, (ay+by)/2
    else:
        midy = ay + (by-ay)*0.5
        d = f'M{ax},{ay} L{ax},{midy} L{bx},{midy} L{bx},{by}'
        lx,ly = (ax+bx)/2, midy-5
    out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.5"{dash} marker-end="url(#arr)"/>')
    if label:
        wlbl = len(label)*6.2+8
        out.append(f'<rect x="{lx-wlbl/2}" y="{ly-9}" width="{wlbl}" height="15" fill="#ffffff" opacity="0.9"/>')
        out.append(f'<text x="{lx}" y="{ly+3}" font-size="9.5" fill="#333" text-anchor="middle">{ESC(label)}</text>')

for a,b,lbl,dsh in E:
    draw_edge(a,b,lbl,dsh)

# back edges: đi vòng bên trái ngoài cùng
def draw_back(a,b,label,xoff):
    ax,ay = anchor(a,"l")
    bx,by = anchor(b,"l")
    xx = xoff
    d = f'M{ax},{ay} L{xx},{ay} L{xx},{by} L{bx},{by}'
    out.append(f'<path d="{d}" fill="none" stroke="#c62828" stroke-width="1.4" stroke-dasharray="6,4" marker-end="url(#arr)"/>')
    out.append(f'<text x="{xx+4}" y="{(ay+by)/2}" font-size="9.5" fill="#c62828" text-anchor="start" transform="rotate(-90 {xx+4} {(ay+by)/2})">{ESC(label)}</text>')

draw_back(*BACK[0], LEFT_PAD-250)
draw_back(*BACK[1], LANE_X[1]-22)  # gpay (lane BE) quay lui sang trái tới k8

# annotations
def draw_annot(text, nid, side):
    cx,cy,kind,label,l = npos(nid)
    bw = 232; bh = 40
    if side=="r":
        ax = (LANE_X[l]+LANE_W) ; bxs = ax+18; ex = ax
    else:
        ax = LANE_X[l]; bxs = ax-18-bw; ex = ax
    by = cy-bh/2
    # connector dashed
    out.append(f'<path d="M{ex + (0 if side=="l" else 0)},{cy} L{(bxs+bw) if side=="l" else bxs},{cy}" stroke="#bf8f00" stroke-width="1.1" stroke-dasharray="3,3"/>')
    out.append(f'<rect x="{bxs}" y="{by}" width="{bw}" height="{bh}" fill="#fffaf0" stroke="#bf8f00" stroke-width="1.1" stroke-dasharray="5,3" rx="3"/>')
    out.append(tspans(text, bxs+bw/2, cy, fs=8.6, fill="#7a5b00"))

for t,nid,side in ANNOT:
    draw_annot(t,nid,side)

# draw nodes
for nid in N:
    cx,cy,kind,label,l = npos(nid)
    col = LANE_COLOR[l]
    if kind=="start":
        out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#e8f5e9" stroke="#2e7d32" stroke-width="2"/>')
        out.append(tspans(label,cx,cy,fs=9.5,fill="#1b5e20",weight="bold"))
    elif kind=="end":
        out.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="#ffebee" stroke="#c62828" stroke-width="3.4"/>')
        out.append(tspans(label,cx,cy,fs=9,fill="#b71c1c",weight="bold"))
    elif kind=="gw":
        r=35
        out.append(f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="#fff2cc" stroke="#bf8f00" stroke-width="1.8"/>')
        out.append(f'<text x="{cx}" y="{cy-r-6}" font-size="15" font-weight="bold" fill="#bf8f00" text-anchor="middle">×</text>')
        out.append(tspans(label,cx,cy,fs=9,fill="#5b4500",weight="bold"))
    else:
        w = NARROW if N[nid][2]!="c" else BOXW
        out.append(f'<rect x="{cx-w/2}" y="{cy-BOXH/2}" width="{w}" height="{BOXH}" rx="9" fill="#ffffff" stroke="{col}" stroke-width="1.7"/>')
        out.append(tspans(label,cx,cy,fs=10,fill="#1a1a1a"))

# legend (đáy sơ đồ)
out.append(f'<text x="{W/2}" y="{H-16}" font-size="11" fill="#555" text-anchor="middle">Ký hiệu BPMN:  ◯ Start Event   ◉ End Event   ▭ Task   ◇× Exclusive Gateway   ┄┄ Text Annotation   — ▸ Sequence Flow</text>')

out.append('</svg>')
open("/Users/hathuy/Documents/FPT-1/diagrams/camcart_bpmn.svg","w",encoding="utf-8").write("\n".join(out))
print("OK SVG", W, H)

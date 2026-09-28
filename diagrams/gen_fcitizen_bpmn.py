# -*- coding: utf-8 -*-
import os

ESC = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

# ---------- Cấu hình lane ----------
LEFT_PAD = 280
LANE_W = 540
LANE_X = {0: LEFT_PAD, 1: LEFT_PAD+LANE_W, 2: LEFT_PAD+2*LANE_W}
LANES = [
    ("KHÁCH HÀNG (CUSTOMER)", LANE_X[0], LANE_W, "#1f4e78", "#eef3fb"),
    ("WEBSITE FPT.VN (FRONTEND)", LANE_X[1], LANE_W, "#2e75b6", "#eef7fd"),
    ("HỆ THỐNG BACKEND & TÍCH HỢP", LANE_X[2], LANE_W, "#7030a0", "#f6f0fb"),
]
HEADER_H = 46
ROW_H = 120
TOP = 84
BOXW, BOXH = 260, 60
NARROW = 230

def lane_cx(l, half="c"):
    x = LANE_X[l]
    if half == "c": return x + LANE_W/2
    if half == "l": return x + LANE_W*0.25
    if half == "r": return x + LANE_W*0.75

def row_y(r): return TOP + HEADER_H + r*ROW_H + ROW_H/2

LANE_COLOR = {0:"#1f4e78", 1:"#2e75b6", 2:"#7030a0"}
N = {
 "start": (0, 0, "c", "start", "Bắt đầu"),
 "k1": (0, 1, "c", "task", "Truy cập fpt.vn/fcitizen"),
 "k2": (0, 2, "c", "task", "Xem các gói ưu đãi cho CBNV"),
 "k3": (0, 3, "c", "task", "Chọn gói & bấm Đăng ký ngay"),
 "k4": (0, 4, "c", "task", "Popup: Chọn CTTV & Nhập Email"),
 "f1": (1, 5, "c", "task", "Call API check Email"),
 "gf1": (1, 6, "c", "gw", "Email chuẩn\nformat?"),
 "f2_otp": (1, 7, "l", "task", "Call API gửi OTP"),
 "f2_sdt": (1, 7, "r", "task", "Hiển thị field\nnhập SĐT"),
 "k_otp": (0, 8, "l", "task", "Nhập OTP"),
 "k_sdt": (0, 8, "r", "task", "Nhập SĐT"),
 "f3_ver": (1, 9, "l", "task", "Verify OTP"),
 "gf2_email": (1, 9, "r", "gw", "Nhập lại\nEmail?"),
 "gf3_otp": (1, 10, "l", "gw", "OTP Hợp lệ?"),
 "f4_send": (1, 10, "r", "task", "Bấm Gửi SĐT"),
 "f5_err": (1, 11, "l", "task", "Thông báo lỗi"),
 "b1_sdt": (2, 11, "r", "task", "Verify đầu số nhà mạng"),
 "gf4_act": (1, 12, "l", "gw", "Hành động\ntiếp theo?"),
 "gb1_val": (2, 12, "r", "gw", "Đầu số\nhợp lệ?"),
 "f6_chk": (1, 13, "l", "task", "Vào luồng checkout\n(step 1)"),
 "b2_push": (2, 13, "r", "task", "Đẩy luồng KHTN\ncho Sale ECOM"),
 "b3_hdld": (2, 14, "l", "task", "Kiểm tra thông tin HĐLĐ"),
 "b4_msg": (2, 14, "r", "task", "Thông báo có\nNV tư vấn"),
 "gb2_hdld": (2, 15, "l", "gw", "Đủ ĐK HĐLĐ?"),
 "end1": (2, 15, "r", "end", "Hoàn tất"),
 "b5_net": (2, 16, "l", "task", "Kiểm tra HĐ Internet"),
 "gb3_net": (2, 17, "l", "gw", "Là KH mới?"),
 "b6_next": (2, 18, "l", "task", "Đi tiếp luồng\ntoàn trình (B4)"),
 "b7_sr": (2, 18, "r", "task", "Đẩy SR cho DVKH"),
 "end2": (2, 19, "l", "end", "Hoàn tất"),
 "end3": (2, 19, "r", "end", "Hoàn tất"),
}

def npos(nid):
    l,r,half,kind,label = N[nid][:5]
    return lane_cx(l,half), row_y(r), kind, label, l

E = [
 ("start", "k1", "", 0),
 ("k1", "k2", "", 0),
 ("k2", "k3", "", 0),
 ("k3", "k4", "", 0),
 ("k4", "f1", "", 0),
 ("f1", "gf1", "", 0),
 ("gf1", "f2_otp", "Đúng format", 0),
 ("gf1", "f2_sdt", "Sai format", 0),
 ("f2_otp", "k_otp", "", 0),
 ("f2_sdt", "k_sdt", "", 0),
 ("k_otp", "f3_ver", "", 0),
 ("k_sdt", "gf2_email", "", 0),
 ("gf2_email", "f4_send", "Không", 0),
 ("f3_ver", "gf3_otp", "", 0),
 ("f4_send", "b1_sdt", "", 0),
 ("gf3_otp", "f5_err", "Fail", 0),
 ("gf3_otp", "f6_chk", "Pass", 0),
 ("f5_err", "gf4_act", "", 0),
 ("gf4_act", "f2_sdt", "Nhập SĐT", 0),
 ("b1_sdt", "gb1_val", "", 0),
 ("gb1_val", "b2_push", "Pass", 0),
 ("f6_chk", "b3_hdld", "", 0),
 ("b2_push", "b4_msg", "", 0),
 ("b4_msg", "end1", "", 0),
 ("b3_hdld", "gb2_hdld", "", 0),
 ("gb2_hdld", "b5_net", "Đủ", 0),
 ("gb2_hdld", "b2_push", "Không đủ", 0),
 ("b5_net", "gb3_net", "", 0),
 ("gb3_net", "b6_next", "KH mới", 0),
 ("gb3_net", "b7_sr", "Hiện hữu", 0),
 ("b6_next", "end2", "", 0),
 ("b7_sr", "end3", "", 0),
]

BACK = [
 ("gf2_email", "f1", "Có"),
 ("gf4_act", "f2_otp", "Gửi lại OTP"),
 ("gb1_val", "k_sdt", "Fail"),
]

W = LANE_X[2] + LANE_W + 40
H = TOP + HEADER_H + 20*ROW_H + 50

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">')
out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
out.append(f'<text x="{W/2}" y="34" font-size="20" font-weight="bold" fill="#1f4e78" text-anchor="middle">SƠ ĐỒ BPMN — LUỒNG FCITIZEN (KHUYẾN MÃI CBNV FPT)</text>')

out.append('<defs>')
out.append('<marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="#444"/></marker>')
out.append('</defs>')

laneTop = TOP
laneBot = H-20
for i,(name,x,w,c,fill) in enumerate(LANES):
    out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{laneBot-laneTop}" fill="{fill}" stroke="{c}" stroke-width="1.4"/>')
    out.append(f'<rect x="{x}" y="{laneTop}" width="{w}" height="{HEADER_H}" fill="{c}"/>')
    out.append(f'<text x="{x+w/2}" y="{laneTop+HEADER_H/2+5}" font-size="13.5" font-weight="bold" fill="#ffffff" text-anchor="middle">{ESC(name)}</text>')

def tspans(label, cx, cy, fs=11, fill="#000", weight="normal"):
    lines = label.split("\\n")
    total = len(lines)
    y0 = cy - (total-1)*fs*0.62
    s = f'<text x="{cx}" y="{y0+fs*0.35}" font-size="{fs}" fill="{fill}" font-weight="{weight}" text-anchor="middle">'
    for j,ln in enumerate(lines):
        dy = 0 if j==0 else fs*1.24
        s += f'<tspan x="{cx}" dy="{dy}">{ESC(ln)}</tspan>'
    s += '</text>'
    return s

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
    col = "#444"
    if abs(ax-bx) < 2:
        d = f'M{ax},{ay} L{bx},{by}'
        lx,ly = ax+8, (ay+by)/2
    else:
        midy = ay + (by-ay)*0.5
        d = f'M{ax},{ay} L{ax},{midy} L{bx},{midy} L{bx},{by}'
        lx,ly = (ax+bx)/2, midy-5
    out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.5"/>')
    # Draw arrow head pointing DOWN at (bx, by)
    out.append(f'<polygon points="{bx-4},{by-6} {bx+4},{by-6} {bx},{by}" fill="{col}"/>')
    if label:
        wlbl = len(label)*6.2+8
        out.append(f'<rect x="{lx-wlbl/2}" y="{ly-9}" width="{wlbl}" height="15" fill="#ffffff" opacity="0.9"/>')
        out.append(f'<text x="{lx}" y="{ly+3}" font-size="9.5" fill="#333" text-anchor="middle">{ESC(label)}</text>')

for a,b,lbl,dsh in E:
    draw_edge(a,b,lbl,dsh)

def draw_back(a,b,label,xoff):
    ax,ay = anchor(a,"l")
    bx,by = anchor(b,"l")
    xx = xoff
    d = f'M{ax},{ay} L{xx},{ay} L{xx},{by} L{bx},{by}'
    out.append(f'<path d="{d}" fill="none" stroke="#c62828" stroke-width="1.4" stroke-dasharray="6,4"/>')
    # Draw arrow head pointing RIGHT at (bx, by)
    out.append(f'<polygon points="{bx-6},{by-4} {bx-6},{by+4} {bx},{by}" fill="#c62828"/>')
    out.append(f'<text x="{xx+4}" y="{(ay+by)/2}" font-size="9.5" fill="#c62828" text-anchor="start" transform="rotate(-90 {xx+4} {(ay+by)/2})">{ESC(label)}</text>')

draw_back(*BACK[0], LANE_X[1]-30)
draw_back(*BACK[1], LANE_X[1]-80)
draw_back(*BACK[2], LANE_X[0]-30)

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

out.append(f'<text x="{W/2}" y="{H-16}" font-size="11" fill="#555" text-anchor="middle">Ký hiệu BPMN:  ◯ Start Event   ◉ End Event   ▭ Task   ◇× Exclusive Gateway   ┄┄ Text Annotation   — ▸ Sequence Flow</text>')
out.append('</svg>')
open("/Users/hathuy/Documents/FPT-1/diagrams/FCitizen_BPMN_Flow.svg","w",encoding="utf-8").write("\n".join(out))
print("Done")

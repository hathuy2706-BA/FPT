/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V4 (COMPACT LUXURY DASHBOARD)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * Các nâng cấp V4:
 * 1. Đưa độ ưu tiên [P1]-[P4] vào góc phải trên & ngoài cùng của thanh task (căn lề phải).
 * 2. Đưa PIC & Trạng thái vào góc phải dưới & ngoài cùng của thanh task (căn lề phải).
 * 3. Giảm độ cao của các task gọn gàng, thanh thoát (chiều cao dòng 38px thay vì 58px).
 * 4. Tiêu đề các tháng sử dụng màu ĐẬM tương ứng cột (T10 Xanh đậm, T11 Tím đậm, T12 Xanh ngọc đậm), chữ trắng.
 * 5. Bỏ hàng 2 & 3 cũ, thay bằng 1 dòng ghi chú:
 *    "(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request".
 * 6. Đóng khung từng tháng riêng biệt, ẩn đường chỉ lưới (gridlines), nền 3 tháng pastel mờ nhẹ.
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// Cấu hình màu Pastel đậm hơn nền cột cho 8 nấc tiến độ / trạng thái
const STATUS_CONFIG = {
  'Chưa tiếp nhận': {
    step: '1/8 (12.5%)',
    bg: '#E2E8F0',        // Pastel xám bạc
    fg: '#1E293B',
    badgeColor: '#475569',
    borderColor: '#CBD5E1'
  },
  'Đã tiếp nhận yêu cầu': {
    step: '2/8 (25.0%)',
    bg: '#E9D5FF',        // Pastel tím thạch anh
    fg: '#581C87',
    badgeColor: '#6B21A8',
    borderColor: '#D8B4FE'
  },
  'Đang phân tích/Document': {
    step: '3/8 (37.5%)',
    bg: '#FED7AA',        // Pastel cam mơ
    fg: '#7C2D12',
    badgeColor: '#C2410C',
    borderColor: '#FDBA74'
  },
  'PO reviewed/Transfer DEV': {
    step: '4/8 (50.0%)',
    bg: '#BBF7D0',        // Pastel xanh bạc hà
    fg: '#14532D',
    badgeColor: '#15803D',
    borderColor: '#86EFAC'
  },
  'PO reviewed': {
    step: '4/8 (50.0%)',
    bg: '#BBF7D0',
    fg: '#14532D',
    badgeColor: '#15803D',
    borderColor: '#86EFAC'
  },
  'DEV In Progress': {
    step: '5/8 (62.5%)',
    bg: '#FEF08A',        // Pastel vàng mật ong
    fg: '#713F12',
    badgeColor: '#A16207',
    borderColor: '#FDE047'
  },
  'UAT': {
    step: '6/8 (75.0%)',
    bg: '#DDD6FE',        // Pastel tím lavender
    fg: '#3B0764',
    badgeColor: '#581C87',
    borderColor: '#C4B5FD'
  },
  'QC/CSOC': {
    step: '7/8 (87.5%)',
    bg: '#BAE6FD',        // Pastel xanh da trời
    fg: '#0C4A6E',
    badgeColor: '#0284C7',
    borderColor: '#7DD3FC'
  },
  'Done': {
    step: '8/8 (100.0%)',
    bg: '#A7F3D0',        // Pastel xanh ngọc lục bảo
    fg: '#064E3B',
    badgeColor: '#059669',
    borderColor: '#6EE7B7'
  }
};

// Màu phân biệt độ ưu tiên chuẩn hình ảnh
const PRIO_STYLE = {
  'P1': { color: '#DC2626', label: '[P1]', weight: 1 }, // Đỏ rực
  'P2': { color: '#EA580C', label: '[P2]', weight: 2 }, // Cam
  'P3': { color: '#2563EB', label: '[P3]', weight: 3 }, // Xanh dương
  'P4': { color: '#64748B', label: '[P4]', weight: 4 }  // Xám
};

// Màu Pastel mờ nhẹ của 3 cột tháng (Background Canvas)
const MONTH_BG = {
  m10: '#F1F5F9', // Xanh xám nhạt mờ
  m11: '#FAF5FF', // Tím nhạt mờ
  m12: '#F0FDF4'  // Xanh ngọc nhạt mờ
};

/**
 * Menu tùy chỉnh khi mở Google Sheet
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 PRODUCT ROADMAP')
    .addItem('🔄 Cập nhật Roadmap Realtime Ngay', 'syncRoadmapFromBacklog')
    .addSeparator()
    .addItem('⏰ Kích hoạt Tự Động Cập Nhật Định Kỳ (Mỗi 10 phút)', 'setupAutoTrigger')
    .addToUi();
}

/**
 * Thiết lập Trigger chạy tự động định kỳ
 */
function setupAutoTrigger() {
  const triggers = ScriptApp.getProjectTriggers();
  for (let i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'syncRoadmapFromBacklog') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }
  ScriptApp.newTrigger('syncRoadmapFromBacklog')
    .timeBased()
    .everyMinutes(10)
    .create();
  
  SpreadsheetApp.getActiveSpreadsheet().toast('Đã kích hoạt tự động đồng bộ mỗi 10 phút!', 'Thành công', 5);
}

/**
 * Hàm lõi: Đồng bộ dữ liệu và vẽ lại Roadmap
 */
function syncRoadmapFromBacklog() {
  const activeSS = SpreadsheetApp.getActiveSpreadsheet();
  activeSS.toast('Đang kết nối và đồng bộ dữ liệu từ Backlog gốc...', 'Đang xử lý', 5);

  let sourceSS;
  try {
    sourceSS = SpreadsheetApp.openById(SOURCE_SPREADSHEET_ID);
  } catch (e) {
    activeSS.toast('Không thể mở file Backlog gốc: ' + e.message, 'Lỗi', 10);
    return;
  }

  const sheets = sourceSS.getSheets();
  const sourceSheet = sheets.find(s => s.getSheetId() === SOURCE_GID) || sheets[0];
  const sourceData = sourceSheet.getDataRange().getValues();

  // 1. Tìm dòng tiêu đề (Header row)
  let headerRowIdx = -1;
  for (let r = 0; r < Math.min(10, sourceData.length); r++) {
    const rowStr = sourceData[r].map(c => String(c).trim()).join('|');
    if (rowStr.includes('US Title') && rowStr.includes('Timeline')) {
      headerRowIdx = r;
      break;
    }
  }

  if (headerRowIdx === -1) {
    activeSS.toast('Không tìm thấy dòng tiêu đề trong sheet gốc!', 'Lỗi', 10);
    return;
  }

  const headers = sourceData[headerRowIdx].map(h => String(h).trim());
  const colMap = {};
  headers.forEach((h, idx) => {
    if (h.includes('US Title')) colMap['title'] = idx;
    else if (h.includes('EPIC')) colMap['epic'] = idx;
    else if (h.includes('Acceptance') || h.includes('Mô tả')) colMap['desc'] = idx;
    else if (h.includes('Ưu tiên')) colMap['prio'] = idx;
    else if (h.includes('PIC (BA)')) colMap['pic'] = idx;
    else if (h.includes('Trạng thái')) colMap['status'] = idx;
    else if (h.includes('Timeline')) colMap['timeline'] = idx;
  });

  // 2. Trích xuất và lọc các task Quý 4 (Không lấy Done / Pending)
  const q4Tasks = [];
  for (let r = headerRowIdx + 1; r < sourceData.length; r++) {
    const row = sourceData[r];
    const titleFull = String(row[colMap['title']] || '').trim();
    if (!titleFull) continue;

    const timeline = String(row[colMap['timeline']] || '').trim();
    const status = String(row[colMap['status']] || '').trim();
    const epic = String(row[colMap['epic']] || '').trim();
    const prio = String(row[colMap['prio']] || 'P2').trim();
    const pic = String(row[colMap['pic']] || '').trim();
    const rawDesc = String(row[colMap['desc']] || '').trim();

    const isQ4 = timeline.includes('Tháng 10') || timeline.includes('Tháng 11') || timeline.includes('Tháng 12');
    const isExcluded = status.toLowerCase() === 'done' || status.toLowerCase() === 'pending';

    if (isQ4 && !isExcluded) {
      let timeGroup = '';
      let startM = 10, endM = 10;
      if (timeline.includes('Tháng 10') && timeline.includes('Tháng 11')) {
        timeGroup = 'span-10-11';
        startM = 10; endM = 11;
      } else if (timeline.includes('Tháng 11') && timeline.includes('Tháng 12')) {
        timeGroup = 'span-11-12';
        startM = 11; endM = 12;
      } else if (timeline.includes('Tháng 10')) {
        timeGroup = 't10';
        startM = 10; endM = 10;
      } else if (timeline.includes('Tháng 11')) {
        timeGroup = 't11';
        startM = 11; endM = 11;
      } else if (timeline.includes('Tháng 12')) {
        timeGroup = 't12';
        startM = 12; endM = 12;
      }

      // Xử lý detail rút gọn (1 câu súc tích)
      let cleanDesc = rawDesc.split('\n')[0].trim();
      if (cleanDesc.startsWith('Tài liệu:')) {
        cleanDesc = 'Quy chuẩn tài liệu phân tích kỹ thuật và nghiệm thu UAT/CSOC';
      } else if (cleanDesc.startsWith('http')) {
        cleanDesc = 'Quy chuẩn cấu hình trang landing page và tích hợp hệ thống';
      } else if (!cleanDesc) {
        cleanDesc = 'Triển khai tính năng và phối hợp tích hợp theo yêu cầu';
      }
      if (cleanDesc.length > 60) {
        cleanDesc = cleanDesc.substring(0, 57) + '...';
      }

      q4Tasks.push({
        title: titleFull.split('\n')[0].trim(),
        epic: epic,
        desc: cleanDesc,
        prio: prio,
        pic: pic,
        status: status,
        timeline: timeline,
        timeGroup: timeGroup,
        startM: startM,
        endM: endM
      });
    }
  }

  // 3. Sắp xếp ưu tiên P1 ➔ P2 ➔ P3 ➔ P4 trong từng nhóm mốc thời gian
  const timeOrder = ['t10', 'span-10-11', 't11', 'span-11-12', 't12'];
  const sortedTasks = [];
  timeOrder.forEach(grp => {
    const subTasks = q4Tasks.filter(t => t.timeGroup === grp);
    subTasks.sort((a, b) => ((PRIO_STYLE[a.prio] ? PRIO_STYLE[a.prio].weight : 99) - (PRIO_STYLE[b.prio] ? PRIO_STYLE[b.prio].weight : 99)));
    sortedTasks.push(...subTasks);
  });

  // 4. Chuẩn bị Sheet Roadmap
  let roadmapSheet = activeSS.getSheetByName(ROADMAP_SHEET_NAME);
  if (!roadmapSheet) {
    roadmapSheet = activeSS.insertSheet(ROADMAP_SHEET_NAME, 0);
  } else {
    roadmapSheet.clear();
  }
  roadmapSheet.activate();

  // ẨN ĐƯỜNG CHỈ (GRIDLINES) ĐỂ BẢNG PHẲNG MỊN NHƯ CANVAS BẢN THIẾT KẾ
  // roadmapSheet.setHideGridlines(true);

  // Đặt chiều rộng cột (Cột A-B: Tháng 10, Cột C-D: Tháng 11, Cột E-F: Tháng 12)
  roadmapSheet.setColumnWidth(1, 280); // A
  roadmapSheet.setColumnWidth(2, 280); // B
  roadmapSheet.setColumnWidth(3, 280); // C
  roadmapSheet.setColumnWidth(4, 280); // D
  roadmapSheet.setColumnWidth(5, 280); // E
  roadmapSheet.setColumnWidth(6, 280); // F

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange("A1:F1");
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 38);

  // ===== DÒNG 2: DÒNG GHI CHÚ DUY NHẤT (THEO YÊU CẦU 5) =====
  const noteRange = roadmapSheet.getRange("A2:F2");
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9.5).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 24);

  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MÀU ĐẬM TƯƠNG ỨNG CỘT, CHỮ TRẮNG - THEO YÊU CẦU 4) =====
  // Tháng 10 (Cột A-B): Xanh đậm
  const m10Header = roadmapSheet.getRange("A3:B3");
  m10Header.merge();
  m10Header.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Header.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#1E3A8A", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11 (Cột C-D): Tím đậm
  const m11Header = roadmapSheet.getRange("C3:D3");
  m11Header.merge();
  m11Header.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Header.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12 (Cột E-F): Xanh ngọc đậm
  const m12Header = roadmapSheet.getRange("E3:F3");
  m12Header.merge();
  m12Header.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Header.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 32);

  // ===== VẼ CÁC TASK DÒNG =====
  const startRow = 4;
  const numTasks = sortedTasks.length;

  // 1. Tô màu Pastel mờ nhẹ nền cột cho toàn bộ thân bảng và đóng khung 3 tháng
  // Cột A-B: Tháng 10
  const m10Body = roadmapSheet.getRange(startRow, 1, numTasks, 2);
  m10Body.setBackground(MONTH_BG.m10)
    .setBorder(false, true, true, true, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Cột C-D: Tháng 11
  const m11Body = roadmapSheet.getRange(startRow, 3, numTasks, 2);
  m11Body.setBackground(MONTH_BG.m11)
    .setBorder(false, true, true, true, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Cột E-F: Tháng 12
  const m12Body = roadmapSheet.getRange(startRow, 5, numTasks, 2);
  m12Body.setBackground(MONTH_BG.m12)
    .setBorder(false, true, true, true, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // 2. Render từng task với layout 2 bên (Trái: Nội dung | Phải: Prio + PIC/Status)
  let curRow = startRow;
  sortedTasks.forEach(t => {
    roadmapSheet.setRowHeight(curRow, 38); // Giảm chiều cao gọn gàng theo yêu cầu 3

    const cfg = STATUS_CONFIG[t.status] || STATUS_CONFIG['Chưa tiếp nhận'];
    const prioCfg = PRIO_STYLE[t.prio] || PRIO_STYLE['P2'];

    // PHẦN BÊN TRÁI: Tên Task & Detail rút gọn
    const epicTag = `[${t.epic}]`;
    const leftLine1 = `${epicTag} ${t.title}`;
    const leftLine2 = `📝 ${t.desc}`;
    const leftFullText = `${leftLine1}\n${leftLine2}`;

    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftFullText);
    // [EPIC]: Xanh Navy, Bold
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9).setForegroundColor("#1E40AF").build()
    );
    // Tên task: Đen than, Bold
    leftBuilder.setTextStyle(epicTag.length + 1, leftLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9).setForegroundColor("#0F172A").build()
    );
    // Detail rút gọn: Nghiêng, Xám ghi
    const detailStart = leftLine1.length + 1;
    leftBuilder.setTextStyle(detailStart, detailStart + leftLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8).setForegroundColor("#475569").build()
    );
    const leftRichText = leftBuilder.build();

    // PHẦN BÊN PHẢI (GÓC PHẢI TRÊN & GÓC PHẢI DƯỚI - THEO YÊU CẦU 1 & 2):
    // Dòng 1 (Góc phải trên): [P1]
    // Dòng 2 (Góc phải dưới): 👤 PIC  ● Trạng thái
    const rightLine1 = prioCfg.label;
    const rightLine2 = `👤 ${t.pic}  ● ${t.status}`;
    const rightFullText = `${rightLine1}\n${rightLine2}`;

    const rightBuilder = SpreadsheetApp.newRichTextValue().setText(rightFullText);
    // Dòng 1: [P1] -> Màu sắc nổi bật theo độ ưu tiên, Bold, Size 9.5
    rightBuilder.setTextStyle(0, rightLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor(prioCfg.color).build()
    );
    // Dòng 2: PIC & Trạng thái -> Size 8, Căn phải
    const rLine2Start = rightLine1.length + 1;
    rightBuilder.setTextStyle(rLine2Start, rLine2Start + rightLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(8).setForegroundColor("#334155").build()
    );
    // Màu trạng thái
    const statusStart = rightFullText.lastIndexOf(t.status);
    if (statusStart !== -1) {
      rightBuilder.setTextStyle(statusStart, statusStart + t.status.length,
        SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8).setForegroundColor(cfg.badgeColor).build()
      );
    }
    const rightRichText = rightBuilder.build();

    // XÁC ĐỊNH VÙNG Ô TRÁI VÀ Ô PHẢI TRONG THANH TASK
    let leftRange, rightRange;
    if (t.timeGroup === 't10') {
      leftRange = roadmapSheet.getRange(curRow, 1, 1, 1);  // Ô A
      rightRange = roadmapSheet.getRange(curRow, 2, 1, 1); // Ô B
    } else if (t.timeGroup === 'span-10-11') {
      roadmapSheet.getRange(curRow, 1, 1, 3).merge();
      leftRange = roadmapSheet.getRange(curRow, 1, 1, 3);  // Ô A:C
      rightRange = roadmapSheet.getRange(curRow, 4, 1, 1); // Ô D
    } else if (t.timeGroup === 't11') {
      leftRange = roadmapSheet.getRange(curRow, 3, 1, 1);  // Ô C
      rightRange = roadmapSheet.getRange(curRow, 4, 1, 1); // Ô D
    } else if (t.timeGroup === 'span-11-12') {
      roadmapSheet.getRange(curRow, 3, 1, 3).merge();
      leftRange = roadmapSheet.getRange(curRow, 3, 1, 3);  // Ô C:E
      rightRange = roadmapSheet.getRange(curRow, 6, 1, 1); // Ô F
    } else if (t.timeGroup === 't12') {
      leftRange = roadmapSheet.getRange(curRow, 5, 1, 1);  // Ô E
      rightRange = roadmapSheet.getRange(curRow, 6, 1, 1); // Ô F
    }

    // ĐỊNH DẠNG Ô TRÁI (NỘI DUNG)
    leftRange.setRichTextValue(leftRichText);
    leftRange.setWrap(false);
    leftRange.setBackground(cfg.bg);
    leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
    // Viền ngoài: Top, Left, Bottom (Bỏ viền Right để liền khối với Ô Phải)
    leftRange.setBorder(true, true, true, false, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

    // ĐỊNH DẠNG Ô PHẢI (GÓC PHẢI TRÊN [P1] & GÓC PHẢI DƯỚI PIC/STATUS)
    rightRange.setRichTextValue(rightRichText);
    rightRange.setWrap(false);
    rightRange.setBackground(cfg.bg);
    rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
    // Viền ngoài: Top, Right, Bottom (Bỏ viền Left để liền khối với Ô Trái)
    rightRange.setBorder(true, false, true, true, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

    curRow++;
  });

  // Footer
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 6);
  footerRange.merge();
  footerRange.setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)  |  FPT Telecom Online Business  |  Cập nhật: " + Utilities.formatDate(new Date(), "GMT+7", "HH:mm dd/MM/yyyy"));
  footerRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B");
  footerRange.setHorizontalAlignment("center").setVerticalAlignment("middle").setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(curRow, 24);

  // 5. Cập nhật Sheet Dữ Liệu Đồng Bộ Backlog (Tra cứu chi tiết)
  let syncSheet = activeSS.getSheetByName(BACKLOG_SYNC_SHEET_NAME);
  if (!syncSheet) {
    syncSheet = activeSS.insertSheet(BACKLOG_SYNC_SHEET_NAME);
  } else {
    syncSheet.clear();
  }

  const syncTitle = syncSheet.getRange("A1:I1");
  syncTitle.merge();
  syncTitle.setValue("DANH SÁCH CHI TIẾT USER STORIES (ĐỒNG BỘ REALTIME TỪ GOOGLE SHEET GỐC)")
    .setFontFamily("Times New Roman").setFontSize(14).setFontWeight("bold").setFontColor("#005696")
    .setHorizontalAlignment("left").setVerticalAlignment("middle");

  const syncHeaders = ["STT", "Hệ thống", "User Story / Đầu mục công việc", "Detail rút gọn", "Ưu tiên", "PIC", "Trạng thái", "Timeline", "Ghi chú tiến trình"];
  syncSheet.getRange("A3:I3").setValues([syncHeaders])
    .setFontFamily("Times New Roman").setFontSize(10).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#005696").setHorizontalAlignment("center").setVerticalAlignment("middle");

  const syncRows = sortedTasks.map((t, idx) => {
    const note = t.timeGroup.startsWith('span') ? `Vắt từ T${t.startM} sang T${t.endM}` : `Hoàn thành trong T${t.endM}`;
    return [idx + 1, `[${t.epic}]`, t.title, t.desc, t.prio, t.pic, t.status, t.timeline, note];
  });

  if (syncRows.length > 0) {
    syncSheet.getRange(4, 1, syncRows.length, 9).setValues(syncRows)
      .setFontFamily("Times New Roman").setFontSize(9.5).setHorizontalAlignment("left").setVerticalAlignment("middle");
    
    for (let r = 0; r < syncRows.length; r++) {
      const st = syncRows[r][6];
      const cfg = STATUS_CONFIG[st] || STATUS_CONFIG['Chưa tiếp nhận'];
      const prioVal = syncRows[r][4];
      const prioCfg = PRIO_STYLE[prioVal] || PRIO_STYLE['P2'];

      syncSheet.getRange(r + 4, 7).setBackground(cfg.bg).setFontColor(cfg.fg).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 5).setFontColor(prioCfg.color).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 6).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  activeSS.toast(`Đã đồng bộ thành công ${q4Tasks.length} task từ Backlog gốc!`, 'Hoàn tất', 5);
}

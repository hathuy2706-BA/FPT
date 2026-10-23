/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V7 (DYNAMIC PROGRESS BAR & COLOR BADGES)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * Các nâng cấp V7 chuẩn xác 100% theo hình ảnh người dùng gửi:
 * 1. THANH TIẾN TRÌNH THEO TRẠNG THÁI (DYNAMIC PROGRESS BAR):
 *    - Mỗi tháng chia làm 8 nấc (8 cột con x 75px = 600px).
 *    - Chiều dài thanh màu chạy từ trái sang phải theo đúng tỷ lệ % trạng thái:
 *      * 1. Chưa tiếp nhận: 1/8 = 12.5% (1 cột màu, 7 cột trắng)
 *      * 2. Đã tiếp nhận: 2/8 = 25.0% (2 cột màu, 6 cột trắng)
 *      * 3. Đang phân tích: 3/8 = 37.5% (3 cột màu, 5 cột trắng)
 *      * 4. PO reviewed: 4/8 = 50.0% (4 cột màu, 4 cột trắng)
 *      * 5. DEV In Progress: 5/8 = 62.5% (5 cột màu vàng, 3 cột trắng) -> như task MENU trong hình
 *      * 6. UAT: 6/8 = 75.0% (6 cột màu tím, 2 cột trắng) -> như task Quản lý trang trong hình
 *      * 7. QC/CSOC: 7/8 = 87.5% (7 cột màu xanh, 1 cột trắng)
 *      * 8. Done: 8/8 = 100.0% (8 cột màu xanh lá)
 *    - Vùng màu bên trái chứa: [Hệ thống] Tên Task & 👤 PIC.
 *    - Vùng nền trắng bên phải chứa: Độ ưu tiên ở góc trên, Trạng thái ở góc dưới.
 * 2. TÔ MÀU ĐỒNG BỘ CHO HỆ THỐNG & ĐỘ ƯU TIÊN:
 *    - [Web, CMS]: Màu xanh ngọc đậm #059669
 *    - [CMS]: Màu xanh tím #4F46E5
 *    - [Web]: Màu xanh da trời #0284C7
 *    - [P1]: Màu đỏ rực #DC2626
 *    - [P2]: Màu cam đậm #EA580C
 *    - [P3]: Màu xanh dương #2563EB
 *    - [P4]: Màu xám #64748B
 * 3. TẮT HOÀN TOÀN TẤT CẢ ĐƯỜNG CHỈ LƯỚI TRONG TOÀN BỘ SHEET.
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// 8 nấc trạng thái chuẩn vòng đời (12.5% mỗi nấc)
const STATUS_STEPS = {
  'Chưa tiếp nhận': { step: 1, percent: '12.5%', bg: '#E2E8F0', fg: '#1E293B', badgeColor: '#475569', borderColor: '#CBD5E1' },
  'Đã tiếp nhận yêu cầu': { step: 2, percent: '25.0%', bg: '#E9D5FF', fg: '#581C87', badgeColor: '#6B21A8', borderColor: '#D8B4FE' },
  'Đang phân tích/Document': { step: 3, percent: '37.5%', bg: '#FED7AA', fg: '#7C2D12', badgeColor: '#C2410C', borderColor: '#FDBA74' },
  'PO reviewed/Transfer DEV': { step: 4, percent: '50.0%', bg: '#BBF7D0', fg: '#14532D', badgeColor: '#15803D', borderColor: '#86EFAC' },
  'PO reviewed': { step: 4, percent: '50.0%', bg: '#BBF7D0', fg: '#14532D', badgeColor: '#15803D', borderColor: '#86EFAC' },
  'DEV In Progress': { step: 5, percent: '62.5%', bg: '#FEF08A', fg: '#713F12', badgeColor: '#A16207', borderColor: '#FDE047' },
  'UAT': { step: 6, percent: '75.0%', bg: '#DDD6FE', fg: '#3B0764', badgeColor: '#581C87', borderColor: '#C4B5FD' },
  'QC/CSOC': { step: 7, percent: '87.5%', bg: '#BAE6FD', fg: '#0C4A6E', badgeColor: '#0284C7', borderColor: '#7DD3FC' },
  'Done': { step: 8, percent: '100.0%', bg: '#A7F3D0', fg: '#064E3B', badgeColor: '#059669', borderColor: '#6EE7B7' }
};

// Màu phân biệt độ ưu tiên chuẩn hình ảnh
const PRIO_STYLE = {
  'P1': { color: '#DC2626', label: 'P1', weight: 1 }, // Đỏ rực
  'P2': { color: '#EA580C', label: 'P2', weight: 2 }, // Cam
  'P3': { color: '#2563EB', label: 'P3', weight: 3 }, // Xanh dương
  'P4': { color: '#64748B', label: 'P4', weight: 4 }  // Xám
};

// Màu Hệ thống chuẩn hình ảnh
function getEpicColor(epic) {
  if (epic.includes('Web') && epic.includes('CMS')) return '#059669'; // Xanh ngọc
  if (epic.includes('CMS')) return '#4F46E5';                         // Xanh tím Indigo
  return '#0284C7';                                                   // Xanh da trời
}

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

      q4Tasks.push({
        title: titleFull.split('\n')[0].trim(),
        epic: epic,
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

  // TẮT HOÀN TOÀN CÁC ĐƯỜNG CHỈ / ĐƯỜNG LƯỚI TRÊN SHEET
  roadmapSheet.setHiddenGridlines(true);

  // ĐẶT ĐỘ RỘNG CHO 24 CỘT TIẾN ĐỘ (8 CỘT/THÁNG x 75px = 600px/THÁNG)
  for (let c = 1; c <= 24; c++) {
    roadmapSheet.setColumnWidth(c, 75);
  }

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange(1, 1, 1, 24);
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 38);

  // ===== DÒNG 2: GHI CHÚ HOT REQUEST =====
  const noteRange = roadmapSheet.getRange(2, 1, 1, 24);
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9.5).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 24);

  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MỖI THÁNG MERGE 8 CỘT) =====
  // Tháng 10: Cột 1 đến 8 (A đến H)
  const m10Header = roadmapSheet.getRange(3, 1, 1, 8);
  m10Header.merge();
  m10Header.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Header.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#1E3A8A", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11: Cột 9 đến 16 (I đến P)
  const m11Header = roadmapSheet.getRange(3, 9, 1, 8);
  m11Header.merge();
  m11Header.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Header.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12: Cột 17 đến 24 (Q đến X)
  const m12Header = roadmapSheet.getRange(3, 17, 1, 8);
  m12Header.merge();
  m12Header.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Header.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 32);

  // ===== VẼ CÁC TASK DÒNG =====
  const startRow = 4;
  const numTasks = sortedTasks.length;

  // 1. TÔ NỀN PASTEL MỜ PHẲNG LÌ CHO TOÀN BỘ 3 THÁNG
  // Xóa toàn bộ đường chỉ bên trong, chỉ giữ ranh giới phân định giữa 3 tháng
  const m10Body = roadmapSheet.getRange(startRow, 1, numTasks, 8);
  m10Body.setBackground(MONTH_BG.m10)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m11Body = roadmapSheet.getRange(startRow, 9, numTasks, 8);
  m11Body.setBackground(MONTH_BG.m11)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m12Body = roadmapSheet.getRange(startRow, 17, numTasks, 8);
  m12Body.setBackground(MONTH_BG.m12)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // 2. Render từng task với THANH TIẾN TRÌNH THEO % TRẠNG THÁI
  let curRow = startRow;
  sortedTasks.forEach(t => {
    roadmapSheet.setRowHeight(curRow, 38);

    const cfg = STATUS_STEPS[t.status] || STATUS_STEPS['Chưa tiếp nhận'];
    const prioCfg = PRIO_STYLE[t.prio] || PRIO_STYLE['P2'];
    const epicColor = getEpicColor(t.epic);

    // Xác định phạm vi cột của task (1 tháng = 8 cột; 2 tháng = 16 cột)
    let startCol = 1, totalCols = 8;
    if (t.timeGroup === 't10') {
      startCol = 1; totalCols = 8;
    } else if (t.timeGroup === 'span-10-11') {
      startCol = 1; totalCols = 16;
    } else if (t.timeGroup === 't11') {
      startCol = 9; totalCols = 8;
    } else if (t.timeGroup === 'span-11-12') {
      startCol = 9; totalCols = 16;
    } else if (t.timeGroup === 't12') {
      startCol = 17; totalCols = 8;
    }

    // TÍNH TOÁN SỐ CỘT CÓ MÀU THEO % TRẠNG THÁI:
    // 1 task = 100% chia 8 nấc (12.5% mỗi nấc)
    let coloredCols = Math.round((cfg.step / 8) * totalCols);
    if (coloredCols < 1) coloredCols = 1;
    if (coloredCols > totalCols) coloredCols = totalCols;
    const whiteCols = totalCols - coloredCols;

    // NỘI DUNG VÙNG TRÁI (VÙNG CÓ MÀU TIẾN TRÌNH):
    // Dòng 1: [Hệ thống] Tên Task
    // Dòng 2: 👤 PIC
    const epicTag = `[${t.epic}]`;
    const leftLine1 = `${epicTag} ${t.title}`;
    const leftLine2 = `👤 ${t.pic}`;
    const leftText = `${leftLine1}\n${leftLine2}`;

    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftText);
    // Tô màu Hệ thống: Màu đặc trưng (Xanh ngọc / Xanh tím / Xanh dương), Bold
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor(epicColor).build()
    );
    // Tên task: Đen than, Bold
    leftBuilder.setTextStyle(epicTag.length + 1, leftLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor("#0F172A").build()
    );
    // PIC: Xám than
    const picStart = leftLine1.length + 1;
    leftBuilder.setTextStyle(picStart, picStart + leftLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(8.5).setForegroundColor("#334155").build()
    );
    const leftRichText = leftBuilder.build();

    // NỘI DUNG VÙNG PHẢI (VÙNG NỀN TRẮNG CHƯA HOÀN THÀNH):
    // Dòng 1: [P1] (Tô màu độ ưu tiên: Đỏ P1 / Cam P2 / Xanh P3)
    // Dòng 2: Trạng thái (Tô màu badge trạng thái)
    const rightLine1 = prioCfg.label;
    const rightLine2 = t.status;
    const rightText = `${rightLine1}\n${rightLine2}`;

    const rightBuilder = SpreadsheetApp.newRichTextValue().setText(rightText);
    // Tô màu Độ ưu tiên
    rightBuilder.setTextStyle(0, rightLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor(prioCfg.color).build()
    );
    // Tô màu Trạng thái
    const statusStart = rightLine1.length + 1;
    rightBuilder.setTextStyle(statusStart, statusStart + rightLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8.5).setForegroundColor(cfg.badgeColor).build()
    );
    const rightRichText = rightBuilder.build();

    // RENDER LÊN SHEET:
    if (whiteCols > 0) {
      // 1. Vùng có màu (tiến trình):
      const leftRange = roadmapSheet.getRange(curRow, startCol, 1, coloredCols);
      leftRange.merge();
      leftRange.setRichTextValue(leftRichText);
      leftRange.setWrap(false);
      leftRange.setBackground(cfg.bg);
      leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
      leftRange.setBorder(true, true, true, false, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

      // 2. Vùng nền trắng (góc phải):
      const rightRange = roadmapSheet.getRange(curRow, startCol + coloredCols, 1, whiteCols);
      rightRange.merge();
      rightRange.setRichTextValue(rightRichText);
      rightRange.setWrap(false);
      rightRange.setBackground("#FFFFFF");
      rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
      rightRange.setBorder(true, false, true, true, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
    } else {
      // Đã hoàn thành 100% (Done): Toàn bộ có màu xanh
      const fullRange = roadmapSheet.getRange(curRow, startCol, 1, totalCols);
      fullRange.merge();
      // Hiển thị cả 2 bên
      const combinedText = `${leftLine1}    ${rightLine1}\n${leftLine2}    ${rightLine2}`;
      fullRange.setValue(combinedText);
      fullRange.setFontFamily("Times New Roman").setFontSize(9).setWrap(false);
      fullRange.setBackground(cfg.bg);
      fullRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
      fullRange.setBorder(true, true, true, true, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
    }

    curRow++;
  });

  // Footer
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 24);
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

  const syncHeaders = ["STT", "Hệ thống", "User Story / Đầu mục công việc", "Tiến độ", "Ưu tiên", "PIC", "Trạng thái", "Timeline", "Ghi chú tiến trình"];
  syncSheet.getRange("A3:I3").setValues([syncHeaders])
    .setFontFamily("Times New Roman").setFontSize(10).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#005696").setHorizontalAlignment("center").setVerticalAlignment("middle");

  const syncRows = sortedTasks.map((t, idx) => {
    const cfg = STATUS_STEPS[t.status] || STATUS_STEPS['Chưa tiếp nhận'];
    const note = t.timeGroup.startsWith('span') ? `Vắt từ T${t.startM} sang T${t.endM}` : `Hoàn thành trong T${t.endM}`;
    return [idx + 1, `[${t.epic}]`, t.title, cfg.percent, t.prio, t.pic, t.status, t.timeline, note];
  });

  if (syncRows.length > 0) {
    syncSheet.getRange(4, 1, syncRows.length, 9).setValues(syncRows)
      .setFontFamily("Times New Roman").setFontSize(9.5).setHorizontalAlignment("left").setVerticalAlignment("middle");
    
    for (let r = 0; r < syncRows.length; r++) {
      const st = syncRows[r][6];
      const cfg = STATUS_STEPS[st] || STATUS_STEPS['Chưa tiếp nhận'];
      const prioVal = syncRows[r][4];
      const prioCfg = PRIO_STYLE[prioVal] || PRIO_STYLE['P2'];

      syncSheet.getRange(r + 4, 7).setBackground(cfg.bg).setFontColor(cfg.fg).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 5).setFontColor(prioCfg.color).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 4).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 6).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  activeSS.toast(`Đã đồng bộ thành công ${q4Tasks.length} task từ Backlog gốc!`, 'Hoàn tất', 5);
}

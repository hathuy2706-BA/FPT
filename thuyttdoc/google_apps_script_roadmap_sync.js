/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE (CHUẨN APPS SCRIPT SPREADSHEET API)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// Cấu hình 8 trạng thái chuẩn vòng đời từ trên xuống (chia 8 phần bằng nhau = 12.5% mỗi nấc)
const STATUS_CONFIG = {
  'Chưa tiếp nhận': {
    step: '1/8 (12.5%)',
    bg: '#D2E4E6',
    fg: '#214349',
    borderColor: '#B0CCD0'
  },
  'Đã tiếp nhận yêu cầu': {
    step: '2/8 (25.0%)',
    bg: '#E6DCF5',
    fg: '#4F378B',
    borderColor: '#D3C3EE'
  },
  'Đang phân tích/Document': {
    step: '3/8 (37.5%)',
    bg: '#FCD5B5',
    fg: '#80350B',
    borderColor: '#F8B88B'
  },
  'PO reviewed/Transfer DEV': {
    step: '4/8 (50.0%)',
    bg: '#D1F2D9',
    fg: '#1B5E20',
    borderColor: '#A8E6B8'
  },
  'PO reviewed': {
    step: '4/8 (50.0%)',
    bg: '#D1F2D9',
    fg: '#1B5E20',
    borderColor: '#A8E6B8'
  },
  'DEV In Progress': {
    step: '5/8 (62.5%)',
    bg: '#FEF08A',
    fg: '#78350F',
    borderColor: '#FDE047'
  },
  'UAT': {
    step: '6/8 (75.0%)',
    bg: '#581C87',
    fg: '#FFFFFF',
    borderColor: '#4A154B'
  },
  'QC/CSOC': {
    step: '7/8 (87.5%)',
    bg: '#005696',
    fg: '#FFFFFF',
    borderColor: '#004070'
  },
  'Done': {
    step: '8/8 (100.0%)',
    bg: '#166534',
    fg: '#FFFFFF',
    borderColor: '#14532D'
  }
};

const PRIO_WEIGHT = { 'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4 };

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

  // 3. Tự động tính toán số liệu Metric
  const totalCount = q4Tasks.length;
  const multiMonthCount = q4Tasks.filter(t => t.timeGroup.startsWith('span')).length;
  const t10Count = q4Tasks.filter(t => t.endM === 10).length;
  const t11Count = q4Tasks.filter(t => t.endM === 11).length;
  const t12Count = q4Tasks.filter(t => t.endM === 12).length;

  // 4. Sắp xếp ưu tiên P1 ➔ P2 ➔ P3 ➔ P4 trong từng nhóm mốc thời gian
  const timeOrder = ['t10', 'span-10-11', 't11', 'span-11-12', 't12'];
  const sortedTasks = [];
  timeOrder.forEach(grp => {
    const subTasks = q4Tasks.filter(t => t.timeGroup === grp);
    subTasks.sort((a, b) => (PRIO_WEIGHT[a.prio] || 99) - (PRIO_WEIGHT[b.prio] || 99));
    sortedTasks.push(...subTasks);
  });

  // 5. Chuẩn bị Sheet Roadmap
  let roadmapSheet = activeSS.getSheetByName(ROADMAP_SHEET_NAME);
  if (!roadmapSheet) {
    roadmapSheet = activeSS.insertSheet(ROADMAP_SHEET_NAME, 0);
  } else {
    roadmapSheet.clear();
  }
  roadmapSheet.activate();

  // Đặt chiều rộng cột (Cột A-B: Tháng 10, Cột C-D: Tháng 11, Cột E-F: Tháng 12)
  roadmapSheet.setColumnWidth(1, 260); // A
  roadmapSheet.setColumnWidth(2, 260); // B
  roadmapSheet.setColumnWidth(3, 260); // C
  roadmapSheet.setColumnWidth(4, 260); // D
  roadmapSheet.setColumnWidth(5, 260); // E
  roadmapSheet.setColumnWidth(6, 260); // F

  // ===== HEADER DÒNG 1 =====
  const titleRange = roadmapSheet.getRange("A1:F1");
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  roadmapSheet.setRowHeight(1, 40);

  // DÒNG 2: Khối Metrics tự động
  const metricValues = [
    [
      `Tổng User Stories: ${totalCount}`,
      `Task Chạy Đa Tháng: ${multiMonthCount}`,
      `Hạn Tháng 10: ${t10Count}`,
      `Hạn Tháng 11: ${t11Count}`,
      `Hạn Tháng 12: ${t12Count}`,
      `Cập nhật lúc: ${Utilities.formatDate(new Date(), "GMT+7", "HH:mm dd/MM")}`
    ]
  ];
  const metricRange = roadmapSheet.getRange("A2:F2");
  metricRange.setValues(metricValues);
  metricRange.setFontFamily("Times New Roman").setFontSize(10).setFontWeight("bold");
  metricRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  metricRange.setBackground("#F8FAFC").setBorder(true, true, true, true, true, true, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID);
  roadmapSheet.setRowHeight(2, 28);

  // DÒNG 3: Legend 8 nấc trạng thái
  const legendRange = roadmapSheet.getRange("A3:F3");
  legendRange.merge();
  legendRange.setValue("CHUẨN 8 NẤC TIẾN ĐỘ VÒNG ĐỜI: 1. Chưa tiếp nhận (1/8) ➔ 2. Đã tiếp nhận (2/8) ➔ 3. Đang phân tích/Doc (3/8) ➔ 4. PO reviewed (4/8) ➔ 5. DEV In Progress (5/8) ➔ 6. UAT (6/8) ➔ 7. QC/CSOC (7/8) ➔ 8. Done (8/8)");
  legendRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#475569");
  legendRange.setHorizontalAlignment("center").setVerticalAlignment("middle").setBackground("#F1F5F9");
  roadmapSheet.setRowHeight(3, 24);

  // DÒNG 4: 3 CỘT THÁNG LỚN (ĐÃ BỎ SPRINT)
  const m10Range = roadmapSheet.getRange("A4:B4");
  m10Range.merge();
  m10Range.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Range.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle");

  const m11Range = roadmapSheet.getRange("C4:D4");
  m11Range.merge();
  m11Range.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Range.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle");

  const m12Range = roadmapSheet.getRange("E4:F4");
  m12Range.merge();
  m12Range.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Range.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle");
  roadmapSheet.setRowHeight(4, 32);

  // ===== VẼ CÁC TASK DÒNG =====
  let curRow = 5;
  sortedTasks.forEach(t => {
    roadmapSheet.setRowHeight(curRow, 46);
    
    // Nền trắng và viền cho toàn bộ 6 ô của dòng
    const rowRange = roadmapSheet.getRange(curRow, 1, 1, 6);
    rowRange.setBackground("#FFFFFF").setBorder(true, true, true, true, false, false, "#E2E8F0", SpreadsheetApp.BorderStyle.SOLID);

    const cfg = STATUS_CONFIG[t.status] || STATUS_CONFIG['Chưa tiếp nhận'];
    const content = `${t.epic} ${t.title} [${t.prio}]\n👤 PIC: ${t.pic}   |   Trạng thái: ${t.status} (${cfg.step})`;

    let targetRange;
    if (t.timeGroup === 't10') {
      targetRange = roadmapSheet.getRange(curRow, 1, 1, 2);
    } else if (t.timeGroup === 'span-10-11') {
      targetRange = roadmapSheet.getRange(curRow, 1, 1, 4);
    } else if (t.timeGroup === 't11') {
      targetRange = roadmapSheet.getRange(curRow, 3, 1, 2);
    } else if (t.timeGroup === 'span-11-12') {
      targetRange = roadmapSheet.getRange(curRow, 3, 1, 4);
    } else if (t.timeGroup === 't12') {
      targetRange = roadmapSheet.getRange(curRow, 5, 1, 2);
    }

    if (targetRange) {
      targetRange.merge();
      targetRange.setValue(content);
      targetRange.setFontFamily("Times New Roman").setFontSize(9.5).setWrap(true);
      targetRange.setBackground(cfg.bg).setFontColor(cfg.fg);
      targetRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
      targetRange.setBorder(true, true, true, true, true, true, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
    }

    curRow++;
  });

  // Footer
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 6);
  footerRange.merge();
  footerRange.setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)  |  FPT Telecom Online Business");
  footerRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B");
  footerRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  roadmapSheet.setRowHeight(curRow, 24);

  // 6. Tạo Sheet Dữ Liệu Đồng Bộ Backlog (Tra cứu chi tiết)
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

  const syncHeaders = ["STT", "EPIC", "User Story / Đầu mục công việc", "Ưu tiên", "PIC (BA)", "Trạng thái", "Tiến độ (8 nấc)", "Timeline mong muốn", "Ghi chú tiến trình"];
  syncSheet.getRange("A3:I3").setValues([syncHeaders])
    .setFontFamily("Times New Roman").setFontSize(10).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#005696").setHorizontalAlignment("center").setVerticalAlignment("middle");

  const syncRows = sortedTasks.map((t, idx) => {
    const cfg = STATUS_CONFIG[t.status] || STATUS_CONFIG['Chưa tiếp nhận'];
    const note = t.timeGroup.startsWith('span') ? `Vắt từ T${t.startM} sang T${t.endM}` : `Hoàn thành trong T${t.endM}`;
    return [idx + 1, t.epic, t.title, t.prio, t.pic, t.status, cfg.step, t.timeline, note];
  });

  if (syncRows.length > 0) {
    syncSheet.getRange(4, 1, syncRows.length, 9).setValues(syncRows)
      .setFontFamily("Times New Roman").setFontSize(9.5).setHorizontalAlignment("left").setVerticalAlignment("middle");
    
    for (let r = 0; r < syncRows.length; r++) {
      const st = syncRows[r][5];
      const cfg = STATUS_CONFIG[st] || STATUS_CONFIG['Chưa tiếp nhận'];
      syncSheet.getRange(r + 4, 6).setBackground(cfg.bg).setFontColor(cfg.fg).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 4).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 7).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  activeSS.toast(`Đã đồng bộ thành công ${totalCount} task từ Backlog gốc!`, 'Hoàn tất', 5);
}

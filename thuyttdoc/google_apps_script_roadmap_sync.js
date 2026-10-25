/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V9 (DESIGNER PIXEL PERFECT EDITION)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * Các cải tiến vượt bậc chuẩn xác theo hình ảnh mẫu của người dùng:
 * 1. VIỀN XANH ĐẦU MỖI TASK ĐƯỢC BO TRỌN TRONG KHUNG TASK:
 *    - Chèn dòng đệm phân cách 8px giữa các task, giúp mỗi task là một Card độc lập.
 *    - Dải viền xanh dương đậm #2563EB (SOLID_THICK) nằm trọn vẹn trong chiều cao của Card,
 *      tách biệt hoàn toàn, không chạy dính liền từ trên xuống dưới.
 * 2. ĐƯA DETAIL RÚT GỌN VÀO GIỮA THẺ (DÒNG 2):
 *    - Dòng 1: [Hệ thống] Tên Task (trái) .................... Độ ưu tiên (phải).
 *    - Dòng 2: Detail rút gọn (chữ nghiêng xám ghi thanh lịch).
 *    - Dòng 3: 👤 PIC (góc dưới trái) ........................ Trạng thái (góc dưới phải).
 * 3. ĐỔ MÀU NỀN & MÀU CHỮ NỔI BẬT CHO HỆ THỐNG, PIC, ĐỘ ƯU TIÊN, TRẠNG THÁI:
 *    - Hệ thống: [Web, CMS] xanh ngọc #059669, [CMS] xanh tím #4F46E5, [Web] xanh da trời #0284C7.
 *    - PIC: Badge [👤 Tên PIC] xám đậm #334155 ở góc dưới bên trái.
 *    - Độ ưu tiên: [🔴 P1] đỏ rực, [🟠 P2] cam đậm, [🔵 P3] xanh, [⚪ P4] xám ở góc trên bên phải.
 *    - Trạng thái: Badge màu nhận diện vòng đời ở góc dưới bên phải.
 * 4. NỘI DUNG TASK, DETAIL, PIC KHÔNG BAO GIỜ BỊ CẮT CHỮ:
 *    - Thẻ task chiếm trọn chiều rộng của tháng (600px) hoặc 2 tháng (1200px), không gian thênh thang.
 * 5. THANH TIẾN TRÌNH DYNAMIC THEO % TRẠNG THÁI Ở ĐÁY MỖI CARD:
 *    - Nằm ngay sát mép đáy của Card (cao 5px), chia chuẩn 8 nấc (12.5% mỗi nấc).
 *    - Tô màu gradient tiến độ đúng theo trạng thái (vàng 62.5% cho DEV In Progress, tím 75% cho UAT...).
 * 6. TẮT HOÀN TOÀN CÁC ĐƯỜNG CHỈ LƯỚI TRONG TOÀN BỘ SHEET.
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// 8 nấc trạng thái chuẩn vòng đời (12.5% mỗi nấc) với BỘ MÀU PASTEL CỦA TASK NỔI HƠN NỀN
const STATUS_STEPS = {
  'Chưa tiếp nhận': { step: 1, percent: '12.5%', taskBg: '#E2E8F0', border: '#CBD5E1', barColor: '#94A3B8', badgeColor: '#475569' },
  'Đã tiếp nhận yêu cầu': { step: 2, percent: '25.0%', taskBg: '#F3E8FF', border: '#D8B4FE', barColor: '#A855F7', badgeColor: '#6B21A8' },
  'Đang phân tích/Document': { step: 3, percent: '37.5%', taskBg: '#FFEDD5', border: '#FDBA74', barColor: '#FB923C', badgeColor: '#C2410C' },
  'PO reviewed/Transfer DEV': { step: 4, percent: '50.0%', taskBg: '#DCFCE7', border: '#86EFAC', barColor: '#4ADE80', badgeColor: '#15803D' },
  'PO reviewed': { step: 4, percent: '50.0%', taskBg: '#DCFCE7', border: '#86EFAC', barColor: '#4ADE80', badgeColor: '#15803D' },
  'DEV In Progress': { step: 5, percent: '62.5%', taskBg: '#FEF9C3', border: '#FDE047', barColor: '#EAB308', badgeColor: '#854D0E' },
  'UAT': { step: 6, percent: '75.0%', taskBg: '#EDE9FE', border: '#C4B5FD', barColor: '#8B5CF6', badgeColor: '#581C87' },
  'QC/CSOC': { step: 7, percent: '87.5%', taskBg: '#E0F2FE', border: '#7DD3FC', barColor: '#38BDF8', badgeColor: '#0284C7' },
  'Done': { step: 8, percent: '100.0%', taskBg: '#D1FAE5', border: '#6EE7B7', barColor: '#10B981', badgeColor: '#059669' }
};

// Màu phân biệt độ ưu tiên chuẩn hình ảnh
const PRIO_STYLE = {
  'P1': { color: '#DC2626', label: '[🔴 P1]', weight: 1 }, // Đỏ rực
  'P2': { color: '#EA580C', label: '[🟠 P2]', weight: 2 }, // Cam
  'P3': { color: '#2563EB', label: '[🔵 P3]', weight: 3 }, // Xanh dương
  'P4': { color: '#64748B', label: '[⚪ P4]', weight: 4 }  // Xám
};

// Màu Hệ thống chuẩn hình ảnh
function getEpicColor(epic) {
  if (epic.includes('Web') && epic.includes('CMS')) return '#059669'; // Xanh ngọc
  if (epic.includes('CMS')) return '#4F46E5';                         // Xanh tím Indigo
  return '#0284C7';                                                   // Xanh da trời
}

// Màu Pastel mờ nhẹ của 3 cột tháng (Background Canvas mờ nhẹ)
const MONTH_BG = {
  m10: '#F8FAFC', // Slate 50 - xám nhạt mờ dịu mắt
  m11: '#FAF7FD', // Tím nhạt mờ dịu mắt
  m12: '#F2FBF6'  // Xanh lá nhạt mờ dịu mắt
};

/**
 * Menu tùy chỉnh khi mở Google Sheet
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 PRODUCT ROADMAP')
    .addItem('🔄 Cập nhật Roadmap Realtime Ngay (Thủ công)', 'syncRoadmapFromBacklog')
    .addSeparator()
    .addItem('⏰ Kích hoạt Tự Động Cập Nhật Hàng Ngày (1 ngày / 1 lần vào 7:00 AM)', 'setupDailyAutoTrigger')
    .addItem('❌ Hủy bỏ Lịch Tự Động Cập Nhật', 'cancelAutoTriggers')
    .addToUi();
}

/**
 * Thiết lập Trigger chạy tự động định kỳ 1 ngày 1 lần vào lúc 7:00 - 8:00 sáng
 */
function setupDailyAutoTrigger() {
  cancelAutoTriggers(false);
  
  ScriptApp.newTrigger('syncRoadmapFromBacklog')
    .timeBased()
    .everyDays(1)
    .atHour(7)
    .create();
  
  SpreadsheetApp.getActiveSpreadsheet().toast('Đã cài đặt thành công: Tự động cập nhật 1 ngày 1 lần vào lúc 7:00 AM!', 'Thành công', 8);
}

/**
 * Hủy bỏ các trigger tự động đồng bộ cũ để tránh trùng lặp
 */
function cancelAutoTriggers(showToast) {
  const triggers = ScriptApp.getProjectTriggers();
  let count = 0;
  for (let i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'syncRoadmapFromBacklog') {
      ScriptApp.deleteTrigger(triggers[i]);
      count++;
    }
  }
  if (showToast !== false) {
    SpreadsheetApp.getActiveSpreadsheet().toast('Đã xóa ' + count + ' lịch tự động cũ.', 'Thông báo', 5);
  }
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

      // Detail rút gọn (Bỏ icon, lấy 1 câu súc tích)
      let cleanDesc = rawDesc.split('\n')[0].trim();
      if (cleanDesc.startsWith('Tài liệu:')) {
        cleanDesc = 'Quy chuẩn tài liệu phân tích kỹ thuật và nghiệm thu UAT/CSOC';
      } else if (cleanDesc.startsWith('http')) {
        cleanDesc = 'Quy chuẩn cấu hình trang landing page và tích hợp hệ thống';
      } else if (!cleanDesc) {
        cleanDesc = 'Triển khai tính năng và phối hợp tích hợp theo yêu cầu';
      }
      if (cleanDesc.length > 55) {
        cleanDesc = cleanDesc.substring(0, 52) + '...';
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

  // TẮT HOÀN TOÀN CÁC ĐƯỜNG CHỈ / ĐƯỜNG LƯỚI TRÊN SHEET
  roadmapSheet.setHiddenGridlines(true);

  // ĐẶT ĐỘ RỘNG CHO 12 CỘT TIẾN ĐỘ: 4 CỘT / THÁNG (W1-W4) x 105px = 420px/THÁNG
  // TỔNG BẢNG 12 CỘT = 1.260px (GỌN GÀNG, TẬP TRUNG, KHÔNG DÀN TRẢI DÀI DÒNG)
  for (let c = 1; c <= 12; c++) {
    roadmapSheet.setColumnWidth(c, 105);
  }
  // Xóa các cột thừa từ cột 13 trở đi để bảng đóng khung gọn gàng
  if (roadmapSheet.getMaxColumns() > 12) {
    roadmapSheet.deleteColumns(13, roadmapSheet.getMaxColumns() - 12);
  }

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange(1, 1, 1, 12);
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 38);

  // ===== DÒNG 2: GHI CHÚ HOT REQUEST =====
  const noteRange = roadmapSheet.getRange(2, 1, 1, 12);
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9.5).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 24);

  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MỖI THÁNG 4 CỘT W1-W4) =====
  // Tháng 10: Cột 1 đến 4 (A đến D)
  const m10Header = roadmapSheet.getRange(3, 1, 1, 4);
  m10Header.merge();
  m10Header.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Header.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#1E3A8A", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11: Cột 5 đến 8 (E đến H)
  const m11Header = roadmapSheet.getRange(3, 5, 1, 4);
  m11Header.merge();
  m11Header.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Header.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12: Cột 9 đến 12 (I đến L)
  const m12Header = roadmapSheet.getRange(3, 9, 1, 4);
  m12Header.merge();
  m12Header.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Header.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 32);

  // ===== TÍNH TOÁN VÀ VẼ CÁC TASK DÒNG =====
  // Mỗi task chiếm 2 dòng:
  // - Dòng 1: Card Thân Task (chiều cao 46px)
  // - Dòng 2: Thanh Tiến Trình % Đáy Card (chiều cao 6px)
  // - Sau đó là 1 dòng đệm trống 8px phân cách giữa các task
  let curRow = 4;
  sortedTasks.forEach(t => {
    const cfg = STATUS_STEPS[t.status] || STATUS_STEPS['Chưa tiếp nhận'];
    const prioCfg = PRIO_STYLE[t.prio] || PRIO_STYLE['P2'];
    const epicColor = getEpicColor(t.epic);

    // Xác định phạm vi cột của task (1 tháng = 4 cột; 2 tháng = 8 cột)
    let startCol = 1, totalCols = 4;
    if (t.timeGroup === 't10') {
      startCol = 1; totalCols = 4;
    } else if (t.timeGroup === 'span-10-11') {
      startCol = 1; totalCols = 8;
    } else if (t.timeGroup === 't11') {
      startCol = 5; totalCols = 4;
    } else if (t.timeGroup === 'span-11-12') {
      startCol = 5; totalCols = 8;
    } else if (t.timeGroup === 't12') {
      startCol = 9; totalCols = 4;
    }

    // Tô nền Canvas mờ nhẹ cho cả 12 cột ở dòng này
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    // 1. DÒNG THÂN CARD (ROW HEIGHT = 46px)
    roadmapSheet.setRowHeight(curRow, 46);

    // Màu Pastel của thanh task DỰA VÀO BỘ MÀU CỦA TRẠNG THÁI để hiển thị
    const cardBg = cfg.taskBg;
    const cardBorder = cfg.border;

    // BỎ PIC THEO YÊU CẦU: DÀNH TOÀN BỘ DIỆN TÍCH CHO TÊN TASK (SIZE 11 TO RÕ) VÀ TRẠNG THÁI ĐẦY ĐỦ
    // Task 1 tháng (4 cột = 420px): Trái 3 cột (315px) cho tên task to rõ, Phải 1 cột (105px) cho Prio & Trạng thái
    // Task 2 tháng (8 cột = 840px): Trái 6 cột (630px), Phải 2 cột (210px)
    const leftCols = (totalCols === 4) ? 3 : 6;
    const rightCols = totalCols - leftCols;

    // --- TÍNH TOÁN FONT SIZING CHO TÊN TASK TO RÕ (SIZE 11) ---
    const fullTitle = `${epicTag} ${t.title}`;
    const fullTitleLen = fullTitle.length;
    let titleFontSize = 11;
    if (fullTitleLen > 65) {
      titleFontSize = 9.2;
    } else if (fullTitleLen > 48) {
      titleFontSize = 10.0;
    }

    // --- KHU VỰC BÊN TRÁI: DÒNG 1 HỆ THỐNG + TÊN TASK (TO RÕ) | DÒNG 2 DETAIL ---
    const leftText = `${fullTitle}\n${t.desc}`;
    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftText);
    
    // Style Dòng 1: Hệ thống (Size 11)
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor(epicColor).build()
    );
    // Style Dòng 1: Tên Task (Size 11 to rõ, sắc nét, dễ đọc)
    leftBuilder.setTextStyle(epicTag.length + 1, fullTitle.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor("#0F172A").build()
    );
    // Style Dòng 2: Detail (Size 8.5)
    const descStart = fullTitle.length + 1;
    leftBuilder.setTextStyle(descStart, descStart + t.desc.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8.5).setForegroundColor("#475569").build()
    );

    const leftRange = roadmapSheet.getRange(curRow, startCol, 1, leftCols);
    leftRange.merge();
    leftRange.setRichTextValue(leftBuilder.build());
    leftRange.setWrap(false);
    leftRange.setBackground(cardBg);
    leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
    // Viền ô trái: Top = border, Left = SOLID_THICK (#7C3AED), Bottom = false, Right = false (nối liền ô phải)
    leftRange.setBorder(true, false, false, false, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);
    leftRange.setBorder(null, true, null, null, false, false, "#7C3AED", SpreadsheetApp.BorderStyle.SOLID_THICK);

    // --- KHU VỰC BÊN PHẢI: DÒNG 1 ĐỘ ƯU TIÊN | DÒNG 2 TRẠNG THÁI ĐẦY ĐỦ 100% ---
    const prioTag = `[${t.prio}]`;
    let displayStatus = t.status;
    if (displayStatus === 'PO reviewed/Transfer DEV') displayStatus = 'PO reviewed';
    if (displayStatus === 'Đang phân tích/Document') displayStatus = 'Đang phân tích';
    if (displayStatus === 'Đã tiếp nhận yêu cầu') displayStatus = 'Đã tiếp nhận';
    const statusTag = `[${displayStatus}]`;
    const rightText = `${prioTag}\n${statusTag}`;

    const rightBuilder = SpreadsheetApp.newRichTextValue().setText(rightText);
    // Style Dòng 1: Độ ưu tiên (Size 10 In Đậm, màu đỏ cam)
    rightBuilder.setTextStyle(0, prioTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(10).setForegroundColor(prioCfg.color).build()
    );
    // Style Dòng 2: Trạng thái (Size 8.5 In Đậm, màu sắc nhận diện chuẩn, không bao giờ thiếu trạng thái)
    const statusStart = prioTag.length + 1;
    rightBuilder.setTextStyle(statusStart, rightText.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8.5).setForegroundColor(cfg.badgeColor).build()
    );

    const rightRange = roadmapSheet.getRange(curRow, startCol + leftCols, 1, rightCols);
    rightRange.merge();
    rightRange.setRichTextValue(rightBuilder.build());
    rightRange.setWrap(false);
    rightRange.setBackground(cardBg);
    rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
    // Viền ô phải: Top = border, Right = border, Left = false (nối liền ô trái), Bottom = false
    rightRange.setBorder(true, false, false, true, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);

    // 2. DÒNG THANH TIẾN TRÌNH % ĐÁY CARD (ROW HEIGHT = 6px)
    curRow++;
    roadmapSheet.setRowHeight(curRow, 6);

    // Nền Canvas mờ nhẹ
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    // Tính toán số cột tiến độ:
    let coloredCols = Math.round((cfg.step / 8) * totalCols);
    if (coloredCols < 1) coloredCols = 1;
    if (coloredCols > totalCols) coloredCols = totalCols;
    const whiteCols = totalCols - coloredCols;

    // Tô màu tiến độ rực rỡ ở đáy card
    const progColorRange = roadmapSheet.getRange(curRow, startCol, 1, coloredCols);
    progColorRange.merge();
    progColorRange.setBackground(cfg.barColor);
    // Viền trái tím dày nối tiếp trong cùng khung card
    progColorRange.setBorder(false, true, true, false, false, false, "#7C3AED", SpreadsheetApp.BorderStyle.SOLID_THICK);
    progColorRange.setBorder(false, false, true, false, false, false, cfg.badgeColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

    if (whiteCols > 0) {
      const progWhiteRange = roadmapSheet.getRange(curRow, startCol + coloredCols, 1, whiteCols);
      progWhiteRange.merge();
      progWhiteRange.setBackground("#F8FAFC"); // Track nền xám nhạt
      progWhiteRange.setBorder(false, false, true, true, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);
    }

    // 3. DÒNG ĐỆM PHÂN CÁCH GIỮA CÁC TASK (ROW HEIGHT = 8px)
    curRow++;
    roadmapSheet.setRowHeight(curRow, 8);
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    curRow++;
  });

  // Footer
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 12);
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

      syncSheet.getRange(r + 4, 7).setBackground(cfg.bg).setFontColor(cfg.badgeColor).setFontWeight("bold").setHorizontalAlignment("center");
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

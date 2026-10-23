/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V6 (PERFECT POSITIONING & ZERO GRIDLINES)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * Các nâng cấp V6 giải quyết triệt để yêu cầu người dùng:
 * 1. ĐƯA ĐỘ ƯU TIÊN VỀ GÓC PHẢI TRÊN NGOÀI CÙNG & PIC/TRẠNG THÁI VỀ GÓC PHẢI DƯỚI NGOÀI CÙNG:
 *    - Sử dụng cấu trúc 2 phân vùng trong mỗi thanh task:
 *      + Vùng Trái (Nội dung: [Hệ thống] + Tên task + Detail) rộng tới 460px (hoặc 1120px khi vắt tháng)
 *        -> Không bao giờ bị cắt chữ hay tràn lề!
 *      + Vùng Phải (Meta) rộng 200px, căn lề PHẢI (right):
 *        * Dòng 1: [P1] nằm sát góc phải trên ngoài cùng (màu đen tuyền #000000 bold).
 *        * Dòng 2: 👤 PIC  ● Trạng thái nằm sát góc phải dưới ngoài cùng.
 *      + Hai vùng nối liền mạch không có đường kẻ ở giữa, tạo thành 1 thanh task thống nhất!
 * 2. TẮT HOÀN TOÀN TẤT CẢ ĐƯỜNG CHỈ / ĐƯỜNG LƯỚI TRONG TOÀN BỘ SHEET:
 *    - Sử dụng roadmapSheet.setHiddenGridlines(true) chuẩn Google Apps Script API.
 *    - Xóa toàn bộ viền ô bên trong các tháng, chỉ giữ lại viền ranh giới phân định giữa 3 tháng.
 * 3. BỎ ICON ở dòng detail (text thuần túy).
 * 4. BÔI ĐEN NỀN NỔI BẬT cho Hệ thống và Độ ưu tiên (#000000 bold).
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

const PRIO_WEIGHT = { 'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4 };

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

      // Xử lý detail rút gọn (BỎ ICON)
      let cleanDesc = rawDesc.split('\n')[0].trim();
      if (cleanDesc.startsWith('Tài liệu:')) {
        cleanDesc = 'Quy chuẩn tài liệu phân tích kỹ thuật và nghiệm thu UAT/CSOC';
      } else if (cleanDesc.startsWith('http')) {
        cleanDesc = 'Quy chuẩn cấu hình trang landing page và tích hợp hệ thống';
      } else if (!cleanDesc) {
        cleanDesc = 'Triển khai tính năng và phối hợp tích hợp theo yêu cầu';
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
    subTasks.sort((a, b) => ((PRIO_WEIGHT[a.prio] || 99) - (PRIO_WEIGHT[b.prio] || 99)));
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

  // TẮT HOÀN TOÀN CÁC ĐƯỜNG CHỈ / ĐƯỜNG LƯỚI TRÊN SHEET (CHUẨN APPS SCRIPT API)
  roadmapSheet.setHiddenGridlines(true);

  // ĐẶT ĐỘ RỘNG CỘT TỐI ƯU:
  // Cột A (Nội dung T10): 460px | Cột B (Meta T10): 200px  -> Tổng T10 = 660px
  // Cột C (Nội dung T11): 460px | Cột D (Meta T11): 200px  -> Tổng T11 = 660px
  // Cột E (Nội dung T12): 460px | Cột F (Meta T12): 200px  -> Tổng T12 = 660px
  roadmapSheet.setColumnWidth(1, 460); // A: Nội dung T10
  roadmapSheet.setColumnWidth(2, 200); // B: Meta T10
  roadmapSheet.setColumnWidth(3, 460); // C: Nội dung T11
  roadmapSheet.setColumnWidth(4, 200); // D: Meta T11
  roadmapSheet.setColumnWidth(5, 460); // E: Nội dung T12
  roadmapSheet.setColumnWidth(6, 200); // F: Meta T12

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange("A1:F1");
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 38);

  // ===== DÒNG 2: GHI CHÚ DUY NHẤT =====
  const noteRange = roadmapSheet.getRange("A2:F2");
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9.5).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 24);

  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MÀU ĐẬM TƯƠNG ỨNG CỘT, CHỮ TRẮNG BOLD) =====
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

  // 1. TÔ NỀN PASTEL MỜ PHẲNG LÌ CHO TOÀN BỘ 3 THÁNG
  // XÓA SẠCH MỌI ĐƯỜNG KẺ CHỈ BÊN TRONG, CHỈ GIỮ LẠI RANH GIỚI PHÂN BIỆT 3 THÁNG
  // Tháng 10: Viền trái Cột A, viền phải Cột B (ngăn cách T11)
  const m10Body = roadmapSheet.getRange(startRow, 1, numTasks, 2);
  m10Body.setBackground(MONTH_BG.m10)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11: Viền trái Cột C, viền phải Cột D (ngăn cách T12)
  const m11Body = roadmapSheet.getRange(startRow, 3, numTasks, 2);
  m11Body.setBackground(MONTH_BG.m11)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12: Viền trái Cột E, viền phải Cột F
  const m12Body = roadmapSheet.getRange(startRow, 5, numTasks, 2);
  m12Body.setBackground(MONTH_BG.m12)
    .setBorder(false, true, true, true, false, false, "#94A3B8", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // 2. Render từng task với 2 VÙNG CHUẨN XÁC 100%:
  // - VÙNG TRÁI: Tên Task & Detail rút gọn (Căn trái)
  // - VÙNG PHẢI: Góc trên [P1], Góc dưới 👤 PIC  ● Trạng thái (Căn phải)
  let curRow = startRow;
  sortedTasks.forEach(t => {
    roadmapSheet.setRowHeight(curRow, 38);

    const cfg = STATUS_CONFIG[t.status] || STATUS_CONFIG['Chưa tiếp nhận'];
    const epicTag = `[${t.epic}]`;
    const prioTag = `[${t.prio}]`;

    // PHẦN BÊN TRÁI: Hệ thống + Tên Task & Detail rút gọn
    const leftLine1 = `${epicTag} ${t.title}`;
    const leftLine2 = t.desc; // Không icon
    const leftFullText = `${leftLine1}\n${leftLine2}`;

    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftFullText);
    // Hệ thống [EPIC]: BÔI ĐEN NỔI BẬT #000000, Bold, 9.5pt
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor("#000000").build()
    );
    // Tên Task: Đen than #0F172A, Bold, 9.5pt
    leftBuilder.setTextStyle(epicTag.length + 1, leftLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor("#0F172A").build()
    );
    // Detail rút gọn: Nghiêng, Xám ghi #475569, 8pt
    const detailStart = leftLine1.length + 1;
    leftBuilder.setTextStyle(detailStart, detailStart + leftLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8).setForegroundColor("#475569").build()
    );
    const leftRichText = leftBuilder.build();

    // PHẦN BÊN PHẢI (GÓC PHẢI TRÊN & GÓC PHẢI DƯỚI - CĂN PHẢI RIGHT):
    // Dòng 1: [P1] -> BÔI ĐEN NỔI BẬT #000000, Bold, 10pt
    // Dòng 2: 👤 PIC  ● Trạng thái -> Size 8, Xám than #334155
    const rightLine1 = prioTag;
    const rightLine2 = `👤 ${t.pic}  ● ${t.status}`;
    const rightFullText = `${rightLine1}\n${rightLine2}`;

    const rightBuilder = SpreadsheetApp.newRichTextValue().setText(rightFullText);
    // Dòng 1: [P1] bôi đen
    rightBuilder.setTextStyle(0, rightLine1.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(10).setForegroundColor("#000000").build()
    );
    // Dòng 2: PIC & Trạng thái
    const rLine2Start = rightLine1.length + 1;
    rightBuilder.setTextStyle(rLine2Start, rLine2Start + rightLine2.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(8).setForegroundColor("#334155").build()
    );
    // Nhấn màu trạng thái
    const statusStart = rightFullText.lastIndexOf(t.status);
    if (statusStart !== -1) {
      rightBuilder.setTextStyle(statusStart, statusStart + t.status.length,
        SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8).setForegroundColor(cfg.badgeColor).build()
      );
    }
    const rightRichText = rightBuilder.build();

    // XÁC ĐỊNH VÙNG TRÁI VÀ PHẢI THEO THỜI GIAN THỰC THI:
    let leftRange, rightRange;
    if (t.timeGroup === 't10') {
      leftRange = roadmapSheet.getRange(curRow, 1, 1, 1);  // Cột A (460px)
      rightRange = roadmapSheet.getRange(curRow, 2, 1, 1); // Cột B (200px)
    } else if (t.timeGroup === 'span-10-11') {
      roadmapSheet.getRange(curRow, 1, 1, 3).merge();
      leftRange = roadmapSheet.getRange(curRow, 1, 1, 3);  // Cột A:C (460 + 200 + 460 = 1120px)
      rightRange = roadmapSheet.getRange(curRow, 4, 1, 1); // Cột D (200px)
    } else if (t.timeGroup === 't11') {
      leftRange = roadmapSheet.getRange(curRow, 3, 1, 1);  // Cột C (460px)
      rightRange = roadmapSheet.getRange(curRow, 4, 1, 1); // Cột D (200px)
    } else if (t.timeGroup === 'span-11-12') {
      roadmapSheet.getRange(curRow, 3, 1, 3).merge();
      leftRange = roadmapSheet.getRange(curRow, 3, 1, 3);  // Cột C:E (1120px)
      rightRange = roadmapSheet.getRange(curRow, 6, 1, 1); // Cột F (200px)
    } else if (t.timeGroup === 't12') {
      leftRange = roadmapSheet.getRange(curRow, 5, 1, 1);  // Cột E (460px)
      rightRange = roadmapSheet.getRange(curRow, 6, 1, 1); // Cột F (200px)
    }

    // ĐỊNH DẠNG VÙNG TRÁI (NỘI DUNG)
    leftRange.setRichTextValue(leftRichText);
    leftRange.setWrap(false);
    leftRange.setBackground(cfg.bg);
    leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
    // Viền bao ngoài: Top, Left, Bottom (Bỏ viền Right để nối liền sang Vùng Phải)
    leftRange.setBorder(true, true, true, false, false, false, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

    // ĐỊNH DẠNG VÙNG PHẢI (GÓC PHẢI TRÊN & GÓC PHẢI DƯỚI NGOÀI CÙNG)
    rightRange.setRichTextValue(rightRichText);
    rightRange.setWrap(false);
    rightRange.setBackground(cfg.bg);
    rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
    // Viền bao ngoài: Top, Right, Bottom (Bỏ viền Left để nối liền sang Vùng Trái)
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
      syncSheet.getRange(r + 4, 7).setBackground(cfg.bg).setFontColor(cfg.fg).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 5).setFontColor("#000000").setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 6).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  activeSS.toast(`Đã đồng bộ thành công ${q4Tasks.length} task từ Backlog gốc!`, 'Hoàn tất', 5);
}

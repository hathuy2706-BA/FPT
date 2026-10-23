/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V3 (PASTEL LUXURY DASHBOARD)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * Các nâng cấp theo yêu cầu người dùng:
 * 1. Ẩn đường chỉ lưới (gridlines), đóng khung 3 cột tháng riêng biệt với viền rõ ràng.
 * 2. 3 cột tháng dùng màu pastel mờ nhẹ (T10 xanh dịu, T11 tím dịu, T12 xanh ngọc dịu).
 * 3. Các cột task dùng màu pastel đậm hơn nền cột 1 chút theo đúng 8 nấc tiến độ.
 * 4. In đậm tên các task, gắn độ ưu tiên ở góc phải bên trên với màu phân biệt P1-P4.
 * 5. Bổ sung dòng detail rút gọn cho từng task (trích xuất từ mô tả gốc).
 * 6. Bỏ chữ "PIC:", chỉ giữ lại icon 👤 và tên PIC.
 * 7. Bỏ text về tiến độ (chỉ dùng màu sắc trực quan đại diện cho % tiến độ).
 * 8. Đóng khung [..] cho các hệ thống/EPIC.
 * 9. Bỏ chữ "Trạng thái", bỏ ký tự "|".
 * 10. Quy định màu đồng bộ chuẩn mực cho: Tên hệ thống, Tên task, Detail, PIC, Độ ưu tiên.
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// Cấu hình màu Pastel đậm hơn nền cho 8 nấc tiến độ / trạng thái
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
    bg: '#DDD6FE',        // Pastel tím lavender đậm
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
  'P4': { color: '#64748B', label: '[P4]', weight: 4 }  // Xám trung tính
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
      if (cleanDesc.length > 70) {
        cleanDesc = cleanDesc.substring(0, 67) + '...';
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
    subTasks.sort((a, b) => ((PRIO_STYLE[a.prio] ? PRIO_STYLE[a.prio].weight : 99) - (PRIO_STYLE[b.prio] ? PRIO_STYLE[b.prio].weight : 99)));
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

  // ẨN ĐƯỜNG CHỈ (GRIDLINES) ĐỂ TẠO GIAO DIỆN SẠCH ĐẸP NHƯ CANVAS BẢN THIẾT KẾ
  roadmapSheet.setHideGridlines(true);

  // Đặt chiều rộng cột (Cột A-B: Tháng 10, Cột C-D: Tháng 11, Cột E-F: Tháng 12)
  roadmapSheet.setColumnWidth(1, 280); // A
  roadmapSheet.setColumnWidth(2, 280); // B
  roadmapSheet.setColumnWidth(3, 280); // C
  roadmapSheet.setColumnWidth(4, 280); // D
  roadmapSheet.setColumnWidth(5, 280); // E
  roadmapSheet.setColumnWidth(6, 280); // F

  // ===== HEADER DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange("A1:F1");
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(16).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 42);

  // DÒNG 2: Khối Metrics tự động (Header KPI Cards)
  const metricValues = [
    [
      `Tổng User Stories: ${totalCount}`,
      `Task Chạy Đa Tháng: ${multiMonthCount}`,
      `Hạn Tháng 10: ${t10Count}`,
      `Hạn Tháng 11: ${t11Count}`,
      `Hạn Tháng 12: ${t12Count}`,
      `Cập nhật: ${Utilities.formatDate(new Date(), "GMT+7", "HH:mm dd/MM")}`
    ]
  ];
  const metricRange = roadmapSheet.getRange("A2:F2");
  metricRange.setValues(metricValues);
  metricRange.setFontFamily("Times New Roman").setFontSize(10).setFontWeight("bold");
  metricRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  metricRange.setBackground("#F8FAFC").setBorder(true, true, true, true, true, true, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID);
  roadmapSheet.setRowHeight(2, 28);

  // DÒNG 3: Chú thích 8 nấc trạng thái thanh lịch
  const legendRange = roadmapSheet.getRange("A3:F3");
  legendRange.merge();
  legendRange.setValue("CHỦ ĐẠO MÀU PASTEL 8 NẤC TIẾN ĐỘ: 1. Chưa tiếp nhận (12.5%) ➔ 2. Đã tiếp nhận (25%) ➔ 3. Đang phân tích (37.5%) ➔ 4. PO reviewed (50%) ➔ 5. DEV In Progress (62.5%) ➔ 6. UAT (75%) ➔ 7. QC/CSOC (87.5%) ➔ 8. Done (100%)");
  legendRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B");
  legendRange.setHorizontalAlignment("center").setVerticalAlignment("middle").setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(3, 24);

  // DÒNG 4: 3 CỘT THÁNG (MÀU PASTEL MỜ NHẸ, ĐÓNG KHUNG RIÊNG TỪNG THÁNG)
  // Tháng 10 (Cột A-B)
  const m10Header = roadmapSheet.getRange("A4:B4");
  m10Header.merge();
  m10Header.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#1E3A8A");
  m10Header.setBackground("#DBEAFE").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#93C5FD", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11 (Cột C-D)
  const m11Header = roadmapSheet.getRange("C4:D4");
  m11Header.merge();
  m11Header.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#581C87");
  m11Header.setBackground("#F3E8FF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#D8B4FE", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12 (Cột E-F)
  const m12Header = roadmapSheet.getRange("E4:F4");
  m12Header.merge();
  m12Header.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(12).setFontWeight("bold").setFontColor("#065F46");
  m12Header.setBackground("#DCFCE7").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#86EFAC", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(4, 34);

  // ===== VẼ CÁC TASK DÒNG =====
  const startRow = 5;
  const numTasks = sortedTasks.length;
  const endRow = startRow + numTasks - 1;

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

  // 2. Render từng task với RichText chuẩn
  let curRow = startRow;
  sortedTasks.forEach(t => {
    roadmapSheet.setRowHeight(curRow, 58); // Chiều cao thoải mái cho 3 dòng

    const cfg = STATUS_CONFIG[t.status] || STATUS_CONFIG['Chưa tiếp nhận'];
    const prioCfg = PRIO_STYLE[t.prio] || PRIO_STYLE['P2'];

    // Chuẩn bị định dạng chuỗi text 3 dòng:
    // Dòng 1: [Hệ thống] Tên Task                  [P1]
    // Dòng 2: 📝 Detail rút gọn
    // Dòng 3: 👤 PIC      ● Trạng thái
    const epicTag = `[${t.epic}]`;
    const prioTag = prioCfg.label;
    
    // Tính toán khoảng trắng đệm để tag P1 dạt về góc phải
    const leftText = `${epicTag} ${t.title}`;
    // Ước lượng độ dài cho khoảng cách đệm
    const padCount = Math.max(4, 52 - leftText.length);
    const paddingSpaces = " ".repeat(padCount);
    
    const line1 = `${leftText}${paddingSpaces}${prioTag}`;
    const line2 = `📝 ${t.desc}`;
    const line3 = `👤 ${t.pic}      ● ${t.status}`;
    const fullText = `${line1}\n${line2}\n${line3}`;

    // Xây dựng RichTextValue để tô màu đồng bộ chuẩn mực từng thành phần:
    const builder = SpreadsheetApp.newRichTextValue().setText(fullText);

    // Style 1: Hệ thống [EPIC] -> Xanh Navy đậm, Bold
    const epicEnd = epicTag.length;
    builder.setTextStyle(0, epicEnd, 
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor("#1E40AF").build()
    );

    // Style 2: Tên Task -> Đen Than #0F172A, Bold
    const titleStart = epicEnd + 1;
    const titleEnd = leftText.length;
    builder.setTextStyle(titleStart, titleEnd,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor("#0F172A").build()
    );

    // Style 3: Tag Độ ưu tiên [P1] -> Màu phân biệt nổi bật P1/P2/P3/P4, Bold
    const prioStart = line1.indexOf(prioTag);
    if (prioStart !== -1) {
      builder.setTextStyle(prioStart, prioStart + prioTag.length,
        SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(9.5).setForegroundColor(prioCfg.color).build()
      );
    }

    // Style 4: Detail rút gọn -> Xám trung tính #475569, Nghiêng, Size 8.5
    const line2Start = line1.length + 1;
    const line2End = line2Start + line2.length;
    builder.setTextStyle(line2Start, line2End,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8.5).setForegroundColor("#475569").build()
    );

    // Style 5: PIC & Trạng thái -> Size 8.5, Đậm nhẹ
    const line3Start = line2End + 1;
    const line3End = line3Start + line3.length;
    builder.setTextStyle(line3Start, line3End,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(8.5).setForegroundColor("#334155").build()
    );

    // Nhấn mạnh màu Trạng thái ở cuối dòng 3
    const statusIdx = fullText.lastIndexOf(t.status);
    if (statusIdx !== -1) {
      builder.setTextStyle(statusIdx, statusIdx + t.status.length,
        SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8.5).setForegroundColor(cfg.badgeColor).build()
      );
    }

    const richTextValue = builder.build();

    // Xác định phạm vi ô theo thời gian thực thi
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
      targetRange.setRichTextValue(richTextValue);
      targetRange.setWrap(true);
      targetRange.setBackground(cfg.bg); // Nền Pastel đậm hơn nền cột theo đúng nấc tiến độ
      targetRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
      targetRange.setBorder(true, true, true, true, true, true, cfg.borderColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
    }

    curRow++;
  });

  // Footer
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 6);
  footerRange.merge();
  footerRange.setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)  |  FPT Telecom Online Business  |  Chuẩn nhận diện Pastel Dashboard");
  footerRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B");
  footerRange.setHorizontalAlignment("center").setVerticalAlignment("middle").setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(curRow, 26);

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
  activeSS.toast(`Đã đồng bộ thành công ${totalCount} task từ Backlog gốc!`, 'Hoàn tất', 5);
}

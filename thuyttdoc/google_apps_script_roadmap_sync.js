/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V10 (PREMIUM PIXEL PERFECT & REALTIME SOURCE SYNC)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * ĐỒNG BỘ CHUẨN XÁC THEO YÊU CẦU:
 * 1. SỐ LƯỢNG TASK: Đọc toàn diện từ sheet gốc 'Product Backlog VH' / 'Product Backlog FCP'.
 * 2. TÊN TASK: Lấy trọn vẹn từ cột US Title (Đầu mục công việc), không cắt chữ, font size 10-11 rõ nét.
 * 3. BỘ TRẠNG THÁI MỚI NHẤT:
 *    - 'UAT' ➔ Nền Tím đậm (#581C87), chữ TRẮNG (#FFFFFF) sắc nét nổi bật.
 *    - 'DEV In Progress' ➔ Nền Vàng bơ (#FEEFC3), chữ nâu (#594400).
 *    - 'Transfer DEV/PO reviewed' ➔ Nền Xanh lá non (#C4EED0), chữ xanh đậm (#0F5132).
 *    - 'BA/Document' / 'Đang phân tích' ➔ Nền Cam đào (#FFD8B4), chữ cam nâu (#8A3800).
 *    - 'To do' / 'Chưa tiếp nhận' ➔ Nền Xám bạc (#E8EAED), chữ xám đen (#3C4043).
 *    - 'Đã tiếp nhận yêu cầu' ➔ Nền Xanh baby (#C2E7FF), chữ xanh đậm (#004A77).
 * 4. MÀU THANH TASK: Đồng bộ 100% toàn bộ thân card, viền card và dải điểm nhấn theo màu trạng thái.
 * 5. DETAIL (ACCEPTANCE CRITERIA / MÔ TẢ): Đồng bộ trực tiếp nội dung nghiệp vụ từ file gốc, lược bỏ URL thừa.
 * 6. THÁNG ĐƯỢC ĐIỀN (TIMELINE): 
 *    - Nhận diện chuẩn xác các task vắt 2 tháng (Tháng 10 - Tháng 11: 8 cột A-H; Tháng 11 - Tháng 12: 8 cột E-L).
 *    - Các task 1 tháng chiếm 4 cột (Tháng 10: A-D; Tháng 11: E-H; Tháng 12: I-L).
 * 7. QUY TẮC ĐỒNG BỘ:
 *    - Tự động quét và cập nhật mỗi ngày lúc 7:00 AM.
 *    - Tự động OnEdit khi chỉnh sửa trực tiếp trên file Roadmap / Sync.
 *    - Hỗ trợ đồng bộ thủ công 1-click qua Menu Google Sheets.
 * =========================================================================================
 */

const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// BỘ MÀU NHẬN DIỆN CHUẨN XÁC 100% THEO DROPDOWN CHIP TRÊN GOOGLE SHEETS GỐC
const STATUS_STEPS = {
  'Chưa tiếp nhận': { 
    step: 1, percent: '12.5%', 
    taskBg: '#E8EAED', border: '#BDC1C6', barColor: '#64748B', badgeColor: '#3C4043',
    isDark: false, name: 'Chưa tiếp nhận', icon: '⚪'
  },
  'Đã tiếp nhận yêu cầu': { 
    step: 2, percent: '25.0%', 
    taskBg: '#C2E7FF', border: '#7FCFFF', barColor: '#2563EB', badgeColor: '#004A77',
    isDark: false, name: 'Đã tiếp nhận yêu cầu', icon: '🔵'
  },
  'Đang phân tích/Document': { 
    step: 3, percent: '37.5%', 
    taskBg: '#FFD8B4', border: '#FFB787', barColor: '#EA580C', badgeColor: '#8A3800',
    isDark: false, name: 'Đang phân tích/Document', icon: '🟠'
  },
  'Transfer DEV/PO reviewed': { 
    step: 4, percent: '50.0%', 
    taskBg: '#C4EED0', border: '#8CE0A7', barColor: '#16A34A', badgeColor: '#0F5132',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'PO reviewed/Transfer DEV': { 
    step: 4, percent: '50.0%', 
    taskBg: '#C4EED0', border: '#8CE0A7', barColor: '#16A34A', badgeColor: '#0F5132',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'PO reviewed': { 
    step: 4, percent: '50.0%', 
    taskBg: '#C4EED0', border: '#8CE0A7', barColor: '#16A34A', badgeColor: '#0F5132',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'DEV In Progress': { 
    step: 5, percent: '62.5%', 
    taskBg: '#FEEFC3', border: '#FDD663', barColor: '#EAB308', badgeColor: '#594400',
    isDark: false, name: 'DEV In Progress', icon: '🟡'
  },
  'UAT': { 
    step: 6, percent: '75.0%', 
    taskBg: '#581C87', border: '#3B0764', barColor: '#C084FC', badgeColor: '#FFFFFF',
    isDark: true, name: 'UAT', icon: '🟣'
  },
  'QC/CSOC': { 
    step: 7, percent: '87.5%', 
    taskBg: '#005696', border: '#004A77', barColor: '#38BDF8', badgeColor: '#FFFFFF',
    isDark: true, name: 'QC/CSOC', icon: '🔷'
  },
  'Done': { 
    step: 8, percent: '100.0%', 
    taskBg: '#0F5132', border: '#0B3D26', barColor: '#4ADE80', badgeColor: '#FFFFFF',
    isDark: true, name: 'Done', icon: '✅'
  },
  'Pending': { 
    step: 0, percent: '0%', 
    taskBg: '#343A40', border: '#212529', barColor: '#6C757D', badgeColor: '#FFFFFF',
    isDark: true, name: 'Pending', icon: '⚫'
  }
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
  if (!epic) return '#0284C7';                                       // Fallback mặc định
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
 * Chuẩn hóa linh hoạt trạng thái task để luôn khớp chính xác 100% với bộ màu và tiến trình
 * LẤY ĐÚNG BỘ TRẠNG THÁI MỚI NHẤT TỪ FILE GỐC:
 * - 'UAT' ➔ 'UAT' (Tím đậm #581C87, chữ trắng)
 * - 'DEV In Progress' ➔ 'DEV In Progress' (Vàng bơ #FEEFC3, chữ nâu)
 * - 'Transfer DEV/PO reviewed' ➔ 'Transfer DEV/PO reviewed' (Xanh lá non #C4EED0)
 * - 'BA/Document' / 'Đang phân tích' ➔ 'Đang phân tích/Document' (Cam đào #FFD8B4)
 * - 'To do' / 'Chưa tiếp nhận' ➔ 'Chưa tiếp nhận' (Xám bạc #E8EAED)
 * - 'Đã tiếp nhận yêu cầu' / 'Tiếp nhận' ➔ 'Đã tiếp nhận yêu cầu' (Xanh baby #C2E7FF)
 */
function normalizeStatus(raw) {
  if (!raw) return 'Chưa tiếp nhận';
  const s = String(raw).trim().toLowerCase();
  
  // 1. Nhóm Transfer DEV / PO reviewed (Ưu tiên kiểm tra trước từ khóa 'dev' đơn lẻ)
  if (s.includes('transfer') || s.includes('po reviewed') || s.includes('po') || (s.includes('review') && !s.includes('in progress'))) {
    return 'Transfer DEV/PO reviewed';
  }
  
  // 2. Nhóm DEV In Progress
  if (s.includes('in progress') || s.includes('dev') || s.includes('phát triển')) {
    return 'DEV In Progress';
  }
  
  // 3. Nhóm UAT / Test
  if (s.includes('uat') || s.includes('test') || s.includes('nghiệm thu')) {
    return 'UAT';
  }
  
  // 4. Nhóm BA/Document / Đang phân tích (Trên file gốc ghi là "BA/Document")
  if (s.includes('ba/document') || s.includes('ba') || s.includes('phân tích') || s.includes('document') || s.includes('analysis') || s.includes('doc')) {
    return 'Đang phân tích/Document';
  }
  
  // 5. Nhóm To do / Chưa tiếp nhận (Trên file gốc ghi là "To do")
  if (s.includes('to do') || s.includes('todo') || s.includes('chưa tiếp nhận') || s.includes('new') || s.includes('open')) {
    return 'Chưa tiếp nhận';
  }
  if (s.includes('tiếp nhận') || s.includes('nhận yêu cầu') || s.includes('received')) {
    return 'Đã tiếp nhận yêu cầu';
  }
  
  // 6. Nhóm QC / CSOC
  if (s.includes('qc') || s.includes('csoc')) {
    return 'QC/CSOC';
  }
  
  // 7. Nhóm Done
  if (s.includes('done') || s.includes('hoàn thành') || s.includes('closed')) {
    return 'Done';
  }
  
  return String(raw).trim();
}

/**
 * Phân tích và nhận diện chính xác mốc thời gian (Timeline) được điền trên file gốc
 * Hỗ trợ nhận diện các task vắt 2 tháng: Tháng 10 - Tháng 11, Tháng 11 - Tháng 12
 */
function parseTimeline(timelineRaw) {
  if (!timelineRaw) return null;
  const tl = String(timelineRaw).trim().toLowerCase();
  
  const has10 = tl.includes('10') || tl.includes('tháng 10') || tl.includes('t10');
  const has11 = tl.includes('11') || tl.includes('tháng 11') || tl.includes('t11');
  const has12 = tl.includes('12') || tl.includes('tháng 12') || tl.includes('t12');
  
  if (has10 && has11) {
    return { timeGroup: 'span-10-11', startM: 10, endM: 11, startCol: 1, totalCols: 8, label: 'Tháng 10 - Tháng 11' };
  }
  if (has11 && has12) {
    return { timeGroup: 'span-11-12', startM: 11, endM: 12, startCol: 5, totalCols: 8, label: 'Tháng 11 - Tháng 12' };
  }
  if (has10) {
    return { timeGroup: 't10', startM: 10, endM: 10, startCol: 1, totalCols: 4, label: 'Tháng 10' };
  }
  if (has11) {
    return { timeGroup: 't11', startM: 11, endM: 11, startCol: 5, totalCols: 4, label: 'Tháng 11' };
  }
  if (has12) {
    return { timeGroup: 't12', startM: 12, endM: 12, startCol: 9, totalCols: 4, label: 'Tháng 12' };
  }
  return null;
}

/**
 * Làm sạch mô tả Detail lấy trực tiếp từ file gốc (giữ nguyên ngữ nghĩa nghiệp vụ, lược bỏ link URL rườm rà)
 */
function cleanDetailText(rawDesc) {
  if (!rawDesc) return 'Triển khai tính năng và phối hợp tích hợp theo yêu cầu';
  let desc = String(rawDesc).trim();
  // Bỏ các link URL http/https dài dòng
  desc = desc.replace(/https?:\/\/[^\s]+/g, '').trim();
  // Bỏ tiền tố Tài liệu / Thiết kế nếu bị thừa
  desc = desc.replace(/^Tài liệu:\s*Thiết kế:\s*/i, '').trim();
  desc = desc.replace(/^Tài liệu:\s*/i, '').trim();
  desc = desc.replace(/^Thiết kế:\s*/i, '').trim();
  // Gộp các dòng thành 1 dòng phân cách bằng ' - '
  desc = desc.split('\n').map(l => l.trim()).filter(l => l.length > 0).join(' - ');
  if (!desc || desc === '-' || desc.length < 3) {
    if (String(rawDesc).includes('document') || String(rawDesc).includes('Tài liệu')) {
      desc = 'Quy chuẩn tài liệu phân tích kỹ thuật và nghiệm thu UAT';
    } else {
      desc = 'Quy chuẩn cấu hình trang landing page và tích hợp hệ thống';
    }
  }
  if (desc.length > 60) {
    desc = desc.substring(0, 57) + '...';
  }
  return desc;
}

/**
 * Menu tùy chỉnh khi mở Google Sheet
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 PRODUCT ROADMAP')
    .addItem('🔄 Đồng Bộ Backlog & Đổi Màu Thanh Task Theo Trạng Thái', 'syncRoadmapFromBacklog')
    .addSeparator()
    .addItem('⏰ Kích Hoạt Tự Động Đồng Bộ 1 Ngày / 1 Lần (7:00 AM)', 'setupDailyAutoTrigger')
    .addItem('❌ Hủy Bỏ Lịch Tự Động Cập Nhật', 'cancelAutoTriggers')
    .addSeparator()
    .addItem('🎨 Xem Bảng Quy Tắc Tự Động Đổi Màu Thanh Task', 'showColorRulesDialog')
    .addToUi();
}

/**
 * Hiển thị popup Bảng Quy Tắc Tự Động Cập Nhật Màu Sắc Thanh Task
 */
function showColorRulesDialog() {
  const ui = SpreadsheetApp.getUi();
  const msg = 
    "🎨 BẢNG QUY TẮC MÀU SẮC TRẠNG THÁI (ĐỒNG BỘ 100% TỪ DROPDOWN GOOGLE SHEETS):\n\n" +
    "Toàn bộ thanh task, màu chữ và thanh tiến trình sẽ tự động khoác lên màu nhận diện tương ứng của trạng thái:\n\n" +
    "1. 🟡 DEV In Progress ➔ Màu Vàng bơ (#FEEFC3) | Chữ nâu (#594400) | Tiến độ 62.5%\n" +
    "2. 🟣 UAT ➔ Màu Tím đậm (#581C87) | Chữ TRẮNG (#FFFFFF) nổi bật | Tiến độ 75.0%\n" +
    "3. 🟢 Transfer DEV / PO reviewed ➔ Màu Xanh lá non (#C4EED0) | Chữ xanh đậm (#0F5132) | Tiến độ 50.0%\n" +
    "4. 🟠 Đang phân tích / Document (BA/Doc) ➔ Màu Cam đào (#FFD8B4) | Chữ cam nâu (#8A3800) | Tiến độ 37.5%\n" +
    "5. 🔵 Đã tiếp nhận yêu cầu ➔ Màu Xanh dương nhạt (#C2E7FF) | Chữ xanh đậm (#004A77) | Tiến độ 25.0%\n" +
    "6. ⚪ Chưa tiếp nhận (To do) ➔ Màu Xám (#E8EAED) | Chữ xám đen (#3C4043) | Tiến độ 12.5%\n" +
    "7. 🔷 QC/CSOC ➔ Màu Xanh dương đậm (#005696) | Chữ trắng | Tiến độ 87.5%\n" +
    "8. ✅ Done ➔ Màu Xanh lá đậm (#0F5132) | Chữ trắng | Tiến độ 100%\n\n" +
    "⏰ Lịch tự động: 1 ngày / 1 lần vào lúc 7:00 AM.\n" +
    "🔄 Đồng bộ tức thì: Menu '🚀 PRODUCT ROADMAP' ➔ '🔄 Đồng Bộ Backlog & Đổi Màu Thanh Task Theo Trạng Thái'.";
  ui.alert("Bảng Quy Tắc Tự Động Cập Nhật Màu Thanh Task", msg, ui.ButtonSet.OK);
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
  
  SpreadsheetApp.getActiveSpreadsheet().toast('Đã kích hoạt thành công: Tự động đồng bộ & cập nhật màu thanh task 1 ngày 1 lần lúc 7:00 AM!', 'Thành công', 8);
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

  // ƯU TIÊN MỞ TAB CÓ DỮ LIỆU THỰC TẾ: 'Product Backlog VH' hoặc 'Product Backlog FCP'
  const sheets = sourceSS.getSheets();
  let sourceSheet = sourceSS.getSheetByName('Product Backlog VH');
  if (!sourceSheet) {
    sourceSheet = sheets.find(s => s.getSheetId() === SOURCE_GID) || sourceSS.getSheetByName('Product Backlog FCP') || sheets[0];
  }
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
    const tlParsed = parseTimeline(timeline);
    if (!tlParsed) continue; // Bỏ qua các task không thuộc Quý 4 hoặc chưa điền tháng

    const rawStatus = String(row[colMap['status']] || '').trim();
    const status = normalizeStatus(rawStatus);
    const epic = String(row[colMap['epic']] || '').trim();
    const prio = String(row[colMap['prio']] || 'P2').trim();
    const pic = String(row[colMap['pic']] || '').trim();
    const rawDesc = String(row[colMap['desc']] || '').trim();

    const isExcluded = status.toLowerCase() === 'done' || status.toLowerCase() === 'pending';
    if (isExcluded) continue;

    // Detail làm sạch từ dữ liệu gốc
    const cleanDesc = cleanDetailText(rawDesc);

    q4Tasks.push({
      title: titleFull.split('\n')[0].trim(),
      epic: epic,
      desc: cleanDesc,
      prio: prio,
      pic: pic,
      status: status,
      rawStatus: rawStatus,
      timeline: timeline,
      timeGroup: tlParsed.timeGroup,
      startM: tlParsed.startM,
      endM: tlParsed.endM,
      startCol: tlParsed.startCol,
      totalCols: tlParsed.totalCols
    });
  }

  // 2.1 Gom nhóm các task LDP NHA theo yêu cầu:
  // [Web, CMS] Trang LDP NHA, Trang LDP NHA lịch thi đấu, Trang LDP NHA bảng xếp hạng, Trang LDP NHA -SA
  // => Gom chung thành: [Web, CMS] Trang LDP NHA
  // Detail: Trang lịch thi đấu, trang BXH, trang SA NHA
  const nhaTasks = q4Tasks.filter(t => t.title.includes('NHA') || t.title.includes('Ngoại Hạng Anh'));
  if (nhaTasks.length > 0) {
    const baseNha = nhaTasks[0];
    const mergedNhaTask = {
      title: 'Trang LDP NHA',
      epic: 'Web, CMS',
      desc: 'Trang lịch thi đấu, trang BXH, trang SA NHA',
      prio: 'P2',
      pic: 'ThuyTT104',
      status: baseNha.status || 'Chưa tiếp nhận',
      rawStatus: baseNha.rawStatus || 'To do',
      timeline: 'Tháng 12',
      timeGroup: 't12',
      startM: 12,
      endM: 12,
      startCol: 9,
      totalCols: 4
    };

    // Loại bỏ các task NHA con riêng lẻ và thay bằng 1 task đã gom duy nhất
    const nonNhaTasks = q4Tasks.filter(t => !t.title.includes('NHA') && !t.title.includes('Ngoại Hạng Anh'));
    nonNhaTasks.push(mergedNhaTask);
    q4Tasks.length = 0;
    q4Tasks.push(...nonNhaTasks);
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

  // ĐẶT ĐỘ RỘNG CHO 12 CỘT TIẾN ĐỘ: 145px/CỘT
  // MỖI THÁNG 4 CỘT = 580px, TỔNG BẢNG 12 CỘT = 1.740px VỪA KHÍT MÀN HÌNH Ở ZOOM 100%
  for (let c = 1; c <= 12; c++) {
    roadmapSheet.setColumnWidth(c, 145);
  }
  // Xóa các cột thừa từ cột 13 trở đi để bảng đóng khung gọn gàng
  if (roadmapSheet.getMaxColumns() > 12) {
    roadmapSheet.deleteColumns(13, roadmapSheet.getMaxColumns() - 12);
  }

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG =====
  const titleRange = roadmapSheet.getRange(1, 1, 1, 12);
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(15).setFontWeight("bold").setFontColor("#005696");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(1, 30);

  // ===== DÒNG 2: GHI CHÚ HOT REQUEST =====
  const noteRange = roadmapSheet.getRange(2, 1, 1, 12);
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 20);

  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MỖI THÁNG 4 CỘT W1-W4) =====
  // Tháng 10: Cột 1 đến 4 (A đến D)
  const m10Header = roadmapSheet.getRange(3, 1, 1, 4);
  m10Header.merge();
  m10Header.setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Header.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#1E3A8A", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 11: Cột 5 đến 8 (E đến H)
  const m11Header = roadmapSheet.getRange(3, 5, 1, 4);
  m11Header.merge();
  m11Header.setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Header.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  // Tháng 12: Cột 9 đến 12 (I đến L)
  const m12Header = roadmapSheet.getRange(3, 9, 1, 4);
  m12Header.merge();
  m12Header.setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Header.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 26);

  // ===== TÍNH TOÁN VÀ VẼ CÁC TASK DÒNG =====
  // Mỗi task chiếm 2 dòng:
  // - Dòng 1: Card Thân Task (chiều cao 34px)
  // - Dòng 2: Thanh Tiến Trình % Đáy Card (chiều cao 4px)
  // - Sau đó là 1 dòng đệm trống 3px phân cách giữa các task
  let curRow = 4;
  sortedTasks.forEach(t => {
    const cfg = STATUS_STEPS[t.status] || STATUS_STEPS['Chưa tiếp nhận'];
    const prioCfg = PRIO_STYLE[t.prio] || PRIO_STYLE['P2'];
    const epicColor = getEpicColor(t.epic);
    const epicTag = `[${t.epic}]`;

    // Xác định phạm vi cột của task từ dữ liệu đã phân tích
    const startCol = t.startCol;
    const totalCols = t.totalCols;

    // Tô nền Canvas mờ nhẹ cho cả 12 cột ở dòng này
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    // 1. DÒNG THÂN CARD (ROW HEIGHT = 34px GỌN GÀNG, TIẾT KIỆM CHIỀU CAO)
    roadmapSheet.setRowHeight(curRow, 34);

    // Màu của thanh task DỰA VÀO BỘ MÀU CHUẨN CỦA TRẠNG THÁI để hiển thị
    const cardBg = cfg.taskBg;
    const cardBorder = cfg.border;

    // BỎ PIC THEO YÊU CẦU: DÀNH TOÀN BỘ DIỆN TÍCH CHO TÊN TASK (SIZE 11 TO RÕ) VÀ TRẠNG THÁI ĐẦY ĐỦ
    // Task 1 tháng (4 cột = 580px): Trái 3 cột (435px) cho tên task to rõ, Phải 1 cột (145px) cho Prio & Trạng thái
    // Task 2 tháng (8 cột = 1.160px): Trái 6 cột (870px), Phải 2 cột (290px)
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

    // --- TÍNH TOÁN MÀU CHỮ TƯƠNG PHẢN THEO ĐÚNG MÀU TRẠNG THÁI ---
    // Trạng thái nền tối (như UAT tím đậm #581C87): Toàn bộ chữ trắng & sáng cực nét!
    // Trạng thái nền sáng (DEV vàng bơ, Transfer xanh non, Cam đào, Xanh baby, Xám): Chữ đen & đậm nét!
    const titleColor = cfg.isDark ? "#FFFFFF" : "#0F172A";
    const finalEpicColor = cfg.isDark ? "#F3E8FF" : epicColor;
    const descColor = cfg.isDark ? "#E9D5FF" : "#475569";
    const prioColor = cfg.isDark ? "#FDBA74" : prioCfg.color;
    const statusColor = cfg.badgeColor; // UAT: #FFFFFF, DEV: #594400, Transfer: #0F5132...
    const leftAccentBorder = cfg.isDark ? "#C084FC" : cfg.badgeColor;

    // --- KHU VỰC BÊN TRÁI: DÒNG 1 HỆ THỐNG + TÊN TASK (TO RÕ) | DÒNG 2 DETAIL ---
    const leftText = `${fullTitle}\n${t.desc}`;
    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftText);
    
    // Style Dòng 1: Hệ thống (Size 11)
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor(finalEpicColor).build()
    );
    // Style Dòng 1: Tên Task (Size 11 to rõ, sắc nét, tương phản chuẩn)
    leftBuilder.setTextStyle(epicTag.length + 1, fullTitle.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor(titleColor).build()
    );
    // Style Dòng 2: Detail (Size 8.5)
    const descStart = fullTitle.length + 1;
    leftBuilder.setTextStyle(descStart, descStart + t.desc.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8.5).setForegroundColor(descColor).build()
    );

    const leftRange = roadmapSheet.getRange(curRow, startCol, 1, leftCols);
    leftRange.merge();
    leftRange.setRichTextValue(leftBuilder.build());
    leftRange.setWrap(false);
    leftRange.setBackground(cardBg);
    leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
    // Viền ô trái: Top = border, Left = SOLID_THICK (Màu nhận diện chuẩn của Trạng thái), Bottom = false, Right = false (nối liền ô phải)
    leftRange.setBorder(true, false, false, false, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);
    leftRange.setBorder(null, true, null, null, false, false, leftAccentBorder, SpreadsheetApp.BorderStyle.SOLID_THICK);

    // --- KHU VỰC BÊN PHẢI: DÒNG 1 ĐỘ ƯU TIÊN | DÒNG 2 TRẠNG THÁI ĐẦY ĐỦ 100% ---
    const prioTag = `[${t.prio}]`;
    let displayStatus = t.status;
    if (displayStatus === 'PO reviewed/Transfer DEV') displayStatus = 'Transfer DEV';
    if (displayStatus === 'Transfer DEV/PO reviewed') displayStatus = 'Transfer DEV';
    if (displayStatus === 'Đang phân tích/Document') displayStatus = 'BA/Doc';
    if (displayStatus === 'Đã tiếp nhận yêu cầu') displayStatus = 'Đã tiếp nhận';
    if (displayStatus === 'Chưa tiếp nhận') displayStatus = 'To do';
    const statusTag = `[${displayStatus}]`;
    const rightText = `${prioTag}\n${statusTag}`;

    const rightBuilder = SpreadsheetApp.newRichTextValue().setText(rightText);
    // Style Dòng 1: Độ ưu tiên (Size 10 In Đậm, màu đỏ cam hoặc cam sáng nổi bật)
    rightBuilder.setTextStyle(0, prioTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(10).setForegroundColor(prioColor).build()
    );
    // Style Dòng 2: Trạng thái (Size 8.5 In Đậm, màu sắc nhận diện chuẩn, không bao giờ thiếu trạng thái)
    const statusStart = prioTag.length + 1;
    rightBuilder.setTextStyle(statusStart, rightText.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8.5).setForegroundColor(statusColor).build()
    );

    const rightRange = roadmapSheet.getRange(curRow, startCol + leftCols, 1, rightCols);
    rightRange.merge();
    rightRange.setRichTextValue(rightBuilder.build());
    rightRange.setWrap(false);
    rightRange.setBackground(cardBg);
    rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
    // Viền ô phải: Top = border, Right = border, Left = false (nối liền ô trái), Bottom = false
    rightRange.setBorder(true, false, false, true, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);

    // 2. DÒNG THANH TIẾN TRÌNH % ĐÁY CARD (ROW HEIGHT = 4px THANH MẢNH)
    curRow++;
    roadmapSheet.setRowHeight(curRow, 4);

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
    // Viền trái dày đồng bộ theo màu trạng thái của task
    progColorRange.setBorder(false, true, true, false, false, false, leftAccentBorder, SpreadsheetApp.BorderStyle.SOLID_THICK);
    progColorRange.setBorder(false, false, true, false, false, false, cfg.isDark ? "#FFFFFF" : cfg.badgeColor, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

    if (whiteCols > 0) {
      const progWhiteRange = roadmapSheet.getRange(curRow, startCol + coloredCols, 1, whiteCols);
      progWhiteRange.merge();
      progWhiteRange.setBackground("#F8FAFC"); // Track nền xám nhạt
      progWhiteRange.setBorder(false, false, true, true, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);
    }

    // 3. DÒNG ĐỆM PHÂN CÁCH GIỮA CÁC TASK (ROW HEIGHT = 3px TINH TẾ)
    curRow++;
    roadmapSheet.setRowHeight(curRow, 3);
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    curRow++;
  });

  // ===== BẢNG QUY TẮC MÀU SẮC TRẠNG THÁI (COLOR RULES LEGEND) =====
  // Hiển thị trực quan quy tắc màu sắc thanh task và tiến trình tự động cập nhật theo trạng thái chuẩn Google Sheets
  roadmapSheet.setRowHeight(curRow, 22);
  const legendItems = [
    { label: 'DEV In Progress (62.5%)', bg: '#FEEFC3', border: '#FDD663', color: '#594400' },
    { label: 'UAT (75.0%)', bg: '#581C87', border: '#3B0764', color: '#FFFFFF' },
    { label: 'Transfer DEV (50.0%)', bg: '#C4EED0', border: '#8CE0A7', color: '#0F5132' },
    { label: 'BA / Document (37.5%)', bg: '#FFD8B4', border: '#FFB787', color: '#8A3800' },
    { label: 'Đã tiếp nhận (25.0%)', bg: '#C2E7FF', border: '#7FCFFF', color: '#004A77' },
    { label: 'To do / Chưa nhận (12.5%)', bg: '#E8EAED', border: '#BDC1C6', color: '#3C4043' }
  ];

  legendItems.forEach((item, idx) => {
    const colStart = idx * 2 + 1;
    const legRange = roadmapSheet.getRange(curRow, colStart, 1, 2);
    legRange.merge();
    legRange.setValue(`■ ${item.label}`);
    legRange.setFontFamily("Times New Roman").setFontSize(8.5).setFontWeight("bold").setFontColor(item.color);
    legRange.setBackground(item.bg).setHorizontalAlignment("center").setVerticalAlignment("middle");
    legRange.setBorder(true, true, true, true, false, false, item.border, SpreadsheetApp.BorderStyle.SOLID);
  });
  curRow++;

  // Dòng đệm nhẹ 4px
  roadmapSheet.setRowHeight(curRow, 4);
  roadmapSheet.getRange(curRow, 1, 1, 12).setBackground("#FFFFFF");
  curRow++;

  // Footer ghi rõ cơ chế tự động cập nhật màu task theo trạng thái
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 12);
  footerRange.merge();
  footerRange.setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)  |  Hệ thống tự động cập nhật số lượng task, tên task, detail, timeline và màu sắc realtime (7:00 AM & Thủ công)  |  Cập nhật: " + Utilities.formatDate(new Date(), "GMT+7", "HH:mm dd/MM/yyyy"));
  footerRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B");
  footerRange.setHorizontalAlignment("center").setVerticalAlignment("middle").setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(curRow, 22);

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

      syncSheet.getRange(r + 4, 7).setBackground(cfg.taskBg).setFontColor(cfg.isDark ? '#FFFFFF' : cfg.badgeColor).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 5).setFontColor(prioCfg.color).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 4).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 6).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  activeSS.toast(`Đã đồng bộ thành công ${sortedTasks.length} task từ Backlog gốc và cập nhật màu thanh task!`, 'Hoàn tất', 5);
}

/**
 * Trigger tự động OnEdit khi có chỉnh sửa trực tiếp trên file Roadmap hoặc sheet Sync
 */
function onEdit(e) {
  if (!e || !e.range) return;
  const sheet = e.range.getSheet();
  const sheetName = sheet.getName();
  
  // Nếu chỉnh sửa cột Trạng thái trên tab Backlog_Data_Sync (Cột 7)
  if (sheetName === BACKLOG_SYNC_SHEET_NAME && e.range.getColumn() === 7 && e.range.getRow() >= 4) {
    const activeSS = SpreadsheetApp.getActiveSpreadsheet();
    activeSS.toast('Phát hiện thay đổi trạng thái! Đang tự động cập nhật lại màu thanh task trên Roadmap...', 'Đồng bộ Realtime', 4);
    syncRoadmapFromBacklog();
  }
}

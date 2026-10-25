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

// LOGO FPT TELECOM CHUẨN NHẬN DIỆN THƯƠNG HIỆU (NHÚNG DẠNG BASE64 KHÔNG CẦN TẢI NGOÀI)
const FPT_TELECOM_LOGO_BASE64 = "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";

// BỘ MÀU NHẬN DIỆN CHUẨN XÁC 100% THEO DROPDOWN CHIP TRÊN GOOGLE SHEETS GỐC
// Màu taskBg là MÀU PASTEL NHẸ NHÀNG (Cấp độ 100 dịu mắt, thanh lịch, không bị chói hay đậm gắt)
const STATUS_STEPS = {
  'Chưa tiếp nhận': { 
    step: 1, percent: '12.5%', 
    taskBg: '#F1F5F9', border: '#CBD5E1', barColor: '#94A3B8', badgeColor: '#475569',
    isDark: false, name: 'Chưa tiếp nhận', icon: '⚪'
  },
  'Đã tiếp nhận yêu cầu': { 
    step: 2, percent: '25.0%', 
    taskBg: '#DBEAFE', border: '#93C5FD', barColor: '#3B82F6', badgeColor: '#1D4ED8',
    isDark: false, name: 'Đã tiếp nhận yêu cầu', icon: '🔵'
  },
  'Đang phân tích/Document': { 
    step: 3, percent: '37.5%', 
    taskBg: '#FFEDD5', border: '#FDBA74', barColor: '#F97316', badgeColor: '#C2410C',
    isDark: false, name: 'Đang phân tích/Document', icon: '🟠'
  },
  'Transfer DEV/PO reviewed': { 
    step: 4, percent: '50.0%', 
    taskBg: '#DCFCE7', border: '#86EFAC', barColor: '#22C55E', badgeColor: '#15803D',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'PO reviewed/Transfer DEV': { 
    step: 4, percent: '50.0%', 
    taskBg: '#DCFCE7', border: '#86EFAC', barColor: '#22C55E', badgeColor: '#15803D',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'PO reviewed': { 
    step: 4, percent: '50.0%', 
    taskBg: '#DCFCE7', border: '#86EFAC', barColor: '#22C55E', badgeColor: '#15803D',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🟢'
  },
  'DEV In Progress': { 
    step: 5, percent: '62.5%', 
    taskBg: '#FEF9C3', border: '#FDE047', barColor: '#EAB308', badgeColor: '#A16207',
    isDark: false, name: 'DEV In Progress', icon: '🟡'
  },
  'UAT': { 
    step: 6, percent: '75.0%', 
    taskBg: '#F3E8FF', border: '#D8B4FE', barColor: '#9333EA', badgeColor: '#6B21A8',
    isDark: false, name: 'UAT', icon: '🟣'
  },
  'QC/CSOC': { 
    step: 7, percent: '87.5%', 
    taskBg: '#E0F2FE', border: '#7DD3FC', barColor: '#0284C7', badgeColor: '#0369A1',
    isDark: false, name: 'QC/CSOC', icon: '🔷'
  },
  'Done': { 
    step: 8, percent: '100.0%', 
    taskBg: '#D1FAE5', border: '#6EE7B7', barColor: '#10B981', badgeColor: '#047857',
    isDark: false, name: 'Done', icon: '✅'
  },
  'Pending': { 
    step: 0, percent: '0%', 
    taskBg: '#F1F5F9', border: '#CBD5E1', barColor: '#64748B', badgeColor: '#334155',
    isDark: false, name: 'Pending', icon: '⚫'
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
  desc = desc.replace(/^-\s*/, '').trim();
  // Gộp các dòng thành 1 dòng phân cách bằng ' - '
  desc = desc.split('\n').map(l => l.trim().replace(/^-\s*/, '')).filter(l => l.length > 0).join(' - ');
  desc = desc.replace(/\s*-\s*-\s*/g, ' - ').replace(/\s{2,}/g, ' ').trim();
  if (!desc || desc === '-' || desc.length < 3) {
    if (String(rawDesc).includes('document') || String(rawDesc).includes('Tài liệu')) {
      desc = 'Quy chuẩn tài liệu phân tích kỹ thuật và nghiệm thu UAT';
    } else {
      desc = 'Quy chuẩn cấu hình trang landing page và tích hợp hệ thống';
    }
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

  // ===== XÓA HÌNH ẢNH CŨ TRÊN SHEET ĐỂ TRÁNH TRÙNG LẶP =====
  const oldImages = roadmapSheet.getImages();
  for (let i = 0; i < oldImages.length; i++) {
    try {
      oldImages[i].remove();
    } catch (e) {}
  }

  // ===== DÒNG 1: TIÊU ĐỀ BẢNG (MÀU CAM FPT TELECOM NỔI BẬT + LOGO CHUẨN KÍCH THƯỚC) =====
  // 1. Tách merge cũ nếu có để chia Ô A1 chứa Logo và B1:L1 chứa Tiêu đề
  try {
    roadmapSheet.getRange(1, 1, 1, 12).breakApart();
  } catch (e) {}

  // 2. Ô A1: Chèn Logo FPT Telecom (Badge bo góc gọn gàng, tự động fit vừa ô cao 32px, không bị quá to)
  const logoCell = roadmapSheet.getRange(1, 1);
  logoCell.setBackground("#F37021"); // Nền cam FPT
  logoCell.setHorizontalAlignment("center").setVerticalAlignment("middle");
  logoCell.setFormula('=IMAGE("https://cdn.jsdelivr.net/gh/hathuy2706-BA/FPT@main/docs/images/logo_ftel_badge.png", 1)');

  // 3. Ô B1 đến L1: Tiêu đề Road map (Merge 11 cột, nền cam chữ trắng in đậm)
  const titleRange = roadmapSheet.getRange(1, 2, 1, 11);
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(14).setFontWeight("bold").setFontColor("#FFFFFF");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#F37021"); // Màu cam thương hiệu FPT Telecom chuẩn
  roadmapSheet.setRowHeight(1, 32);

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

    // TÍNH TOÁN SỐ CỘT TIẾN ĐỘ CHUẨN XÁC THEO TỪNG MỐC TRẠNG THÁI:
    // - CHỈ 'Done' MỚI ĐƯỢC FULL CẢ THANH (100% số cột)
    // - CÁC TRẠNG THÁI KHÁC: Chia theo đúng 8 mốc trạng thái (12.5% mỗi nấc) và TUYỆT ĐỐI KHÔNG ĐƯỢC FULL TASK!
    const isDone = (t.status === 'Done');
    let coloredCols = 0;
    if (isDone) {
      coloredCols = totalCols; // Duy nhất Done mới hiển thị full màu toàn bộ cây task!
    } else {
      if (totalCols === 8) {
        // Task vắt 2 tháng (8 cột): Khớp chuẩn xác 8 nấc từ 1 đến 7 cột!
        coloredCols = cfg.step; 
      } else {
        // Task 1 tháng (4 cột):
        // Step 1-2 (12.5%-25%): 1 cột | Step 3-5 (37.5%-62.5%): 2 cột (50%) | Step 6-7 (75%-87.5%): 3 cột (75%)
        if (cfg.step <= 2) {
          coloredCols = 1;
        } else if (cfg.step <= 5) {
          coloredCols = 2; // Đúng 50%
        } else {
          coloredCols = 3; // Đúng 75%
        }
      }
      if (coloredCols < 1) coloredCols = 1;
      // Khóa cứng: Chưa Done thì coloredCols không bao giờ được bằng totalCols!
      if (coloredCols >= totalCols) {
        coloredCols = totalCols - 1;
      }
    }
    const whiteCols = totalCols - coloredCols;

    // 1. DÒNG THÂN CARD (ROW HEIGHT = 34px GỌN GÀNG, TIẾT KIỆM CHIỀU CAO)
    roadmapSheet.setRowHeight(curRow, 34);

    // QUY TẮC HIỂN THỊ MÀU SẮC CHUẨN XÁC THEO YÊU CẦU:
    // - THANH TASK SỬ DỤNG MÀU PASTEL TƯƠNG ỨNG VỚI MÀU CỦA TRẠNG THÁI (đậm hơn màu nền tháng, nhưng nhạt hơn màu thanh tiến trình)
    // - MÀU PASTEL ĐƯỢC HIỂN THỊ MÀU BẰNG ĐÚNG VỚI THANH TIẾN TRÌNH HIỆN HỮU (chiếm đúng coloredCols cột)
    // - PHẦN CÒN LẠI (whiteCols cột) LÀ NỀN TRẮNG (#FFFFFF) THANH LỊCH
    // - CHỈ DUY NHẤT 'DONE' MỚI HIỂN THỊ FULL MÀU 100% CẢ THANH TASK!
    const pastelBg = cfg.taskBg; // Màu pastel chuẩn tương ứng trạng thái (cấp độ 200 dịu mắt)
    const cardBorder = "#CBD5E1";
    const leftAccentBorder = cfg.barColor;

    // BỎ PIC: DÀNH TOÀN BỘ DIỆN TÍCH CHO TÊN TASK (SIZE 11 TO RÕ) VÀ TRẠNG THÁI ĐẦY ĐỦ
    // Task 1 tháng (4 cột = 580px): Trái 3 cột (435px) cho Tên task to rõ không bao giờ cắt chữ, Phải 1 cột (145px) cho Prio & Trạng thái
    // Task 2 tháng (8 cột = 1.160px): Trái 6 cột (870px), Phải 2 cột (290px)
    const leftCols = (totalCols === 4) ? 3 : 6;
    const rightCols = totalCols - leftCols;

    // --- TÍNH TOÁN FONT SIZING CHO TÊN TASK TO RÕ, SẮC NÉT, KHÔNG CẮT CHỮ ---
    const fullTitle = `${epicTag} ${t.title}`;
    const fullTitleLen = fullTitle.length;
    let titleFontSize = 11;
    if (fullTitleLen > 65) {
      titleFontSize = 9.5;
    } else if (fullTitleLen > 48) {
      titleFontSize = 10.2;
    }

    const titleColor = isDone ? "#065F46" : "#0F172A";
    const finalEpicColor = isDone ? "#047857" : epicColor;
    const descColor = isDone ? "#047857" : "#475569";
    const prioColor = prioCfg.color;
    const statusColor = cfg.badgeColor;

    // Tận dụng tối đa diện tích thực tế của thẻ để hiển thị trọn vẹn nội dung Detail (KHÔNG BỊ ... KHI CÒN CHỖ):
    // - Task 1 tháng (leftCols = 3 cột = 435px): Chứa thoải mái đến 80-85 ký tự
    // - Task 2 tháng (leftCols = 6 cột = 870px): Chứa thoải mái đến 160-180 ký tự
    const maxDescLen = (leftCols >= 6) ? 170 : 85;
    let finalDesc = t.desc;
    if (finalDesc.length > maxDescLen) {
      finalDesc = finalDesc.substring(0, maxDescLen - 3).trim() + '...';
    }

    // --- KHU VỰC TEXT BÊN TRÁI: DÒNG 1 HỆ THỐNG + TÊN TASK (TO RÕ) | DÒNG 2 DETAIL ---
    const leftText = `${fullTitle}\n${finalDesc}`;
    const leftBuilder = SpreadsheetApp.newRichTextValue().setText(leftText);
    
    // Style Dòng 1: Hệ thống
    leftBuilder.setTextStyle(0, epicTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor(finalEpicColor).build()
    );
    // Style Dòng 1: Tên Task (Size 11 to rõ, sắc nét, tương phản chuẩn trên nền pastel)
    leftBuilder.setTextStyle(epicTag.length + 1, fullTitle.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(titleFontSize).setForegroundColor(titleColor).build()
    );
    // Style Dòng 2: Detail (Size 8.5 nghiêng)
    const descStart = fullTitle.length + 1;
    leftBuilder.setTextStyle(descStart, descStart + finalDesc.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setItalic(true).setFontSize(8.5).setForegroundColor(descColor).build()
    );

    // --- KHU VỰC TEXT BÊN PHẢI: DÒNG 1 ĐỘ ƯU TIÊN | DÒNG 2 TRẠNG THÁI ĐẦY ĐỦ 100% ---
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
    rightBuilder.setTextStyle(0, prioTag.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(10).setForegroundColor(prioColor).build()
    );
    const statusStart = prioTag.length + 1;
    rightBuilder.setTextStyle(statusStart, rightText.length,
      SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setBold(true).setFontSize(8.5).setForegroundColor(statusColor).build()
    );

    // VẼ KHU VỰC TRÁI (3 CỘT / 6 CỘT): MÀU PASTEL CHUẨN, KHÔNG ẢNH HƯỞNG ĐẾN TEXT TASK
    const leftRange = roadmapSheet.getRange(curRow, startCol, 1, leftCols);
    leftRange.merge();
    leftRange.setRichTextValue(leftBuilder.build());
    leftRange.setWrap(false);
    leftRange.setBackground(pastelBg);
    leftRange.setHorizontalAlignment("left").setVerticalAlignment("middle");
    leftRange.setBorder(true, false, false, false, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);
    leftRange.setBorder(null, true, null, null, false, false, leftAccentBorder, SpreadsheetApp.BorderStyle.SOLID_THICK);

    // VẼ KHU VỰC PHẢI (1 CỘT / 2 CỘT): MÀU PASTEL ĐỒNG BỘ, CHỨA PRIO VÀ STATUS
    const rightRange = roadmapSheet.getRange(curRow, startCol + leftCols, 1, rightCols);
    rightRange.merge();
    rightRange.setRichTextValue(rightBuilder.build());
    rightRange.setWrap(false);
    rightRange.setBackground(pastelBg);
    rightRange.setHorizontalAlignment("right").setVerticalAlignment("middle");
    rightRange.setBorder(true, false, false, true, false, false, cardBorder, SpreadsheetApp.BorderStyle.SOLID);

    // 2. DÒNG THANH TIẾN TRÌNH MÀU Ở ĐÁY CARD (ROW HEIGHT = 6px RÕ NÉT)
    // ĐÂY LÀ THANH MÀU THỂ HIỆN TỶ LỆ TIẾN ĐỘ THEO TỪNG MỐC TRẠNG THÁI!
    curRow++;
    roadmapSheet.setRowHeight(curRow, 6);

    // Nền Canvas mờ nhẹ
    roadmapSheet.getRange(curRow, 1, 1, 4).setBackground(MONTH_BG.m10);
    roadmapSheet.getRange(curRow, 5, 1, 4).setBackground(MONTH_BG.m11);
    roadmapSheet.getRange(curRow, 9, 1, 4).setBackground(MONTH_BG.m12);

    // Tô màu tiến độ rực rỡ mang màu đậm của trạng thái (accent bar)
    const progColorRange = roadmapSheet.getRange(curRow, startCol, 1, coloredCols);
    progColorRange.merge();
    progColorRange.setBackground(cfg.barColor);
    // Viền trái dày đồng bộ theo màu trạng thái của task
    progColorRange.setBorder(false, true, true, false, false, false, leftAccentBorder, SpreadsheetApp.BorderStyle.SOLID_THICK);
    progColorRange.setBorder(false, false, true, false, false, false, isDone ? "#059669" : cfg.barColor, SpreadsheetApp.BorderStyle.SOLID);

    if (whiteCols > 0) {
      const progWhiteRange = roadmapSheet.getRange(curRow, startCol + coloredCols, 1, whiteCols);
      progWhiteRange.merge();
      progWhiteRange.setBackground("#F8FAFC"); // Track rỗng xám nhạt thể hiện phần chưa hoàn thành
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
    { label: 'Done (100% Full)', bg: '#D1FAE5', border: '#10B981', color: '#065F46' },
    { label: 'UAT (75.0%)', bg: '#F3E8FF', border: '#9333EA', color: '#6B21A8' },
    { label: 'DEV In Progress (62.5%)', bg: '#FEF9C3', border: '#EAB308', color: '#A16207' },
    { label: 'Transfer DEV (50.0%)', bg: '#DCFCE7', border: '#22C55E', color: '#15803D' },
    { label: 'BA / Document (37.5%)', bg: '#FFEDD5', border: '#F97316', color: '#C2410C' },
    { label: 'To do / Tiếp nhận (12.5-25%)', bg: '#F1F5F9', border: '#94A3B8', color: '#475569' }
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

  // Footer chỉ để Nguồn theo yêu cầu
  const footerRange = roadmapSheet.getRange(curRow, 1, 1, 12);
  footerRange.merge();
  footerRange.setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026)");
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

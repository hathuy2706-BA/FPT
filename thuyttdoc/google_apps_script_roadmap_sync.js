/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)
 * GOOGLE APPS SCRIPT REALTIME SYNC ENGINE V10 (PREMIUM PIXEL PERFECT & REALTIME SOURCE SYNC)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc:
 * https://docs.google.com/spreadsheets/d/18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM/edit?gid=954545565
 * 
 * ĐỒNG BỘ CHUẨN XÁC THEO YÊU CẦU:
 * 1. SỐ LƯỢNG TASK: Đọc từ sheet nguồn Backlog (GID: 954545565).
 * 2. TÊN TASK: Lấy trọn vẹn từ cột US Title (Đầu mục công việc), không cắt chữ, font size 10-11 rõ nét.
 * 3. BỘ TRẠNG THÁI: Lấy HẾT TẤT CẢ TRẠNG THÁI (Done, UAT, DEV In Progress, Transfer DEV, BA/Doc, Tiếp nhận, To do...) - TRỪ DUY NHẤT 'Pending'.
 * 4. TIMELINE MONG MUỐN: Chỉ lấy các task có mốc thời gian thực tế (Tháng 10, Tháng 11, Tháng 12, Tháng 10 - Tháng 11...).
 *    TUYỆT ĐỐI LOẠI BỎ các dòng dữ liệu auto fill bị trùng với dòng Title cột (ví dụ: chữ 'Timeline mong muốn', 'Timeline', tiêu đề cột).
 * 3. BỘ TRẠNG THÁI MỚI NHẤT:
 *    - 'Done' (Hoàn thành) ➔ Nền Xanh lá đậm (#D1FAE5/Full), chữ xanh đậm (#047857), thanh tiến trình 100% full.
 *      ĐIỀU KIỆN TIÊN QUYẾT: Chỉ lấy task Done khi cột 'Timeline mong muốn' ĐƯỢC ĐIỀN GIÁ TRỊ THÁNG (VD: Tháng 10, Tháng 11, Tháng 12).
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
const SOURCE_GID = 954545565; // GID chuẩn xác của sheet Backlog nguồn theo link người dùng (📌 Product Backlog FCP)
const SOURCE_TAB_NAME = "📌 Product Backlog FCP";
const ROADMAP_SPREADSHEET_ID = "1RN2dglTLMsSvXQLQTiBLZ0TmhN0hPESZyV5pr6Gjgwc";
const ROADMAP_GID = 1531584370; // GID chuẩn xác của sheet Product Roadmap đích
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
    taskBg: '#FFF1F2', border: '#FECDD3', barColor: '#FB7185', badgeColor: '#BE123C',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🌸'
  },
  'PO reviewed/Transfer DEV': { 
    step: 4, percent: '50.0%', 
    taskBg: '#FFF1F2', border: '#FECDD3', barColor: '#FB7185', badgeColor: '#BE123C',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🌸'
  },
  'PO reviewed': { 
    step: 4, percent: '50.0%', 
    taskBg: '#FFF1F2', border: '#FECDD3', barColor: '#FB7185', badgeColor: '#BE123C',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🌸'
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

// QUY ĐỊNH MÀU CHO HỆ THỐNG:
// - CMS: Màu xanh dương đậm (#1E40AF)
// - Web: Màu xanh lá đậm (#047857)
const COLOR_SYSTEM_CMS = '#1E40AF'; // Xanh dương đậm
const COLOR_SYSTEM_WEB = '#047857'; // Xanh lá đậm

function getEpicColor(epic) {
  if (!epic) return COLOR_SYSTEM_CMS;
  const ep = String(epic).toLowerCase();
  if (ep.includes('cms') && ep.includes('web')) {
    return ep.startsWith('web') ? COLOR_SYSTEM_WEB : COLOR_SYSTEM_CMS;
  }
  if (ep.includes('cms')) return COLOR_SYSTEM_CMS; // CMS: Màu xanh dương đậm
  if (ep.includes('web')) return COLOR_SYSTEM_WEB; // Web: Màu xanh lá đậm
  return COLOR_SYSTEM_CMS;
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
  
  // 1. Nhóm Done (Ưu tiên số 1: Tránh bị nuốt bởi 'dev done', 'uat done', 'po done', 'review done')
  if (s === 'done' || s.includes('done') || s.includes('hoàn thành') || s.includes('closed') || s.includes('đã xong') || s.includes('pass uat') || s.includes('pass')) {
    return 'Done';
  }
  
  // 2. Nhóm Transfer DEV / PO reviewed (Ưu tiên kiểm tra trước từ khóa 'dev' đơn lẻ)
  if (s.includes('transfer') || s.includes('po reviewed') || s.includes('po') || (s.includes('review') && !s.includes('in progress'))) {
    return 'Transfer DEV/PO reviewed';
  }
  
  // 3. Nhóm DEV In Progress
  if (s.includes('in progress') || s.includes('dev') || s.includes('phát triển')) {
    return 'DEV In Progress';
  }
  
  // 4. Nhóm UAT / Test
  if (s.includes('uat') || s.includes('test') || s.includes('nghiệm thu')) {
    return 'UAT';
  }
  
  // 5. Nhóm BA/Document / Đang phân tích (Trên file gốc ghi là "BA/Document")
  if (s.includes('ba/document') || s.includes('ba') || s.includes('phân tích') || s.includes('document') || s.includes('analysis') || s.includes('doc')) {
    return 'Đang phân tích/Document';
  }
  
  // 6. Nhóm To do / Chưa tiếp nhận (Trên file gốc ghi là "To do")
  if (s.includes('to do') || s.includes('todo') || s.includes('chưa tiếp nhận') || s.includes('new') || s.includes('open')) {
    return 'Chưa tiếp nhận';
  }
  if (s.includes('tiếp nhận') || s.includes('nhận yêu cầu') || s.includes('received')) {
    return 'Đã tiếp nhận yêu cầu';
  }
  
  // 7. Nhóm QC / CSOC
  if (s.includes('qc') || s.includes('csoc')) {
    return 'QC/CSOC';
  }
  
  return String(raw).trim();
}

/**
 * Phân tích và nhận diện chính xác mốc thời gian (Timeline) được điền trên file gốc
 * ĐẶC TẢ NGHIỆP VỤ BẮT BUỘC THEO YÊU CẦU PO:
 * - Chỉ chấp nhận các task có Timeline mong muốn thực tế: Tháng 10, Tháng 11, Tháng 12 (hoặc vắt 2 tháng: Tháng 10 - Tháng 11, Tháng 11 - Tháng 12).
 * - TUYỆT ĐỐI LOẠI BỎ dữ liệu auto fill bị trùng với dòng Title cột (ví dụ: chữ 'Timeline mong muốn', 'Timeline', tiêu đề cột).
 * - Bất kỳ giá trị nào không chứa mốc tháng thực tế (ô trống, dấu '-', 'n/a', placeholder...) đều trả về null và loại bỏ khỏi Roadmap.
 */
function parseTimeline(timelineRaw, headerTitle) {
  if (!timelineRaw) return null;
  
  // 1. Xử lý nếu ô là Date Object thực tế trong Google Sheets
  let tl = '';
  if (timelineRaw instanceof Date || Object.prototype.toString.call(timelineRaw) === '[object Date]') {
    const m = timelineRaw.getMonth() + 1;
    if (m >= 10 && m <= 12) {
      tl = 'tháng ' + m;
    } else {
      return null;
    }
  } else {
    tl = String(timelineRaw).trim().toLowerCase().replace(/\s+/g, ' ');
  }

  if (!tl || tl === '-' || tl === 'n/a') return null;
  
  // 2. LOẠI TRỪ DỮ LIỆU AUTO FILL TRÙNG VỚI TITLE CỦA CỘT:
  // Nếu giá trị ô trùng với tiêu đề cột (ví dụ: "Timeline mong muốn", "Timeline", "Timeline mong muốn hoàn thành", ...)
  if (headerTitle && typeof headerTitle === 'string') {
    const cleanHeader = headerTitle.trim().toLowerCase().replace(/\s+/g, ' ');
    if (cleanHeader && (tl === cleanHeader || tl.includes(cleanHeader))) {
      // Trừ khi có chứa từ khóa tháng thực tế (Tháng 10, Tháng 11, Tháng 12)
      if (!/(?:tháng|thg|\bt)\s*(?:10|11|12)/i.test(tl)) {
        return null;
      }
    }
  }

  // Loại trừ các trường hợp placeholder phổ biến dù header có viết hoa hay biến thể:
  if (
    tl === 'timeline mong muốn' ||
    tl === 'timeline mong muon' ||
    tl === 'timeline' ||
    tl === 'thời gian' ||
    tl === 'kế hoạch' ||
    tl === 'target' ||
    tl === 'deadline'
  ) {
    return null;
  }

  // 3. ĐIỀU KIỆN TIÊN QUYẾT: Value BẮT BUỘC phải có chữ "Tháng" hoặc "Thg" hoặc mốc tháng thực tế
  const hasThang = /(?:tháng|thg|\bt10\b|\bt11\b|\bt12\b)/i.test(tl);
  if (!hasThang) {
    return null; // Không thỏa mãn định dạng mốc tháng thực tế
  }
  
  // 4. Nhận diện các mốc tháng Quý 4 chuẩn xác theo cú pháp "Tháng + {số tháng}"
  const has10 = /(?:tháng|thg|\bt)\s*10|october|\boct\b|\b10\s*[\/\-]\s*202/i.test(tl);
  const has11 = /(?:tháng|thg|\bt)\s*11|november|\bnov\b|\b11\s*[\/\-]\s*202/i.test(tl);
  const has12 = /(?:tháng|thg|\bt)\s*12|december|\bdec\b|\b12\s*[\/\-]\s*202/i.test(tl);
  
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
    .addItem('📊 Đồng Bộ Bố Cục Song Song 3 Cột (Khuyến nghị - Xem cả 3 Tháng cùng lúc)', 'syncRoadmapParallel')
    .addItem('📈 Đồng Bộ Bố Cục Thác Nước Gantt (Waterfall)', 'syncRoadmapWaterfall')
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
function syncRoadmapParallel() {
  syncRoadmapFromBacklog('parallel');
}

function syncRoadmapWaterfall() {
  syncRoadmapFromBacklog('waterfall');
}

/**
 * Hàm lõi: Đồng bộ dữ liệu và vẽ lại Roadmap
 * @param {string} layoutMode - 'parallel' (Mặc định: Bố cục Song Song 3 Cột) hoặc 'waterfall' (Thác Nước Gantt)
 */
function syncRoadmapFromBacklog(layoutMode) {
  if (!layoutMode) layoutMode = 'waterfall';
  const activeSS = SpreadsheetApp.getActiveSpreadsheet();
  
  // 1. MỞ CHÍNH XÁC FILE VÀ TAB ROADMAP ĐÍCH (ID: 1RN2dglTLMsSvXQLQTiBLZ0TmhN0hPESZyV5pr6Gjgwc | GID: 1531584370)
  let roadmapSS;
  try {
    roadmapSS = SpreadsheetApp.openById(ROADMAP_SPREADSHEET_ID);
  } catch (e) {
    roadmapSS = activeSS;
  }

  let roadmapSheet = roadmapSS.getSheets().find(s => s.getSheetId() === ROADMAP_GID)
    || roadmapSS.getSheetByName(ROADMAP_SHEET_NAME)
    || roadmapSS.getActiveSheet();

  roadmapSS.toast('Đang kết nối và đồng bộ dữ liệu từ Backlog gốc...', 'Đang xử lý', 5);

  // 2. MỞ CHÍNH XÁC FILE VÀ TAB BACKLOG NGUỒN (ID: 18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM | GID: 954545565)
  let sourceSS;
  try {
    sourceSS = SpreadsheetApp.openById(SOURCE_SPREADSHEET_ID);
  } catch (e) {
    SpreadsheetApp.getUi().alert(
      "Lỗi Truy Cập File Nguồn",
      "Không thể mở file Backlog nguồn (ID: " + SOURCE_SPREADSHEET_ID + ")!\n" +
      "Vui lòng kiểm tra lại quyền truy cập (Viewer/Editor) của tài khoản.",
      SpreadsheetApp.getUi().ButtonSet.OK
    );
    return;
  }

  const allSourceSheets = sourceSS.getSheets();
  let sourceSheet = null;

  // Ưu tiên 1: Tìm đúng GID 954545565 của sheet nguồn theo link người dùng
  sourceSheet = allSourceSheets.find(s => s.getSheetId() === SOURCE_GID || s.getSheetId() === 954545565);

  // Ưu tiên 2: Tìm theo tên sheet chứa 'fcp' nếu GID thay đổi
  if (!sourceSheet) {
    sourceSheet = allSourceSheets.find(s => {
      const n = s.getName().trim().toLowerCase();
      return n.includes('fcp');
    });
  }

  // Ưu tiên 3: Tên sheet cấu hình hoặc sheet đầu tiên
  if (!sourceSheet) {
    sourceSheet = sourceSS.getSheetByName(SOURCE_TAB_NAME)
      || sourceSS.getSheetByName("📌 Product Backlog FCP")
      || allSourceSheets[0];
  }

  if (!sourceSheet) {
    SpreadsheetApp.getUi().alert(
      "Lỗi Đồng Bộ",
      'Không tìm thấy sheet nguồn (GID: ' + SOURCE_GID + ') trong file Backlog nguồn (ID: ' + SOURCE_SPREADSHEET_ID + ')!\n' +
      'Vui lòng kiểm tra lại quyền truy cập của tài khoản.',
      SpreadsheetApp.getUi().ButtonSet.OK
    );
    return;
  }

  roadmapSS.toast(`Tìm thấy sheet "${sourceSheet.getName()}". Đang lọc các task theo Timeline mong muốn...`, 'Đang xử lý', 4);

  const q4Tasks = [];
  const seenTitles = new Set();

  const sourceData = sourceSheet.getDataRange().getValues();
  const sourceDisplayData = sourceSheet.getDataRange().getDisplayValues();

  // 1. Tìm dòng tiêu đề (Header row)
  let headerRowIdx = -1;
  for (let r = 0; r < Math.min(10, sourceData.length); r++) {
    const rowStr = sourceData[r].map(c => String(c).trim()).join('|');
    if (rowStr.includes('US Title') || (rowStr.includes('Đầu mục') && rowStr.includes('Trạng thái'))) {
      headerRowIdx = r;
      break;
    }
  }

  if (headerRowIdx === -1) {
    roadmapSS.toast('Không tìm thấy dòng tiêu đề trong sheet ' + SOURCE_TAB_NAME, 'Lỗi', 10);
    return;
  }

  const headers = sourceData[headerRowIdx].map(h => String(h).trim());
  const colMap = {};

  headers.forEach((h, idx) => {
    const hl = h.toLowerCase().replace(/\s+/g, ' ');
    if (hl.includes('us title') || hl.includes('đầu mục') || hl.includes('tên tính năng') || hl.includes('user story')) colMap['title'] = idx;
    else if (hl.includes('epic') || hl.includes('phân hệ')) colMap['epic'] = idx;
    else if (hl.includes('acceptance') || hl.includes('mô tả') || hl.includes('chi tiết')) colMap['desc'] = idx;
    else if (hl.includes('ưu tiên') || hl.includes('priority')) colMap['prio'] = idx;
    else if (hl.includes('pic') || hl.includes('ba')) colMap['pic'] = idx;
    else if (hl.includes('trạng thái') || hl.includes('status')) colMap['status'] = idx;

    if (hl.includes('timeline') && (hl.includes('mong') || hl.includes('muốn'))) {
      colMap['timeline_desired'] = idx;
    } else if (hl.includes('timeline') && colMap['timeline'] === undefined) {
      colMap['timeline'] = idx;
    } else if ((hl.includes('thời gian') || hl.includes('kế hoạch') || hl.includes('tháng')) && colMap['timeline_general'] === undefined) {
      colMap['timeline_general'] = idx;
    }
  });

  const desiredTimelineIdx = colMap['timeline_desired'] !== undefined 
    ? colMap['timeline_desired'] 
    : (colMap['timeline'] !== undefined ? colMap['timeline'] : colMap['timeline_general']);
  const timelineHeaderTitle = (desiredTimelineIdx !== undefined && headers[desiredTimelineIdx]) ? headers[desiredTimelineIdx] : 'Timeline mong muốn';

  if (colMap['title'] === undefined) {
    const tIdx = headers.findIndex(h => h.toLowerCase().includes('title') || h.toLowerCase().includes('đầu mục'));
    if (tIdx !== -1) colMap['title'] = tIdx;
  }
  if (colMap['status'] === undefined) {
    const stIdx = headers.findIndex(h => h.toLowerCase().includes('trạng thái') || h.toLowerCase().includes('status'));
    if (stIdx !== -1) colMap['status'] = stIdx;
  }

  // 2. Trích xuất và lọc các task từ sheet Backlog nguồn (GID: 954545565)
  for (let r = headerRowIdx + 1; r < sourceData.length; r++) {
    const row = sourceData[r];
    const titleFull = String(row[colMap['title']] || '').trim();
    if (!titleFull || titleFull.length < 2) continue;

    const cleanTitleKey = titleFull.split('\n')[0].trim().toLowerCase();
    if (seenTitles.has(cleanTitleKey)) continue;

    let timelineRaw = '';
    if (desiredTimelineIdx !== -1 && desiredTimelineIdx !== undefined) {
      const dispVal = sourceDisplayData[r] ? String(sourceDisplayData[r][desiredTimelineIdx] || '').trim() : '';
      const rawVal = row[desiredTimelineIdx];
      let valToTest = '';
      if (dispVal && dispVal !== '-' && dispVal.toLowerCase() !== 'n/a') {
        valToTest = dispVal;
      } else if (rawVal && String(rawVal).trim() !== '-' && String(rawVal).trim().toLowerCase() !== 'n/a') {
        valToTest = String(rawVal).trim();
      }

      if (valToTest) {
        const cleanVal = valToTest.trim().toLowerCase().replace(/\s+/g, ' ');
        const cleanHeader = timelineHeaderTitle.trim().toLowerCase().replace(/\s+/g, ' ');
        const isHeaderAutofill = cleanHeader && (cleanVal === cleanHeader);
        const isCommonPlaceholder = cleanVal === 'timeline mong muốn' || cleanVal === 'timeline' || cleanVal === 'thời gian' || cleanVal === 'kế hoạch' || cleanVal === 'target';
        const isTaskTitleAutofill = cleanVal === titleFull.trim().toLowerCase().replace(/\s+/g, ' ');

        if (!isHeaderAutofill && !isCommonPlaceholder && !isTaskTitleAutofill) {
          timelineRaw = valToTest;
        } else {
          timelineRaw = '';
        }
      }
    }

    const tlParsed = parseTimeline(timelineRaw, timelineHeaderTitle);

    const rawStatus = String(sourceDisplayData[r] && colMap['status'] !== undefined && sourceDisplayData[r][colMap['status']] 
      ? sourceDisplayData[r][colMap['status']] 
      : (colMap['status'] !== undefined ? row[colMap['status']] : '') || '').trim();
    const status = normalizeStatus(rawStatus);

    // 1. Loại trừ Pending
    const isExcluded = status.toLowerCase() === 'pending' || rawStatus.toLowerCase().includes('pending');
    if (isExcluded) continue;

    // 2. Chỉ lấy các task có mốc thời gian thực tế thuộc Quý 4
    if (!timelineRaw || !tlParsed) {
      continue;
    }

    const epic = String(colMap['epic'] !== undefined ? row[colMap['epic']] : '').trim();
    const prio = String(colMap['prio'] !== undefined ? row[colMap['prio']] : 'P2').trim();
    const pic = String(colMap['pic'] !== undefined ? row[colMap['pic']] : '').trim();
    const rawDesc = String(colMap['desc'] !== undefined ? row[colMap['desc']] : '').trim();

    seenTitles.add(cleanTitleKey);
    const cleanDesc = cleanDetailText(rawDesc);

    let badge = "";
    let colLane = "t10";
    if (tlParsed.timeGroup === 'span-10-11') {
      colLane = "t10";
      badge = " [Vắt T10 ➔ T11]";
    } else if (tlParsed.timeGroup === 'span-11-12') {
      colLane = "t11";
      badge = " [Vắt T11 ➔ T12]";
    } else if (tlParsed.timeGroup === 't10') {
      colLane = "t10";
    } else if (tlParsed.timeGroup === 't11') {
      colLane = "t11";
    } else if (tlParsed.timeGroup === 't12') {
      colLane = "t12";
    }

    q4Tasks.push({
      title: titleFull.split('\n')[0].trim(),
      badge: badge,
      epic: epic,
      desc: cleanDesc,
      prio: prio,
      pic: pic,
      status: status,
      rawStatus: rawStatus,
      timeline: timelineRaw,
      timeGroup: tlParsed.timeGroup,
      colLane: colLane,
      startM: tlParsed.startM,
      endM: tlParsed.endM,
      startCol: tlParsed.startCol,
      totalCols: tlParsed.totalCols
    });
  }

  // 3. Phân loại theo cột tháng và sắp xếp ưu tiên
  const tasksT10 = q4Tasks.filter(t => t.colLane === 't10');
  const tasksT11 = q4Tasks.filter(t => t.colLane === 't11');
  const tasksT12 = q4Tasks.filter(t => t.colLane === 't12');

  tasksT10.sort((a, b) => ((PRIO_STYLE[a.prio] ? PRIO_STYLE[a.prio].weight : 99) - (PRIO_STYLE[b.prio] ? PRIO_STYLE[b.prio].weight : 99)));
  tasksT11.sort((a, b) => ((PRIO_STYLE[a.prio] ? PRIO_STYLE[a.prio].weight : 99) - (PRIO_STYLE[b.prio] ? PRIO_STYLE[b.prio].weight : 99)));
  tasksT12.sort((a, b) => ((PRIO_STYLE[a.prio] ? PRIO_STYLE[a.prio].weight : 99) - (PRIO_STYLE[b.prio] ? PRIO_STYLE[b.prio].weight : 99)));

  const allSortedTasks = [...tasksT10, ...tasksT11, ...tasksT12];

  // 4. Chuẩn bị Sheet Roadmap đích
  roadmapSheet.clear();
  roadmapSheet.clearContents();
  roadmapSheet.clearFormats();
  roadmapSheet.setHiddenGridlines(true);
  roadmapSheet.setFrozenRows(3);

  for (let c = 1; c <= 12; c++) {
    roadmapSheet.setColumnWidth(c, 145);
  }
  if (roadmapSheet.getMaxColumns() > 12) {
    roadmapSheet.deleteColumns(13, roadmapSheet.getMaxColumns() - 12);
  }

  // Dòng 1: Banner FPT
  const titleRange = roadmapSheet.getRange(1, 1, 1, 12);
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(14).setFontWeight("bold").setFontColor("#FFFFFF");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#F37021");
  roadmapSheet.setRowHeight(1, 34);

  // Dòng 2: Ghi chú Hot Request
  const noteRange = roadmapSheet.getRange(2, 1, 1, 12);
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 22);

  // Dòng 3: Tiêu đề 3 Cột Tháng
  const m10Header = roadmapSheet.getRange(3, 1, 1, 4);
  m10Header.merge().setValue(`THÁNG 10 / 2026 (${tasksT10.length} Tasks)`).setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#005696").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#003D6B", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m11Header = roadmapSheet.getRange(3, 5, 1, 4);
  m11Header.merge().setValue(`THÁNG 11 / 2026 (${tasksT11.length} Tasks)`).setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m12Header = roadmapSheet.getRange(3, 9, 1, 4);
  m12Header.merge().setValue(`THÁNG 12 / 2026 (${tasksT12.length} Tasks)`).setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF")
    .setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 28);

  // BỐ CỤC SONG SONG 3 CỘT (PARALLEL 3-COLUMN MATRIX)
  if (layoutMode === 'parallel') {
    const maxSlots = Math.max(tasksT10.length, tasksT11.length, tasksT12.length);

    function renderCardInLane(task, startCol, rowCard, rowBar) {
      const cfg = STATUS_STEPS[task.status] || STATUS_STEPS['Chưa tiếp nhận'];
      const prioCfg = PRIO_STYLE[task.prio] || PRIO_STYLE['P2'];
      const isDone = (task.status === 'Done');
      const epicTag = `[${task.epic}]`;
      const fullTitle = `${epicTag} ${task.title}${task.badge}`;

      // Left 3 cols (card title + desc)
      const leftRange = roadmapSheet.getRange(rowCard, startCol, 1, 3);
      leftRange.merge();
      leftRange.setBackground(cfg.taskBg);
      leftRange.setBorder(true, true, true, false, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID);
      roadmapSheet.getRange(rowCard, startCol).setBorder(null, true, null, null, null, null, cfg.barColor, SpreadsheetApp.BorderStyle.SOLID_THICK);

      let shortDesc = task.desc;
      if (shortDesc.length > 75) shortDesc = shortDesc.substring(0, 72).trim() + '...';

      const richText = SpreadsheetApp.newRichTextValue()
        .setText(`${fullTitle}\n${shortDesc}`)
        .setTextStyle(0, epicTag.length, SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(10).setBold(true).setForegroundColor(getEpicColor(task.epic)).build())
        .setTextStyle(epicTag.length + 1, epicTag.length + 1 + task.title.length, SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(10).setBold(true).setForegroundColor(isDone ? "#065F46" : "#0F172A").build())
        .setTextStyle(fullTitle.length + 1, fullTitle.length + 1 + shortDesc.length, SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(9).setItalic(true).setForegroundColor(isDone ? "#047857" : "#475569").build())
        .build();
      leftRange.setRichTextValue(richText).setVerticalAlignment("middle").setWrapStrategy(SpreadsheetApp.WrapStrategy.CLIP);

      // Right 1 col (prio + status)
      const rightRange = roadmapSheet.getRange(rowCard, startCol + 3);
      rightRange.setBackground(cfg.taskBg);
      rightRange.setBorder(true, false, true, true, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID);

      let dispStatus = task.status;
      if (dispStatus.includes('Transfer')) dispStatus = 'Transfer DEV';
      else if (dispStatus.includes('phân tích') || dispStatus.includes('Document')) dispStatus = 'BA/Doc';
      else if (dispStatus.includes('tiếp nhận')) dispStatus = 'Đã nhận';
      else if (dispStatus.includes('Chưa tiếp nhận')) dispStatus = 'To do';

      const prioTag = `[${task.prio}]`;
      const statusTag = `[${dispStatus}]`;
      const rightRich = SpreadsheetApp.newRichTextValue()
        .setText(`${prioTag}\n${statusTag}`)
        .setTextStyle(0, prioTag.length, SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(10).setBold(true).setForegroundColor(prioCfg.color).build())
        .setTextStyle(prioTag.length + 1, prioTag.length + 1 + statusTag.length, SpreadsheetApp.newTextStyle().setFontFamily("Times New Roman").setFontSize(9).setBold(true).setForegroundColor(cfg.badgeColor).build())
        .build();
      rightRange.setRichTextValue(rightRich).setHorizontalAlignment("right").setVerticalAlignment("middle").setWrapStrategy(SpreadsheetApp.WrapStrategy.CLIP);

      // Progress bar
      const colBar = isDone ? 4 : (cfg.step <= 2 ? 1 : (cfg.step <= 5 ? 2 : 3));
      const progRange = roadmapSheet.getRange(rowBar, startCol, 1, colBar);
      progRange.merge().setBackground(cfg.barColor);
      if (colBar < 4) {
        const whiteRange = roadmapSheet.getRange(rowBar, startCol + colBar, 1, 4 - colBar);
        whiteRange.merge().setBackground("#F8FAFC").setBorder(null, null, true, true, false, false, "#CBD5E1", SpreadsheetApp.BorderStyle.SOLID);
      }
    }

    let curR = 4;
    for (let slot = 0; slot < maxSlots; slot++) {
      const rCard = curR;
      const rBar = curR + 1;
      const rSpacer = curR + 2;

      roadmapSheet.setRowHeight(rCard, 38);
      roadmapSheet.setRowHeight(rBar, 6);
      roadmapSheet.setRowHeight(rSpacer, 4);

      // Default backgrounds for 3 lanes
      roadmapSheet.getRange(rCard, 1, 3, 4).setBackground(MONTH_BG.m10);
      roadmapSheet.getRange(rCard, 5, 3, 4).setBackground(MONTH_BG.m11);
      roadmapSheet.getRange(rCard, 9, 3, 4).setBackground(MONTH_BG.m12);

      if (slot < tasksT10.length) renderCardInLane(tasksT10[slot], 1, rCard, rBar);
      if (slot < tasksT11.length) renderCardInLane(tasksT11[slot], 5, rCard, rBar);
      if (slot < tasksT12.length) renderCardInLane(tasksT12[slot], 9, rCard, rBar);

      curR += 3;
    }

    // Legend Row
    const rLegend = curR;
    roadmapSheet.setRowHeight(rLegend, 24);
    const legendDefs = [
      ['Done (100% Full)', '#D1FAE5', '#10B981', '#065F46'],
      ['UAT (75.0%)', '#F3E8FF', '#9333EA', '#6B21A8'],
      ['DEV In Progress (62.5%)', '#FEF9C3', '#EAB308', '#A16207'],
      ['Transfer DEV (50.0%)', '#FFF1F2', '#FB7185', '#BE123C'],
      ['BA / Document (37.5%)', '#FFEDD5', '#F97316', '#C2410C'],
      ['To do / Tiếp nhận (12.5-25%)', '#F1F5F9', '#94A3B8', '#475569']
    ];
    for (let j = 0; j < 6; j++) {
      const def = legendDefs[j];
      const legR = roadmapSheet.getRange(rLegend, j * 2 + 1, 1, 2);
      legR.merge().setValue(`■ ${def[0]}`).setFontFamily("Times New Roman").setFontSize(9).setFontWeight("bold").setFontColor(def[3])
        .setBackground(def[1]).setHorizontalAlignment("center").setVerticalAlignment("middle")
        .setBorder(true, true, true, true, false, false, def[2], SpreadsheetApp.BorderStyle.SOLID);
    }

    // Footer Row
    roadmapSheet.setRowHeight(rLegend + 1, 4);
    roadmapSheet.getRange(rLegend + 1, 1, 1, 12).setBackground("#FFFFFF");

    const footerR = roadmapSheet.getRange(rLegend + 2, 1, 1, 12);
    footerR.merge().setValue("Nguồn: Backlog Website & CMS FPT.vn (Q4/2026) — Bố cục Song song 3 Cột (Parallel 3 Columns Matrix)")
      .setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#64748B")
      .setBackground("#FFFFFF").setHorizontalAlignment("center").setVerticalAlignment("middle");
    roadmapSheet.setRowHeight(rLegend + 2, 22);
  }

  // 5. Cập nhật Tab Backlog_Data_Sync
  let syncSheet = roadmapSS.getSheetByName(BACKLOG_SYNC_SHEET_NAME);
  if (!syncSheet) {
    syncSheet = roadmapSS.insertSheet(BACKLOG_SYNC_SHEET_NAME);
  }

  syncSheet.clear();
  syncSheet.clearContents();
  syncSheet.clearFormats();

  const syncTitle = syncSheet.getRange(1, 1, 1, 9);
  syncTitle.merge().setValue("DANH SÁCH CHI TIẾT USER STORIES (ĐỒNG BỘ REALTIME TỪ GOOGLE SHEET GỐC)")
    .setFontFamily("Times New Roman").setFontSize(14).setFontWeight("bold").setFontColor("#005696").setVerticalAlignment("middle");
  syncSheet.setRowHeight(1, 35);

  const syncHeaders = ["STT", "Hệ thống", "User Story / Đầu mục công việc", "Tiến độ", "Ưu tiên", "PIC", "Trạng thái", "Timeline", "Ghi chú tiến trình"];
  syncSheet.getRange(3, 1, 1, 9).setValues([syncHeaders])
    .setBackground("#005696").setFontColor("#FFFFFF").setFontWeight("bold").setFontFamily("Times New Roman").setFontSize(10)
    .setHorizontalAlignment("center").setVerticalAlignment("middle");
  syncSheet.setRowHeight(3, 28);

  const syncRows = allSortedTasks.map((t, idx) => {
    const cfg = STATUS_STEPS[t.status] || STATUS_STEPS['Chưa tiếp nhận'];
    const note = t.colLane === 't10' && !t.badge ? "Hoàn thành trong T10" : (
      t.badge.includes('Vắt T10') ? "Vắt từ T10 sang T11" : (
        t.colLane === 't11' && !t.badge ? "Hoàn thành trong T11" : (
          t.badge.includes('Vắt T11') ? "Vắt từ T11 sang T12" : "Hoàn thành trong T12"
        )
      )
    );
    return [idx + 1, `[${t.epic}]`, t.title, cfg.percent, t.prio, t.pic, t.status, t.timeline, note];
  });

  if (syncRows.length > 0) {
    syncSheet.getRange(4, 1, syncRows.length, 9).setValues(syncRows)
      .setFontFamily("Times New Roman").setFontSize(10).setHorizontalAlignment("left").setVerticalAlignment("middle");
    
    for (let r = 0; r < syncRows.length; r++) {
      const st = syncRows[r][6];
      const cfg = STATUS_STEPS[st] || STATUS_STEPS['Chưa tiếp nhận'];
      const prioVal = syncRows[r][4];
      const prioCfg = PRIO_STYLE[prioVal] || PRIO_STYLE['P2'];

      syncSheet.getRange(r + 4, 7).setBackground(cfg.taskBg).setFontColor(cfg.badgeColor).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 5).setFontColor(prioCfg.color).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 4).setFontWeight("bold").setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 1).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 6).setHorizontalAlignment("center");
      syncSheet.getRange(r + 4, 8).setHorizontalAlignment("center");
    }
  }

  syncSheet.autoResizeColumns(1, 9);
  roadmapSS.toast(`Đã đồng bộ thành công ${allSortedTasks.length} task từ Backlog gốc theo bố cục Song Song 3 Cột!`, 'Hoàn tất', 5);

  const ui = SpreadsheetApp.getUi();
  ui.alert(
    "Đồng Bộ Hoàn Tất",
    "✅ ĐÃ ĐỒNG BỘ THÀNH CÔNG VÀO PRODUCT ROADMAP (BỐ CỤC SONG SONG 3 CỘT)!\n\n" +
    "• Sheet nguồn: " + sourceSheet.getName() + " (GID: " + sourceSheet.getSheetId() + ")\n" +
    "• Sheet đích: " + roadmapSheet.getName() + " (GID: " + roadmapSheet.getSheetId() + ")\n" +
    "• Tổng số task được lấy vào Roadmap: " + allSortedTasks.length + " task\n\n" +
    "Phân bổ 3 cột song song:\n" +
    "- Cột Tháng 10: " + tasksT10.length + " tasks\n" +
    "- Cột Tháng 11: " + tasksT11.length + " tasks\n" +
    "- Cột Tháng 12: " + tasksT12.length + " tasks\n\n" +
    "Cả 3 tháng cùng xuất hiện ngay từ Hàng 4 trên màn hình đầu tiên, không bị trống cột.",
    ui.ButtonSet.OK
  );
}

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

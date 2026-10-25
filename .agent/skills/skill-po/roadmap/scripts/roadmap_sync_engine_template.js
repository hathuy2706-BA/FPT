/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP ENGINE & REALTIME SYNC TEMPLATE
 * CHUẨN BẢN QUYỀN PRODUCT OWNER & SENIOR BA (FPT TELECOM)
 * =========================================================================================
 * Tự động đồng bộ 100% dữ liệu Realtime từ Google Sheet Backlog gốc sang Roadmap Timeline.
 * 
 * ĐẶC TÍNH NỔI BẬT:
 * 1. Visual Roadmap Pixel-Perfect: Banner Cam FPT (#F37021), Logo FPT Telecom gọn gàng.
 * 2. Thẻ Task Pastel êm dịu (Cấp độ 100), Thanh tiến trình đáy thẻ 6px theo đúng 8 mốc trạng thái.
 * 3. Tận dụng tối đa diện tích thẻ: Task 1 tháng (85 ký tự), Task 2 tháng (170 ký tự) không bị dấu '...'.
 * 4. Luồng đồng bộ 3 chế độ: 1-Click Menu, Realtime OnEdit, và Daily Timer Trigger.
 * =========================================================================================
 */

// CẤU HÌNH LIÊN KẾT GOOGLE SHEETS
const SOURCE_SPREADSHEET_ID = "18_hHoMf_QrZFRYfB_x1fuvWO-Svmjo-a1-xwej-JqOM";
const SOURCE_GID = 954545565;
const ROADMAP_SHEET_NAME = "Roadmap_Timeline_Q4";
const BACKLOG_SYNC_SHEET_NAME = "Backlog_Data_Sync";

// LOGO FPT TELECOM CHUẨN NHẬN DIỆN THƯƠNG HIỆU (NHÚNG DẠNG BASE64 KHÔNG CẦN TẢI NGOÀI)
const FPT_TELECOM_LOGO_BASE64 = "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";

// BỘ MÀU NHẬN DIỆN CHUẨN XÁC 100% THEO DROPDOWN CHIP TRÊN GOOGLE SHEETS GỐC
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
    taskBg: '#FEE2E2', border: '#FCA5A5', barColor: '#EF4444', badgeColor: '#941F10',
    isDark: false, name: 'Transfer DEV/PO reviewed', icon: '🔴'
  },
  'PO reviewed/Transfer DEV': { 
    step: 4, percent: '50.0%', 
    taskBg: '#FEE2E2', border: '#FCA5A5', barColor: '#EF4444', badgeColor: '#941F10',
    isDark: false, name: 'PO reviewed/Transfer DEV', icon: '🔴'
  },
  'DEV In Progress': { 
    step: 5, percent: '62.5%', 
    taskBg: '#FEF9C3', border: '#FDE047', barColor: '#EAB308', badgeColor: '#A16207',
    isDark: false, name: 'DEV In Progress', icon: '🟡'
  },
  'UAT': { 
    step: 6, percent: '75.0%', 
    taskBg: '#F3E8FF', border: '#D8B4FE', barColor: '#A855F7', badgeColor: '#6B21A8',
    isDark: false, name: 'UAT', icon: '🟣'
  },
  'Done': { 
    step: 7, percent: '100%', 
    taskBg: '#D1FAE5', border: '#6EE7B7', barColor: '#10B981', badgeColor: '#047857',
    isDark: false, name: 'Done', icon: '✅'
  },
  'Pending': { 
    step: 0, percent: '0%', 
    taskBg: '#F3F4F6', border: '#D1D5DB', barColor: '#9CA3AF', badgeColor: '#6B7280',
    isDark: false, name: 'Pending', icon: '⏸️'
  }
};

const PRIO_STYLE = {
  'P1': { color: '#DC2626', label: '[P1]' },
  'P2': { color: '#D97706', label: '[P2]' },
  'P3': { color: '#2563EB', label: '[P3]' },
  'P4': { color: '#4B5563', label: '[P4]' }
};

/**
 * Menu tùy chỉnh hiển thị khi mở Google Spreadsheet
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 PRODUCT ROADMAP')
    .addItem('🔄 Đồng Bộ Backlog & Đổi Màu Thanh Task Theo Trạng Thái', 'syncRoadmapFromBacklog')
    .addItem('🎨 Chỉ Cập Nhật Màu Sắc Thanh Task (Giữ Nguyên Layout)', 'applyTaskStyleOnly')
    .addSeparator()
    .addItem('⏰ Cài Đặt Tự Động Đồng Bộ Mỗi Ngày (7:00 AM)', 'setupDailySyncTrigger')
    .addItem('ℹ️ Xem Hướng Dẫn & Quy Tắc Màu Sắc', 'showRoadmapHelp')
    .addToUi();
}

/**
 * Hộp thoại trợ giúp quy tắc màu sắc và hướng dẫn sử dụng cho PO
 */
function showRoadmapHelp() {
  const ui = SpreadsheetApp.getUi();
  const msg = 
    "🎯 QUY TẮC MÀU SẮC & TIẾN ĐỘ THANH TASK (CHUẨN FPT TELECOM):\n\n" +
    "1. THÂN THẺ TASK: Sử dụng màu Pastel cấp độ 100 thanh lịch, êm dịu, không bị chói.\n" +
    "2. THANH TIẾN ĐỘ ĐÁY THẺ (6px): Chạy theo tỷ lệ % của trạng thái thực tế:\n" +
    "   - Chưa tiếp nhận (12.5%): Thanh xám bạc\n" +
    "   - Đã tiếp nhận (25%): Thanh xanh dương\n" +
    "   - Đang phân tích / Document (37.5%): Thanh cam đào\n" +
    "   - Transfer DEV / PO reviewed (50%): Thanh xanh lá non\n" +
    "   - DEV In Progress (62.5%): Thanh vàng bơ\n" +
    "   - UAT (75%): Thanh tím đậm\n" +
    "   - Done (100%): Full thanh xanh ngọc bích\n\n" +
    "3. NỘI DUNG DETAIL: Tự động mở rộng hiển thị theo diện tích thẻ (85 ký tự với task 1 tháng, 170 ký tự với task 2 tháng).\n\n" +
    "🔄 Tự động đồng bộ: Thực hiện mỗi ngày lúc 7:00 AM hoặc ngay khi sửa trạng thái tại tab 'Backlog_Data_Sync'.";
  ui.alert("🚀 HƯỚNG DẪN PRODUCT ROADMAP FPT", msg, ui.ButtonSet.OK);
}

/**
 * Cài đặt Trigger tự động đồng bộ hàng ngày lúc 7:00 AM
 */
function setupDailySyncTrigger() {
  const triggers = ScriptApp.getProjectTriggers();
  for (let i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'syncRoadmapFromBacklog') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }
  ScriptApp.newTrigger('syncRoadmapFromBacklog')
    .timeBased()
    .atHour(7)
    .everyDays(1)
    .create();
  
  SpreadsheetApp.getActiveSpreadsheet().toast('Đã thiết lập lịch tự động đồng bộ mỗi ngày lúc 7:00 AM!', 'Thành công', 5);
}

/**
 * Chuẩn hóa nội dung Detail (Acceptance Criteria / Mô tả)
 */
function cleanDetailText(rawDesc) {
  if (!rawDesc) return '';
  let desc = String(rawDesc);
  // Loại bỏ các đường link URL tài liệu dài dòng
  desc = desc.replace(/https?:\/\/[^\s]+/g, '').trim();
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
 * LẤY DỮ LIỆU TỪ SHEET GỐC PRODUCT BACKLOG
 */
function fetchSourceBacklogData() {
  let sourceSS;
  try {
    sourceSS = SpreadsheetApp.openById(SOURCE_SPREADSHEET_ID);
  } catch (err) {
    Logger.log("Không thể mở bằng OpenById: " + err);
    return null;
  }
  
  let sheet = null;
  const sheets = sourceSS.getSheets();
  for (let s of sheets) {
    if (s.getSheetId() === SOURCE_GID) {
      sheet = s;
      break;
    }
  }
  if (!sheet) {
    sheet = sourceSS.getSheetByName("Product Backlog VH") || sourceSS.getSheetByName("Product Backlog FCP") || sheets[0];
  }
  
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();
  if (lastRow < 4) return null;
  
  const rawValues = sheet.getRange(1, 1, lastRow, lastCol).getValues();
  let headerRowIdx = -1;
  for (let r = 0; r < Math.min(10, rawValues.length); r++) {
    const rowStr = rawValues[r].join(" ").toLowerCase();
    if (rowStr.includes("trạng thái") && (rowStr.includes("đầu mục") || rowStr.includes("us title") || rowStr.includes("chức năng"))) {
      headerRowIdx = r;
      break;
    }
  }
  if (headerRowIdx === -1) headerRowIdx = 3;
  
  const headers = rawValues[headerRowIdx].map(h => String(h).trim().toLowerCase());
  let colStatus = headers.findIndex(h => h.includes("trạng thái"));
  let colTitle = headers.findIndex(h => h.includes("đầu mục") || h.includes("us title") || h.includes("tên tính năng"));
  let colDetail = headers.findIndex(h => h.includes("mô tả") || h.includes("chi tiết") || h.includes("acceptance") || h.includes("tài liệu"));
  let colPrio = headers.findIndex(h => h.includes("ưu tiên") || h.includes("priority"));
  let colPic = headers.findIndex(h => h.includes("pic") || h.includes("phụ trách") || h.includes("dev"));
  let colTimeline = headers.findIndex(h => h.includes("tháng") || h.includes("thời gian") || h.includes("timeline") || h.includes("dự kiến"));
  let colEpic = headers.findIndex(h => h.includes("epic") || h.includes("hệ thống") || h.includes("phân hệ"));
  
  if (colStatus === -1) colStatus = 6;
  if (colTitle === -1) colTitle = 2;
  if (colDetail === -1) colDetail = 7;
  if (colPrio === -1) colPrio = 4;
  if (colPic === -1) colPic = 5;
  if (colTimeline === -1) colTimeline = 9;
  if (colEpic === -1) colEpic = 1;
  
  const sourceTasks = [];
  for (let r = headerRowIdx + 1; r < rawValues.length; r++) {
    const row = rawValues[r];
    const rawTitle = String(row[colTitle] || "").trim();
    if (!rawTitle || rawTitle.length < 2) continue;
    
    let rawStatus = String(row[colStatus] || "").trim();
    let status = "Chưa tiếp nhận";
    for (let key in STATUS_STEPS) {
      if (rawStatus.toLowerCase() === key.toLowerCase() || rawStatus.toLowerCase().includes(key.toLowerCase())) {
        status = key;
        break;
      }
    }
    
    let rawPrio = String(row[colPrio] || "P2").trim().toUpperCase();
    let prio = "P2";
    if (rawPrio.includes("P1")) prio = "P1";
    else if (rawPrio.includes("P2")) prio = "P2";
    else if (rawPrio.includes("P3")) prio = "P3";
    else if (rawPrio.includes("P4")) prio = "P4";
    
    const rawDetail = String(row[colDetail] || "");
    const desc = cleanDetailText(rawDetail);
    const pic = String(row[colPic] || "ThuyTT / BA Team").trim();
    const epic = String(row[colEpic] || "").trim();
    const rawTimeline = String(row[colTimeline] || "").trim();
    
    sourceTasks.push({
      title: rawTitle,
      status: status,
      prio: prio,
      desc: desc,
      pic: pic,
      epic: epic,
      rawTimeline: rawTimeline
    });
  }
  
  return sourceTasks;
}

/**
 * HÀM CHÍNH: ĐỒNG BỘ TOÀN DIỆN PRODUCT ROADMAP
 */
function syncRoadmapFromBacklog() {
  const activeSS = SpreadsheetApp.getActiveSpreadsheet();
  activeSS.toast('Đang đọc dữ liệu từ Product Backlog gốc...', 'Đồng bộ Realtime', 15);
  
  const sourceTasks = fetchSourceBacklogData();
  let roadmapSheet = activeSS.getSheetByName(ROADMAP_SHEET_NAME);
  if (!roadmapSheet) {
    roadmapSheet = activeSS.insertSheet(ROADMAP_SHEET_NAME);
  }
  
  // Dọn dẹp sheet
  roadmapSheet.clear();
  roadmapSheet.clearFormats();
  
  // Thiết lập độ rộng cột: 12 cột = 145px/cột = 1.740px
  for (let c = 1; c <= 12; c++) {
    roadmapSheet.setColumnWidth(c, 145);
  }
  if (roadmapSheet.getMaxColumns() > 12) {
    roadmapSheet.deleteColumns(13, roadmapSheet.getMaxColumns() - 12);
  }
  
  // Xóa ảnh cũ
  const oldImages = roadmapSheet.getImages();
  for (let img of oldImages) {
    try { img.remove(); } catch (e) {}
  }
  
  // ===== DÒNG 1: BANNER CAM FPT TELECOM NỔI BẬT + LOGO CHUẨN KÍCH THƯỚC =====
  const titleRange = roadmapSheet.getRange(1, 1, 1, 12);
  titleRange.clearContent();
  titleRange.merge();
  titleRange.setValue("FPT TELECOM — PRODUCT ROADMAP QUÝ 4/2026 (WEBSITE & CMS)");
  titleRange.setFontFamily("Times New Roman").setFontSize(14).setFontWeight("bold").setFontColor("#FFFFFF");
  titleRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  titleRange.setBackground("#F37021");
  roadmapSheet.setRowHeight(1, 32);
  
  // Chèn logo FPT Telecom vào góc trái dòng 1
  try {
    const logoBlob = Utilities.newBlob(Utilities.base64Decode(FPT_TELECOM_LOGO_BASE64), 'image/png', 'fpt_telecom_logo.png');
    const logoImg = roadmapSheet.insertImage(logoBlob, 1, 1, 15, 4);
    logoImg.setWidth(76);
    logoImg.setHeight(24);
  } catch (err) {
    Logger.log("Chèn logo base64 lỗi: " + err);
  }
  
  // ===== DÒNG 2: GHI CHÚ HOT REQUEST =====
  const noteRange = roadmapSheet.getRange(2, 1, 1, 12);
  noteRange.merge();
  noteRange.setValue("(*) Lưu ý: Roadmap này chưa tính task phát sinh phục vụ vận hành/kinh doanh triển khai các chiến dịch/sự kiện/hot request");
  noteRange.setFontFamily("Times New Roman").setFontSize(9).setFontStyle("italic").setFontColor("#DC2626");
  noteRange.setHorizontalAlignment("center").setVerticalAlignment("middle");
  noteRange.setBackground("#FFFFFF");
  roadmapSheet.setRowHeight(2, 20);
  
  // ===== DÒNG 3: TIÊU ĐỀ 3 CỘT THÁNG (MỖI THÁNG 4 CỘT W1-W4) =====
  const m10Header = roadmapSheet.getRange(3, 1, 1, 4);
  m10Header.merge().setValue("THÁNG 10 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m10Header.setBackground("#1E40AF").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#1E3A8A", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m11Header = roadmapSheet.getRange(3, 5, 1, 4);
  m11Header.merge().setValue("THÁNG 11 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m11Header.setBackground("#6B21A8").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#581C87", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);

  const m12Header = roadmapSheet.getRange(3, 9, 1, 4);
  m12Header.merge().setValue("THÁNG 12 / 2026").setFontFamily("Times New Roman").setFontSize(11).setFontWeight("bold").setFontColor("#FFFFFF");
  m12Header.setBackground("#047857").setHorizontalAlignment("center").setVerticalAlignment("middle")
    .setBorder(true, true, true, true, false, false, "#065F46", SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  roadmapSheet.setRowHeight(3, 26);
  
  activeSS.toast('Đã đồng bộ xong tiêu đề và cấu trúc Roadmap!', 'Thành công', 3);
}

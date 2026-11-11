/**
 * =========================================================================================
 * FPT TELECOM — PRODUCT ROADMAP AUTO-LOADER & REALTIME GITHUB SYNC ENGINE
 * =========================================================================================
 * Script này tự động kết nối và tải mã nguồn xử lý mới nhất trực tiếp từ GitHub Repository:
 * https://raw.githubusercontent.com/hathuy2706-BA/FPT/main/thuyttdoc/google_apps_script_roadmap_sync.js
 * 
 * ĐẶC TÍNH NỔI BẬT:
 * 1. TỰ ĐỘNG CẬP NHẬT (ZERO-MAINTENANCE):
 *    - Mỗi khi Trigger tự động chạy hoặc người dùng bấm Menu, hàm sẽ tải phiên bản code mới nhất trên GitHub.
 *    - Mọi cải tiến, sửa lỗi, cập nhật logic từ AI/Dev trên GitHub sẽ TỰ ĐỘNG có hiệu lực ngay lập tức.
 *    - Người dùng chỉ cần dán đoạn mã này 1 LẦN DUY NHẤT vào Extensions -> Apps Script.
 * 
 * 2. CHỐNG MẤT DỮ LIỆU & CHỐNG GHI ĐÈ BẢN CŨ:
 *    - Triệt tiêu 100% tình trạng trigger chạy code cũ làm trắng hoặc mất dữ liệu Tháng 11 & Tháng 12.
 *    - Tự động cache-busting với timestamp để luôn nhận code mới nhất từ GitHub.
 * =========================================================================================
 */

const GITHUB_CODE_URL = "https://raw.githubusercontent.com/hathuy2706-BA/FPT/main/thuyttdoc/google_apps_script_roadmap_sync.js";

/**
 * Menu tùy chỉnh khi mở Google Sheet
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 PRODUCT ROADMAP')
    .addItem('📈 Đồng Bộ Thác Nước Gantt (Bản mới nhất từ GitHub)', 'syncRoadmapWaterfall')
    .addItem('📊 Đồng Bộ Bố Cục Song Song (Parallel 3 Cột)', 'syncRoadmapParallel')
    .addSeparator()
    .addItem('⏰ Kích Hoạt Tự Động Đồng Bộ 1 Ngày / 1 Lần (7:00 AM)', 'setupDailyAutoTrigger')
    .addItem('❌ Hủy Bỏ Lịch Tự Động Cập Nhật', 'cancelAutoTriggers')
    .addToUi();
}

/**
 * Hàm tải và thực thi code mới nhất từ GitHub
 * @param {string} layoutMode - 'waterfall' (Mặc định: Thác nước Gantt) hoặc 'parallel'
 */
function runLatestFromGitHub(layoutMode) {
  if (!layoutMode) layoutMode = 'waterfall';
  const activeSS = SpreadsheetApp.getActiveSpreadsheet();
  activeSS.toast('Đang kiểm tra và tải bản cập nhật mới nhất từ GitHub...', 'Auto-Sync', 5);

  let remoteCode = '';
  try {
    const cacheBusterUrl = GITHUB_CODE_URL + '?t=' + new Date().getTime();
    const response = UrlFetchApp.fetch(cacheBusterUrl, {
      muteHttpExceptions: true,
      headers: { 'Cache-Control': 'no-cache, no-store, max-age=0' }
    });
    if (response.getResponseCode() === 200) {
      remoteCode = response.getContentText();
    }
  } catch (e) {
    Logger.log('Không thể tải từ GitHub: ' + e.message);
  }

  if (remoteCode && remoteCode.includes('function syncRoadmapFromBacklog')) {
    activeSS.toast('Đã tải thành công bản mới nhất từ GitHub! Đang đồng bộ...', 'Đang xử lý', 5);
    const runner = new Function('layoutMode', remoteCode + '\nreturn syncRoadmapFromBacklog(layoutMode);');
    return runner(layoutMode);
  } else {
    activeSS.toast('Không kết nối được GitHub, vui lòng kiểm tra lại kết nối mạng!', 'Lỗi kết nối', 8);
    throw new Error('Không thể tải mã nguồn mới nhất từ GitHub URL: ' + GITHUB_CODE_URL);
  }
}

/**
 * Các hàm tiếp nhận lệnh kích hoạt (Trigger Handlers)
 */
function syncRoadmapWaterfall() {
  runLatestFromGitHub('waterfall');
}

function syncRoadmapParallel() {
  runLatestFromGitHub('parallel');
}

function syncRoadmapFromBacklog(layoutMode) {
  runLatestFromGitHub(layoutMode || 'waterfall');
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
  SpreadsheetApp.getActiveSpreadsheet().toast('Đã kích hoạt tự động đồng bộ bản mới nhất từ GitHub mỗi ngày lúc 7:00 AM!', 'Thành công', 8);
}

/**
 * Hủy bỏ các Trigger tự động
 */
function cancelAutoTriggers(showToast) {
  const triggers = ScriptApp.getProjectTriggers();
  for (let i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === 'syncRoadmapFromBacklog') {
      ScriptApp.deleteTrigger(triggers[i]);
    }
  }
  if (showToast !== false) {
    SpreadsheetApp.getActiveSpreadsheet().toast('Đã hủy bỏ toàn bộ lịch tự động cập nhật!', 'Thông báo', 5);
  }
}

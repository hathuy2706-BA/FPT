# Cửa Level 0 · Giai đoạn 1 — Công cụ của tester đi làm

**Checklist nguồn:** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-1.md`
**Cửa trước:** `references/cua-gd0.md`
**Cửa sau:** `references/cua-gd2.md`

Repo bằng chứng của cửa này: **`qa-portfolio`** (public) — vẫn là repo của GĐ0, nó lớn dần
qua GĐ1 chứ không tạo repo mới. Mọi đường dẫn dưới đây là đường dẫn trong repo đó.

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Cả **19** tiêu chí trong bảng dưới đạt **≥2**, mỗi tiêu chí có
đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ sơ. Không bù trừ:
một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

**2. Capstone — một đợt test hoàn chỉnh.** Thư mục `qa-portfolio/dot-test-01/` có đủ **5
sản phẩm**, thiếu một cái là chưa mở cổng:

| # | File / thư mục | Nội dung tối thiểu |
|---|---|---|
| 1 | `chien-luoc.md` | 4 thay đổi giả định + kế hoạch 2 ngày + ưu tiên theo rủi ro + **out-of-scope** + rủi ro còn lại khi phát hành |
| 2 | `api-tests/` | collection chạy được bằng một lệnh + báo cáo kết quả đã commit |
| 3 | `exploratory/` | 2 charter + 2 báo cáo phiên |
| 4 | `bugs/` | ≥5 bug **mới tìm được trong đợt**, ưu tiên loại phân quyền / race / tầng API |
| 5 | `bao-cao-cuoi-dot.md` | mẫu 6 dòng của S1.4, kết bằng **đề xuất phát hành hay không, kèm lý do** |

Thiếu một mục, hoặc mục có nhưng rỗng phần cốt lõi (ví dụ `bugs/` toàn bug chép lại từ
GĐ0 chứ không phải bug mới của đợt) → **chưa mở cổng**, nói rõ thiếu mục nào.

**3. Ràng buộc riêng của GĐ1 — bằng chứng chạy phải nằm trong repo** (nguyên tắc 1 của
Level 0: mỗi module đẻ ra một sản phẩm công khai).

GĐ1 là giai đoạn đầu tiên học viên có thứ **chạy được**. Với mọi tiêu chí dính tới việc
chạy (S1.1-f, S1.4-c, và capstone mục 2), bằng chứng phải gồm **cả hai**: (a) **lệnh chạy**
ghi trong README — dán vào terminal là chạy, và (b) **output thật đã commit** — file báo
cáo trong repo, ảnh chụp report có số pass/fail, hoặc link CI run.

Output dán trong chat **không tính điểm** — không phân biệt được với gõ tay (luật bằng
chứng trong `SKILL.md`). Dùng nó để hỏi tiếp, không dùng để kết luận.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

> **Ghi chú khi mở cổng — nói thẳng với học viên, đừng để họ tự đoán.** GĐ1 là mốc 🎯
> **đủ điều kiện nộp CV fresher QC** (`CHECKLIST-GIAI-DOAN-1.md` dòng 5), không phải GĐ0
> và không phải GĐ2. Khi báo cổng đã mở, khuyên họ **nộp CV song song với việc học Giai
> đoạn 2** — vừa đi làm vừa học automation là con đường nhanh nhất; đợi xong GĐ2 mới nộp
> là tự kéo dài thời gian thất nghiệp mà không đổi lấy gì.

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| S1.1-a | Đọc Swagger và tự gọi được endpoint không cần hướng dẫn | `qa-portfolio/api-tests/README.md` § "Danh sách endpoint đã phủ" — bảng ≥8 endpoint, mỗi dòng có method · đường dẫn · cần token không · tham số bắt buộc | Bảng dựng từ Swagger thật của app, mỗi endpoint đã tự gọi được ít nhất một lần (có request tương ứng trong collection), và có ≥1 ghi chú đối chiếu với traffic DevTools — không phải chép nguyên trang Swagger | Nêu được **cái giá của việc lấy Swagger làm nguồn sự thật duy nhất**: spec lỗi thời thì phủ trượt endpoint UI đang thật sự gọi; nói được khi nào họ tin traffic DevTools hơn spec và mất gì khi đổi nguồn |
| S1.1-b | Chuỗi đăng nhập → lưu token → dùng ở request sau | `qa-portfolio/api-tests/` — folder `_setup` có request đăng nhập kèm script lưu token vào biến môi trường, + ≥1 request sau dùng biến đó; kèm `api-tests/.env.example` hoặc file env đã commit | Token lấy động lúc chạy chứ không dán cứng; file env commit không chứa token/mật khẩu thật; chạy lại collection từ đầu vẫn tự lấy token mới, không phải sửa tay | Nói được **đánh đổi giữa đăng nhập một lần ở `_setup` và đăng nhập lại trong từng request**: được tốc độ, mất tính độc lập của từng request; ai trả giá khi token hết hạn giữa lượt chạy dài |
| S1.1-c | Phủ đủ 6 nhóm case cho ≥1 endpoint (≥12 request có assertion) | `qa-portfolio/api-tests/README.md` § "Ma trận case theo 6 nhóm" — mỗi ô trỏ đúng tên request trong collection | Đủ 6 nhóm (happy path · validate đầu vào · xác thực & phân quyền · không tồn tại/xung đột · nghiệp vụ · phi chức năng nhẹ), ≥12 request, mỗi request ≥2 assertion và có assertion chạm vào body chứ không chỉ status | Nói được vì sao **dồn 12 request vào một endpoint thay vì rải mỏng 12 endpoint**: được chiều sâu để bắt bug nghiệp vụ, mất phủ rộng — endpoint nào đang không ai chạm, và tín hiệu gì khiến họ đảo lại lựa chọn đó |
| S1.1-d | Có case 401/403 và case dữ liệu âm/sai kiểu; có assertion "không lộ trường nhạy cảm" | `qa-portfolio/api-tests/` — 4 request bắt buộc của S1.1 Bước 3 (endpoint admin bằng token user thường · endpoint cần auth không token · gửi `price`/`quantity` âm · assertion trường nhạy cảm), kèm kết quả trong báo cáo đã commit | Cả 4 case tồn tại và **đã chạy thật**; case dữ liệu âm kỳ vọng 4xx — nếu app trả 200 thì đã thành bug report chứ không sửa kỳ vọng cho suite xanh; assertion nhạy cảm liệt kê tên trường cụ thể của app này | Nói được đánh đổi giữa **danh sách đen** (liệt kê trường cấm xuất hiện) và **danh sách trắng** (chốt đúng bộ field được phép trả về): cái nào bỏ sót gì khi backend thêm field mới, vì sao vẫn chọn cái đang dùng |
| S1.1-e | Tìm được ≥1 chỗ **UI chặn mà API không chặn**, có cURL + bằng chứng DB | `qa-portfolio/api-tests/README.md` § "Bug tầng API tìm được" — ≥2 bug, mỗi bug có lệnh cURL tái hiện đầy đủ + query SQL kèm kết quả cho thấy dữ liệu bậy đã vào DB | cURL dán vào terminal chạy lại được (đủ header, đủ body), query trỏ đúng bản ghi vừa tạo, và mô tả nêu rõ UI chặn bằng cách nào còn API bỏ qua ở bước nào | Cân được bản vá phía UI **mua được gì** (rẻ, làm ngay, chặn được người dùng bình thường) và **không mua được gì** (ai gọi thẳng API vẫn qua) — nên vì sao lỗi này phải vá ở **server**; xếp mức nghiêm trọng theo hệ quả dữ liệu chứ không theo độ khó tái hiện |
| S1.1-f | Chạy được cả collection bằng một lệnh | `qa-portfolio/api-tests/README.md` § "Cách chạy" — **lệnh cụ thể** (`newman run …` / `bru run …`) **và** output thật đã commit: file báo cáo trong `api-tests/` hoặc ảnh chụp report có số pass/fail | Lệnh chạy được từ máy trắng theo đúng README, không phải sửa tay file nào; báo cáo đã commit khớp số request trong collection. Output dán chat không tính — bằng chứng phải nằm trong repo | Nói được đánh đổi khi **trỏ collection sang môi trường công khai để pipeline chạy được** (S1.4 Bước 3): được CI chạy thật, mất độ trung thực với app thật — hoặc đánh đổi ngược lại giữa chạy cả collection mỗi lần và tách một folder smoke chạy trước |
| S1.2-a | Chạy đủ 8 case session, kiểm token sau logout ở tầng API | `qa-portfolio/kiem-thu-web-sau.md` § "Bảng 8 case session" — 8 dòng đủ *thao tác · kết quả thực tế · kỳ vọng · có bug không*; case 2 và case 7 kèm bằng chứng API/DevTools | Đủ 8 tình huống của S1.2 mục 3.1; case 2 (dùng lại token cũ sau logout) và case 7 (đổi mật khẩu → phiên cũ ở thiết bị khác) kết luận dựa trên **lệnh gọi API thật + status trả về**, không dựa vào việc UI đã đá về trang đăng nhập | Nói được vì sao "token vẫn sống sau logout" là lỗi phía server, và **cái giá của từng cách vá** (thu hồi token phải giữ danh sách đen / rút ngắn hạn token làm người dùng phải đăng nhập lại nhiều hơn) — vì sao nhiều hệ thống cố ý chấp nhận rủi ro đó, và họ đề nghị mức nào cho app này |
| S1.2-b | Ma trận phân quyền ≥3 vai trò × ≥8 chức năng, test đủ 3 tầng (UI/URL/API) | `qa-portfolio/kiem-thu-web-sau.md` § "Ma trận phân quyền" — bảng ≥3 vai trò × ≥8 chức năng, mỗi ô có kết quả cho cả 3 tầng, ô có bug được tô đậm kèm cURL | Kỳ vọng từng ô ghi **trước** khi test; không ô nào bỏ trống tầng API; có ≥1 ô lệch giữa tầng UI và tầng API, được đánh dấu và có cURL chứng minh | Nói được vì sao ma trận dừng ở đúng kích thước đó: 3 vai trò × 8 chức năng × 3 tầng là 72 phép thử — **ô nào cắt được và rủi ro còn lại sau khi cắt**, ai gánh nếu đoán sai chỗ cắt |
| S1.2-c | Đã thử IDOR (đổi id trên URL) | `qa-portfolio/kiem-thu-web-sau.md` § "Ma trận phân quyền" (mục IDOR) — ghi rõ tài khoản A, ID bản ghi thuộc tài khoản B lấy ở đâu, đường dẫn đã gọi, response nhận được | Có ID thật của bản ghi thuộc tài khoản khác (lấy từ DB hoặc từ chính tài khoản B), thử ở **cả URL và endpoint API**, kết luận nêu status + phần dữ liệu lộ ra — không dừng ở "đã thử, bị chặn" | Nói được vì sao đổi id trên URL là **mẫu thử rẻ nhưng chưa đủ**: nó chỉ phủ id tuần tự, còn IDOR qua tham số trong body/header thì chưa ai soi; họ đánh đổi thời gian đó cho việc gì và điều kiện nào khiến họ quay lại soi tiếp |
| S1.2-d | Tìm & xác minh ≥1 vấn đề double submit/race bằng SQL | `qa-portfolio/kiem-thu-web-sau.md` § "Race & trạng thái" — ≥1 kịch bản double submit/race có ảnh hoặc video + query SQL kèm số dòng **trước và sau** thao tác | Nêu rõ cách tạo tình huống (bấm 2 lần, Slow 3G, 2 tab cùng sửa, Back rồi submit lại), query đếm đúng bản ghi bị nhân đôi, kết luận bám vào số dòng DB chứ không vào cảm giác nhìn UI | Nói được **giới hạn của bằng chứng SQL**: DB có 2 dòng chưa chứng minh người dùng bình thường tạo ra được tình huống đó; họ cần làm thêm gì để chứng minh, và vì sao vẫn báo ngay thay vì đợi đủ bằng chứng — cái giá của mỗi lựa chọn |
| S1.2-e | Kiểm empty / loading / error state cho ≥3 màn hình | `qa-portfolio/kiem-thu-web-sau.md` § "Race & trạng thái" — bảng ≥3 màn hình × 3 trạng thái, mỗi ô ghi **cách tạo ra trạng thái** + ảnh thật | Mỗi trạng thái tạo bằng thao tác mô tả lại được (tài khoản mới / tìm không kết quả cho empty · Slow 3G cho loading · chặn request bằng DevTools cho error); ảnh là ảnh app thật; phần error ghi nguyên văn thông báo app hiện ra (có lộ stacktrace hay `undefined` không) | Nói được vì sao ba trạng thái này đáng thời gian hơn thêm vài case happy path, **và cái giá của lựa chọn đó**: chúng hiếm khi chặn phát hành nên dễ bị hoãn vô hạn; họ xếp ưu tiên ra sao và bỏ cái nào trước khi hết giờ |
| S1.3-a | Charter có out-of-scope và rủi ro nhắm tới | `qa-portfolio/exploratory/` — 3 charter theo khung S1.3 mục 3.2, mỗi cái có mục "Ngoài phạm vi" và "Rủi ro đang nhắm tới" không rỗng | Charter viết theo công thức *khám phá vùng nào · bằng cách nào · để phát hiện loại rủi ro cụ thể nào*; out-of-scope liệt kê thứ có thật đã cân nhắc rồi loại, không phải "mọi thứ còn lại"; rủi ro nhắm tới bám vào quan sát từ S1.2 chứ không phải rủi ro chung của mọi app | Bảo vệ được **một dòng out-of-scope cụ thể**: nếu bug nghiêm trọng lọt đúng ở đó thì hệ quả gì và ai chịu, vì sao vẫn chấp nhận đánh đổi ấy trong 90 phút, và điều kiện nào kéo nó vào phạm vi phiên sau |
| S1.3-b | Chạy được phiên exploratory 90 phút có note theo dòng thời gian | `qa-portfolio/exploratory/session-report-01.md` § "Note thô (dòng thời gian)" — note có mốc giờ, ≥1 dòng mỗi 5 phút, dùng đủ ký hiệu SETUP / TEST / BUG / Q / IDEA | Mốc giờ liên tục phủ đủ 90 phút; có ≥4 dòng `BUG` là phát hiện **mới** ngoài bộ case ở S0.3; có cả dòng `Q` và `IDEA` — dấu hiệu họ ghi trong phiên chứ không viết lại sau | Nói được đánh đổi của luật **"thấy bug thì ghi rồi đi tiếp"**: được phủ rộng hết charter, mất chiều sâu tại chỗ (bug ghi vội có thể thiếu điều kiện thật); nêu một lần họ cố ý phá luật đó và vì sao lần đó đáng |
| S1.3-c | Báo cáo phiên có mục "chưa soi / rủi ro còn lại" | `qa-portfolio/exploratory/session-report-01.md` § "Tóm tắt (lead đọc 2 phút)" — dòng "Chưa soi (rủi ro còn lại)" + dòng đánh giá chốt một trong ba mức (an toàn / cần thêm 1 phiên / rủi ro cao, đề nghị chặn release) | Mục "chưa soi" liệt kê vùng cụ thể, không phải "còn nhiều thứ chưa test"; dòng đánh giá chốt hẳn một mức kèm lý do; toàn báo cáo không có câu ngụ ý đã test hết | Nói được vì sao dòng "chưa soi" **có lợi cho chính người viết** dù nghe như tự khai thiếu sót: ai dùng nó ra quyết định gì, và cân giữa cái giá của việc viết ra (bị hỏi vì sao chưa làm) với cái giá của việc giấu (mất uy tín khi bug lọt) |
| S1.3-d | Trả lời được "2 ngày test gì, bỏ gì" với lý do dựa trên rủi ro | `qa-portfolio/dot-test-01/chien-luoc.md` (nâng từ `exploratory/chien-luoc-test-release.md`) — 4 thay đổi giả định, phân bổ ngày 1 / ngày 2, mục out-of-scope, mục "rủi ro còn lại khi phát hành"; kèm ghi chú vòng phản biện AI (giữ hay đổi quyết định nào) | Ưu tiên bám công thức *rủi ro = khả năng hỏng × thiệt hại khi hỏng*; ngày 1 là luồng kiếm tiền + vùng vừa thay đổi, ngày 2 là regression + exploratory vùng rủi ro cao; mục bỏ ghi rõ bỏ cái gì chứ không im lặng | Giữ được ≥1 quyết định trước phản biện **và nói được cái giá của nó**: bỏ sai thì ai chịu, mất bao lâu mới biết mình sai, tín hiệu nào giữa đợt sẽ khiến họ đảo thứ tự ngay |
| S1.4-a | Quản lý bug đúng vòng đời, comment verify nêu build + môi trường | `qa-portfolio/quan-ly-test/` — ảnh chụp bảng quản lý bug với vòng đời thật của ≥3 ticket (New → Triage → In Progress → Ready for QA → Verified/Reopened) + nội dung comment verify | ≥3 ticket đi hết vòng đời, trong đó có ≥1 lần Reopened; comment verify đủ **ba việc** của S1.4 mục 3.1: chạy lại bước tái hiện, regression cục bộ quanh vùng vừa sửa, và ghi rõ build + môi trường + tài khoản — không phải "vẫn lỗi" / "OK rồi" | Nói được đánh đổi giữa **Reopen ticket cũ** và **mở ticket mới** khi lỗi quay lại: lịch sử gọn hơn nhưng mất dấu số lần fix hụt (hoặc ngược lại); họ chọn cách nào, trong bối cảnh team nào, và mất gì khi chọn vậy |
| S1.4-b | Dùng đúng Pass/Fail/**Blocked**/Skipped; báo cáo có mục chặn phát hành | `qa-portfolio/quan-ly-test/bao-cao-test-run-01.md` — theo mẫu 6 dòng của S1.4 mục 3.3, đủ dòng "Chặn phát hành", "Vùng CHƯA test (rủi ro còn lại)" và "Đề xuất"; test run có ≥1 case **Blocked** thật | Có case Blocked thật (ví dụ tắt container DB) và họ giải thích được vì sao không ghi Fail; case Skipped có lý do; dòng "Đề xuất" chốt hẳn phát hành hay không kèm lý do, không lửng lơ | Nói được đánh đổi khi **đề xuất chặn phát hành**: chi phí hoãn release đặt cạnh rủi ro của bug đó, ai là người thật sự quyết; và họ làm gì khi PO vẫn phát hành — ghi lại cái gì, cho ai, để bảo vệ điều gì |
| S1.4-c | Đọc được log CI fail và phân biệt sản phẩm hỏng / test hỏng / flaky | `qa-portfolio/quan-ly-test/` — file workflow CI + **một build đỏ thật** do chính học viên tạo ra (link run hoặc ảnh chụp log), kèm phân tích chỉ ra **dòng lỗi đầu tiên** và xếp vào 1 trong 3 loại đỏ | Build đỏ nằm trong repo `qa-portfolio` chứ không phải log dán chat; phân tích trỏ vào **dòng lỗi đầu tiên** (không phải dòng cuối), kết luận loại đỏ có dẫn chứng dòng log cụ thể, và nêu bước kiểm tra tiếp theo để xác nhận | Nói được cái giá của phản xạ **"Re-run cho xanh"**: mỗi lần re-run mua được gì (qua được PR hôm nay) và trả bằng gì (cả team ngừng tin màu đỏ); chốt ngưỡng của chính mình — lặp mấy lần thì họ dừng lại điều tra thay vì chạy lại |
| AI | Chỉ ra được ≥1 endpoint hoặc field AI **bịa** khi đối chiếu Swagger thật | `qa-portfolio/api-tests/README.md` § "AI hỗ trợ ở đâu" — prompt đã dùng ở S1.1 Bước 5, số case AI đề xuất, số case dùng được, và ≥1 endpoint/field AI bịa kèm cách phát hiện | Chỉ ra field hoặc endpoint **cụ thể** không có trong Swagger thật của app, kèm cách phát hiện (đối chiếu spec / gọi thử nhận 404) và con số đề xuất-loại; không phải nhận xét chung "AI hay bịa" | Nói được **đánh đổi khi đặt AI đúng ở bước mở rộng phủ** (sau khi đã tự viết 12 case): tiết kiệm được gì, phải trả bằng bao nhiêu công chạy thử từng case đề xuất, và chỗ nào họ quyết định **không** dùng AI vì kiểm chứng đắt hơn tự viết |

**Lưu ý về S1.1-e:** checklist giai đoạn ghi ≥1, nhưng hands-on và capstone S1.1 (Bước 3,
mục 4) đều đòi ≥2 — chấm theo ≥2.

**Lưu ý về S1.3-d và capstone:** module S1.3 sinh ra `exploratory/chien-luoc-test-release.md`,
còn capstone giai đoạn đòi `dot-test-01/chien-luoc.md`. Đây là **một tài liệu qua hai lần
nâng**, không phải hai bài. Chấm trên bản trong `dot-test-01/`; bản nháp ở `exploratory/`
chỉ dùng để đối chiếu xem họ đã sửa gì sau vòng phản biện.

> **Tiêu chí không bắt buộc:** checklist nguồn còn một dòng S1.2 *"Responsive theo 3 mốc
> cố định, mọi phát hiện có screenshot thật"* **không** có dấu ✔. Không dùng nó làm điều
> kiện mở cổng và không đưa vào bảng trên. Vẫn hỏi được trong phỏng vấn (tầng 1) để phân
> loại điểm 3 — nhưng câu đó **không tính vào Điểm TB** của buổi thi và không ghi thành
> điểm trong hồ sơ; trả lời kém ở đó chỉ chặn điểm 3, không bao giờ đánh trượt.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

1. **Đủ HTTP để test** — 400 vs 401 vs 403 vs 404 vs 422 vs 500 khác nhau ở chỗ nào; bắt lấy ví dụ từ chính API họ vừa test, cấm đọc lại định nghĩa. *(S1.1)*
2. **Sáu nhóm case cho một endpoint** — kể đủ 6 nhóm và nói mỗi nhóm bắt loại bug gì; nhóm nào người mới gần như luôn bỏ và vì sao. *(S1.1)*
3. **Bug chỉ lộ ở tầng API** — vì sao "UI chặn" không đồng nghĩa "API chặn"; kể 3 dạng (chặn số âm, ẩn nút không kiểm quyền, response trả thừa dữ liệu) và cách thử từng dạng. *(S1.1)*
4. **Assertion tới đâu là đủ** — status vs hình dạng body vs giá trị nghiệp vụ vs hiệu ứng phụ; vì sao assertion "không lộ trường nhạy cảm" ít người viết mà giá trị cao. *(S1.1)*
5. **Tám case session** — bắt kể ra, rồi chỉ đúng case nào **không thể** kết luận bằng mắt nhìn UI mà phải gọi API/xem DevTools. *(S1.2)*
6. **Phân quyền ba tầng và IDOR** — UI / URL / API kiểm ba thứ khác nhau ra sao; "ẩn nút mà server không kiểm quyền" nghĩa là gì; IDOR thử bằng cách nào. *(S1.2)*
7. **Race & double submit** — ba cách tạo ra tình huống; vì sao phải xác minh bằng SQL chứ không tin UI. *(S1.2)*
8. **Empty / loading / error state** — cách tạo ra từng trạng thái trên app thật, và vì sao ba trạng thái này chiếm phần lớn bug UX. Kèm 3 mốc responsive cố định và vì sao không kéo cửa sổ ngẫu nhiên *(phần responsive không bắt buộc — chỉ dùng để phân loại điểm 3; câu này không tính vào Điểm TB)*. *(S1.2)*
9. **Charter và out-of-scope** — charter khác "test bừa" ở chỗ nào; vì sao thiếu out-of-scope là đang ngầm hứa đã test hết. *(S1.3)*
10. **SFDIPOT và cách ghi note trong phiên** — bí quá 5 phút thì mở lăng kính nào; vì sao thấy bug phải ghi rồi đi tiếp thay vì điều tra ngay. *(S1.3)*
11. **Pass / Fail / Blocked / Skipped và mẫu báo cáo 6 dòng** — ghi Fail cho case Blocked thì báo cáo bị bóp méo ra sao; metric nào dễ bị bóp méo nhất, metric nào khó nhất. *(S1.4)*
12. **Ba loại đỏ trên CI và giao tiếp khi bất đồng** — dấu hiệu nhận ra từng loại; dev nói "cái này by design" mà không có tài liệu thì xử lý theo thứ tự nào. *(S1.4)*
13. **AI đối chiếu spec thật** — vì sao phải dán spec thật vào prompt thay vì để AI tự nhớ endpoint; ràng buộc nào trong prompt chặn được việc AI bịa field. *(AI)*

### Tầng 2 — Đào sâu vào bài của học viên

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC, điền chỗ trống bằng nội dung thật trong bài họ,
rồi mới hỏi. Câu hỏi không có chỗ trống đã điền = câu lý thuyết trá hình, không tính là
tầng 2. Tầng này chống học thuộc và chống bài do AI viết — **một câu 0 điểm ở đây là phủ
quyết**, trượt bất kể điểm trung bình.

1. *"Ma trận 6 nhóm của bạn, nhóm `<tên nhóm>` có `<n>` request. Lấy request `<tên request>` — nó đỏ khi bug gì xảy ra? Xoá nó đi thì mình mất khả năng bắt cái gì?"*
2. *"Request `<tên request>` assert `<trích assertion>`. Nếu tôi đổi dữ liệu gửi lên thành `<biến thể>`, assertion này còn đúng không — hay nó vẫn xanh trong khi sản phẩm đã sai?"*
3. *"Trong § 'Bug tầng API tìm được', bug `<số>` có cURL `<trích>`. Chạy lại giúp tôi: dòng nào trong response chứng minh API không chặn, và query nào chứng minh dữ liệu bậy đã vào DB?"*
4. *"Collection của bạn lưu token vào biến `<tên biến>` ở folder `_setup`. Nếu tôi chạy riêng folder `<tên folder>` mà bỏ qua `_setup` thì chuyện gì xảy ra? Bạn đã thử chưa?"*
5. *"Báo cáo chạy collection đã commit ở `<đường dẫn>` ghi `<n>` pass / `<m>` fail. `<m>` case fail đó là sản phẩm hỏng hay kỳ vọng bạn viết sai? Chỉ cho tôi bug report tương ứng."*
6. *"Trong `kiem-thu-web-sau.md`, ô `<vai trò>` × `<chức năng>` bạn đánh dấu có bug. Ba tầng UI / URL / API cho ba kết quả gì? Ô nào trong ma trận bạn chỉ test một tầng — và vì sao dừng ở đó?"*
7. *"Case session số `<n>` bạn kết luận `<trích>`. Bạn kiểm bằng UI hay bằng lệnh gọi API? Nếu bằng UI thì làm sao biết server đã thật sự thu hồi token?"*
8. *"Kịch bản race `<trích>` ghi DB có `<n>` dòng sau thao tác. Trước thao tác có mấy dòng? Bạn chắc dòng thừa do thao tác của bạn chứ không phải rác từ lần test trước bằng cách nào?"*
9. *"Bảng trạng thái ghi màn `<tên màn>` ở trạng thái error hiện `<trích thông báo>`. Bạn tạo ra lỗi đó bằng cách nào, và người dùng thật gặp trạng thái này trong tình huống nào?"*
10. *"Charter `<tên file>` ghi ngoài phạm vi `<trích>`. Nếu bug nghiêm trọng lọt đúng ở đó sau release, bạn nói gì với lead? Điều gì sẽ khiến bạn kéo nó vào phạm vi phiên sau?"*
11. *"Note phiên lúc `<mốc giờ>` ghi `BUG <trích>`, tới `<mốc giờ sau>` bạn mới quay lại chỗ đó. Trong khoảng giữa bạn làm gì, và vì sao không dừng lại điều tra ngay lúc thấy?"*
12. *"Mục 'Chưa soi (rủi ro còn lại)' trong `session-report-01.md` ghi `<trích>`. Ai đọc dòng này, và họ ra quyết định gì khác đi nhờ nó?"*
13. *"`dot-test-01/chien-luoc.md` xếp `<hạng mục>` vào ngày 1 và `<hạng mục khác>` vào ngày 2. Đổi chỗ hai cái thì rủi ro nào tăng? Bạn cố ý bỏ `<trích mục bỏ>` — bug lọt ở đó thì ai chịu?"*
14. *"`bao-cao-test-run-01.md` ghi `<n>` case Blocked. Case nào, chặn vì cái gì, vì sao không phải Fail? Nếu tôi đổi hết Blocked thành Fail thì báo cáo này nói sai điều gì với người quyết release?"*
15. *"Mở log build đỏ `<link / ảnh>` ra. Chỉ cho tôi **dòng lỗi đầu tiên**, không phải dòng cuối. Từ dòng đó bạn kết luận loại đỏ nào — và bằng chứng nào **loại trừ** hai loại còn lại?"*
16. *"Mục 'AI hỗ trợ ở đâu' ghi AI đề xuất `<n>` case, bạn dùng `<m>`. Chọn một case bị loại vì AI bịa field `<tên field>` — bạn phát hiện ở bước nào, bằng cách nào?"*
17. *"Bug `<ID>` trong `dot-test-01/bugs/` là bug mới của đợt này. Nó thuộc nhóm nào — phân quyền, race hay tầng API? Nếu không nhờ đợt test này thì nó lọt tới đâu?"*

### Tầng 3 — Tình huống

1. *"Release có 4 thay đổi, bạn có **2 ngày**. Test gì trước, **bỏ gì**, vì sao — và cuối 2 ngày bạn báo cáo gì cho người quyết phát hành?"*
2. *"Bạn được giao test một API vừa xong, chưa có UI, Swagger viết sơ sài và có chỗ sai. Nửa ngày. Giờ đầu tiên làm gì, và cuối buổi giao được cái gì?"*
3. *"Pipeline chạy collection của bạn đỏ 3 ngày liên tiếp, mỗi lần một test khác nhau, chạy lại thì xanh. Team bắt đầu bỏ qua màu đỏ. Bạn làm gì, theo thứ tự nào?"*
4. *"Dev đóng bug phân quyền của bạn với lý do 'by design, UI đã ẩn nút rồi'. Không có tài liệu nào nói vậy, sprint còn 2 ngày. Bạn xử lý ra sao?"*
5. *"PO nói 'cứ release đi, bug đó nhỏ thôi' với bug double submit tạo đơn trùng. Bạn không có quyền chặn. Làm gì, và ghi lại cái gì?"*
6. *"Bạn có 90 phút exploratory cho một vùng vừa bị sửa gấp trước release, không ai kể cho bạn họ sửa gì. Charter viết thế nào, và cuối phiên giao gì cho lead?"*
7. *"Bạn nộp CV fresher. Nhà tuyển dụng nhắn: 'gửi tôi một thứ chứng minh em test được'. Bạn gửi cái gì trong repo, và giải thích nó trong 3 câu ra sao?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Kể trôi 6 nhóm case nhưng collection chỉ có happy path và vài case thiếu trường** — nhóm nghiệp vụ và nhóm phi chức năng nhẹ trống trơn, tức là chưa bao giờ áp bảng đó vào bài thật.
2. **Nói đúng câu "UI chặn không có nghĩa API chặn" nhưng § "Bug tầng API tìm được" không có cURL nào** — bug liệt kê ra đều là lỗi hiển thị, thứ nhìn bằng mắt cũng thấy.
3. **Ma trận phân quyền kín ô nhưng mọi ô đều test ở tầng UI**, cột API trống hoặc ghi "giống UI" — chính là lỗi mà tiêu chí này tồn tại để bắt.
4. **Thuộc định nghĩa Blocked nhưng test run không có case Blocked nào**, hoặc có mà giải thích được vì sao không ghi Fail — chưa từng gặp tình huống đó thật.
5. **Charter đủ mục nhưng out-of-scope ghi "các phần khác của hệ thống"** — câu này dán vào charter nào cũng đúng, nghĩa là chưa cân nhắc gì; hỏi ngay họ đã loại cái gì và vì sao.
6. **Note phiên đều tăm tắp mỗi 5 phút một dòng, không có dòng `Q` hay `IDEA` nào, mọi dòng `BUG` đều đã chỉn chu như bug report** — dấu viết lại sau phiên chứ không ghi trong phiên.
7. **Nói được ba loại đỏ CI nhưng mở log thật ra thì chỉ vào dòng cuối**, hoặc trong repo không có build đỏ nào — chưa từng tự làm CI đỏ để đọc.
8. **Kể vanh vách IDOR nhưng không nói được lấy ID bản ghi của người dùng khác ở đâu** — chưa từng thử, chỉ đọc.
9. **cURL và query SQL trong bài viết rất chuẩn nhưng không đọc được từng header / từng mệnh đề khi bị hỏi**, hoặc không biết bỏ header nào đi thì request hỏng — dấu chép nguyên từ AI.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `gd1 — <YYYY-MM-DD>`. Dòng "Nhánh nghề (Level 0)": cửa đang mở đổi thành `gd2`, module đang học `S2.1`. Ghi thêm mốc 🎯 *đủ điều kiện nộp CV fresher* |
| 2. Bảng tiêu chí | Thay bằng tiêu chí của cửa `gd2`. **Không xoá bảng gd1** — lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; các đường dẫn bằng chứng cũ còn dùng lại khi nghi bài giả hoặc khi placement |
| 2. Capstone | `đạt` — kèm đường dẫn `qa-portfolio/dot-test-01/` |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `gd1` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt (ví dụ responsive chưa làm, hoặc tiêu chí chỉ vừa đạt 2) — để phiên sau quay lại |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa gd1, đạt |
```

**Cập nhật checklist nguồn** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-1.md`: rà
lại cột `Tự đánh giá`, tick đủ 19 tiêu chí đã chấm ≥2. Dòng responsive không bắt buộc —
chỉ tick nếu đã thật sự chấm dựa trên screenshot trong repo. Cột `Reviewer` **để trống** —
ô đó dành cho QE/QC người thật muốn xác nhận thêm, không bao giờ tự tick.

**Mở cửa kế tiếp:** `gd2` — đọc `references/cua-gd2.md`, checklist nguồn
`curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-2.md`, module đầu tiên
`curriculum/level-0-sinh-vien/S2.1-coding-nen-cho-tester.md`. Repo bằng chứng của GĐ2 là
**`qa-automation`** — repo mới, `qa-portfolio` giữ nguyên không xoá.

**Nhắc học viên — quan trọng, đừng bỏ:** đây là mốc 🎯 **đủ điều kiện nộp CV fresher QC**.
Khuyên họ **nộp CV ngay, song song với việc học Giai đoạn 2**, không đợi xong automation
mới nộp. Khi nhà tuyển dụng hỏi "em đã làm gì rồi", câu trả lời là `qa-portfolio/dot-test-01/`
— một sprint thu nhỏ có tài liệu, không phải lời kể. Nhắc thêm: nhánh AI (`l1`) là nhánh
**song song**; đạt `gd1` không tự mở `l1`, muốn mở thì chạy placement riêng cho nhánh đó.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

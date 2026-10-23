# Cửa Level 0 · Giai đoạn 2 — Automation nền

**Checklist nguồn:** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-2.md`
**Cửa trước:** `references/cua-gd1.md`
**Cửa sau:** — (cửa cuối nhánh Level 0)

Repo bằng chứng của cửa này: **`qa-automation`** (public) — repo mới, không gộp vào
`qa-portfolio`. Mọi đường dẫn dưới đây là đường dẫn trong repo đó.

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Cả **28** tiêu chí trong bảng dưới đạt **≥2**, mỗi tiêu chí có
đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ sơ. Không bù trừ:
một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

**2. Capstone.** Repo public `qa-automation` có đủ:

| # | Sản phẩm | Nội dung tối thiểu |
|---|---|---|
| 1 | Suite | ≥12 API test + 5 E2E test, chạy bằng một lệnh |
| 2 | **CI xanh** | workflow chạy API → E2E mỗi PR, có badge trong README, và một run xanh từ commit đang chấm |
| 3 | `evidence/` | bằng chứng test đỏ đúng lúc (ảnh + trace) |
| 4 | **`AUDIT.md`** | tự audit suite theo 6 câu của S2.4 mục 3.5, gồm cả lỗ hổng phủ còn lại |
| 5 | `tests/e2e/e2e-plan.md` | luồng được chọn, luồng bị loại + lý do |
| 6 | `tai-lieu/test-plan-dot-01.md` | 7 mục, **≤2 trang**, có entry/exit criteria + rủi ro còn lại khi phát hành |
| 7 | `tai-lieu/test-strategy.md` | 8 mục, **≤2 trang**, mọi con số đo từ CI thật |
| 8 | `README.md` | trả lời đủ 5 câu của S2.4 mục 3.6, gồm "cố ý chưa phủ gì và vì sao" |

CI đỏ tại thời điểm chấm → **chưa mở cổng**, kể cả khi học viên nói "chỉ flaky thôi": đỏ
mà chưa kết luận được nguyên nhân chính là thứ tiêu chí S2.3-f và S2.4-c tồn tại để bắt.
Hai tài liệu ở mục 6–7 vượt 2 trang cũng là **chưa xong** — cắt xuống là một phần bài.

**3. Ràng buộc riêng của GĐ2 — luật bằng chứng nghiêm nhất trong sáu cửa**
(**nguyên tắc 3 của Level 0**: test phải biết FAIL — suite xanh không chứng minh gì).

Mọi tiêu chí automation đòi **đủ ba thứ**, thiếu một thì tiêu chí đó chưa được chấm:

| | Đòi gì | Không tính là gì |
|---|---|---|
| a | **Đường dẫn file test** trong repo | Mô tả "em có test cho cái đó" |
| b | **Bằng chứng chạy nằm trong repo hoặc CI** — file báo cáo đã commit, link CI run, hoặc bạn tự chạy suite nếu repo có trên máy này | Output dán trong chat: không phân biệt được với gõ tay |
| c | **Bằng chứng test ĐỎ đúng lúc** — sửa code sản phẩm hoặc dữ liệu cho hỏng thì test phải fail, đúng test liên quan | Suite xanh: một suite toàn test rỗng cũng xanh |

Ba thứ này áp cho từng tiêu chí, không phải cho cả cửa: một tiêu chí có file và có báo cáo
chạy nhưng chưa bao giờ chứng minh được nó đỏ thì **tối đa điểm 1**.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| S2.1-a | Viết được hàm, dùng `filter`/`map`, đúng `async/await`, try/catch có ném lại | `qa-automation/helpers/` (hoặc `utils/` — xem lưu ý dưới bảng): `data.ts` (hàm sinh dữ liệu) + `api-client.ts` (hàm đăng nhập lấy token và gọi API kèm token) | Mọi hàm async đều được `await` khi gọi — không chỗ nào dùng Promise như thể là dữ liệu; try/catch **ném lại** lỗi thay vì nuốt; có ≥1 chỗ dùng `filter`/`map` trên dữ liệu thật của suite chứ không phải bài tập dán vào; hàm có kiểu tham số và kiểu trả về | Nói được đánh đổi giữa **bắt lỗi ở tầng helper** và **để lỗi nổ thẳng trong test**: bắt sớm cho thông báo dễ đọc nhưng dễ che mất nguyên nhân gốc và stacktrace; chỗ nào trong suite họ cố ý **không** bắt, và ai trả giá khi đoán sai |
| S2.1-b | Đọc stacktrace, chỉ đúng dòng code gây lỗi; có `debug-notes.md` ≥5 lỗi | `qa-automation/debug-notes.md` — ≥5 mục, mỗi mục đủ *lỗi tự gây ra · thông báo lỗi nguyên văn · cách tìm ra nguyên nhân* | ≥5 lỗi **khác loại** (quên `await`, sai tên field, token sai, URL sai…); thông báo lỗi dán nguyên văn và họ chỉ đúng dòng trỏ vào **file của mình**, không phải dòng trong `node_modules`; mỗi mục nêu công cụ đã dùng | Nói được vì sao dừng ở `console.log` hay leo lên debugger trong từng ca cụ thể — **cái giá của mỗi lối** (log rẻ nhưng phải chạy lại nhiều lượt; debugger dựng lâu nhưng thấy giá trị thật), và một ca họ chọn sai mất bao lâu mới nhận ra |
| S2.1-c | Giải thích lại được code mình viết mà không nhìn màn hình | Chấm **trực tiếp** trên `qa-automation/helpers/api-client.ts` (hoặc `utils/` — xem lưu ý dưới bảng; hoặc một spec do họ viết): đóng file lại, học viên kể lại luồng. Ghi vào Nhật ký hồ sơ: ngày · file đã đóng · ≥1 câu đã hỏi · chỗ họ kể lệch (nếu có). Đây là tiêu chí duy nhất của cửa chấm tại chỗ thay vì đọc từ file | Kể đúng thứ tự các bước hàm làm, tên biến chính, chỗ nào có thể ném lỗi, và vì sao có dòng đó — lệch chi tiết cú pháp thì bỏ qua, lệch về **luồng** thì chưa đạt | Nói được chỗ nào trong hàm họ **cố ý viết dài hơn mức cần** cho dễ đọc thay vì viết gọn: đánh đổi giữa ngắn và dễ sửa cho người sau, và ai trả giá khi chọn nhầm phía |
| S2.1-d | Secret đọc từ biến môi trường, `.env` không bị commit | `qa-automation/.env.example` (đã commit) + `.gitignore` + chỗ đọc `process.env` trong `helpers/` và `playwright.config.ts` | `.gitignore` chặn đủ `.env`, `node_modules`, `.auth/`, `test-results/`; `.env.example` liệt kê đủ biến README nhắc tới; grep cả repo không ra mật khẩu/token thật; thiếu biến thì code ném lỗi rõ ràng chứ không chạy tiếp với `undefined` | Nói được đánh đổi khi để **giá trị mặc định trong code** (`?? 'http://localhost:8091'`): chạy được ngay trên máy mới nhưng che mất cấu hình sai trên CI — biến nào họ cố ý không đặt mặc định và vì sao chấp nhận việc suite chết ngay khi thiếu nó |
| S2.2-a | ≥12 API test chạy bằng một lệnh, có báo cáo | `qa-automation/tests/api/` + `README.md` § "Chạy thế nào" + **báo cáo đã commit hoặc link CI run** của lượt chạy nhóm API | Một lệnh chạy hết nhóm API; số test trong báo cáo ≥12 và khớp số spec trong thư mục; báo cáo nằm trong repo hoặc là artifact của một CI run — ảnh dán chat không tính | Nói được đánh đổi giữa **một lệnh chạy tất cả** và **tách nhóm `@smoke` chạy trước**: feedback nhanh hơn nhưng có cửa để lọt bug ngoài smoke; ngưỡng thời gian nào khiến họ tách, và bỏ phủ ở đâu khi tách |
| S2.2-b | Mọi test assert tới tầng nghiệp vụ hoặc hiệu ứng phụ — không có test rỗng | `qa-automation/tests/api/*.spec.ts` + `AUDIT.md` § test rỗng đã xoá hoặc sửa | Không test nào dừng ở status code; assertion chạm quy tắc nghiệp vụ thật của app (tổng tiền bằng tổng dòng hàng) hoặc hiệu ứng phụ (GET lại thấy bản ghi, đăng nhập được bằng tài khoản vừa tạo); mỗi test có dòng ghi **"test này ĐỎ khi bug gì xảy ra"** | Nói được cái giá của assertion tầng 4: mỗi lần gọi thêm request để xác nhận là thêm thời gian chạy và thêm một chỗ để flaky — test nào họ **cố ý dừng ở tầng 3** và bug loại nào chấp nhận để lọt vì lựa chọn đó |
| S2.2-c | Có test phân quyền (401/403) + assertion "không lộ trường nhạy cảm" | `qa-automation/tests/api/` — test gọi endpoint cần auth không token (401), test gọi endpoint admin bằng token user thường (403), và assertion liệt kê trường nhạy cảm không được xuất hiện | Ba thứ là test riêng chạy độc lập, không gộp; test 403 dùng token user thật lấy động từ fixture chứ không dán cứng; assertion nhạy cảm ghi đúng tên trường của API app này | Nói được đánh đổi khi kiểm phân quyền ở **tầng API thay vì E2E**: rẻ, nhanh, chứng minh được server chặn — nhưng **không** chứng minh UI đã ẩn đúng thứ người dùng thấy; họ bù chỗ hổng đó bằng gì và chấp nhận rủi ro nào |
| S2.2-d | Bằng chứng ≥3 test **đỏ đúng lúc** khi sản phẩm bị phá | `qa-automation/evidence/` — ≥3 mục, mỗi mục có ảnh lần chạy đỏ + chú thích *đã phá gì → test nào đỏ → thông báo lỗi nói gì* | Cả 3 lần là **phá sản phẩm hoặc dữ liệu đầu vào**, không phải chỉ sửa kỳ vọng cho sai; đỏ **đúng test liên quan** chứ không đỏ cả suite; thông báo lỗi đọc là hiểu bug gì. Ảnh nằm trong repo | Nói được vì sao mutation kiểu "sửa `toBe(201)` thành `toBe(200)`" **yếu hơn** phá sản phẩm thật — cái đầu chỉ chứng minh assertion có chạy, cái sau chứng minh test bắt được bug; họ trả giá gì để làm cách mạnh (dựng lại môi trường, phải revert) và chỗ nào chấp nhận cách yếu |
| S2.3-a | Có `e2e-plan.md` nêu luồng chọn **và luồng bị loại + lý do** | `qa-automation/tests/e2e/e2e-plan.md` § luồng được chọn + § luồng bị loại và lý do | Đúng 5 luồng chọn, mỗi luồng ghi vì sao đáng e2e; danh sách loại có lý do bám **tiêu chí tầng** (kiểm được ở API thì không lên e2e), không phải "không đủ thời gian" | Bảo vệ được một luồng **bị loại**: nếu nó hỏng thật thì ai phát hiện và sau bao lâu — đánh đổi giữa chi phí một e2e (giờ viết + giờ bảo trì mỗi năm) và độ trễ phát hiện lỗi mà họ chấp nhận |
| S2.3-b | 5 e2e phủ luồng chính; selector bền; **không** XPath vị trí | `qa-automation/tests/e2e/*.spec.ts` (5 spec) — selector theo thứ tự ưu tiên của S2.3 mục 3.2 | Không có XPath theo vị trí và không có chuỗi CSS class do framework sinh ra; selector trỏ vào thuộc tính có ý nghĩa (`getByTestId` / `getByRole` / `getByLabel`); app thiếu `data-testid` thì có ghi chú đã đề nghị dev thêm | Nói được đánh đổi khi bám `getByRole` theo nhãn hiển thị: đọc như người dùng, nhưng **vỡ khi đổi copy hoặc thêm ngôn ngữ** — vì sao vẫn chọn nó thay vì CSS class, và họ chấp nhận sửa bao nhiêu test mỗi lần copy đổi |
| S2.3-c | **Không** `waitForTimeout`/`sleep` trong toàn suite | Toàn `qa-automation/tests/`, `fixtures/`, `helpers/` — grep `waitForTimeout` / `sleep` không ra kết quả; chỗ cần chờ dùng `expect(...)` hoặc `waitForResponse` | Grep sạch thật, kể cả trong helper và fixture; mỗi chỗ chờ là chờ **một điều kiện cụ thể** (element hiện ra, response tạo đơn về) chứ không phải chờ trang "nói chung" | Cân được đánh đổi mà `waitForTimeout` **thật sự** mua bán: trả bằng thời gian chạy cộng dồn cho mọi lượt, mà xác suất đỏ vẫn còn nguyên — tức là chỉ giấu chứ không sửa flaky; nêu một chỗ họ từng thật sự phải chờ (animation, debounce) đã xử lý bằng cách nào và mất gì |
| S2.3-d | Bối cảnh dựng bằng API/seed, chỉ đi UI ở phần đang test | `qa-automation/tests/e2e/*.spec.ts` — phần chuẩn bị gọi API/seed rồi deep-link tới màn cần test; `README.md` bảng thời gian chạy **trước/sau** | Không spec nào click qua UI để đăng ký, đăng nhập hay thêm giỏ khi đó không phải phần đang test; bảng thời gian có **con số thật** đo trước và sau khi áp seed qua API | Nói được cái giá của việc seed qua API: nhanh hơn nhiều nhưng **chính đoạn UI bị bỏ qua đó không còn ai bắt bug** — bug ở luồng thêm giỏ hàng sẽ lọt tới đâu, họ bù bằng test nào, và vì sao vẫn chấp nhận đánh đổi |
| S2.3-e | Assert cả UI lẫn dữ liệu; session tái sử dụng, `.auth/` không commit | `qa-automation/tests/e2e/` (spec checkout assert cả UI lẫn dữ liệu qua API) + `tests/auth.setup.ts` + `playwright.config.ts` § `projects` (`storageState`) + `.gitignore` | Assertion dữ liệu kiểm **quy tắc nghiệp vụ** (tổng tiền bằng tổng dòng hàng), không dừng ở "có đơn"; project `setup` chạy trước qua `dependencies`; `.auth/` không có trong git | Nói được đánh đổi khi **tái sử dụng một session cho cả suite**: tiết kiệm mỗi lần đăng nhập, nhưng các test dùng chung một tài khoản nên dễ giẫm dữ liệu của nhau khi chạy song song — họ chặn bằng gì và còn chấp nhận rủi ro nào |
| S2.3-f | `--repeat-each=3 --workers=2` vẫn xanh; flaky sửa nguyên nhân, không tăng retries | Link CI run hoặc báo cáo đã commit của **lượt chạy lặp** đó + `playwright.config.ts` (mức `retries`) + `AUDIT.md` § flaky đã sửa nguyên nhân gì | Bằng chứng lượt chạy lặp nằm trong repo hoặc CI, không phải lời kể; config không đặt `retries` cao để che; mỗi flaky từng gặp có ghi **nguyên nhân theo bảng S2.3 mục 3.7** và cách sửa tận gốc | Nói được khi nào `retries` là lựa chọn **hợp lệ** (phụ thuộc hạ tầng ngoài tầm kiểm soát) và cái giá của nó: mua được pipeline xanh, trả bằng việc mất tín hiệu đỏ; ngưỡng cụ thể của họ là bao nhiêu |
| S2.3-g | Dùng được trace viewer để chỉ ra nguyên nhân một lần fail | `qa-automation/evidence/` — file trace hoặc ảnh chụp trace viewer của một lần đỏ, kèm chú thích chỉ ra bước nào hỏng và bằng chứng nào trong trace dẫn tới kết luận | Trace là của một lần đỏ **thật** (phá sản phẩm hoặc build đỏ trên CI); chú thích trỏ vào request hoặc trạng thái DOM cụ thể tại giây fail, không mô tả chung chung; config có bật `trace` khi retry và `screenshot` khi fail | Nói được vì sao trace kết luận nhanh hơn chạy lại `--headed`, **và cái giá của việc bật trace**: artifact nặng hơn, chạy chậm hơn — họ chọn mức nào (`on` / `on-first-retry` / `off`) và mất gì ở mức đó |
| S2.4-a | Helper/fixture tách khi lặp ≥3 lần, không trừu tượng hoá thừa | `qa-automation/helpers/` + `fixtures/` + `pages/` (nếu có) + `README.md` § refactor (trước bao nhiêu dòng, sau bao nhiêu, tách những gì) | Mỗi helper/fixture có **≥3 chỗ gọi thật** trong suite; Page Object chỉ tồn tại cho màn hình bị ≥3 test thao tác và **không chứa assert**; README ghi con số trước/sau chứ không mô tả suông | Chỉ ra được một chỗ họ **cố ý không tách** dù đã lặp: vì sao tách ở đó làm khó đọc hơn là tiết kiệm, và ai trả giá nếu chỗ đó lặp thêm vài lần nữa |
| S2.4-b | CI chạy API → E2E mỗi PR, artifact lưu kể cả khi fail | `qa-automation/.github/workflows/` — job API rồi job E2E có `needs`, bước `upload-artifact` có `if: always()`, secret qua `secrets`; kèm link **1 run xanh và 1 run đỏ** | Workflow chạy trên `pull_request`; thứ tự nhanh → chậm ràng bằng `needs`; `if: always()` có ở **cả hai** job; dùng `npm ci` chứ không `npm install`; không có secret nằm trong file | Nói được đánh đổi của `needs`: tiết kiệm 10 phút mỗi khi API đỏ, nhưng lần chạy đó **mất luôn thông tin e2e** — khi nào họ bỏ ràng buộc để chạy song song, và trả bằng gì |
| S2.4-c | Đã tải artifact từ build đỏ và dùng trace kết luận nguyên nhân | `qa-automation/AUDIT.md` § build đỏ (hoặc `evidence/`) — link run đỏ + chú thích cho thấy đã tải artifact, mở trace, và kết luận nguyên nhân + loại đỏ | Build đỏ là run thật của repo này; chú thích nêu bước nào fail, **dòng lỗi đầu tiên**, bằng chứng trong trace, và xếp vào sản phẩm hỏng / test hỏng / hạ tầng-flaky kèm bước xác nhận tiếp theo | Nói được vì sao `if: always()` là dòng đắt nhất trong pipeline (thiếu nó thì đúng lúc cần bằng chứng lại không có), **và đánh đổi khi lưu artifact**: dung lượng, thời gian upload, hạn lưu — họ chọn mức nào và mất gì khi cắt |
| S2.4-d | Có `AUDIT.md` tự audit suite, nêu cả lỗ hổng phủ còn lại | `qa-automation/AUDIT.md` — đủ 6 câu của S2.4 mục 3.5 + mục lỗ hổng phủ còn lại | Mỗi phát hiện trích **đúng tên test hoặc dòng code** làm bằng chứng và ghi đã xử lý ra sao (xoá / sửa / giữ + lý do); mục lỗ hổng nêu **vùng rủi ro nghiệp vụ cụ thể** chưa có test nào phủ, không phải "còn nhiều thứ chưa phủ" | Nói được vì sao **để lại** một lỗ hổng thay vì viết thêm test: giờ viết cộng bảo trì đặt cạnh rủi ro thật của vùng đó, cái gì phải xảy ra thì họ đóng nó, và ai gánh rủi ro trong lúc chờ |
| S2.4-e | Clone repo về máy trắng chạy được theo đúng README | `qa-automation/README.md` § "Chạy thế nào" (3 lệnh) + bằng chứng máy trắng: **link CI run xanh từ commit đang chấm** (CI chính là máy trắng) hoặc log lần clone sạch đã commit | README đủ 5 câu của S2.4 mục 3.6, gồm mục "cố ý chưa phủ gì và vì sao"; lệnh đúng thứ tự `npm ci` → cài trình duyệt → chạy test; `.env.example` đủ biến; CI xanh từ commit đang chấm | Nói được cái giá của việc suite phụ thuộc app chạy local: người review không chạy được nếu không tự dựng Toolshop — họ giải quyết ra sao (compose, môi trường công khai, tách nhóm test không cần app) và đánh đổi gì khi chọn cách đó |
| S2.5-a | Xếp đúng ≥9/12 câu vào PLAN hay STRATEGY, mỗi câu có lý do | `qa-automation/tai-lieu/` — bảng 12 câu của S2.5 Bước 2 với cột PLAN/STRATEGY + cột lý do (thường nằm trong `phan-bien-tai-lieu.md`) | ≥9/12 đúng; mỗi lý do dùng quy tắc *"câu này còn đúng ở release sau không"*; hai câu ranh giới (môi trường staging và định nghĩa exit) có lập luận chứ không đoán bừa | Nói được đánh đổi khi **đẩy một luật lên strategy** thay vì để trong plan: strategy ổn định và ai vào dự án cũng đọc, nhưng sửa rất chậm vì phải thuyết phục cả nhóm; plan linh hoạt nhưng mỗi release phải quyết lại từ đầu — họ đặt luật nào ở đâu và vì sao |
| S2.5-b | `test-plan-dot-01.md` có entry/exit criteria **và** "rủi ro còn lại khi phát hành" | `qa-automation/tai-lieu/test-plan-dot-01.md` § 5 "Entry / Exit criteria" và § 7 "Rủi ro còn lại khi phát hành" | Đủ 7 mục trong ≤2 trang; entry/exit là điều kiện **kiểm được** (con số, trạng thái) chứ không phải mô tả; mục 6 (rủi ro **của việc test**) và mục 7 (rủi ro **của sản phẩm** khi phát hành) không lẫn vào nhau | Nói được đánh đổi khi siết exit criteria (ví dụ "không còn bug High mở"): chất lượng cao hơn nhưng release trễ và mở đường cho việc hạ severity để lách — họ đặt ngưỡng ở đâu, ai chịu hệ quả của ngưỡng đó |
| S2.5-c | `test-strategy.md` ≤ 2 trang, mọi con số đo từ CI thật | `qa-automation/tai-lieu/test-strategy.md` (8 mục) + nguồn của 4 con số ở S2.5 Bước 3: thời gian suite trên CI · số test mỗi tầng · tỉ lệ flaky qua 10 lượt · thời gian nhóm smoke | Đủ 8 mục trong ≤2 trang; **cả 4 con số truy được** về một CI run hoặc một lệnh đã chạy có bằng chứng trong repo — không có số tròn đẹp không rõ nguồn; nhóm `@smoke` có thật trong suite để đo được | Nói được đánh đổi khi cắt tài liệu xuống 2 trang: mất ngữ cảnh cho người mới vào dự án, đổi lại là **có người đọc thật** — câu nào họ tiếc nhất khi cắt và vì sao vẫn cắt |
| S2.5-d | Có ≥3 dòng "**KHÔNG** tự động hoá X **vì** Y, thay vào đó Z" cụ thể tới sản phẩm | `qa-automation/tai-lieu/test-strategy.md` § 2 "Phạm vi tự động hoá" — ≥3 dòng đúng mẫu | Mỗi dòng nói đúng thứ của app này, **copy sang dự án khác là sai ngay**; lý do bám tiêu chí loại ở S2.5 mục 3.5 (không có oracle máy đọc được, còn đổi liên tục, phụ thuộc bên thứ ba…); phần Z là cách kiểm thay thế cụ thể, không phải "test tay" chung chung | Chạy được **phép thử ROI bằng con số** cho ≥1 dòng (số lần chạy mỗi năm × thời gian test tay đặt cạnh giờ viết + giờ bảo trì) và nói được con số nào đảo ngược quyết định — dấu hiệu họ cân đánh đổi chứ không phát biểu nguyên tắc |
| S2.5-e | Chỉ ra được ≥1 assertion đang nằm sai tầng + nên chuyển đi đâu | `qa-automation/tai-lieu/test-strategy.md` § 3 "Phân tầng" — bảng quyết định tầng của S2.5 Bước 4a, ≥1 dòng đánh dấu sai tầng kèm nơi nên chuyển và lý do | Assertion chỉ ra là assertion **có thật trong suite của họ** và trỏ được vào tên test cụ thể; lý do nêu rõ tầng dưới chứng minh được điều đó bằng cách nào | Áp được luật ngón tay cái (lên tầng cao hơn là chậm ~10× và hỏng vặt ~10×) vào chính suite mình: chuyển assertion đó xuống thì tiết kiệm bao nhiêu, **mất bằng chứng gì** (không còn chứng minh người dùng thấy được trên trình duyệt) — và vì sao vẫn chuyển, hoặc vì sao vẫn giữ |
| S2.5-f | Chính sách flaky đủ 4 dòng: ngưỡng · ai fix · bao lâu · quá hạn thì sao | `qa-automation/tai-lieu/test-strategy.md` § 7 "Flaky & sở hữu" | Ngưỡng có số **và có cách đo** (`--repeat-each=10`); người fix là một vai cụ thể; thời hạn tính bằng ngày làm việc; quá hạn thì quarantine — tách khỏi pipeline chính nhưng vẫn chạy nightly và ghi vào `AUDIT.md`, không xoá âm thầm | Nói được vì sao `retries: 2` không sửa flaky mà chỉ làm mình thôi nhìn thấy nó, **và cái giá của quarantine**: pipeline sạch lại nhưng vùng đó mất phủ trong lúc chờ — ai gánh, và bao lâu thì họ coi là quá lâu |
| AI | Chỉ ra được ≥1 test/selector do AI sinh bị rỗng hoặc bịa, và cách phát hiện | `qa-automation/tests/api/README.md` § "AI hỗ trợ ở đâu" (prompt đã dùng, số test AI sinh, số bị loại + lý do) hoặc `qa-automation/tests/e2e/README.md` § "AI hỗ trợ ở đâu" (selector AI bịa, cách phát hiện) | Chỉ ra **test hoặc selector cụ thể** bị loại: test chỉ assert status (rỗng), hoặc selector không tồn tại trong DOM app; cách phát hiện là thao tác thật (chạy thử không tìm thấy element / phá sản phẩm mà test vẫn xanh), không phải nhận xét chung | Nói được ràng buộc nào trong prompt chặn được cái gì và cái gì **không chặn nổi** — đánh đổi khi siết prompt chặt hơn (AI trả về ít hơn, đầy dòng "CẦN LẤY SELECTOR") so với để rộng rồi tự lọc, và họ chọn phía nào ở bước nào |
| AI | Chỉ ra được ≥1 câu chung chung trong tài liệu do AI gợi ý và đã thay bằng nội dung riêng của dự án | `qa-automation/tai-lieu/phan-bien-tai-lieu.md` — bản nháp trước phản biện + phản biện của AI + quyết định từng điểm (sửa gì / giữ gì kèm lý do bảo vệ) | Có ≥1 câu **copy sang dự án khác vẫn đúng** được chỉ ra, và trích được **cả hai bản** (trước và sau khi thay bằng nội dung riêng của suite này); có ≥1 điểm họ **giữ nguyên** kèm lý do bảo vệ chứ không sửa hết theo AI | Nói được vì sao câu chung chung nguy hiểm hơn câu sai — câu sai bị bắt ngay, câu chung chung được gật đầu rồi không ai làm theo; **đánh đổi khi viết cụ thể** (phải cập nhật mỗi lần dự án đổi) mà họ vẫn chọn |

**Lưu ý về đường dẫn `utils/` và `helpers/`:** capstone S2.1 nộp vào `qa-automation/utils/`,
còn cấu trúc chuẩn ở S2.4 mục 3.2 dùng `helpers/` — bước refactor của S2.4 chuyển sang
`helpers/`. Chấp nhận cả hai vị trí, miễn **khớp với README của repo**. Đường dẫn trong
README nói một đằng, file nằm một nẻo thì đó là lỗi thuộc S2.4-e, không phải S2.1-a.

> **Tiêu chí không bắt buộc:** khác GĐ0 và GĐ1, checklist nguồn GĐ2 **không có dòng nào
> thiếu ✔** — cả 28 dòng đều bắt buộc và đều nằm trong bảng trên. Nhưng "Checklist năng
> lực" (mục 5) của từng module còn vài tiêu chí không lên tới checklist giai đoạn: giải
> thích được vì sao thiếu `await` là nguy hiểm (S2.1), phân biệt charter/plan/strategy bằng
> ví dụ tự nghĩ (S2.5), trả lời được 5 câu phỏng vấn có dẫn chiếu tài liệu (S2.5). Xử lý
> chúng theo cùng một luật: **hỏi được ở tầng 1** để phân loại điểm 3, nhưng **không tính
> vào Điểm TB** của buổi thi và không ghi thành điểm trong hồ sơ; trả lời kém ở đó chỉ
> chặn điểm 3, không bao giờ đánh trượt.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

1. **`async/await` và xử lý lỗi** — quên `await` thì test "pass" sai như thế nào; vì sao try/catch phải ném lại thay vì nuốt lỗi. *(S2.1)*
2. **Đọc stacktrace** — dòng nào nói *lỗi gì*, dòng nào nói *ở đâu*; vì sao phải bỏ qua các dòng trong `node_modules`. *(S2.1)*
3. **Năm tầng assertion và "test rỗng"** — kể đủ 5 tầng; test chỉ có tầng 1 để lọt loại bug nào; vì sao tầng 3 và 4 mới bắt được bug thật. *(S2.2)*
4. **Test độc lập & chạy lại được** — ba quy tắc bất di bất dịch; vì sao hard-code email cố định là bom hẹn giờ. *(S2.2)*
5. **Test phải biết FAIL** — mutation thủ công là gì; vì sao "suite xanh" không phải bằng chứng; đây là **nguyên tắc 3 của Level 0**. *(S2.2)*
6. **Cái gì đáng e2e** — vì sao một app thường chỉ cần 5–15 e2e; 20 tổ hợp validate của một form thì test ở tầng nào và vì sao. *(S2.3)*
7. **Thứ tự ưu tiên selector** — vì sao XPath theo vị trí bị cấm; app chưa có `data-testid` thì làm gì trước khi viết cả suite. *(S2.3)*
8. **Chờ đúng cách** — Playwright tự chờ ở đâu; `waitForTimeout` sai ở hai mặt nào cùng lúc. *(S2.3)*
9. **Spine của một e2e chuẩn** — 5 bước; vì sao dựng bối cảnh bằng API lại khiến test đỏ **đúng chỗ** hơn. *(S2.3)*
10. **Flaky: nguyên nhân thật** — bốn triệu chứng và nguyên nhân tương ứng; vì sao thêm `retries` là nợ kỹ thuật có lãi. *(S2.3, S2.5)*
11. **Ba tầng tái sử dụng** — helper → fixture → Page Object, mỗi tầng dùng khi nào; vì sao đừng bắt đầu bằng POM; POM chứa gì và **không** chứa gì. *(S2.4)*
12. **Pipeline ở mức hiểu, không phải copy** — `if: always()` giải quyết chuyện gì; vì sao xếp API trước E2E; vì sao `npm ci` chứ không `npm install`. *(S2.4)*
13. **Charter vs Plan vs Strategy** — quy tắc phân loại một câu bất kỳ; bắt lấy ví dụ mỗi loại từ chính tài liệu họ viết. *(S2.5)*
14. **Quyết định tầng và tiêu chí LOẠI** — bốn câu hỏi dừng ở YES đầu tiên; ba điều kiện để chọn auto và các dấu hiệu loại; phép thử ROI thô. *(S2.5)*
15. **Metric đo đúng** — vì sao "số test đã tự động hoá" là metric nguy hiểm nhất; metric nào khó bóp méo nhất. *(S2.5)*
16. **Ràng buộc trong prompt cho AI viết test** — ràng buộc nào chặn selector bịa, ràng buộc nào chặn test rỗng. *(AI)*

### Tầng 2 — Đào sâu vào bài của học viên

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC — ở cửa này là **đọc thẳng code họ viết** — điền
chỗ trống bằng nội dung thật, rồi mới hỏi. Câu hỏi không có chỗ trống đã điền = câu lý
thuyết trá hình, không tính là tầng 2. Tầng này chống học thuộc và chống bài do AI viết —
**một câu 0 điểm ở đây là phủ quyết**, trượt bất kể điểm trung bình.

1. *"Trong `<file spec>`, test `<tên test>` bạn dùng selector `<trích selector>`. **Vì sao chọn selector này** mà không phải `<lựa chọn kề, ví dụ getByRole thay cho getByTestId>`? Dev đổi `<thứ gì đó trong DOM>` thì test này còn chạy không?"*
2. *"Đọc qua `tests/e2e/` của bạn — **chỗ nào trong suite này sẽ flaky trước**? Tôi để ý `<tên spec>` ở bước `<trích bước cụ thể>`; bạn thấy chỗ nào, và vì sao là chỗ đó chứ không phải chỗ khác? Đã chạy `--repeat-each` đủ để biết chưa hay đang đoán?"*
3. *"Test `<tên test>` assert `<trích assertion>`. Nếu tôi sửa sản phẩm để `<mô tả một bug cụ thể>`, test này có đỏ không? Nếu không thì bug đó ai bắt?"*
4. *"`evidence/` của bạn có `<n>` mục. Chọn mục `<tên>` — bạn đã phá cái gì, test nào đỏ, và thông báo lỗi có đủ để người khác hiểu bug không? Cho tôi xem chỗ bạn phá."*
5. *"Trong `helpers/<tên file>`, hàm `<tên hàm>` có try/catch ở `<vị trí>`. Nếu bỏ dòng `throw` đi thì test hỏng ở đâu — và vì sao nó vẫn có thể xanh?"*
6. *"`e2e-plan.md` loại luồng `<tên luồng>` với lý do `<trích>`. Nếu luồng đó hỏng trên production, ai phát hiện đầu tiên và sau bao lâu? Bạn vẫn giữ quyết định đó chứ?"*
7. *"Spec `<tên spec>` dựng bối cảnh bằng `<API/seed nào>` rồi mới đi UI. Đoạn UI bạn vừa nhảy qua — bug ở đó ai bắt? Có test nào của bạn phủ nó không?"*
8. *"`playwright.config.ts` của bạn đặt `retries: <n>` và `trace: <giá trị>`. Vì sao là con số đó? Đổi `retries` thành 0 thì tuần này CI của bạn đỏ mấy lần?"*
9. *"`AUDIT.md` ghi lỗ hổng phủ `<trích>`. Nếu vùng đó hỏng thì hệ quả nghiệp vụ là gì, và vì sao bạn vẫn để đó thay vì viết thêm một test?"*
10. *"Bảng thời gian trước/sau trong README ghi `<n>` giây xuống `<m>` giây. Con số đó đo lúc nào, trên máy nào? Nếu tôi chạy trên CI thì khác bao nhiêu, và vì sao?"*
11. *"Trong `test-strategy.md` § 2, dòng `KHÔNG tự động hoá <trích>`. Nếu quản lý bảo 'auto luôn đi', bạn phản bác bằng con số nào? Ước lượng giúp tôi giờ viết và giờ bảo trì."*
12. *"§ 3 của strategy nói assertion `<trích>` đang nằm sai tầng. Chỉ cho tôi đúng test đang chứa nó — chuyển xuống API thì mình mất khả năng chứng minh điều gì?"*
13. *"§ 7 chính sách flaky của bạn ghi ngưỡng `<trích>`. Đo bằng lệnh nào, kết quả gần nhất là bao nhiêu? Test nào đang vi phạm ngưỡng đó ngay lúc này?"*
14. *"`test-plan-dot-01.md` § 5 ghi exit criteria `<trích>`. Đợt test kết thúc mà tiêu chí đó chưa đạt thì bạn viết gì trong báo cáo, và ai là người quyết?"*
15. *"`phan-bien-tai-lieu.md` cho thấy bạn **giữ nguyên** điểm `<trích>` dù AI phản đối. Bảo vệ nó giúp tôi. Nếu 6 tháng nữa suite bị bỏ hoang thì lý do khả dĩ nhất theo hai tài liệu này là gì?"*
16. *"Mục 'AI hỗ trợ ở đâu' ghi AI sinh `<n>` test, bạn loại `<m>`. Chọn một test bị loại — nó rỗng ở chỗ nào, và bạn phát hiện bằng cách nào chứ không phải bằng cảm giác?"*

### Tầng 3 — Tình huống

1. *"**CI đỏ lúc 9 giờ sáng**, cả team đang chờ merge. **15 phút đầu bạn làm gì**, theo thứ tự nào — và bạn phân biệt sản phẩm hỏng / test hỏng / flaky bằng bằng chứng nào trước khi báo cho ai?"*
2. *"Suite của bạn chạy 18 phút trên PR, dev bắt đầu merge trước rồi xem sau. Bạn có ba cách xử lý — chọn cách nào cho repo này và **cắt mất cái gì**?"*
3. *"Bạn nhận bàn giao một suite 60 e2e, xanh 100%, không ai nhớ nó bắt được bug nào. Ngày đầu tiên bạn làm gì để biết suite này có tác dụng thật không?"*
4. *"Dev sửa xong tính năng và bảo 'test của em đỏ vì em viết sai chứ sản phẩm đúng'. Bạn có trace và log. Xử lý ra sao, và ở đâu thì bạn chấp nhận là mình sai?"*
5. *"Một test đỏ ngẫu nhiên khoảng 1 trong 5 lần, sprint còn 2 ngày và nó đang chặn PR của người khác. Bạn làm gì hôm nay, và ghi lại cái gì?"*
6. *"Lead muốn bạn 'tự động hoá hết regression trong 2 tuần'. Trả lời thế nào — dựa vào tài liệu nào của bạn, và bạn đề nghị làm gì trong 2 tuần đó?"*
7. *"Phỏng vấn Junior Automation, người ta hỏi: 'làm sao em biết test của em có tác dụng?'. Bạn mở cái gì trong repo và nói gì trong 3 câu?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Giải thích được Page Object Model bằng lý thuyết nhưng không nói được vì sao dự án mình chia POM như vậy** — hoặc có POM cho màn hình chỉ 1 test đụng tới, hoặc POM chứa cả assert; hỏi "màn nào đáng POM trong repo này và vì sao" là đứng.
2. **Nói trôi "test phải biết FAIL" nhưng `evidence/` chỉ có ảnh sửa kỳ vọng cho sai** — chưa bao giờ phá sản phẩm thật, tức là chưa chứng minh test bắt được bug.
3. **Kể đủ 5 tầng assertion nhưng mở spec ra thì phần lớn test dừng ở status code** — và `AUDIT.md` không nhắc gì tới test rỗng.
4. **Đọc thuộc "không dùng `waitForTimeout`" nhưng grep ra `sleep` trong helper**, hoặc mọi chỗ chờ đều là `waitForLoadState` chung chung — biết luật, chưa hiểu vì sao có luật.
5. **Suite xanh tuyệt đối nhưng không giải thích được lần đỏ gần nhất là khi nào** — không có build đỏ nào trong lịch sử CI, tức là chưa từng dùng CI để tìm ra thứ gì.
6. **Nói được định nghĩa flaky và quarantine nhưng `retries` trong config đặt cao**, hoặc `AUDIT.md` không có tên test flaky nào — chính sách chép vào tài liệu chứ chưa từng thi hành.
7. **`test-strategy.md` trôi chảy nhưng mọi câu đều copy sang dự án khác vẫn đúng** — không có tên module, không có con số, không có dòng "KHÔNG tự động hoá" nào chạm vào sản phẩm này.
8. **Con số trong strategy tròn đẹp (5 phút, 1%, 20 test) nhưng không chỉ được run CI hay lệnh nào đã đo ra chúng** — số phỏng đoán, vi phạm thẳng tiêu chí S2.5-c.
9. **Code dùng pattern chưa từng thấy ở đâu khác trong repo** (cách viết fixture khác hẳn phần còn lại, comment tiếng Anh trong repo tiếng Việt) **và họ không sửa được nó khi bị yêu cầu đổi một chi tiết nhỏ** — dấu AI viết hộ; hỏi thẳng vào dòng đó.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `gd2 — <YYYY-MM-DD>`. Dòng "Nhánh nghề (Level 0)": ghi `hoàn tất Level 0` — nhánh này **hết cửa**, không mở cửa mới |
| 2. Bảng tiêu chí | Không còn cửa kế trong nhánh nghề. Lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; chỉ mở bảng mới nếu học viên chạy placement sang nhánh AI |
| 2. Capstone | `đạt` — kèm link repo `qa-automation` và link một CI run xanh |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `gd2` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt (ví dụ trace viewer chỉ dùng được một lần, hoặc tiêu chí chỉ vừa đạt 2) — để phiên sau quay lại |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa gd2, đạt — hoàn tất Level 0 |
```

**Cập nhật checklist nguồn** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-2.md`: rà
lại cột `Tự đánh giá`, tick đủ 28 tiêu chí đã chấm ≥2. Cột `Reviewer` **để trống** — ô đó
dành cho người làm automation thật muốn xác nhận thêm; `AUDIT.md`, `evidence/` và
`tai-lieu/test-strategy.md` là ba chỗ khó tự chấm nhất, khuyến khích học viên xin review
người thật đúng ba chỗ đó.

**Không có cửa kế tiếp trong nhánh nghề.** Nói rõ với học viên họ đang đứng ở đâu và ba
hướng đi tiếp trong `CHECKLIST-GIAI-DOAN-2.md` mục "Sau Level 0, đi đâu tiếp": nhánh AI
(`l1` → `l2` → `l3`, **cần chạy placement riêng** — đạt `gd2` không tự mở `l1`), chọn
hướng chuyên sâu ở Giai đoạn 4 của lộ trình sinh viên, hoặc đi xin việc ngay.

**Nhắc học viên:** giờ họ có **hai repo kể trọn một câu chuyện** — `qa-portfolio` (hiểu
chất lượng, test được như người đi làm) và `qa-automation` (tự động hoá được và nói được
vì sao làm vậy). Ranh giới cũng phải nói thẳng: đây là mức fresher/junior automation **có
sản phẩm chứng minh được**, chưa phải SDET — kiến trúc framework quy mô lớn, performance,
security, test infra là chặng sau, học khi đã đi làm.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

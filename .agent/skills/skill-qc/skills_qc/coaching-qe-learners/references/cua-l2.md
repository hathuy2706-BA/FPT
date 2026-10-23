# Cửa Level 2 — Practitioner (nhánh AI)

**Checklist nguồn:** `curriculum/level-2-practitioner/LEVEL-CHECKLIST.md`
**Cửa trước:** `references/cua-l1.md`
**Cửa sau:** `references/cua-l3.md`

Repo bằng chứng của cửa này: **repo / PR của dự án thật học viên đang làm** — không phải
`qa-portfolio`, không phải Toolshop. Capstone Level 1–3 đều là *"áp vào dự án thật"*, nên
bằng chứng phải sống ở nơi công việc thật của họ sống. Mọi đường dẫn dưới đây tính từ thư
mục `qe-ai/` trong repo đó — chính thư mục đã dùng ở cửa `l1`, không tạo chỗ mới.

Tên file dưới đây là **gợi ý của cửa**, không phải quy định của curriculum — và bản thân
thư mục `qe-ai/` cũng là quy ước do cửa đặt ra (khác `qa-portfolio` / `qa-automation` vốn
là quy định của Level 0). Chấp nhận tên khác miễn nội dung § đủ và đường dẫn thật được ghi
vào hồ sơ.

**Hệ quả bắt buộc — ẩn danh TRƯỚC khi đưa vào prompt và TRƯỚC khi commit.** Ở L2 mức độ
nguy hiểm cao hơn hẳn L1: bài của cửa này là **test data**, **log lỗi thật**, **story
thật**, **suite thật** — bốn thứ dễ dính PII, token và bí mật kinh doanh nhất. Học viên
phải thay bằng dữ liệu giả cùng hình dạng ở cả hai mốc: dán vào prompt là mốc một, commit
vào repo là mốc hai. Kỹ năng này đã được chấm ở cửa `l1` tiêu chí **M1.4** (bằng chứng
M1.4 đòi commit nguyên văn output gốc của AI, tức chép lại cả phần input đã dán vào) — vi
phạm ở đây không chỉ là lỗi của một dòng L2 mà là dấu hiệu cửa `l1` đã cho qua non. Thấy
dữ liệu thật trong bằng chứng → **không chấm dòng đó**, trả lại, và ghi vào mục "Chỗ yếu
cần ôn" của hồ sơ kèm mã `M1.4`.

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Bảng dưới có **7 dòng**, đúng bằng số dòng trong checklist nguồn.
**6 dòng chặn cổng** — `M2.1`, `M2.2`, `M2.4`, `M2.5`, `M2.6`, `Capstone` — phải đạt
**≥2**, mỗi dòng có đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ
sơ. Không bù trừ: một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

**`M2.3` là nhánh nâng cao** — `curriculum/README.md` đánh dấu *(nâng cao)*,
`LEVEL-CHECKLIST.md` ghi *(nâng cao, khuyến khích)* và nói thẳng "không chặn lên level với
bạn manual". Vì vậy: manual tester **bỏ trống M2.3 vẫn mở được cổng**. Nếu học viên có nộp
thì **chấm thật** và ghi điểm vào hồ sơ như mọi dòng khác — nhưng điểm dưới 2 ở M2.3
**không chặn**, chỉ ghi vào mục "Chỗ yếu cần ôn".

Khác GĐ0–GĐ2, `LEVEL-CHECKLIST.md` của L2 **không có cột `Bắt buộc ✔`** — nghĩa là mọi
dòng đều bắt buộc trừ đúng ngoại lệ `M2.3` nêu trên. Đừng đi tìm dấu ✔ trong file nguồn
rồi kết luận "không dòng nào bắt buộc".

**2. Capstone.** *"Áp ≥1 kỹ năng Level 2 vào dự án thật, có bằng chứng output"* — nghĩa là
**một trong các sản phẩm ở bảng dưới đã thật sự đi vào công việc**, không phải một bài thứ
bảy viết riêng để nộp:

| # | Phải có | Nội dung tối thiểu |
|---|---|---|
| 1 | Một output thật | bộ test case / charter + ma trận rủi ro / bộ test data / bug report / báo cáo audit — chọn ≥1, là file trong `qe-ai/` |
| 2 | Bằng chứng nó **được dùng** | link ticket, PR, comment, hoặc tài liệu sprint nơi output đó được người khác đọc và dùng |
| 3 | § "Kết quả thật" | ai đã dùng, quyết định nào đổi vì nó (thêm case vào đợt test, đổi mức severity, hoãn release, sửa suite) |

Output viết xong rồi nằm im trong repo → **chưa đạt capstone**: dòng checklist đòi *"áp
vào dự án thật"*, không phải *"viết cho đúng khuôn"*.

**3. Ràng buộc riêng của L2 — bằng chứng là OUTPUT của skill, không phải ảnh chụp chat.**

Mỗi tiêu chí `M2.x` gắn với đúng một skill QE trong repo. Bằng chứng hợp lệ là **sản phẩm
thật do việc dùng skill đó tạo ra trên bài thật**, đã commit:

| Tiêu chí | Skill phải dùng | Sản phẩm nộp |
|---|---|---|
| `M2.1` | `generating-test-cases` | bộ test case đã phân loại + danh sách case đã loại |
| `M2.2` | `designing-test-strategy` | test charter + ma trận rủi ro có ưu tiên |
| `M2.3` | `writing-automation-tests` | file test chạy được + bằng chứng đỏ đúng lúc |
| `M2.4` | `generating-test-data` | bộ test data đúng định dạng + ghi chú lần nạp thử |
| `M2.5` | `analyzing-bugs-and-logs` | báo cáo triage + bug report 6 phần |
| `M2.6` | `auditing-test-quality` | báo cáo audit có trích `path:line` |

**Ảnh chụp màn hình chat không tính điểm** — không phân biệt được với gõ tay, và không đọc
được bằng công cụ. Dùng nó để hỏi tiếp, không dùng để kết luận. Bài dán trong chat thì
phải commit vào `qe-ai/` rồi mới ghi điểm.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| M2.1 | Dùng AI phân tích 1 story: chỉ ra điểm mơ hồ + sinh test case phủ biên/âm, loại case AI bịa — skill `generating-test-cases` | `qe-ai/test-cases-<ma-story>.md` § "Story gốc" (link ticket + nguyên văn) + § "Câu hỏi làm rõ" (≥3 câu, mỗi câu kèm **câu trả lời thật từ BA/PO**) + § "Bộ case đã phân loại" (cột Loại ghi positive, negative hoặc boundary) + § "Giữ nguyên / Sửa / Loại bỏ" | ≥3 câu hỏi làm rõ có **câu trả lời thật của người**, không phải câu học viên tự đoán; bộ case phủ đủ ba loại và nhãn khớp nội dung case; § "Loại bỏ" có ≥1 case bị loại vì AI bịa, lý do trỏ vào **hành vi thật của app hoặc đúng câu chữ story**; không dòng nào để trống lý do | Nói được **đánh đổi khi cắt bộ case xuống**: cắt nhóm nào, rủi ro còn lại sau khi cắt là gì và ai gánh, vì sao bộ 15 case sống đáng hơn 40 case không ai cập nhật — kèm chi phí bảo trì thật của đội họ |
| M2.2 | Viết được test charter + ma trận rủi ro có ưu tiên cho 1 tính năng — skill `designing-test-strategy` | `qe-ai/charter-<tinh-nang>.md` § "Mục tiêu khám phá" + § "In-scope và Out-of-scope" + § "Ma trận rủi ro" (bảng có cột khả năng xảy ra, cột ảnh hưởng, cột ưu tiên) + § "Đã cắt gì và vì sao" + § "Kết quả chạy thử" (≥2 ý tưởng, có input và quan sát thật) | Charter nói rõ **cái gì không test trong phiên này**, không chỉ liệt kê ý tưởng; mỗi rủi ro có mức khả năng và mức ảnh hưởng **do người xếp**, lý do bám vào bối cảnh thật (lịch sử bug, lượng người dùng, cam kết SLA) chứ không phải xếp theo thứ tự AI liệt kê; ≥1 rủi ro bị cắt kèm lý do; § "Kết quả chạy thử" có input cụ thể và quan sát thật, kể cả khi khác dự đoán | Nói được **cái giá của một mục out-of-scope**: nếu vùng đó hỏng thì ai phát hiện, sau bao lâu, và điều gì xảy ra sẽ khiến họ kéo nó vào lại phiên sau — đánh đổi giữa 90 phút có giới hạn và độ trễ phát hiện lỗi họ chấp nhận |
| M2.3 | *(nâng cao, khuyến khích — **không chặn mở cổng**)* Viết automation test có AI hỗ trợ, test FAIL đúng khi có bug — skill `writing-automation-tests` | `qe-ai/automation/<ten-test>.spec.ts` (hoặc file test theo stack của họ) + `qe-ai/automation/README.md` § "Hành vi mong đợi viết trước khi hỏi AI" + § "AI sinh gì, tôi sửa gì" (trích cả bản gốc lẫn bản đã sửa) + **bằng chứng chạy nằm trong repo hoặc CI** cho cả hai chiều xanh và đỏ + link PR thêm test vào suite thật | Assertion chạm **hành vi nghiệp vụ** đã mô tả ở § đầu tiên, không dừng ở kiểu `toBeDefined` hay "khác 500"; § "AI sinh gì, tôi sửa gì" trích được đúng dòng đã siết lại và nói vì sao; bằng chứng đỏ là **phá sản phẩm hoặc dữ liệu đầu vào rồi test đỏ đúng test liên quan**, không phải sửa kỳ vọng cho sai; báo cáo chạy nằm trong repo hoặc là artifact của một CI run | Nói được **đánh đổi khi assert sâu tới tầng nghiệp vụ**: mỗi lần gọi thêm để xác nhận là thêm thời gian chạy và thêm một chỗ để flaky — test nào họ cố ý dừng nông hơn, lớp bug nào chấp nhận lọt vì lựa chọn đó |
| M2.4 | Sinh được bộ test data đa dạng (biên + unicode), đúng định dạng, không chứa dữ liệu thật — skill `generating-test-data` | `qe-ai/test-data-<entity>.json` (hoặc `.csv` / `.sql`) + `qe-ai/test-data-<entity>.md` § "Schema thật lấy từ đâu" (link code, migration hoặc API doc) + § "Prompt đã dùng" + § "Quan sát khi nạp thử" (từng nhóm hợp lệ, biên, unicode, không hợp lệ) | Schema **trích từ nguồn thật** có đường dẫn, không phải mô tả nhớ lại; bộ data đủ bốn nhóm — nhóm khối lượng lớn là tuỳ chọn theo capstone module, nên bảng đòi bốn còn tầng 1 hỏi năm là không vênh — và **nạp được thật** — § quan sát ghi nhóm nào bị từ chối, nhóm nào lưu sai; ≥1 bất thường tìm ra khi nạp; grep cả file không ra dữ liệu người thật (email công ty, số điện thoại, mã khách hàng) | Nói được **đánh đổi khi đẩy tỉ lệ nhóm biên và unicode lên cao**: bắt được lớp bug encode và giới hạn độ dài, nhưng bộ data khó đọc hơn và mỗi lần schema đổi phải sinh lại — họ giữ tỉ lệ nào, và bỏ nhóm nào trước khi thiếu thời gian |
| M2.5 | Phân tích log lỗi + viết bug report tái hiện được, có giả thuyết nguyên nhân đã kiểm chứng — skill `analyzing-bugs-and-logs` | `qe-ai/bug-<ma-ticket>.md` § "Log gốc đã che" + § "Giả thuyết AI đưa ra" + § "Kiểm chứng" (số lần gọi lại, input từng lần, kết quả từng lần) + § "Bug report" (đủ 6 phần: tiêu đề, môi trường, bước tái hiện, mong đợi vs thực tế, mức độ, log đính kèm) + link ticket thật | § "Kiểm chứng" có **số lần và kết quả từng lần**, kết luận ghi rõ xác nhận hay bác bỏ; phần nguyên nhân trong bug report diễn đạt đúng mức — đã tái hiện thì viết "đã xác nhận kèm bằng chứng", chưa tái hiện thì viết "nghi ngờ, cần kiểm tra thêm", không bê nguyên khẳng định của AI; log đính kèm là đoạn liên quan trực tiếp đã che, không phải cả file; severity có một câu lý do bám tác động quan sát được | Nói được **đánh đổi ở chỗ dừng điều tra**: điều tra thêm một tầng nữa tốn bao lâu, đổi lại dev tiết kiệm được gì — và cái giá của việc đoán bừa nguyên nhân trong report: dev đi sai hướng hoặc đóng bug vì "không tái hiện được" |
| M2.6 | Audit 1 test suite bằng skill `auditing-test-quality`: chỉ ra ≥1 fake test + ≥1 khoảng trống | `qe-ai/audit-<module>.md` § "Fake hoặc tautological test" (mỗi mục có `path:line` + câu giải thích bằng lời của chính học viên) + § "Khoảng trống rủi ro" (xếp hạng, ưu tiên vùng tiền, bảo mật, ghi dữ liệu, tính điểm) + § "Nhận định" (một đoạn: suite này có đáng tin để release không) | Mọi phát hiện trích **đúng `path:line` trong suite thật của dự án**, mở ra đọc thấy khớp; mỗi fake test có lời giải thích riêng của học viên trả lời được "xoá tính năng thật đi thì test này còn pass không", không phải dán lại báo cáo AI; § "Khoảng trống" nêu **vùng rủi ro nghiệp vụ cụ thể** chứ không phải "còn nhiều chỗ chưa phủ"; hai loại phát hiện tách bạch, không gộp | Nói được **vì sao để lại một khoảng trống thay vì viết thêm test**: giờ viết cộng giờ bảo trì đặt cạnh rủi ro thật của vùng đó, cái gì phải xảy ra thì họ đóng nó, và ai gánh rủi ro trong lúc chờ |
| Capstone | Áp ≥1 kỹ năng Level 2 vào dự án thật, có bằng chứng output (test case / charter / bug report / data / báo cáo audit) | Một trong các file ở các dòng trên + **bằng chứng nó được dùng thật** (link ticket, PR, comment, tài liệu sprint) + § "Kết quả thật" ghi ai đã dùng và quyết định nào đổi vì nó | Bằng chứng "được dùng" là dấu vết của **người khác** — comment của lead, case được thêm vào đợt test, ticket đổi severity, PR sửa suite theo báo cáo audit — không phải học viên tự khẳng định. **QE đơn độc trong đội không ai đọc tài liệu QE** thì chấp nhận dấu vết trong chính hệ thống công việc: case đã vào bộ regression của đợt, ticket đổi trạng thái/severity theo report, commit sửa suite tham chiếu báo cáo audit — có ngày; § "Kết quả thật" nêu một quyết định cụ thể đã đổi, có ngày | Nói được **đánh đổi khi chọn đúng kỹ năng đó cho tình huống đó**: kỹ năng nào họ đã cân nhắc rồi bỏ, bỏ vì nó đắt hơn giá trị nhận lại ở chỗ nào, và trong bối cảnh nào thì lựa chọn đảo lại |

**Lưu ý về M2.1:** capstone module M2.1 cho phép kết luận *"không có case bịa"* mà không
loại case nào — nhưng đòi **giải thích đã đối chiếu bằng cách nào**. Cửa chấm theo đúng
tinh thần đó: § "Loại bỏ" trống **kèm** mô tả cách đối chiếu (đối với spec nào, mở app kiểm
field nào) vẫn đạt 2; trống trơn không kèm gì thì chưa có bằng chứng phân biệt đúng/sai
trong output AI — tối đa 1. Đừng đánh trượt chỉ vì con số case bị loại bằng 0.

**Lưu ý về M2.3:** hai chỗ lệch so với module, đều siết chặt hơn. (a) `LEVEL-CHECKLIST.md`
và `curriculum/README.md` xếp M2.3 là **nhánh nâng cao** — cửa không chặn vì dòng này, nói
rõ điều đó với học viên manual ngay từ đầu để họ không tưởng mình thiếu bài. (b) Capstone
module M2.3 nhận *"log hoặc screenshot output"* làm bằng chứng chạy, nhưng **luật bằng
chứng ở `SKILL.md` mạnh hơn**: output dán trong chat không tính điểm vì không phân biệt
được với gõ tay. Ở cửa này bằng chứng chạy phải nằm **trong repo hoặc CI** — file báo cáo
đã commit, link CI run, hoặc bạn tự chạy suite nếu repo có trên máy này.

**Lưu ý về M2.6:** hands-on module M2.6 cho dựng một `sample-suite/checkout.spec.js` ba
test để luyện tay. File đó **không tính là bằng chứng của cửa**: dòng checklist đòi audit
*"1 test suite"*, và capstone module M2.6 nói rõ là **một phần suite thật của dự án**. Bài
nộp chỉ có suite mẫu tự dựng → chưa chấm dòng M2.6, trả lại và hỏi họ chọn module nào
trong dự án để audit.

**Lưu ý về Capstone:** dòng `Capstone` **không phải bài thứ bảy**. Sáu module M2.1–M2.6 đều
đã có capstone riêng chạy trên dự án thật; dòng `Capstone` của level chọn **một trong số
đó** và đòi thêm đúng một thứ mà các dòng kia không đòi: **bằng chứng output đã đi vào
công việc và làm đổi một quyết định**. Vì vậy một file có thể vừa là bằng chứng của
`M2.5` vừa là bằng chứng của `Capstone` — nhưng **ghi hai điểm riêng** trong hồ sơ, chấm
theo hai cột khác nhau, đừng gộp.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

> **M2.3 là module nâng cao, có thể bỏ hợp lệ.** Câu 6 (và phần M2.3 của câu 5) chỉ hỏi
> khi học viên có nộp M2.3. Học viên bỏ M2.3 hợp lệ thì **không hỏi**, hoặc hỏi để phân
> loại điểm 3 nhưng **không tính vào Điểm TB** — không bao giờ đánh trượt vì nó.

1. **Vì sao phải hỏi câu hỏi làm rõ TRƯỚC khi sinh test case** — bỏ bước đó thì AI sinh thiếu loại case nào, và vì sao chính khái niệm "hết hạn" là thứ AI không thể tự có mốc. *(M2.1)*
2. **Hai lỗi đặc trưng của AI ở bước sinh test case** — bỏ sót biên vì không biết con số thật, và bịa hành vi hợp lý-nhưng-sai khi story thiếu chi tiết; phân biệt hai lỗi bằng cách rà nào. *(M2.1)*
3. **Charter vs Plan vs Strategy** — quy tắc phân loại *"câu này còn đúng ở release sau không"*; bắt lấy ví dụ mỗi loại từ chính tài liệu họ viết. *(M2.2)*
4. **Charter phải nói cái KHÔNG test** — vì sao out-of-scope mới là phần làm charter có giá trị; và vì sao để AI tự xếp ưu tiên rủi ro là sai. *(M2.2)*
5. **Test luôn xanh và test tautological** — ba dạng hay gặp; vì sao "suite xanh" không phải bằng chứng; mutation thủ công là gì. *(M2.3, M2.6)*
6. **Oracle trước, code sau** — vì sao chưa viết được câu "hành vi mong đợi là gì" thì chưa được nhờ AI viết test. *(M2.3)*
7. **Năm nhóm của một bộ test data đủ** — hợp lệ, biên, không hợp lệ, unicode, khối lượng lớn: nhóm nào hay bị bỏ sót nhất và lớp bug nào ẩn ở đó. *(M2.4)*
8. **Ba phần bắt buộc của một prompt sinh data** — schema, số lượng theo nhóm, định dạng xuất; thiếu phần nào thì AI đoán và đoán sai kiểu gì. *(M2.4)*
9. **PII và tuân thủ** — vì sao "ẩn phần nhạy cảm rồi dán phần còn lại" vẫn là vi phạm; cách thay bằng dữ liệu giả cùng hình dạng. *(M2.4, M2.5)*
10. **Stacktrace chỉ nơi exception nổi lên, không phải nơi lỗi bắt đầu** — ví dụ thiếu validate ở tầng trên nhưng lỗi nổ ở tầng DB; hệ quả nếu bug report ghi nhầm. *(M2.5)*
11. **Giả thuyết vs kết luận trong bug report** — cách diễn đạt khác nhau ra sao, và vì sao khác biệt đó quyết định dev đi đúng hay sai hướng. *(M2.5)*
12. **Xanh nghĩa là test đã chạy, không nghĩa là test đã kiểm được gì** — vì sao test giả nguy hiểm hơn test thiếu; bài kiểm tra nhanh đọc phần arrange so với phần assert. *(M2.6)*

### Tầng 2 — Đào sâu vào bài của học viên

> **M2.3 bỏ hợp lệ:** câu 7–8 dựa vào bằng chứng M2.3. Học viên không nộp M2.3 thì bỏ hai
> câu đó và bù bằng câu khác trong tầng này — **không** chấm 0 cho câu không hỏi, vì một số
> 0 ở tầng 2 là phủ quyết.

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC — ở cửa này gồm cả **đọc thẳng suite và file test
data họ nộp** — điền chỗ trống bằng nội dung thật, rồi mới hỏi. Câu hỏi không có chỗ trống
đã điền = câu lý thuyết trá hình, không tính là tầng 2. Tầng này chống học thuộc và chống
bài do AI viết — **một câu 0 điểm ở đây là phủ quyết**, trượt bất kể điểm trung bình.

1. *"Bộ test case bạn sinh ở `qe-ai/test-cases-<ma-story>.md` có `<N>` case — **case nào bạn đã CẮT và vì sao?** Chỉ cho tôi đúng dòng trong § 'Loại bỏ', và nói rủi ro còn lại sau khi cắt."*
2. *"Câu hỏi làm rõ `<trích một câu>` bạn ghi câu trả lời của BA là `<trích>`. Nếu BA trả lời ngược lại thì case nào trong bảng của bạn phải viết lại?"*
3. *"Case `<ID>` bạn gắn nhãn `<positive / negative / boundary>`. Vì sao là nhãn đó mà không phải nhãn kề? Cho tôi một case khác cùng nhãn nhưng kiểm thứ khác hẳn."*
4. *"Trong `qe-ai/charter-<tinh-nang>.md`, rủi ro `<trích>` bạn xếp khả năng `<mức>` và ảnh hưởng `<mức>`. Dựa vào cái gì trong dự án bạn — lịch sử bug, lượng dùng, hay đoán?"*
5. *"Charter của bạn để `<trích một mục out-of-scope>` ngoài phạm vi. Nếu vùng đó hỏng trên production, ai phát hiện đầu tiên và sau bao lâu? Bạn vẫn giữ quyết định đó chứ?"*
6. *"Bạn chạy thử ý tưởng `<trích>` và ghi quan sát `<trích>` — khác dự đoán trong charter ở chỗ nào? Phát hiện đó có làm bạn thêm rủi ro mới vào ma trận không?"*
7. *"Trong `qe-ai/automation/<ten-test>.spec.ts`, assertion `<trích>` kiểm điều gì? Nếu tôi sửa sản phẩm để `<mô tả một bug cụ thể>`, test này có đỏ không — và bạn đã thử chưa?"*
8. *"§ 'AI sinh gì, tôi sửa gì' cho thấy bạn siết `<trích bản gốc>` thành `<trích bản đã sửa>`. Bản gốc để lọt bug loại nào? Vì sao bạn nhận ra?"*
9. *"Trong `qe-ai/test-data-<entity>.json`, bản ghi `<trích một bản ghi nhóm biên>` — giá trị này là biên của rule nào, và bạn lấy rule đó từ đâu trong code?"*
10. *"Bạn ghi bất thường khi nạp thử là `<trích>`. Đó là bug của sản phẩm hay data bạn sinh sai định dạng? Bạn phân biệt hai khả năng đó bằng cách nào?"*
11. *"Trong `qe-ai/bug-<ma-ticket>.md`, giả thuyết AI đưa ra là `<trích>` còn kết luận của bạn là `<trích>`. Chỉ cho tôi **bằng chứng nào loại trừ giả thuyết còn lại** — không phải bằng chứng nào ủng hộ kết luận của bạn."*
12. *"Bug này bạn để mức `<severity>`. Nếu lead hạ xuống một bậc, bạn nói gì? Điều gì trong log hoặc trong tái hiện của bạn bảo vệ được mức đó?"*
13. *"Trong `qe-ai/audit-<module>.md` bạn gọi `<path:line>` là fake test. Xoá tính năng thật đi thì test đó còn pass không? Nói bằng lời của bạn, đừng đọc lại báo cáo."*
14. *"Khoảng trống `<trích>` bạn xếp ưu tiên cao nhất. Nếu vùng đó hỏng thì hệ quả nghiệp vụ là gì — và vì sao bạn vẫn chưa viết test cho nó?"*

### Tầng 3 — Tình huống

1. *"Suite đang xanh 100% và lead hỏi 'tin được không'. Bạn kiểm chứng thế nào, trong bao lâu, và bạn trả lời lead bằng đúng mấy câu?"*
2. *"Sprint còn 2 ngày, có 3 story mới chưa ai viết test case. Bạn dùng AI ở khâu nào, tự làm khâu nào, và bạn nói gì nếu vẫn không kịp phủ hết?"*
3. *"BA trả lời câu hỏi làm rõ của bạn bằng 'cứ làm như hệ thống cũ đi'. Bạn làm gì tiếp, và bạn ghi gì vào test case để sau này không ai hiểu nhầm?"*
4. *"Bug production, log có token và số điện thoại khách hàng thật, sếp giục phân tích ngay. Bạn xử lý theo thứ tự nào — và bạn từ chối làm gì?"*
5. *"Bạn nhận bàn giao một suite 200 test, coverage 90%, không ai nhớ nó bắt được bug nào. Ngày đầu tiên bạn làm gì để biết nó có tác dụng thật?"*
6. *"Dev phản bác báo cáo audit của bạn: 'test đó có từ lâu rồi, vẫn chạy tốt'. Bạn trả lời thế nào, và ở đâu thì bạn chấp nhận là mình sai?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Bộ test case không cắt case nào, và không kèm bằng chứng đối chiếu** — mọi case AI sinh nằm nguyên trong bản nộp, § "Loại bỏ" trống trơn. Capstone module M2.1 **có** cho phép kết luận "không có case bịa", nhưng đòi nói rõ đã đối chiếu bằng cách nào; trống trơn không kèm cách đối chiếu mới là dấu hiệu **nhận nguyên output AI**. Hỏi ngay case nào họ đã cân nhắc cắt rồi giữ lại và vì sao.
2. **Kể trôi quy trình 3 bước của M2.1 nhưng § "Câu hỏi làm rõ" không có câu trả lời của người** — mọi câu trả lời đều do học viên tự điền; nghĩa là chưa bao giờ hỏi BA thật, chỉ diễn lại bài tập.
3. **Charter dài, đủ mục, nhưng out-of-scope trống hoặc ghi "những thứ khác"** — biết định nghĩa charter, chưa từng phải bảo vệ một quyết định bỏ.
4. **Ma trận rủi ro xếp đúng thứ tự AI liệt kê** — cột khả năng và cột ảnh hưởng điền cho có, không dòng nào có lý do bám bối cảnh dự án; hỏi "vì sao dòng này cao hơn dòng kia" là đứng.
5. **Nói trôi "test phải biết FAIL" nhưng bằng chứng đỏ là sửa kỳ vọng cho sai** — chưa bao giờ phá sản phẩm, tức là chưa chứng minh test bắt được bug.
6. **Bộ test data đủ bốn nhóm nhưng chưa nạp thử lần nào** — § "Quan sát" ghi chung chung, không nhóm nào bị từ chối, không bất thường nào; hỏi "bản ghi 255 ký tự nạp vào ra sao" là tắc.
7. **Bug report ghi nguyên khẳng định của AI ở phần nguyên nhân** — "nguyên nhân là do…" mà § "Kiểm chứng" không có số lần gọi lại nào; đọc mượt nhưng chưa ai tái hiện.
8. **Báo cáo audit dán nguyên văn output của skill** — mỗi phát hiện có `path:line` nhưng không câu nào là lời của học viên; hỏi "xoá tính năng đi test này còn pass không" thì phải mở lại báo cáo mới trả lời được.
9. **Văn phong bài lệch hẳn cách họ nói trong chat**, code dùng pattern không có ở đâu khác trong repo dự án, hoặc comment tiếng Anh trong repo tiếng Việt — và không sửa nổi một chi tiết nhỏ khi bị yêu cầu đổi.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `l2 — <YYYY-MM-DD>`. Dòng "Nhánh AI": cửa đang mở đổi thành `l3`, module đang học `M3.1` |
| 2. Bảng tiêu chí | Thay bằng tiêu chí của cửa `l3`. **Không xoá bảng l2** — lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; đường dẫn bằng chứng cũ còn dùng lại khi placement hoặc khi nghi bài giả |
| 2. Capstone | `đạt` — kèm đường dẫn file output và link nơi nó được dùng thật (ticket hoặc PR) |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `l2` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt — nêu rõ nếu **M2.3 chưa làm** (bỏ qua hợp lệ nhưng L3 đòi code, cần biết trước), hoặc tiêu chí chỉ vừa đạt 2 |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa l2, đạt |
```

**Cập nhật checklist nguồn** `curriculum/level-2-practitioner/LEVEL-CHECKLIST.md`: rà lại
cột `Tự đánh giá`, tick các tiêu chí đã chấm ≥2. **M2.3 không nộp thì để trống**, không
tick hộ và cũng không coi là thiếu. Cột `Reviewer` **để trống** — ô đó dành cho QE senior
hoặc lead người thật muốn xác nhận thêm; báo cáo audit (`M2.6`) là chỗ khó tự chấm nhất,
khuyến khích học viên xin review người thật đúng chỗ đó.

**Mở cửa kế tiếp:** `l3` — đọc `references/cua-l3.md`, checklist nguồn
`curriculum/level-3-builder/LEVEL-CHECKLIST.md`, module đầu tiên
`curriculum/level-3-builder/M3.1-dung-ai-test-tool-chuyen-dung.md`.

**Nhắc học viên:** L3 là **nhánh nâng cao dành cho người đã vững code** — bằng chứng của
nó là code chạy được, không phải tài liệu. Ai bỏ qua `M2.3` ở L2 thì nói thẳng: L3 sẽ đòi
đúng thứ đã bỏ qua, nên nên quay lại làm `M2.3` trước khi mở `l3`. Ranh giới của L2 cũng
phải nói rõ: họ đã **tự chủ vòng đời test hằng ngày với AI**, nhưng vẫn là *người dùng*
công cụ, chưa *tự xây* công cụ.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

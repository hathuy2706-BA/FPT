# Cửa Level 3 — Builder (nhánh AI)

**Checklist nguồn:** `curriculum/level-3-builder/LEVEL-CHECKLIST.md`
**Cửa trước:** `references/cua-l2.md`
**Cửa sau:** — (cửa cuối nhánh AI)

Repo bằng chứng của cửa này: **repo / PR của dự án thật học viên đang làm** — không phải
`qa-portfolio`, không phải Toolshop. Capstone Level 1–3 đều là *"áp vào dự án thật"*. Ở
L3 bằng chứng là **code chạy được**, nên nó có thể sống ở một **repo công cụ riêng** của
học viên nếu repo công ty không nhận được — miễn **ghi rõ một chỗ trong hồ sơ** và không
đổi qua lại giữa các phiên. Mọi đường dẫn dưới đây tính từ thư mục `qe-ai/` trong repo đã
chọn, trừ các file adapter của `M3.2` vốn phải nằm đúng vị trí quy ước ở gốc repo.

Tên file dưới đây là **gợi ý của cửa**, không phải quy định của curriculum — và bản thân
thư mục `qe-ai/` cũng là quy ước do cửa đặt ra (khác `qa-portfolio` / `qa-automation` vốn
là quy định của Level 0). Chấp nhận tên khác miễn nội dung § đủ và đường dẫn thật được ghi
vào hồ sơ. Riêng `qe-ai/pipeline/`: **đánh số theo chặng là bắt buộc**, tên cụ thể thì
không — module chỉ nêu `01-input` … `04-summary` làm ví dụ, nên pipeline 5 chặng hay
pipeline triage-bug đặt tên khác vẫn hợp lệ miễn thứ tự chặng đọc ra được.

**Hệ quả bắt buộc — ẩn danh TRƯỚC khi đưa vào prompt và TRƯỚC khi commit.** Ở L3 rủi ro
lớn nhất trong ba cửa: script và pipeline **tự động gửi nội dung đi** mỗi lần chạy, nên
một requirement hay log dính dữ liệu công ty sẽ rời khỏi máy lặp đi lặp lại mà không ai
rà lại từng lượt. Học viên phải thay bằng dữ liệu giả cùng hình dạng ở cả hai mốc — dán
vào prompt là mốc một, commit vào repo là mốc hai — và phải chỉ ra được **chỗ nào trong
script** làm việc đó. Kỹ năng này đã chấm ở cửa `l1` tiêu chí **M1.4**; vi phạm ở đây là
dấu hiệu cửa `l1` cho qua non, ghi lại mã `M1.4` vào mục "Chỗ yếu cần ôn".

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Cả **4** tiêu chí trong bảng dưới đạt **≥2**, mỗi tiêu chí có
đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ sơ. Không bù trừ:
một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

Khác GĐ0–GĐ2, `LEVEL-CHECKLIST.md` của L3 **không có cột `Bắt buộc ✔`** — nghĩa là **mọi
dòng trong bảng đều bắt buộc**, kể cả dòng `Capstone (M3.4)`. Đừng đi tìm dấu ✔ trong file
nguồn rồi kết luận "không dòng nào bắt buộc". Bản thân L3 là **nhánh nâng cao** cho người
đã vững code — đó là điều kiện để *vào* cửa, không phải cái cớ để hạ chuẩn *trong* cửa.

**2. Capstone (M3.4).** Một pipeline QE chạy end-to-end trên ít nhất một input mẫu:

| # | Sản phẩm | Nội dung tối thiểu |
|---|---|---|
| 1 | `qe-ai/pipeline/` | log từng chặng, đánh số theo thứ tự chạy: `01-input.md`, `02-test-cases.md`, `03-test-run.log`, `04-summary.md` |
| 2 | Sơ đồ chặng | các chặng + input/output từng chặng, dạng text hoặc markdown là đủ |
| 3 | Điểm human-in-the-loop | **≥1 điểm dừng**, nêu rõ vị trí và rủi ro gì nếu bỏ nó |
| 4 | Một lần chạy thật | log của ít nhất một lượt end-to-end trên input thật, kèm nhận xét chỗ nào phải sửa lại so với thiết kế |

Không có điểm human-in-the-loop nào → **chưa mở cổng**, không thương lượng: M3.4 mục 2 ghi
thẳng đó là quy tắc bắt buộc, và hậu quả của một kết luận sai tự động (bỏ sót bug hoặc báo
bug giả) đắt hơn thời gian tiết kiệm được. Pipeline chạy được nhưng không có log lần vết
từng chặng cũng là **chưa xong** — hộp đen thì không debug được, đúng thứ tiêu chí này tồn
tại để chặn.

**3. Ràng buộc riêng của L3 — bằng chứng là CODE CHẠY ĐƯỢC, không phải mô tả.**

| | Đòi gì | Không tính là gì |
|---|---|---|
| a | **Đường dẫn file code** trong repo, mở ra đọc được | "em có viết một script làm việc đó" |
| b | **Bằng chứng chạy nằm trong repo hoặc CI** — file log đã commit, artifact CI run, hoặc bạn tự chạy nếu repo có trên máy này | output dán trong chat: không phân biệt được với gõ tay |
| c | **Không có secret trong code** — grep cả repo không ra key thật, `.gitignore` chặn `.env` | "key em xoá trước khi commit rồi" |

**Luật cứng của cửa này: hard-code API key = điểm 0, không thương lượng.** Không phải điểm
1 để sửa lại — 0, ghi lý do vào hồ sơ. Lý do: key gọi API tương đương một tấm thẻ tín
dụng, và key đã commit thì coi như đã lộ kể cả khi commit sau đó bị xoá (lịch sử git vẫn
giữ). Học viên phải **thu hồi key đó** rồi mới nộp lại bằng key mới đọc từ ENV. Áp cả cho
`M3.3` lẫn `Capstone (M3.4)` nếu pipeline có chặng gọi API.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| M3.1 | Áp được 1 AI test tool chuyên dụng lên Toolshop + nêu 2 hạn chế thực tế | `qe-ai/tool-<ten-tool>.md` § "Luồng đã áp" (luồng A hoặc B của M3.1 mục 4) + **output thật của tool đã commit** (file test tool sinh ra, ảnh báo cáo visual diff, hoặc collection xuất được) + § "Hai hạn chế tự quan sát" + § "Đánh giá 4 tiêu chí" (tích hợp, chi phí, độ chính xác, lock-in và lộ dữ liệu) | Output của tool là **file thật trong repo**, không phải mô tả bằng lời; nói đúng tool thuộc nhóm nào trong bốn nhóm và nhóm đó giải quyết vấn đề gì mà coding assistant thường không giải quyết được; **cả hai hạn chế là thứ họ tự gặp khi chạy** — selector tool sinh ra không ổn định, vùng nhiễu bị báo là khác biệt, case biên sinh thiếu so với Swagger — không phải hạn chế chép từ trang so sánh của vendor | Nói được **đánh đổi khi đưa tool này vào pipeline hiện có**: nó mua được gì (giờ viết test, lớp kiểm thử làm tay không nổi), trả bằng gì (license, khoá định dạng, dữ liệu rời khỏi hạ tầng công ty), và **tiêu chí nào sẽ khiến họ dừng pilot** — có con số hoặc mốc thời gian, không phải "nếu thấy không hợp" |
| M3.2 | Viết được 1 skill QE mới đúng chuẩn repo (SKILL.md hợp lệ + ≥1 adapter) và gọi được | `.claude/skills/<ten-skill>/SKILL.md` (frontmatter `name` khớp tên thư mục + `description` dạng *Use when …* có mệnh đề *Not for …*) + **đủ touch point** của `.claude/skills/writing-qe-skills/SKILL.md` § "Touch points when adding one skill": `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursor/rules/<ten>.mdc`, `.windsurf/rules/<ten>.md`, một dòng trong bảng skill của `README.md` + `qe-ai/skill-<ten>-output.md` (output một lần gọi thật trên tình huống thật) | `description` nói **KHI NÀO dùng** kèm câu hỏi ví dụ thật đồng nghiệp hay gõ, **không** tóm tắt quy trình — description leak quy trình thì AI đọc xong thấy đủ và bỏ qua thân skill, đó là lỗi bản chất chứ không phải lỗi trình bày; thân skill là quy trình từng bước + nguyên tắc, làm theo được mà không hỏi lại; **mọi adapter đều trỏ về bản gốc, không copy nội dung**; § output cho thấy assistant đi đúng quy trình đã viết, không bỏ bước | Nói được **đánh đổi khi siết `description` hẹp hơn**: gọi đúng lúc hơn nhưng bỏ lỡ những tình huống lân cận đáng lẽ nó phục vụ được — họ chọn ranh giới ở đâu, `Not for …` trỏ sang skill nào, và ai trả giá khi hai skill cùng bật hoặc cùng im |
| M3.3 | Viết script gọi Claude API tự động 1 việc QE; key đọc từ **ENV**, không hard-code — **hard-code key = điểm 0, không thương lượng** | `qe-ai/tools/<ten-script>.py` (hoặc file tương đương theo ngôn ngữ họ dùng): chỗ đọc `os.environ.get("ANTHROPIC_API_KEY")` và thoát sớm khi thiếu, biến model đọc từ `CLAUDE_MODEL`, lời gọi `client.messages.create`, khối bắt `APIConnectionError` và `APIError`, dòng in `response.usage.input_tokens` và `output_tokens` + `.gitignore` có `.env` + `qe-ai/tools/README.md` § "Việc lặp lại này là gì" + § "Output thật + token đã dùng" + § "Đối chiếu output với nguồn thật" | Script **chạy thật** và log lượt chạy nằm trong repo hoặc CI; output script sinh ra **đã được đối chiếu với nguồn thật** (Swagger / code / requirement) và loại được ≥1 case bịa — hoặc có bằng chứng đối chiếu khi kết luận không có case bịa; key chỉ đến từ ENV, thiếu biến thì script báo lỗi rõ ràng và dừng chứ không chạy tiếp với giá trị rỗng; ID model **không viết chết trong logic gọi API**; lỗi mạng và lỗi API đều được bắt và in thông báo đọc hiểu được, không crash bằng traceback thô; số token in ra sau mỗi lượt; grep cả repo và cả lịch sử commit không ra key thật | Nói được **đánh đổi khi chuyển việc này từ chatbot sang script**: được nhất quán và chạy hàng loạt, trả bằng chi phí token mỗi lượt cộng chi phí bảo trì khi prompt hay API đổi — và **ngưỡng cụ thể** (số lần chạy mỗi tháng, số token mỗi lượt) mà dưới ngưỡng đó họ sẽ quay lại làm tay |
| Capstone (M3.4) | Dựng 1 pipeline/agent QE chạy end-to-end trên 1 input mẫu, có điểm human-in-the-loop + log | `qe-ai/pipeline/` với log đánh số theo chặng (`01-input.md`, `02-test-cases.md`, `03-test-run.log`, `04-summary.md`) + `qe-ai/pipeline/README.md` § "Sơ đồ chặng" (input/output từng chặng) + § "Điểm human-in-the-loop" (vị trí, lý do, rủi ro nếu bỏ) + § "Pipeline hay agent và vì sao" | Chạy được end-to-end trên ít nhất một input **thật của dự án**, log đủ để chỉ ra một kết quả sai nằm ở chặng nào — mỗi file log có input nhận vào, prompt hoặc lệnh đã chạy, output nhận được; ≥1 điểm dừng đặt **sau chặng dễ bị AI hiểu sai hoặc bịa nhất**, kèm lý do vì sao là chỗ đó; nói được vì sao chọn pipeline tuần tự thay vì agent tự quyết; § tóm tắt cuối đã được **người đối chiếu lại với log gốc**, có ghi chú chỗ báo cáo AI nói lệch | Nói được **cái giá của mỗi điểm dừng thêm vào**: mỗi lần chờ người là bao nhiêu giờ trôi qua và pipeline mất bao nhiêu phần tốc độ, đổi lại chặn được lớp sai nào — chặng nào họ **cố ý không** đặt điểm dừng, và ai gánh nếu chặng đó sai hàng loạt |

**Lưu ý về M3.1:** dòng checklist level đòi áp tool **lên Toolshop** (đúng hands-on mục 4),
còn capstone module M3.1 lại là **bản đề xuất tool cho dự án thật**. Đây là hai thứ, không
phải một. Cửa chấm theo **dòng checklist**: bằng chứng bắt buộc là output thật chạy trên
Toolshop. Bản đề xuất cho dự án thật (`qe-ai/tool-<ten-tool>.md` § "Đề xuất áp dụng") là
bằng chứng **bổ sung** — dùng để phân loại điểm 3, thiếu nó thì tối đa 2, nhưng không chặn
mở cổng.

**Lưu ý về M3.2:** dòng checklist ghi *"SKILL.md hợp lệ + **≥1 adapter**"*, còn
`.claude/skills/writing-qe-skills/SKILL.md` § "Touch points when adding one skill" liệt kê
**7 touch point** và nói thẳng *"One touch point missed means one tool silently can't see
it"*. Cửa chấm theo **writing-qe-skills** — đây là chỗ siết hơn checklist, nói rõ lý do
cho học viên: skill này là kỹ năng **đóng gói cho cả team dùng chung**, mà thiếu một
adapter thì đúng nhóm dùng công cụ đó không bao giờ biết skill tồn tại, tức là hỏng đúng
mục đích của bài.

Nhưng đòi đủ 7 touch point trong **repo công ty** là không khả thi — nơi đó thường không có
`.cursor/`, `.windsurf/` hay Copilot. Nên thang điểm neo vào **công cụ team dùng thật**, chứ
không vào con số 7:

| Điểm | Khi nào |
|:---:|---|
| ≥2 | Đủ `SKILL.md` + adapter cho **mọi công cụ AI team đang dùng** |
| 1 | Thiếu adapter của một công cụ team đang dùng — trả lại bổ sung |
| 0 | Đủ `SKILL.md` nhưng không adapter nào |

Adapter cho công cụ team **không** dùng là bằng chứng bổ sung, dùng phân loại điểm 3 (họ
đóng gói cho cả hệ sinh thái chứ không chỉ cho mình). Hỏi học viên team dùng công cụ gì
trước khi chấm dòng này — đừng suy từ danh sách 7 file.

**Lưu ý về M3.3:** dòng checklist chỉ ghi hai thứ — *script gọi Claude API tự động 1 việc
QE* và *key đọc từ ENV, không hard-code*. Bốn thứ còn lại trong cột "Điểm 2" (model đọc từ
biến cấu hình, bắt lỗi API, in token, đối chiếu output với nguồn thật) lấy từ **checklist
năng lực mục 5 của module M3.3** — đó là định nghĩa của cụm *"script gọi Claude API"*
trong lộ trình này, không phải yêu cầu tự nghĩ ra. Riêng **hard-code key = 0** là luật của
cửa, không phải của module: module chỉ nói "sai tuyệt đối", cửa quy ra điểm để không có
chỗ thương lượng.

**Lưu ý về Capstone (M3.4) — cửa bỏ đường lui của module:** capstone module M3.4 cho phép
nộp *bản thiết kế chi tiết + một buổi demo giả lập* nếu chưa dựng được pipeline (hạn chế
công cụ hoặc quyền truy cập môi trường thật). Cửa **không** nhận đường lui đó, vì dòng
checklist level ghi thẳng *"pipeline/agent QE **chạy** end-to-end"* — và cả tiêu chí lẫn
bằng chứng của cửa đều dựa vào log lượt chạy thật, thứ mà bản thiết kế không sinh ra được.
Nói thẳng lý do cho học viên chứ đừng để họ tưởng bị chấm oan. Bị chặn thật vì môi trường:
pipeline chạy trên **input mẫu ẩn danh** ngay trên máy họ vẫn được tính — điều kiện là log
đủ bốn chặng và có điểm human-in-the-loop, không bắt buộc phải chạy trong hạ tầng công ty.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

1. **Bốn nhóm AI test tool chuyên dụng** — test generation, self-healing, visual, API: mỗi nhóm giải quyết vấn đề gì mà một coding assistant thuần văn bản không giải quyết được. *(M3.1)*
2. **Self-healing che giấu thay đổi hành vi thật** — khi nào "tự sửa selector" là tốt, khi nào nó vừa nuốt mất một lỗi hồi quy. *(M3.1)*
3. **Bốn tiêu chí chọn tool** — tích hợp, chi phí, độ chính xác, lock-in và lộ dữ liệu; vì sao con số benchmark của vendor không thay được một lượt pilot trên app của mình. *(M3.1)*
4. **`description` quyết định skill có được kích hoạt hay không** — vì sao nó phải nói KHI NÀO dùng chứ không tóm tắt quy trình; description leak quy trình gây hậu quả gì. *(M3.2)*
5. **Mô hình bản gốc + adapter mỏng** — vì sao adapter không bao giờ copy nội dung; bỏ sót một touch point thì ai mất gì. *(M3.2)*
6. **Một việc xứng đáng thành skill khi nào** — lặp lại, non-obvious, áp được sang tình huống khác; vì sao skill kể lại một lần xử lý sự cố thì chưa phải skill. *(M3.2)*
7. **Key đọc từ ENV** — vì sao "xoá key trước khi commit" không cứu được gì khi lịch sử git vẫn giữ; `.gitignore` phải có trước hay sau khi tạo `.env`. *(M3.3)*
8. **Khi nào viết script, khi nào ở lại chatbot** — bốn dấu hiệu nên viết script; hai loại chi phí phải trả khi chuyển sang script. *(M3.3)*
9. **Pipeline vs agent** — khác nhau ở chỗ **ai quyết định bước tiếp theo**; vì sao ở mức capstone ưu tiên pipeline tuần tự. *(M3.4)*
10. **Vì sao pipeline sai khác hẳn người làm sai** — sai một chỗ nhân bản ra cả chuỗi; và vì sao báo cáo do chính AI viết dễ tạo cảm giác an toàn giả. *(M3.4)*

### Tầng 2 — Đào sâu vào bài của học viên

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC — ở cửa này là **đọc thẳng code, SKILL.md và log
pipeline họ viết** — điền chỗ trống bằng nội dung thật, rồi mới hỏi. Câu hỏi không có chỗ
trống đã điền = câu lý thuyết trá hình, không tính là tầng 2. Tầng này chống học thuộc và
chống bài do AI viết — **một câu 0 điểm ở đây là phủ quyết**, trượt bất kể điểm trung bình.

1. *"Tool `<ten-tool>` sinh ra `<trích một selector hoặc một case>` trong output bạn commit. Selector đó bám vào cái gì? Dev đổi `<thứ gì đó trong DOM hoặc trong spec>` thì nó còn chạy không?"*
2. *"Bạn ghi hạn chế `<trích hạn chế 1>`. Kể lại lần bạn gặp nó — bạn đang làm gì, tool trả về gì, và bạn xử lý ra sao? Hạn chế này có làm bạn bỏ tool không?"*
3. *"**Skill bạn viết trigger sai lúc nào?** `description` của nó ghi `<trích nguyên văn description>` — câu này nói KHI NÀO dùng hay đang tóm tắt quy trình? Đọc lại và chỉ cho tôi phần nào là trigger."*
4. *"`Not for …` trong description của bạn trỏ sang `<tên skill kề>`. Cho tôi một yêu cầu nằm đúng ranh giới hai skill — bạn muốn cái nào bật, và description hiện tại có phân được không?"*
5. *"Bạn tạo adapter ở `<đường dẫn adapter>`. Mở ra đọc giúp tôi — nó trỏ về bản gốc hay đang chép lại quy trình? Nếu mai bạn sửa `SKILL.md`, file này có phải sửa theo không?"*
6. *"§ output ở `qe-ai/skill-<ten>-output.md` cho thấy assistant làm `<trích một bước>`. Bước đó có trong quy trình bạn viết không — ở dòng nào? Nếu không, skill thiếu gì?"*
7. *"Trong `qe-ai/tools/<ten-script>.py`, chỗ đọc key là `<trích dòng>`. Nếu tôi chạy script này trên máy chưa đặt biến môi trường thì chuyện gì xảy ra — chỉ đúng dòng xử lý, và nói vì sao dừng sớm ở đó tốt hơn chạy tiếp."*
8. *"Script của bạn bắt `<trích tên exception>`. Còn lỗi loại `<một lỗi khác, ví dụ vượt rate limit hoặc timeout>` thì rơi vào đâu? Người chạy script sẽ thấy gì trên màn hình?"*
9. *"Lượt chạy gần nhất ghi input `<n>` token, output `<m>` token. Chạy `<số lần>` lượt mỗi tuần thì tốn bao nhiêu — bạn tra bảng giá ở đâu, và con số nào làm bạn đổi ý về việc tự động hoá?"*
10. *"Trong `qe-ai/pipeline/`, chặng `<số>` nhận `<trích input>` và trả `<trích output>`. Nếu chặng đó sai thì chặng sau hỏng kiểu gì — và log nào của bạn cho thấy điều đó?"*
11. *"Điểm dừng của bạn đặt sau chặng `<số>`. Vì sao là chỗ đó chứ không phải sau chặng `<số kề>`? Bỏ nó đi thì lớp sai nào lọt thẳng tới báo cáo cuối?"*
12. *"`04-summary.md` viết `<trích một câu kết luận>`. Mở `03-test-run.log` ra đối chiếu — câu đó có đúng với log không, hay AI đã làm đẹp thêm một chút?"*

### Tầng 3 — Tình huống

1. *"Pipeline bạn dựng chạy sai một bước lúc 2 giờ sáng. Bạn phát hiện bằng cách nào — cái gì báo cho bạn, bạn mở file nào trước, và bạn biết được là chặng nào hỏng sau bao lâu?"*
2. *"Chi phí token tháng này gấp 5 lần tháng trước, không ai đổi gì rõ ràng. Bạn khoanh vùng ra sao, và bạn đặt cái gì vào chỗ đó để lần sau biết sớm hơn?"*
3. *"Team dùng skill bạn viết được hai tháng thì bắt đầu bỏ qua nó. Bạn tìm hiểu nguyên nhân bằng cách nào, và bạn sửa skill hay sửa quy trình?"*
4. *"Lead muốn bỏ hết điểm human-in-the-loop cho pipeline chạy tự động qua đêm. Bạn trả lời thế nào, và bạn đề xuất bù bằng cơ chế gì?"*
5. *"Một tool AI bạn đang pilot vừa đổi chính sách dữ liệu: từ nay gửi mã nguồn lên cloud của họ. Bạn làm gì trong ngày hôm nay, và bạn nói gì với người đã duyệt pilot?"*
6. *"Bạn rời dự án trong 2 tuần nữa. Bàn giao thế nào để skill, script và pipeline bạn dựng không thành ba thứ không ai dám đụng?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Kể đủ bốn nhóm AI test tool nhưng hai "hạn chế thực tế" đều là câu chung chung** — "còn đắt", "chưa chính xác lắm" — không gắn với lượt chạy nào trên Toolshop; hỏi "lúc đó tool trả về cái gì" là đứng.
2. **Giải thích được vì sao `description` quan trọng nhất nhưng description trong bài lại tóm tắt quy trình** — biết luật, chưa từng thấy hậu quả của việc vi phạm nó.
3. **Có `SKILL.md` nhưng adapter chép lại nguyên quy trình** — hoặc chỉ có đúng một adapter cho công cụ họ dùng; hỏi "sửa SKILL.md thì file kia có phải sửa theo không" thì lộ ngay là chưa hiểu mô hình bản gốc.
4. **Nói trôi "key đọc từ ENV" nhưng grep lịch sử commit ra key thật ở một commit cũ** — hoặc `.env` được thêm vào `.gitignore` *sau* khi đã commit; đây là điểm 0, không phải chỗ để giải thích.
5. **Script chạy được nhưng không đọc được từng khối của chính mình** — không biết bỏ khối bắt lỗi đi thì người dùng thấy gì, không biết `usage` lấy ở đâu ra; code chép nguyên từ tài liệu hoặc từ AI.
6. **Pipeline có sơ đồ đẹp nhưng `qe-ai/pipeline/` không có log của lượt chạy nào** — hoặc log chỉ có file cuối, không có chặng giữa; sơ đồ là thiết kế, chưa phải thứ đã chạy.
7. **Phân biệt trôi chảy pipeline với agent nhưng không nói được vì sao bài mình chọn cái đã chọn** — hoặc điểm human-in-the-loop đặt ở chặng cuối cùng cho có, không phải sau chặng dễ sai nhất.
8. **Code dùng pattern không có ở đâu khác trong repo**, comment tiếng Anh trong repo tiếng Việt, hoặc cấu trúc script khác hẳn phần còn lại — và không sửa nổi một chi tiết nhỏ khi bị yêu cầu đổi.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `l3 — <YYYY-MM-DD>`. Dòng "Nhánh AI": ghi `hoàn tất Level 3` — nhánh này **hết cửa**, không mở cửa mới |
| 2. Bảng tiêu chí | Không còn cửa kế trong nhánh AI. Lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; chỉ mở bảng mới nếu học viên chạy placement sang nhánh Level 0 |
| 2. Capstone | `đạt` — kèm đường dẫn `qe-ai/pipeline/` và link commit hoặc PR của lượt chạy end-to-end đã chấm |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `l3` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt (ví dụ pipeline mới chạy đúng một input mẫu, hoặc skill chưa ai ngoài họ dùng) — để phiên sau quay lại |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa l3, đạt — hoàn tất nhánh AI |
```

**Cập nhật checklist nguồn** `curriculum/level-3-builder/LEVEL-CHECKLIST.md`: rà lại cột
`Tự đánh giá`, tick đủ 4 tiêu chí đã chấm ≥2. Cột `Reviewer` **để trống** — ô đó dành cho
QE senior / lead / SDET người thật muốn xác nhận thêm; `SKILL.md` và pipeline là hai chỗ
khó tự chấm nhất, khuyến khích học viên xin review người thật đúng hai chỗ đó.

**Không có cửa kế tiếp.** Đây là **cửa cuối** của nhánh AI — nói rõ với học viên họ đang
đứng ở đâu. Nhánh Level 0 (`gd0` → `gd1` → `gd2`) vẫn là nhánh **song song**: đạt `l3`
không tự mở `gd0`; ai muốn bổ nền nghề thì chạy placement riêng cho nhánh đó.

**Nhắc học viên:** họ đã đi hết ranh giới của lộ trình — từ *người dùng* AI thành **người
xây công cụ QE bằng AI**: có skill dùng chung được cho team, có script tự động hoá một
việc lặp lại, có pipeline chạy end-to-end với điểm dừng cho người. Ranh giới phía sau cũng
phải nói thẳng: lộ trình này dừng ở **công cụ QE cho một team**, chưa phải test
infrastructure quy mô lớn, performance, security, hay vận hành nền tảng AI nội bộ — những
thứ đó học khi đã dựng và bảo trì thật vài vòng.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

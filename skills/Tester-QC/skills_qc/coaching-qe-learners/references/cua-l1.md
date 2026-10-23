# Cửa Level 1 — Foundation (nhánh AI)

**Checklist nguồn:** `curriculum/level-1-foundation/LEVEL-CHECKLIST.md`
**Cửa trước:** — (cửa đầu tiên nhánh AI)
**Cửa sau:** `references/cua-l2.md`

Repo bằng chứng của cửa này: **repo / PR của dự án thật học viên đang làm** — không phải
`qa-portfolio`, không phải Toolshop. Capstone của cả Level 1–3 đều là *"áp vào dự án
thật"*, nên bằng chứng phải sống ở nơi công việc thật của họ sống. Mọi đường dẫn dưới đây
tính từ thư mục `qe-ai/` học viên tạo trong repo đó. Repo công ty không cho thêm thư mục
lạ → dùng một repo riêng của học viên và **ghi rõ một chỗ trong hồ sơ**, không đổi qua lại
giữa các phiên.

Tên file dưới đây là **gợi ý của cửa**, không phải quy định của curriculum — và bản thân
thư mục `qe-ai/` cũng là quy ước do cửa đặt ra (khác `qa-portfolio` / `qa-automation` vốn
là quy định của Level 0). Chấp nhận tên khác miễn nội dung § đủ và đường dẫn thật được ghi
vào hồ sơ.

**Hệ quả bắt buộc — ẩn danh TRƯỚC khi đưa vào prompt và TRƯỚC khi commit.** Bài Level 1
lấy nguyên liệu từ công việc thật, nên hầu như bài nào cũng dính dữ liệu công ty: tên
khách hàng, email, số điện thoại, token, log production, tên module chưa công bố. Học viên
phải thay bằng dữ liệu giả **cùng hình dạng** ở cả hai mốc — dán vào prompt là mốc một,
commit vào repo là mốc hai. Đây chính là chỗ tiêu chí **M1.4** chạm tới: bằng chứng M1.4
đòi commit **nguyên văn output gốc của AI**, mà output gốc chép lại đúng phần input đã dán
vào. Thấy dữ liệu thật trong bằng chứng → **không chấm dòng đó**, trả lại yêu cầu ẩn danh
rồi nộp lại; không cho điểm kèm lời nhắc nhở.

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Cả **5** tiêu chí trong bảng dưới đạt **≥2**, mỗi tiêu chí có
đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ sơ. Không bù trừ:
một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

Khác GĐ0–GĐ2, `LEVEL-CHECKLIST.md` của L1 **không có cột `Bắt buộc ✔`** — nghĩa là **mọi
dòng trong bảng đều bắt buộc**, kể cả dòng `Capstone`. Đừng đi tìm dấu ✔ trong file nguồn
rồi kết luận "không dòng nào bắt buộc".

**2. Capstone.** Một tài liệu ngắn `qe-ai/dung-ai-an-toan.md` (10–15 dòng, dài hơn không
phải điểm cộng), đủ:

| # | Phần | Nội dung tối thiểu |
|---|---|---|
| 1 | § "3 việc SẼ giao cho AI" | 3 mục, mỗi mục kèm lý do vì sao an toàn hoặc hiệu quả với **đúng dự án đó** |
| 2 | § "3 việc SẼ KHÔNG giao cho AI" | 3 mục, mỗi mục nêu **rủi ro cụ thể** nếu giao, không phải "vì AI không đáng tin" |
| 3 | Danh sách đối chiếu "AI nói vs Thực tế" | nộp kèm — module M1.1 mục 6 yêu cầu nộp cùng, và đó là bằng chứng của dòng M1.1 |

Thiếu một phần, hoặc có phần nhưng cả 6 mục đều copy sang công ty khác vẫn đúng → **chưa
mở cổng**, nói rõ thiếu gì.

**3. Ràng buộc riêng của L1 — giữ bản gốc của AI, không chỉ nộp bản cuối.**

Cả cửa này đo một việc: học viên có **đối chiếu** output AI với thực tế hay không. Muốn
chấm được việc đó thì phải có hai bản đặt cạnh nhau, không phải một:

| Tiêu chí | Bản gốc phải giữ | Bản sau phải giữ |
|---|---|---|
| `M1.1` | nguyên văn câu AI trả lời khi chưa được cấp context | thứ quan sát được trên app thật |
| `M1.3` | diff assistant đề xuất **trước khi** học viên sửa | commit hoặc PR cuối cùng |
| `M1.4` | output gốc AI sinh, nguyên văn | danh sách đã sửa và đã loại kèm lý do |

Bài chỉ có bản cuối, bản gốc "không lưu lại" → **chưa chấm được**, không phải điểm 1: chưa
có gì để chứng minh học viên từng đối chiếu. Trả lại, yêu cầu làm lại trên một output khác
và lưu bản gốc ngay từ đầu.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| M1.1 | Chỉ ra được việc AI dễ sai trong QE + 1 ví dụ ảo giác cụ thể | `qe-ai/ai-sai-o-dau.md` § "AI nói vs Thực tế" (bảng 3–5 dòng, mỗi dòng có cột *AI nói nguyên văn* và cột *quan sát trên app*) + § "Việc AI dễ sai trong sản phẩm tôi test" (≥2 việc) | ≥1 dòng là **bịa rõ ràng** — field, thông báo lỗi, phương thức thanh toán, hay số bước không tồn tại — chứ không phải "AI nói hơi chung chung"; cột *AI nói* là trích nguyên văn, không phải kể lại; ≥2 việc AI dễ sai gắn với sản phẩm họ đang test; giải thích ảo giác bằng cơ chế **dự đoán từ tiếp theo theo xác suất** và tính non-deterministic, không phải "AI chưa đủ thông minh" | Nói được **cái giá của việc kiểm chứng**: một lượt đối chiếu đầy đủ tốn bao lâu so với tự làm từ đầu, chỗ nào họ **cố ý không kiểm** vì hậu quả sai ở đó rẻ, và ai gánh nếu đoán sai chỗ đó |
| M1.2 | Viết được prompt có cấu trúc (vai trò + context + định dạng) cho 1 việc QE | `qe-ai/prompt-template-<ten-viec>.md` § "Template" (đủ 5 phần role · context · task · format · constraint, có chỗ trống dạng `[...]` để điền mỗi lần dùng) + § "Một lần chạy thật" (input thật **đã ẩn danh** + output nhận về) + § "Tiết kiệm ở khâu nào" | Template có **chỗ trống điền được**, không phải một prompt dán cứng cho một lần dùng; phần Context lấy từ quan sát hệ thống thật (tên trường, ràng buộc nghiệp vụ, thông báo lỗi), không có PII hay secret thật; có ≥1 ví dụ few-shot; output ở § "Một lần chạy thật" bám đúng định dạng mà phần Format đòi — lệch định dạng nghĩa là template chưa được chạy thử | Nói được **đánh đổi khi siết Constraint chặt hơn**: output ngắn và đúng khuôn hơn, nhưng mất luôn những hướng ngoài khuôn mà AI có thể gợi ra; ràng buộc nào họ cố ý để lỏng, và trả bằng bao nhiêu công lọc tay mỗi lần dùng |
| M1.3 | Dùng AI coding assistant + review diff trước khi apply | `qe-ai/dung-coding-assistant.md` § "Prompt đã dùng" + § "Diff gốc assistant đề xuất" (bản trước khi sửa) + § "Tôi đã review gì" (trả lời đúng 3 câu của M1.3 Bước 3: đúng phạm vi file, assertion hợp lý, có lệnh nguy hiểm nào) + § "Kết quả cuối và vì sao" — kèm **link commit hoặc PR thật** của thay đổi đó | Diff gốc được lưu **trước khi sửa**, không phải chỉ bản đã merge; § "Tôi đã review gì" trả lời 3 câu bằng nội dung của **chính diff đó** (nêu tên file bị đụng ngoài ý muốn, dòng assertion đáng ngờ), không phải mô tả quy trình chung; § "Kết quả cuối" nói rõ giữ / sửa / bỏ kèm lý do; commit mang tên học viên, không do assistant tự đẩy | Nói được **đánh đổi khi nới quyền cho assistant**: auto-approve nhóm lệnh nào thì tiết kiệm bao nhiêu lần bấm xác nhận mỗi buổi, đổi lại mất khả năng chặn thao tác nào — và lệnh nào họ **không bao giờ** cho tự chạy trên repo này dù chậm |
| M1.4 | Áp checklist kiểm chứng, loại được ≥1 case AI sai/thừa — **không chỉ ra được case đã loại kèm output gốc thì tối đa điểm 1** | `qe-ai/kiem-chung-output-ai.md` § "Output gốc AI sinh" (nguyên văn, đã ẩn danh) + § "Checklist kiểm chứng" (đủ 5 dòng của M1.4 mục 3, mỗi dòng kèm ghi chú **đã kiểm bằng cách nào**) + § "Đã sửa / Đã loại" (≥1 mục, mỗi mục kèm lý do) | § "Output gốc" là **nguyên văn bản AI trả về**, không phải bản đã dọn kể lại; ≥1 case bị loại trích được **cả câu gốc lẫn lý do loại**, lý do bám vào một quan sát thật (mở app thấy field không tồn tại, đối chiếu đúng câu chữ requirement), không phải "nghe không hợp lý"; 5 dòng checklist đều có ghi chú tái dựng được, không tick suông. **Không có case nào bị loại, hoặc có mà không kèm output gốc để đối chiếu → tối đa 1**, dù phần còn lại viết tốt | Nói được **đánh đổi ở chỗ dừng kiểm chứng**: output nào họ soát từng dòng, output nào chỉ soát mẫu, lớp lỗi nào chấp nhận lọt vì lựa chọn đó — kèm thời gian thật của một lượt soát đầy đủ để con số đứng được |
| Capstone | Tài liệu ngắn: cách tôi sẽ dùng AI an toàn trong dự án (3 việc nên / 3 việc không) | `qe-ai/dung-ai-an-toan.md` § "3 việc SẼ giao cho AI" + § "3 việc SẼ KHÔNG giao cho AI", 10–15 dòng, mỗi mục một dòng lý do | Cả 6 mục nói đúng thứ của **dự án họ đang làm** — tên module, loại dữ liệu, công cụ team dùng — copy sang dự án khác là sai ngay; 3 việc KHÔNG nêu rủi ro cụ thể (dán log có dữ liệu khách hàng, tin hành vi API mà chưa gọi thử, để AI quyết pass/fail một bug chạm tiền) chứ không phải "vì AI hay sai" | Nói được **đánh đổi ở một mục nằm sát ranh giới**: việc nào họ suýt xếp nhầm nhóm, điều kiện gì (có công cụ nội bộ đã duyệt, ẩn danh được hoàn toàn) sẽ khiến họ chuyển nó sang nhóm SẼ, và họ chấp nhận rủi ro nào khi chuyển |

**Lưu ý về M1.4:** capstone module M1.4 cho phép **không loại case nào** nếu giải thích
được vì sao output đúng 100%; dòng checklist level thì ghi thẳng *"loại được ≥1 case AI
sai/thừa"*. Cửa chấm theo **dòng checklist**: không có case bị loại nghĩa là chưa có bằng
chứng nào cho thấy học viên phân biệt được đúng và sai trong output AI — tối đa điểm 1,
trả lại và đổi sang một output khác. Đây là chỗ siết hơn module, nói thẳng lý do cho học
viên chứ đừng để họ tưởng bị chấm oan.

**Lưu ý về Capstone và M1.1:** capstone của level **trùng** với capstone module M1.1 —
một tài liệu, không phải hai bài. Nhưng hai dòng chấm hai thứ khác nhau: **M1.1** chấm
trên *danh sách đối chiếu "AI nói vs Thực tế"*, **Capstone** chấm trên *tài liệu 3 việc
nên / 3 việc không*. Module M1.1 mục 6 yêu cầu nộp cả hai cùng lúc, nên chúng đến cùng
một lần — vẫn ghi **hai điểm riêng** trong hồ sơ, đừng gộp.

**Lưu ý về M1.1 — cửa đổi sân so với module:** hands-on M1.1 chạy trên **Toolshop**, còn
cửa đòi danh sách đối chiếu làm trên **sản phẩm thật học viên đang test**, và Dấu hiệu #1
loại thẳng ví dụ lấy từ Toolshop. Lý do: dòng checklist không giới hạn app, mà cả Level
1–3 đo năng lực **trên việc thật** — ví dụ Toolshop chứng minh học viên đọc tài liệu, không
chứng minh họ nhận ra AI sai ở sản phẩm mình chịu trách nhiệm. Học viên đã làm bản Toolshop
thì không phải bỏ đi: dùng nó làm bản nháp, chuyển sang app thật là đủ. Ô này còn nhập thêm
hai tiêu chí lấy từ **checklist năng lực mục 5 của module** (≥2 việc AI dễ sai gắn với sản
phẩm đang test; giải thích ảo giác bằng cơ chế dự đoán xác suất) — chúng không có trong dòng
checklist level, nhưng là cách duy nhất phân biệt hiểu thật với thuộc lòng ở tiêu chí này.

**Lưu ý về M1.3:** capstone module M1.3 chỉ đòi *diff + ghi chú review*; cửa đòi thêm
**link commit hoặc PR thật mang tên học viên**. Siết vì diff rời không chứng minh được
thay đổi đã thật sự đi vào sản phẩm, mà M1.3 đo chính việc *dùng assistant trong công việc
thật*. Repo công ty không cho chia sẻ link → chấp nhận ảnh chụp trang commit có mã hash và
tên tác giả, ghi rõ trong hồ sơ là bằng chứng thay thế.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

1. **LLM là bộ dự đoán từ tiếp theo, không phải cơ sở dữ liệu tra cứu** — vì sao "giọng tự tin" không phải tín hiệu "đúng"; cùng một prompt hỏi hai lần ra hai kết quả thì đó là lỗi hay là cơ chế. *(M1.1)*
2. **Chất lượng output phụ thuộc context được cấp** — hỏi suông về một hệ thống AI chưa từng thấy thì nó lấp chỗ trống bằng gì; bắt lấy ví dụ trên chính sản phẩm họ test. *(M1.1)*
3. **Ba nhóm việc KHÔNG giao cho AI** — con số/sự kiện chính xác của hệ thống thật, dữ liệu nhạy cảm, quyết định cuối ảnh hưởng release; mỗi nhóm một ví dụ từ dự án của họ. *(M1.1)*
4. **Năm phần của một prompt QE** — role · context · task · format · constraint; bỏ từng phần đi thì output hỏng theo kiểu nào, khác nhau ra sao. *(M1.2)*
5. **Few-shot giải quyết chuyện gì mà mô tả bằng lời không giải quyết được** — một ví dụ mẫu đủ tốt phải mang thông tin gì; vì sao một ví dụ thường đã đổi được định dạng cả bộ output. *(M1.2)*
6. **Dữ liệu nào được dán, dữ liệu nào không** — và cách thay dữ liệu thật bằng dữ liệu giả **cùng hình dạng** để output không lệch. *(M1.2, M1.4)*
7. **Chatbot vs coding assistant tích hợp repo** — khác nhau ở input, output, ngữ cảnh, rủi ro; vì sao "có tay để hành động" làm rủi ro nhảy bậc chứ không tăng dần. *(M1.3)*
8. **Ba việc không bao giờ bỏ qua khi dùng assistant** + phân biệt lệnh an toàn với lệnh nguy hiểm khi cấp quyền chạy; vì sao yêu cầu mơ hồ là nguyên nhân phổ biến nhất của sửa nhầm chỗ. *(M1.3)*
9. **Bốn kỹ thuật kiểm chứng output AI** — chạy thử app thật, đối chiếu requirement, hỏi lại AI phản biện, rà logic thủ công: mỗi kỹ thuật bắt tốt lỗi loại nào và **không** bắt được loại nào; vì sao hỏi lại AI không thay được chạy thử. *(M1.4)*
10. **Ba loại lỗi trong output AI sinh test case** — case bịa, case thừa, case thiếu: phân biệt bằng câu hỏi nào; vì sao case bịa nguy hiểm hơn case thiếu. *(M1.4)*

### Tầng 2 — Đào sâu vào bài của học viên

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC, điền chỗ trống bằng nội dung thật trong bài họ,
rồi mới hỏi. Câu hỏi không có chỗ trống đã điền = câu lý thuyết trá hình, không tính là
tầng 2. Tầng này chống học thuộc và chống bài do AI viết — **một câu 0 điểm ở đây là phủ
quyết**, trượt bất kể điểm trung bình.

1. *"Trong `qe-ai/ai-sai-o-dau.md` bạn ghi AI nói `<trích nguyên văn>` còn thực tế là `<trích cột quan sát>`. Mở sản phẩm ra chỉ cho tôi chỗ bạn đối chiếu. Nếu hôm đó bạn không mở app, case nào trong bài của bạn sẽ sai theo?"*
2. *"Bạn liệt kê `<việc AI dễ sai>` là một điểm yếu của AI trong dự án bạn. Lần gần nhất nó xảy ra là khi nào, và bạn phát hiện ở bước nào — trước hay sau khi đưa vào bài?"*
3. *"Template ở `qe-ai/prompt-template-<ten-viec>.md` có phần Constraint ghi `<trích>`. **Prompt này thiếu ràng buộc gì khiến output lan man?** Chỉ vào đúng đoạn trong § 'Một lần chạy thật' nơi output đi lạc khỏi thứ bạn cần."*
4. *"Phần Context của template có chỗ trống `<tên chỗ trống>`. Lần chạy thật bạn điền gì vào đó — bản đã ẩn danh khác bản gốc ở chỗ nào, và việc thay đó có làm output kém đi không?"*
5. *"Ví dụ few-shot của bạn là `<trích ví dụ>`. Bỏ nó ra rồi chạy lại thì output đổi thế nào? Bạn đã thử chưa, hay đang đoán?"*
6. *"Trong `qe-ai/dung-coding-assistant.md`, diff gốc đụng vào `<tên file>`. Bạn có yêu cầu nó đụng file đó không? Dòng nào trong diff làm bạn dừng lại — chỉ đúng dòng."*
7. *"Bạn ghi kết quả cuối là `<giữ / sửa / bỏ>`. Nói cho tôi assertion `<trích>` trong đề xuất đó kiểm điều gì — nếu sản phẩm hỏng theo kiểu `<một bug cụ thể của module đó>` thì nó có đỏ không?"*
8. *"Trong `qe-ai/kiem-chung-output-ai.md`, output gốc có `<n>` mục, bạn loại `<m>`. Chọn mục `<trích một mục bị loại>` — nó sai ở ràng buộc nào, và bạn phát hiện bằng thao tác gì chứ không phải bằng cảm giác?"*
9. *"Dòng checklist `<trích một dòng>` bạn tick kèm ghi chú `<trích ghi chú>`. Dựng lại giúp tôi đúng thao tác đó — bạn mở cái gì, gõ gì, nhìn vào đâu để kết luận?"*
10. *"Trong `qe-ai/dung-ai-an-toan.md`, mục `<trích một việc trong nhóm SẼ KHÔNG>`. Nếu mai công ty duyệt một công cụ AI nội bộ, mục này có chuyển sang nhóm SẼ không? Cụ thể cái gì đổi thì bạn đổi ý?"*

### Tầng 3 — Tình huống

1. *"AI trả về một requirement không có trong spec — bạn xử lý sao, và bạn nói gì với BA?"*
2. *"PO đưa một story 3 dòng, dev code chiều nay, bạn có 20 phút trước standup. Dùng AI ở bước nào, và bước nào bạn nhất định tự làm — vì sao chia như vậy?"*
3. *"Đồng nghiệp gửi bạn 30 test case do AI sinh và xin duyệt trong hôm nay. Bạn duyệt theo thứ tự nào, và bạn nói gì nếu không kịp soát hết?"*
4. *"Lead bảo 'dán nguyên log production này vào chatbot cho nhanh'. Bạn trả lời thế nào, và đề xuất cách nào thay thế mà vẫn kịp việc?"*
5. *"Assistant vừa sửa 6 file cho một yêu cầu bạn tưởng chỉ đụng 1 file. Bạn làm gì trước, và tới đâu thì bạn quyết định bỏ hết làm lại thay vì gỡ từng chỗ?"*
6. *"Team định cấm dùng AI sau một lần bug lọt vì test case AI bịa. Bạn đồng ý hay phản đối — và bạn đề xuất luật gì thay cho lệnh cấm?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Kể vanh vách "AI hay ảo giác" nhưng không đưa được ví dụ ảo giác nào từ chính công việc mình** — mọi ví dụ đều là ví dụ trong tài liệu (MoMo, Confirm password), không có cái nào mang tên module hay thông báo lỗi của sản phẩm họ test.
2. **Đọc trôi 5 phần của một prompt tốt nhưng prompt trong bài chỉ có mỗi Task** — hoặc phần Context copy nguyên từ M1.2 (Toolshop, form Register) trong khi bài là dự án khác hẳn.
3. **Nói "luôn review diff trước khi apply" nhưng bài chỉ có bản đã merge** — không giữ diff gốc, tức là không còn gì để chứng minh có bước review; hỏi "assistant định sửa file nào ngoài ý bạn" là đứng.
4. **Checklist 5 dòng tick đủ nhưng mọi ghi chú đều là "đã kiểm tra, ổn"** — không dòng nào tái dựng được thành thao tác; đây là tick suông, không phải kiểm chứng.
5. **Danh sách "3 việc KHÔNG giao cho AI" copy sang công ty khác vẫn đúng** — không tên module, không loại dữ liệu, không công cụ team đang dùng; nghe hay nhưng không ràng buộc ai cả.
6. **§ "Output gốc AI sinh" sạch sẽ, đúng khuôn, không mục nào bị loại** — dấu hiệu họ dán bản cuối vào chỗ đáng lẽ là bản gốc; hỏi thẳng bản gốc lưu ở đâu, lúc mấy giờ.
7. **Văn phong bài lệch hẳn cách họ nói trong chat**, thuật ngữ tiếng Anh chen nguyên khối vào bài tiếng Việt — và khi bị yêu cầu đổi một chi tiết nhỏ trong chính bài mình thì không sửa nổi.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `l1 — <YYYY-MM-DD>`. Dòng "Nhánh AI": cửa đang mở đổi thành `l2`, module đang học `M2.1` |
| 2. Bảng tiêu chí | Thay bằng tiêu chí của cửa `l2`. **Không xoá bảng l1** — lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; đường dẫn bằng chứng cũ còn dùng lại khi placement hoặc khi nghi bài giả |
| 2. Capstone | `đạt` — kèm đường dẫn `qe-ai/dung-ai-an-toan.md` và link commit hoặc PR chứa nó |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `l1` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt (ví dụ chỉ loại được đúng 1 case ở M1.4, hoặc template prompt chưa qua vòng lặp cải tiến nào) — để phiên sau quay lại |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa l1, đạt |
```

**Cập nhật checklist nguồn** `curriculum/level-1-foundation/LEVEL-CHECKLIST.md`: rà lại cột
`Tự đánh giá`, tick đủ 5 tiêu chí đã chấm ≥2. Cột `Reviewer` **để trống** — ô đó dành cho
QE senior / lead người thật muốn xác nhận thêm, không bao giờ tự tick.

**Mở cửa kế tiếp:** `l2` — đọc `references/cua-l2.md`, checklist nguồn
`curriculum/level-2-practitioner/LEVEL-CHECKLIST.md`, module đầu tiên
`curriculum/level-2-practitioner/M2.1-phan-tich-requirement-sinh-test-case.md`. Repo bằng
chứng **vẫn là repo dự án thật** — thư mục `qe-ai/` lớn dần qua L2, không tạo repo mới.

**Nhắc học viên:** L1 mới là *dùng AI có kỷ luật*, chưa phải *tạo ra sản phẩm test bằng
AI* — ranh giới đó nằm ở L2. Và nhánh Level 0 (`gd0` → `gd2`) là nhánh **song song**: đạt
`l1` không tự mở `gd0`; muốn mở thì chạy placement riêng cho nhánh đó.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

# Cửa Level 0 · Giai đoạn 0 — Nền tảng kiểm thử

**Checklist nguồn:** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-0.md`
**Cửa trước:** — (cửa đầu tiên)
**Cửa sau:** `references/cua-gd1.md`

Repo bằng chứng của cửa này: **`qa-portfolio`** (public). Mọi đường dẫn dưới đây là đường
dẫn trong repo đó.

## Điều kiện mở cổng phỏng vấn

Đủ **cả ba**, thiếu một là chưa mở — không có ngoại lệ "gần đủ", "học lâu rồi", "cố gắng nhiều".

**1. Tiêu chí bắt buộc.** Cả **16** tiêu chí trong bảng dưới đạt **≥2**, mỗi tiêu chí có
đường dẫn bằng chứng thật **đã được mở ra đọc** + ngày chấm trong hồ sơ. Không bù trừ:
một tiêu chí 1 không gỡ được bằng một tiêu chí 3 ở chỗ khác.

**2. Capstone.** Repo public `qa-portfolio`, README có mục lục, có đủ 5 nhóm file:

| # | File | Nội dung tối thiểu |
|---|---|---|
| 1 | `phan-tich-rui-ro.md` | bản đồ hệ thống + xếp hạng rủi ro có lý do + câu hỏi cho PO |
| 2 | `thiet-ke-test-<tinh-nang>.md` | EP/BVA + decision table + state transition + mục "vì sao tôi cắt những case này" |
| 3 | `test-cases.md` | ≥20 case có ID, ưu tiên, truy vết requirement |
| 4 | `bug-reports.md` | 10 bug thật + mục "bug tôi tâm đắc nhất" |
| 5 | `sql-verification.md` + `khoanh-vung-loi.md` | bằng chứng đọc được hệ thống dưới UI |

Thiếu một file, hoặc file có nhưng rỗng phần cốt lõi → **chưa mở cổng**, nói rõ thiếu file nào.

**3. Ràng buộc riêng của GĐ0 — "tay trước, AI sau"** (nguyên tắc 2 của Level 0).

Bài phải **do học viên tự làm**. Claude ở giai đoạn này chỉ được **giải thích khái niệm**
và **chấm bài** — không viết hộ dưới bất kỳ dạng nào: không bảng EP/BVA mẫu, không test
case mẫu, không câu bug report mẫu, không query SQL sẵn để chép, không "bản rút gọn cho
bạn hình dung", không viết tiếp phần còn thiếu của bản học viên đang làm dở.

Ở GĐ0 luật siết chặt hơn mức chung của skill: ngay cả **ví dụ minh hoạ 1–2 cái** cũng
**không được viết dưới dạng chạy được** (bảng test case, dòng case, query hoàn chỉnh) —
chỉ được **mô tả bằng lời** hình dạng của nó.

Nếu trong quá trình học Claude đã lỡ sản xuất một phần nào của deliverable: **phần đó
không tính là bằng chứng**. Học viên phải làm lại phần đó bằng tay trước khi mở cổng, và
ghi lý do vào Nhật ký hồ sơ.

Cổng chưa mở → nêu **mã tiêu chí** còn thiếu, không mở "linh động".

## Tiêu chí & cách chấm

| Mã | Tiêu chí (rút từ checklist nguồn) | Bằng chứng bắt buộc | Điểm 2 nghĩa là | Điểm 3 nghĩa là |
|---|---|---|---|---|
| S0.1-a | Giải thích được vì sao không thể test hết + hệ quả với cách làm việc | `qa-portfolio/phan-tich-rui-ro.md` § "Nếu chỉ có 1 ngày test app này" (đoạn kết 5 dòng) | Nói được không gian test là vô hạn vì tổ hợp trường × trạng thái × môi trường, và hệ quả trực tiếp là phải xếp thứ tự theo rủi ro; đoạn kết nêu rõ test gì trước, bỏ gì | Nêu được **cái giá của việc bỏ**: vùng nào bị bỏ, rủi ro còn lại là gì ai gánh, và điều kiện nào sẽ khiến họ đảo lại thứ tự ưu tiên đó |
| S0.1-b | Có bản đồ ≥8 màn hình kèm xếp hạng rủi ro **có lý do** | `qa-portfolio/phan-tich-rui-ro.md` § "Bản đồ hệ thống" — bảng ≥8 màn hình, mỗi dòng có cột mức rủi ro + cột lý do | Đủ ≥8 màn, mỗi màn ghi người dùng làm được gì / dữ liệu nào đổi, mức rủi ro kèm lý do một câu bám vào **hệ quả khi hỏng** (mất tiền / mất dữ liệu / lộ quyền), không phải "vì quan trọng" | Giải thích được vì sao màn X xếp cao hơn màn Y khi **cả hai cùng chạm tiền hoặc quyền**, và chấp nhận đánh đổi gì khi dồn thời gian vào X |
| S0.1-c | Tìm được ≥5 điểm mơ hồ trong requirement + câu hỏi cho PO | `qa-portfolio/phan-tich-rui-ro.md` § "Câu hỏi cho PO" — ≥5 mục theo khuôn *chỗ mơ hồ · vì sao nguy hiểm · câu hỏi* | ≥5 điểm mơ hồ thật (thiếu định nghĩa trạng thái lỗi, thiếu quy tắc phân quyền, thiếu hành vi biên…), mỗi câu hỏi PO trả lời được bằng một câu — không phải "làm rõ thêm giúp em" | Xếp được điểm nào **phải hỏi trước khi dev code** và điểm nào chấp nhận vừa làm vừa hỏi, nêu cái giá của việc hoãn hỏi từng nhóm |
| S0.2-a | Áp EP + BVA cho ≥3 trường thật, có phân vùng rỗng & sai kiểu | `qa-portfolio/thiet-ke-test-<tinh-nang>.md` § "EP/BVA" — bảng ≥3 trường, mỗi trường ≥4 phân vùng + ≥4 giá trị biên | Ràng buộc **quan sát từ app thật**, không đoán; mỗi trường đủ ≥4 phân vùng gồm **rỗng** và **sai kiểu**; biên chọn theo quy tắc dưới/đúng/trên và giải thích được vì sao là giá trị đó | Chỉ ra được vì sao chọn **BVA thay vì liệt kê hết giá trị** trong phân vùng, và **cái giá** của lựa chọn đó — lớp bug nào sẽ lọt khi chỉ test rìa; nói được khi nào rút xuống 2 điểm mỗi biên là chấp nhận được |
| S0.2-b | Lập được decision table ≥3 điều kiện và chỉ ra chỗ requirement thiếu | `qa-portfolio/thiet-ke-test-<tinh-nang>.md` § "Decision table" + danh sách "requirement chưa định nghĩa" | Bảng đủ tổ hợp cho ≥3 điều kiện, kết quả mỗi dòng khớp quy tắc nghiệp vụ, và chỉ ra ≥2 chỗ requirement chưa định nghĩa mà chính bảng phơi ra | Nói được **cái giá khi rút gọn bảng** (gộp dòng / dùng *don't care*): độ phủ mất gì, vì sao vẫn chấp nhận được — hoặc ngược lại, vì sao **không** rút gọn dù bảng dài |
| S0.2-c | Liệt kê ≥5 chuyển trạng thái **không hợp lệ** cần chặn | `qa-portfolio/thiet-ke-test-<tinh-nang>.md` § "State transition" — sơ đồ + bảng chuyển tiếp không hợp lệ | Sơ đồ trạng thái + ≥5 chuyển tiếp không hợp lệ, mỗi cái nêu **cách tạo được tình huống đó trên app**, trong đó ≥2 cái chỉ làm được bằng thao tác "bẩn" (Back trình duyệt, 2 tab, gọi thẳng API) | Nói được vì sao **ưu tiên đường cấm hơn phủ hết đường hợp lệ**, và cái giá phải trả — luồng hợp lệ nào bị test mỏng đi vì lựa chọn đó |
| S0.3-a | Bộ ≥20 test case: precondition đủ, kết quả mong đợi đo được, có ưu tiên | `qa-portfolio/test-cases.md` — bảng ≥20 case + § "Kỹ thuật đã dùng" + § "Đã bỏ gì và vì sao" | ≥20 case có ID, ưu tiên, truy vết về requirement; precondition đủ để **chạy độc lập theo bất kỳ thứ tự nào**; kết quả mong đợi trích **đúng chuỗi thông báo thật** của app; ≤30% là P1 | Bảo vệ được mục "Đã bỏ gì và vì sao": case nào đã cắt, **rủi ro còn lại sau khi cắt**, và vì sao 20 case sống đáng hơn 40 case không ai cập nhật (chi phí bảo trì) |
| S0.3-b | Người ngoài chạy được ≥3 case mà không hỏi thêm | `qa-portfolio/test-cases.md` § "Kiểm định chéo" — ai chạy, ID 3 case, chỗ họ phải hỏi lại, bản case đã sửa sau đó | Có ghi chép buổi chạy chéo thật (tên người + ngày), nêu đúng chỗ họ phải hỏi lại hoặc kết luận pass/fail khác, và case đã được sửa theo phát hiện đó | Nói được **đánh đổi giữa precondition chi tiết và case ngắn dễ bảo trì**: chỗ nào cố ý để mở vì viết đủ tốn hơn giá trị nhận lại, và ai sẽ trả giá nếu đoán sai |
| S0.4-a | 10 bug report thật, ≥3 bug không phải lỗi hiển thị | `qa-portfolio/bug-reports.md` — 10 report đủ khung + § "Bug tôi tâm đắc nhất" | Đủ 10 bug thật, ≥3 bug thuộc logic / dữ liệu / phân quyền / luồng; mỗi bug đủ khung (môi trường, precondition, bước, thực tế, mong đợi + căn cứ, bằng chứng, tần suất); tiêu đề theo công thức **nơi + triệu chứng + điều kiện** | Nói được vì sao chọn báo **đúng 10 bug này** mà bỏ những phát hiện khác — cân giữa cái giá của bug nhiễu (làm loãng backlog, mất uy tín) và cái giá của bỏ sót |
| S0.4-b | Bước tái hiện đã rút gọn; người lạ tái hiện được ≥1 bug | `qa-portfolio/bug-reports.md` — mỗi bug ghi **số bước trước/sau rút gọn**; ≥1 bug có ghi chú người lạ tái hiện được (tên + ngày + kết quả) | Mọi bug ghi rõ số bước trước và sau khi rút gọn, chuỗi bước còn lại là tối thiểu và có dữ liệu cụ thể; ≥1 bug có bằng chứng người lạ chạy theo và ra đúng lỗi; ≥1 bug cho thấy việc rút gọn đã **làm lộ điều kiện thật** gây lỗi (kiểu "không phải xoá sản phẩm mà là xoá sản phẩm **cuối cùng**") | Nói được khi nào **dừng** rút gọn vì thời gian bỏ thêm vượt giá trị thông tin thu được — và ai trả giá nếu dừng sớm |
| S0.4-c | Severity & Priority đánh riêng, mỗi cái có lý do | `qa-portfolio/bug-reports.md` — cột Severity và Priority tách rời, mỗi cột kèm một câu lý do; có ≥1 bug hai cột lệch nhau | Hai cột đánh độc lập, lý do Severity bám vào hệ quả kỹ thuật/nghiệp vụ, lý do Priority bám vào bối cảnh (số người ảnh hưởng, lịch release), không để mặc định | Bảo vệ được một ô **"severity thấp / priority cao"** (hoặc ngược lại) trong chính bài mình, nói rõ Priority là quyết định của PO/lead và mình đánh đổi gì khi vẫn đề xuất khác họ |
| S0.5-a | Viết được query JOIN xác minh một thao tác UI | `qa-portfolio/sql-verification.md` — mục có query `JOIN` ≥2 bảng, ghi đủ *thao tác UI · query · kết quả · kết luận* | Query chạy được trên DB thật, gắn với một thao tác UI cụ thể, kết luận bám vào số liệu trả về chứ không vào cảm giác | Nêu được **2 cách kết quả query này có thể đánh lừa** (NULL, dữ liệu cũ, đơn vị tiền, `JOIN` vs `LEFT JOIN`) và vì sao vẫn chấp nhận query này thay vì bản chặt chẽ hơn nhưng tốn công |
| S0.5-b | Phát hiện ≥1 vấn đề dữ liệu bằng SQL (trùng / mồ côi / lệch tổng) | `qa-portfolio/sql-verification.md` — mục nêu vấn đề dữ liệu tìm được, kèm query + kết quả + kết luận | ≥1 vấn đề thật thuộc nhóm trùng / mồ côi / lệch tổng, có query và số dòng trả về, và giải thích được vì sao đó là **vấn đề** chứ không phải dữ liệu test rác | Nói được vì sao chọn kiểm bằng **SQL thay vì qua UI**, và cái giá của lối kiểm này — thấy dữ liệu sai nhưng chưa chứng minh được người dùng gặp phải, nên phải làm thêm gì |
| S0.5-c | Đưa sản phẩm lên GitHub qua branch + Pull Request | Link **PR đã merge** trong repo `qa-portfolio` (ví dụ `https://github.com/<user>/qa-portfolio/pull/1`) + `qa-portfolio/README.md` có mục lục | Repo public, có ≥1 PR tạo từ branch riêng và đã merge (không commit thẳng `main`), README giới thiệu repo, và học viên đọc được diff của chính PR đó | Nói được vì sao vẫn dùng **branch + PR cho repo một mình làm**: được gì (đọc lại diff, lịch sử sạch), mất gì (thao tác thêm), và khi nào bỏ PR là hợp lý |
| S0.5-d | Khoanh được FE/BE theo quy trình 4 bước, có bằng chứng | `qa-portfolio/khoanh-vung-loi.md` — 3 bug, mỗi bug có bằng chứng Network (request/response hoặc cURL) + query SQL + kết luận FE/BE | Cả 3 bug đi đủ 4 bước (có request không → status code → so response với màn hình), kết luận FE hay BE **dựa trên bằng chứng đính kèm**, không dựa cảm giác | Chỉ ra được trường hợp bằng chứng **chưa đủ để kết luận** và mình dừng ở "chưa xác định", nêu cái giá của việc đoán bừa FE/BE trong bug report — dev đi sai hướng vì tin mình |
| AI | Chỉ ra được ≥1 lần AI bịa/sai trong bài của mình và cách mình phát hiện | `qa-portfolio/test-cases.md` § "AI hỗ trợ ở đâu" (prompt đã dùng, số case AI sinh, số bị loại, lý do loại) — hoặc `qa-portfolio/thiet-ke-test-<tinh-nang>.md` § "AI bịa gì trong bài này" | Chỉ ra ≥1 chỗ AI bịa/sai **cụ thể trong chính bài mình** (chuỗi thông báo không có thật, ràng buộc AI tự đoán, case trùng phân vùng), kèm cách phát hiện (đối chiếu app thật / đối chiếu ràng buộc đã cung cấp) và con số sinh / loại | Nói được **đánh đổi khi dùng AI ở đúng công đoạn đó**: tiết kiệm được gì, phải trả bằng bao nhiêu công kiểm chứng, và chỗ nào họ quyết định **không** dùng AI vì kiểm chứng đắt hơn tự làm |

**Lưu ý về S0.1-b:** capstone module `S0.1` chỉ đòi 5 luồng trên app tự chọn; checklist
giai đoạn đòi **≥8 màn hình** — bản nộp cho cửa phải gộp về một file `phan-tich-rui-ro.md`
và mở rộng lên ≥8 màn (Toolshop hoặc app tự chọn, miễn nhất quán trong file).

> **Tiêu chí không bắt buộc:** checklist nguồn còn một dòng S0.2 *"Giải thích được pairwise
> bằng ví dụ có con số"* **không** có dấu ✔. Không dùng nó làm điều kiện mở cổng và không
> đưa vào bảng trên. Vẫn hỏi được trong phỏng vấn (tầng 1) để phân loại điểm 3 — nhưng câu
> đó **không tính vào Điểm TB** của buổi thi và không ghi thành điểm trong hồ sơ; trả lời
> kém ở đó chỉ chặn điểm 3, không bao giờ đánh trượt.

## Chủ đề phỏng vấn KÍN

> Không dán nguyên văn phần này cho học viên. Sinh câu hỏi tại chỗ từ chủ đề + từ bằng chứng học viên đã nộp.

Buổi thi thật: 8–12 câu, **≥3 câu tầng 2**, lấy từ **≥2 bằng chứng khác nhau**. Không phản
hồi đúng/sai cho tới hết buổi.

### Tầng 1 — Nền tảng

1. **Mục tiêu của test là cung cấp thông tin** — vì sao một ngày không tìm ra bug nào vẫn có thể là ngày làm việc tốt; thông tin đó phục vụ ai ra quyết định gì. *(S0.1)*
2. **Test level vs test type** — hai trục cắt nhau; bắt lấy ví dụ trên chính app họ test, cấm đọc lại định nghĩa. *(S0.1)*
3. **Acceptance criteria đo được** — cho một AC mơ hồ, bắt viết lại thành dạng đo được; phản xạ với tính từ mơ hồ (*nhanh, phù hợp, hợp lý, đầy đủ*). *(S0.1)*
4. **EP vs BVA** — mỗi kỹ thuật giải quyết vấn đề gì khác nhau; vì sao lại là 3 điểm mỗi biên chứ không phải 1; hai phân vùng người mới hay quên. *(S0.2)*
5. **Chọn kỹ thuật theo tình huống** — đưa 3 tình huống (ô nhập có khoảng giá trị / nhiều điều kiện đan nhau / đối tượng có vòng đời), bắt chọn kỹ thuật và nói lý do. Kèm pairwise giải quyết vấn đề gì, bằng ví dụ có con số *(chủ đề này không bắt buộc — chỉ dùng để phân loại điểm 3; câu này không tính vào Điểm TB)*. *(S0.2)*
6. **Kết quả mong đợi đo được & một case kiểm một điều** — vì sao "hiển thị thông báo phù hợp" là case không bao giờ fail; case gộp che mất cái gì; ngoại lệ end-to-end hợp lệ khi nào. *(S0.3)*
7. **Precondition & tính độc lập của case; độ ưu tiên P1/P2/P3** — vì sao case phụ thuộc thứ tự là bom hẹn giờ; vì sao >30% P1 nghĩa là chưa xếp hạng. *(S0.3)*
8. **Severity vs Priority** — ai quyết cái nào; bắt tự dựng một ví dụ cho ô "severity thấp / priority cao" và một ví dụ cho ô ngược lại. *(S0.4)*
9. **Bằng chứng theo tầng lỗi & xử lý "không tái hiện được"** — nghi lỗi dữ liệu/API thì đính gì, nghi lỗi server thì đính gì; dev nói không tái hiện được thì làm gì theo thứ tự nào. *(S0.4)*
10. **Ba câu hỏi tester dùng SQL để trả lời** — dữ liệu có thật sự được ghi không, có bản ghi thừa/trùng không, dữ liệu liên quan có nhất quán không; `JOIN` vs `LEFT JOIN` khi đi tìm bản ghi mồ côi. *(S0.5)*
11. **Git ở mức làm việc** — branch / commit / PR / diff / merge conflict; vì sao **tester** cần đọc diff của một PR (suy ra vùng cần regression). *(S0.5)*
12. **DevTools & quy trình 4 bước khoanh FE/BE** — không có request nào bay đi thì kết luận gì; `200` mà UI vẫn sai thì phân biệt FE/BE bằng cách nào; token còn dùng được sau logout nghĩa là gì. *(S0.5)*

### Tầng 2 — Đào sâu vào bài của học viên

**Cách dùng:** mở bằng chứng ra đọc TRƯỚC, điền chỗ trống bằng nội dung thật trong bài họ,
rồi mới hỏi. Câu hỏi không có chỗ trống đã điền = câu lý thuyết trá hình, không tính là
tầng 2. Tầng này chống học thuộc và chống bài do AI viết — **một câu 0 điểm ở đây là phủ
quyết**, trượt bất kể điểm trung bình.

1. *"Trong `qa-portfolio/phan-tich-rui-ro.md` bạn xếp `<màn hình A>` mức Cao còn `<màn hình B>` mức Trung bình. Cả hai đều chạm `<tiền / dữ liệu người dùng>` — vì sao lệch mức? Nếu chỉ test được một, bạn bỏ cái nào và mất gì?"*
2. *"Trong `qa-portfolio/thiet-ke-test-<tinh-nang>.md`, trường `<tên trường>` bạn chọn biên `<giá trị>`. Vì sao là giá trị đó mà không phải `<giá trị kề>`? Bỏ nó đi thì lớp bug nào lọt?"*
3. *"Bảng của bạn có phân vùng `<tên phân vùng>` với đại diện `<giá trị>`. Cho tôi hai giá trị khác cũng thuộc phân vùng đó — và vì sao ở app này test một cái là đủ?"*
4. *"Decision table của bạn, dòng `<số>`, cho kết quả `<kết quả>`. Requirement chỗ nào nói vậy? Nếu spec không nói, câu hỏi nào cho PO bạn đã ghi lại?"*
5. *"Bạn liệt kê chuyển trạng thái không hợp lệ `<trích>`. Trên app, bạn tạo được tình huống đó bằng thao tác nào? Nếu app chặn ở UI thì bạn còn cách nào thử tiếp không?"*
6. *"Trong `qa-portfolio/test-cases.md`, case `<ID>` có precondition `<trích>`. Nếu tôi chạy case này ngay sau case `<ID khác>` thì kết quả có đổi không? Vì sao?"*
7. *"Kết quả mong đợi của case `<ID>` ghi nguyên văn `<trích chuỗi>`. Bạn lấy chuỗi này từ đâu — mở app ra chỉ cho tôi chỗ nó hiện."*
8. *"Case `<ID>` bạn để P1, case `<ID khác>` để P2. Đổi chỗ hai cái này thì hỏng gì? Đếm giúp tôi bộ này có bao nhiêu phần trăm P1."*
9. *"Mục 'Đã bỏ gì và vì sao' nói bạn cắt `<nhóm case>`. Rủi ro còn lại sau khi cắt là gì, và điều gì xảy ra sẽ khiến bạn thêm chúng lại?"*
10. *"Trong `qa-portfolio/bug-reports.md`, bug `<ID / tiêu đề>` bạn ghi rút gọn từ `<n>` xuống `<m>` bước. Bước nào bỏ mà lỗi vẫn còn, bỏ bước nào thì lỗi biến mất? Vậy điều kiện thật gây lỗi là gì?"*
11. *"Bug `<ID>` bạn ghi Severity `<mức>` và Priority `<mức>` — hai cột lệch nhau. Bảo vệ giúp tôi từng cột. Nếu lead hạ Priority xuống, bạn nói gì?"*
12. *"Trong `qa-portfolio/sql-verification.md`, query mục `<số>` dùng `<JOIN / LEFT JOIN>`. Đổi sang loại kia thì kết quả khác thế nào — kết luận `<trích kết luận>` của bạn còn đúng không?"*
13. *"Query mục `<số>` trả về `<n>` dòng và bạn kết luận `<trích>`. Kết quả này có thể đánh lừa bạn bằng cách nào?"*
14. *"Trong `qa-portfolio/khoanh-vung-loi.md`, bug `<số>` bạn kết luận lỗi `<FE / BE>`. Chỉ cho tôi **dòng bằng chứng nào loại trừ phía còn lại** — không phải dòng nào ủng hộ kết luận của bạn."*
15. *"Mục 'AI hỗ trợ ở đâu' ghi AI sinh `<n>` case, bạn loại `<m>`. Chọn một case bị loại và nói nó sai ở ràng buộc nào — bạn phát hiện bằng cách nào?"*
16. *"PR `<số>` trong repo `qa-portfolio` của bạn sửa `<file>`. Đọc diff đó và nói cho tôi thay đổi ấy ảnh hưởng tới case nào của bạn."*

### Tầng 3 — Tình huống

1. *"Sáng mai release, bạn có 3 tiếng và một build vừa sửa module thanh toán. Test gì trước, bỏ gì, và báo cáo gì cho người quyết release?"*
2. *"PO đưa một story dài 4 dòng, dev bắt đầu code chiều nay. Bạn có 30 phút trước buổi refinement — làm gì trước?"*
3. *"Bạn có 1 ngày cho một app hoàn toàn lạ, không spec, không ai bàn giao. Giờ đầu tiên làm gì, và cuối ngày bạn giao được cái gì?"*
4. *"Dev trả bug của bạn kèm 'không tái hiện được', sprint còn 1 ngày. Bạn làm gì, theo thứ tự nào, và đến mức nào thì dừng?"*
5. *"UI báo 'Đặt hàng thành công' nhưng khách nói không thấy đơn. Bạn có quyền vào DB và DevTools, 1 tiếng — khoanh vùng thế nào và dừng ở đâu để không đoán bừa?"*
6. *"Được giao 2 tuần viết test case cho 6 màn hình, nhưng 2 màn còn đang đổi thiết kế hằng ngày. Chia thời gian ra sao, và 2 màn đó bạn xử lý kiểu gì?"*
7. *"AI sinh cho bạn 40 test case trong 2 phút, deadline nộp là chiều nay. Bạn làm gì với 40 case đó trước khi nộp, và nếu không kịp làm hết thì cắt bước nào?"*

## Dấu hiệu trả lời thuộc lòng

Thấy các dấu hiệu này thì **hỏi tiếp vào chính bài học viên**, đừng cho qua. Không giải
thích nổi lựa chọn trong bài mình → **điểm 0**, ghi lý do vào hồ sơ.

1. **Đọc trôi định nghĩa EP/BVA nhưng không chỉ được ranh giới trong chính bài mình** — phải mở file dò lại, hoặc chỉ vào một giá trị giữa phân vùng và gọi đó là biên.
2. **Thuộc câu "Severity là mức nghiêm trọng, Priority là mức ưu tiên sửa" rồi tắc khi phải bảo vệ một bug cụ thể** — hoặc trong `bug-reports.md` không có bug nào hai cột lệch nhau, tức là chưa bao giờ thật sự đánh riêng.
3. **Kết quả mong đợi trong test case là chuỗi thông báo trơn tru nhưng mở app ra không khớp / không tồn tại** — đây là dấu AI viết hộ chứ không phải quên đối chiếu; hỏi ngay chuỗi đó lấy ở đâu.
4. **Nói trôi quy trình 4 bước khoanh FE/BE nhưng `khoanh-vung-loi.md` không có request/response nào** — kết luận FE/BE đứng một mình, không có gì loại trừ phía còn lại.
5. **Lý do xếp rủi ro là nhãn chứ không phải hệ quả** — "vì màn hình này quan trọng", "vì người dùng hay dùng"; hỏi "hỏng thì mất gì" là đứng.
6. **Giải thích được vì sao phải rút gọn bước tái hiện nhưng report vẫn ghi 15 bước, không có số trước/sau** — biết lý thuyết, chưa từng ngồi rút gọn.
7. **Query trong `sql-verification.md` chạy được nhưng không đọc được từng mệnh đề khi bị hỏi**, hoặc không biết đổi `JOIN` sang `LEFT JOIN` thì kết quả đổi ra sao — query chép nguyên từ AI.
8. **Văn phong bài lệch hẳn so với cách họ nói trong chat**, thuật ngữ tiếng Anh chen vào bài tiếng Việt, hoặc ≥20 case đánh số đều tăm tắp nhưng cộng lại chỉ phủ 3 phân vùng.

## Sau khi đạt cửa

**Ghi hồ sơ** `curriculum/tien-do/<ten-hoc-vien>.md` (khuôn: `curriculum/tien-do/TEMPLATE.md`),
ngày dạng `YYYY-MM-DD`:

| Mục trong hồ sơ | Ghi gì |
|---|---|
| 1. Trạng thái hiện tại | **Cửa đã đạt:** thêm `gd0 — <YYYY-MM-DD>`. Dòng "Nhánh nghề (Level 0)": cửa đang mở đổi thành `gd1`, module đang học `S1.1` |
| 2. Bảng tiêu chí | Thay bằng tiêu chí của cửa `gd1`. **Không xoá bảng gd0** — lưu trữ bảng cũ theo quy ước ở `references/ho-so-tien-do.md`; các đường dẫn bằng chứng cũ còn dùng lại khi placement hoặc khi nghi bài giả |
| 2. Capstone | `đạt` — kèm link repo `qa-portfolio` |
| 3. Lịch sử phỏng vấn | Thêm một dòng: ngày · cửa `gd0` · loại `thi` · Điểm TB · cột "Tầng 2 có câu 0?" = `không` · Kết quả `đạt` |
| 4. Chỗ yếu cần ôn | Ghi chủ đề còn mỏng dù đã đạt (ví dụ pairwise chưa làm, hoặc tiêu chí chỉ vừa đạt 2) — để phiên sau quay lại |
| 5. Nhật ký | Thêm một dòng vào bảng — khuôn ở ngay dưới bảng này |

Dòng thêm vào mục 5 Nhật ký (bảng 2 cột `Ngày` / `Việc đã làm`):

```
| <YYYY-MM-DD> | thi cửa gd0, đạt |
```

**Cập nhật checklist nguồn** `curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-0.md`: rà
lại cột `Tự đánh giá`, tick đủ 16 tiêu chí đã chấm ≥2. Cột `Reviewer` **để trống** — ô đó
dành cho QE/QC người thật muốn xác nhận thêm, không bao giờ tự tick.

**Mở cửa kế tiếp:** `gd1` — đọc `references/cua-gd1.md`, checklist nguồn
`curriculum/level-0-sinh-vien/CHECKLIST-GIAI-DOAN-1.md`, module đầu tiên
`curriculum/level-0-sinh-vien/S1.1-api-testing.md`. Repo bằng chứng **vẫn là
`qa-portfolio`** — nó lớn dần qua GĐ1, không tạo repo mới.

**Nhắc học viên:** GĐ1 là mốc 🎯 đủ điều kiện nộp CV fresher, không phải GĐ0. Và nhánh AI
(`l1`) là nhánh **song song** — đạt `gd0` không tự mở `l1`; muốn mở thì chạy placement
riêng cho nhánh đó.

**Trượt thì không ghi gì vào mục 1.** Ghi chủ đề yếu vào mục 4, quay về bước giao việc ở
đúng module đó. **Phải nộp bài khắc phục rồi mới được thi lại** — không cho thi lại ngay
để đoán mò.

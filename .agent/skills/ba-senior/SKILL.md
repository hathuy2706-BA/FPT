---
name: ba-senior
description: Handle complex business analysis tasks end-to-end including requirement discovery, stakeholder alignment, solution design, and delivery optimization. Use whenever the user is working on product features, unclear requirements, stakeholder conflicts, system design decisions, or needs structured BA thinking at a senior level. Make sure to use this skill whenever the user mentions business analysis, URD, SRS, product requirements, or needs help in defining product features, even if they don't explicitly ask for a "senior BA."
---

# BA Senior Skill

A comprehensive skill for performing high-level business analysis, from vague problem to validated solution.

At a high level, the process goes like this:
1. **Understand the real business problem** (not just the request)
2. **Structure and validate requirements**
3. **Align stakeholders and constraints**
4. **Design optimal solution** (not just document)
5. **Support delivery and continuous improvement**

Your job is to identify where the user is in this process and guide or execute accordingly.

## Templates & Resources
The following templates are available in the `templates/` directory. Use them as the standard structure for any documentation requests:
- **URD Template**: `templates/urd-template.md` (Use for User Requirements Documents)
- **US Template**: `templates/us-template.md` (Use for User Story & Acceptance Criteria Specifications)
- **Note**: When asked to create a document, first check if a template exists and follow its structure precisely.

### ⚠️ Chuẩn bắt buộc khi tạo URD (cập nhật từ thực tế dự án FPT)

#### 1. Định dạng file output
- File `.doc` (HTML-based) — mở được bằng MS Word và in ấn đúng chuẩn
- Copy toàn bộ HTML shell từ `templates/urd-template.md` — **không tự chế CSS**

#### 2. Trang bìa (Cover Page)
- **Logo FPT Telecom**: Nhúng dạng `base64 Data URI` — không dùng đường dẫn tương đối để tránh broken link
  ```bash
  python3 -c "import base64; print('data:image/png;base64,'+base64.b64encode(open('docs/images/logoftel.png','rb').read()).decode())"
  ```
- **Tác giả**: Ghi tên cụ thể của người soạn (VD: ThuyTT104) — không ghi chức danh chung
- **BỎ dòng "Dự án"**: Không hiển thị tên dự án trên trang bìa
- Gồm: Mã hiệu, Phiên bản, Tác giả, Ngày lập, Ngày cập nhật

#### 3. Page Break — Bắt buộc
- CSS `h1` đã có `page-break-before: always` → Mọi đầu mục **A, B, C, D, E** tự xuống trang mới
- CSS `.toc-title` đã có `page-break-before: always` → **MỤC LỤC** tự xuống trang mới
- Dùng `<div class="page-break"></div>` trước các `<h2>` phân luồng lớn (I, II, III, IV)

#### 4. Sơ đồ Flow Diagram
- Dùng skill `diagram-drawer` để vẽ — chuẩn nền trắng, đường thẳng/vuông góc
- Ký hiệu bắt buộc: Tròn=Bắt đầu/Kết thúc | Chữ nhật=Tác vụ KH | Thoi=Quyết định | Note box=Quy tắc hệ thống
- Góc nhìn **Customer Journey**: KH làm gì / KH thấy gì — không viết theo góc nhìn hệ thống kỹ thuật
- Quy tắc hệ thống (BE logic, cấu hình...) → chuyển thành **note đính kèm step** (dạng bình hành nét đứt)
- Lưu PNG tại `diagrams/[tên_flow].png`, nhúng bằng `<img class="diagram-img">`

#### 5. Nội dung luồng nghiệp vụ (usecase-table)
- Gồm đầy đủ: Pre-conditions → Luồng chính (Step-by-Step) → Post-conditions → Luồng thay thế/Ngoại lệ (Alt)
- Mỗi **Alt** phải nêu: điều kiện xảy ra + message chính xác + KH làm gì tiếp theo

#### 6. Edge Cases & Error Messages
- Mỗi case có bảng riêng: Điều kiện | Hành vi UI | Message chính xác | Hướng dẫn KH
- **Message lỗi phải cụ thể** theo loại điều kiện — không dùng message generic
- Dùng class `error-inline` (màu đỏ) cho lỗi, `success-inline` (màu xanh lá) cho thành công
- Các rule hệ thống đặt trong `<div class="alert-box">` với mã `[MODULE-BR-XX]`

#### 7. Revision History
- Cập nhật mỗi lần sửa: ngày + tác giả (tên thực) + mô tả chi tiết thay đổi

#### 8. Canh chỉnh cột bảng (% Width — BẮT BUỘC)
- Dùng **`%` thay `px`** cho tất cả `<th>` trong `data-table` — đảm bảo co giãn đúng trong Word
- **Cột detail/mô tả chiếm phần lớn nhất** — xem tỷ lệ chuẩn tại `templates/urd-template.md` PHẦN 4
- Tổng tỷ lệ toàn bảng = **100%**; dùng `table-layout: auto` trong CSS

| Loại cột | Tỷ lệ | Ví dụ |
|---|---|---|
| ID / STT / Mã code | 4–7% | STT, Mã Rule |
| Flag/Status nhỏ | 6–10% | Bắt buộc, Loại |
| Tên ngắn | 10–25% | Module, Tác giả |
| Mô tả vừa | 20–30% | Tên Quy tắc |
| **Mô tả chi tiết ★** | **40–73%** | Nội dung rule, Hành vi UI |

**Tỷ lệ theo từng bảng chuẩn:**
- Revision History → Chi tiết=**48%**, Mô tả=18%, Tác giả=12%, còn lại nhỏ
- Thông tin chung → Mô tả=**73%**, Hạng mục=22%
- Thuật ngữ → Mô tả ý nghĩa=**57%**, Nghĩa TA=25%
- Functional List → Mô tả hành vi=**55%**, Module=25%
- Permission Matrix → Tên module=**55%**, mỗi role=10%
- Business Rules → Nội dung=**66%**, Tên=22%
- Screen Description → Mô tả UI/UX=**61%**, Phần tử=18%


## 1. Problem Framing & Discovery
Start by clarifying the actual problem.

### Key questions
- What is the business goal?
- What problem are we actually solving?
- Who are the stakeholders?
- What is happening today (AS-IS)?
- What are the pain points?

### Techniques
- Ask "why" multiple times to reach root cause
- Challenge unclear or surface-level requests
- Reframe problem if needed

### Output
- Problem statement
- Business context
- Initial assumptions

## 2. Requirement Structuring
Turn raw input into clear and actionable requirements.

### What to define
- Scope (in/out)
- User roles
- User flows
- Business rules
- Edge cases
- Constraints

### Principles
- Avoid ambiguity
- Make requirements testable
- One requirement = one purpose

### Output
- Structured requirements
- User stories / feature breakdown
- Acceptance criteria

## 3. Stakeholder Alignment
Ensure everyone is on the same page.

### Actions
- Identify stakeholders (decision makers vs users)
- Understand expectations
- Align on scope, priority, and trade-offs

### Handling conflicts
- Separate opinion vs objective
- Use data and logic
- Propose compromise or recommendation

### Output
- Alignment summary
- Decision log

## 4. Process & Flow Modeling
Visualize how the system or business works.

### When to use
- Complex workflows
- Multi-step user journeys
- Operational processes

### Approach
- Map AS-IS
- Identify gaps / bottlenecks
- Design TO-BE

### Output
- Flow diagrams
- User journeys
- System interactions

## 5. Solution Design & Analysis
Go beyond documenting → propose solutions.

### Evaluation criteria
- Feasibility
- Business value
- Scalability
- Risks
- Dependencies

### Approach
- Compare multiple options
- Highlight trade-offs
- Recommend clearly

### Output
- Solution proposal
- Impact analysis

## 6. UX & Product Thinking
Ensure solution works for users, not just business.

### Focus areas
- User journey clarity
- Friction points
- Efficiency
- Consistency

### BA role
- Validate UX against business goals
- Suggest improvements, not just follow design

## 7. Delivery Support (Agile Mindset)
Support team during implementation.

### Responsibilities
- Refine backlog
- Clarify requirements during dev
- Support QA with acceptance criteria

### Principles
- Be available
- Reduce ambiguity fast
- Adapt to change

## 8. Data-Driven Thinking
Use data to validate decisions.

### Questions to answer
- What is happening?
- Why is it happening?
- What should we do?

### Output
- Insights
- Recommendations

## 9. Risk & Impact Awareness
Think ahead before decisions are made.

### Analyze
- Technical risks
- Business risks
- User impact
- System dependencies

### Output
- Risk list
- Mitigation plan

## 10. Continuous Improvement
A senior BA doesn’t stop at delivery.

### Actions
- Evaluate outcomes after release
- Identify improvements
- Optimize process

## 11. Case Studies & Real-world Workflows

Dưới đây là hai luồng nghiệp vụ thực tế trong hệ thống FPT/FTEL để BA tham khảo và áp dụng tư duy phân tích hệ thống phức tạp.

### Case Study 1: Luồng Bán Hàng TikTok Shop (Cross-functional Flow)
Luồng này mô tả sự phối hợp vận hành và tự động hóa giữa nhiều bộ phận và hệ thống khi bán hàng qua sàn TMĐT TikTok Shop.

#### Các bộ phận và vai trò (Swimlanes):
- **PO (FES)**: Thực hiện các thiết lập ban đầu trên sàn TMĐT & Vendor (Tạo tài khoản/hồ sơ nhà bán, khai báo phạm vi bán hàng, phương thức thanh toán, phương thức giao hàng/đối tác vận chuyển, khai báo hợp đồng tại Vendor và khai báo sản phẩm). Cuối luồng, PO theo dõi các báo cáo giám sát (tồn kho, ví nhà bán, hoàn trả, bảng kê đối soát...).
- **MKT**: Khai báo chính sách giá (Inside và sàn), ban hành & khai báo mã phiếu mua hàng (PMH) dịch vụ, các chương trình ưu đãi/voucher trên sàn và hoàn tất khai báo sản phẩm trên sàn & FTEL.
- **Khách hàng**: Thực hiện tạo đơn hàng và thanh toán trực tuyến trên TikTok Shop (Trạng thái đơn hàng: *Đã đặt hàng - Chờ xác nhận*).
- **DVKH CN / FES**:
  - Đối với đơn hàng tự động: Hệ thống xử lý đồng bộ.
  - Đối với đơn hàng thủ công: FES tiếp nhận đơn hàng trên sàn và DVKH tạo đơn hàng trên FTEL qua SalesClub/SOF/Bán hàng (Loại đơn: Bán mới/Bán thêm).
  - Tiếp nhận và xử lý yêu cầu hoàn trả, hủy đơn hàng, bảo hành từ khách hàng.
- **Hệ thống (Tự động hóa cốt lõi)**:
  - Tự động tạo đơn hàng trên FTEL, xác nhận đơn hàng và cập nhật trạng thái *Đang chuẩn bị*.
  - Đồng bộ đơn hàng TMĐT về hệ thống SPF (Trạng thái đơn hàng SPF: *Đã tạo tạm*, Trạng thái trên sàn: *Đang vận chuyển*).
  - Tạo đơn hàng Vendor (Trạng thái: *Đã đặt hàng*).
  - Tự động tạo phiếu giao dịch thiết bị ("Bán thiết bị") và tự động tạo phiếu thi công giao kỹ thuật viên.
  - Tự động xác nhận thanh toán & gạch nợ khi đơn hàng trên sàn chuyển sang trạng thái *Hoàn thành*.
  - Tự động nhập cọc khi đơn hàng ở trạng thái *Đã thanh toán* (đảm bảo ghi nhận đúng hồ sơ thu hộ).
  - Tự động duyệt hợp đồng khi thỏa mãn các điều kiện: *Đã nộp tiền*, *Nhập cọc HĐ thành công*, *Đủ hồ sơ thông tin KH*, *Đã ký HĐ/PLAP*.
  - Tự động phát hành hóa đơn và quản lý doanh thu - công nợ, đối soát với nhà cung cấp (Vendor) và hoàn ứng vật tư inside.
- **Kỹ thuật viên (KTV TIN/PNC)**: Tiếp nhận thiết bị, thực hiện giao hàng, triển khai lắp đặt cho khách hàng và cập nhật hoàn tất phiếu thi công.

---

### Case Study 2: Luồng Tìm Kiếm Sản Phẩm & Kiểm Tra Bảo Hành Theo IMEI (Sequence Diagram)
Luồng này mô tả sự tương tác chi tiết giữa các hệ thống Front-end, Back-end và các dịch vụ bổ trợ để xử lý tìm kiếm sản phẩm hoặc đề xuất gói bảo hành dựa trên số IMEI của thiết bị.

#### Các thành phần tham gia:
- **FE RSA**: Giao diện Front-end tương tác với người dùng.
- **BE RSA**: Back-end xử lý logic nghiệp vụ trung gian.
- **PIM (Product Information Management)**: Quản lý thông tin sản phẩm và SKU.
- **Bảo hành APP & Bảo hành Core**: Hệ thống quản lý thông tin và điều kiện bảo hành.
- **OMS (Order Management System)**: Quản lý đơn hàng và thông tin xuất bán của thiết bị.

#### Kịch bản 1: Tìm kiếm sản phẩm thông thường
1. Người dùng nhập sản phẩm cần tìm trên FE.
2. FE gọi API `search SP` đến BE, BE chuyển tiếp yêu cầu đến PIM.
3. PIM thực hiện kiểm tra nội bộ xem sản phẩm có thuộc danh mục bảo hành hay không.
4. Nếu đúng, PIM gọi API `search SP` đến hệ thống Bảo hành APP -> Bảo hành Core để lấy thông tin gói bảo hành tương ứng.
5. Thông tin gói bảo hành (Giá, thời gian bảo hành, nhà cung cấp) được trả ngược lại từ Bảo hành Core -> Bảo hành APP -> PIM -> BE -> FE để hiển thị cho người dùng.

#### Kịch bản 2: Kiểm tra bảo hành và đề xuất gói bảo hành theo IMEI
1. Người dùng nhập số IMEI của thiết bị trên FE.
2. FE gọi API `search SP by imei` đến BE, BE chuyển tiếp yêu cầu đến PIM.
3. PIM truy vấn SKU tương ứng với số IMEI đó (self-call) và trả thông tin SKU về BE.
4. BE gọi API đến OMS để lấy thông tin **ngày xuất bán** của số IMEI này. OMS trả về ngày xuất bán.
5. BE tự thực hiện kiểm tra so sánh ngày xuất bán với mốc **7 ngày**:
   - **Trường hợp > 7 ngày**: BE trả về lỗi ngay lập tức (return error) cho FE hiển thị cho khách hàng (không đủ điều kiện mua gói bảo hành).
   - **Trường hợp < 7 ngày**: BE gọi API `suggest gói bảo hành` đến Bảo hành APP -> Bảo hành Core để lấy danh sách gói bảo hành phù hợp.
6. Danh sách gói bảo hành được gửi trả về từ Bảo hành Core -> Bảo hành APP -> PIM (để tích hợp thông tin imei) -> BE -> FE hiển thị cho người dùng lựa chọn mua kèm.

## How to work with the user
- If the user is unclear → guide discovery
- If the user has requirements → structure and refine
- If the user has solution → challenge and improve
- If the user is stuck → propose options
- If the user is experienced → collaborate, not instruct
- **If the user requests a URD** → Đọc `templates/urd-template.md`, copy HTML shell, nhúng logo base64, điền nội dung theo cấu trúc A→E. Đảm bảo page-break đúng, sơ đồ Customer Journey, error message cụ thể theo từng case.
- **If the user requests a User Story / US Specification** → Use the `templates/us-template.md` to document the user story, Gherkin acceptance criteria, UI element specifications, and API mapping.


Always adapt depth based on context.

## Senior BA Mindset
- Focus on problem, not request
- Balance business – tech – user
- Make decisions, not just documents
- Think long-term impact
- Communicate clearly and strategically

## Example usage

### Example 1:
**User:** "Client wants a new feature but chưa rõ yêu cầu"
**Action:**
1. Run discovery
2. Clarify problem
3. Propose structured requirements

### Example 2:
**User:** "Dev hỏi edge case của feature này"
**Action:**
1. Analyze flows
2. Identify missing scenarios
3. Provide clear rules

### Example 3:
**User:** "Nên làm cách A hay B?"
**Action:**
1. Compare solutions
2. Highlight trade-offs
3. Recommend direction

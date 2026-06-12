# For building AI Agent
### 1. System Design

Agent system is software => need skill to design a software system to design the agents system (building an orchestra)
=> Need to design how agents talk to each other, use tools effectively,...

### 2. Tool & contract design

Each tool has its own contract, any fuzzy part might lead to agent hallucination
=> Need to clarify the details on schema/input/output/purpose

### 3. Retrieval engineering 

Using RAG for enhancing context
- Chunking
- Embbed
- Reranking

### 4. Reliability engineering 

- Fail
    - Retry 
    - Timeout 
    - Circus breaker

### 5. Security and safety 

- Prompt injection
- Input validation
- Output filter
- Permission boundary

### 6. Evaluation and observability

- Can not improve what can not measure
- Need tracing, log... Complete timeline of what agent did and why
- Metric: success rate, latency, cost per task
- Automate tests that catch regressions before they ship

### 7. Product thinking (most important)

- when agent ask for clarification
- when escalate to actual human
- how to build trust so people actually use it in real work
- UX design for system inherently unpredictable
- Think about the others end not just the code in the middle


# 7 kỹ năng cần thiết để trở thành kỹ sư AI Agent:

### System Design: 
Hiểu cách các thành phần như LLM, công cụ, cơ sở dữ liệu và các tác nhân con (sub-agents) phối hợp nhịp nhàng với nhau.
### Tool and Contract Design: 
Đảm bảo các công cụ có cấu trúc dữ liệu chặt chẽ để AI không phải "tự suy diễn" các yêu cầu đầu vào.
### Retrieval Engineering: 
Tối ưu hóa RAG (Retrieval Augmented Generation) thông qua việc phân đoạn tài liệu, mô hình nhúng và xếp hạng lại (reranking) để đảm bảo ngữ cảnh chính xác.
### Reliability Engineering: 
Xây dựng cơ chế xử lý lỗi như thử lại (retry), đặt thời gian chờ (timeout) và các mạch ngắt (circuit breakers) để hệ thống không bị treo khi gặp sự cố.
### Security and Safety: 
Thiết lập các ranh giới quyền hạn, kiểm tra đầu vào và bộ lọc đầu ra để tránh các cuộc tấn công như tiêm lệnh (prompt injection).
### Evaluation and Observability: 
Sử dụng tính năng theo dõi (tracing) và các quy trình kiểm thử tự động để đo lường hiệu suất thay vì chỉ dựa vào cảm tính.
### Product Thinking: 
Thiết kế trải nghiệm người dùng (UX) để xử lý các tình huống AI không chắc chắn, tạo sự tin tưởng và hỗ trợ người dùng một cách hiệu quả.

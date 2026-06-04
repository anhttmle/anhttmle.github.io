![CPU, GPU, TPU diagram](/assets/content_images/computing_unit-01.png)
Reference: https://www.youtube.com/watch?v=MUWAbpg1xLo

# CPU
CPU (Central Processing Unit): CPU xử lý các tác vụ tính toán đa mục đích. 
- Nó được xây dựng để có độ trễ thấp và xử lý các luồng điều khiển phức tạp, logic rẽ nhánh, system call, interrupt, và các đoạn code cần nhiều quyết định.
- Hệ điều hành, cơ sở dữ liệu và phần lớn ứng dụng chạy trên CPU vì chúng cần sự linh hoạt đó.

# GPU
GPU (Graphics Processing Unit): GPU hoạt động khác. Thay vì có ít core, nó phân tán công việc ra hàng nghìn core để thực thi cùng một lệnh trên tập dữ liệu lớn (kiểu SIMT/SIMD).
- Nếu workload mang tính lặp lại như tính toán ma trận, xử lý pixel, hay các phép toán tensor, GPU xử lý rất nhanh.

# TPU
TPU (Tensor Processing Unit): TPU là phần cứng chuyên dụng. Kiến trúc của nó được thiết kế xoay quanh phép nhân ma trận sử dụng systolic array, với dataflow do compiler điều khiển và buffer on-chip cho weights và activations.
- TPU cực nhanh cho việc huấn luyện và suy luận mạng nơ-ron, miễn là workload phù hợp tốt với phần cứng.

# Terms

## SIMT/SIMD
SIMD và SIMT là hai mô hình xử lý song song dùng để thực hiện cùng một phép toán trên nhiều dữ liệu cùng lúc, nhưng chúng khác nhau về mô hình luồng (threading model):

#### SIMD (Single Instruction, Multiple Data)
Định nghĩa: Một lệnh duy nhất được thực thi đồng thời trên nhiều phần tử dữ liệu.

Cách hoạt động: Một luồng (thread) đơn lẻ thực thi lệnh với nhiều dữ liệu qua các "lane" (kênh) xử lý song song.

Đặc điểm:
- Tất cả các lane thực thi đồng bộ (lockstep) — cùng một bộ đếm chương trình (program counter).
- Không có program counter riêng cho từnglane, không hỗ trợ đường đi thực thi phân kỳ.
- Hiệu quả cao về diện tích và năng lượng khi dữ liệu đều đặn (regular).

Ứng dụng: CPU với instructions đặc biệt (SSE, AVX), xử lý ảnh, âm thanh, video, tính toán khoa học.

#### SIMT (Single Instruction, Multiple Threads)
Định nghĩa: Một lệnh được thực thi đồng thời trên nhiều luồng độc lập.

Cách hoạt động: Một nhóm luồng (ví dụ: warp trong GPU CUDA) thực thi cùng lệnh đồng bộ, nhưng mỗi luồng có:
- Program counter riêng
- Stack riêng
- Có thể có đường đi thực thi phân kỳ (divergent).

Đặc điểm:
- Là mở rộng của SIMD kết hợp với mô hình đa luồng.
- Linh hoạt hơn, phù hợp với dữ liệu không đều và luồng điều khiển phức tạp.
- Hỗ trợ hàng nghìn luồng chạy đồng thời, che lấp latency tốt.

Ứng dụng: GPU (NVIDIA CUDA, AMD ROCm), tính toán song song quy mô lớn.

#### Bảng so sánh nhanh

| Khía cạnh | SIMD | SIMT |
| --- | --- | --- |
| Đơn vị thực thi | Một luồng, nhiều dữ liệu | Nhiều luồng, mỗi luồng một dữ liệu |
| Program counter | Chung cho tất cả lane | Riêng cho từng luồng |
| Phân kỳ luồng | Không hỗ trợ | Hỗ trợ (threads có thể đi nhánh khác) |
| Hiệu quả | Tối ưu khi dữ liệu đều | Tối ưu khi luồng/dữ liệu không đều |
| Phần cứng điển hình | CPU (AVX, SSE) | GPU (CUDA, ROCm) |
| Mô hình lập trình | Vector hóa | Đa luồng (thread-based) |

Tóm lại: SIMD là kiến trúc xử lý vector cứng nhắc nhưng hiệu quả cao; SIMT là mô hình đa luồng linh hoạt được xây dựng trên nền SIMD, phù hợp cho GPU và các bài toán song song quy mô lớn.

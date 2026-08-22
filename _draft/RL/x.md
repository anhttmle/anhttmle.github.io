# [Lecture 01: Introduction to Reinforcement Learning](https://maninae.github.io/cs234/lectures/lecture01.html)

## Definitionf
> Reinforcement Learning.
> A computational framework in which an agent learns to make sequential decisions by interacting with an environment, receiving reward signals, and adjusting its behavior to maximize cumulative reward over time.

## 4 Pillars of Reinforcement Learning
Bốn “trụ cột” là bốn khó khăn nền tảng mà hầu như mọi bài toán RL đều phải giải: **tối ưu mục tiêu, hệ quả dài hạn, khám phá, và khái quát hóa**. Chúng liên kết với nhau: agent vừa phải tìm policy tốt, vừa học từ dữ liệu do chính hành động của nó tạo ra.

### 1. Optimization

RL cần một **objective rõ ràng**, thường là tối đa hóa tổng reward tích lũy chứ không chỉ reward ở bước hiện tại:

$$
\max_\pi \; \mathbb{E}_\pi\left[\sum_{t=0}^{H-1}\gamma^t r_t\right]
$$

Trong đó policy $\pi$ quyết định hành động ở mỗi trạng thái; $\gamma$ điều chỉnh mức độ coi trọng reward tương lai. Khác với supervised learning tối ưu loss trên nhãn cố định, RL tối ưu chất lượng của toàn bộ chuỗi quyết định.

Ví dụ, trong bot đặt lịch nha khoa, tối ưu không nên là “bot trả lời trôi chảy” mà có thể là xác suất lịch hẹn hợp lệ, tỷ lệ khách đến khám, hoặc giá trị dài hạn của khách hàng.

### 2. Delayed consequences

Một hành động hiện tại có thể tạo hiệu ứng chỉ xuất hiện rất lâu sau đó. Vì vậy agent phải lập kế hoạch theo hệ quả dài hạn, không được tham lam chọn hành động có reward tức thời cao nhất.

Có hai bài toán con:

- **Planning:** dự đoán các hậu quả về sau trước khi chọn hành động hiện tại.
- **Temporal credit assignment:** khi reward tốt/xấu xuất hiện ở cuối episode, xác định những hành động trước đó nào đáng được “ghi công” hoặc “chịu trách nhiệm”.

Ví dụ Montezuma’s Revenge: nhặt chìa khóa có thể không thưởng ngay, nhưng là điều kiện để mở cửa và nhận reward lớn sau nhiều bước. Nếu agent chỉ nhìn reward tức thời, nó sẽ không học được hành vi này.

### 3. Exploration

Agent chỉ quan sát outcome của hành động **đã chọn**, không biết trực tiếp “nếu làm cách khác thì sao”. Do đó, agent phải chủ động thử nghiệm để thu thập thông tin về môi trường.

Đây là trade-off kinh điển:

- **Exploration:** thử hành động mới/chưa chắc chắn để khám phá cơ hội tốt hơn.
- **Exploitation:** chọn hành động đang được tin là tốt nhất để thu reward ngay.

Ví dụ recommender: luôn đề xuất item có CTR cao nhất là exploitation; thỉnh thoảng thử item mới để học CTR thực tế là exploration. Nếu chỉ exploitation quá sớm, hệ thống có thể kẹt ở lựa chọn “khá tốt” mà bỏ lỡ item tốt hơn.

### 4. Generalization

Không gian trạng thái thực tế thường khổng lồ hoặc liên tục, nên không thể tạo lookup table kiểu “mỗi state một action”. Agent phải học từ số trải nghiệm hữu hạn và hành động tốt cả ở những state chưa từng gặp.

Deep neural network thường đóng vai trò function approximator cho policy $\pi_\theta(a\mid s)$, value $V_\phi(s)$, hoặc $Q_\phi(s,a)$. Đây là lý do Deep RL mạnh: mạng neural có thể khai thác các pattern chung giữa các state tương tự, thay vì ghi nhớ từng trường hợp riêng lẻ.

Ví dụ với voice bot, agent không thể chỉ học chính xác từng câu khách từng nói. Nó cần khái quát từ các cách diễn đạt khác nhau như “đặt lịch”, “muốn khám răng”, hoặc “cho tôi hẹn bác sĩ” về cùng một intent và chọn action hội thoại phù hợp.

## Mối liên hệ

| Trụ cột | Câu hỏi chính | Nếu xử lý kém |
|---|---|---|
| Optimization | Ta thực sự muốn tối đa hóa điều gì? | Agent tối ưu sai metric/reward hacking |
| Delayed consequences | Hành động hôm nay tác động reward mai sau thế nào? | Chính sách ngắn hạn, không biết credit assignment |
| Exploration | Có nên thử một lựa chọn chưa biết không? | Kẹt ở local optimum hoặc tốn quá nhiều trial |
| Generalization | Làm sao xử lý state mới chưa từng thấy? | Cần dữ liệu khổng lồ, overfit vào trajectory đã thấy |

Bài giảng nhấn mạnh rằng RL không chỉ là “nhận reward rồi update model”: độ khó thực sự nằm ở việc thiết kế objective đúng, truyền reward qua thời gian, cân bằng khám phá-khai thác, và khái quát hóa từ trải nghiệm hạn chế.


## Giải thích concepts:
> RL is particularly powerful in two settings:
> (1) when no examples of desired behavior exist—for instance because the goal is to surpass human performance—and
> (2) when the problem involves an enormous search space with delayed outcomes, making hand-designed solutions infeasible.
> 

Hai điểm này nói về **khi nào Reinforcement Learning (RL) có lợi thế rõ rệt hơn supervised learning, rule-based system, hoặc tìm kiếm truyền thống**: khi không có “đáp án mẫu” để bắt chước, và khi cần tối ưu chuỗi quyết định rất dài với kết quả chỉ xuất hiện muộn.

### 1. Không có ví dụ hành vi đúng

Supervised learning cần dữ liệu dạng $ (x, y) $: đầu vào và nhãn/đáp án đúng. Nhưng nhiều bài toán không có sẵn nhãn “hành động tốt nhất”, đặc biệt nếu mục tiêu là làm tốt hơn con người. 

Ví dụ là **AlphaGo Zero**: không cần dữ liệu các ván cờ chuyên nghiệp để học nước đi đúng. Agent tự chơi với chính nó, nhận thưởng khi thắng và phạt khi thua, rồi dần tìm ra chiến lược hiệu quả hơn. Trong tình huống này, con người chỉ cần mô tả luật chơi và tiêu chí thắng; không cần chỉ cho hệ thống mọi nước đi tốt tại từng bàn cờ.

Điểm cốt lõi:

- Ta biết **mục tiêu cuối** hoặc có thể đo được nó: thắng/thua, doanh thu dài hạn, tỷ lệ hoàn thành nhiệm vụ, số lỗi, mức tiêu thụ năng lượng.
- Ta không biết trước **hành động tối ưu ở từng trạng thái**.
- Agent tạo dữ liệu bằng tương tác: thử hành động, quan sát hệ quả, cập nhật policy để tối đa hóa tổng reward.

#### Vì sao imitation không đủ?

Nếu chỉ học bắt chước chuyên gia, policy thường bị chặn ở chất lượng dữ liệu chuyên gia: nó học phân phối hành động đã quan sát, ít cơ hội khám phá chiến lược mới. RL có thể vượt mức đó nếu reward được thiết kế/đo lường đúng và môi trường cho phép thử nghiệm hoặc mô phỏng.

Ví dụ trong robotics: bạn có thể không có hàng triệu demo về “cách cầm mọi vật thể dưới mọi góc”, nhưng có thể đặt reward là cầm được vật, không làm rơi, không va chạm. Agent học qua trial-and-error trong simulator, sau đó transfer sang robot thật.

### 2. Không gian tìm kiếm khổng lồ, reward đến muộn

Nhiều bài toán không phải là chọn một hành động độc lập, mà là chọn **một chuỗi hành động**. Nếu mỗi bước có $A$ lựa chọn và episode dài $H$ bước, số chuỗi hành động có thể tăng theo $A^H$. Việc liệt kê mọi khả năng nhanh chóng bất khả thi.

Ví dụ: với 10 hành động mỗi bước và horizon 100, số chuỗi là $10^{100}$. Vì vậy, một hệ rule-based hoặc brute-force search không thể viết/duyệt hết các phương án.

RL dùng policy, value function, và đôi khi model để khái quát hóa: thay vì nhớ từng chuỗi hành động, agent học ước lượng “trạng thái này hứa hẹn thế nào về reward tương lai” và chọn hành động cải thiện giá trị đó. Lecture mô tả value là tổng reward tương lai có chiết khấu: $V^\pi(s) = \mathbb{E}_\pi[\sum_{k\ge0}\gamma^k r_{t+k}\mid s_t=s]$.

#### “Delayed outcomes” nghĩa là gì?

Hành động tốt có thể không cho reward ngay, thậm chí gây thiệt ngắn hạn, nhưng mở đường cho reward lớn sau này.

Ví dụ game:

- Nhặt chìa khóa: reward ngay có thể bằng 0.
- Đi vòng qua các phòng: vẫn không có reward.
- Mở cửa bằng chìa khóa ở rất lâu sau: nhận reward lớn.

Nếu agent chỉ tối ưu reward tức thời, nó sẽ bỏ qua chìa khóa. RL cần giải bài toán **temporal credit assignment**: khi reward cuối cùng xuất hiện, hành động nào trong lịch sử dài đã thực sự góp phần tạo nên thành công đó? [maninae.github](https://maninae.github.io/cs234/lectures/lecture01.html)

### Ví dụ gần với hệ AI sản phẩm

Trong một voice bot cho phòng khám, reward không nên chỉ là “một lượt hội thoại có phản hồi”, vì điều đó dễ khiến bot trả lời dài hoặc câu giờ. Mục tiêu thực tế thường là chuỗi kết quả:

$$
\text{Hiểu nhu cầu} \rightarrow \text{sàng lọc đúng} \rightarrow \text{đặt lịch hợp lệ} \rightarrow \text{khách đến khám}
$$

Reward mạnh nhất như “khách đến khám” có thể chỉ biết sau vài ngày. Do đó, RL có tiềm năng tối ưu policy hội thoại dài hạn, nhưng chỉ khả thi khi có logging tốt, attribution đủ tin cậy, ràng buộc an toàn rõ ràng, và thường nên huấn luyện/offline evaluate trước thay vì khám phá trực tiếp trên khách hàng. Đây chính là dạng bài toán có search space lớn và outcome bị trễ.

### Khi hai điểm kết hợp

RL đặc biệt hợp khi đồng thời:

- Không có nhãn cho “hành động đúng tại mỗi bước”.
- Có reward cuối hoặc metric kinh doanh đo được.
- Mỗi hành động làm thay đổi trạng thái và cơ hội về sau.
- Không gian trạng thái/hành động quá lớn để viết rules hoặc search toàn diện.
- Có simulator, logged trajectories, hoặc môi trường đủ an toàn để thu thập trải nghiệm.

Ngược lại, nếu bạn đã có nhãn chính xác cho từng input và mỗi quyết định là độc lập, supervised learning thường đơn giản hơn, rẻ hơn và ổn định hơn RL.

# [Lecture 01: Introduction to Reinforcement Learning](https://maninae.github.io/cs234/lectures/lecture01.html)

## Definitionf
> Reinforcement Learning.
> A computational framework in which an agent learns to make sequential decisions by interacting with an environment, receiving reward signals, and adjusting its behavior to maximize cumulative reward over time.

## Bốn trụ cột của Reinforcement Learning

Điều gì làm RL khác với các nhánh machine learning khác? Có **bốn thách thức nền tảng** xuất hiện trong hầu như mọi bài toán RL: **tối ưu hóa, hệ quả bị trì hoãn, khám phá, và khái quát hóa**.

### 1. Tối ưu hóa

Mục tiêu của RL là tìm ra cách ra quyết định tối ưu, hoặc gần tối ưu. Để làm được điều đó, bài toán phải có một **hàm mục tiêu rõ ràng**.

Một ví dụ đơn giản là tìm tuyến đường ngắn nhất giữa hai thành phố trên mạng lưới giao thông. Trong RL, mục tiêu thường là **tối đa hóa tổng phần thưởng tích lũy** theo thời gian, thay vì chỉ tối đa hóa reward ở bước hiện tại.

Giả thuyết “**Reward is Enough**” của Silver, Singh, Precup và Sutton cho rằng việc tối đa hóa reward có thể là một mục tiêu đủ tổng quát để tạo ra phần lớn, thậm chí toàn bộ, các năng lực được nghiên cứu trong trí tuệ tự nhiên và nhân tạo.

### 2. Hệ quả bị trì hoãn

Một hành động thực hiện ở hiện tại có thể tạo ảnh hưởng rất xa trong tương lai. Ví dụ: tiết kiệm cho hưu trí, hoặc nhặt một chiếc chìa khóa sớm trong game *Montezuma’s Revenge* để mở một cánh cửa ở rất lâu sau đó.

Điều này tạo ra hai thách thức liên quan chặt chẽ:

- **Lập kế hoạch (planning):** Quyết định không chỉ dựa vào lợi ích tức thời mà phải xét đến hệ quả dài hạn.
- **Gán công lao theo thời gian (temporal credit assignment):** Khi cuối cùng thành công hoặc thất bại xảy ra, rất khó xác định chính xác các quyết định trong quá khứ nào đã gây ra kết quả đó.

Ví dụ trong sản phẩm: một recommender có thể nhận reward lớn khi user mua hàng sau 10 lần tương tác. RL phải học xem hành động nào trong toàn bộ chuỗi—thứ tự gợi ý, thời điểm gửi thông báo, giá khuyến mãi—thực sự đóng góp cho conversion.

### 3. Khám phá

Agent RL học về thế giới thông qua việc ra quyết định, tương tự một nhà khoa học thực hiện thí nghiệm. Khi học đi xe đạp, bạn cần thử nhiều lần—và có thể ngã—mới biết cách giữ thăng bằng.

Điểm khó là agent chỉ quan sát reward của **hành động nó thực sự đã chọn**, chứ không biết reward của các hành động thay thế mà nó không thử. Nếu chọn học Stanford thay vì MIT, bạn chỉ trải nghiệm quỹ đạo ở Stanford; không thể trực tiếp quan sát điều gì sẽ xảy ra nếu đã chọn MIT.

Vì vậy, RL luôn có trade-off cơ bản:

- **Exploration:** Thử hành động mới để thu thập thông tin và có thể phát hiện phương án tốt hơn.
- **Exploitation:** Chọn hành động đang được biết là cho reward cao để tối đa hóa kết quả hiện tại.

Ví dụ trong contextual bandit cho quảng cáo: luôn hiển thị quảng cáo có CTR cao nhất là exploitation; thi thoảng hiển thị một creative mới để đo hiệu quả của nó là exploration.

### 4. Khái quát hóa

Policy là một ánh xạ từ kinh nghiệm quá khứ sang hành động. Về lý thuyết, ta có thể lập một lookup table ghi sẵn hành động cho mọi tình huống có thể xảy ra. Tuy nhiên, trong thực tế state space quá lớn nên cách này không khả thi.

Agent phải học từ dữ liệu và kinh nghiệm hữu hạn, rồi hành động hợp lý ở những state mới chưa từng thấy. Đây chính là năng lực **generalization**.

Deep learning đặc biệt phù hợp ở đây: neural network có thể biến observation phức tạp—ảnh, âm thanh, text, history hành vi, graph state—thành representation và xấp xỉ policy/value function trên state space rất lớn. Đây là một lý do quan trọng khiến kết hợp RL với deep neural networks, tức **deep RL**, đạt nhiều kết quả đáng chú ý.


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

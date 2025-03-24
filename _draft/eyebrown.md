# Tóm tắt vấn đề & Đề xuất giải pháp

## Tóm tắt Vấn đề
- **Dữ liệu huấn luyện hạn chế:**  
  - Chỉ sử dụng 100 hình ảnh (55 cho training, 45 cho testing) mà không có k-fold validation.
  - Quá trình huấn luyện chỉ thực hiện trong 5 epoch, gây giới hạn về khả năng tổng quát hóa của mô hình.

- **Thiếu Data Augmentation:**  
  - Mô hình hiện tại không được huấn luyện với các kỹ thuật augmentation.  
  - Điều này dẫn đến tính nhạy cảm cao với các biến đổi như thay đổi ánh sáng, xoay, và scale.  

- **Nhạy cảm với điều kiện ảnh:**  
  - Dù chỉ thay đổi một chút góc độ hoặc ánh sáng, mô hình trả về kết quả khác biệt rõ rệt, làm giảm sự tin tưởng của người dùng.

## Đề xuất Giải pháp

Hai phương án được đề xuất, thực hiện song song để cải thiện hiệu năng của hệ thống:

### Phương án 1: Tối ưu hoá Mô hình AI hiện tại
- **Tăng cường dữ liệu huấn luyện:**  
  - Sử dụng công cụ tự động để tạo thêm các biến thể của hình ảnh gốc.  
  - Ví dụ: Từ mỗi ảnh gốc có thể tạo ra 10 ảnh qua các thao tác như xoay, điều chỉnh độ sáng, làm mờ, và làm sắc nét.

- **Cải tiến kỹ thuật huấn luyện:**  
  - Tinh chỉnh các tham số như số epoch, chiến lược learning rate (warm up & decay).  
  - Sử dụng thêm các kỹ thuật validation (ví dụ: k-fold validation) để đánh giá chính xác hơn hiệu năng của mô hình.

- **Mã mẫu cho Data Augmentation:**
  ```python
  # Rotate ảnh
  def rotate_image(image, angle):
      h, w = image.shape[:2]
      center = (w // 2, h // 2)
      matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
      rotated = cv2.warpAffine(image, matrix, (w, h))
      return rotated

  image = cv2.imread("eyebrow_sample.jpg")
  rotated_image = rotate_image(image, 15)
  cv2.imwrite("rotated.jpg", rotated_image)

  # Chỉnh độ sáng
  def adjust_brightness(image, alpha=1.2, beta=50):
      return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

  bright_image = adjust_brightness(image, alpha=1.5, beta=30)
  cv2.imwrite("bright_image.jpg", bright_image)

  # Thay đổi độ nét: làm mờ và làm sắc nét
  blurred = cv2.GaussianBlur(image, (7, 7), 0)
  cv2.imwrite("blurred.jpg", blurred)

  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
  sharpened = cv2.filter2D(image, -1, kernel)
  cv2.imwrite("sharpened.jpg", sharpened)


### Phương án 2: Áp dụng Consistency Training (UDA)

- **Mục tiêu**:
    Huấn luyện mô hình để nhận diện cùng một đối tượng dưới nhiều biến thể khác nhau (góc độ, ánh sáng, độ nét) nhằm đưa ra kết quả ổn định nhất.
- **Các bước triển khai**:
    - Định nghĩa tiêu chí Consistency:
      - Xác định các giới hạn biến đổi (đến mức nào ảnh vẫn là cùng một đối tượng) dựa trên các chỉ số như IoU (Intersection over Union).
    - Ứng dụng kỹ thuật UDA:
      - Áp dụng nguyên lý của UDA (Unsupervised Data Augmentation) để tận dụng dữ liệu chưa được gán nhãn và tăng cường tính ổn định trong dự đoán.
    - Lợi ích:
      - Giảm sự nhạy cảm của mô hình với những biến đổi nhỏ, cải thiện độ chính xác và độ tin cậy của kết quả.

![Porfolio-7  Eyebrown drawio](https://github.com/user-attachments/assets/ecd6ca55-742c-40f8-90ea-1b130e430078)


## Kết luận
- Tóm lại:
  - Cả hai phương án đều nhằm giải quyết vấn đề về dữ liệu hạn chế và tính nhạy cảm của mô hình đối với các biến đổi của ảnh.
  - Phương án 1 tập trung vào việc tối ưu hoá quy trình hiện tại qua việc tăng cường dữ liệu và điều chỉnh các thông số huấn luyện.
  - Phương án 2 hướng tới việc xây dựng một hệ thống học sâu ổn định hơn thông qua consistency training theo các nguyên tắc được đề xuất trong UDA paper.
- Đề xuất cho khách hàng:
  - Triển khai song song cả hai giải pháp để có thể so sánh và đánh giá hiệu quả, từ đó đưa ra hướng đi tối ưu cho hệ thống AI.

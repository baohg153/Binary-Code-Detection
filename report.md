### Abstract: (Trí)

### Introduction: (Trí)

### Related Work: (Trí)

### Dataset (EDA): (Khôi)
- Trong này nhớ đề cập thách thức cần giải quyết: Tập test khác tập train (về domain, ngôn ngữ)

### Methodology: 
1. Features: (Khôi)
- Trình bày có những feature gì (tìm cách phân loại các features đó gồm những loại nào).
- Phân tích từng feature. 

2. Model: (Bảo)
- Trình bày các model sử dụng, tại sao dùng các model này.
- Trình bày ý tưởng và tại sao nghĩ tới việc chọn threshold. 

### Experiment setup: (Khôi)

### Results: (Bảo)
1. So sánh các model (đặc biệt so sánh fc model và tree-alike)
2. So sánh việc train trên toàn bộ dữ liệu và chỉ phần nhỏ dữ liệu 
    (train 200K lại luôn cho ra kqua tốt hơn 500K)
3. So sánh việc train trên all features và train trên vài features có chọn lọc
    Đưa ra kết quả, các features [1, 2, 3, 4] rất mạnh.
4. Error analysis:
    Vẽ confusion matrix, hay những biểu đồ khác, cho thấy model dự đoán sai nhiều ở đâu.

### Conclusion: (Trí)
- Tổng kết lại, mình đã làm gì, thu được kết quả thế nào.
- Bàn về limitations (mặt hạn chế) của phương pháp hiện tại, và future works.
    + Limitations
        . ví dụ như nó chỉ dùng 7 features, là lượng thông tin còn khá ít. 
        . các features của nhóm tập trung vào "phong cách code" đẹp/xấu. Có những người code rất chuẩn mực, không cẩu thả thì ko thể detect bởi các feature này được.
        . chưa dựa vào ngữ nghĩa mà chỉ dựa vào các features đếm đc (có thể trích paper kia, để nói là ngữ nghĩa giúp chống lại covariance shift tốt).
        ...
    + Future works: (mình sẽ cải tiến thêm thế nào trong tương lai)


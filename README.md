# Giới Thiệu

Đoạn code trên là một chương trình Python để phân tích và tính toán điểm bài kiểm tra dựa trên các đáp án đúng. Chương trình cho phép người dùng nhập đường dẫn đến tệp dữ liệu chứa các câu trả lời của sinh viên, sau đó nó sẽ thực hiện phân tích và tính toán các thông số thống kê về điểm số, câu hỏi được bỏ qua nhiều nhất và câu hỏi bị trả lời sai nhiều nhất. Cuối cùng, chương trình lưu điểm của từng sinh viên vào tệp mới.

### Để chạy chương trình, bạn cần làm theo các bước sau:

#### Bước 1: Cài đặt thư viện pandas (nếu chưa có):
Nếu bạn chưa cài đặt thư viện pandas, hãy mở cửa sổ dòng lệnh (Command Prompt hoặc Terminal) và chạy lệnh sau:
```python
pip install pandas
```
#### Bước 2: Sao chép đoạn code vào một tệp mới:
Tạo một tệp văn bản mới và lưu nội dung của đoạn mã Python vào đó. Bạn có thể sử dụng trình soạn thảo văn bản mặc định của hệ điều hành hoặc bất kỳ trình soạn thảo mã nguồn nào bạn thích.
#### Bước 3: Lưu tệp và đặt tên tệp là *lastname_firstname_grade_the_exams.py*.
Đặt tên tệp là *'lastname_firstname_grade_the_exams.py'* để dễ dàng nhận biết chương trình này.
#### Bước 4: Mở cửa sổ dòng lệnh và chuyển đến thư mục chứa tệp *lastname_firstname_grade_the_exams.py*
Mở cửa sổ dòng lệnh (Command Prompt hoặc Terminal) và sử dụng lệnh ***'cd'*** (hoặc ***'chdir'*** trên Windows) để di chuyển đến thư mục chứa tệp *'lastname_firstname_grade_the_exams.py'*. Ví dụ:
```
cd /path/to/your/directory

```
#### Bước 5: Chạy chương trình:
Nhập lệnh sau để chạy chương trình:
```
python test_score_analyzer.py
```
Sau khi bạn chạy lệnh, chương trình sẽ yêu cầu người dùng nhập một số để chọn công việc thực hiện.Sau khi nhập đúng, hàm trả về số lựa chọn công việc để chương trình tiếp tục thực hiện công việc tương ứng.

#### Bước 6: Phân tích dữ liệu và tính toán các thông số thống kê:
Chương trình sẽ tiến hành phân tích dữ liệu và tính toán các thông số thống kê về điểm số của sinh viên. Sau khi hoàn thành, nó sẽ in kết quả lên màn hình.

Chương trình cũng sẽ lưu điểm của từng sinh viên vào một tệp mới có tên là *'class..._grades.txt'* (... là số thứ tự của lớp) trong cùng thư mục. Điểm của từng sinh viên sẽ được lưu dưới dạng một bảng với hai cột: *'StudentID'* và *'Grade'*.

**Lưu ý:** Đường dẫn đến tệp chứa dữ liệu bài kiểm tra. Hãy nhập đường dẫn đúng của tệp dữ liệu (bao gồm cả tên tệp và phần mở rộng) và nhấn Enter.






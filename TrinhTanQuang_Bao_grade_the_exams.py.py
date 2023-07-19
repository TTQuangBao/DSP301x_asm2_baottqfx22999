import pandas as pd

def check_file():
    # Yêu cầu người dùng nhập đường dẫn đúng của tệp
    while True:
        input_path = input(f"Enter the correct file path: ")
        try:
            # Mở tệp và đọc từng dòng vào biến datalines
            with open(input_path, 'r', encoding="utf8") as file:
                datalines = file.readlines()
                # In thông báo khi mở tệp thành công và trả về dữ liệu và đường dẫn của tệp
                print("Successfully opened " + input_path[-10:-4] + '.txt' )
                return datalines, input_path
        except FileNotFoundError:
            # Xử lý ngoại lệ nếu không tìm thấy tệp và yêu cầu người dùng nhập lại đường dẫn
            print("File cannot be found.")

def is_valid_data(line):
    # Tách các giá trị trong dòng bằng dấu phẩy
    values = line.strip().split(',')
    # Kiểm tra số lượng giá trị trong dòng, nếu không đủ 26 giá trị, trả về 0 (invalid)
    if len(values) != 26:
        return 0

    # Kiểm tra mã sinh viên (giá trị đầu tiên)
    if not values[0].startswith('N'):
        return 2  # Nếu không bắt đầu bằng 'N', trả về 2 (invalid)
    elif not values[0][1:].isdigit():
        return 3  # Nếu không có số sau 'N', trả về 3 (invalid)
    elif len(values[0]) != 9:
        return 4  # Nếu độ dài của mã sinh viên không đúng, trả về 4 (invalid)

    # Nếu dữ liệu hợp lệ, trả về 1 (valid)
    return 1

def calculate_score(answer_key, student_answers):
    # Tính điểm dựa trên các câu trả lời của sinh viên và đáp án
    score = 0
    for ans_key, ans_student in zip(answer_key.split(','), student_answers):
        if ans_student == '':
            continue  # Nếu câu trả lời của sinh viên là rỗng, bỏ qua câu này
        elif ans_student == ans_key:
            score += 4  # Nếu câu trả lời đúng, cộng 4 điểm
        else:
            score -= 1  # Nếu câu trả lời sai, trừ 1 điểm
    return score

def calculate_statistics(scores):
    # Tính các thống kê về điểm
    high_scores_count = len([score for score in scores if score > 80])  # Số lượng điểm cao hơn 80
    mean_score = round(sum(scores) / len(scores), 2)  # Điểm trung bình, làm tròn đến 2 chữ số thập phân
    highest_score = max(scores)  # Điểm cao nhất
    lowest_score = min(scores)  # Điểm thấp nhất
    score_range = highest_score - lowest_score  # Phạm vi điểm

    sorted_scores = sorted(scores)  # Sắp xếp điểm tăng dần
    num_students = len(sorted_scores)  # Tổng số sinh viên
    if num_students % 2 == 1:
        median_score = sorted_scores[num_students // 2]  # Trung vị với số lượng sinh viên lẻ
    else:
        median_score = (sorted_scores[num_students // 2 - 1] + sorted_scores[num_students // 2]) / 2  # Trung vị với số lượng sinh viên chẵn

    return high_scores_count, mean_score, highest_score, lowest_score, score_range, median_score

def analyze_class(lines, answer_key):
    # Phân tích dữ liệu và tính toán điểm và các thông số thống kê
    valid_lines = [line for line in lines if is_valid_data(line) == 1]  # Lọc các dòng hợp lệ

    scores = []  # Danh sách các điểm của sinh viên
    question_skip_counts = {i: 0 for i in range(1, 26)}  # Đếm số lần bỏ qua từng câu hỏi
    question_wrong_counts = {i: 0 for i in range(1, 26)}  # Đếm số lần trả lời sai từng câu hỏi
    student_grades = {}  # Bảng điểm của sinh viên

    # Duyệt qua các dòng hợp lệ và tính toán điểm, số câu bỏ qua, số câu trả lời sai
    for line in valid_lines:
        student_id, *student_answers = line.strip().split(',')
        score = calculate_score(answer_key, student_answers)
        scores.append(score)
        student_grades[student_id] = score

        for i, ans in enumerate(student_answers):
            if ans == '':
                question_skip_counts[i + 1] += 1
            elif ans != answer_key.split(',')[i]:
                question_wrong_counts[i + 1] += 1

    # Tính các thông số thống kê
    high_scores_count, mean_score, highest_score, lowest_score, score_range, median_score = calculate_statistics(scores)
    
    # Tìm câu hỏi bị bỏ qua nhiều nhất và tỷ lệ bỏ qua
    max_skipped = max(question_skip_counts.values())
    questions_skipped = [q for q, count in question_skip_counts.items() if count == max_skipped]
    skip_ratio = round(max_skipped / len(valid_lines), 2)

    # Tìm câu hỏi bị trả lời sai nhiều nhất và tỷ lệ trả lời sai
    max_wrong = max(question_wrong_counts.values())
    questions_wrong = [q for q, count in question_wrong_counts.items() if count == max_wrong]
    wrong_ratio = round(max_wrong / len(valid_lines), 2)

    return high_scores_count, mean_score, highest_score, lowest_score, score_range, median_score, student_grades, max_wrong, questions_wrong, wrong_ratio, max_skipped, questions_skipped, skip_ratio

def save_grades_to_file(filename, student_grades):
    # Chuyển dictionary student_grades thành DataFrame
    df = pd.DataFrame(list(student_grades.items()), columns=['StudentID', 'Grade'])

    try:
        # Lưu DataFrame vào tệp
        df.to_csv(filename[-10:-4] + "_grades.txt", index=False)
        print(f"Grades saved to {filename[-10:-4]}_grades.txt")
    except Exception as e:
        # Hiển thị thông báo lỗi nếu xảy ra lỗi khi lưu tệp
        print("An error occurred while saving grades:", str(e))

def work_check():
    try:
        # Hiển thị menu lựa chọn công việc
        print('****************************************************')
        print('***Plese select the number for appropritate tasks:')
        print(' 1. Quit program.')
        print(' 2. Calculate and analyze test scores.')
        print('****************************************************')
        input_work = int(input('Enter your choice: '))

        # Trả về lựa chọn công việc
        return input_work
    except:
        # Xử lý ngoại lệ nếu người dùng nhập không phải số
        print('Please only enter the value 1 or 2.')
    # Trả về kết quả từ hàm check_file()
    return check_file()

def main():
    # Đáp án đúng của bài kiểm tra
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

    # Vòng lặp chính
    while True:
        # Gọi hàm work_check() để hiển thị menu và lựa chọn công việc
        if work_check() == 2:
            # Nếu lựa chọn công việc là 2, tiến hành phân tích dữ liệu và tính toán
            lines, filename = check_file()
            print("**** ANALYZING ****")
            valid_lines = 0
            invalid_lines = 0

            # Duyệt qua các dòng dữ liệu và kiểm tra tính hợp lệ của từng dòng
            for line in lines:
                if is_valid_data(line) == 1:
                    valid_lines += 1
                elif is_valid_data(line) == 0:
                    print("Invalid line of data: does not contain exactly 26 values: \n", line.strip())
                    invalid_lines += 1
                elif is_valid_data(line) == 2:
                    print("Invalid line of data: N# is invalid: \n", line.strip())
                    invalid_lines += 1
                elif is_valid_data(line) == 3:
                    print("Invalid line of data: N# is invalid: \n", line.strip())
                    invalid_lines += 1
                elif is_valid_data(line) == 4:
                    print("Invalid line of data: N# is invalid: \n", line.strip())
                    invalid_lines += 1
            if invalid_lines == 0:
                print('No errors found!')
                
            # In thông tin báo cáo về dữ liệu kiểm tra
            print("**** REPORT ****")
            print("Total valid lines of data:", valid_lines)
            print("Total invalid lines of data:", invalid_lines)

            # Tính toán và in thông tin thống kê
            total_Hscore, average_score, highest_score, lowest_score, score_range, median_score, student_grades, max_wrong, questions_wrong, wrong_ratio, max_skipped, questions_skipped, skip_ratio = analyze_class(lines, answer_key)

            print('Total student of high scores: ', total_Hscore)
            print('Mean (average) score: ', average_score)
            print('Highest score: ', highest_score)
            print('Lowest score: ', lowest_score)
            print('Range of scores: ', score_range)
            print('Median score: ', median_score)
            print("Question that most people skip:", ", ".join(f"{q} - {max_skipped} - {skip_ratio}" for q in questions_skipped))
            print("Question that most people answer incorrectly:", ", ".join(f"{q} - {max_wrong} - {wrong_ratio}" for q in questions_wrong))

            # Lưu điểm của sinh viên vào tệp
            save_grades_to_file(filename, student_grades)

        else:
            # Nếu lựa chọn công việc là 1, kết thúc chương trình
            print('See you later')
            break


if __name__ == "__main__":
    main()

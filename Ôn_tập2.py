class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Major: {self.major}")


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self):
        student_id = input("Nhập mã sinh viên cần xóa: ").strip()
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s) 
                print(f"Đã xóa sinh viên {s.name}")
                return
        print("Không tìm thấy sinh viên")

    def list_students(self):
        print(f"Danh sách sinh viên môn {self.course_name}:")
        for s in self.students:
            s.display_info()
        if not self.students:
            print("Chưa có sinh viên nào")
            
# 2.1 Tổng các số chẵn (dùng hàm cơ bản)
def sum_even(numbers):
    tong = 0
    for num in numbers:
        if num % 2 == 0:       # nếu chia hết cho 2
            tong = tong + num
    return tong


# 2.2 Đảo ngược thứ tự từ (dùng hàm cơ bản)
def reverse_words(sentence):
    words = sentence.split()         # tách thành list từ
    result = ""                      # chuỗi kết quả
    for i in range(len(words)-1, -1, -1):  # đếm ngược từ cuối về đầu
        result = result + words[i] + " "
    return result.strip()            # bỏ khoảng trắng thừa ở cuối


# 2.3 Đếm số lần xuất hiện ký tự (dùng hàm cơ bản)
def char_frequency(s):
    freq = {}                        
    for char in s:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    return freq



# Tìm số lớn nhất và lớn thứ hai
def second_largest(lst):
    if len(lst) < 2:
        return None
    max1 = lst[0]
    max2 = lst[0]
    for x in lst:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x
    return max2

# Tìm số lớn nhất và lớn thứ hai
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chuẩn hóa họ tên (viết hoa chữ cái đầu mỗi từ)
def standardize_name(name):
    words = name.strip().lower().split()
    result = ""
    for word in words:
        result += word[0].upper() + word[1:] + " "
    return result.strip()
# Ví dụ: "  ngUYeN   vAN an   " → "Nguyen Van An"

# Xóa tất cả phần tử có giá trị x trong list
def remove_all(lst, x):
    i = 0
    while i < len(lst):        
        if lst[i] == x:
            lst.pop(i)
        else:
            i += 1
    return lst
            
# Loại bỏ phần tử trùng lặp
def remove_duplicates(lst):
    result = []
    for x in lst:
        if x not in result:    # chỉ thêm nếu chưa có
            result.append(x)
    return result
           
if __name__ == "__main__":
    sv1 = Student("01", "TT", "CNTT")
    sv2 = Student("02", "TB", "CNTT")
    sv3 = Student("03", "TA", "CNTT")
    
    Mon1 = Course("01", "Lập Trình AI")
    
    Mon1.add_student(sv1)
    
    Mon1.list_students()
    
    Mon1.remove_student()
    
    Mon1.list_students()
    
    print("\n")
    print(sum_even([1, 2, 3, 4, 6]))       
    print(reverse_words("I love Python"))     
    print(char_frequency("banana"))               
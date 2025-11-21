class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = int(salary)

    def display_info(self):
        print(f"ID: {self.emp_id} | Tên: {self.name} | Mức lương: {self.salary}")

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def find_by_salary(self):
        min_salary = int(input("Nhập mức lương: "))
        results = [emp for emp in self.employees if emp.salary >= min_salary]

        for emp in results:
            emp.display_info()
        return results

    def show_all(self):
        for emp in self.employees:
            emp.display_info()

def count_digits(s):
    dem = 0
    for c in s:
        if '0' <= c <= '9':
            dem += 1
    return dem


def common_elements(list1, list2):
    ketqua = []
    for x in list1:
        if x in list2 and x not in ketqua:
            ketqua.append(x)
    return ketqua


def word_count(sentence):
    s = sentence.lower()
    chuoi = ""
    for c in s:
        if ('a' <= c <= 'z') or c == ' ':
            chuoi += c

    tu = chuoi.split()
    d = {}
    for t in tu:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    return d

# 2. Tổng số chẵn trong list
def sum_even(lst):
    tong = 0
    for x in lst:
        if x % 2 == 0:
            tong += x
    return tong

# 3. Đảo ngược thứ tự từ trong câu
def reverse_words(s):
    words = s.split()
    res = ""
    for i in range(len(words)-1, -1, -1):
        res += words[i] + " "
    return res.strip()  

# 7. Chuẩn hóa họ tên (viết hoa đầu mỗi từ)
def standardize_name(s):
    words = s.strip().lower().split()
    res = ""
    for w in words:
        res += w[0].upper() + w[1:] + " "
    return res.strip()

# 8. Xóa tất cả phần tử = x trong list
def remove_all(lst, x):
    i = 0
    while i < len(lst):
        if lst[i] == x:
            lst.pop(i)
        else:
            i += 1
    return lst

# 9. Loại bỏ trùng lặp trong list
def remove_duplicates(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

# 11. Đảo ngược số (123 → 321)
def reverse_number(n):
    dao = 0
    while n > 0:
        dao = dao * 10 + n % 10
        n //= 10
    return dao

# 12. Tổng các chữ số của số
def sum_digits(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

# 13. Đếm nguyên âm trong chuỗi
def count_vowels(s):
    dem = 0
    for c in s.lower():
        if c in 'aeiou':
            dem += 1
    return dem

# 15. Kiểm tra chuỗi đối xứng (palindrome)
def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    nv1 = Employee("01", "TT", "10000")
    nv2 = Employee("02", "TA", "10002")
    nv3 = Employee("03", "TB", "10003")

    CT1 = Company()

    CT1.add_employee(nv1)
    CT1.add_employee(nv2)
    CT1.add_employee(nv3)

    CT1.show_all()

    CT1.find_by_salary()

    print(count_digits("abc12345d"))          # 5
    print(count_digits("hello2024"))          # 4

    print(common_elements([1,2,3,4], [2,4,6,8]))   # [2, 4]
    print(common_elements([1,1,2,2], [2,2,3]))     # [2]

    print(word_count("Python is great, and python is powerful!"))
    



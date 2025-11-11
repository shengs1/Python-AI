import math

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Các số nguyên tố từ 1 đến 50 là:")
for number in range(1, 51):
    if is_prime(number):
        print(number, end=" ")
print("\n")

# Hàm đếm nguyên âm
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

result_b = count_vowels("Artificial Intelligence")
print("Số nguyên âm (vowels) trong chuỗi là:", result_b)
print("\n")

# Hàm tính giá trị trung bình
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

result_c = average([4, 7, 2, 9, 5])
print("Giá trị trung bình là:", result_c)
print("\n")

# Lớp Book
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print("Id:", self.book_id)
        print("Tiêu đề:", self.title)
        print("Tác giả:", self.author)
        print("Giá:", self.price)
        print("---------------")

# Lớp Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author_name):
        result = []
        for book in self.books:
            if book.author.lower() == author_name.lower():
                result.append(book)
        return result

    def get_total_value(self):
        total = 0
        for book in self.books:
            total += book.price
        return total

    def display_info(self):
        for book in self.books:
            book.display_info()

# Thêm sách vào thư viện
b1 = Book(1, "Python Cơ Bản", "Nguyễn Nhật Ánh", 100000)
b2 = Book(2, "AI Toàn Tập", "Nguyễn Nhật Ánh", 150000)
b3 = Book(3, "Data Science", "Trần Thị B", 120000)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

print("Thông tin tất cả sách trong thư viện:")
lib.display_info()

print("\nTìm sách của Nguyễn Nhật Ánh:")
books = lib.search_by_author("Nguyễn Nhật Ánh")
for i in books:
    i.display_info()

print("Tổng giá trị sách trong thư viện:", lib.get_total_value())

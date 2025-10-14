print("HÀM")
print("28. In thiệp Cảm ơn")
print("1. Thiệp Cảm ơn Cơ bản")
def print_thank_you(ten):
    """
    In ra một chuỗi chứa
    "Thank you" và tên

    Tham số
    -------
    ten : string
        tên là tên của ai đó
    """
    print("Thank you", ten)

print_thank_you("Maria")

print_thank_you("Xiao")

print("\n2. Thiệp cảm ơn trang trọng")

def print_thank_you(tiento, ho, ten):
    """
    In ra một chuỗi chứa
    "Thank you" và đầu vào

    Tham số
    --------
    tiento : string
        là ông hay bà
    ho : string
        họ
    ten : string
        tên là tên của ai đó
    """
    print("Thank you", tiento, ho, ten)

print_thank_you("Mrs", "Maria", "Lopez")
# Kết quả: Thank you Mrs Maria Lopez

print_thank_you("Mr", "Xiao", "Li")
# Kết quả: Thank you Mr Xiao Li

print("\n3. Thiếu tên!")
def print_thank_you(tiento, ho, ten=""):
    """
    In ra một chuỗi chứa
    "Thank you" và đầu vào

    Tham số
    --------
    tiento : string
        là ông hay bà
    ho : string
        họ
    ten : string
        tên là tên của ai đó, mặc định là trống
    """
    print("Thank you", tiento, ho, ten)

print_thank_you("Mrs", "Maria", "Lopez")
# Thank you Mrs Maria Lopez
print_thank_you("Mr", "Xiao")
# Thank you Mr Xiao

print("\n4. Thiếu tiền tố và/hoặc họ!")
def print_thank_you(tiento="", ho="", ten=""):
    """
    In ra một chuỗi chứa "Thank you" và đầu vào

    Tham số
    ----------
    tiento : string
        là ông hay bà, mặc định để trống
    ho : string
        họ, mặc định để trống
    ten : string
        tên, mặc định để trống
    """

    print("Ông/bà:", tiento)
    print("Họ:", ho)
    print("Tên:", ten)
    print("Thank you", tiento, ho, ten)

# Ví dụ gọi hàm:
print_thank_you("Mrs", "Maria", "Lopez")
# Ông/bà: Mrs
# Họ: Maria
# Tên: Lopez
# Thank you Mrs Maria Lopez

print_thank_you(ho="Xiao", ten="Li")
# Ông/bà:
# Họ: Xiao
# Tên: Li
# Thank you  Xiao Li

print("\nBài tập áp dụng")

print("\n1. Các trường hợp chuỗi")
def truong_hop_chuoi(s):
    print("Chuỗi gốc:", s)
    print("Chữ thường:", s.lower())
    print("Chữ hoa:", s.upper())
    print("Chữ cái đầu hoa:", s.title())
    print("Đổi chỗ chữ cái đầu:", s.swapcase())
    print()

print("Gọi với một từ")
truong_hop_chuoi("Hello")

print("\nGọi với ít nhất hai từ")
truong_hop_chuoi("Hello World")

print("\nGọi cho mỗi phần tử của danh sách")
summer_vacation = ["Hiking trails", "weekEndcampIng", "enjoying nature", "fishing"]
for item in summer_vacation:
    truong_hop_chuoi(item)

print("\n2. Độ dài chuỗi")
def loc_theo_do_dai(danh_sach_chuoi, do_dai):
    for chuoi in danh_sach_chuoi:
        if len(chuoi) == do_dai:
            print(chuoi)

print("Gọi với hai độ dài khác nhau")
danh_sach_chuoi_mau = ["apple", "banana", "cherry", "date"]
print("vd1 với do dai = 5")
loc_theo_do_dai(danh_sach_chuoi_mau, 5)
print("\nvd2 với do dai = 6")
loc_theo_do_dai(danh_sach_chuoi_mau, 6)

print("\n3. Nhiều số")
def chia_het_cho(danh_sach_so, uoc_so=2):
    for so in danh_sach_so:
        if so % uoc_so == 0:
            print(so)

print("Gọi với hai ước số khác nhau")
danh_sach_so_mau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("vd1 với ước số = 3")
chia_het_cho(danh_sach_so_mau, 3)
print("vd2 với ước số = 4")
chia_het_cho(danh_sach_so_mau, 4)

print("\nGọi mà không có ước số")
chia_het_cho(danh_sach_so_mau)

print("\n4. Nhân đôi số")
def tao_tu_dien_nhan_doi():
    n = int(input("Nhập một số: "))
    d = {}
    for i in range(1, n + 1):
        d[i] = i * 2
    print(d)


print("Gọi hàm")
tao_tu_dien_nhan_doi()

print("\n Bài tập áp dụng T185")
import random

def chon_tu_ngau_nhien(danh_sach_tu):
    tu_duoc_chon = random.choice(danh_sach_tu)  # chọn ngẫu nhiên 1 từ
    return tu_duoc_chon.lower()  # chuyển về chữ thường

# Ví dụ sử dụng:
ds_tu = ["muỗng", "Nĩa", "DAO"]
tu_ket_qua = chon_tu_ngau_nhien(ds_tu)
print("Từ được chọn:", tu_ket_qua)

def hien_thi_chu_da_doan(chu_da_doan, tu):
    ket_qua = ""

    for chu in tu:
        if chu.lower() == chu_da_doan.lower():
            ket_qua += chu + " "  # nếu đoán đúng, hiển thị chữ
        else:
            ket_qua += "_ "       # nếu chưa đoán đúng, hiển thị gạch dưới

    return ket_qua.strip()

# Ví dụ sử dụng:
tu = "hello"
chu_doan = "l"
ket_qua = hien_thi_chu_da_doan(chu_doan, tu)
print("Kết quả đoán:", ket_qua)







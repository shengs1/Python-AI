print("27. Tổng quan về chuỗi")
print("1. Cắt chuỗi")
two_ways = "rsecwyadrkd"
print(two_ways)

print("\nTrích xuất từng ký tự thứ hai:")
print(two_ways[::2])

print("\nTrích xuất từng ký tự thứ hai và đảo ngược kết quả:")
print(two_ways[::-2])


print("\2. Các phép toán số học trên chuỗi")
print("Nối chuỗi hai chuỗi:")
daya="laugh"
dayb="fun"
combo=daya+dayb
print(combo)

print("\nSao chép một chuỗi 5 lần:")
motcuoi=":)"
namcuoi=motcuoi*5
print(namcuoi)


print("\n3. Thay thế hoặc xóa chuỗi con")
print("Cho chuỗi sau:")
favorites = "I like cooking, my family, and my friends"
print(favorites)

print("\nThay thế ký tự ở vị trí 0 bằng U bằng cách sử dụng cắt và gán")
#favorites [O] = "U"
print("LỖI")

print("\nLàm lại nhiệm vụ tương tự bằng cách sử dụng cắt và nối:")
from_position_one = favorites [1:] #Xóa phần tử đầu tiên
favorites= "U" + from_position_one #Nối U với dãy đã xóa
print(favorites)

print("\nLàm lại cùng một tác vụ bằng phương thức chuỗi .split():")
#bằng phương thức chuỗi .split():

favorites = "I like cooking, my family, and my friends"
print(favorites)

parts = favorites.split("I") # cắt bỏ chữ I
print(parts)

favorites= "U" + parts [1] # nối với thành phần part [1]
print (favorites)

print("\nThay thế dấu phẩy bằng dấu chấm phẩy bằng phương thức chuỗi: .replace():")
favorites = "I like cooking, my family, and my friends"
favorites = favorites.replace(",", ";")
print(favorites)

print("\nBỏ dấu phẩy:")
favorites = "I like cooking, my family, and my friends"
favorites = favorites.replace(",", "")
print(favorites)



print("\n4. Tìm kiếm một chuỗi con trong một chuỗi")
print("Cho chuỗi sau:")
us = "we are"
print(us)

print("\nTìm vị trí của ký tự e bằng phương thức .find():")
positions = us.find("e")
print(positions)

print("\nTìm vị trí của ký tự e bằng một cách khác:")
#khởi tạo dãy vị trí
positions=[]
# tìm tất cả
for i in range(len(us)):
    if us [i]=="e":
        positions.append(i)
print(positions)

print("\nTìm vị trí của ký tự f bằng phương thức .find():")
positions = us.find("f")
print(positions)


print("\n5. Đếm số chuỗi con trong một chuỗi")
print("Cho chuỗi sau:")
hobbies = "I like going to the movies, traveling, and singing"
print(hobbies)

print("\nĐếm số lượng chuỗi con bằng phương thức .count():")
demchuoi = hobbies.count("ing")
print(demchuoi)

print("\n6. Chuỗi vào danh sách và ngược lại")
print("Cho chuỗi sau:")
string = "How are you"
print(string)

print("\nChuyển đổi chuỗi thành danh sách các chuỗi trong đó mỗi phần tử là một từ:")
list_of_strings = string.split()
print(list_of_strings)

print("\nChuyển đổi danh sách các chuỗi thành chuỗi bằng phương thức .join():")
# thêm khoảng trắng giửa các thành phần
string_from_list = " ".join(list_of_strings)
print(string_from_list)

print("\n7. Thay đổi kiểu chữ")
print("Cho chuỗi sau:")
loichao="Hello! We are DHV"
print(loichao)

print("\Sửa đổi chuỗi thành chữ hoa và chữ thường; chỉ đổi ký tự đầu tiên của chuỗi thành chữ, "
      "sau đó là từng từ trong chuỗi; cuối cùng, đảo ngược các trường hợp:")
#in hoa
print(loichao.upper())
#in thuong
print(loichao.lower())
# Viết hoa chữ đầu tiên
print(loichao.capitalize())
# Viết hoa chữ cái đầu tiên mỗi chữ
print(loichao.title())
# Hoán đổi hoa thành thường, thường thành Hoa
print(loichao.swapcase())

print("\8. In biến")
print("Cho chuỗi sau:")
chaosang="morning"
print(chaosang)

print("\nIn ra Good morning! theo 4 cách khác nhau, sử dụng (1) nối chuỗi, (2) phân tách bằng "
      "dấu phẩy, (3) phương thức .format() và (4) chuỗi f:")
#(1) Nối chữ +
print("Good" + chaosang + "!")
#(2) dùng dây",
print("Good", chaosang, "!")
# (3) the method .format()
print("Good {}!".format(chaosang))
# (4) f-strings
print(f"""Good {chaosang}!""")

print("\n Cho một chuỗi và một biến số:")
chaosang="morning"
thoigian=10
print(chaosang)
print(thoigian)

print("\nsử dụng cùng bốn phương pháp trên (lưu ý rằng các câu được viết trên hai dòng riêng biệt):")
# (1) Nối chữ bằng dấu cộng
print("Good " + chaosang + "!\nIt's " + str(thoigian) + " a.m.\n")

# (2) Dùng dấu phẩy để nối
print("Good", chaosang, "!\nIt's", str(thoigian), "a.m.\n")

# (3) Sử dụng phương thức .format()
print("Good {}!\nIt's {} a.m.\n".format(chaosang, thoigian))

# (4) Sử dụng f-strings (Python 3.6+)
print(f"Good {chaosang}!\nIt's {thoigian} a.m.")

print("\nVậy còn việc in số với số thập phân ít hơn thì sao?")
print("Cho biến số sau:")
giatri=1.23456
print(giatri)

print("\nIn Số là 1,23—chỉ lưu ý hai chữ số thập phân đầu tiên—sử dụng bốn phương pháp trên:")
# (1) Nối chuỗi với round và str
print("Giá trị là " + str(round(giatri, 2)))

# (2) Dùng dấu phẩy để nối
print("Giá trị là", round(giatri, 2))

# (3) Dùng phương thức .format()
print("Giá trị là {:.2f}".format(giatri))

# (4) Dùng f-strings (Python 3.6+)
print(f"Giá trị là {giatri:.2f}")


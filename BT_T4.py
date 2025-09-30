#Từ điển
print("Từ điển")
classics = {"Austen": "Pride and Prejudice","Shelley":"Frankenstein","Joyce":"Ulyssessss"}
#1
print("1")
print(classics)

#2
# as dict_items
print("\n2")
print(classics.items())
# as a list of tuples
print(list(classics.items()))

#3
# authors as dict_items
print("\n3")
print(classics.keys())
# authors as a list
print(list(classics.keys()))

#4
# titles as dict_items.
print("\n4")
print(classics.values())
# titles as a list
print(list(classics.values()))

#5
print("\n5-6")
print("Wrong title: " + classics ["Joyce"])

#6
classics ["Joyce"] = "Ulysses"
print("Corrected title: " + classics ["Joyce"])

#7
# adding the first book (syntax 1)
print("\n7")
classics ["Swift"] = "Gulliver's travels"
print(classics)

#8
# adding the second book (syntax 2)
print("\n7")
classics.update({"Bronte":"Jane Eyre"})
print(classics)

#9
# deleting the first book (syntax 1)
print("\n9")
del classics["Austen"]
print(classics)

#10
# deleting the second book (syntax 2)
print("\n10")
classics.pop("Joyce")
print(classics)

#Bài Tập Áp Dụng
print("\n")
print("Bài Tập Áp Dụng")
print("Bài 1")
student = {"First name":"Bruce", "Last name":"Zhiang", "Sex":"Male", "Age":21,
"Course":"Literature", "Hobby":"Swimming"}

print("a. In ra tất cả các khóa và giá trị của chúng")
print(student)

print("\nb. In ra tất cả các khóa.")
print(student.keys())

print("\nc. In ra tất cả các giá trị.")
print(student.values())

print("\nd. Bruce gần đây đã chuyển khóa học của mình từ Literature to Foreign Languages, vì vậy bạn cần cập nhật dữ liệu của anh ấy")
student["Course"] = "Foreign Languages"
print(student)

print("\ne. Có hai thông tin bị thiếu: Address and Phone number,vì vậy bạn cần thêm chúng vào (sử dụng (hai cú pháp khác nhau).")
print("Cách 1:")
student["Address"] = "CBA"
student["Phone number"] = "9999"
print(student)

print("\nCách 2:")
student.update({"Address": "ABC"})
student.update({"Phone number": "8888"})
print(student)

print("\nf. Cuối cùng, do chính sách bảo mật mới, bạn phải xóa Sex và Hobby.")
#Cách 1
del student["Sex"]
#Cách 2
student.pop("Hobby")
print(student)

print("\n")
print("Bài 2")
pets = [{"name":"Toby", "animal type":"dog", "age":2},
{"name":"Kitty", "animal type":"cat", "age":5},
{"name":"Tiki", "animal type":"parrot", "age":1}]

print("a. Bạn vừa tiếp nhận một bệnh nhân mới, một chú ngựa 4 tuổi tên là Sugar, và bạn thêm nó vào danh sách.")
pets.append({"name": "Sugar", "animal type": "horse", "age": 4})
print(pets)

print("\nb. Bây giờ, bạn cần in ra tất cả tên các loài động vật. Trước tiên, hãy thực hiện việc này bằng vòng lặp for qua các phần tử và sau đó bằng vòng lặp for qua các chỉ mục.")
for pet in pets:
    print(pet["animal type"])

print("\nc. Cuối cùng, bạn thêm một mục cho biết tất cả các loài động vật hiện đang ở phòng khám (bạn sử dụng kiểu dữ liệu nào?).")
animal_types = set()
for pet in pets:
    animal_types.add(pet["animal type"])

print("các loài động vật hiện đang ở phòng khám: ", animal_types)

print("\n")
print("Bài 3")
print("\na. Tạo một danh sách các từ điển chứa 3 hương vị nước ép (cam, chanh và lựu), giá cả và màu sắc của chúng.")
juices = [
    {"flavor": "orange", "price": 15000, "color": "orange"},
    {"flavor": "lemon", "price": 12000, "color": "yellow"},
    {"flavor": "pomegranate", "price": 18000, "color": "red"}
]

print("\nb. Thêm mục 'in shop' với giá trị True cho mỗi loại nước ép")
for juice in juices:
    juice["in shop"] = True
    print(juice)

print("\nc. Thêm đơn hàng mới - nước ép nho")
juices.append({
    "flavor": "grape",
    "price": 16000,
    "color": "purple",
    "in shop": True
})
print(juices)

print("\nd. Tính giá trung bình của các loại nước ép")
total_price = sum(juice["price"] for juice in juices)
average_price = total_price / len(juices)
print(f"Giá trung bình của một loại nước ép là: {average_price:.0f} VND")





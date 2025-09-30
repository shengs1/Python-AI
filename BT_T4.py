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

print("\n25. Chuyến đi Thụy Sĩ (Từ điển với danh sách là giá trị)")
print("1 bắt đầu với một từ điển trống:")
tips={} # dictionary Go use {}
print(tips)

print("\n2 đưa ra một số gợi ý:")
tips ["cities"] = ["Bern", "Lucern"]
tips ["food"] = ["chocolate", "raclette"]
print(tips)

print("\n3  thêm hai thành phố nữa và hai món ăn:")
# use .append()
print("Cách thêm 1:")
tips["cities"].append("Lugano")
print(tips)

print("\n4")
# Method 2 to add to use +
print("Cách thêm 2:")
tips["cities"] += ["Geneva"]
print(tips)

print("\n5")
# use get() and append
print("Cách thêm 3 dùng get và append:")
tips.get("food").append("onion tarte")
print(tips)

print("\n6")
# use get() and +
print("Cách thêm 4 dùng get và +:")
tips ["food"] = tips.get("food") + ["fondue"]
print(tips)

print("\n7")
# print key and value
print("Kiểm tra xem từ điển có chính xác không, in từng mục một:")
for k,v in tips.items():
    print(k,v)

print("\n8")
print("Cải thiện bản in để dễ đọc hơn:")
for k,v in tips.items():
    print("{:>6}: {}".format(k,v)) #right align before : 6 characters
#string .format() là  định dạng các đối số và chèn chúng vào các chỗ giữ chỗ

print("\n9")
print("chỉ muốn in các khóa hoặc các giá trị:")
for k in tips.keys():
    print(k)

print("\n10")
print("Tương tự cho giá trị:")
for v in tips.values():
    print(v)

print("\nBài Tập Áp Dụng 1")
print("Dữ liệu ban đầu:")
store = {"furniture": ["chair", "table", "sofa"], "amount": [24, 7, 6], "price": [200, 500, 1200]}
print(store)

print("\na. Khách mua 4 chiếc ghế (chair), cập nhật số lượng bằng phép toán số học:")
# Ghế là món đầu tiên trong danh sách furniture, index = 0
store["amount"][0] -= 4  # Trừ 4 chiếc ghế
print(store)

print("\nb. Thêm 9 tấm thảm, mỗi tấm 150 đô; và 4 chiếc đèn, mỗi chiếc 180 đô:")
print("Sử dụng cú pháp khác nhau: .append() và toán tử cộng +=:")
print("Sử dụng cú pháp .append()")
store["furniture"].append("carpet")  # Thêm tấm thảm
store["amount"].append(9)             # Số lượng 9 tấm thảm
store["price"].append(150)            # Giá 150 đô/tấm
print(store)

print("Sử dụng cú toán tử cộng +=:")
store["furniture"] += ["lamp"]        # Thêm đèn
store["amount"] += [4]                 # Số lượng 4 chiếc đèn
store["price"] += [180]
print(store)

print("\nc. Chủ nhà hàng mua tất cả các bàn (table):")
# Bàn ở index 1 trong danh sách
print("Cách 1: dùng trực tiếp chỉ số")
store["amount"][1] = 0
print(store)
print("Cách 2: dùng phương thức index() để tìm vị trí và cập nhật:")
idx = store["furniture"].index("table")
store["amount"][idx] = 0
print(store)

print("\nd. In từ điển với căn chỉnh khóa sang phải, giá trị sang trái:")
for key in store:
    print(f"{key:>10}: {store[key]}")

print("\ne. Tính tổng giá trị tồn kho = số lượng * giá của từng món, rồi cộng lại:")
total_value = 0
for amount, price in zip(store["amount"], store["price"]):
    total_value += amount * price
print("Tổng giá trị đồ nội thất còn trong kho:", total_value)



print("\nBài Tập Áp Dụng 2")
#Dữ liệu ban đầu
dictionary = {"numbers": [2, 3, 4, 5, 6, 7, 8, 9, 10]}
print("Dữ liệu ban đầu:")
print(dictionary)

# a. Thêm cặp khóa: giá trị với khóa là 'even' và giá trị là danh sách True/False cho số chẵn/lẻ
print("\na. Thêm cặp khóa 'even' với True cho số chẵn, False cho số lẻ:")
even_list = [num % 2 == 0 for num in dictionary["numbers"]]
dictionary["even"] = even_list
print(dictionary)

# b. Trừ 1 cho mỗi số trong danh sách numbers
print("\nb. Trừ 1 cho mỗi số trong danh sách 'numbers':")
dictionary["numbers"] = [num - 1 for num in dictionary["numbers"]]
print(dictionary)

# c. Sửa đổi danh sách Boolean 'even' sao cho tương ứng với danh sách số mới
print("\nc. Dịch chuyển danh sách Boolean 'even' để phù hợp với danh sách số mới:")
# Ở đây dịch chuyển có thể hiểu là dịch trái hoặc dịch phải 1 vị trí.
# Do số bị trừ đi 1, số lẻ/chẵn sẽ thay đổi. Chúng ta sẽ dịch chuyển danh sách 'even' sang phải 1 vị trí
# để "cập nhật" tương ứng với numbers mới.
dictionary["even"] = [dictionary["even"][-1]] + dictionary["even"][:-1]
print(dictionary)


# ------------------------------------------------------------------
# Phần 4: In hình tam giác với số nguyên người dùng nhập

print("\nPhần 4: In hình tam giác số")

while True:
    n = input("Nhập số nguyên dương (hoặc nhập 'exit' để thoát): ")
    if n.lower() == "e":
        print("Kết thúc chương trình.")
        break

    if not n.isdigit() or int(n) <= 0:
        print("Vui lòng nhập số nguyên dương hợp lệ.")
        continue

    n = int(n)

    # Tạo dictionary chứa số và danh sách lặp lại số đó
    triangle_dict = {}
    for i in range(1, n + 1):
        triangle_dict[i] = [i] * i

    # In ra hình tam giác theo yêu cầu
    for key in triangle_dict:
        print(key, triangle_dict[key])

print("\n26. Đếm, nén và sắp xếp")
print("1. Đếm phần tử")
greetings = "hello! how are you?"
print(greetings)

print("\n1. Sử dụng if/elif:")
# create character library and value is count
demkytu={}
for kytu in greetings:
    if kytu not in demkytu.keys(): # if that character is not already in the # key of the character count

        demkytu[kytu]=1;
    else:
        demkytu [kytu]+=1
    for k,v in demkytu.items():
        print(k,v)

print("\n2. Sử dụng .get():")
# create character library and value is count
demkytu = {}
for kytu in greetings:
    demkytu[kytu] = demkytu.get(kytu, 0) + 1
for k, v in demkytu.items():
    print(k, v)

print("\n2. Nén thông tin")
print("1")
print("Cho danh sách sau:")
sparse_vector = [0, 0, 0, 1, 0, 7, 0, 0, 4, 0, 0, 0, 8, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(sparse_vector)

print("\n2")
print("Chuyển đổi nó thành một từ điển:")
# create a dictionary for it
sparse_dict = {}
for i in range(len(sparse_vector)):
    if sparse_vector[i] != 0: # if the value there is not 0
        sparse_dict[i] = sparse_vector[i] # write to dictionary position i # and other value o there
print(sparse_dict)

print("\n3")
print("thêm lưu trữ chiều dài của dãy số vào từ điển")
sparse_dict["length"] = len(sparse_vector)
# print out each key and corresponding value
for k,v in sparse_dict.items():
    print(k,v)

print("\n4")
print("Làm thế nào để chúng ta quay lại vectơ thưa thớt? (khôi phục)")
#đầu tiên xác định chiều dài qua thông số lưu trữ
khoiphuc=[0]*sparse_dict["length"]
# ban đầu tất cả đều là 0
# Bây giờ chúng ta khôi phục các vị trí khác 0
#add thêm các giá trị 0 vào
for k,v in sparse_dict.items():
    if k!= "length": # Loại bỏ phần tử cuối cùng
        khoiphuc [k]= v # khôi phục vị trí k giá trị v
print(khoiphuc)

print("\n3. Sắp xếp từ điển")
print("1")
print("Cho từ điển sau:")
registry = {"Shaili": 4, "Chris":90, "Maria":70}
print(registry)

print("\n2")
print(". Sắp xếp từ điển")
# khởi tạo từ điển sau khi được sắp xếp
sapxep={}
# sắp sếp theo key
# đầu tiên lấy hết danh sách key
sapxep_keys=list(registry.keys())
sapxep_keys.sort();
print(sapxep_keys)

print("\n3")
print("sau đó đi tìm value tương ứng")
for k in sapxep_keys:
    sapxep[k]=registry[k]
print(sapxep)

print("\4")
print("Sắp xếp các mục từ điển theo giá trị của chúng:")
# khởi tạo từ điển sau khi được sắp xếp
sapxep={}
# sắp sếp theo key theo giá trị
sapxep_key=sorted(registry, key=registry.get)
print(sapxep_key)

print("\5")
print("sau đó đi tìm value tương ứng")
for k in sapxep_key:
    sapxep[k]=registry[k]
print(sapxep)
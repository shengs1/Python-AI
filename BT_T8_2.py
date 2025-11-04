print("36. Bảo mật cửa hàng trực tuyến")
class Product:
    """Lớp đại diện cho một sản phẩm"""

    #hàm khởi tạo
    def __init__(self, name):
        #khởi tạo
        self.name = name
        self.price = 0
        self.discount = 0
        self.tax_rate = 0

    #--- hàm get/set ------
    def get_price(self):
        #trả giá trị giá về
        return self.price

    def set_price(self, price):
        # đặt giá trị mới
        # để chắc ăn chúng ta nên kiểm tra giá trị đầu vào
            # (1) phải là int hay float
            # (2) phải la số dương
        if isinstance(price, (int,float)) and price > 0:
            self.price = price
        else:
            raise ValueError("Bạn đã nhập sai, Giá phải là một"  "số lớn hơn 0.")

    def set_discount(self):
        #trả giá trị giá về
        return self.discount

    def set_discount(self, discount):
        # đặt giá trị mới
        # để chắc ăn chúng ta nên kiểm tra giá trị đầu vào
            # (1) phải là int hay float
            # (2) phải la số dương
        if isinstance(discount, (int,float)) and 0<discount<self.price:
            self.discount = discount
        else:
            raise ValueError("Bạn đã nhập sai, Giá phải là một"  "số lớn hơn 0.")

    #------phương pháp
    def apply_coupon(self, coupon):
        """Cập nhật discount dựa trên coupon"""
        if coupon == "SAVE4":
            self.discount += 4
            print("Coupon SAVE4 được áp dụng")
        elif coupon == "SUMMER10":
            self.discount += 10
            print("Coupon SUMMER10")
        else:
            print("Coupon của bạn đã được áp dụng")

    def calculate_tax(self,price):
        #tính giá trị tax
        tax=round(price*self.tax_rate,2) #Nhân làm tròn 2 số
        print("Tiền thuê trong số", price, "Coins")
        return tax

def calculate_price(self):
    """Tính số tiền phải trả"""
    # tính số tiền được giảm giá
    discounted_price = self.__price - self.__discount

    # tính tiền thuế trong giá trị được giảm giá trên
    tax = self.__calculate_tax(discounted_price)

    # cộng tiền thuế vào số tiền sau giảm giá
    taxed_price = discounted_price + tax

    return taxed_price


# --- BUILT-IN METHOD ------------
def __str__(self):
    """In các thuộc tính ra"""
    return "Tên: " + self.name

# thiết lập tên sản phẩm
t_shirt = Product("Feel good")
print("Tên áo thun:", t_shirt.name)

# thiết lập giá dùng set và đọc lại giá trị dùng get
print("-> Giá ban đầu")
t_shirt.set_price(30)
print("Giá:", t_shirt.get_price(), "coins")

# thiết lập giảm giá
print("-> Giảm giá")
t_shirt.set_discount(4)
print("Giảm giá:", t_shirt.get_discount(), "coins")

# giá sau khi tính giảm giá và thuế
print("-> Giá sau khi tính giảm giá và thuế")
t_shirt_price = t_shirt.calculate_price()
print("Giá:", t_shirt_price, "coins")

# giá sau khi tính coupon, giảm giá và thuế
print("-> Giá sau khi tính coupon, giảm giá và thuế")
t_shirt.apply_coupon("SAVE4")
t_shirt_price = t_shirt.calculate_price()
print("Giá:", t_shirt_price, "coins")



print("\nBài tập áp dụng")
# 1. Đèn Lux
lamp = Product("Lux")
lamp.set_price(40)
lamp.set_discount(0)
print("Tên sản phẩm:", lamp.name)
print("-> Giá ban đầu (chưa có phiếu giảm giá):")
print("Giá:", lamp.calculate_price(), "coins")

lamp.apply_coupon("SUMMER10")
print("-> Giá sau khi áp dụng phiếu giảm giá SUMMER10:")
print("Giá:", lamp.calculate_price(), "coins")

print("----------------------------------------")

# 2. Bóng bãi biển Giant ball
ball = Product("Giant ball")
ball.set_price(10)
ball.set_discount(0.5)
print("Tên sản phẩm:", ball.name)
print("-> Giá ban đầu (chưa có phiếu giảm giá):")
print("Giá:", ball.calculate_price(), "coins")

ball.apply_coupon("SAVE4")
print("-> Giá sau khi áp dụng phiếu giảm giá SAVE4:")
print("Giá:", ball.calculate_price(), "coins")

print("----------------------------------------")

# 3. Nhật ký My adventures
journal = Product("My adventures")
journal.set_price(15)
journal.set_discount(3)
print("Tên sản phẩm:", journal.name)
print("-> Giá ban đầu (chưa có phiếu giảm giá):")
print("Giá:", journal.calculate_price(), "coins")

journal.apply_coupon("SPRINGSALES30")
print("-> Giá sau khi áp dụng phiếu giảm giá SPRINGSALES30:")
print("Giá:", journal.calculate_price(), "coins")


print("\n37. Làm thế nào để thêm mẫu sách?")
print("Kế thừa")
class Book(Product):
    """Lớp con của Product tên là Book"""

    # khởi tạo
    def __init__(self, name):
        super().__init__(name)
        self.__book_sample = ""

    # ------- khai báo hàm set và get --------
    def get_book_sample(self):
        return self.__book_sample

    def set_book_sample(self, name):
        # kiểm tra tên nhập vào phải chuỗi str không
        if isinstance(name, str):
            self.__book_sample = name
        else:
            raise TypeError("Tên book phải là dạng chuỗi (str)")

    # ------------ methods ------------
    def read_sample(self):
        if self.__book_sample != "":
            print(self.__book_sample + " [...] - Đã có chưa? Mua đi!")
        else:
            print("Book không tồn tại.")

# tạo book
coding_book = Book("Let's code!")

# set giá và giảm giá
coding_book.set_price(20)
coding_book.set_discount(2)

# in các giá trị ban đầu
print("Book tên:", coding_book.name)
print("Giá ban đầu:", coding_book.get_price(), " | Giảm giá:", coding_book.get_discount(), "coins")

# in giá sau cùng (sau giảm giá, coupon, thuế)
print("\nGiá sau khi giảm giá, coupon, và tiền thuế:")
coding_book.apply_coupon("SUMMER10")
print("Giá cuối cùng:", coding_book.calculate_price(), "coins")

# đọc sample
print("\n-> Đang đọc sách:")
coding_book.set_book_sample("Coding is a lot about telling a computer what to do")
coding_book.read_sample()

print("\nBài tập áp dụng")
print("1")
class Product:
    def __init__(self, name):
        self.name = name
        self.__price = 0
        self.__discount = 0
        self.__coupon_discount = 0
        self.__tax_rate = 0.1  # thuế 10%

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_discount(self, discount):
        self.__discount = discount

    def get_discount(self):
        return self.__discount

    def __calculate_tax(self, amount):
        """Tính thuế dựa trên giá trị sau khi giảm"""
        return amount * self.__tax_rate

    def apply_coupon(self, code):
        """Áp dụng mã giảm giá"""
        if code == "SAVE4":
            self.__coupon_discount = 4
        elif code == "SUMMER10":
            self.__coupon_discount = 10
        elif code == "SPRINGSALES30":
            self.__coupon_discount = 30
        else:
            self.__coupon_discount = 0

    def calculate_price(self):
        """Tính tổng giá sau khi giảm và cộng thuế"""
        discounted_price = self.__price - self.__discount - self.__coupon_discount
        if discounted_price < 0:
            discounted_price = 0
        tax = self.__calculate_tax(discounted_price)
        return discounted_price + tax

# Khởi tạo sản phẩm
t_shirt = Product("Feel good")
t_shirt.set_price(30)
t_shirt.set_discount(4)
t_shirt.apply_coupon("SAVE4")

print("Tên sản phẩm:", t_shirt.name)
print("Giá sau khi tính giảm giá và thuế:", t_shirt.calculate_price(), "coins")

# Thử gọi phương thức không tồn tại trong lớp Product
try:
    t_shirt.read_sample()
except AttributeError as e:
    print("\nLỗi:", e)
    print("→ Vì lớp Product không có phương thức read_sample(). "
          "Phương thức này chỉ có ở lớp con (ví dụ: Book).")

print("\n2")
class Vehicle:
    def __init__(self, model, energy_consumption):
        self.model = model
        self.energy_consumption = energy_consumption  # kWh/100km

    def calculate_energy_needed(self, distance):
        """Tính năng lượng cần thiết cho chuyến đi (kWh)."""
        return (self.energy_consumption / 100) * distance


class ElectricCar(Vehicle):
    def __init__(self, model, energy_consumption, battery_capacity):
        super().__init__(model, energy_consumption)
        self.battery_capacity = battery_capacity

    def can_complete_trip(self, distance):
        """Kiểm tra xem xe có đủ pin cho chuyến đi không."""
        energy_needed = self.calculate_energy_needed(distance)
        print(f"\nMẫu xe: {self.model}")
        print(f"  - Mức tiêu thụ: {self.energy_consumption} kWh/100km")
        print(f"  - Dung lượng pin: {self.battery_capacity} kWh")
        print(f"  - Năng lượng cần cho {distance} km: {energy_needed:.1f} kWh")

        if energy_needed <= self.battery_capacity:
            print(f" {self.model} có thể hoàn thành chuyến đi {distance} km.")
        else:
            print(f" {self.model} KHÔNG đủ pin cho chuyến đi {distance} km.")


car1 = ElectricCar("E-Nature", 15, 75)
car2 = ElectricCar("E-Green", 18, 40)
distance = 300

car1.can_complete_trip(distance)
car2.can_complete_trip(distance)


print("\n38. Tùy chỉnh phiếu giảm giá cho thiết bị điện tử")
print("Đa hình")
class Electronics(Product):
    """Lớp con đại diện cho một sản phẩm điện tử"""

    # --------methods----------
    # bây giờ chúng ta chỉ viết để lên phương thức apply_coupon()
    def apply_coupon(self, coupon):

        if coupon == "TECH100":
            self.set_discount(self.get_discount()+10)
            # vì biến discount là private nên bạn phải set và get!
            print("Mã coupon TECH100 được áp dụng!")
        else:
            print("Mã coupon của bạn không có giá trị.")

# thiết lập các thông số
laptop = Electronics("E-notebook")
laptop.set_price(1000)
laptop.set_discount(50)

# Tính toán giá sau khi giảm giá
print("-> Giá sau khi giảm giá")
laptop_price = laptop.calculate_price()
print("Giá:", laptop_price, "coins")

# Giá sau khi áp dụng coupon
print("Giá sau khi tính coupon")
laptop.apply_coupon("TECH100")
laptop_price = laptop.calculate_price()
print("Giá:", laptop_price, "coins")

laptop.apply_coupon("SAVE4")

t_shirt = Product("Feel good")
t_shirt.apply_coupon("SAVE4")
t_shirt.apply_coupon("TECH100")

coding_book = Book("Let's code!")
coding_book.apply_coupon("SAVE4")
coding_book.apply_coupon("TECH100")


print("\nBài tập áp dụng")
# Giá cơ bản cho mọi đơn hàng
base_price = 10  # xu

# Hàm tính giá pizza
def gia_pizza(size):
    if size == "small":
        return base_price
    elif size == "medium":
        return base_price * 1.2  # tăng 20%
    elif size == "large":
        return base_price * 1.5  # tăng 50%
    else:
        raise ValueError("Kích cỡ pizza không hợp lệ")

# Hàm tính giá burger
def gia_burger(them_phomai=False, them_hanh=False):
    price = base_price
    if them_phomai:
        price += 1.5  # thêm phô mai
    if them_hanh:
        price += 1  # thêm hành
    return price

# Tạo các đơn hàng cần kiểm tra
pizza_nho = gia_pizza("small")
pizza_vua = gia_pizza("medium")
pizza_lon = gia_pizza("large")
burger_day_du = gia_burger(them_phomai=True, them_hanh=True)

# In từng đơn và tổng chi phí
print("Pizza nhỏ:", pizza_nho, "xu")
print("Pizza vừa:", pizza_vua, "xu")
print("Pizza lớn:", pizza_lon, "xu")
print("Burger (phô mai + hành):", burger_day_du, "xu")

tong = pizza_nho + pizza_vua + pizza_lon + burger_day_du
print("Tổng chi phí:", tong, "xu")



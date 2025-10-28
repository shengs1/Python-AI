print("1. Lớp, đối tượng và thuộc tính")

class Product:
    '''Lớp đại diện cho một sản phâm'''

    def __init__(self, name):
        self.name = name
        self.price = 0
        self.discount = 0

t_shirt = Product("Feel good")

print("-> Thuộc tính của đối tượng t_shirt khi khởi tạo:")
print("Name:", t_shirt.name)
print("Giá:", t_shirt.price)
print("Discount:", t_shirt.discount)

print("-> Thuộc tính của đối tượng t_shirt sau khi tùy chỉnh:")
t_shirt.price = 30
print("Giá:", t_shirt.price, "coins")
t_shirt.discount = 4
print("Discount:", t_shirt.discount, "coins")

lamp=Product("Lux")
lamp.price=40
print("Tên:", lamp.name)
print("Giá:", lamp.price, "coins")
print("Giảm giá:", lamp.discount, "coins")



print("\n2. Phương thức")
class Product2:
    """Lớp đại diện cho một sản phẩm"""

    #----- Hàm khởi tạo -----
    def __init__(self, name):
        """Khởi tạo thuộc tính của sản phẩm"""
        self.name = name
        self.price = 0
        self.discount = 0

    #----- Phương pháp -----
    def apply_coupon(self, coupon):
        """Cập nhật discount dựa trên coupon"""
        if coupon == "SAVE4":
            self.discount += 4
            print("Coupon SAVE4 ĐƯỢC ÁP DỤNG")
        elif coupon == "SUMMER10":
            self.discount += 10
            print("Coupon SUMMER10 ĐƯỢC ÁP DỤNG")
        else:
            print("Coupon của bạn KHÔNG ĐƯỢC ÁP DỤNG")

    def calculate_price(self):
        """Tính số tiền phải trả"""
        updated_price = self.price - self.discount
        return updated_price

    #----- Built-in method -----
    def __str__(self):
        """In các thuộc tính ra"""
        return f"Tên: {self.name}"

t_shirt = Product2("Feel good")
t_shirt.price = 30
t_shirt.discount = 4

print("Tên:", t_shirt.name, "| Giá ban đầu:", t_shirt.price, "coins. Khuyến mãi:", t_shirt.discount, "coins.")

# Tính toán giá sau khi áp dụng giảm giá
print("-> Giá sau khi áp dụng giảm giá")
t_shirt_price = t_shirt.calculate_price()
print("Giá:", t_shirt_price, "coins.")

# Áp dụng coupon
print("\nÁp dụng coupon")
t_shirt.apply_coupon("SAVE4")
print("Khuyến mãi:", t_shirt.discount, "coins.")

# Tính toán giá sau khi áp dụng coupon
print("-> Giá sau khi áp dụng giảm giá và coupon")
t_shirt_price = t_shirt.calculate_price()
print("Giá:", t_shirt_price, "coins.")


lamp = Product2("Lux")
lamp.price = 40

print("\nGiá ban đầu")
print("Giá:", lamp.price, "coins.")

print("-> Giá sau khi áp dụng Coupon")
lamp.apply_coupon("SUMMER10")
lamp_price = lamp.calculate_price()
print("Giá:", lamp_price, "coins.")


print("\nBài tập áp dụng")
class Product:
    """Lớp đại diện cho một sản phẩm"""

    def __init__(self, name, price, discount):
        """Khởi tạo sản phẩm"""
        self.name = name
        self.price = price
        self.discount = discount

    def apply_coupon(self, coupon):
        """Áp dụng mã giảm giá"""
        if coupon == "SAVE4":
            self.discount += 4
            print("Coupon SAVE4 được áp dụng!")
        elif coupon == "SUMMER10":
            self.discount += 10
            print("Coupon SUMMER10 được áp dụng!")
        elif coupon == "SPRINGSALES30":
            self.discount += 30
            print("Coupon SPRINGSALES30 được áp dụng!")
        else:
            print("Mã coupon không hợp lệ!")

    def calculate_price(self):
        """Tính giá sau khi giảm"""
        final_price = self.price - self.discount
        # Không cho giá âm
        if final_price < 0:
            final_price = 0
        return final_price

    def __str__(self):
        """Hiển thị thông tin sản phẩm"""
        return f"Tên: {self.name}, Giá gốc: {self.price} xu, Giảm giá: {self.discount} xu"


print("Sản phẩm 1: Giant ball")
giant_ball = Product("Giant ball", 10, 0.5)
print(giant_ball)

# Giá trước khi áp dụng coupon
print("Giá trước khi áp dụng coupon:", giant_ball.calculate_price(), "xu")

# Áp dụng mã giảm giá
giant_ball.apply_coupon("SAVE4")
print("Giá sau khi áp dụng coupon:", giant_ball.calculate_price(), "xu\n")


print("\nSản phẩm 2: My adventures")
journal = Product("My adventures", 15, 3)
print(journal)

# Giá trước khi áp dụng coupon
print("Giá trước khi áp dụng coupon:", journal.calculate_price(), "xu")

# Áp dụng mã giảm giá
journal.apply_coupon("SPRINGSALES30")
print("Giá sau khi áp dụng coupon:", journal.calculate_price(), "xu\n")

# In ra đối tượng
print("Thông tin sản phẩm sau cùng:")
print(giant_ball)
print(journal)

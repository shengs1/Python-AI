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


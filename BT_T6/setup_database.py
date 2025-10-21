import random


def create_username(first_name, last_name):
    """
    Tạo username gồm chữ cái đầu của tên và họ, viết thường
    """
    username = first_name[0] + last_name
    username = username.lower()
    return username


def create_password():
    """
    Tạo mật khẩu gồm 4 chữ số ngẫu nhiên
    """
    password = str(random.randint(1000, 9999))
    return password


def create_database(customers):
    """
    Tạo một cơ sở dữ liệu dưới dạng từ điển với username làm khóa và password làm giá trị

    Tham số:
    customers : list
        Danh sách các danh sách con, mỗi danh sách con chứa tên và họ của khách hàng

    Giá trị trả về:
    db : dict
        Cơ sở dữ liệu (từ điển) username -> password
    n_customers : int
        Số lượng khách hàng trong cơ sở dữ liệu
    """
    db = {}

    # Lặp qua từng khách hàng trong danh sách customers
    for khach in customers:
        # Tạo username từ tên và họ
        username = create_username(khach[0], khach[1])
        # Tạo password ngẫu nhiên
        password = create_password()
        # Lưu username và password vào cơ sở dữ liệu
        db[username] = password

    n_customers = len(db)
    return db, n_customers

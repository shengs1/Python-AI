print("33. Quà sinh nhật")
print("1. Đọc tệp .txt")
def read_txt(file_name_in):
    """
    Đọc một tệp .txt có mỗi dòng là một số
    và trả về danh sách các số đó.
    """
    numbers = []

    try:
        with open(file_name_in, "r") as file:
            for line in file:
                line = line.strip()  # Xóa khoảng trắng và ký tự xuống dòng
                if line:  # Bỏ qua dòng trống
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"Bỏ qua dòng không hợp lệ: '{line}'")
    except FileNotFoundError:
        print(f"⚠️ Không tìm thấy tệp '{file_name_in}'.")

    return numbers

purchases = read_txt("purchases.txt")
print(purchases)

print("\n2. Phân tích các số")
def calculate_stats(numbers):
    """
    Tính giá trị nhỏ nhất, lớn nhất và tổng của danh sách số.
    """
    if not numbers:
        return None, None, 0  # Tránh lỗi nếu danh sách rỗng

    min_val = min(numbers)
    max_val = max(numbers)
    total = sum(numbers)

    return min_val, max_val, total


# --- Gọi hàm và in kết quả ---
mi, ma, to = calculate_stats(purchases)
print("Giá trị nhỏ nhất:", mi)
print("Giá trị lớn nhất:", ma)
print("Giá trị tổng:", to)




print("\n3. Lưu phân tích")
def write_txt(file_name_out, min_val, max_val, total):
    """
    Ghi kết quả thống kê (min, max, sum) ra tệp văn bản.
    """
    # ✅ Thêm encoding="utf-8" để ghi được tiếng Việt
    with open(file_name_out, "w", encoding="utf-8") as file:
        file.write(f"Giá trị nhỏ nhất: {min_val}\n")
        file.write(f"Giá trị lớn nhất: {max_val}\n")
        file.write(f"Giá trị tổng: {total}\n")

    print(f" Đã ghi kết quả vào tệp '{file_name_out}' thành công!")

write_txt("purchases_out.txt", mi, ma, to)





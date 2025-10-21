print("31. Giai thừa")
print("1. Hàm đệ quy")
print("1.")
def giai_thua_loop(n):
    # Khởi tạo giai thừa bằng 1
    giai_thua = 1

    # Tính giai thừa từ 2 đến n
    for i in range(2, n + 1):
        giai_thua *= i

    return giai_thua

# Tính giai thừa 4 và in ra kết quả
ket_qua = giai_thua_loop(4)
print(ket_qua)


print("\n2.")
def giai_thua_dequy(n):
    if n > 1:
        return giai_thua_dequy(n - 1) * n
    else:
        return 1

# Tính giai thừa 4 và in ra kết quả
ket_qua = giai_thua_dequy(4)
print(ket_qua)

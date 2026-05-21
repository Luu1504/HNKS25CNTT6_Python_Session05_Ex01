initial_price = int(input("Nhập số tiền ban đầu: "))

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")

if initial_price > 500000:
    total_price = initial_price * 0.1
else:
    total_price = initial_price
print(f"Tổng số tiền khách phải trả là: {total_price}")

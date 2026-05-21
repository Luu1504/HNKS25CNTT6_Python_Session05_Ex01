branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

# LỖI CODE CŨ: Đặt vòng lặp tháng ở ngoài và vòng lặp chi nhánh ở trong làm đảo lộn thứ tự nhập liệu
# KHẮC PHỤC: Đưa vòng lặp chi nhánh ra ngoài để cố định từng chi nhánh trước
for i in range(1, branch_count + 1):
    # KHẮC PHỤC: Đưa vòng lặp tháng vào trong để chạy lần lượt từ tháng 1 đến tháng 3 cho chi nhánh đó
    for j in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {i}, tháng {j}: "))

print("\n-------------- Kết quả --------------")

# LỖI CODE CŨ: Tiếp tục sai trật tự vòng lặp hiển thị khiến dữ liệu bị xé lẻ theo tháng
# KHẮC PHỤC: Đảo vòng lặp chi nhánh ra ngoài cùng để gom dữ liệu theo từng chi nhánh khi in báo cáo
for i in range(1, branch_count + 1):
    # KHẮC PHỤC: Vòng lặp tháng nằm trong để in lần lượt các tháng của chi nhánh đang được chọn
    for j in range(1, month_count + 1):
        # LỖI CODE CŨ: Viết thừa ký tự f trong chuỗi biến: "f"{revenue} triệu đồng" khiến Python in ra cả chữ f
        # KHẮC PHỤC: Loại bỏ chữ f dư thừa để hiển thị con số chính xác
        print(f"Chi nhánh {i}, tháng {j}: {revenue} triệu đồng")
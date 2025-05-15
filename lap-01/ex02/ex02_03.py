#Nhập số từ người dùng
so = input("Nhập một số nguyên: ")
#Kiể m tra xem số đó có phải là số chẵn hay không
if int(so) % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải số chẵn.")
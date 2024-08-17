N=int(input("Nhập vào một số nguyên dương: "))  
if N>0:  
    i=1  
    while i<=10:  
        print(f"{N}x{i}={N*i}")  
        i+=1  
else:  
    print("Số không hợp lệ. Vui lòng nhập một số nguyên dương.")

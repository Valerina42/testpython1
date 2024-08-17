n=int(input("Nhập một số nguyên dương:"))  
tong=0
print("Các số chẵn từ 0 đến",n,"là:")  
for i in range(n+1):  
    if i%2==0:  
        print(i)  
        tong+=i  
print("Tổng các số chẵn là:",tong)

# Find GCD (HCF) of Two Numbers  12, 18 → 6

a=int(input("enter a number:"))
b=int(input("enter a second number"))
for i in range(min(a,b),0,-1):
    if a%1==0 & b%i==0:
        print("gcf=",i)
        break


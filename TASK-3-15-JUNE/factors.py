#  Find Factors of a Number       12 → 1, 2, 3, 4, 6, 12 

n=12
for i in range(1,n+1):
    if n%i==0:
     print(i,end=" ")
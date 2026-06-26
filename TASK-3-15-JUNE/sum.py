
# 1........ | Sum of Digits                  1234 → 10 
n=1234
sum=0
while(n>0):
    temp=n%10
    sum=sum+temp
    n//=10
print(sum)

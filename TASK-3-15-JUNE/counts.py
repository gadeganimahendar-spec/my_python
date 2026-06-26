# Count Digits in a Number       12345 → 5
n=12345
count=0
while(n>0):
    temp=n%10
    count+=1
    n//=10
print(count)    

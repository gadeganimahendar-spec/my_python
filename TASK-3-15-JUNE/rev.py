#  Reverse a Number               1234 → 4321 
n=1234
val=0
while(n>0):
    temp=n%10
    val=val*10+temp
    n//=10
print(val,end="")

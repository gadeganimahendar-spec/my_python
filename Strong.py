
# Find length of number 3   
#    separate each number 1,5,3   
#    1 power length of number    
#    sum    
#    check condition 

n=153
m=str(n)
lenth=len(m)
res=0
x=n

while(n>0):
    pow=0
    temp=n%10
    pow=temp**lenth
    res=res+pow
    n=n//10
if(res==x):
    print(" is  a strong number")
else:
    ("not  strong number")

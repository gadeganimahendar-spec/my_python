# Check Armstrong Number         153 → Armstrong
n=input("enter  a number:")
s=0
for i in n:
    g=s+int(i)**len(n)
if s==int(n):
    print("is armstrong")
else:
    print("not a armstrong")

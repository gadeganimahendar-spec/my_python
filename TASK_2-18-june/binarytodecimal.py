s="1011"
n=len(s)-1
d=0
for i in range(len(s)):
    d=d+int(s[i])*(2**(n-i))
print(d)    



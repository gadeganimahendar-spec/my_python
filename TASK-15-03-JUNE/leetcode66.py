# leetcode -66
l=[1,2,3]
total=0
for i in l:
    total=(total*10)+i
total+=1
t=[]
for i in str(total):
     t.append(int(i))
print(t)
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
l3=[]
for i in range (len(l1)):
    l=[]
    for j in range(len(l1[i])):
        add=0
        for k in range(len(l1[i])):
            add=add+(l1[i][k]*l2[k][j])
        l.append(add)
    l3.append(l)  

for i in range(len(l3)):
    for j in range(len(l3[i])):
        print(l3[i][j],end=" ") 
    print() 

print("hello")
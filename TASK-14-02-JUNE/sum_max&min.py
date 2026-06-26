
# length of list
l=[1,2,3,4,5]
length=0
for i in l:
    length+=1
print(length)

#  sum of list
l=[1,2,3,4,5]
sum=0
for i  in l:
    sum+=i
print(sum)

# product of list
l=[1,2,4,6]
product=1
for val in l:
    product=product*val
print(product)

# max of list
l=[1,5,9,3]
max1=l[0]
for i in range(1,len(l)):
    if max1<l[i]:
        max1=l[i]
print(max1)

# min of list
l=[1,2,3,4,5]
min1=l[0]
for i in range(1,len(l)):
    if min1>=l[i]:
        min1=l[i]
print(min1)

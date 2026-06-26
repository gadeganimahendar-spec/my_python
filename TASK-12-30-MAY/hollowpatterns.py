'''square hallow rattern'''
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or j==n-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
print("==========================================")
'''right hallow triangle'''
n=5
for i in range(n):
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("==========================================")
n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()


print("=======================================")

''' reverse right hallow triangle'''
n=5
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("==============================")
'''
*
* *
*  *
*   *
*  *
* *
*
'''

n=5
for i in range(n):
    for j in range(i+1):
        if(j==0 or j==i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(i+1):
        if(j==0 or j==i):
            print("*", end=" ")
        else:
            print(" " , end=" ")
    print()

print("==================================")

'''piramid pattern'''

n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print("*", end=" ")
    print()

print("==========================")

'''hallow priamid pattern'''
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print("==================================")

'''left angle triangle'''

n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        if(j==0 or i==n-1 or j==i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
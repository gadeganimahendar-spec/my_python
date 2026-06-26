# print("square patterns===========================")
n=5
m=5
for i in range(n):
     for j in range(m):
         print("*",end=" " )
     print()

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# [right angle triangel=============================]

n=5
for i in range(n):
    for j in range(i+1):
        if(i==i or j==j or i==n-1 ):
            print("*",end=" ")
    print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")           



# number triangel
n=5
for i  in range(n):
    for j in range(1,i+1):
        if(i==1 or j==j):
            print(j,end=" ")
    print()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    

# print("repeated triangle")
n=5
for i in range(n):
    for j in range(1,i+1):
        if(i==i or j==j ):
            print(i,end=" ")
    print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  

# alphabet triangele 


n=5
for  i in range(n):
 val=65
 for j in range(1,i+1):
    if(i==i or j==j):
       print(chr(val),end=" ")
       val+=1
 print()     

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# inverted star triangle
n=5
for i in range(n,-1 ,-1):
    for j in range(i+1):
        if( i==i or j==j ):
            if(i+1):
             print("*",end=" ")
            else:
                 print("*",end=" ")
    print()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # inverted number triangle

n=5
for i  in range(n,0,-1):
        for j in range(1,i+1):
            if(i==j or j==j):
                if(i+1):
                 print(j,end=" ")
        print()
            

#    continous number  pattern

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
n=5 
num=0
for i  in range(n):
    for j in range(1,i+1):
        if(i==1 or j==j):
            num+=1
            print(num,end=" ")
    print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")

    # right -aligned star triangle
     
n=5
for i in range(1,i+1):
    for j in range(n-i):
      print(" ",end=" ")
    for i  in range(i):
      print("*",end=" ")

    print()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # pyramid pattern
n=5
for i  in range (n):
    for j  in range(n-i):
       print(" ",end="")
    for j in range(i+1):
       print("*",end=" ")

    print()
                     

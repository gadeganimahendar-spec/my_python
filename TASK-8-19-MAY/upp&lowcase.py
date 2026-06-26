# 1.  Print given value is positive or not  Given char(n) is upper case or lower case(without using built in function)  Pass or fail(have 6subject) eg:s1>35 c
chr=input("enter the words:")
if "A" <= chr <="Z":
    print("upper case")
elif "a" <= chr <="z":
    print("lower case")
else:
    print("not a alphabet")
 
#  Print given value is positive or not 
n=int(input("enter a number:"))
if n>0:
    print("positive number")
else:
    print("not a positive")


 # Pass or fail(have 6subject)
n=int(input("enter 1st subject marks:"))
n=int(input("enter 2nd subject marks:"))
n=int(input("enter 3rd subject marks:"))
n=int(input("enter 4th subject marks:"))
n=int(input("enter 5th subject marks:"))        
n=int(input("enter 6th subject marks:"))
if n>35:
    print("pass")
else:
    print("fail")

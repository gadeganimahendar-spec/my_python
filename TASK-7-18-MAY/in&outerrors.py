# 1..input errror
# a.value error
age=int(input("enter the age:"))

# input=abc
# error =value error:invalid literal for int


# b. EOF(end of file) error
name=input('enter name:')

# input=text
# error=eof when raeding a line



# 2..output error
# a.type NameError
age=20
print("age="+age)

# error=can only concatenate str(not"int")to str

# b.error handling examples
try:
    num=int(input("enter a number:"))
    print("number:",num)
except ValueError:
    print("invalid input")
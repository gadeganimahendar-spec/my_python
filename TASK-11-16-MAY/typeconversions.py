# # type convertions
# int to int
x=10
print(int(x))
print(type(x))

#int to str
x=10
print(str(x))
print(type(x))

#int to float
x=10
print(float(x))
print(type(x))

#int to complex
x=10+3j
print(complex(x))
print(type(x))

# float to float
x=10.0
print(float(x))
print(type(x))

#float to int
x=22.0
print(int(x))
print(type(x))

#float to str
x=33.0
print(str(x))
print(type(x))

#float to complex
x=33.0
print(complex(x))
print(type(x))

# str to str
x="siri"
print(str(x))
print(type(x))

#str to int

#here convertion string to int or float the string must should be in the form  base of 10 or decimal number
 
x="10000"
print(int(x))
print(type(x))

# str to float
x="1000.0"
print(float(x))
print(type(x))

# str to complex

# here convertion string to complex the string must should be in the form  complex number
 
x="3+5j"
print(complex(x))
print(type(x))

# com to com
x=3+5j
print(complex(x))
print(type(x))

# com to str
x=3+5j
print(str(x))
print(type(x))

#comp to float
# here int() and float() argument must be a string or a real number, not 'complex'
x=3+5j
print(float(x.real))
print(type(x))

# comp to int
x=3+5j
print(int(x.real))
print(type(x))
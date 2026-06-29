'''Write a program to find the area of a rectangle.
Write a program to find the area of a square.
Write a program to find the area of a triangle.
Write a program to find the area of a circle.
Write a program to find the area of a parallelogram.
Write a program to find the area of a rhombus.
Write a program to find the area of a trapezium.
Write a program to find the area of an equilateral triangle.
Write a program to find the area of a sector of a circle.
Write a program to find the area of a semicircle.
Perimeter Problems
Write a program to find the perimeter of a rectangle.
Write a program to find the perimeter of a square.
Write a program to find the circumference of a circle.
Write a program to find the perimeter of a triangle.
Write a program to find the perimeter of a parallelogram.
Write a program to find the perimeter of a rhombus.
Write a program to find the perimeter of a regular pentagon.
Write a program to find the perimeter of a regular hexagon.
Write a program to find the perimeter of a trapezium.
Write a program to find the perimeter of an equilateral triangle.
Cube Problems
Write a program to find the volume of a cube.
Write a program to find the total surface area of a cube.
Write a program to find the lateral surface area of a cube.
Write a program to find the cube of a given number.
Write a program to check whether a number is a perfect cube.
Write a program to find the sum of cubes of two numbers.
Write a program to find the difference of cubes of two numbers.
Write a program to print cubes from 1 to N.
Write a program to find the cube root of a number.
Write a program to find the largest cube less than or equal to N.'''

#area of rectangle
l=5
b=3
area=l*b
print("Area of rectangle is:", area)
#area of square
s=4
area=s*s
print("Area of square is:", area)
#area of triangle
b=4
h=5
area=0.5*b*h
print("Area of triangle is:", area)
#area of circle
r=7
PI=3.14
area=PI*r*r
print("Area of circle is:", area)
#area of a parallelogram
b=6
h=4
area=b*h
print("Area of parallelogram is:", area)
#area of a rhombus
d1=8
d2=5
area=0.5*d1*d2
print("Area of rhombus is:", area)
#area of a trapezium
a=3
b=5
h=4
area=0.5*(a+b)*h
print("Area of trapezium is:", area)
#area of an equilateral triangle using fromula (sqrt(3)/4)*s^2
from math import sqrt
s=6
area=(sqrt(3)/4)*s*s
print("Area of equilateral triangle is:", area)
#area of a sector of a circle
r=5
theta=60
area=(theta/360)*PI*r*r
print("Area of sector of a circle is:", area)
#area of a semicircle
r=4
area=0.5*PI*r*r
print("Area of semicircle is:", area)



#perimeter problems
#perimeter of rectangle
l=5
b=3
perimeter=2*(l+b)
print("Perimeter of rectangle is:", perimeter)
#perimeter of square
s=4
perimeter=4*s
print("Perimeter of square is:", perimeter)
#perimeter of triangle
a=3
b=4
c=5
perimeter=a+b+c
print("Perimeter of triangle is:", perimeter)
#perimeter of parallelogram
a=6
b=4
perimeter=2*(a+b)
print("Perimeter of parallelogram is:", perimeter)
#perimeter of rhombus
s=5
perimeter=4*s
print("Perimeter of rhombus is:", perimeter)
#perimeter of pentagon
s=7
perimeter=5*s
print("Perimeter of pentagon is:", perimeter)
#perimeter of hexagon
s=8
perimeter=6*s
print("Perimeter of hexagon is:", perimeter)
#perimeter of trapezium
a=3
b=5
c=4
d=6
perimeter=a+b+c+d
print("Perimeter of trapezium is:", perimeter)
#perimeter of a equilateral triangle
s=6
perimeter=3*s
print("Perimeter of equilateral triangle is:", perimeter)



#cube problems
#volume of a cube
s=4
volume=s**3
print("Volume of cube is:", volume)
#surface area of a cube
s=4
surface_area=6*s**2
print("Surface area of cube is:", surface_area)
#lateral surface area of a cube
s=4
lateral_surface_area=4*s**2
print("Lateral surface area of cube is:", lateral_surface_area)
#cube of a given number
n=3
cube=n**3
print("Cube of", n, "is:", cube)
#write a program to check whether a number is a perfact cube
n=27
cube_root=n**(1/3)
if cube_root**3==n:
    print(n, "is a perfect cube.")
else:
    print(n, "is not a perfect cube.")
    
#write a program to find the sum of cubes of two numbers
a=2
b=3
sum_of_cubes=a**3 + b**3
print("Sum of cubes of", a, "and", b, "is:", sum_of_cubes)
#write a program to find the difference of cubes of two numbers
a=5
b=2
difference_of_cubes=a**3 - b**3
print("Difference of cubes of", a, "and", b, "is:", difference_of_cubes)
#write a program to print cubes from 1 to n
n=10
print("Cubes from 1 to", n, "are:")
for i in range(1, n+1):
    print(i**3)
#write a program to find the cube root of a number
n=27
cube_root=n**(1/3)
print("Cube root of", n, "is:", cube_root)
#write a program to find the sum of cubes of first n natural numbers
n=5
sum_of_cubes=0
for i in range(1, n+1):
    sum_of_cubes += i**3
print("Sum of cubes of first", n, "natural numbers is:", sum_of_cubes)





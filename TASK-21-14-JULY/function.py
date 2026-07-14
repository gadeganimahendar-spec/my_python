         

# 3d shapes
    
def shapes(symbol):
    def cube(a,b,c):
        return  a*a*a
    def cuboid(a,b,c):
        return a*b*c
    def cylinder(a,b):
        return  3.14*a**2*b
    def sphere (a):
        return 3/4*3.14*a**3
    def prism(a,b):
        return a*b
    match (symbol):
        case  "cube":
            a=int(input("enter the a value:"))
            a=int(input("enter the a value:"))
            a=int(input ("enter the a value:"))
            return a*a*a
        case "cuboid":
            a= int(input("enter length  value:"))
            b=int(input("enter width value: "))
            c=int(input( "enter breadth value:")) 
            return a*b*c
        case "cylinder ":
            a=int(input("enter raduis value: "))
            b= int(input("enter heifht value:"))
            return 3.14*a**2*b
        case "sphere":
            a=int(input("enter radius value"))
            return 3/4*3.14*a**3
        case "prism":
            a=int(input("enter base value: "))
            b= int(input("enter height value:"))
            return a*b

symbol=input("enter the  symbol:")
print(shapes(symbol))         
            

    
  

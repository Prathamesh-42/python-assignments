import shapes

print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice=int(input("Enter your choice: "))

if choice==1:
    r=float(input("enter radius: "))
    print("Area of circle=",shapes.circle_area(r))

elif choice==2:
    l=float(input("Enter length: "))
    w=float(input("Enter width: "))
    print("Area of rectangle=",shapes.rectangle_area(l,w))

elif choice==3:
    b=float(input("Enter base: "))
    h=float(input("Enter height: "))
    print("Area of triangle=",shapes.triangle_area(b,h))

else:
    print("INVALID")        
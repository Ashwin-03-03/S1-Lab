# WAP to find the area and perimeter of circle where the radius is input by the user.

def areaAndPerimeterOfCircle():
    import math
    PI = math.pi
    radius = int(input("Enter the radius of the circle: "))
    area = PI * radius * radius
    perimeter = 2 * PI * radius
    print(f"Area of the circle is: {area:.3f} cm²")
    print(f"Perimeter of the circle is: {perimeter:.3f} cm")
    
areaAndPerimeterOfCircle()
    
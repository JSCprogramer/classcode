import math

def circlmath():
    r=float(input("Enter the radius of your circle: "))
    A=math.pi*r**2
    C=2*math.pi*r
    print(f"the area of your cricle is {A:.2f}")
    print(f"the circumference of your cricle is {C:.2f}")
circlmath()
def rec():
    leng=float(input("Enter the length of the rectangle: "))
    width=float(input("Enter the width of the rectangle: "))
    P=2*(leng+width)
    A=leng*width
    print(f"the area of your rectangle is {A}")
    print(f"the perimeter of your rectangle is {P}")

rec()

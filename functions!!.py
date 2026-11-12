


def odd(num): #first try works but could be better
    if num % 2==0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
        
odd(int(input("Enter a number to determin if its odd or even: ")))


def bet(): #Put the input inside of the function for muti time use
    num=int(input("Enter a number to determin if its odd or even: "))
    if num % 2==0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")
bet()
limit = int(input('Enter a number: '))
Sum = 0
number = 1

while number <= limit:
    Sum += number
    number += 1

print('Sum of numbers from 1 to', limit, "is:", Sum)

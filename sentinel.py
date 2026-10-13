sentinel = "exit"
user_input = input("Enter a value (or 'exit' to quit): ")

while user_input != sentinel:
    print("You entered:", user_input)
    user_input = input("Enter another value (or 'exit' to quit):")
print('loop exited.')

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    should_continue = True
    user__num_input1 = input('Enter a number: ')
    
    while should_continue:
        user_num_input2 = input('Enter another number: ')
        for operation in operations:
            print(operation)
        
        user_operation = input('Enter your operation: ')
        result = operations[user_operation](float(user__num_input1), float(user_num_input2))
        print(f"{user__num_input1} {user_operation} {user_num_input2} = {result}")
        
        while True:
            choice = input('Would you like to do another operation? (y/n): ').lower()
            if choice in ('y', 'n'):
                break
            print("Invalid input! Please enter 'y' for yes or 'n' for no.")
        
        if choice == 'y':
            user__num_input1 = result
        else:
            print('Thank you for using the calculator!')
            should_continue = False

calculator()

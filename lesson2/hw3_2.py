while True: # first number
    first_number = input('Enter first number! ')

    try:
        first_number = float(first_number)
        break       
    
    except ValueError:
        print(f'Number {first_number} is not a number')

while True: # second number
    second_number = input('Enter second number! ')

    try:
        second_number = float(second_number)
        break       
    
    except ValueError:
        print(f'Number {second_number} is not a number')


while True: # enter operators
    operation = input('Enter operation (*, /, +, -)! ')

    if operation == '*': # multiplication
        result = first_number * second_number
        break
    
    elif operation == '/': # division
        try:
            result = first_number / second_number
            break
    
        except ZeroDivisionError:
            print('You cannot divide by zero!')
            break

    elif operation == '+': # amount
        result = first_number + second_number
        break
            
    elif operation == '-': # difference
        result = first_number - second_number
        break

    else:
        print(f'Operation {operation} not fit!')
        
while True: # example solution

    if operation == '/' and second_number == 0:
        break
    
    else:
        equality_derivation = input('Input "="! ')
        if equality_derivation == '=':
            equality_derivation = result
            print(equality_derivation)
            break

        else:
            print('Something is wrong! Try again.')

print('Thank You!')

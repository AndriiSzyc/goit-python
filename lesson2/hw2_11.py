second_number = None
while True: # first_number
    first_number = input('Enter first number! ')

    if first_number == '=':
        break

    try:
        first_number = float(first_number)
        break

    except ValueError:
            print(f'Number {first_number} is not a number')

if first_number == '=':
    print('Thank You!')

elif first_number != '=':

    while True: # operation
        if second_number == '=':
            break
        
        operation = input('Enter operation (*, /, +, -)! ')
        elif operation == '=':
            break
        elif operation == '*':
            
            second_number = input('Enter second number! ')
            if second_number == '=':
                break
            
            try:
                second_number = float(second_number)
                result = first_number + second_number
                print(result)
                first_number = result
                    
            
            except ValueError:
                print(f'Number {second_number} is not a number')
                continue
            
        elif operation == '/':
            second_number = input('Enter second number! ')
            if second_number == '=':
                break
            try:
                second_number = float(second_number)
                result = first_number / second_number
                print(result)
                first_number = result

            except ValueError:
                print(f'Number {second_number} is not a number')
                continue
        
            except ZeroDivisionError:
                print('You cannot divide by zero!')
                continue
        elif operation == '+':
            second_number = input('Enter second number! ')
            if second_number == '=':
                break
            try:
                second_number = float(second_number)
                result = first_number + second_number
                print(result)
                first_number = result
            
            except ValueError:
                print(f'Number {second_number} is not a number')
                continue
        elif operation == '-':
            second_number = input('Enter second number! ')
            if second_number == '=':
                break
            try:
                second_number = float(second_number)
                result = first_number - second_number
                print(result)
                first_number = result
            
            except ValueError:
                print(f'Number {second_number} is not a number')
                continue
        else:
            print(f'Operation {operation} not fit!')
            continue

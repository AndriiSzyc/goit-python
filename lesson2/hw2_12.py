first_number = input('Enter first number! ')
second_number = None
operation = None
while type(first_number) != float:
    
    if first_number == '=':
        break
    try:
        first_number = float(first_number)
        break

    except ValueError:
        print(f'Number {first_number} is not a number')
        first_number = input('Enter first number! ')

  
while type(first_number) == float:
    if second_number == '=' or operation == '=':
        break

    while True:
        second_number = input('Enter second number! ')

        if second_number == '=':
            break
        try:
            second_number = float(second_number)
            break

        except ValueError:
            print(f'Number {second_number} is not a number')

    while type(second_number) == float or second_number  != '=':
        operation = input('Enter operation (*, /, +, -)! ')

        if operation == '*':    
            result = first_number * second_number
            print(result)
            first_number = result
            break
            
        elif operation == '+':
            result = first_number + second_number
            print(result)
            first_number = result
            break

        elif operation == '-':
            result = first_number - second_number
            print(result)
            first_number = result
            break

        elif operation == '/':
            try:
                result = first_number / second_number
                print(result)
                first_number = result
                break
            
            except ZeroDivisionError:
                print('You cannot divide by zero!')

                
        elif operation == '=':
            break

        else: 
            print(f'Operation {operation} not fit!')
            continue    



print('Thank You!')


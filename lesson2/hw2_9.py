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

    while True:
        second_number = input('Enter second number! ')
        
        if second_number == '=':
            break
        try:
            second_number = float(second_number)
            while True:
                
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
            
        
        except ValueError:
            print(f'Number {second_number} is not a number')

  
                
    
print('Thank You!')

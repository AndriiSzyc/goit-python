while True:
    while True: # first number
        first_number = input('Enter first number! ')

        if first_number == '=':
            break

        try:
            first_number = float(first_number)
        
            while True: # second number

                second_number = input('Enter second number! ')
                if second_number == '=':
                    break
                try:
                    second_number = float(second_number)
                    break       
    
                except ValueError:
                    print(f'Number {second_number} is not a number')       
            break
        except ValueError:
            print(f'Number {first_number} is not a number')
    
    if first_number == '=' or second_number == '=':
        break   

    elif first_number and second_number == int or float:
        while True:
            operation = input('Enter operation (*, /, +, -)! ')
            
  
            if operation == '*':
                result = first_number * second_number
                print(result)
                break

            elif operation == '/': # division
                try:
                    result = first_number / second_number
                    print(result)
                    break
                    
                
                except ZeroDivisionError:
                    print('You cannot divide by zero!')
                    break
            
            elif operation == '+': # amount
                result = first_number + second_number
                print(result)
                break

            elif operation == '-': # difference
                result = first_number - second_number
                print(result)
                break
            elif operation == '=':
                continue

            else: 
                print(f'Operation {operation} not fit!')
                continue
    

print('Thank You!')

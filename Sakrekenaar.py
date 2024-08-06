# Function that adds two numbers
def add(a, b):
    return a + b

# Function that subtracts two numbers
def subtract(a, b):
    return a - b

# Function that multiplies two numbers
def multiply(a, b):
    return a * b

# Function that divides two numbers
def divide(a, b):
    return a / b

print('Calculator.')
print('')
print('1 - Add')
print('2 - Subtract')
print('3 - Multiply')
print('4 - Divide')
print('Enter \'x\' to exit the program at anytime.')
print('-------------------------------------------')

while True:
    # Take user input
    user_input = input("Enter your choice (1, 2, 3, or 4): ")
    
    #perform calculation based on users choice and make sure it is an integer or float.
    if user_input in ('1', '2', '3', '4'):
        while True:
            try:
                input1 = float(input('Enter first number: '))
                break
            except ValueError:
                # Verify that input is not a letter.
                print('Please enter a valid number.')
        
        while True:
            try:
                input2 = float(input('Enter second number: '))
                break
            except ValueError:
                # Verify that input is not a letter.
                print('Please enter a valid number.')

        # If and elif statements to execute based on user choice
        if user_input == '1':
            print(input1, '+', input2, '=', add(input1, input2))
        elif user_input == '2':
            print(input1, '-', input2, '=', subtract(input1, input2))
        elif user_input == '3':
            print(input1, '*', input2, '=', multiply(input1, input2))
        elif user_input == '4':
            print(input1, '/', input2, '=', divide(input1, input2))
    #elif statement to check when user enters 'x' to exit loop anytime(Sentinel variable)
    elif user_input.lower() == 'x':
        print('Goodbye!')
        break
    #else statement if user input is not one of the provided.
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 'x' to exit.")
        continue

    # Ask for user input to continue or exit
    continue_or_end = input('Do you want to do another calculation? (\'x\' to Exit. Enter any other input to continue): ')
    
    # User input 'x' will break the loop and any other input will let the calculaion continue
    if continue_or_end.lower() == 'x':
        print('Goodbye!')
        break
    else: 
        continue
            
    


  
        
   
            
   

    




  
    
    

    

   









    



    














    



    
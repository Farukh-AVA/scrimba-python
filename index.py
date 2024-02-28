print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculator(num_1 = 0, num_2 = 0, operator=""):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2    
    elif operator == "/":
        return num_1 / num_2
    else:
        return num_1*9/5 +32 
        
        
num_1 = input('Please enter num 1: ')
num_2 = input('Please enter num 2: ')
operator  = input('Please enter operator') 
        
result = calculator(int(num_1), int(num_2), operator)           
print(result)

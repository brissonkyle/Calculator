from error_object import CalculatorInputError
from helpers.addition_module import add
from helpers.subtraction_module import subtract
from helpers.multiplication_module import multiply
from helpers.division_module import divide



print('Welcome to my Calculator, Please select an option : ')
print('1 Add :')
print('2 Subtract :')
print('3 Multiply :')
print('4 Divide :')
selection = int(input('You choose :'))
num1 = int(input('Please Enter First Number :'))
num2 = int(input('Please Enter Second Number :'))
CalculatorInputError


try :
    num1 = str(num1)
    num2 = str(num2)
except CalculatorInputError:
    print(CalculatorInputError)

if selection == 1 :
    print(add(num1,num2))
elif selection == 2 :
    print(subtract(num1,num2))
elif selection == 3 :
    print(multiply(num1,num2))
elif selection == 4 :
    print(divide(num1,num2))



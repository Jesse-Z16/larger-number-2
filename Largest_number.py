# Find the largest number out of the 3 entered

number1 = int(input('Enter the 1st number:'))
number2 = int(input('Enter the 2nd number:'))
number3 = int(input('Enter the 3rd number:'))

if (number1 == number2) and (number1 == number3):
    print('The largest number is',number1)
    
elif (number1 > number2) and (number1 > number3):
    print('The largest number is',number1)
    
elif (number2 > number1) and (number2 > number3):
    print('The largest number is',number2)
    
elif (number3 > number1) and (number3 > number2):
    print('The largest number is',number3)
    

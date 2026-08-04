#simple Calculator
choice = input('Choose operator (+,-,*,/,%,):')
n1 = int(input('Enter a 1st number :'))
n2 = int(input('Enter a 2nd number :'))

if choice == '+':
    add = n1+n2
    print('Addition:',add)
if choice == '-':
    sub = n1-n2
    print('Substraction:',sub)
if choice == '*':
    multi = n1*n2
    print('Multiplication:',multi)

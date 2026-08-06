#ATM transcition
pin=1397
i=1
while i<=3:
    my_pin=int(input('Enter a number :'))
    if my_pin == pin:
        print('Valid pin')
    else:
        print('Invalid Pin')
    i=i+1

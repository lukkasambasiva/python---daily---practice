#movie ticket
age = int(input('Enter age:'))
if age<13:
    print('child ticket')
elif age>13 and age<59:
    print('Adult ticket')
else:
    print('Citizen Ticket')



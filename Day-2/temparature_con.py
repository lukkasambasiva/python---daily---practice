# converts celius to fahrenheeit
'''step1:remember the user choice
step2:remember a temparature
step3:convert a c to f
step4:cocverts a f to c
step5:disply the result'''

choice =str(input('Enter  convert choice (CtoF/FtoC):'))
temp =float(input('Enter Temperature:'))

if choice =="CtoF":
    fah_conv =(temp*9/5)+32
    print('Fahrenheit:',fah_conv)
elif choice=="FtoC":
    cel_conv=(temp-32)*5/9
    print('celsius:',cel_conv)
else:
    print('invalid Output')

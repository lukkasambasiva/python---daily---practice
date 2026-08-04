a#time sheet

hours = int(input('Enter a working hours :'))

if hours<16:
    if hours<=8:
        wage = hours*100
    elif hours<=10:
        wage = 8*100+(hours-10)*200
    elif hours<=12:
        wage = 8*100+2*200+(hours-12)*400
    else:
        wage = 8*100+2*200+2*400+(hours-12)*500
    print('Erned Your money:',wage)
else:
    print('Invalid Time')

#sum of the digits in a given number
num=int(input('enter a number:'))
while True:
    s=0
    while num>0:
        d = num%10
        s=s+d
        num = num//10
    if s>9:
        num=s
    else:
        print(s)
        break


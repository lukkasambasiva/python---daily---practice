#GCD
n1=int(input('Enter a number :'))#48
n2=int(input('Enter a number :'))#18
if n1>n2:
    big=n1
else:
         big=n2
     
d=big
while d>=1:
    if n1%d==0 and n2%d==0:
        print('GCD',d)
        break
    d=d-1
else:
    print('not GCD')
    

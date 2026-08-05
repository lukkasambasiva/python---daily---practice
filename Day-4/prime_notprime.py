num = int(input('Enter a number :'))
d=2
while d<=num//2:
       if num%d==0:
          print('Not prime')
          break
       d=d+1
else:
    print(' prime')

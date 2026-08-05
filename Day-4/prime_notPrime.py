#prime or not prime
num=int(input('Enter a number :'))
d=1
count=0
while d<=num:
    if num%d == 0:
     count = count+1

    d=d+1
if count==2:
    print('Prime')
else:
    print('Not prime')

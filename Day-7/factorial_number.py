#factoiral of a given number
num=int(input('Enter a number :'))
f=1
while num>=1:
    
    f*=num
    num-=1
print(f)

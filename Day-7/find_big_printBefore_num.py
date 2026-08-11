#find the biggest number but print before number
num=int(input('Enter a number :'))
big=0
second=0
while num>0:
    d=num%10
    if d>big:
        second =big
        big=d
    elif d>second:
        second=d
    num//=10
print(big)
print(second)

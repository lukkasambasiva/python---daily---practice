#factorial of 1 to n numbers
num=int(input('Enter a number :'))
i=1
f=1
while i<=num:
    f*=i
    print(i)
    i+=1
print(f)

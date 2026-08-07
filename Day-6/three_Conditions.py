num =int(input('Enter a number :'))
i=1
c=0
while i<=num:
    if i%2==0 and i%3!=0 and i%5==0:
        c=c+1

    i=i+1
print(c)

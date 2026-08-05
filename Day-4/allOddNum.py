#all odd numbers amd divisible by 7
num = int(input('Enter a number :'))
i=1
s=0
while i<=num:
    if i%2!=0 and i%7==0:
        s=s+i
    i=i+1
print(s)
        

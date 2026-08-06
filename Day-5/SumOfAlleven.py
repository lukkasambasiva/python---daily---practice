#sum of all even numbers
num=int(input('Enter a number :'))
i=1
s=0
while i<=num:
     if i%2==0:
         s=s+i

     i=i+1
print(s)

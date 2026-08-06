#sum of all numbers divisible by 4
num=int(input('Enter a number :'))
i=1
s=0
while i<=num:
    if i%4==0:
      s=s+i
    
        
    i=i+1
print(s)

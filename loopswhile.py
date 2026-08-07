num =int(input('Enter a number:'))#123
cnt=0
original=num
while num>0:
    d=num%10
    cnt=cnt+1
    num=num//10
if cnt == 5: 
    e=original//10000
    print(e)
elif cnt == 4: 
    e=original//1000
    print(e)
elif cnt == 3: 
    e=original//100
    print(e)
elif cnt == 2: 
    e=original//10
    print(e)
    

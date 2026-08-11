#print nth prime number
num=int(input('Enter a number :'))
i=2
c=0
while True:
    d=2
    while d<=i//2:
        if i%d==0:
            break
    
        
        d+=1
    else:
        c+=1
        if c==num:
            print(i)
            break
        
    
    i+=1

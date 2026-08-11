#prime numbers 1 to 1000
num=1
while num<=1000:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        
        d=d+1
    else:
        print(num)


    num = num+1

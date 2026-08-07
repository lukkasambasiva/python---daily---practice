#ATM pin verfication
my_pin=1397
i=1
while i<=3:
    pin=int(input('Enter your Pin :'))
    if my_pin == pin:
        while True:
        print('1. Withdrow')
        print('2. Deposit')
        print('3. check balance')
        print('4. Exit')
        break
        ch = int(input('choose a Option:'))
        if ch == 1:
            print('Enter Your amount:')
            if ch==amount:
                if ch%100==0 or ch%500==0:
                    amount=amount-ch
                   print('Collect your Amount')
                   
                else:
                   print('designation is wrong')
            else:
                print('Insuffint Balance')
        if ch==2:
            if ch%100==0 or ch%500:

            
        else:
            
                   
    else:
         print('Invalid Pin')
         i=i+1
     
else:
    print('Your Card is Blocked')
    
 

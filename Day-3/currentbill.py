#Curent bill

watts =int(input('Enter a consumed Watts :'))
if watts>0:
   if watts<=100:
       bill = watts*5
   elif watts<=200:
       bill = 5*100+(watts-100)*7
   elif watts<=300:
       bill = 5*100+7*100+(watts-200)*10
   else:
       bill = 5*100+7*100+10*100+(watts-300)*20
   print('Current Bill Amount:',bill)
else:
    print('Invaild bill')

#shop keeper
'''>1000-10%
mship-5%
copuon-5%'''

amount = int(input('Enter Your Bill :'))#2000
mship = input('Do u have Mship(yes/no):')
copun = input('Do u have Copun(yes/no):')

if amount>1000:
    amount =amount-amount*0.1
    
if mship =='yes':
    amount =amount-amount*0.05
    
if copun =='yes':
    amount = amount-amount*0.05
    
print('U have pay the Amount:',amount)




#loan eligible
age = int(input('Enter a age:'))
salary = int(input('Enter your salary :'))
crd_score = int(input('Enter Your cradit score :'))
if age>=21:
    if salary>=30000:
        if crd_score>=700:
            if salary>50000 and crd_score>800:
                print('Premium Loan Approved')
            else:
                print('Loan Approved')
        else:
            print('Loan rejected')
    else:
        print('loan Rejected')
else:
    print('Loan Rejected')

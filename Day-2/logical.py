'''step1:remeber the student  marks 
step2:check the sports certificate (yes / no)
step3:marks>=35 or sport certificate if yes
        it eligible
step4:2 conditions is false it Not eligible'''


std_marks =int(input('Enter Your Marks :'))#35
std_cer = str(input('you have sports Certificate :(yes/No)'))#yes
if std_marks>=35 or std_cer=="yes":#35>=35=T or yes=yes
    print('Eligible')
else:
    print('Not Eligible')
    

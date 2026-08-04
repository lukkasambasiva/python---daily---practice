#age calculator 
'''step1:remember to bith year
step2:remember to current passing year
step3:subrction current passing year- birth year
step4:show the age'''



birth_year =int(input("Enter the Birth Year :"))
current_year= int(input("Enter The Current year :"))
age = (current_year - birth_year)
months= age*12
days = age*365
print("Your Age :",age)
print("In months :",months)
print("In Days :",days)




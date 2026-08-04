#marks grade
#>90-A grade
#>80-B grade
#<70-C grade

marks = int(input('Enter a marks :'))
if marks>=70:
   if marks>=90:
      print('A Grade')
   elif marks>=80:
      print('B Grade')
   elif marks>=70:
      print('C grade')
else:
    print('Failed')


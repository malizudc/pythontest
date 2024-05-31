electric_bill= input('enter your unit:')

#convert the string to int
units= int(electric_bill)

#determine the unit price
if units <= 100:
 unit_price = 0
 print (unit_price)
# for the first 100 units

elif units <= 200:
   unit_price = 5
   print (f'you will pay ${unit_price} for the bill')

else:
   unit_price = 10
   print (f'you will pay ${unit_price} for the bill')
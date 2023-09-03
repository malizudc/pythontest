my_age= input('enter your age')

#convert the string to int
your_age= int(my_age)

#determine the ticket price
if your_age < 5:
 ticket_price = 500
 print (ticket_price)

elif your_age < 16:
   ticket_price = 800
   print (ticket_price)

   
else:
   ticket_price = 1500
   print (f'you will pay ${ticket_price} for the ticket')
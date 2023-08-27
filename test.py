message= 2
print (message)
name= 'JOHN'
mymessage= f'HI {name}'
print (mymessage)

myname= "PETER"
greeting= f'GOOD MORNING {myname}'
print (greeting)

jname= "JAMES"
mgreet= "GOOD AFTERNOON"
mgreeting= mgreet + " "+jname + ", " +"HOW ARE YOU"
print (mgreeting)

str="HOW ARE YOU?"
str_len= len(str)
print (str_len)

str1= "PETER IS A GOOD BOY"
print (str1[11:15])
str1_len= len(str1)
print (str1_len)

strr="j" + [1:2]
print (strr)

age= input('enter your age')
if int(age)>= 18:
    print ('you are eligible to vote')
else:
  print ('you are not eligible to vote')

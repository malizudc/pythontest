my_score= input('enter your percentage')
#convert the string to int

your_score= int(my_score)
#determine the grade

if your_score <60:
  grade= 'D'
  print (f'your grade is {grade}')

elif your_score >=60 and your_score <=80:
    grade= 'C'
    print (f'your grade is {grade}')

elif your_score >80 and your_score <=90:
    grade= 'B'
    print (f'your grade is {grade}')

else:
     grade='A'   
     print (f' CONGRATULATIONS!!! your grade is {grade}')
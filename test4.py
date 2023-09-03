my_score= input('enter your score')

#convert the string to int
your_score= int(my_score)
#determine the grade
if your_score <= 20:
  grade= 'F'
  print (f'SORRY... YOU FAILED!!! your grade is {grade}')

elif your_score <= 40:
    grade= 'D'
    print (f'CONGRATULATIONS FAIR ENOUGH !!! your grade is {grade}')

elif your_score <= 60:
    grade= 'C'
    print (f'CONGRATULATIONS YOU PASSED!!! your grade is {grade}')

elif your_score <= 80:
  grade= 'B'
  print (f'CONGRATULATIONS YOU PASSED!!! your grade is {grade}')

else:
  grade= 'A'   
  print (f'CONGRATULATIONS YOU PASSED!!! your grade is {grade}')

 

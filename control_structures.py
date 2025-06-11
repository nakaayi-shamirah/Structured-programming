## if statements

'''
syntax
if condition:
  logic
  eliff condition:
  logic
else:
     logic

'''

## A program that accepts a number from the user (1-9),
# it tells him the number entered

print("welcome to number teller")
number =int(input("please enter a number between 1 and 9"))
if number == 1:
    print("you have entered number one")
elif number == 2:
    print("you have entered number two")
elif number == 3:
    print("you have entered number three")
elif number == 4:
    print("you have entered number four")
elif number == 5:
    print("you have entered number five")
elif number == 6:
    print("you have entered number six")
elif number == 7:
    print("you have entered number seven")
elif number == 8:
    print("you have entered number eight")
elif number == 9:
    print("you have entered number nine")



#TODO
'''
with the use of if statements, write a python that allows an instructor to enter a mark strictly 
between 0-100

on receiving the mark, the program has to assign a grade based on your definrd clusters ie 80-90 is A,
91-100 is A+
'''


print("students' marks")
if "mark" >= 91:
    print(grade = "A+")
elif "mark" >= 80:
    print(grade = "A")
elif "mark" >= 70:
    print(grade = "C")
elif "mark" >= 60:
    print(grade = "D")
else:
    print(grade = "F")
    
    
    
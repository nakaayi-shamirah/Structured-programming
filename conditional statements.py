#Prompt user to input a numeric score
score = int(input("Enter your numeric score 0-100:"))

#Determine grade using the gradin scale
if score >= 80 and score <=100:
      print ("grade A")
elif score >= 70 and score <= 79:
     print ("grade B")
elif score >= 60 and score <= 69:
     print ("grade C") 
elif score >= 50 and score <= 59:
     print ("grade D")
elif score >= 0 and score <= 50:
     print ("grade F")
else:
     print ("grade Invalid score (must be between 0 and 100")

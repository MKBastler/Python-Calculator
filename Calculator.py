#This is a simple calculator using the console
print ("Calculator program. You got following options: 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division") 
try:
 number=int(input("Make your choice"))
 while (number>4 or number<1): 
  number=int(input("Please select 1 for addition, 2 for subtraction, 3 for multiplication or 4 for division"))
except: print("You use the wrong input format")
#Catch when letter is inserted  
try:
   if (number==1):
    #Addition
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x+y
    print (z)

   elif (number==2):
    #Subtraction
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x-y
    print (z)

   elif (number==3):
    #Multiplication
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x*y
    print (z)
	
   elif (number==4):
    #Division
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x/y
    print (z)
except ZeroDivisionError: print("You cannot devide through zero")
#Catch deviding through zero
except ValueError: print("Please use numbers")
#Catch any other input error
except: print("Please use the proper input methods")
#Catch code related errors
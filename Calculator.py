print ("Calculator program. You got following options: 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division") 
number=int(input("Make your choice"))
while (number>4 or number<1): 
  number=int(input("Please select 1 for addition, 2 for subtraction, 3 for multiplication or 4 for division"))
  
try:
   if (number==1):
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x+y
    print (z)

   elif (number==2):
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x-y
    print (z)

   elif (number==3):
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x*y
    print (z)
	
   elif (number==4):
    x=float(input("Select the first number:"))
    y=float(input("Select the second number:"))
    z=x/y
    print (z)
except ZeroDivisionError: print("You cannot devide through zero")
except ValueError: print("Please use numbers")
except: print("Please use the proper input methods")

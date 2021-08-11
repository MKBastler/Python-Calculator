print ("Calculator Programm. You got following options: 1 for Addition, 2 for subtraction, 3 for multiplication and 4 for division")
number=int(input ("Make your choice:"))
if (number==1):
	x=float(input ("Select the first number:"))
	y=float(input ("Select the second number:"))
	z=x+y
	print (z)

elif (number==2):
	x=float(input ("Select the first number:"))
	y=float(input ("Select the second number:"))
	z=x-y
	print (z)

elif (number==3):
	x=float(input ("Select the first number:"))
	y=float(input ("Select the second number:"))
	z=x*y
	print (z)
	
elif (number==4):
	x=float(input ("Select the first number:"))
	y=float(input ("Select the second number:"))
	z=x/y
	print (z)

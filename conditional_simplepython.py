#Python Condition Simple Codes
#If Statements
#First Code
var_a = 6
var_b = 2

if var_a>var_b:
    print (var_a, " is the greatest")

#Second Code
var_c = input ("Would you like to see the text? (press y if yes):")
if var_c=="y":
    print("You are beautiful love")

#Third Code
var_d = int(input("Please Enter a number: "))
var_e = int(input("Please Enter a number to operate with: "))
var_f = input("what operation you want to do perform with given numbers?, (+-*/): ")
if var_f=="-":
    print ("If we minus ", var_e, " from", var_d, " we will get ", var_d - var_e )
if var_f=="+":
    print ("The sum of given numbers would be ", var_d+var_e)
if var_f=="*":
    print ("The product of given numbers would be ", var_d*var_e)
if var_f=="/":
    print ("If we divide ", var_d, " by", var_e, " we will get ", var_d / var_e)

#If Else Statement
#Fourth Code
var_g = 12
var_h = 18
if var_g>var_h:
    print (var_g, " is greater than ", var_h)
else:
    print (var_h, " is greater than ", var_g)

#Fifth Code
var_i = input ("Please Enter Your Name: ")
var_j = int(input("Please Enter Your Age: "))
if var_j>=18:
     print ("You can get Driving license congratulations ", var_i)
else:
    print ("You can not get Driving license sorry ", var_i)

#Elif Statement
#Sixth Code
var_i = input ("Please Enter Your Name: ")
print ("You like coding?")
var_j = input("Please enter y for yes n for no:")
if var_j=="y":
     print ("You love coding wow ", var_i)
elif var_j=="n":
    print ("You do not like coding oh ", var_i)
else:
    print ("Error!, Please enter the valid key either y or n")

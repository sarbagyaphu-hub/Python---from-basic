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

#Nested If statements
#Seventh Code
var_k = 20
var_l = "yessss"
if var_k>18:
    print ("You are eligible for driving license")
    if var_l=="yessss":
        print("You have driving license, do not submit application again")
    elif var_l=="no":
        print("you can submit application online")
elif var_k==18:
    print ("you have to wait for one more year to submit application")
else:
    print ("You are a minor cannot have license")
    
# Eighth Code
var_m = input("Please Enter Your name: \n")
var_n = int(input("Please Enter your age: \n"))

if var_n == 18:
    print("You have to wait for a year to submit application")

elif var_n > 18:
    var_o = input("Do you have a driving license? Enter yes or no: ")

    if var_o == "yes":
        var_p = input("Is it expired? Enter yes or no: ")

        if var_p == "yes":
            print("You can submit application online.")

        elif var_p == "no":
            print("Not expired means you want to add category?")
            var_q = input("Do you want to add category? Enter yes or no: ")

            if var_q == "yes":
                print("You can submit application online.")

            elif var_q == "no":
                print("You cannot submit a new application as you already have a valid license.")

            else:
                print("Please enter a correct response.")

        else:
            print("Please enter a correct response.")

    elif var_o == "no":
        print("Please submit an application online.")

    else:
        print("Please enter a correct response.")

else:
    print("You are a minor and cannot submit an application until you are older than 18.")

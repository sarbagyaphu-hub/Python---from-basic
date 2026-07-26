#For loop in python
#First Code
var_a = 1
print ("The loop shall print 1 5 times ")
for i in range (5):
    print (var_a)
    
#Second Code
var_b = 1
print ("This shall print 1 to 5")
for var_b in range (1,6):
    print (var_b)

#Third Code
var_c = int(input("Enter the number you want to create a multiplication table of : "))
var_d = 1
print ("Multiplication Table of ", var_c)
for var_d in range (1,11):
    var_e = var_c*var_d
    print (var_c, " * ", var_d, " = ", var_e)
    
#Fourth Code 
print ("this is decriment")
var_f = 10
for i in range (9):
    print (var_f)
    var_f -=1
    
#Fifth Code
var_g = int(input("Please enter a number you want opposite multiplication table of : "))
var_h = 10
for i in range (10):
    var_i = var_g*var_h
    print (var_g, " * ", var_h, " = ", var_i)
    var_h -=1


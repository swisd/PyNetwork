"""
Math


+       addition
-       subtraction
*       multiplication
/       float division
**      exponentiation
abs()   absolute value
//      integer division
%       remainder



Ternary operator:


print("your age :")
age = float(input())
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


Logical Operators:

-AND
-OR
-NOT

-> And usage

if high income and good credit are both true, it will print "eligible"
if one or both conditions is(are) false, it will not print "eligible"



high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible")
-> Or usage

if high income or good credit are both true, it will print "eligible"
if both conditions are false, it will not print "eligible"


if high_income or good_credit:
    print("eligible")

-> Not usage

inverses value of a boolean

if 'student' is true it will print "not eligible" but, if 'student' is false it will print "Eligible

high_income = True
good_credit = True
student = True

if not student:
    print("eligible")
else:
 print("Not eligible")

"""
"""
Math
-----------------------------
operator  |  operation
-----------------------------
+         |  addition
-         |  subtraction
*         |  multiplication
/         |  float division
**        |  exponentiation
abs()     |  absolute value
//        |  integer division
%         |  remainder
-----------------------------
======================
Python  | Mathematics
======================
pi      | π
string  | string
sqrt(x) | Ѵͯ
sin(x)  | sinͯ
cos(x)  | cosͯ
tan(x)  | tanͯ
asin(x) | arcsinͯ
acos(x) | arccosͯ
atan(x) | arctanͯ
log(x)  | lnͯ
log10(x)| log¹⁰ͯ
exp(x)  | eͯ
ceil(x) | ┌ͯ┐
floor(x)| └ͯ┘
======================

-------------
Lists:
-------------
example;

[2, 3, 4, 5]
["a", "b", "c"]

square brackets define a list
lists can be assigned by a variable

letters = ["a", "b", "c"]
matrix = [[0,1],[2,3],[4,5]]
n = list(range(1001))
chars = list("Hello World")   len


[0] * 100 will repeat '0,' 100 times

multiple lists ca be added together

list unpacking
numbers = [1,2,3]
first, second, third

first = numbers[0]
second = numbers[1]
third = numbers[2]

unpack and pack

first, second, *other = numbers

unpack first and second then pack anything other than first and second in other

------------
-------------------
Ternary operator:
------------------

print("your age :")
age = float(input())
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

-------------------------

---------------------
Logical Operators:
---------------------
-AND
-OR
-NOT
---------------------

----------------
-> And usage

if high income and good credit are both true, it will print "eligible"
if one or both conditions is(are) false, it will not print "eligible"



high_income = True
good_credit = True

if high_income and good_credit:
    print("eligible")

----------------
-> Or usage

if high income or good credit are both true, it will print "eligible"
if both conditions are false, it will not print "eligible"


if high_income or good_credit:
    print("eligible")


----------------
-> Not usage

inverses value of a boolean

if 'student' is true it will print "not eligible" but, if 'student' is false it will print "Eligible

1  high_income = True
2  good_credit = True
3  student = True
4
5  if not student:
6    print("eligible")
7  else:
8    print("Not eligible")
 -----------------------------------------------

------------
Loops:
------------
For        |  for i in range(x):
Nested     |
While      |  while x  /  while x == y
if         |  if i in range(x):

------------
Variables:
------------
int  ==  integer
str == string
bool == boolean (true, false)
float == floating point number
------------
Statements:
------------
statement    |  example/description
-----------------------
if           |  if x == y:  / IF variable x is equal to variable y, ...
or           |  if x or y == z: /  if variable x OR variable y is equal to variable z
not          |
else         |               /if the 'if' statement is 'False'
elif         |  elif x == y: /
break        |            / Exit Loop
for          |
when         |
-----------------------

-------------
Functions:
-------------
print()
round()
input()
float()
open()
-------
To create a function;

Define the function using 'def',
use lowercase letters,
use underscores to separate multiple words,
always add parentheses and a colon at the end of the function name.
When defining a function, list the parameters inside the parentheses.*
-------
Example;
------

1   def greet(first_name, last_name):
2       print("Hi there!")
3       print("Welcome aboard.")
4
5
6   greet("abc", "ghi")
7

# Remember to add 2 line breaks after the function to keep your code clean. If you forget to add the 2 line
breaks, don't worry. As soon as you save the changes, auto pep8  will add two line breaks for you.

the output should look like this;

Hi there!
Welcome aboard
abc ghi

Process finished with exit code 0
---------------------------------------------
-------------
Parameters:
-------------
A parameter is the input that you define in your function.





-------------
Arguments:
-------------
An argument is a given value for a parameter


7   greet("abc, "ghi")

the arguments in this sample are "abc" and "ghi". these are the arguments of the 'greet()' function from the
previous example.

if you remove one of the required arguments specified in the parameters, you will get a red underline and
an error error will appear on the output.
--

1   def greet(first_name, last_name):
2   print(f"Hi {first_name} {last_name}!")
3   print("Welcome aboard.")
4
5
6   greet("abc")
7


the output will be;


Traceback (most recent call last):
  File "E:/Python/Courses/Python Book/123.py", line 6, in <module>
    greet("abc")
TypeError: greet() missing 1 required positional argument: 'last_name'

Process finished with exit code 1


--
when you hover over the red underline you will get:

[pylint] E1120:No value for
argument in function call
---------------------------------
full code (revised)


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard.")


greet("abc", "ghi")


the output should look like this

Hi abc ghi!
Welcome aboard.

Process finished with exit code 0

Note :  you can repeat and change a function and it's arguments
---------
* a function must always have parameters.
----------------
------------------
Types of functions
------------------



Type 1 - Preform a task

examples:
print("a")
greet("abc", "ghi")

Type 2 - Return a value

examples:
round(1.9)

def get_greeting(name):
    return f"hi {name}"


message = get_greeting("abc")
file = open("context.txt", "w")\
file.write(message)
----------------------------------------

------------------------------
Keyword Arguments  (kwargs)
------------------------------
keyword arguments make arguments more readable

regular arguments

print(increment(2, 1))

keyword arguments


print(increment(number=2, by=1))


---------------------

def increment(number, by)
    return number + by


    result = increment(2, 1)
  print(result)


----------------------------
-----------------
Default arguments
-----------------
example;
---------

def increment(number, by=1)
    return number + by


    result = increment(2)
  print(result)
---------
Used so that you don't have to constantly type in a variable that will always stay the same. Optional
 parameters always come after the required parameters
---------------------
-------------
*args (xargs)
-------------
 example;

 def multiply(*numbers):
     print(numbers)
     return x * y

 multiply(2, 3, 4, 5)

the output should look like this

(2, 3, 4, 5)


Process finished with exit code 0


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

-------------
**args (xxargs)
-------------
example

def save_user(**user):
    print(user)


save_user(id=1,name="John", age=22)


the output should be;

{'id':1, 'name': 'John', 'age': 22}         <-   dictionary

when you use **, you can pass multiple keyword arguments

dictionaries

  print(user["id"])

  Using the bracket notation, you can get the values of various keys in the created dictionary
------------
Scope
------------

in this example, message is not defined.         in this example, name is undefined

def greet():                                       def greet(name):
    message = "a"                                      message = "a"


print(message)                                     print(name)



so, the scope of the name and message variables are the greet functions, and you refer to these variables
as local variables in this function. They're local in this function, which means they don't exist anywhere
else.

in contrast to local variables, we have global variables, which are accessible anywhere in the file. so
the scope of the global variable is the file

example;

local variable                          global variable

def greet(name):                          message = "a"
    message = "a"
                                          def greet(name):

def send_email(name):
    message = "b"                         def send_email(name):
                                              message = "b"

greet("John")
                                         greet("John")


-----------------------------------------------
message = "a"

def greet(name):
    message = "b"


greet("John")
print(message)

 global message
------------------------------------------------

-------------
Debugging
-------------

-------------------
fizz buzz solution
-------------------
d = float(input())
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
       return "FizzBuzz"
    if input % 3 == 0:
       return "Fizz"
    if input % 5 == 0:
       return "Buzz"
    return input


print(fizz_buzz(d))

-----------------

-------------
Lambdas
-------------
example;
items = [
   ("Product1",10),
   ("Product2",9),
   ("Product3",12),
]

def sort_item(item):
    return item[1]

items.sort(key=lambda parameters:expression)
print(items)



items.sort(key=lambda item:item[1])
print(items)

A lambda is a function that we can use to transform each item in our original list.

-------------
Map (function)
-------------

items = [
   ("Product1",10),
   ("Product2",9),
   ("Product3",12),
]

prices = []
for item in items:
    prices.append(item[1])

map(lambda)

# the map function takes 2 parameters; function, and one or more iterables. so as the first argument,we can pass a
lambda function and as a second argument, we can pass our list of items. this map function, will apply to the
 lambda function,for each item in this list.

prices = list(map(lambda item ; item[1], items))



print(prices)
--
output

[10, 9, 12]

-------------------------------
----------
Filter
----------
1  items = [
2     ("Product1",10),
3     ("Product2",9),
4     ("Product3",12),
5  ]
Here we have a list of items. Lets say we want to filter this list and only get the items with a price greater than or
equal to 10. One basic way is to define an empty list like 'filtered', then we iterate over our list of items, for each
item we get the price, if it matches our criteria, we'll add it to this list.



1  items = [
2     ("Product1",10),
3     ("Product2",9),
4     ("Product3",12),
5  ]
6
7  filtered = []

That's pretty basic and the better approach is to use the built in filter function 'filter()' . This function, just like
the map function, takes two parameters: a function and an iterable. So it will apply this function on each item of the
iterable.if the item matches some criteria, it will return it. So let's see how we can use this function. As a first
argument, I'm going to pass a lambda function. This function takes an item and returns a boolean value that determines
if this item matches the criteria or not. In this case, we want to get the price of each item, and see if it is greater
than or equal to 10. So the result of this expression is a boolean value. If it's True, this item will return. Now as
a second argument to the filter function, we pass our items list. Let's temporarily store the result in a variable
called 'x' and print it

1  items = [
2     ("Product1",10),
3     ("Product2",9),
4     ("Product3",12),
5  ]
6
7  x = filter(lambda item: item[1] >= 10, items)
8  print(x)
9

output:

<filter object at 0x00000289F4C66AF0>

Process finished with exit code 0

So we get a filter object. The filter object, just like the map object, is iterable, so we can loop over it. We can
also convert it to a list right away. So let's call this, now we get a filtered list, and we can print on the terminal.

1  items = [
2     ("Product1",10),
3     ("Product2",9),
4     ("Product3",12),
5  ]
6
7  filtered = list(filter(lambda item: item[1] >= 10, items))
8  print(filtered)
9

output:

[('Product1', 10), ('Product3', 12)]

Process finished with exit code 0So, as you can see, we only have items one and three because their prices are greater
than or equal to 10.
---------------------------------
--------------------
List Comprehensions
--------------------

We have our square brackets for defining a list, and here we will write a comprehension expression like this.(Ln 8)


 1 items = [
 2    ("Product1",10),
 3    ("Product2",9),
 4    ("Product3",12),
 5 ]
 6
 7 prices = list(map(lambda item ; item[1], items))
 8 [expression for item in items]
 9
10 filtered = list(filter(lambda item: item[1] >= 10, items))
11
12
13
14

  items = [
     ("Product1",10),
     ("Product2",9),
     ("Product3",12),
  ]

In this example, we are iterating over an iterable and then applying this expression on each item.(Ln 8)
If you want to get the price of an item, We can write an expression like this. 


7 prices = list(map(lambda item ; item[1], items))
8 [item[1] for item in items]


This is what we call a list comprehension, and it produces the exact same result as what we have on line 7, so, let's store the result in prices.


8 prices = [item[1] for item in items]


As you can see, this code is shorter and cleaner, we don't have all these parentheses and colons compared to line 7. The preferred way to map and filter lists is to use list comprehensions. As part of this mapping, you can also filter items, so if I want to rewrite what we have on line 10 using a list comprehension, that would look like this.(line 11)


10 filtered = list(filter(lambda item: item[1] >= 10, items))
11 filtered = [item for item in items]


We'll iterate over the list of items, we'll get each item and simply return it. However, we want to filter them, so we'll add an if statement, if item of 1 is greater than or equal to 10.


10 filtered = list(filter(lambda item: item[1] >= 10, items))
11 filtered = [item for item in items if item[1] >= 10]


What we have on line 11 is more readable and cleaner than what we have on line 10, but if youwant to use the map or filter functions, that's perfectly fine.

---------------------------------
-------------
Zip Function
-------------

Here we have two lists





"""

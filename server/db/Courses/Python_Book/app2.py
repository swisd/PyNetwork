import time

print("Input number (0 - 255)")
inp = int(input())
numbers = [2, 4, 6, 8]
product = inp
for number in numbers:
    product = product * number

print('The product is:', product)


print("Please enter your score.")
score = float(input())
if score >= 90:
    print("A")
if score >= 80 and score <= 89:
    print("B")
if score >= 70 and score <= 79:
    print("C")
if score >= 60 and score <= 69:
    print("D")
if score <= 59:
    print("F")


print("Please enter text")
text = str(input())
print("Please enter your encryption key")
key = int(input())
keystr = str(key)
textencr = str(enumerate(text))
print(textencr, "{",key,"}"" []")

n = 0
x = eval(input("Please enter a number between 0 and 1:"))
e = eval(input("How many numbers do you want:"))
for i in range(e):
  n = n + 1
  x = 3.9 * x * (1 - x)
  print(n,":",x)
  time.sleep(0.5)


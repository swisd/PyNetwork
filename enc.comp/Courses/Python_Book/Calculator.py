print("Calculator Program")
loop = 'yes'
while loop == 'yes':

 print("Type 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for remainder, 6 for exponent ")
 inp = input()

 if inp == '1':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 + inp2)
 elif inp == '2':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 - inp2)
 elif inp == '3':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 * inp2)
 elif inp == '4':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 / inp2)
 elif inp == '5':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 % inp2)
 elif inp == '6':
    print("Enter first number")
    inp1 = float(input())
    print("Enter second number")
    inp2 = float(input())
    print(inp1 ** inp2)

 print("would you like to continue?")
 loop = str(input())

print("PyCalculator V1.2.8")
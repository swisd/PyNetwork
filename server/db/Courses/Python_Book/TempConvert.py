print("Press 1 for Temperature converter.")
print("Press 2 for Pressure converter.")
inp = input()

if inp == '1':
 print(">>>")
 print('Temperature converter')
 print('Enter 1 to convert from C to F.')
 print('Enter 2 to convert from F to C.')
 print('Enter 3 to convert from F to K.')
 print('Enter 4 to convert from C to K.')
 print('Enter 5 to convert from K to C.')
 print('Enter 6 to convert from K to F.')
 print("Enter 7 for conversions.")
 print("Enter 8 to exit")
 temp = input()
 if temp == '1':
     print(">>>")
     print('Please enter temp in C')
     tempInC = float(input())
     tempInF = (9/5 * tempInC) + 32
     print(">>>")
     print('Temp in F is:', tempInF)
 if temp == '2':
     print(">>>")
     print('Please enter temp in F')
     tempInF = float(input())
     print(">>>")
     print('Temp in C is:', (tempInF - 32) * 5/9)
 if temp == '8':
     print(">>> TempPressConvert V3.8.5 ")
     print("©2022 ")
 if temp == '7':
     print("C to F : (9/5 x C) + 32 = F")
     print("F to C :  (F - 32) * 5/9 = C")
     print('C to K : K = C + 273.15')
     print('F to K : K = (F - 32) / 1.8 + 273.15')
     print('K to C : C = K - 273.15')
     print('K to F : F = K * 1.8 - 459.67')
 if temp == '3':
     print('>>>')
     print('Please enter temp in F')
     tempInF = float(input())
     tempInK = (tempInF - 32) / 1.8 + 273.15
     print('Temp in K is:', tempInK)
 if temp == '4':
     print('>>>')
     print('Please enter temp in C')
     tempInC = float(input())
     tempInK = tempInC + 273.15
     print('>>>')
     print('Temp in K is:', tempInK)
 if temp == '5':
     print('>>>')
     print('Enter temp in K')
     tempInK = float(input())
     tempInC = tempInK - 273.15
     print('>>>')
     print('Temp in C is', tempInC)
 if temp == '6':
     print('>>>')
     print('Enter temp in K')
     tempInK = float(input())
     tempInF = tempInK * 1.8 - 459.67
     print('>>>')
     print('Temp in F is :', tempInF)

if inp == '2':
 print()

print(">>> TempPressConvert V3.8.6 ")
print("©2022  ")

password=''
counter=1
triesleft=0
print('Please enter password for system access')
password = input()
while counter < 4:
 if password == 'gl':
  print('access granted')
  counter = 4
 else:
   print('Access Denied.')
   triesleft = 3 - counter
   print('Attmepts left')
   print(triesleft)
   counter = counter + 1
   if triesleft > 0:
    print('Please try again')
   password = input()
 
if triesleft == 0:
   print('SYSTEM ACCESS PERMANENTLY DISABLED')

if counter == 4:
   print('Tempature converter')
   print('enter 1 to convert from C to F.') 
   print('enter 2 to convert from F to C.')
   temp = input()
   if temp == '1':
     print('Please enter temp in C')
     tempInC=float(input())
     tempInF = (9/5 * tempInC) + 32
     print('Temp in F is:', tempInF) 
   else:
    if temp == '2':
     print('Please enter temp in F')
     tempInF = float(input())
     print('Temp in C is:', (tempInF - 32) * 5/9)




 




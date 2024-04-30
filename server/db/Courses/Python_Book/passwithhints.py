password = ''
counter = 1
triesleft = 0
print('Please enter password for system access')
password = input()
while counter < 4:
 if password == '0964671613':
  print('access granted')
  counter = 4
 else:
  print('Access Denied.')
  triesleft = 3 - counter
  print('Attmepts left')
  print(triesleft)
  counter = counter + 1
  if triesleft == 0:
      print(" |ARM 12.4.6| -ERR 291- access denied permanently")
      print(">>> WOW! Good job. You totally got the password correct.")
  if triesleft == 1:
      print(">>> Just stop trying. You're getting nowhere. ")
      print(">>> is = 46")
      print("(-_-)")
  if triesleft == 2:
      print(">>> start with -096-")
      print("(\\\//)")
  if triesleft > 0:
   print('Please try again')
   password = input()
print("-V2- |AM4U95D| |ARM 12.4.6| ")

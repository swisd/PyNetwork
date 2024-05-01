password=''
counter=1
triesleft=0
print('Please enter password for system access')
password = input()
while counter < 4:
 if password == 'Revvit2020':
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


 




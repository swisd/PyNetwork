
def increment(number, by):
    return number + by


umber = 1.0101010101010101010101


for i in range(2):
  result = increment(umber, umber)
  print(result)
  umber = umber * umber


def greeting(name):
    return f"{name}"


message = greeting(umber)
file = open("C:/PyDev/Missile/log/blackbox/CRS_DIR.iSr", "r")
print(file.read())

while True:
    s = input()
    if s == '0':
        print("Sorry, this file can't be deleted.")
    if s == '01101001':
        print("initializing...")
        quit()
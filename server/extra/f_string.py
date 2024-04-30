# Trick 1: Separators

n: int = 1000000000
print(f'{n:_}') # Separates int using _
print(f'{n:,}') # Separates int using ,

# -----------------------------
# Trick 2: Spacing

var: str = 'var'

print(f'{var:>20}:') # makes 'var' take up 20 chars of space, forces text right align
print(f'{var:<20}:') # opposite arrow, forces text left align
print(f'{var:^20}:') # center align text
print(f'{var:_^20}:') # center align text with fill element _



# -----------------------------
# Trick 3: Datetime

from datetime import datetime

now: datetime = datetime.now()
print(f'{now:%m.%d.%y (%H:%M:%S)}') # Datetime format using f-string
print(f'{now:%c}')# local version of datetime format
print(f'{now:%I%p}')# 12hr am/pm


# -----------------------------
# Trick 4: Decimal Points

n: float = 1234.5678
print(f'{n:.2f}')# first two decimal points, rounded
print(f'{n:,.2f}')# first two decimal points, rounded with separator


# -----------------------------
# Trick 5: Outputs

a: int  = 5
b: int = 10

print(f'{a + b = }') # give output of {}
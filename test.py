from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.GREEN )
print( Fore.BLACK )

what = input("nma qilamiz? (+, -): ")

print( Back.CYAN )

int = a = float( input("birinchi sonni kiriting: ") )
int = b = float( input("ikkinchi sonni kiriting: ") )

print( Back.YELLOW )
print( Fore.BLACK )

if what == "+":
  c = a + b  
  print("natija: " + str(c))
elif what == "-":
  c = a - b
  print("natija: " + str(c))
else:
  print("xato!")

input()
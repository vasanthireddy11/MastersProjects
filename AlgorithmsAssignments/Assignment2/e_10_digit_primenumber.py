import math
from decimal import Decimal, getcontext

getcontext().prec = 1000
e = Decimal(0)
for i in range(1000):
    e += Decimal(1)/math.factorial(i)
e_str = str(e)
e_length = len(e_str);
print("estring", e_str)
x = 2;
y = 12;
def my_function(num):
  for i in range(2, num):
  	if num % i  == 0:
	  	break
  else:
	  print("consecutive 10 digit prime number is:", num)

str_eachTenDigits = '';
int_t = 0;
for i in range(1, e_length - 11):
  str_eachTenDigits = e_str[x:y];
  int_t = int(str_eachTenDigits);
  my_function(int_t)
  x+=1;
  y+=1;
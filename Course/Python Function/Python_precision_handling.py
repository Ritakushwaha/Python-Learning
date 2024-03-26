# Precicion handling using Rounding Method

r = round(8.875645, 2)
print(r)

f = '{:.3f}'.format(9.9999)
print(f)

# Precision handling using getcontext()
from decimal import Decimal, getcontext
getcontext().prec = 5
r = Decimal('3')/Decimal('9')
print(r)

# Precision handling with Math Module
import math
a = 3.524221
print(math.trunc(a))
print(math.ceil(a))
print(math.floor(a))

'''
Precision handling using 
- %
- format()
- round(x,n)
- f string
'''

a = 4.5678
print('%.2f' % a)
print('{0:.3f}'.format(a))
print(round(a,2))
print(f'{a:0,.2f}')

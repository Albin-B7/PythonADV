from My_math import square

result = square(5)
print(result)

import My_math

result = My_math.square(7)
print(result)

import math as m

result = m.sqrt(25)
print(result)

from math import sqrt as sq

result = sq(49)
print(result)


import importlib
import my_module

importlib.reload(my_module)
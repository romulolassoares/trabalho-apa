# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc() 

import numpy as np
from random import randint
   
def create_array(size, random):
   arr = np.arange(0, size, 1, dtype=int)
   #age_group = "Minor" if age < 18 else "Adult"
   p = int(size * random)

   for i in range(p):
      p1 = randint(0, size - 1)
      p2 = randint(0, size - 1)
      arr[p1], arr[p2] = arr[p2], arr[p1]
   return arr
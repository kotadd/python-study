# import sys

# sys.argv
# help(sys)
# dir(sys)

import random

result = {'kni': 0,'hik': 0,'hir': 0,'yug': 0,'kaz': 0}

for a in range(1000):
  a = random.choice(['kni','hik','hir','yug','kaz'])
  result[a] += 1

print(result)
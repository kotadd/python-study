# map, filter, zip and reduce
from functools import reduce

my_list = [1,2,3]
your_list = (10,20,30)
their_list = (5,4,3)

def multiply_by2(item):
  return item*2

def check_odd(item):
  return item % 2 == 1

def accumulator(acc, item):
  return acc + item


print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 == 1, my_list)))

# print(list(zip(my_list, your_list, their_list)))
# print (their_list)
print(reduce(lambda acc, item: acc + item, your_list, 0))

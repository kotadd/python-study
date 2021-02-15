def fib(number):
  if (type(number) != int or number < 0): return -1
  if (number == 0): return 0

  a = 0
  b = 1

  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + b

for x in fib(10):
  pass

print(x)


# def generator_function(num):
#   for i in range(num):
#     yield i**2

# g = generator_function(3)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(g)
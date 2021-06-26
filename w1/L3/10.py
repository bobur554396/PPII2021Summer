# Fibonaci list

# 0 1 1 2 3 5 8 13 ...
# a b


def fib1(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    # n = a + b
    # a = b
    # b = n
    a, b = b, a + b


def fib2(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

for i in fib2(100):
  print(i)


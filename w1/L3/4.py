# Lambda function

def fun(a):
  return a * a

a = lambda x: x * x

# print(a(2))

sum = lambda a, b: a + b

# print(sum(2, 4))

# def fun(n):
#   return lambda x: x + n 


def fun(n):
  return lambda x: x * n


# add_two = fun(2)
# print(add_two(100))

doubler = fun(2)
print(doubler(20))

tripler = fun(3)
print(tripler(4))

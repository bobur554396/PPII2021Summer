# - [ ] Generators


def fun():
  yield 1
  yield 2
  yield 3


a = fun()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def fun2():
  for i in range(10000000000):
    yield i


a = fun2()

for i in a:
  print(i)
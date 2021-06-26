def sum(a, b):
  print(a + b)


def sum2(a, b):
  return a + b


sum2('hello', 'hi')

def sum3(a: int, b: int) -> int:
  return a + b


sum3(2, 3)

def square(a: int):
  return a * a



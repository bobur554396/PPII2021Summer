l = ['a', 'b', 'c']

# for i, val in enumerate(l, 100):
#   print(i, val)


def my_enumerate(iterable, start=0):
  for item in iterable:
    yield start, item
    start += 1


for i, val in my_enumerate(l):
  print(i, val)

a = [False, 0, '', 1]

print(any(a))


def my_any(iterable):
  for i in iterable:
    if i:
      return True
  return False


print(my_any(a))

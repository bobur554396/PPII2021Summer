a = [True, 10, 0, 'hello']

print(all(a))

def my_all(iterable):
  for i in iterable:
    if not i:
      return False
  return True  

print(my_all(a))
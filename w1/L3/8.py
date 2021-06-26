class Counter:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a > 10:
      raise StopIteration

    x = self.a
    self.a += 1
    return x

c = Counter()

it = iter(c) # will call __iter__ method inside of the class

# print(next(it))  # will call __next__ method inside of the class
# print(next(it))  # will call __next__ method inside of the class
# print(next(it))  # will call __next__ method inside of the class
# print(next(it))  # will call __next__ method inside of the class
# print(next(it))  # will call __next__ method inside of the class
# print(next(it))  # will call __next__ method inside of the class

for i in it:
  print(i)
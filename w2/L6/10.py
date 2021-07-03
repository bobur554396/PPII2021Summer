ages = [20, 15, 12, 30, 40]

def take_adult(age):
  return age >= 18


# adults = list(filter(take_adult, ages))

# print(adults)


def my_filter(func, iterable):
  for item in iterable:
    if func(item):
      yield item


adults = list(my_filter(take_adult, ages))
print(adults)


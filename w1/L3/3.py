def f1(a, b, *args): # *args - optional arguments ---> tuple
  print(a, b)
  for arg in args:
    print(arg)


# f1(2, 3, 'hello', '1', 123)


def f2(name, age, *args):
  print(f'{name} - {age}')


# f2(name='Alice', age=20)


def f3(**kwargs): # **kwargs - optional keyword arguments ---> dict
  print(kwargs)


# f3(name='Bob', age=20, gpa=3.0)


def f4(a, b=2, *arg, **kwargs): # default value
  print(a + b)


f4(2, 4)

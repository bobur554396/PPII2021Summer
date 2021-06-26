# Collections - List, Tuple, Set, Dictionary
a = [20, 3, 5]
b = list((2, 3, 5))


a.remove(3)

a.append(10)
a.append(100)

a.sort(reverse=False)

# print(a + b)
a.extend(b)

a.insert(2, 4)

a.pop()


c = [1, True, 'hello', 'h', {'name': 'Student 1'}]


# print('hello' in c)

# print(a)


# for i in c:
#   print(i)

for i, val in enumerate(c):
  print(i, val)

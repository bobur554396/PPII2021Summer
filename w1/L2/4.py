# Dictionary

a = {
  'id': 123,
  'name': 'Student 1',
  'age': 20,
}

print(type(a))

b = dict()
b['a'] = 1
b['b'] = 1

print(b)
print(type(b))

print(a.keys())
print(a.values())

# for i in a.items():
#   print(i[1])

for key, val in a.items():
  print(f'{key} ====> {val}')


a.pop('id')

print(a)
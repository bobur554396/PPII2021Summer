# type casting 
a = 123
b = str(a)

print(type(a))
print(type(b))

a = 15.4
b = int(a)

print(a, type(a))
print(b, type(b))


try:
  a = "123a"
  b = int(a)
except Exception as e:
  print('error: '+ str(e))

print(a, type(a))
print(b, type(b))

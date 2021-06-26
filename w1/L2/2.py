# Tuple

a = [1, 2, 3]
print(type(a))

a = (1) # int 
a = (1,) # tuple
print(type(a))

b = tuple((2, 3, 10, 20, 33))

print(type(b))


# d = b[0]
# e = b[1]

d, e, *nums = b

print(d)
print(e)
print(nums)



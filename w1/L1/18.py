# a = 2

# # print(id(a))
# # print(hex(id(a)))

# b = a

# # print(id(b))
# # print(hex(id(b)))

# print(b)

a = [1, 2, 3]

# b = a[:]
b = a.copy()

print(id(a))
print(id(b))

print(a, b)


a.append(5)

print(a, b)

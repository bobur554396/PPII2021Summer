line = input()

# if line == line[::-1]:
#   print('YES')
# else:
#   print('NO')

# print('YES') if line == line[::-1] else print('NO')
print('YES') if line == ''.join(reversed(line)) else print('NO')


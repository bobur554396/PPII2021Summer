# - [ ] anagram?
# line neil - ok
# line nell - no

line1, line2 = input().split()

# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90

# l = 'line'
# l = ''.join(sorted(l))
# print(l)


# l2 = 'neil'
# l2 = ''.join(sorted(l2))
# print(l2)

# print('YES') if ''.join(sorted(line1)) == ''.join(sorted(line2)) else print('NO')
print('YES') if sorted(line1) == sorted(line2) else print('NO')

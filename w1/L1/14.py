# - [ ] palindrome?
# aba - ok
# acbbca - ok
# abc - not
# abbaa - not

line = input()

ok = True
for i in range(len(line) // 2):
  # print(line[0], line[len(line) - 0 - 1])
  # print(line[1], line[len(line) - 1 - 1])
  # print(line[2], line[len(line) - 2 - 1])
  
  # print(line[i], line[len(line) - i - 1])
  if line[i] != line[len(line) - i - 1]:
    ok = False
    break

if ok:
  print('YES')
else:
  print('NO')


# for i in range(11):
#   print(i)


# for i in range(0, 10, 3):
#   print(i)
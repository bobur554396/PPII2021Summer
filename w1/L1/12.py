# line = input()

# print(len(line))


'''
4
4 10 -1 100
'''
n = int(input())
# [<returning iter val> for <iter> in <list> condition ]
numbers = [int(n) for n in input().split()] 

print(numbers)
# nums = []
# for n in numbers:
#   nums.append(int(n))

# print(nums)

s = 0
for i in numbers:
  if i > 0:
    s += i

# print(s)

print(sum([n for n in numbers if n > 0]))
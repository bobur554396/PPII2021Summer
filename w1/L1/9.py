a = 'hello world!'


# C++ loop
# for(int i = 0; i < n; i++){
# }



# for i in a:
#   if i == 'l':
#     continue
#   else:
#     print(i)

# for i in range(len(a)):
#   if i % 2 == 0:
#     print(a[i])


for i, val in enumerate(a):
  if i % 2 != 0:
    print(val)
  else:
    print('*')


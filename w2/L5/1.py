'''
Mode:
  r - read
  w - write
  a - append
  x - create
'''
f = open('file1.txt', 'r')

text = f.read()
# text = f.readline()
# text = f.readlines()

# print(text)
f.close()



f2 = open('file4.txt', 'a')
f2.write(text.upper())
f2.close()

with open('file1.txt', 'r') as f:
  text = f.read()
  print(text)

with open('file5.txt', 'w') as f:
  f.write(text)
import os


for root, dirs, files in os.walk('.'):
  print(root)
  print(dirs)
  print(files)
  print('-'*70)
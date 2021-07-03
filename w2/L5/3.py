import os

# print(os.getcwd())


# os.chdir('Dir1')
# os.mkdir('Dir1_1')
for obj in os.listdir('.'):
  if os.path.isdir(obj):
    print(f'Folder: {obj}')
  if os.path.isfile(obj):
    filename, ext = os.path.splitext(obj)
    if ext == '.py':
      print(f'Python file: {obj}')
    if ext == '.txt':
      print(f'Text file: {obj}')

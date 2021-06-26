name = 'John' # Global Variable

def greeting():
  print(f'hello {name}')


def greeting2(n):
  name = 'Bob' # Local variable
  print(f'hello {name}')

greeting()
greeting2('Alice')





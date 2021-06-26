class Person():
  a = 1
  x = 'a'

  def __init__(self, name, age, *args, **kwargs):
    self.name = name
    self.age = age

  def greeing(self):
    print(f'hello {self.name}')
  
  def __str__(self) -> str:
      return f'{self.name} - {self.age}'


p = Person('Alice', 20) # p - instance of class Person

p.greeing() # calling instnace method

print(p) # automaticly calls __str__ method from class


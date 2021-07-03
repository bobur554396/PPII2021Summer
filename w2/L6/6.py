a = 2
# print(callable(a))

class Person:
  name = 'Alice'
  age = 20

  @classmethod
  def test(cls, a, b): # class method
    return a + b

  def get_age(self): # instance method
    return self.age

  def __str__(self):
      return f'{self.name} - {self.age}'


p = Person()

p.get_age()  # p.get_age(p)
print(p.get_age())

print(callable(p.get_age))

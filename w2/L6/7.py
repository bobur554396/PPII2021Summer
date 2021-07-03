a = 2
# print(callable(a))


class Person:
  name = 'Alice'
  age = 20

  @classmethod
  def test(cls, a, b):  # class method
    return a + b

  def get_age(self):  # instance method
    return self.age

  def __str__(self):
      return f'{self.name} - {self.age}'


p = Person()

print(getattr(p, 'age'))
print(getattr(p, 'age2', 18))

print(hasattr(p, 'age'))
print(hasattr(p, 'age2'))

setattr(p, 'age', 21)
setattr(p, 'age2', 25)

delattr(p, 'age2')

# print(p.age2)  # error, 'Person' object has no attribute 'age2'
print(p.age)


print(dir(p))
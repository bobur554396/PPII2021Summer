# - [ ] Inheritance

class Person():
  def __init__(self, name, age, *args, **kwargs):
    self.name = name
    self.age = age

  def greeing(self):
    print(f'hello {self.name}')

  def __str__(self):
      return f'{self.name} - {self.age}'

# Person - Parent / Base class 
# Student - Child / Derived class
class Student(Person):
  def __init__(self, name, age, id, gpa, *args, **kwargs):
    super().__init__(name, age)
    self.id = id
    self.gpa = gpa
  
  def __str__(self):
      return f'{super().__str__()} - {self.id} - {self.gpa}'

s = Student('Alice', 20, '12BD123123', 3.8)

s.greeing()

print(s)


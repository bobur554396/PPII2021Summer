import json

student = {
  'ID': '12BD123',
  'name': 'Alice',
  'age': 20,
  'gpa': 3.8
}

print(type(student))

student_str = json.dumps(student) # serializing dictionary object to str
print(student_str)
print(type(student_str))

student_dict = json.loads(student_str) # deserializing back to dictionary
print(student_dict)
print(type(student_dict))

print(student_dict['age'])
print(student_dict['name'])


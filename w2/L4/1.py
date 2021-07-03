# Regular Expression
import re

txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
x = re.search("ra.+Sp", txt)

if x:
  print(x.start())
  print(x.end())
  print(x.group())
  print(x.span())

if x:
  print("YES! We have a match!")
else:
  print("No match")




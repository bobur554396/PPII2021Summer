import re

txt = "The    rain   in       Spain"

# x = re.split("\s", txt)
# x = re.split("\s+", txt)
x = re.split("\s+", txt, maxsplit=1)

print(x)

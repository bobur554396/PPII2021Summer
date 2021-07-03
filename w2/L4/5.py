import re

txt = "The       rain        in         Spain"
# x = re.sub("\s", "9", txt)  # The9999rain9999in9999Spain
# x = re.sub("\s+", "9", txt)  # The9rain9in9Spain

x = re.sub("\s+", " ", txt)  # The rain in Spain

print(x)

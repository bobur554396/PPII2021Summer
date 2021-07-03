"""
Examples from text: 

[aA]lma -------> Alma, alma
[0123456789] <=>  [0-9]  <=>  \d -----> all digits
\+?[7|8]\(?\d{3}\)?\d{3}-?\d{2}-?\d{2} ----> 
      77071112233
      +77071112233
      +7(707)1112233
      +7(707)111-22-33
      8(707)111-22-33
      

[a-zA-Z]+@[a-zA-Z]{2,10}\.[a-zA-Z]{2,5}   <------>  \w+@\w{2,10}\.\w{2,5}





\+{0,1}   <=>  \+?


\+\d{11} ------->    +77071112233
"""
import re

email_pattern = re.compile(r'\w+@\w{2,10}\.\w{2,5}')


f = open('in.txt', 'r')

text = f.read()


res = re.findall(email_pattern, text)

print(res)


f.close()

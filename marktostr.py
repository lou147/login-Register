import re


markdown = '### 123,*456*, ``` python``` '
pattern = '123'
str1 = re.sub(pattern, '', markdown)
print(str1)

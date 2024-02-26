#\d : Matches any digit char
#\D : Matches any non-digit char
#\w : Matches any word char(alphanumeric+underscore)
#\W : Matches any non-word char
#\s : Matches any whitespace char
#\S : Matches any non-whitespace char
#\b : Matches a word boundary
#\A : startwith
#\Z : endswith
#. : matches every char

import re

# text = "Hello, my phone number is 123"
# pattern = r"\S"
# res = re.finditer(pattern,text)
# for x in res:
#     print(x.start(),"->",x.group())

# text = "Hello, my phone number is 123"
# pattern = r"\b123\b"  #\b is used to find specific words
# res = re.finditer(pattern,text)
# for x in res:
#     print(x.start(),"->",x.group())
    
# text = "Hello, my phone number is 123"
# pattern = r"\AHello"  
# res = re.finditer(pattern,text)
# for x in res:
#     print(x.start(),"->",x.group())

# text = "Hello, my phone number is 123"
# pattern = r"123\Z"  
# res = re.finditer(pattern,text)
# for x in res:
#     print(x.start(),"->",x.group())
    
# text = "Hello, my phone number is 123"
# pattern = r"."  #It returns all the string seperately.
# res = re.finditer(pattern,text)
# for x in res:
#     print(x.start(),"->",x.group())
    
# . is showing all strings, but what if we want to find '.' in our data.   
# text = "Hello. my phone number is 123"
# pattern = r"\."  # To ignore any special symbol, we add backslash to it
# res = re.finditer(pattern,text)
# for x in res:
#     print(x)
    
# text = "Hello, my[]phone number is 123"
# pattern = r"\[\]"  # To ignore any special symbol, we add backslash to it
# res = re.finditer(pattern,text)
# for x in res:
#     print(x)

# text = "Hello, my\\\phone number is 123"
# pattern = r"\\"  # To ignore any special symbol, we add backslash to it
# res = re.finditer(pattern,text)
# for x in res:
#     print(x)

text_data = """Today is 2023-10-02, and I have a meeting scheduled for
2023-10-05"""

pattern = r"\d{4}-\d{2}-\d{2}"
res = re.finditer(pattern,text_data)
for x in res:
    print(x)
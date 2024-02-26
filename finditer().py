import re

pattern = re.compile("ab",re.IGNORECASE)
data = "abaababa"

res = re.finditer(pattern,data)

for i in res:
    print(i.group())# used to group all the matched patterns
    print(i.start())# returns the first occured index of every matched pattern
    print(i.end())# returns the ending index of every matched pattern
    # span = (i.start(),i.end())
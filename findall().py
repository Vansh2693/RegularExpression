import re

pattern = re.compile("ab",re.IGNORECASE)
data = "abaababa"

res = re.findall(pattern,data)#returns a list of matched pattern

for i in res:
    print(i)
    
#finditer() method is space efficient as memory allocation of items does not take place
#whereas in findall() all the items have memory allocation
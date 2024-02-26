import re
pattern = "PYTHON"

data = "python is very powerful and python has lots of features"

match = re.search(pattern,data,re.IGNORECASE)# used re.IGNORECASE to ignore the case of words

print(match)
print(type(match))

if match:
    print("Found!",match.group()) # object_name.group() function is used to get the pattern searched in the data
else:
    print("Not Found!")
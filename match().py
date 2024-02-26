import re
pattern = r"python" # raw string('r') is used to ignore the escape sequences

data = "hello, python is very powerful and python has lots of features"

match = re.match(pattern,data,)# searches for pattern occurence in the beginning

print(match)
print(type(match))

if match:
    print("Found!",match.group()) # object_name.group() function is used to get the pattern searched in the data
else:
    print("Not Found!")
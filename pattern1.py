import re
pattern = "dog|cat"
data = " I saw Dog running behind cat and cat climbed but dog couldn't"

match_iter = re.finditer(pattern,data,re.IGNORECASE)
count = 0

for i in match_iter:
    print(i)
    count+=1
print("Count:",count)

# These functions find all non-overlapping matches of a regular expression pattern in a given string

pattern1 = "bb"
data1 = "bbbababa"

print(re.findall(pattern1,data1))
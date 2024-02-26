import re
# #find digits in given data
# pattern = r'[^A-Za-z0-9]'#carrot symbol is used to neglect the values
# data = "The price is $100."
# res = re.finditer(pattern,data)
# for i in res:
#     print(i)
    
#use case: 
#condition for password: 1. contains atleast one digit or atkeast one uppercase letter

pattern1 = r'[A-Z0-9]'
data1 = input("Enter your password:")
res = re.findall(pattern1,data1)

if res:
    print("Valid password")
else:
    print("Write a valid password")

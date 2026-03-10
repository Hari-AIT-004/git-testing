# a= ["a","e","i","o","u","i","j"]
# b=["i","j","k","l","a","m","o","e","i"]

# c=[]

# for c in a and b:
#     if a==b and b==a:
#         continue
#     else:
#         #c=append(a,b)
#         print(c)


# a= ["a","e","i","o","u","i","j"]
# b=["i","j","k","l","a","m","o","e","i"]

# c=a + b
# e=[]
# for d in c:
#     if d not in e:
#         print(e.append(d))
#     else:
#         continue
# print(e)

    

a= ["a","e","i","o","u","i","j"]
b=["i","j","k","l","a","m","o","e","i"]

#c=a+b
# result = list(dict.fromkeys(c))
# print(result)

# result= list(set(a+b))
# print(result)

result=[]
for c in a+b:
    if c not in result:
        result.append(c)

print(result)
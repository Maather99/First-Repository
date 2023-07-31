n=3
str="Python is a popular programming language"
list = []
text = str.split(" ")
for x in text:
    if len(x) > n:
        list.append(x)
print(list)
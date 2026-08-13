s = input()

result = ""
for i in range(len(s)):
    if s[i].isupper():
        if i != 0:
            result += "_" + s[i].lower()
        else:
            result += s[i].lower()
    else:
        result += s[i]

print(result)
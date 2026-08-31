s = input()
words = s.split(" ", 1)

if len(words) > 1:
    print(words[0].upper() + " " + words[1])
else:
    print(words[0].upper())
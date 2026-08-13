sentence = input()

vowels = "AEIOUaeiou"
result = ""

for char in sentence:
    if char not in vowels:
        result += char

print(result)
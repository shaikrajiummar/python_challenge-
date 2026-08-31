def count_the_vowels(word):
    # Complete this function
    count = 0
    for char in word:
        if char in "aeiou":
            count += 1
    return count


word = input()
# Call the count_the_vowels function
result = count_the_vowels(word)
print(result)
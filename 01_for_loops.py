# 01_for_loops.py
# ==============================================================================
# Learn Python For Loops
# For loops are used to iterate over a sequence (list, tuple, dictionary, set, string)
# or a range of numbers.
# ==============================================================================

print("--- 1. Looping over a Range of Numbers ---")
# range(stop) -> iterates from 0 up to (but not including) stop
print("Iterating from 0 to 4:")
for i in range(5):
    print(f"  Current value: {i}")

print("\nIterating from 1 to 5:")
# range(start, stop) -> iterates from start up to (but not including) stop
for i in range(1, 6):
    print(f"  Count: {i}")

print("\nIterating with a step (even numbers from 2 to 10):")
# range(start, stop, step) -> steps by the specified value
for i in range(2, 11, 2):
    print(f"  Even number: {i}")


print("\n--- 2. Looping over a List ---")
fruits = ["apple", "banana", "cherry", "dragonfruit"]
print("My favorite fruits:")
for fruit in fruits:
    print(f"  - {fruit.capitalize()}")


print("\n--- 3. Looping with Index and Value (enumerate) ---")
# Using enumerate() allows you to track the index of each item in a list
for index, fruit in enumerate(fruits, start=1):
    print(f"  Fruit #{index} is {fruit}")


print("\n--- 4. Looping over a String ---")
word = "Python"
print(f"Spelling '{word}' letter by letter:")
for letter in word:
    print(f"  Letter: {letter}")


print("\n--- 5. Looping over a Dictionary ---")
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Looping through keys only:")
for name in student_scores:
    print(f"  Student: {name}")

print("\nLooping through keys and values together (using .items()):")
for name, score in student_scores.items():
    print(f"  {name} scored {score}%")

print("\n==============================================================================")
print("Well done! You have completed the For Loops section. Run 02_while_loops.py next!")
print("==============================================================================")

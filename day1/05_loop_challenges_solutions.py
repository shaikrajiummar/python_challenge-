# 05_loop_challenges_solutions.py
# ==============================================================================
# Python Loops Challenges - SOLUTIONS
# Compare your solutions with the implementations below!
# ==============================================================================

# ------------------------------------------------------------------------------
# CHALLENGE 1: Sum of Even Numbers
# Task: Write a loop to calculate the sum of all even numbers from 1 to 100 (inclusive).
# Expected Output: 2550
# ------------------------------------------------------------------------------
print("--- Challenge 1: Sum of Even Numbers ---")
even_sum = 0
for num in range(2, 101, 2):
    even_sum += num

print(f"Correct Answer: {even_sum} (Expected: 2550)")


# ------------------------------------------------------------------------------
# CHALLENGE 2: Factorial Calculation
# Task: Calculate the factorial of a given number (e.g., n = 5) using a while loop.
# Expected Output: 120
# ------------------------------------------------------------------------------
print("\n--- Challenge 2: Factorial of 5 ---")
n = 5
factorial = 1
temp = n
while temp > 0:
    factorial *= temp
    temp -= 1

print(f"Correct Answer: {factorial} (Expected: 120)")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Reverse a String
# Task: Given a string, use a loop to reverse it.
# Expected Output: "nohtyP"
# ------------------------------------------------------------------------------
print("\n--- Challenge 3: Reverse a String ---")
text = "Python"
reversed_text = ""
# We can loop through the string backwards, or prepending each character to the start
for char in text:
    reversed_text = char + reversed_text

print(f"Correct Answer: '{reversed_text}' (Expected: 'nohtyP')")


# ------------------------------------------------------------------------------
# CHALLENGE 4: Fibonacci Sequence
# Task: Generate and print the first 10 numbers in the Fibonacci sequence.
# Expected Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# ------------------------------------------------------------------------------
print("\n--- Challenge 4: Fibonacci Sequence ---")
fibonacci_sequence = []
a, b = 0, 1
for _ in range(10):
    fibonacci_sequence.append(a)
    a, b = b, a + b

print(f"Correct Answer: {fibonacci_sequence} (Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Draw a Pyramidal Arrow
# Task: Write nested loops to draw the arrow pattern using stars (*).
# ------------------------------------------------------------------------------
print("\n--- Challenge 5: Draw a Pyramidal Arrow ---")
max_stars = 3

# Top half and peak
for i in range(1, max_stars + 1):
    for j in range(i):
        print("*", end="")
    print()

# Bottom half
for i in range(max_stars - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n==============================================================================")
print("All challenges solved! You are now a loop expert. Keep practicing! 🚀")
print("==============================================================================")

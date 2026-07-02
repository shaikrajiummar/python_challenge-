# 04_nested_loops.py
# ==============================================================================
# Learn Python Nested Loops
# A nested loop is a loop inside the body of another loop. 
# The "inner loop" will execute all its iterations for every single iteration of the "outer loop".
# ==============================================================================

print("--- 1. Printing a 2D Coordinate Grid ---")
# Outer loop controls rows
for row in range(3):
    # Inner loop controls columns
    for col in range(3):
        print(f"  (Row {row}, Col {col})", end=" ")
    print()  # Newline after each row is completed


print("\n--- 2. Drawing Patterns (Right-Angled Triangle) ---")
# Let's draw a triangle of stars
height = 5
print(f"Drawing a triangle of height {height}:")
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()  # Newline after printing the stars in a row


print("\n--- 3. Iterating Over a 2D List (Matrix) ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elements of the 3x3 matrix:")
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()


print("\n--- 4. Real-world analogy: Multiplication Table ---")
print("Simple 1-5 multiplication table:")
for i in range(1, 6):
    for j in range(1, 6):
        # Format output to line up columns nicely
        print(f"{i * j:3}", end="")
    print()

print("\n==============================================================================")
print("Fantastic! You have completed all main concepts. Now try the challenges in 05_loop_challenges.py!")
print("==============================================================================")

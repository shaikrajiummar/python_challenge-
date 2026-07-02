# 03_loop_control.py
# ==============================================================================
# Learn Python Loop Control Statements
# Loop control statements change execution from its normal sequence.
# - break: Terminates the loop statement and transfers execution to the statement immediately following the loop.
# - continue: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# - pass: Used when a statement is required syntactically but you do not want any command or code to execute.
# - else: Executed when the loop finishes iterating completely, but NOT if it was terminated by a 'break'.
# ==============================================================================

print("--- 1. The 'break' Statement ---")
print("Searching for the number 5 in range 1-10. We will stop when we find it:")
for number in range(1, 11):
    print(f"  Checking: {number}")
    if number == 5:
        print("  Found 5! Breaking out of the loop early.")
        break  # Immediately exits the for loop
print("Loop ended.")


print("\n--- 2. The 'continue' Statement ---")
print("Printing only odd numbers from 1 to 8 (skipping evens):")
for number in range(1, 9):
    if number % 2 == 0:
        continue  # Skips the rest of this iteration and goes to the next number
    print(f"  Odd number: {number}")


print("\n--- 3. The 'pass' Statement ---")
# pass is a null operation. It's useful as a placeholder when writing code.
print("Iterating and doing nothing for even numbers (using pass):")
for number in range(1, 5):
    if number % 2 == 0:
        pass  # Placeholder - does nothing but prevents SyntaxError
    else:
        print(f"  Processed odd number: {number}")


print("\n--- 4. Python's Unique Loop 'else' Clause ---")
# The else block executes ONLY if the loop completed successfully without hitting a break.
print("Example A: Searching for a clean item (no break is hit):")
grocery_list = ["apple", "banana", "orange"]
for item in grocery_list:
    print(f"  Checking {item}...")
    if item == "poison_ivy":
        print("  Danger found! Breaking!")
        break
else:
    # This runs because we went through the whole list and did not hit 'break'
    print("  ✅ Grocery list is safe! (No break statement was hit)")

print("\nExample B: Searching for a bad item (break is hit):")
dangerous_list = ["apple", "poison_ivy", "orange"]
for item in dangerous_list:
    print(f"  Checking {item}...")
    if item == "poison_ivy":
        print("  ⚠️ Danger found! Breaking out immediately!")
        break
else:
    # This will NOT run because a break was encountered
    print("  ✅ This will not be printed because the list had danger.")

print("\n==============================================================================")
print("Excellent! Loop controls are vital for flow control. Onwards to 04_nested_loops.py!")
print("==============================================================================")

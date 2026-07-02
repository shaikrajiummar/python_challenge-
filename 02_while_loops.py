# 02_while_loops.py
# ==============================================================================
# Learn Python While Loops
# A while loop repeatedly executes a target statement as long as a given condition is true.
# WARNING: Always ensure the condition eventually becomes False, otherwise you get an "Infinite Loop"!
# ==============================================================================

print("--- 1. Basic Counting with a While Loop ---")
count = 1
while count <= 5:
    print(f"  Count is: {count}")
    count += 1  # Crucial! If we don't increment, count remains 1 and the loop runs forever.


print("\n--- 2. Decrementing (Countdown) ---")
countdown = 5
while countdown > 0:
    print(f"  T-minus {countdown}...")
    countdown -= 1
print("  🚀 Liftoff!")


print("\n--- 3. Using a Sentinel Value (Looping until stopped) ---")
# Often used when you don't know beforehand how many times the loop should run.
import random

target_number = 7
current_guess = 0
attempts = 0

print("Generating random numbers from 1 to 10 until we find 7...")
while current_guess != target_number:
    current_guess = random.randint(1, 10)
    attempts += 1
    print(f"  Attempt {attempts}: Generated {current_guess}")

print(f"🎉 Success! Found {target_number} in {attempts} attempts.")


print("\n--- 4. Simulated User Input Validation ---")
# Let's simulate checking if a user entered a valid positive number
# (Instead of raw input which blocks execution, we will simulate input trials)
simulated_inputs = [-5, -2, 0, 4, 10]
input_index = 0

print("Simulating input validation: We need a number greater than 0.")
user_number = -1

while user_number <= 0:
    if input_index < len(simulated_inputs):
        user_number = simulated_inputs[input_index]
        print(f"  User entered: {user_number}")
        input_index += 1
    else:
        break  # Safe fallback if simulation runs out of inputs

    if user_number <= 0:
        print("    ❌ Invalid input! Please enter a number greater than 0.")
    else:
        print(f"    ✅ Thank you! Valid number {user_number} received.")

print("\n==============================================================================")
print("Great! You have mastered While Loops. Check out 03_loop_control.py next!")
print("==============================================================================")

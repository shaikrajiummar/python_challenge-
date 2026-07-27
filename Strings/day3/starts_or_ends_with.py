# Read two input strings
S1 = input()
S2 = input()

# Check if S1 starts with S2 or ends with S2
starts_or_ends = S1.startswith(S2) or S1.endswith(S2)

# Print the validation result (True or False)
print(starts_or_ends)

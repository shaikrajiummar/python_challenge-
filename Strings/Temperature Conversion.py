s = input().strip()

unit = s[-1]
val = float(s[:-1])

# Convert input value to Celsius first
if unit == "C":
    c = val
elif unit == "F":
    c = (val - 32) * 5 / 9
elif unit == "K":
    c = val - 273

# Derive Fahrenheit and Kelvin from Celsius
f = (c * 9 / 5) + 32
k = c + 273

# Round and print results
print(f"{round(c, 2)}C")
print(f"{round(f, 2)}F")
print(f"{round(k, 2)}K")
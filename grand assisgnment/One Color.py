s = input()

# Count the occurrences of 'R' and 'G'
count_r = s.count("R")
count_g = s.count("G")

# The minimum changes required is the smaller of the two counts
print(min(count_r, count_g))
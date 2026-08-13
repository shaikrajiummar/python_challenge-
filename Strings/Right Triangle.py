n = int(input())

for i in range(1, n + 1):
    row_str = ""
    
    # Numbers counting UP from 1 to i
    for j in range(1, i + 1):
        row_str += str(j)
        
    # Numbers counting DOWN from i-1 to 1
    for j in range(i - 1, 0, -1):
        row_str += str(j)
        
    print(row_str)
rows = 5
# Upper half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# Lower half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

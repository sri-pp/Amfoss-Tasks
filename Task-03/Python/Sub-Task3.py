def pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "* " * (i + 1))
    for j in range(rows - 1, 0, -1):
        print(" " * (rows - j) + "* " * j)
rows = int(input("Enter the number of rows for the diamond pattern: "))
pyramid(rows)

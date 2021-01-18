def findNumPaths(cols, rows):
    if cols == 1 and rows == 1:
        return 1
    elif cols == 1:
        return findNumPaths(cols, rows-1)
    elif rows == 1:
        return findNumPaths(cols-1, rows)
    else:
        return findNumPaths(cols-1, rows) + findNumPaths(cols, rows-1)

print(findNumPaths(3,3))

def binarySearch(values):
    top = len(values) - 1
    mid = (len(values) - 1) // 2
    bottom = 0

    if (bottom == top):
        # base case
        return values[0]

    while True:

        if values[mid] > values[mid + 1] and values[mid] > values[mid - 1]:
            return mid

        elif values[mid] >= values[mid - 1] and values[mid] <= values[mid + 1]:
            
            mid = (top + mid) // 2
        else:
            mid = (bottom + mid) // 2
            
              


    
print(binarySearch([1,2,3,4,3,2,1]))

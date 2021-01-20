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


def checkBitonic(numbers):

    reverse = list(reversed(numbers))
    pos = 0

    if (len(numbers) == 1) or not numbers:
        return False

    pos = binarySearch(numbers)


    # increasing part
    first_half = numbers[0:pos]
    # decreasing part
    second_half = numbers[pos:]


    if not first_half or not second_half:
        return False

    if list(reversed(second_half)) == sorted(second_half) and (first_half == sorted(first_half)):
        return True    



print(checkBitonic([1, 2, 3 ,4 ,5, 4 ,3]))


# N
# sorted is log(N) in python
# all complexity should be log(N) + Nlog(N)
# so overall still Nlog(N) not log(N)
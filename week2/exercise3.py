def binSearch(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        mid = (start + end) // 2
        
        
        step = step+1
        if element == array[mid]:
            return mid



        if element < array[mid]:
            end = mid - 1


        else:
            start = mid + 1
    return -1



def highestValuePos(values):
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


def checkBitonic(numbers, value):

    reverse = list(reversed(numbers))
    pos = 0

    if (len(numbers) == 1) or not numbers:
        return False

    pos = highestValuePos(numbers)


    # increasing part
    first_half = numbers[0:pos]
    # decreasing part
    second_half = numbers[pos:]


    if not first_half or not second_half:
        return False

    # if list(reversed(second_half)) == sorted(second_half) and (first_half == sorted(first_half)):
    #     return True    


    return binSearch(first_half, value) != -1 or binSearch(second_half, value) != -1



print(checkBitonic([1, 2, 3 ,4 ,5, 4 ,3], -1))



# finding the highest value by splitting array in half and checking the center value whether it is more than
# the left element and less than the next right element
# this should be O(log(N))
# Then we use binary search to find the value in the increasing part and the descending part, this is O(Log(N))




# Old comments
# N
# sorted is log(N) in python
# all complexity should be log(N) + Nlog(N)
# so overall still Nlog(N) not log(N)

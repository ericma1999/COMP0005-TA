import math
def checkBitonic(numbers):

    reverse = list(reversed(numbers))
    pos = 0

    if (len(numbers) == 1) or not numbers:
        return False

    for i in range(0, len(numbers)):

        if (numbers[i] > numbers[i + 1]):
            pos = i + 1
            break

        if(reverse[i] > reverse[i+1]):
            pos = len(numbers) - (i + 1)
            break


    first_half = numbers[0:pos]
    second_half = numbers[pos:]


    if not first_half or not second_half:
        return False

    if list(reversed(second_half)) == sorted(second_half) and (first_half == sorted(first_half)):
        return True

def findMaxBitonic(values):
    top = len(values) - 1
    bot = 0
    while(True):
        mid = round((top+bot)/2)
        val = values[mid]
        left = values[mid-1]
        right = values[mid+1]
        if(val >= left and val >= right):
            return mid
        elif(val >= left and val <= right):
            bot = mid
        else:
            top = mid

def binarySearchDec(values, target):
    top = len(values) - 1
    bot = 0
    while(True):
        mid = (top+bot)//2
        val = values[mid]
        if(val == target):
            return True
        if(bot == top):
            return False
        elif(val > target):
            bot = mid+1
        else:
            top = mid-1

def binarySearchAsc(values, target):
    top = len(values) - 1
    bot = 0
    while(True):
        mid = (top+bot)//2
        val = values[mid]
        if(val == target):
            return True
        if(bot == top):
            return False
        elif(val < target):
            bot = mid+1
        else:
            top = mid-1

def checkNumBitonic(values,target):
    midIndex = findMaxBitonic(values)
    if values[midIndex] == target:
        return True
    return (binarySearchAsc(values[:midIndex], target) or binarySearchDec(values[midIndex:], target))

print(checkNumBitonic([1, 3, 4, 6, 9, 14, 11, 7, 2, -4, -9], 1))

#print(checkBitonic([1, 3, 4, 6, 9, 14, 11, 7, 2, -4, -9] ))



# sorted is Nlog(N) in python
# all complexity should be log(N) + Nlog(N)
# so overall still Nlog(N) not log(N)

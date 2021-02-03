def enhancedFlip(i,j,pancakes):
    sub = pancakes[i:j+1]
    sub.reverse()
    pancakes[:] = pancakes[0:i] + sub + pancakes[j+1:]

def pancakeSort(pancakes):
    count = 0
    maxNum = 0
    flippedIndecies = []

    length = len(pancakes)
    maxIndex = None
    minIndex = None

    currentIndex = 0

    value = None
    shouldBreak = False

    while True:
        exist_disorder = False
        for i in range(1, length - 1):
            if pancakes[i] < pancakes[i+1] and pancakes[i] < pancakes[i - 1]:
                maxIndex = i
                value = pancakes[i]
                exist_disorder = True
                break

        if not exist_disorder:
            break
        for j in range(0, length - 1):
            if pancakes[j] > value:
                minIndex = j
                break
     
        enhancedFlip(minIndex, maxIndex, pancakes)


if __name__ == "__main__":
    pancakes =  [1, 8, 9, 3, 2, 7, 6, 5, 4, 10]
    pancakeSort(pancakes)
    print(pancakes)
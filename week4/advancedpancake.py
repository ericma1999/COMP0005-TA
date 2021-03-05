def superFlip(i,j,pancakes):
    sub = pancakes[i:j+1]
    sub.reverse()
    pancakes[:] = pancakes[0:i] + sub + pancakes[j+1:]

def pancakeSort(pancakes):
    length = len(pancakes) + 1
    pancakes.insert(length, max(pancakes) + 1)

    maxIndex = None
    minIndex = None

    currentIndex = 0

    value = None
    swaps = []
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
        swaps += [[minIndex + 1, maxIndex + 1]]
        superFlip(minIndex, maxIndex, pancakes)

    pancakes.pop()

    print(swaps)



if __name__ == "__main__":
    # pancakes =  [1, 8, 9, 3, 2, 7,15,22,1000,500,32]
    pancakes = [1, 8, 7, 6 ,5 ,4 ,2, 3, 9] 
    # breaks here
    # pancakes = [1, 8, 9, 3, 2, 7, 6, 5, 4, 10]
    pancakeSort(pancakes)
    print(pancakes)
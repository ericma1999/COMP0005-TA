
# Cheat version
def insertionSort(array):
    negativeNumbers = 0
    for i in range(0, len(array)):
            if array[i] < 0:
                negativeNumbers+=1
            for j in range(i, 0, -1):
                if (array[j] < array[j-1]):
                    store = array[j-1]
                    array[j-1] = array[j]
                    array[j] = store


    positives = array[negativeNumbers::]
    negatives = array[:negativeNumbers]

    result = []

    while len(positives) > 0 or len(negatives) > 0:
        if len(positives) > 0:
            result.append(positives.pop(0))
        
        if len(negatives) > 0:
            result.append(negatives.pop())

    print(result)



test = [-8, 1, 2, 0, -4, 6, 12, 5, -10, 16, 7, 11]
insertionSort(test)
print(test)
# print(test)
# separtePosAndNegatives()
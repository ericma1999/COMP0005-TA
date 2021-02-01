
# def insertionSort(array):
#     for i in range(0, len(array)):
#         for j in range(i, 0, -1):
#             if (array[j] < array[j-1]):
#                 store = array[j-1]
#                 array[j-1] = array[j]
#                 array[j] = store



def insertionSort(word):
    for i in range(0, len(word)):
        for j in range(i, 0, -1):
            if (word[j] < word[j-1]):
                word = swap(word, j-1,j)
    
    return word
    
def mergeSort(arr, arr2):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
        L2 = arr2[:mid]
 
        # into 2 halves
        R = arr[mid:]
        R2 = arr2[mid:]
 
        # Sorting the first half
        mergeSort(L, L2)
        
 
        # Sorting the second half
        mergeSort(R,R2)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                arr2[k] = L2[i]
                i += 1
            else:
                arr[k] = R[j]
                arr2[k] = R2[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            arr2[k] = L2[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            arr2[k] = R2[j]
            j += 1
            k += 1
    


def swap(value, i, j):
    return ''.join((value[:i], value[j], value[i+1:j], value[i], value[j+1:]))



def findAnagrams(words):
    secondList = []

    for word in words:
        sortedWord = insertionSort(word)
        secondList.append(sortedWord)

    mergeSort(secondList, words)
    i = 0
    currentValue = ""
    while(i < len(secondList)):
        if i == 0:
            currentValue = secondList[i]
            i+=1
            continue

        if secondList[i] == currentValue:
            i+=1
            continue
        else:
            deletedWords = words[:i]
            print(deletedWords)
            secondList = secondList[i::]
            words = words[i::]
            i = 0

        # print(words)
    print(words)

if __name__ == "__main__":
    
    words = ["eat", "tea", "part", "ate", "trap", "pass"]
    findAnagrams(["eat", "tea", "part", "ate", "trap", "pass"])
words = ["eat", "tea", "part", "ate", "trap", "pass"]

def sort(word):
    for i in range(0,len(word)):
        for j in range(i, 0, -1):
            if (word[j] < word[j-1]):
                word = swap(word, j-1, j)
    return word

def swap(value, i, j):
    return ''.join((value[:i], value[j], value[i+1:j], value[i], value[j+1:]))

def sortArray(vals):
    newList = []
    for word in vals:
        newList.append(sort(word))
    return newList


def mergeSort(arr,arr2):
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
        mergeSort(L,L2)


        # Sorting the second half
        mergeSort(R,R2)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                arr2[k] =L2[i]
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

def anagrams(words, words2):
    groups = [[]]
    count = 0
    value = words.pop(0)
    groups[count].append(words2.pop(0))
    while(len(words) > 0):
        while(value == words[0]):
            words.pop(0)
            groups[count].append(words2.pop(0))
        count += 1
        value = words.pop(0)
        groups.append([])
        groups[count].append(words2.pop(0))
    return groups

sortedWords = sortArray(words)
mergeSort(sortedWords,words)

print(sortedWords)
print(words)

print(anagrams(sortedWords, words))

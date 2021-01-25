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

print(sortArray(words))

pancakes = [3,2,4,1]

def flip(i,pancakes):
    sub = pancakes[0:i+1]
    sub.reverse()
    pancakes[:] = sub + pancakes[i+1:]

def pancakeSort(pancakes):
    count = len(pancakes)
    maxNum = 0
    flippedIndecies = []
    while(count > 0):
        maxNum = max(pancakes[0:count])
        if maxNum == pancakes[count-1]:
            count -= 1
        elif maxNum == pancakes[0]:
            flip(count-1, pancakes)
            count -= 1
            flippedIndecies.append(0)
        else:
            flippedIndecies.append(pancakes.index(maxNum))
            flip(pancakes.index(maxNum), pancakes)
            flip(count-1, pancakes)
            flippedIndecies.append(0)
            count -= 1
    return flippedIndecies

def enhancedFlip(i,j,pancakes):
    sub = pancakes[i:j+1]
    sub.reverse()
    pancakes[:] = pancakes[0:i] + sub + pancakes[j+1:]
    print(pancakes)

pancakes = [3,2,4,1]

def flip(i,pancakes):
    sub = pancakes[0:i+1]
    sub.reverse()
    pancakes[:] = sub + pancakes[i+1:]
    print(pancakes)

def pancakeSort(pancakes):
    count = len(pancakes)
    maxNum = 0
    while(count > 0):
        print(count)
        maxNum = max(pancakes[0:count])
        if maxNum == pancakes[count-1]:
            count -= 1
        elif maxNum == pancakes[0]:
            flip(count - 1, pancakes)
            count -= 1
        else:
            flip(pancakes.index(maxNum), pancakes)
            flip(count - 1, pancakes)
            count -= 1

print(pancakes)
pancakeSort(pancakes)
#print(pancakes)
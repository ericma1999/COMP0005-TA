costs = [2, 5, 3, 1, 7, 3, 4]
totalWeights = []
def climbStairs(stairs, currentWeight):
    minusFirst = stairs[1:]
    minusSecond = stairs[2:]
    if(len(stairs) <= 2):
        totalWeights.append(currentWeight + stairs[0])
    elif(len(stairs) != 3):
        climbStairs(minusFirst, currentWeight + stairs[0])
        climbStairs(minusSecond, currentWeight + stairs[1])
    else:
        climbStairs(minusFirst, currentWeight)
        climbStairs(minusSecond, currentWeight)

climbStairs(costs, 0)
print(min(totalWeights))

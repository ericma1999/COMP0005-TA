

# def minClimbingStairs(stairs):
#     length = len(stairs)

#     if not stairs:
#         return 0

#     output = 0
#     if(stairs[0] > stairs[1]):
#         output = stairs[1]
#     elif (stairs[0] < stairs[1]):
#         output = stairs[0]
#     else:
#         output = stairs[1]

#     print(output)

#     if (len(stairs) % 2 == 0):

#         return output + minClimbingStairs(stairs[2:])
#     else:
#         return output + minClimbingStairs(stairs[1:])




def minClimbingStairs(stairs):
    length = len(stairs)
    if len(stairs) == 1:
        return stairs[0]

    if not stairs:
        return 0

    output = 0
    if(stairs[0] > stairs[1]):
        output = stairs[1]
    elif (stairs[0] < stairs[1]):
        output = stairs[0]
    else:
        output = stairs[1]

    print(output)

    if (len(stairs) % 2 == 0):

        return output + minClimbingStairs(stairs[2:])
    else:
        return output + minClimbingStairs(stairs[1:])





print(minClimbingStairs([16, 19, 10, 12, 18]))

# print(minClimbingStairs([2, 5, 3, 1, 7, 3, 4]))
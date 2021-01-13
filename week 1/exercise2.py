# recursive version
## the space complexity is O(N) //not sure about this
### constant memory assignment of variables in each, but has more depth as n increases
## the time complexity is O(2^N) as the bigger value of N will generate more node trees.


def fibonacci(n):
    if n == 0:
        print("Error")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# iterative version

## the space complexity is O(N) as the total space required depends on N. Since if n increases the more loops.
## the time complexity is O(N) as the bigger value of N will require for iterations in the for loop.


def fibonacci_iterative(n):
    
    next_value = 1
    current_value = 1
    previous_value = 0

    if n <=0:
        print("Error")
        return

    if n == 1: return 0;

    for x in range(n - 2):
        next_value = current_value + previous_value
        previous_value = current_value
        current_value = next_value

    return next_value



# print(fibonacci(5))
# print(fibonacci_iterative(5))
for x in range(1,6):
    print(fibonacci_iterative(x))
def linear_search(arr, target):
    # Your code here
    # if target in arr:
    #     return arr.index(target)
    for index, element in enumerate(arr):  #O(n) -- Big O notation
        if element == target:  # O(1)
             return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):  # O(log n) if emplimented correctly.


    # Your code here
    index_left = 0
    index_right = len(arr) -1  # length of arr -1 this be 0

    while index_left <= index_right: # O(n) What happens inside the loop
        middle = (index_left + index_right) // 2 # this is like .floor()
        if arr[middle] > target:  # this cuts the itteration in half as it keeps skipping things.
            index_right = middle -1   # O(1) time complexity. basic assignment doesn't kill it.
        elif arr[middle] < target: # cuts in half again
            index_left = middle +1 # O(1) time complexity. basic assignment doesn't kill it.
        else: # stop itteration. Best case. # O(1) huzzah!
            return middle  # It did it!

    return -1  # not found, Nah it doesn't exist.

# Big O is checking if the worst case happens how long does it take.
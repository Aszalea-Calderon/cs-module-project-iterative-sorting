# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                print("BEFORE DAT SWITCH:",arr)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("AFTER DAT SWITCH:",arr)

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# def counting_sort(arr, maximum=None):
#     # Your code here https://www.cs.usfca.edu/~galles/visualization/CountingSort.html, https://visualgo.net/bn/sorting
#     if len(arr) == 0: # If arr is none, nah. Bye
#         return
#     max_pointer = int(max(arr)) #this will check for the max number in the arr
#     if min(arr) < 0: # This checks if it any number is a negative
#         print("Nah, why you putting in negitives. That's so mean.")
#     # Buckets, Output and count
#     output_bucket = [0] * len(arr) # This makes a list with 0's, this initializes it with however many zeros there are for the length of array. If you didn't put a number it would make multiple lists
#     count_bucket = [0 for _ in range(max_pointer +1)] # this does the same as above. But PYTHON *sssssss*
#     for element in arr:
#         count_bucket[element] +=1
#     for i in range(1,len(count_bucket)): # odd
#         count_bucket[i] += count_bucket[i - 1]
#     for i in range(len(arr) -1, -1, -1): # range takes 3 arguments, start, stop, and by how much,
#         output_bucket[count_bucket[arr[i]-1 ]] = arr[i]
#         count_bucket[arr[i]] -= 1
#     for i in range(len(arr)):
#         arr[i] = output_bucket[i]
#     return arr


def counting_sort(arr, maximum=None):
    if arr == []:
        return arr
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    res = []
    temp = [0 for _ in range(0, max(arr) + 1)]
    for i in arr:
        temp[i] += 1
    for i in range(0,len(temp)):
        while temp[i] > 0:
            res.append(i)
            temp[i] -= 1
    return res




import random

'''
The sort_and_count and merge_and_count functions correspond to the pseudocode provided in the PDF document.
The remaining part of the file is dedicated to verifying the accuracy of our algorithm's output.
'''


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Our O(nlogn) Algorithm ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def merge_and_count(a, b):
    r = 0  # r is a variable to store the number of inversions
    i, j = 0, 0 # i, j are the indexes of a and b respectively
    m = len(a) # m = size of a
    n = len(b) # n = size of b

    # Loop to count inversions
    while i < m and j < n:
        if 2*b[j] < a[i]:
            # If 2*b[j] is less than a[i], there are inversions because all remaining elements in a are greater than 2*b[j]
            r += m - i # Increment count of inversions by the remaining elements in a
            j += 1 # Move to the next element in b
        else:
            i += 1 # Move to the next element in a
    i, j = 0, 0 # Reset i and j to 0 for merging
    c = [None] * (m + n) # Create a new array/list c to store merged elements
    
    # Loop to merge the two arrays a and b into c while maintaining sorted order
    for k in range(m + n):
        if i < m and (j >= n or a[i] < b[j]):
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
    return (r, c) # Return the count of inversions and the merged array c


def sort_and_count(A, low, high):
    if low == high:  # Base case: if the array has only one element
        return (0, [A[low]])

    mid = (low + high) // 2  # Calculate the midpoint correctly
    (r1, A1) = sort_and_count(A, low, mid)  # Recur on the left half
    (r2, A2) = sort_and_count(A, mid + 1, high)  # Recur on the right half
    (r, A) = merge_and_count(A1, A2)  # Merge the sorted halves and count inversions
    
    return (r1 + r2 + r, A)  # Return total inversions and merged array

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''



'''
~~~~~~~~~~~ Other implementations to check the correctness of our agorithm ~~~~~~~~~~~~~~
'''

# O(n^2) function to calculate strong reversals ---- This function helps us to check if the result of our function is correct
def count_strong_reversals(A):
    count = 0
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > 2*A[j]:
                count += 1
    return count


if __name__ == "__main__":

    print("Test Algorithm")
    print("----------------------")

    # Generate a list of 20 random numbers
    random_numbers = [random.randint(1, 100) for _ in range(20)]
    print("Generated a list of 20 random integers between 1 and 100 to test our algorithm:", end=" ")
    print(random_numbers)

    # print the output of our algorithm for the random array
    print("The output from our Algorithm O(nlogn) is: ", end="")
    algorithm_result = sort_and_count(random_numbers, 0, len(random_numbers) - 1)
    print(algorithm_result)

    # Compare our result to that of another easy-to-program algorithm to verify our correctness
    print("We are comparing the output of our algorithm to that of an O(n^2) algorithm to check for matches")
    print("Algorithm O(n^2) output: ", end="")
    other_algorithm_result = count_strong_reversals(random_numbers)
    print(other_algorithm_result)
    print("Same output = ", algorithm_result[0] == other_algorithm_result)


    '''
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
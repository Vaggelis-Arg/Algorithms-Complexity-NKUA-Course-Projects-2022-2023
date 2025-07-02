import random


def min_max(arr, low, high):
    if low == high: # Check if there is only one element
        return arr[low], arr[low]

    if high == low + 1: # Check if there are two elements
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    else:
        mid = (low + high) // 2

        # Recursively find min and max for the left and right subarrays
        min1, max1 = min_max(arr, low, mid)
        min2, max2 = min_max(arr, mid + 1, high)

        return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)] # Generate a random array of 10 elements
    print(arr)
    min_element, max_element = min_max(arr, 0, len(arr) - 1) # Find the minimum and maximum elements
    # Calculate the longest distance (maximum element - minimum element)
    print("Longest distance = Maximum element - Minimum element = ", max_element, " - ", min_element, " = ",  max_element - min_element)
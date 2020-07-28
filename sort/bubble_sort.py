
"""
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes
"""

def bubble_sort(source):
    is_sorted = False
    unsorted_len = len(source) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_len):
            if source[i] > source[i+1]:
                source[i], source[i+1] = source[i+1], source[i]
                is_sorted = False
        unsorted_len -= 1
    return source

if __name__ == "__main__":
    print(bubble_sort([4,6,1,3,9,2,7]))

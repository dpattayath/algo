
"""
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and
time complexity can be expressed as following recurrence relation.
    T(n) = 2T(n/2) + \Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in
case II of Master Method and solution of the recurrence is \Theta(nLogn).
Time complexity of Merge Sort is \Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.
Auxiliary Space: O(n)
Algorithmic Paradigm: Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes
"""

def merge_sort(source):
    if len(source) > 1:
        mid = len(source)//2 # Finding the mid of the sourceay
        L = source[:mid] # Dividing the sourceay elements
        R = source[mid:] # into 2 halves

        merge_sort(L) # Sorting the first half
        merge_sort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp sourceays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                source[k] = L[i]
                i+= 1
            else:
                source[k] = R[j]
                j+= 1
            k+= 1

        # Checking if any element was left
        while i < len(L):
            source[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            source[k] = R[j]
            j+= 1
            k+= 1
    return source

if __name__ == "__main__":
    print(merge_sort([4,6,1,3,9,2,6,7]))

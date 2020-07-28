
# O(n^2)
def inversionCount(q):
    n = len(q)
    total_bribes = 0
    for i in range(0, n):
        bribes = 0
        for j in range(i+1, n):
            if q[i] > q[j]:
                bribes += 1
        if bribes > 2:
            print("Too chaotic") # if more than 2 inversions
            break
        else:
            total_bribes += bribes
    else:
        print(total_bribes)

def inversionCountOptimized(q):
    n = len(q)
    swap = 0
    for i in range(n-1, -1, -1):
        if q[i] != i+1:
            if q[i-1] == (i+1):
                swap += 1
                q[i-1] = q[i]
                q[i] = (i+1)
            elif q[i-2] == (i+1):
                swap += 2
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = (i+1)
            else:
                print("Too chaotic")
                break
    else:
        print(swap)


"""
Sorted array
find the pairs less than the limit
"""
def sum_of_pairs(source, limit):
    count = 0
    i = len(source) - 1
    j = 0
    while j < i:
        if source[i] + source[j] < limit:
            count += i - j
            j += 1
        else:
            i -= 1
    return count

if __name__ == "__main__":
    print(sum_of_pairs([2,4,6,8,9], 14))

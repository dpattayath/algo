
def find_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + find_sum(lst[1:])

def find_count(lst):
    if len(lst) == 1:
        return 1
    return 1 + find_count(lst[1:])

def find_max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = find_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

if __name__ == "__main__":
    print(find_max([4,5,1,3,56,7]))
    print(find_sum([4,5,1,3,56,7]))
    print(find_count([4,5,1,3,56,7]))

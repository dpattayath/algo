
"""
num xor num => 0
0 xor num => num
"""
def lonely_integer(source):
    result = 0
    for i in source:
        result ^= i
    return result

print(lonely_integer([9,1,2,3,2,9,1,7,7]))

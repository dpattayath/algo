
"""
GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers
is the largest number that divides both of them.
Time Complexity: O(Log min(a, b))

If we substract smaller number from larger GCD doesn't change. So if we keep substracting repeatedly
the larger of two, we end up with GCD

modulo operator in Euclidean algorithm .

A simple solution is to find all prime factors of both numbers, then find union of all factors present in both numbers.
Finally return product of elements in union.
"""
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


"""
LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
For example LCM of 15 and 20 is 60 and LCM of 5 and 7 is 35.

An efficient solution is based on below formula for LCM of two numbers ‘a’ and ‘b’.
a x b = LCM(a, b) * GCD (a, b)
LCM(a, b) = (a x b) / GCD(a, b)
"""
def find_lcm(a, b):
    return int((a * b) / gcd(a,b))

def lcm_array(source):
    lcm = find_lcm(source[0], source[1])
    for i in range(2, len(source)):
        lcm = find_lcm(lcm, source[i])
    return lcm

"""
LCD for fractions 5/12 and 7/15 is 60.
We can write both fractions as 25/60 and
28/60 so that they can be added and
subtracted easily.

LCD for fractions 1/3 and 4/7 is 21.

LCD => LCM of denominators of the fractions
"""

print(gcd(15, 20))
print(find_lcm(15, 20))
print(lcm_array([2, 7, 3, 9, 4]))

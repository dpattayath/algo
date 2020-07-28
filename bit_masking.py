

def check_ith_bit(num, i):
    mask = 0b1 << i
    return (num & mask) != 0

print(check_ith_bit(0b00101100, 5))
print(check_ith_bit(0b01001100, 5))


def set_ith_bit(num, i):
    mask = 0b1 << i
    return bin(num | mask)

print(set_ith_bit(0b01001100, 5))


def clear_ith_bit(num, i):
    mask = ~(0b1 << i)
    return bin(num & mask)

print(clear_ith_bit(0b0101100, 3))

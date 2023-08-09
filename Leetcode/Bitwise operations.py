'''
bitwise operations
& :and
~ :not
|: or
^ XOR
'''

a=2
x=[3,5,6,8,14]
for b in x:
    print(f"{a},{b} and:",(a&b))
    print(f"{a},{b} or:",(a|b))
    print(f"{a},{b} not:",(~b))
    print(f"{a},{b} XOR:",(a^b))
    print("next number_____","\n")


def getSum( a, b) :
    while (b != 0):
        carry = (a & b)
        a = a ^ b
        b = carry << 1
    return a

print(getSum(5,6))
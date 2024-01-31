def plusOne(digits) :
    leng=len(digits)
    for x in range(leng-1,-1,-1):
        if digits[x]==9:
            digits[x]=0
        else:
            digits[x]=digits[x]+1
            return digits

    return [1]+digits


digits=[5]
print(plusOne(digits))

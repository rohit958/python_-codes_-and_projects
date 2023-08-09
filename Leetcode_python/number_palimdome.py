n=[121,43434,56]


def isPalindrome(x) :
    rev = 0
    temp=int(x)
    while (temp>0):
        rev = rev*10 +(temp % 10)
        temp//=10
    if rev ==x:
        return True
    else:
        return False


for num in n:
    print(isPalindrome(num))
'''A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.'''



def isPalindrome(s):
    txt=''
    for char in s:
        if char.isalnum():
            txt=txt +char.lower()
        else:
            continue
    if txt == txt[::-1]:
        return True
    else:
        return False




print(isPalindrome("A man, a plan, a canal: Panama"))
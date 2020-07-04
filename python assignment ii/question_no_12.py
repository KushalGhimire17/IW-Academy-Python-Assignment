"""check palindrome
"""
def is_palindrome(string):
    if string.casefold() == string[-1::-1].casefold():
        return True
    else:
        return False

print(is_palindrome("mAdaM"))
print(is_palindrome("KUSHAL"))
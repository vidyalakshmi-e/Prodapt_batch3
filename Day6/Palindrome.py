def is_palindrome(s):
    text=s.lower()
    return text==text[::-1]
word=input("Enter a string: ")
if is_palindrome(word):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")
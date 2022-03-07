def palindrome(a):
    if a.lower() == a.lower()[::-1]:
        return "The string is a Palindrome"
    else:
        return "The string is not a Palindrome"

x = str(input("Enter any words: "))

palindrome_string = palindrome(x)
print(palindrome_string)
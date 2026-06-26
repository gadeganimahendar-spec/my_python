# Check Palindrome Number        121 → Palindrome
n=input("enter a number:")
if(n==n[::-1]):
    print("palindrome")
else:
    print("not a palindrome")
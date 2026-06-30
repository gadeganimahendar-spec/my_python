# separate vowels and consonants in string "hi hello raju"


s = str(input("Enter the characters: "))

l = [ [ch for ch in s if ch.lower() in "aeiou"],[ch for ch in s if ch.isalpha() and ch.lower() not in "aeiou"]]

print("Vowels:", l[0])
print("Consonants:", l[1])


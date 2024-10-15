s=input("enter a word")
if any(i in 'aeiouAEIOU' for i in s):
    print("Yes,", s, "contains a vowel")
else:
    print("No,", s, "contains no vowels")
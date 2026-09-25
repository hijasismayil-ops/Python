# input a string print vowels and their index?

# 1.
string = input("Enter a string: ")
for i in range(len(string)):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
        print(f"Vowel: {string[i]} at index: {i}")

# 2.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for index in range(len(string)):
    if string[index] in vowels:
        print(f"Vowel: {string[index]} at index: {index}")
str = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for letter in str:
    if letter in vowels:
        vowel_count += 1

print("Number of vowels: ", vowel_count)

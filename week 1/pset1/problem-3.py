str = input("Enter a string: ")
substrings = []
current_substring = []

for i in range(len(str) - 2):
    if str[i] <= str[i + 1]:
        current_substring.append(str[i])
        if str[i + 1] > str[i + 2]:
            current_substring.append(str[i + 1])
            substrings.append(''.join(current_substring))
            current_substring = []

min_substring = substrings[0]
for i in substrings:
    if (len(i) > len(min_substring)):
        min_substring = i

print(min_substring)

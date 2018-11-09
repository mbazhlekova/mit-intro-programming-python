str = input("Enter a string: ")
bob_count = 0

for i in range(len(str) - 2):
    if str[i:(i+3)] == 'bob':
        bob_count += 1

print("Number of times bob occurs is: ", bob_count)

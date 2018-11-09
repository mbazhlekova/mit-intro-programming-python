cube = 27
for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of ", cube, " is ", guess)

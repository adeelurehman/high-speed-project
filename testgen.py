import random

# Generate 10000 pairs of 16-bit signed integers
pairs = []
for i in range(10000):
    x = random.randint(-32768, 32767)
    y = random.randint(-32768, 32767)
    pairs.append((x, y))

# Write the pairs to a dat file as strings
with open('pairs.dat', 'w') as f:
    for pair in pairs:
        # Convert the pair to a string
        data = f"{pair[0]} {pair[1]}\n"
        # Write the string to the file
        f.write(data)

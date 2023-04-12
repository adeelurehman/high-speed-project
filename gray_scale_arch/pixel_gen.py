import random

# Generate 10000 pairs of 16-bit signed integers
pairs = []
for i in range(100000):
    x = random.randint(-32768, 32767)
    pairs.append(x & 0x00FFFFFF)

# Write the pairs to a dat file as strings
with open('pixels.dat', 'w') as f:
    for pair in pairs:
        # Convert the pair to a string
        data = f"{pair}\n"
        # Write the string to the file
        f.write(data)

import random
import struct

# Generate 10000 pairs of 16-bit signed integers
pairs = []
for i in range(10000):
    x = random.randint(-32768, 32767)
    y = random.randint(-32768, 32767)
    pairs.append((x, y))

# Write the packed pairs to a dat file
with open('pairs.dat', 'wb') as f:
    for pair in pairs:
        f.write(f"{pair[0]} {pair[1]}")

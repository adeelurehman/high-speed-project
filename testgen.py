import random
import struct

# Generate 10000 pairs of 16-bit signed integers
pairs = []
for i in range(10000):
    x = random.randint(-32768, 32767)
    y = random.randint(-32768, 32767)
    pairs.append((x, y))

# Pack the pairs into bytes objects
packed_pairs = []
for x, y in pairs:
    packed_x = struct.pack('h', x)
    packed_y = struct.pack('h', y)
    packed_pairs.append(packed_x + packed_y)

# Write the packed pairs to a dat file
with open('pairs.dat', 'wb') as f:
    for packed_pair in packed_pairs:
        f.write(packed_pair)

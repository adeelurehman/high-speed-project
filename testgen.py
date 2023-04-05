import struct

# Generate pairs of 16 bit signed integers
pairs = []
for i in range(10000):
    x = struct.pack('h', i)
    y = struct.pack('h', -i)
    pairs.append((x, y))

# Write the pairs to a dat file
with open('pairs.dat', 'wb') as f:
    for x, y in pairs:
        f.write(x)
        f.write(y)

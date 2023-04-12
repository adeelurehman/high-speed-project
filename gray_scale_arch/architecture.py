def splitter(input):
    R = (input & 0x00FF0000) >> 16
    G = (input & 0x0000FF00) >> 8
    B = (input & 0x000000FF)
    return R, G, B

def right_shift(input, shift):
    return input >> shift

def accurate_RCA_8_bit(A, B):
    return (A + B) & 0xFF

def grayscale_truth(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)
    return int(0.2989 * R + 0.5870 * G + 0.1140 * B)

def architecture_paper(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)
    R1 = right_shift(R, 2)
    R2 = right_shift(R, 5)

    G1 = right_shift(G, 1)
    G2 = right_shift(G, 4)

    B1 = right_shift(B, 4)
    B2 = right_shift(B, 5)

    Y = accurate_RCA_8_bit(R1, R2)
    Y = accurate_RCA_8_bit(Y, G1)
    Y = accurate_RCA_8_bit(Y, G2)
    Y = accurate_RCA_8_bit(Y, B1)
    Y = accurate_RCA_8_bit(Y, B2)
    return Y

# Reduce RCA adds by reducing bits going into 8 bit cumulative adder
def architecture_1(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)

    R1 = right_shift(R, 2)
    G1 = right_shift(G, 1)
    B1 = right_shift(B, 4)
    B2 = right_shift(B, 5)

    Y1 = accurate_RCA_8_bit(B1, B2)
    Y2 = accurate_RCA_8_bit(R1, G1)
    Y = accurate_RCA_8_bit(Y1, Y2)
    return Y

# Similar to architcure 1, but bit flip 4 & 5 to randomly add 16 back to grayscale to round up
def architecture_2(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)

    R1 = right_shift(R, 2)
    G1 = right_shift(G, 1)
    B1 = right_shift(B, 4)
    B2 = right_shift(B, 5)

    Y1 = accurate_RCA_8_bit(B1, B2)
    Y2 = accurate_RCA_8_bit(R1, G1)
    Y = accurate_RCA_8_bit(Y1, Y2)

    Y = Y | 0x18 # flip bit 4 & 5 to add 8 + 16 in most cases
    return Y
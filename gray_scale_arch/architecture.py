def splitter(input):
    R = (input & 0x00FF0000) >> 16
    G = (input & 0x0000FF00) >> 8
    B = (input & 0x000000FF)
    return R, G, B

def right_shift(input, shift):
    return input >> shift

def accurate_RCA_8_bit(A, B):
    return (A + B) & 0xFF

def approximate_RCA_3_bit_LOA(A, B):
    #approximate adder for 3 bits
    lower_three = (A | B) & 0x07 # 3 bit or for lower bits

    #accurate adder
    Cin = (((A & 0x04) & (B & 0x04))) >> 2 # Cin is the and of bit 2
    A = A >> 3
    B = B >> 3

    add = ((A + B + Cin) << 3) | lower_three
    return add

def approximate_RCA_2_bit_LOA(A, B):
    #approximate adder for 3 bits
    lower_two = (A | B) & 0x03 # 3 bit or for lower bits

    #accurate adder
    Cin = (((A & 0x02) & (B & 0x02))) >> 1 # Cin is the and of bit 2
    A = A >> 2
    B = B >> 2

    add = ((A + B + Cin) << 2) | lower_two
    return add

def architecture_truth(RGB_pixel_32):
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
    

# Approximate RCA with LOA of 3 bits combined with architecture 1
def architecture_2(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)

    R1 = right_shift(R, 2)
    G1 = right_shift(G, 1)
    B1 = right_shift(B, 4)
    B2 = right_shift(B, 5)

    Y1 = approximate_RCA_3_bit_LOA(B1, B2)
    Y2 = approximate_RCA_3_bit_LOA(R1, G1)
    Y = approximate_RCA_3_bit_LOA(Y1, Y2)

    return Y

# Architecture with approximate LOA of 2 bits
def architecture_3(RGB_pixel_32):
    R, G, B = splitter(RGB_pixel_32)

    R1 = right_shift(R, 2)
    G1 = right_shift(G, 1)
    B1 = right_shift(B, 4)
    B2 = right_shift(B, 5)

    Y1 = approximate_RCA_2_bit_LOA(B1, B2)
    Y2 = approximate_RCA_2_bit_LOA(R1, G1)
    Y = approximate_RCA_2_bit_LOA(Y1, Y2)

    return Y

# # Reduce RCA adds by reducing bits going into 8 bit cumulative adder
# def architecture_4(RGB_pixel_32):
#     R, G, B = splitter(RGB_pixel_32)

#     R1 = right_shift(R, 2)
#     R2 = right_shift(R, 5)
#     B1 = right_shift(B, 4)
#     G1 = right_shift(G, 1)

#     Y1 = accurate_RCA_8_bit(R1, R2)
#     Y2 = accurate_RCA_8_bit(B1, G1)
#     Y = accurate_RCA_8_bit(Y1, Y2)
#     return Y

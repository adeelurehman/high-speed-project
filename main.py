# Bitwise
def genSum(A, B, Cin):
    return (A&B&Cin) | (A&Cin | B) & ~Cin
    # return (A+B+Cin)&1

# Bitwise
def genCarry(A, B, Cin):
    return A & Cin | B
    # return int(((A+B+Cin) >> 1) > 0)

# Integer
def add(A, B, Cin):
    C_in_curr = Cin
    Cout = 0

    for i in range(16):
        A_bit = ((2**i) & A) >> i
        B_bit = ((2**i) & B) >> i

        Cout |= genSum(A_bit, B_bit, C_in_curr) << i
        C_in_curr = genCarry(A_bit, B_bit, C_in_curr)
    
    return Cout

print(add(2, 2, 0))

def truth_adder(A, B, C):
    sum = (A+B+C)&1
    cout= int(((A+B+C) >> 1) > 0)
    return sum, cout

def approx_1(A, B, C):
    sum = (A+B+C)&1
    cout= int(((A+B+C) >> 1) > 0)
    return sum, cout

def approx_2(A, B, C):
    sum = (A + B) & 0x01
    cout = C & 0x01
    return sum, cout

def approx_3(A, B, C):
    cout = ((A * C) + B) & 0x01
    sum = (1 - cout) & 0x01
    return sum, cout

def approx_5(A, B, C):
    cout = A & 0x01
    sum = B & 0x01
    return sum, cout

def approx_6(A, B, C):
    cout = ((1 - A) + (B * C)) & 0x01
    sum = A & 0x01
    return sum, cout

def approx_8(A, B, C):
    cout = (((1-A) + B) * C) & 0x01
    sum  = ((A * B) + (B*C) + (A*C)) & 0x01
    return sum, cout


def test_two_pairs():
    failed = False
    for s0 in range (0, 2):
        for s1 in range (0, 2):
            for cin in range(0, 2):
                apr1_sum, apr1_cout = approx_5(s0, s1, cin)
                apr2_sum, apr2_cout = approx_6(s0, s1, cin)
                t_sum, t_cout = truth_adder(s0, s1, cin)

                if not ((apr1_sum == t_sum and apr1_cout == t_cout) or (apr2_sum == t_sum and apr2_cout == t_cout)):
                    failed = True
                    print(f"DOES NOT WORK for A: {s0}, B: {s1}, C: {cin}")
                    print(f"Apr 1 sum: {apr1_sum} COUt: {apr1_cout}")
                    print(f"App 2 sum: {apr2_sum} COUt: {apr2_cout}")
                    print(f"Truth sum: {t_sum} COUt: {t_cout}")


                if (apr1_sum == t_sum and apr1_cout == t_cout) and (apr2_sum == t_sum and apr2_cout == t_cout):
                    print(f"{s0} {s1} {cin} | x")
                elif (apr1_sum == t_sum and apr1_cout == t_cout):
                    print(f"{s0} {s1} {cin} | 1")
                else:
                    print(f"{s0} {s1} {cin} | 0")
    if not failed:
        print("Is good")

if __name__ == "__main__":
    test_two_pairs()


# What works:
# approx 3 and 5

'''
Does not work

'''
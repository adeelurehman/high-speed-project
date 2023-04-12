from architecture import *

if __name__ == "__main__":
    # Using readlines()
    file1 = open('gray_scale_arch/pixels.dat', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    count = 0
    paper_error = 0
    arch1_error = 0
    arch2_error = 0

    for line in Lines:
        count = count + 1
        value = int(line)
        truth = grayscale_truth(value)

        V1 = architecture_paper(value)
        paper_error += abs(truth - V1)

        V2 = architecture_1(value)
        arch1_error += abs(truth - V2)
        
        V3 = architecture_2(value)
        arch2_error += abs(truth - V3)


    paper_average_error = paper_error / count
    arch1_average_error = arch1_error / count
    arch2_average_error = arch2_error /count

    print(f"Paper average error (value): {paper_average_error}")
    print(f"Arch1 average error (value): {arch1_average_error}")
    print(f"Arch2 average error (value): {arch2_average_error}")
    

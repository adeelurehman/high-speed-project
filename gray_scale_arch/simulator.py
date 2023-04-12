from architecture import *

if __name__ == "__main__":
    # Using readlines()
    file1 = open('pixels.dat', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    count = 0

    paper_error = 0
    paper_percent_error = 0

    arch1_error = 0
    arch1_percent_error = 0

    arch2_error = 0
    arch2_percent_error = 0

    arch3_error = 0
    arch3_percent_error = 0

    arch4_error = 0
    arch4_percent_error = 0



    for line in Lines:
        count = count + 1
        value = int(line)
        truth = architecture_truth(value)

        if truth == 0:
            truth = 1
    
        V1 = architecture_paper(value)
        paper_error += abs(truth - V1)
        error = abs(truth - V1)
        paper_percent_error += (error / truth)
        

        V2 = architecture_1(value)
        arch1_error += abs(truth - V2)
        error = abs(truth - V2)
        arch1_percent_error += (error / truth)
        
        V3 = architecture_2(value)
        arch2_error += abs(truth - V3)
        error = abs(truth - V3)
        arch2_percent_error += (error / truth)

        V4 = architecture_3(value)
        arch3_error += abs(truth - V4)
        error = abs(truth - V4)
        arch3_percent_error += (error / truth)

        V5 = architecture_4(value)
        arch4_error += abs(truth - V5)
        error = abs(truth - V5)
        arch4_percent_error += (error / truth)


    paper_average_error = paper_error / count
    arch1_average_error = arch1_error / count
    arch2_average_error = arch2_error /count
    arch3_average_error = arch3_error /count
    arch4_average_error = arch4_error /count

    paper_percent_error = paper_percent_error * 100/ count
    arch1_percent_error = arch1_percent_error * 100/ count
    arch2_percent_error = arch2_percent_error * 100/ count
    arch3_percent_error = arch3_percent_error * 100/ count
    arch4_percent_error = arch4_percent_error * 100/ count

    print(f"Paper average error (value): {paper_average_error}")
    print(f"Paper average error (percent): {paper_percent_error}")

    print(f"Arch1 average error (value): {arch1_average_error}")
    print(f"Arch1 average error (percent): {arch1_percent_error}")

    print(f"Arch2 average error (value): {arch2_average_error}")
    print(f"Arch2 average error (percent): {arch2_percent_error}")

    print(f"Arch3 average error (value): {arch3_average_error}")
    print(f"Arch3 average error (percent): {arch3_percent_error}")

    #print(f"Arch4 average error (value): {arch4_average_error}")
    #print(f"Arch4 average error (percent): {arch4_percent_error}")
    

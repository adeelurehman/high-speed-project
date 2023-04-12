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


    paper_average_error = paper_error / count
    arch1_average_error = arch1_error / count
    arch2_average_error = arch2_error /count

    paper_percent_error = paper_percent_error / count
    arch1_percent_error = arch1_percent_error / count
    arch2_percent_error = arch2_percent_error / count

    print(f"Paper average error (value): {paper_average_error}")
    print(f"Paper average error (percent): {paper_percent_error}")

    print(f"Arch1 average error (value): {arch1_average_error}")
    print(f"Arch1 average error (percent): {arch1_percent_error}")

    print(f"Arch2 average error (value): {arch2_average_error}")
    print(f"Arch2 average error (percent): {arch2_percent_error}")
    

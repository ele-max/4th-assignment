import math

file = open("rosalind_pmch.txt", "r")
lines = file.readlines()
file.close()

seq = ''
for line in lines:
    if line[0] != '>':
        seq += line.replace('\n', '')

def PMCH():
    A_U = 0
    C_G = 0
    for nucl in seq:
        if nucl == 'A' or nucl == 'U':
            A_U += 1
        elif nucl == 'C' or nucl == 'G':
            C_G += 1
    AU_perf_match = math.factorial(A_U // 2)  # Use integer division here
    CG_perf_match = math.factorial(C_G // 2)  # Use integer division here
    print(AU_perf_match * CG_perf_match)
    return

PMCH()

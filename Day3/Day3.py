# Bennett Marra 2022

# Read input from file
file = open('./input.txt', 'r')
lines = file.readlines()
file.close

# Gamma rate
binarygammarate = ""
for place in range(len(lines[0])):
    zeroVal = 0
    oneVal = 0

    # scan to find the occurrence rates
    for line in lines:
        if line[place] == '0':
            zeroVal += 1
        elif line[place] == '1':
            oneVal += 1

    # assign the bit (assumes no equal edge case)
    if zeroVal > oneVal:
        binarygammarate += '0'
    elif oneVal > zeroVal:
        binarygammarate += '1'

print(int(binarygammarate,2))
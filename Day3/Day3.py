# Bennett Marra 2022

# Read input from file
file = open('./input.txt', 'r')
lines = file.readlines()
file.close

# Rate calculation
binarygammarate = ""
binaryepsilonrate = ""

# scan though each placevalue on each line (going "forward")
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
        binaryepsilonrate += '1'
    elif oneVal > zeroVal:
        binarygammarate += '1'
        binaryepsilonrate += '0'

print(int(binarygammarate,2))
print(int(binaryepsilonrate,2))
print(int(binarygammarate,2)*int(binaryepsilonrate,2))
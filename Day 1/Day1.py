# Bennett Marra 2022

# Read input from file
import sys

file = open('./Day 1/input.txt', 'r')
newLines = file.read()
stringContents = newLines.splitlines()
#print(stringContents)

# convert strings into ints
intContents = []
for line in stringContents:
    intLine = int(line)
    intContents.append(intLine)

#print(intContents)

# Setup complete, now for the problem
timesIncreased = 0
oldVal = sys.maxsize # makes initial oldVal biggest int possible

for newVal in intContents:
    if oldVal < newVal:
        timesIncreased += 1
    oldVal = newVal

print(timesIncreased)
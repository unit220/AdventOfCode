# Bennett Marra 2022

# Read input from file
file = open('./input.txt', 'r')
lines = file.readlines()
# Get rid of new line
cleanLines = []
for element in lines:
    cleanLines.append(element.strip())

# Set up variables
horizontal = 0
depth = 0

for line in cleanLines:
    # print(line)
    splitLine = line.split()
    # print(splitLine)
    splitWord = splitLine[0]
    # print(splitWord)
    splitInt = int(splitLine[1])
    # print(splitInt)

    if splitWord == "forward":
        horizontal += splitInt
    elif splitWord == "down":
        depth += splitInt
    elif splitWord == "up":
        depth -= splitInt

    # def route(splitWord):
    #     match splitWord:
    #         case ("forward"):
    #             horizontal += splitInt
    #         case ("down"):
    #             vert += splitInt
    #             return vert
    #         case ("up"):
    #             vert -= splitInt
    #             return vert

print(horizontal)
print(depth)
print(horizontal*depth)
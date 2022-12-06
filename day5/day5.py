import time

class Instructions:
    def __init__(self, nr, fromStack, toStack):
        self.nr = nr
        self.fromStack = fromStack
        self.toStack = toStack

def readInput(instructionsList, stacks):
    f = open('C:\\git\\adventofcode2022\\day5\\input5.txt', 'r')
    lines = f.readlines()
    f.close()
    
    #1,5,9,13,17,21,25,29,33 are the starting col positions of the stacks, dont forget to reverse the stacks
    lineCount = 0
    for line in lines:
        if line == '\n':
            continue
        
        if lineCount < 8:
            if line[1] != '' and line[1] != ' ':
                stacks[0].append(line[1])
            if line[5] != '' and line[5] != ' ':
                stacks[1].append(line[5])
            if line[9] != '' and line[9] != ' ':
                stacks[2].append(line[9])
            if line[13] != '' and line[13] != ' ':
                stacks[3].append(line[13])
            if line[17] != '' and line[17] != ' ':
                stacks[4].append(line[17])
            if line[21] != '' and line[21] != ' ':
                stacks[5].append(line[21])
            if line[25] != '' and line[25] != ' ':
                stacks[6].append(line[25])
            if line[29] != '' and line[29] != ' ':
                stacks[7].append(line[29])
            if line[33] != '' and line[33] != ' ':
                stacks[8].append(line[33])
        else:
            if line != '\n' and lineCount > 8:
                line = line.replace('move ','')
                line = line.replace('from ','')
                line = line.replace('to ','')
                line = line.replace('\n','')
            
                line = line.split(' ')
                instructionsList.append(Instructions(line[0], line[1], line[2]))
        
        lineCount += 1
        
    for stack in stacks:
        stack.reverse()
        
    return stacks, instructionsList

def part1():
    instructionsList = []
    stacks = []
    
    for i in range(0,9):
        stacks.append([])
    
    stacks, instructionsList = readInput(instructionsList, stacks)
    
    for instruction in instructionsList:
        for i in range(0, int(instruction.nr)):
            stacks[int(instruction.toStack) - 1].append(stacks[int(instruction.fromStack) - 1].pop())
    
    result = ''
    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    
    print(result)

def part2():
    instructionsList = []
    stacks = []
    
    for i in range(0,9):
        stacks.append([])
    
    stacks, instructionsList = readInput(instructionsList, stacks)
    
    for instruction in instructionsList:
        myStack = []
        
        for i in range(0, int(instruction.nr)):
            if len(stacks[int(instruction.fromStack) - 1]) > 0:
                myStack.append(stacks[int(instruction.fromStack) - 1].pop())
        
        myStack.reverse()
        for item in myStack:
            stacks[int(instruction.toStack) - 1].append(item)
    
    result = ''
    for stack in stacks:
        if len(stack) > 0:
            result += stack.pop()
    
    print(result)

if __name__ == '__main__':
    st = time.time()
    
    part1()
    part2()
    
    et = time.time()
    if (et - st) < 1:
        rt = str(round((et - st) * 1000,3)) + "ms"
    else:
        rt = str(round(et - st,3)) + "s"

    print("runtime: ", rt)

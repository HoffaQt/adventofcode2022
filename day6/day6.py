import time

def testStr(subStr, length):
    strList = list(subStr)
    for i in range(0,length):
        temp = strList[i]
        strList[i] = ''
        if temp in strList:
            return False
        
    return True

def part1():
    data = ''
    index = 0
    
    with open('C:\\git\\adventofcode2022\\day6\\input6.txt', 'r') as file:
        data = file.read().rstrip()
    
    while index < len(data):
        subStr = data[index:index+4]
        if testStr(subStr,4):
            print(f'{subStr} is a valid marker on index: {index+4}')
            break
        else:
            index += 1

def part2():
    data = ''
    index = 0
    
    with open('C:\\git\\adventofcode2022\\day6\\input6.txt', 'r') as file:
        data = file.read().rstrip()
    
    while index < len(data):
        subStr = data[index:index+14]
        if testStr(subStr,14):
            print(f'{subStr} is a valid marker on index: {index+14}')
            break
        else:
            index += 1

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

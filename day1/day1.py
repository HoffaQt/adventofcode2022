class Elf:
    def __init__(self, foodList : list[int], tot : int) -> None:
        self.foodList = foodList
        self.tot = tot
    
    def calcTot(self):
        sum = 0
        for food in self.foodList:
            s = food.replace('\n', '')
            sum += int(s)
        
        return sum

class ElfList:
    def __init__(self, elfList : list[Elf]) -> None:
        self.elfList = elfList

    def calcElfTot(self):
        for e in self.elfList:
            e.tot = e.calcTot()

def part(array, start, end, comp_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and comp_func(array[high], pivot):
            high = high - 1

        while low <= high and not comp_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, compare_func):
    if start >= end:
        return

    p = part(array, start, end, compare_func)
    quick_sort(array, start, p-1, compare_func)
    quick_sort(array, p+1, end, compare_func)

if __name__ == '__main__':
    f = open('input1.txt', 'r')
    lines = f.readlines()

    myList = ElfList([])
    e = Elf([], 0)
    
    for line in lines:
        if line == '\n':
            myList.elfList.append(e)
            e = Elf([], 0)
            
        else:
            e.foodList.append(line)

    myList.calcElfTot()
    quick_sort(myList.elfList, 0, len(myList.elfList) -1, lambda x, y: x.tot < y.tot)
    
    print(myList.elfList[0].tot + myList.elfList[1].tot + myList.elfList[2].tot)
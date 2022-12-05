roundValue = {
    'A': 1, #Rock
    'B': 2, #Paper
    'C': 3, #Scissors
    'X': 1, #Rock
    'Y': 2, #Paper
    'Z': 3 #Scissors
}

def part1():
    f = open('C:\\git\\adventofcode2022\\day2\\input2.txt', 'r')
    lines = f.readlines()
    f.close()
    
    score = 0
    for line in lines:
        opponent = line[0]
        myMove = line[2]
        
        #draw
        if roundValue[myMove] == roundValue[opponent]:
            score += 3
            score += roundValue[myMove]
        #loss
        elif roundValue[myMove] == 1 and roundValue[opponent] == 2:
            score += roundValue[myMove]
        elif roundValue[myMove] == 2 and roundValue[opponent] == 3:
            score += roundValue[myMove]
        elif roundValue[myMove] == 3 and roundValue[opponent] == 1:
            score += roundValue[myMove]
        #win
        elif roundValue[myMove] == 1 and roundValue[opponent] == 3:
            score += 6
            score += roundValue[myMove]
        elif roundValue[myMove] == 2 and roundValue[opponent] == 1:
            score += 6
            score += roundValue[myMove]
        elif roundValue[myMove] == 3 and roundValue[opponent] == 2:
            score += 6
            score += roundValue[myMove]
    
    print(score)

def part2():
    f = open('C:\\git\\adventofcode2022\\day2\\input2.txt', 'r')
    lines = f.readlines()
    f.close()
    
    score = 0
    for line in lines:
        opponent = line[0]
        myMove = line[2]
        case = ''
        
        if line[2] == 'X':
            case = 'lose'
        elif line[2] == 'Y':
            case = 'draw'
        elif line[2] == 'Z':
            case = 'win'
            
        #draw
        if case == 'draw':
            score += 3
            score += roundValue[opponent]
        #loss
        elif case == 'lose':
            if roundValue[opponent] == 3:
                score += 2
            elif roundValue[opponent] == 2:
                score += 1
            elif roundValue[opponent] == 1:
                score += 3
        #win
        elif case == 'win':
            if roundValue[opponent] == 3:
                score += 6
                score += 1
            elif roundValue[opponent] == 2:
                score += 6
                score += 3
            elif roundValue[opponent] == 1:
                score += 6
                score += 2
    
    print(score)
    
if __name__ == '__main__':
    part1()
    part2()
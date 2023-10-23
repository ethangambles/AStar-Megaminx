import random
import math
import heapq
import copy
import time

NUM_FACES=12
NUM_PIECES_PER_FACE= 11

TOTAL_PIECES = 132

COLORS = ['W', 'F', 'V', 'U', 'B', 'R', 'P', 'G', 'O', 'T', 'Y', 'S']
#W= white, F= forest, V=violet, U=gold, B=blue, R=red, P=pink, G=green, O=orange, T=teal, Y=yellow, S=silver

MOVES = ['Clockwise', 'Counterclockwise']


neighbors = {
    #white on top
    'W': ['U','B','R','F','V'],
    #top layer
    'F': ['Y','T','V','W','R'],
    'R': ['P','Y','F','W','B'],
    'B': ['G','P','R','W','U'],
    'U': ['O','G','B','W','V'],
    'V': ['T','O','U','W','F'],
    #second layer
    'T': ['V','F','Y','S','O'],
    'Y': ['F','R','P','S','T'],
    'P': ['R','B','G','S','Y'],
    'G': ['B','U','O','S','P'],
    'O': ['U','V','T','S','G'],
    #silver on bottom
    'S': ['Y','P','G','O','T']

}

def printBottomRowFace(megaminx,face):
    print("    " + megaminx[face][1])
    print(" " + megaminx[face][10] + "/   \\" + megaminx[face][2])
    print(megaminx[face][9] + "/  " + megaminx[face][0] + "  \\" + megaminx[face][3])
    print(" " + megaminx[face][8] + "\\   /" +megaminx[face][4])
    print("  " + megaminx[face][7] + "|" +megaminx[face][6] + "|" + megaminx[face][5] + '\n')

def printTopRowFace(megaminx,face):
    print("  " + megaminx[face][5] + "|" +megaminx[face][6] + "|" + megaminx[face][7])
    print(" " + megaminx[face][4] + "/   \\" +megaminx[face][8])
    print(megaminx[face][3] + "\\  " + megaminx[face][0] + "  /" + megaminx[face][9])
    print(" " + megaminx[face][2] + "\\   /" + megaminx[face][10])
    print("    " + megaminx[face][1] + '\n')

def printMegaMinx(megaminx):
    for i in range(0,NUM_FACES):
        if i >=1 and i <=5:
            printTopRowFace(megaminx,i)
        else:
            printBottomRowFace(megaminx,i)

def swapNeighbor(megaminx, faceColor, neighbor1, cubee1, cubee2, cubee3, neighbor2, cubee4,cubee5,cubee6):
    #neighbor2 overrides neighbor1 and cubee4, cubee5, cubee6 override cubee1, cubee2, cubee 3 respectively
    megaminx[COLORS.index(neighbors[faceColor][neighbor1])][cubee1], megaminx[COLORS.index(neighbors[faceColor][neighbor1])][cubee2], megaminx[COLORS.index(neighbors[faceColor][neighbor1])][cubee3] = megaminx[COLORS.index(neighbors[faceColor][neighbor2])][cubee4], megaminx[COLORS.index(neighbors[faceColor][neighbor2])][cubee5],megaminx[COLORS.index(neighbors[faceColor][neighbor2])][cubee6]

def swapSelf(megaminx, face):
    temp = [megaminx[face][1], megaminx[face][2], megaminx[face][10], megaminx[face][9]]
    megaminx[face][1], megaminx[face][10], megaminx[face][9] = temp[3], megaminx[face][8], megaminx[face][7]
    megaminx[face][8], megaminx[face][7] = megaminx[face][6], megaminx[face][5]
    megaminx[face][6], megaminx[face][5], megaminx[face][4] = megaminx[face][4], megaminx[face][3], temp[1]
    megaminx[face][3], megaminx[face][2] = temp[0], temp[2]

def moveFaceClockwise(megaminx, face): 
    faceColor = COLORS[face]  #number index of the random color

    #is faceColor in top row or bottom row?
    if COLORS.index(faceColor) >=1 and COLORS.index(faceColor) <=5:
        topRow = True
    else:
        topRow = False
    #print(faceColor)
    if faceColor != 'W' and faceColor != 'S':
        temp = [megaminx[COLORS.index(neighbors[faceColor][0])][1], megaminx[COLORS.index(neighbors[faceColor][0])][10], megaminx[COLORS.index(neighbors[faceColor][0])][9]]

        #move 1
        swapNeighbor(megaminx, faceColor, 0,1,10,9,4,5,4,3)

        #Moving top/bottom
        if topRow:
            index = neighbors['W'].index(faceColor)
        else:
            index = neighbors['S'].index(faceColor)

        #Moves 2 and 3 depending on where face is in relation to top/bottom
        if index == 0:
            swapNeighbor(megaminx, faceColor, 4, 5, 4, 3, 3, 1, 10, 9)
            swapNeighbor(megaminx,faceColor, 3, 1, 10, 9, 2, 9, 8, 7)
        elif index == 1:
            swapNeighbor(megaminx,faceColor, 4, 5, 4, 3, 3, 3, 2, 1)
            swapNeighbor(megaminx,faceColor, 3, 3, 2, 1, 2, 9, 8, 7)
        elif index == 2:
            swapNeighbor(megaminx,faceColor, 4, 5, 4, 3, 3, 5, 4, 3)
            swapNeighbor(megaminx,faceColor, 3, 5, 4, 3, 2, 9, 8, 7)
        elif index == 3:
            swapNeighbor(megaminx,faceColor, 4, 5, 4, 3, 3, 7, 6, 5)
            swapNeighbor(megaminx,faceColor, 3, 7, 6, 5, 2, 9, 8, 7)
        elif index == 4:
            swapNeighbor(megaminx,faceColor, 4, 5, 4, 3, 3, 9, 8, 7)
            swapNeighbor(megaminx,faceColor, 3, 9, 8, 7, 2, 9, 8, 7)
        
        #move 4
        swapNeighbor(megaminx,faceColor,2,9,8,7,1,3,2,1)
        
        #use temp for move 5
        megaminx[COLORS.index(neighbors[faceColor][1])][3], megaminx[COLORS.index(neighbors[faceColor][1])][2], megaminx[COLORS.index(neighbors[faceColor][1])][1] = temp[0], temp[1], temp[2]
    
    #different changes if top or bottom (W or S) is selected
    if faceColor == 'W' or faceColor == 'S':
        temp = [megaminx[COLORS.index(neighbors[faceColor][0])][5], megaminx[COLORS.index(neighbors[faceColor][0])][6], megaminx[COLORS.index(neighbors[faceColor][0])][7]]

        #move 1-4
        swapNeighbor(megaminx, faceColor, 0, 5, 6, 7, 4, 5, 6, 7)
        swapNeighbor(megaminx, faceColor, 4, 5, 6, 7, 3, 5, 6, 7)
        swapNeighbor(megaminx, faceColor, 3, 5, 6, 7, 2, 5, 6, 7)
        swapNeighbor(megaminx, faceColor, 2, 5, 6, 7, 1, 5, 6, 7)

        #use temp for move 5
        megaminx[COLORS.index(neighbors[faceColor][1])][5], megaminx[COLORS.index(neighbors[faceColor][1])][6], megaminx[COLORS.index(neighbors[faceColor][1])][7] = temp[0], temp[1], temp[2]
    
    #update face itself
    swapSelf(megaminx, face)

def moveFaceCounterClockwise(megaminx, face):
    for i in range(0,4):
        moveFaceClockwise(megaminx,face)

def scramble(megaminx,moves):
    for i in range(0,moves):
        #direction = random.choice(MOVES)

        #only use Clockwise moves to scramble
        randFace = random.randrange(NUM_FACES)
        faceColor = COLORS[randFace]
        moveFaceClockwise(megaminx, randFace)


        #if direction == 'Clockwise':
            #moveFaceClockwise(megaminx, randFace)
        #elif direction == 'Counterclockwise':
            #moveFaceCounterClockwise(megaminx, randFace)

        print('Moving ' + faceColor + ' face Clockwise\n')
    
def isSolved(megaminx):
    correctPieces = 0
    for i in range(NUM_FACES):
        for j in range(NUM_PIECES_PER_FACE):
            if megaminx[i][j] == megaminx[i][0]:
                correctPieces = correctPieces + 1
    if correctPieces == TOTAL_PIECES:
        return True
    else:
        return False

#heuristic- ceiling(every piece not on the correct face divided by 15)
def heuristic(megaminx):
    outOfPlace = 0
    for i in range(NUM_FACES):
        for j in range(NUM_PIECES_PER_FACE):
            if megaminx[i][j] != megaminx[i][0]: #if piece not on correct face
                outOfPlace = outOfPlace + 1

    outOfPlace = outOfPlace / 15
    outOfPlace = math.ceil(outOfPlace)
    return outOfPlace


def astar(megaminx):
    unexplored = [(heuristic(megaminx), megaminx, 0)] #start state
    explored = set()
    nodesExpanded = 0
    while unexplored:
        _, currentState, depth = heapq.heappop(unexplored) #pop the element with the smallest f off the queue- heappop() automatically does this
        
        nodesExpanded +=1

        #if currentState is solved, return
        if isSolved(currentState):
            return currentState, depth, nodesExpanded
        
        #add new state to explored list
        explored.add(tuple(map(tuple, currentState)))

        g = depth + 1 #increment g to be one more than the current depth

        #try all possible moves in current state
        for i in range(NUM_FACES):
            newPuzzle = copy.deepcopy(currentState)

            #only move counterclockwise on solving
            moveFaceCounterClockwise(newPuzzle, i)

            #if this state has not been explored
            if (tuple(map(tuple, newPuzzle))) not in explored:
                f = heuristic(currentState) + g  # f = h + g - from astar algorithm
                heapq.heappush(unexplored, (f, newPuzzle, g)) #push new state
    return None


        
if __name__ == '__main__':
    random.seed()

    #this code runs 5 k randomized puzzles for each k from 3 to 10
    for k in range(3,10): #I found my implementation runs out of memory at k=10
        for i in range(0,5):
            start = time.time()
            megaminx = [[0 for i in range(NUM_PIECES_PER_FACE)] for j in range(NUM_FACES)]

            for i in range(NUM_FACES):
                for j in range(NUM_PIECES_PER_FACE):
                    megaminx[i][j] = COLORS[i]

            print("Reset Megaminx")
            scramble(megaminx, k)

            solved, depth, nodesExpanded = astar(megaminx)

            if solved is not None:
                end = time.time()
                total = end - start
                print("Solved " + str(k) + " scramble in "+ str(total) +" seconds with " + str(depth) +" moves and "+str(nodesExpanded) +" nodes expanded.\n ")
                with open('output.txt', 'a') as f:
                    f.writelines("Solved " + str(k) + " scramble in "+ str(total) +" seconds with " + str(depth) +" moves and "+str(nodesExpanded) +" nodes expanded.\n " + str(solved) + '\n\n')
            else:
                print("Failed " + k +" scramble.\n")
                with open('output.txt', 'a') as f:
                    f.writelines("Failed " + k +" scramble.\n")
    
    
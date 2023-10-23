# AStar-Megaminx
This program first creates a solved megaminx puzzle, then randomizes that puzzle 5 times for each k from 3 to 9. I stopped the randomization at 9 because I found that my computer starts to run out of memory at that point. 
To randomize, only clockwise moves were used. On each of these randomized puzzles, the A* algorithm is applied to them to solve the puzzle. In each step of the algorithm, the state with the smallest f value is popped off the ‘unexplored’ heap and is tested to see if it is the solved state. 
If it is in the solved state, then the algorithm is returned. If not, the new state is added to the ‘explored’ set, and each face is rotated counterclockwise 1 time to create 12 new states. If these states have not already been explored, then the f value is computed, which is the heuristic of the newly created state added with the depth of the new state.
These values are then pushed into the ‘unexplored’ heap, and the algorithm loops back to the start. After each cube is solved, the amount of time it took to solve, the number of moves, and the number of nodes expanded are all printed to the terminal, and to a file named ‘output.txt’ to check the results more easily.
Simply running this code will automatically create 5 k randomized puzzles for each k from 3 to 9, and print the results as the solving occurs.


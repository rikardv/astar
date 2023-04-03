
# 8 puzzle solver with A*

This code provides a solution to solve a sliding puzzle game using A* search algorithm with two different heuristic functions: Manhattan distance and the number of misplaced tiles.

The PuzzleState class represents a state of the puzzle, which contains the current state, the parent state, the move to get to the current state, the depth of the state in the search tree, and a score that is calculated by adding the depth and the result of a heuristic function. There are three main functions to calculate the score and two heuristic functions to choose from.

The solve_puzzle function takes an initial state of the puzzle as input and uses the A* search algorithm to find the solution. The function creates an instance of the PuzzleState class with the initial state and adds it to a priority queue. The priority queue is then used to store and sort the states based on their score. The function continues to loop over the states in the priority queue until the goal state is found or there are no more states left in the queue. It prints the path to the solution and the number of moves needed to solve the puzzle if the solution is found. Otherwise, it returns that the puzzle cannot be solved.

There are some test data at the end of the code to try out different initial states of the puzzle. The user can modify and run the code with their own test cases.


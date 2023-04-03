from queue import PriorityQueue

class PuzzleState:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.score = self.get_score()
    
    # For the priority queue to make the comparision
    def __lt__(self, other):
        return self.score < other.score
     
    def get_score(self):
        return self.depth + self.get_heuristic()
    
    # Manhattan distance heuristic
    def get_manhattan_heuristic(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j]-1, 3)
                    h += abs(x-i) + abs(y-j)
        return h

    # Number of misplaced tiles heuristic
    def get_misplaced_heuristic(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0 and self.state[i][j] != 3*i + j + 1:
                    h += 1
        return h
    
    # find zero position of the puzzle
    # [[1, 2, 3], [4, 0, 6], [7, 5, 8]] ---> (1,1)
    def get_zero_pos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)
    
    # Takes in a puzzle and generate all possible combinations
    def get_successors(self):
        i, j = self.get_zero_pos()
        successors = []
        if i > 0: # swap with upper
            successors.append(self.swap((i, j), (i-1, j)))
        if i < 2: # swap with lower
            successors.append(self.swap((i, j), (i+1, j)))
        if j > 0: # swap with left
            successors.append(self.swap((i, j), (i, j-1)))
        if j < 2: # swap with right
            successors.append(self.swap((i, j), (i, j+1)))
        return successors
    
    def swap(self, pos1, pos2):
        # Extract the row and column indices from the position tuples
        i1, j1 = pos1
        i2, j2 = pos2
        
        # Create a new copy of the state
        new_state = [row[:] for row in self.state]
        
        # Swap the values in the corresponding positions
        new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
        return PuzzleState(new_state, self, (i2, j2), self.depth+1)
    
    # Helper function to see how the solution was found by following parent nodes
    def print_path(self):
        path = []
        curr = self
        while curr:
            path.append(curr)
            curr = curr.parent
        path.reverse()
        for state in path:
            print(state)
            print()
            print('|')
            print('|')
            print('V')
            print()
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))

    # Function in order to print the states
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.state])
    
def solve_puzzle(initial_state):
    start_state = PuzzleState(initial_state)
    visited_states = set()
    pq = PriorityQueue()
    pq.put(start_state)
    while not pq.empty():
        curr_state = pq.get()
        print("Looking for successors of:")
        print(curr_state)
        print('\n')
        if curr_state.get_manhattan_heuristic() == 0:
            print("Solved in", curr_state.depth, "moves!")
            curr_state.print_path()
            return
        visited_states.add(curr_state)
        for successor in curr_state.get_successors(): # put all successors in priority queue
            if successor in visited_states: #make sure we don't go to same state again
                continue
            print(successor.score)
            print(successor)
            print('\n')
            pq.put(successor)
    print("Puzzle cannot be solved!")


## Some test data
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
initial_state_v2 = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
hard_puzzle = [[4,1,2], [5,8,3], [0,7,6]]
solve_puzzle(hard_puzzle)
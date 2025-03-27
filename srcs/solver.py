from srcs.custom_queue import PriorityQueue
from srcs.puzzle import PuzzleState

class Solver:
    def __init__(self, dimension, values, heuristic_fn):
        
        self.queue = PriorityQueue()
        self.initial_state = PuzzleState(dimension, values, heuristic_fn)
        self.queue.add(self.initial_state, self.initial_state.cost)
        self.states_evaluated = 1

    def is_solvable(self):
        """Check if the puzzle is solvable using inversion count"""
        tiles = self.initial_state.tiles
        inversion_count = 0
        
        for i, tile in enumerate(self.initial_state.spiral_iterator()):
            val_i = tile.value if tile.value != 0 else len(tiles)
            
            for other_tile in self.initial_state.spiral_iterator(i+1):
                val_j = other_tile.value if other_tile.value != 0 else len(tiles)
                if val_j < val_i:
                    inversion_count += 1
                    
        return inversion_count % 2 == 0

    def find_solution(self):
        
        if not self.is_solvable():
            raise Exception('This puzzle configuration cannot be solved.')
            
        while True:
            current_state = self.queue.extract()
            
            if current_state is None:
                return None
                
            if current_state.cost == 0:
                return current_state
                
            next_states = current_state.generate_next_states()
            
            for state in next_states:
                self.states_evaluated += 1
                self.queue.add(state, state.cost)
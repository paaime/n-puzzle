from srcs.traverser import SpiralTraverser
from srcs.position import Position
from srcs.tile import Tile

class PuzzleState:
    visited_states = set()

    def __init__(self, dimension, values, heuristic_fn, parent=None, goal_state=None, depth=0):
        self.dimension = dimension
        self.tiles = self._create_tiles(values)
        self._connect_tiles()
        self.empty_tile = self.find_tile_by_value(0)
        self.heuristic_fn = heuristic_fn
        self.parent = parent
        self.goal_state = self._create_goal_state(dimension) if goal_state is None else goal_state
        self.depth = depth

    @property
    def cost(self):
        return self.heuristic_fn(self)

    def spiral_iterator(self, start_index=0):
        for idx, pos in enumerate(SpiralTraverser(self.dimension)):
            if idx >= start_index:
                yield self.get_tile_at_position(pos)

    def _get_solution_states(self):
        """Return the list of states in the solution path"""
        state = self
        states = []
        
        while state is not None:
            states.append(state)
            state = state.parent
        
        states.reverse()
        return states

    def get_solution_path(self):
        """Return a string representation of the solution path with states displayed side by side"""
        # Collect all states in the path
        state = self
        states = []
        
        while state is not None:
            states.append(state)
            state = state.parent
        
        states.reverse()
        
        # If there's only one state, just return its string representation
        if len(states) == 1:
            return str(states[0])
        
        # For puzzles with many states, group them into rows of max 5 states per row
        max_states_per_row = 5
        state_groups = [states[i:i+max_states_per_row] for i in range(0, len(states), max_states_per_row)]
        
        all_results = []
        
        for group in state_groups:
            # Get string representation of each state and split into rows
            state_strings = [str(state) for state in group]
            state_rows = [s.split('\n') for s in state_strings]
            
            # Determine number of rows in each state
            num_rows = len(state_rows[0])
            
            # Create the output with states side by side
            result_rows = []
            for row_idx in range(num_rows):
                row_parts = []
                
                for state_idx, state_row_list in enumerate(state_rows):
                    # Get the current row for this state
                    row_part = state_row_list[row_idx]
                    row_parts.append(row_part)
                
                # Join with even spacing
                result_rows.append("  |  ".join(row_parts))
            
            all_results.append("\n".join(result_rows))
        
        # Join the groups with a divider
        return "\n\n".join(all_results)

    @classmethod
    def _create_goal_state(cls, dimension):
        """Create the goal state for the puzzle""" 
        positions = []
        for idx, pos in enumerate(SpiralTraverser(dimension)):
            val = 0 if idx == (dimension ** 2) - 1 else idx + 1
            positions.append((val, pos))
            
        positions.sort(key=lambda x: f'{x[1].y_coord}{x[1].x_coord}')
        values = [x[0] for x in positions]
        
        result = cls(dimension, values, None, goal_state=True)
        result.goal_state = result
        
        return result

    def __str__(self):
        max_digits = max(len(str(tile.value)) for tile in self.tiles)
        grid_rows = []
        row = []
        
        for idx, tile in enumerate(self.tiles):
            formatted_val = f"{tile.value}{' ' * (max_digits - len(str(tile.value)) + 1)}"
            row.append(formatted_val)
            
            if (idx + 1) % self.dimension == 0:
                grid_rows.append(row)
                row = []
                
        return '\n'.join(''.join(row) for row in grid_rows)

    def _connect_tiles(self):
        for tile in self.tiles:
            tile.discover_adjacent_tiles()

    def _create_tiles(self, values):
        
        tiles = []
        for idx, val in enumerate(values):
            pos = Position.from_index(idx, self.dimension)
            tile = Tile(val, pos, self, idx)
            tiles.append(tile)
        return tiles

    def find_tile_by_value(self, value):
        for tile in self.tiles:
            if tile.value == value:
                return tile
        return None

    def get_tile_at_position(self, position):
        idx = Position.to_index(position, self.dimension)
        return self.tiles[idx]

    def get_state_signature(self):
        return tuple(tile.value for tile in self.tiles)

    def clone(self):
        return type(self)(
            self.dimension, 
            self.get_state_signature(), 
            self.heuristic_fn, 
            parent=self, 
            goal_state=self.goal_state, 
            depth=self.depth+1
        )

    def generate_next_states(self):
        
        possible_moves = [
            self.empty_tile.position.move_up(),
            self.empty_tile.position.move_down(),
            self.empty_tile.position.move_left(),
            self.empty_tile.position.move_right()
        ]
        
        valid_moves = [pos for pos in possible_moves 
                      if pos.within_bounds(self.dimension)]
                      
        next_states = []
        
        for move in valid_moves:
            new_state = self.clone()
            new_state.empty_tile < new_state.get_tile_at_position(move)
            
            signature = new_state.get_state_signature()
            if signature not in self.visited_states:
                self.visited_states.add(signature)
                next_states.append(new_state)
                
        return next_states
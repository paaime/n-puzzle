class Tile:
    def __init__(self, value, position, puzzle, idx):
        self.position = position
        self.puzzle = puzzle
        self._value = value
        self.idx = idx
        self.adjacent_tiles = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val
        if new_val == 0:
            self.puzzle.empty_tile = self

    def discover_adjacent_tiles(self):
        possible_positions = [
            self.position.move_up(),
            self.position.move_right(),
            self.position.move_down(),
            self.position.move_left()
        ]
        
        valid_positions = [pos for pos in possible_positions 
                          if pos.within_bounds(self.puzzle.dimension)]
        
        self.adjacent_tiles = [self.puzzle.get_tile_at_position(pos) 
                              for pos in valid_positions]

    def swap_values(self, other_tile):
        self.value, other_tile.value = other_tile.value, self.value

    def __lt__(self, other):
        if self.value != 0:
            raise ValueError('Only the empty tile can move to another position')
        self.swap_values(other)

    def __gt__(self, other):
        if other.value != 0:
            raise ValueError('Can only move a tile to the empty position')
        self.swap_values(other)
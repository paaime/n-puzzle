from functools import total_ordering

@total_ordering
class Position:
    def __init__(self, x_coord, y_coord, is_delta=False):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_delta = is_delta

    def __repr__(self):
        delta_param = ', is_delta=True' if self.is_delta else ''
        return f'{self.__class__.__name__}({self.x_coord}, {self.y_coord}{delta_param})'

    def __sub__(self, other):
        if not isinstance(other, Position):
            raise ValueError('Subtraction only supported between Position objects')
            
        x_diff = abs(self.x_coord - other.x_coord)
        y_diff = abs(self.y_coord - other.y_coord)
        return Position(x_diff, y_diff, is_delta=True)

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def __lt__(self, other):
        if not isinstance(other, Position):
            raise ValueError('Cannot compare Position with non-Position object')
        if self.y_coord != other.y_coord:
            return self.y_coord < other.y_coord
        return self.x_coord < other.x_coord

    def move_up(self):
        return Position(self.x_coord, self.y_coord - 1)
        
    def move_down(self):
        return Position(self.x_coord, self.y_coord + 1)
        
    def move_right(self):
        return Position(self.x_coord + 1, self.y_coord)
        
    def move_left(self):
        return Position(self.x_coord - 1, self.y_coord)

    def within_bounds(self, grid_size, exception=None):
        in_bounds = 0 <= self.x_coord < grid_size and 0 <= self.y_coord < grid_size
        if exception is not None and not in_bounds:
            raise exception
        return in_bounds

    def manhattan_distance(self):
        if not self.is_delta:
            raise ValueError('Manhattan distance only applicable to delta positions')
        return self.x_coord + self.y_coord

    @classmethod
    def from_index(cls, idx, grid_size):
        if idx < 0:
            raise ValueError('Index must be non-negative')
        row = idx // grid_size
        col = idx % grid_size
        return cls(col, row)

    @staticmethod
    def to_index(pos, grid_size):
        return pos.y_coord * grid_size + pos.x_coord
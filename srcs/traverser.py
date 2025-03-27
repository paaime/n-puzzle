from srcs.position import Position

class SpiralTraverser:
    def __init__(self, dimension):
        self.dimension = dimension

    def __iter__(self):
        col, row = 0, 0
        right_bound = self.dimension - 1
        left_bound = 0
        top_bound = 0
        bottom_bound = self.dimension - 1
        
        # Direction functions
        move = [
            lambda c, r: (c + 1, r),  # right
            lambda c, r: (c, r + 1),  # down
            lambda c, r: (c - 1, r),  # left
            lambda c, r: (c, r - 1)   # up
        ]
        
        # Bound adjustment functions
        adjust_bounds = [
            lambda r, l, t, b: (r, l, t + 1, b),    # after right
            lambda r, l, t, b: (r - 1, l, t, b),    # after down
            lambda r, l, t, b: (r, l, t, b - 1),    # after left
            lambda r, l, t, b: (r, l + 1, t, b)     # after up
        ]
        
        direction = 0

        for _ in range(self.dimension ** 2):
            yield Position(col, row)
            
            new_col, new_row = move[direction](col, row)
            
            # Check if we need to change direction
            if (new_col < left_bound or new_col > right_bound or 
                new_row < top_bound or new_row > bottom_bound):
                
                right_bound, left_bound, top_bound, bottom_bound = adjust_bounds[direction](
                    right_bound, left_bound, top_bound, bottom_bound)
                
                direction = (direction + 1) % 4
                new_col, new_row = move[direction](col, row)
                
            col, row = new_col, new_row
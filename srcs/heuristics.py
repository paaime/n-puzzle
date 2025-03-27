from srcs.position import Position

def manhattan_distance(puzzle):
    """Sum of Manhattan distances between each tile and its goal position"""
    total = 0
    for num in range(puzzle.dimension ** 2):
        current = puzzle.find_tile_by_value(num)
        goal = puzzle.goal_state.find_tile_by_value(num)
        
        diff = current.position - goal.position
        total += diff.manhattan_distance()
    
    return total

def misplaced_tiles(puzzle):
    """Count of tiles that are not in their goal position"""
    count = 0
    for num in range(puzzle.dimension ** 2):
        # Skip the empty tile (0)
        if num == 0:
            continue
            
        current = puzzle.find_tile_by_value(num)
        goal = puzzle.goal_state.find_tile_by_value(num)
        
        if current.position != goal.position:
            count += 1
    
    return count

def linear_conflict(puzzle):
    """
    Manhattan distance plus linear conflict
    A linear conflict occurs when two tiles are in their goal row/column but in wrong order
    Each conflict forces one tile to move out of the row/column and back in (adding 2 moves)
    """
    # Start with the Manhattan distance
    total = manhattan_distance(puzzle)
    
    # Add the linear conflict penalty
    total += row_conflicts(puzzle) * 2
    total += column_conflicts(puzzle) * 2
    
    return total

def row_conflicts(puzzle):
    """Count conflicts in each row"""
    conflicts = 0
    dim = puzzle.dimension
    
    for row in range(dim):
        # Get tiles in this row that belong in this row in the goal state
        tiles_in_row = []
        for col in range(dim):
            pos = Position(row, col)
            tile = puzzle.get_tile_at_position(pos)
            
            # Skip empty tile
            if tile.value == 0:
                continue
                
            # Get the goal position for this tile
            goal_pos = puzzle.goal_state.find_tile_by_value(tile.value).position
            
            # If tile belongs in this row in the goal state, add it
            if goal_pos.y_coord == row:
                tiles_in_row.append((tile.value, col, goal_pos.x_coord))
        
        # Count conflicts in this row
        for i in range(len(tiles_in_row)):
            for j in range(i + 1, len(tiles_in_row)):
                # If tile i is to the right of tile j but should be to the left, conflict
                if tiles_in_row[i][1] < tiles_in_row[j][1] and tiles_in_row[i][2] > tiles_in_row[j][2]:
                    conflicts += 1
                # If tile j is to the right of tile i but should be to the left, conflict
                elif tiles_in_row[i][1] > tiles_in_row[j][1] and tiles_in_row[i][2] < tiles_in_row[j][2]:
                    conflicts += 1
    
    return conflicts

def column_conflicts(puzzle):
    """Count conflicts in each column"""
    conflicts = 0
    dim = puzzle.dimension
    
    for col in range(dim):
        # Get tiles in this column that belong in this column in the goal state
        tiles_in_col = []
        for row in range(dim):
            pos = Position(row, col)
            tile = puzzle.get_tile_at_position(pos)
            
            # Skip empty tile
            if tile.value == 0:
                continue
                
            # Get the goal position for this tile
            goal_pos = puzzle.goal_state.find_tile_by_value(tile.value).position
            
            # If tile belongs in this column in the goal state, add it
            if goal_pos.x_coord == col:
                tiles_in_col.append((tile.value, row, goal_pos.y_coord))
        
        # Count conflicts in this column
        for i in range(len(tiles_in_col)):
            for j in range(i + 1, len(tiles_in_col)):
                # If tile i is below tile j but should be above, conflict
                if tiles_in_col[i][1] < tiles_in_col[j][1] and tiles_in_col[i][2] > tiles_in_col[j][2]:
                    conflicts += 1
                # If tile j is below tile i but should be above, conflict
                elif tiles_in_col[i][1] > tiles_in_col[j][1] and tiles_in_col[i][2] < tiles_in_col[j][2]:
                    conflicts += 1
    
    return conflicts
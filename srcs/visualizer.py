import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "Hide"

import pygame
import time

class PuzzleVisualizer:
    """Visualizes the N-puzzle and its solution"""
    
    def __init__(self, size, tile_size=100, animation_speed=0.3):
        """
        Initialize the visualizer.
        
        Args:
            size: Size of the puzzle (N for NxN)
            tile_size: Pixel size of each tile
            animation_speed: Delay between moves in seconds
        """
        self.size = size
        self.tile_size = tile_size
        self.animation_speed = animation_speed
        self.width = size * tile_size
        self.height = size * tile_size
        
        # Colors
        self.bg_color = (240, 240, 240)
        self.tile_color = (100, 149, 237)  # Cornflower blue
        self.text_color = (255, 255, 255)
        self.highlight_color = (50, 205, 50)  # Lime green
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"{size}x{size} N-Puzzle Solver")
        self.font = pygame.font.SysFont('Arial', tile_size // 3)
        
    def draw_puzzle(self, puzzle_state, highlight=None):
        """Draw the puzzle state"""
        self.screen.fill(self.bg_color)
        
        for i in range(self.size):
            for j in range(self.size):
                # Get tile at this position
                idx = i * self.size + j
                tile = puzzle_state.tiles[idx]
                value = tile.value
                
                if value != 0:  # Skip the empty tile
                    rect = pygame.Rect(
                        j * self.tile_size, 
                        i * self.tile_size,
                        self.tile_size - 4, 
                        self.tile_size - 4
                    )
                    
                    # Use highlight color if this tile just moved
                    color = self.highlight_color if highlight == value else self.tile_color
                    
                    pygame.draw.rect(self.screen, color, rect, border_radius=10)
                    
                    # Draw the number
                    text = self.font.render(str(value), True, self.text_color)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    def visualize_solution(self, solution_states):
        """Visualize the solution path"""
        if not solution_states:
            return
            
        # Draw initial state
        self.draw_puzzle(solution_states[0])
        pygame.time.wait(1000)  # Wait 1 second before starting
        
        # Find the moving tile between each pair of states
        for i in range(1, len(solution_states)):
            prev_state = solution_states[i-1]
            curr_state = solution_states[i]
            
            # Find the tile that moved
            moved_tile = None
            for idx, (prev_tile, curr_tile) in enumerate(zip(prev_state.tiles, curr_state.tiles)):
                if prev_tile.value != 0 and prev_tile.value != curr_tile.value:
                    moved_tile = prev_tile.value
                    break
            
            # Draw the current state with the moved tile highlighted
            self.draw_puzzle(curr_state, highlight=moved_tile)
            
            # Check for quit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            
            # Delay between moves
            time.sleep(self.animation_speed)
        
        # Keep the final state visible until user closes the window
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
        
        pygame.quit()
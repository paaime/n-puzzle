#!/usr/bin/env python3
import argparse
import time
import signal
import sys
from srcs.parser import FileParser
from srcs.solver import Solver
from srcs.heuristics import  manhattan_distance, linear_conflict, misplaced_tiles
from srcs.visualizer import PuzzleVisualizer
from srcs.utils import generate_random_puzzle

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BRIGHT_YELLOW = "\033[93m"

def keyboard_interrupt_handler(signal, frame):
    print("\n\nProgram stopped by user. Exiting...")
    sys.exit(0)

def main():
    # Set up keyboard interrupt handler
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Solve N-puzzle using A* algorithm')
    
    # Source options
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument('-f', '--file', help='Path to puzzle file')
    source_group.add_argument('-r', '--random', type=int, help='Generate random puzzle of given size')
    
    # Heuristic options
    parser.add_argument('-H', '--heuristic', 
                      choices=['manhattan', 'linear_conflict', 'misplaced'],
                      default='manhattan',
                      help='Heuristic function to use')
    
    # Visualization options
    parser.add_argument('-v', '--visualize', action='store_true',
                      help='Visualize the solution')
    parser.add_argument('-s', '--speed', type=float, default=0.3,
                      help='Animation speed (seconds between moves)')
    
    
    # Parse arguments
    args = parser.parse_args()

    # Ensure speed is within valid range (0.01 to 1.0)
    args.speed = min(max(args.speed, 0.01), 1.0)
    
    # Map heuristics
    heuristics = {
        'manhattan': manhattan_distance,
        'linear_conflict': linear_conflict,
        'misplaced': misplaced_tiles
    }
    
    heuristic_fn = heuristics[args.heuristic]
    
    # Get puzzle data
    try:
        if args.file:
            dimension, values = FileParser(args.file).extract_puzzle_data()
            print(f"Loaded puzzle of size {dimension} from file {args.file}")
        else:
            if args.random <= 1:
                raise ValueError("Random puzzle size must be greater than 1")
            dimension, values = generate_random_puzzle(args.random)
            print(f"Generated random puzzle of size {args.random}")
        
        # Initialize and solve
        print(f"\nSolving with {args.heuristic} heuristic...")
        start_time = time.time()
        
        try:
            puzzle_solver = Solver(dimension, values, heuristic_fn)
            
            # Check solvability
            if not puzzle_solver.is_solvable():
                raise ValueError("Puzzle is not solvable")
            
            # Solve the puzzle
            solution = puzzle_solver.find_solution()
            elapsed_time = time.time() - start_time
            
            if solution:
                print("\nSolution found!\n")
                print(solution.get_solution_path())
                print()
                print(f"{Colors.BOLD}Number of moves:{Colors.RESET} {Colors.BRIGHT_YELLOW}{solution.depth}{Colors.RESET}")
                print(f"{Colors.BOLD}Time complexity:{Colors.RESET} {Colors.BRIGHT_YELLOW}{puzzle_solver.states_evaluated}{Colors.RESET} states evaluated")
                print(f"{Colors.BOLD}Space complexity:{Colors.RESET} {Colors.BRIGHT_YELLOW}{puzzle_solver.queue.peak_size}{Colors.RESET} states in memory")
                print(f"Solved in {Colors.BOLD}{Colors.BRIGHT_YELLOW}{elapsed_time:.4f} seconds{Colors.RESET}")
                
                # Visualize if requested
                if args.visualize:
                    print("\nVisualizing solution...")
                    solution_states = solution._get_solution_states()
                    visualizer = PuzzleVisualizer(dimension, animation_speed=args.speed)
                    visualizer.visualize_solution(solution_states)
            else:
                print("\nNo solution found.")
                
        except KeyboardInterrupt:
            elapsed_time = time.time() - start_time
            print("\n\nProgram stopped by user after {:.2f} seconds".format(elapsed_time))
            return
            
    except ValueError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram stopped by user. Exiting...")
        sys.exit(0)
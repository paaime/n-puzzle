from srcs.utils import exit_with_message

class FileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.content_lines = self._extract_content(self.file_path)
        if len(self.content_lines) < 4:
            exit_with_message('Not enough data in input file.')

    def _extract_content(self, path):
        try:
            lines = []
            with open(path, 'r') as input_file:
                for line in input_file:
                    clean_line = line.split('#')[0].strip()
                    if clean_line:
                        lines.append(clean_line)
            return lines
        except Exception:
            exit_with_message('Unable to open or read the specified file.')

    def extract_puzzle_data(self):
        dimension_line = self.content_lines[0]
        puzzle_lines = self.content_lines[1:]
        dimension = self._parse_dimension(dimension_line)
        
        return dimension, self._parse_puzzle_data(puzzle_lines, dimension)

    def _parse_dimension(self, dimension_line):
        try:
            dim = int(dimension_line)
            if dim < 3:
                exit_with_message('Puzzle size must be at least 3.')
            return dim
        except:
            exit_with_message('Invalid puzzle size format.')

    def _parse_puzzle_data(self, lines, dimension):
        if len(lines) != dimension:
            exit_with_message('Number of rows does not match specified dimension.')

        values = []
        try:
            for line in lines:
                row_values = line.split()
                if len(row_values) != dimension:
                    exit_with_message('Number of columns does not match specified dimension.')
                
                for val_str in row_values:
                    value = int(val_str)
                    if value < 0:
                        exit_with_message('Negative values are not allowed in the puzzle.')
                    values.append(value)
        except:
            exit_with_message('Invalid number format in puzzle data.')

        self._validate_puzzle_values(values)
        return values

    def _validate_puzzle_values(self, values):
        if len(set(values)) != len(values):
            exit_with_message('Duplicate values detected in puzzle.')
        if max(values) != len(values) - 1:
            exit_with_message('Invalid value range in puzzle data.')
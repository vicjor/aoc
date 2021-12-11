from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import Dict, Hashable, List, Set, Tuple
from functools import reduce


def find_lowpoints(heightmap: List[str]) -> List[str]:
    """Find all lowpoints in heightmap (lower than any adjacent locations)."""
    lowpoints = []
    lowpoints_coordinates = {}
    for i, row in enumerate(heightmap):
        for j, col in enumerate(row):
            if is_lowpoint(heightmap, i, j):
                lowpoints_coordinates[(i, j)] = col
    return lowpoints_coordinates


def is_lowpoint(heightmap: List[str], row: int, col: int) -> bool:
    """Return whether a single point is a low point or not."""
    point = int(heightmap[row][col])
    # Bottom row
    if row == len(heightmap) - 1:
        if col == len(heightmap[row]) - 1:
            # Bottom right
            if point < int(heightmap[row][col-1]) and point < int(heightmap[row-1][col]):
                return True
            return False
        # Bottom left
        elif col == 0:
            if point < int(heightmap[row][col+1]) and point < int(heightmap[row-1][col]):
                return True
            return False
        else:
            if point < int(heightmap[row][col+1]) and point < int(heightmap[row][col-1]) and point < int(heightmap[row-1][col]):
                return True
            return False
    # Top row
    elif row == 0:
        # Top left
        if col == 0:
            if point < int(heightmap[row+1][col]) and point < int(heightmap[row][col+1]):
                return True
            return False
        # Top right
        elif col == len(heightmap[row]) - 1:
            if point < int(heightmap[row][col-1]) and point < int(heightmap[row+1][col]):
                return True
            return False
        else:
            if point < int(heightmap[row][col+1]) and point < int(heightmap[row][col-1]) and point < int(heightmap[row+1][col]):
                return True
            return False
    # Right edge
    elif col == len(heightmap[row])-1:
        if point < int(heightmap[row+1][col]) and point < int(heightmap[row-1][col]) and point < int(heightmap[row][col-1]):
            return True
        return False
    # Left edge
    elif col == 0:
        if point < int(heightmap[row+1][col]) and point < int(heightmap[row-1][col]) and point < int(heightmap[row][col+1]):
            return True
        return False
    # For all cases that is not top, bot, left or right edge.
    else:
        if point < int(heightmap[row][col+1]) and point < int(heightmap[row+1][col]) and point < int(heightmap[row][col-1]) and point < int(heightmap[row-1][col]):
            return True
        return False


def get_risk_level(lowpoints_coordinates: Dict[Tuple[int, int], str]) -> int:
    """Add one to all low points and sum."""
    risk_level = map(lambda x: int(x)+1, list(lowpoints_coordinates.values()))
    return sum(risk_level)


class BasinFinder:
    """
    Class to help find basin size by using DFS.
    """

    def __init__(self, heightmap: List[str]):
        self.heightmap = heightmap

    def is_valid(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.heightmap) and 0 <= col < len(self.heightmap[0])

    def get_neighbors(self, row: int, col: int) -> List[Tuple[int, int]]:
        neighbors = []
        if self.is_valid(row+1, col):
            neighbors.append((row+1, col))
        if self.is_valid(row-1, col):
            neighbors.append((row-1, col))
        if self.is_valid(row, col+1):
            neighbors.append((row, col+1))
        if self.is_valid(row, col-1):
            neighbors.append((row, col-1))
        return neighbors

    def get_basin_size(self, heightmap: List[str], row: int, col: int, visited: Set[Tuple[int, int]] = None):
        """Recursive DFS."""
        visited = visited or {(row, col)}
        neighbors = self.get_neighbors(row, col)
        for _ in neighbors:
            i, j = _[0], _[1]
            if (i, j) not in visited and self.is_valid(i, j) and int(heightmap[i][j]) < 9:
                visited.add((i, j))
                self.get_basin_size(heightmap, i, j, visited)
        return len(visited)


def find_basins(lowpoints_coordinates: Dict[Tuple[int, int], str], heightmap: List[str]) -> List[int]:
    """Return three largest basins"""
    basins = []
    lowpoints = list(lowpoints_coordinates.keys())
    for point in lowpoints:
        row, col = point[0], point[1]
        bf = BasinFinder(heightmap)
        basin = bf.get_basin_size(heightmap, row, col)
        basins.append(basin)
        # Sort list so the three largest basins are at the end of the list
        basins = sorted(basins)
    return basins[len(basins)-3::]


def multiply_basins(basins: List[int]) -> int:
    """Return product of three largest basins"""
    return reduce(lambda x, y: x*y, basins)


def main():
    heightmap = file_reader("data/input9.txt")
    lowpoints = find_lowpoints(heightmap)
    risk_level = get_risk_level(lowpoints)
    print("## PART 1 ##")  # 603.
    print(f"The sum of the risk level in the heightmap is {risk_level}.\n")

    print("## PART 2 ##")  # 786780.
    basins = find_basins(lowpoints, heightmap)
    basins_multiplied = multiply_basins(basins)
    print(f"Three largest basins {basins} multiplied is {basins_multiplied}.\n")


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")

from collections import defaultdict
from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import DefaultDict, List


def create_graph(data: List[str]):
    """Create a graph G from input data."""
    G = defaultdict(list)
    for nodes in data:
        x, y = nodes.split("-")[0:2]
        G[x].append(y)
        G[y].append(x)
    return G


def is_valid(G: DefaultDict[str, List[str]], path: List[List[str]], node: List[str]) -> bool:
    """Check if adding a node to a path is valid"""
    if node == 'end':
        return True
    elif node == 'start':
        return False
    elif node.islower() and node in path:
        return False
    else:
        return True


def has_two_small_caves(path: List[str]) -> bool:
    """Return whether a given path already have two small caves in it."""
    small_caves = [x for x in path if x.islower()]
    return len(small_caves) != len(set(small_caves))


def is_valid_2(G: DefaultDict[str, List[str]], path: List[str], node: str) -> bool:
    """Check if adding a node to a path is valid, allowing a single small cave to be visited twice."""
    if node == 'end':
        return True
    elif node == 'start':
        return False
    elif node.islower() and node in path:
        if not has_two_small_caves(path):
            return True
        return False
    else:
        return True


def find_all_paths(G: List[List[str]], start: str, end: str, path=[], pt_2=False) -> List[List[str]]:
    """DFS. Recursively find all paths from start to end."""
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in G[start]:
        if pt_2:
            if is_valid_2(G, path, node):
                paths_from_node = find_all_paths(G, node, end, path, pt_2=True)
                for p in paths_from_node:
                    paths.append(p)
        else:
            if is_valid(G, path, node):
                paths_from_node = find_all_paths(G, node, end, path)
                for p in paths_from_node:
                    paths.append(p)
    return paths


def main():
    data = file_reader("data/input12.txt")
    G = create_graph(data)
    number_of_paths = len(find_all_paths(G, "start", "end"))
    number_of_paths_2 = len(find_all_paths(G, "start", "end", pt_2=True))
    print("## PART 1 ##")
    print(f"{number_of_paths} paths from start to end.")  # 3761
    print("## PART 2 ##")
    # 99138
    print(f"{number_of_paths_2} paths when allowing a single small cave to be visited twice.")


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")

import sys
from pprint import pprint

# Check if it is possible to go to (x, y) from the current position.
def isSafe(mat, visited, x, y):
    '''
    This function returns false if the cell is invalid
    AND has value 0 or already visited
    '''
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and \
           not (mat[x][y] == 0 or visited[x][y])


# Find the shortest possible route in a matrix `mat` from source cell (i, j)
# to destination cell `dest`.

# `min_dist` stores the length of the longest path from source to a destination
# found so far, and `dist` maintains the length of the path from a source cell to
# the current cell (i, j).

ALL_PATHS = {}

def findShortestPath(mat, visited, i, j, dest, min_dist=sys.maxsize, dist=0, path=[]):

    # if the destination is found, aka if we've found a path, updated the min
    # row , col
    if (i, j) == dest:
        ALL_PATHS[str(path)] = path
        return min(dist, min_dist)

    # set (i, j) cell as visited
    visited[i][j] = 1

    # go to the bottom cell
    if isSafe(mat, visited, i + 1, j):

        min_dist = findShortestPath(mat, visited, i + 1, j, dest, min_dist, dist + 1, path + [(i + 1,  j)])

    # go to the right cell
    if isSafe(mat, visited, i, j + 1):
        min_dist = findShortestPath(mat, visited, i, j + 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])

    # go to the top cell
    if isSafe(mat, visited, i - 1, j):
        min_dist = findShortestPath(mat, visited, i - 1, j, dest, min_dist, dist + 1, path + [(i + 1,  j)])

    # go to the left cell
    if isSafe(mat, visited, i, j - 1):
        min_dist = findShortestPath(mat, visited, i, j - 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])


    # DIAGONAL DIRECTIONS

    # north west
    if isSafe(mat, visited, i - 1, j - 1):
        min_dist = findShortestPath(mat, visited, i - 1, j - 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])

    # south east
    if isSafe(mat, visited, i + 1, j + 1):
        min_dist = findShortestPath(mat, visited, i + 1, j + 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])

    # north east
    if isSafe(mat, visited, i - 1, j + 1):
        min_dist = findShortestPath(mat, visited, i - 1, j + 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])
    # south west
    if isSafe(mat, visited, i + 1, j - 1):
        min_dist = findShortestPath(mat, visited, i + 1, j - 1, dest, min_dist, dist + 1, path + [(i + 1,  j)])
    #backtrack: remove (i, j) from the visited matrix
    visited[i][j] = 0

    return min_dist


# Wrapper over findShortestPath() function
def findShortestPathLength(mat, src, dest):

    # get source cell (i, j)
    i, j = src

    # get destination cell (x, y)
    x, y = dest

    # base case
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1

    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # construct an `M × N` matrix to keep track of visited cells
    # _ is a placeholder , we want 3 False's in the list
    visited = [[False for _ in range(N)] for _ in range(M)]

    min_dist = findShortestPath(mat, visited, i, j, dest)

    # print(30 * "*")
    # pprint(ALL_PATHS)
    # print(30 * "*")

    for k, v in ALL_PATHS.items():
        if len(v) == min_dist:
            for i, j in v:
                print(f"({i}, {j})", end= "-")

    if min_dist != sys.maxsize:
        return min_dist
    return -1


if __name__ == '__main__':

    # mat = [
    #     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    #     [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    #     [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    #     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    #     [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    # ]
    # mat2 = [
    #     [1,0],
    #     [1, 1]
    # ]

    mat3 = [
        [1,0,0],
        [1,0,0],
        [1,1,1]
    ]

    mat4 = [
        [1,0,0],
        [1,1,0],
        [1,1,1]
    ]

    src = (0, 0)
    dest = (2, 2)

    min_dist = findShortestPathLength(mat3, src, dest)

    if min_dist != -1:
        print("The shortest path from source to destination has length", min_dist)
    else:
        print("Destination cannot be reached from source")

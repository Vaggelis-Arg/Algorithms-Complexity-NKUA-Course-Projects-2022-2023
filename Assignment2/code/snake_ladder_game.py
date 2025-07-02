from collections import deque


def bfs_min_dice_throws(G, end):
    dist = {v: float('inf') for v in G}
    dist[1] = 0
    queue = deque()
    queue.append(1)
    while queue:
        curr_cell = queue.popleft()
        if curr_cell == end:
            return dist[curr_cell]
        for next_cell in G[curr_cell]:
            if dist[next_cell] == float('inf'):
                dist[next_cell] = dist[curr_cell] + 1
                queue.append(next_cell)
    return None


if __name__ == "__main__":
    '''
    This example shows the board from Exercise 3 of our assignment.
    The board is represented as a graph using an adjacency list.
    '''
    grid = {
        1: [2, 15, 4, 5, 6, 6],
        2: [15, 4, 5, 6, 6, 19],
        4: [5, 6, 6, 19, 9, 10],
        5: [6, 6, 19, 9, 10, 11],
        6: [6, 19, 9, 10, 11, 12],
        9: [10, 11, 12, 1, 14, 15],
        10: [11, 12, 1, 14, 15, 16],
        11: [12, 1, 14, 15, 16, 17],
        12: [1, 14, 15, 16, 17, 18],
        13: [14, 15, 16, 17, 18, 19],
        14: [15, 16, 17, 18, 19, 33],
        15: [16, 17, 18, 19, 33, 9],
        16: [17, 18, 19, 33, 9, 22],
        17: [18, 19, 33, 9, 22, 23],
        18: [19, 33, 9, 22, 23, 35],
        19: [33, 9, 22, 23, 35, 25],
        22: [23, 35, 25, 26, 27, 28],
        23: [35, 25, 26, 27, 28, 29],
        25: [26, 27, 28, 29, 30, 31],
        26: [27, 28, 29, 30, 31, 32],
        27: [28, 29, 30, 31, 32, 33],
        28: [29, 30, 31, 32, 33, 22],
        29: [30, 31, 32, 33, 22, 35],
        30: [31, 32, 33, 22, 35, 36],
        31: [32, 33, 22, 35, 36, 35],
        32: [33, 22, 35, 36, 35, 22],
        33: [22, 35, 36, 35, 22, 33],
        35: [36, 35, 22, 33, 32, 31],
        36: []
    }
    
    end_cell = 36
    
    print("Minimum number of dice throws to reach cell", end_cell, ":", bfs_min_dice_throws(grid, end_cell))

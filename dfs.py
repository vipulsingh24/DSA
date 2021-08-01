from stack import Stack
from helper import get_path, offsets, is_legal_pos

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_cell

    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 4 for row in range(3)]
    print(maze)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    print(result)
    # assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
            

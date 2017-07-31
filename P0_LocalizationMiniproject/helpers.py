def normalize(grid):
    total = 0.0
    for row in grid:
        for cell in row:
            total += cell
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            grid[i][j] = float(cell) / total
    return grid


def blur(grid, blurring):
    height = len(grid)
    width  = len(grid[0])

    center_prob = 1.0-blurring
    corner_prob = blurring / 12.0
    adjacent_prob = blurring / 6.0

    window = [
            [corner_prob,  adjacent_prob,  corner_prob],
            [adjacent_prob, center_prob,  adjacent_prob],
            [corner_prob,  adjacent_prob,  corner_prob]
        ]
    new = [[0.0 for i in range(width)] for j in range(height)]
    for i in range(height):
        for j in range(width):
            grid_val = grid[i][j]
            for dx in range(-1,2):
                for dy in range(-1,2):
                    mult = window[dx+1][dy+1]
                    new_i = (i + dy) % height
                    new_j = (j + dx) % width
                    new[new_i][new_j] += mult * grid_val
    return normalize(new)

def is_robot_localized(beliefs, true_pos):

    best_belief = 0.0
    best_pos = None
    second_best = 0.0
    for y, row in enumerate(beliefs):
        for x, belief in enumerate(row):
            if belief > best_belief:
                second_best = best_belief
                best_belief = belief
                best_pos = (y,x)
            elif belief > second_best:
                second_best = belief
    if best_belief / second_best > 2.0:
        # robot thinks it knows where it is
        return best_pos == true_pos
    else:
        # No strong single best belief
        return None
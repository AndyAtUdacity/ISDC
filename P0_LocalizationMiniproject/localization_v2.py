from helpers import normalize, blur

class Robot():
    p_hit = 3.0
    p_miss = 1.0
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.beliefs = self.initialize_beliefs()

    def initialize_beliefs(self):
        height = len(self.grid)
        width  = len(self.grid[0])
        area = height * width
        belief_per_cell = 1.0 / area
        return [[belief_per_cell for i in range(width)] for j in range(height)]

    def move(self, dy, dx ):
        new_beliefs = [[0.0 for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                previous_belief = self.beliefs[i][j]
                new_i = (i + dy) % self.height
                new_j = (j + dx) % self.width
                new_beliefs[int(new_i)][int(new_j)] = previous_belief
        self.beliefs = blur(new_beliefs)

    def sense(self, color):
        for i in range(self.height):
            for j in range(self.width):
                cell = self.grid[i][j]
                if cell ==color:
                    self.beliefs[i][j] *= self.p_hit
                else:
                    self.beliefs[i][j] *= self.p_miss
        self.beliefs = normalize(self.beliefs)
class Robot:
    directions = ["up", "right", "down", "left"]

    moves = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, grid):
        n = len(grid)
        m = len(grid[0])

        dx, dy = Robot.moves[self.direction]

        if grid[self.x][self.y] == ".":
            grid[self.x][self.y] = "C"

        while True:
            nx = self.x + dx
            ny = self.y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break

            if grid[nx][ny] == "#":
                break

            self.x = nx
            self.y = ny

            if grid[self.x][self.y] == ".":
                grid[self.x][self.y] = "C"

        self.turn()

    def turn(self):
        i = Robot.directions.index(self.direction)
        self.direction = Robot.directions[(i + 1) % 4]


class Game:
    def __init__(self, r1, r2):
        self.grid = [
            list("#..#.."),
            list(".#...."),
            list("#....."),
            list(".#...."),
            list("...#..")
        ]

        self.r1 = r1
        self.r2 = r2

    def simulate(self):
        for _ in range(15):
            self.r1.move(self.grid)
            self.r2.move(self.grid)

    def count_clean(self):
        count = 0
        for row in self.grid:
            for c in row:
                if c == "C":
                    count += 1
        return count


x1, y1, d1 = input().split()
x2, y2, d2 = input().split()

r1 = Robot(int(x1), int(y1), d1)
r2 = Robot(int(x2), int(y2), d2)

game = Game(r1, r2)

game.simulate()

print(game.count_clean())
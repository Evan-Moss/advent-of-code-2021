with open('input.txt', 'r') as file:
    lines = [[int(x) for x in list(f.strip())] for f in file.readlines()]

class Point:
    def __init__(self, val):
        self.value = val
        self.flashed = False
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()

    def flash(self):
        self.flashed = True
    
    def reset_flash(self):
        self.flashed = False
    
    def step(self):
        if self.value < 9 and not self.flashed:
            self.value += 1
        else:
            self.value = 0
            self.flash()

class Grid:
    def __init__(self, lines):
        self.y_len = len(lines[0])
        self.x_len = len(lines)
        self.lines = lines
        self.get_lines()
        self.flash_queue = []
        self.num_flashes = 0
    
    def get_lines(self):
        for x in range(self.x_len):
            for y in range(self.y_len):
                self.lines[x][y] = Point(lines[x][y])

    def __str__(self):
        ret = ''
        for l in self.lines:
            ret += str(l) + '\n'
        return ret
    
    def get_adjacents(self, x, y):
        x_range = range(x-1 if x-1 >= 0 else 0, x+2 if x+2 < self.x_len else self.x_len)
        y_range = range(y-1 if y-1 >= 0 else 0, y+2 if y+2 < self.y_len else self.y_len)
        adjacents = []
        for xx in x_range:
            for yy in y_range:
                if not (xx == x and yy == y) and not self.lines[xx][yy].flashed:
                    adjacents.append((xx, yy))
        return adjacents

    def update_point(self, x, y):
        self.lines[x][y].step()

    def flash_point(self, x, y):
        adjs = self.get_adjacents(x,y)
        for a in adjs:
            self.update_point(a[0], a[1])
            if self.lines[a[0]][a[1]].flashed:
                self.flash_queue.append((a[0],a[1]))

    def reset_flashes(self):
        if self.all_flashed():
            return
        for y in lines:
            for x in y:
                x.reset_flash()
        self.flash_queue = []

    def all_flashed(self):
        return all([x.flashed for x in sum(self.lines, [])])

    def step(self):
        for y in range(self.y_len):
            for x in range(self.x_len):
                self.update_point(x,y)
                if self.lines[x][y].flashed: self.flash_queue.append((x,y))

        for coord in self.flash_queue:
            self.num_flashes += 1
            self.flash_point(coord[0], coord[1])
                
        self.reset_flashes()

grid = Grid(lines)
counter = 1
while grid.all_flashed() == False:
    grid.step()
    # print(grid)
    if counter == 100:
        # Part 1
        print(grid.num_flashes)
    counter += 1
# Part 2
print(counter)
#0 - поле
#1 - дерево
#2 -река
#3 - госпиталь
#4 - магазин

CELL_TYPES = "🟩🌳🌊🏥🏠"

class Map:

    #def generate_rivers():

    #def generate_firest():

    def print_map(self):
        print("⬛" * (self.w + 2))
        for row in self.cells:
            print("⬛", end="")
            for cell in row:
                if 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.w + 2))

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

battle = Map(30,20)
battle.cells[1][2] = 1
battle.cells[2][4] = 2
battle.cells[4][4] = 3
battle.cells[5][5] = 4
if battle.check_bounds(20,9):
    print("YES")
battle.print_map()
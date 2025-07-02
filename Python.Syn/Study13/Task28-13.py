class Tortuga(object):
    x, y, s = 0, 0, 0

    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        if s <= 0:
            print("< zero")
        self.s = s


    def go_up(self):
        self.y += self.s
        return self.y

    def go_down(self):
        self.y -= self.s
        return self.y

    def go_left(self):
        self.x -= self.s
        return self.x

    def go_right(self):
        self.x += self.s
        return self.x

    def evolve(self):
        self.s -= 1
        return self.s

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        return self.s


    def count_moves(self, x2, y2):
        dist_x = abs(self.x - x2)
        dist_y = abs(self.y - y2)

        move_x = (dist_x + self.s - 1) // self.s
        move_y = (dist_y + self.s - 1) // self.s
        return move_x + move_y

tortila = Tortuga(3,4,2)
print(tortila.go_up())
print(tortila.go_down())
print(tortila.go_left())
print(tortila.go_right())
print(tortila.evolve())
print(tortila.degrade())
print(tortila.count_moves(2,1))
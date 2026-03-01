class Bomb:
    def __init__(self, x, y, time=3):
        self.time = time
        self.x = x
        self.y = y

    def tic(self):
        print(
            f"Bomb fuse is burning, move away from the ({self.x},{self.y}) area ({self.time} moves left)"
        )
        self.time -= 1

    def is_exploding(self):
        return self.time == 0

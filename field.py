import random

class Field:
    def __init__(self, algorithm, size=500) -> None:
        self.field = [i for i in range(size)]
        self.algorithm = algorithm
    
    def shuffle(self) -> None:
        random.shuffle(self.field)

    def is_sorted(self) -> bool:
        for i in range(len(self.field)):
            if self.field[i] != i: return False
        return True

    def sort(self, steps=-1) -> None:
        while steps != 0:
            self.field = self.algorithm(self.field)
            steps -= 1

            if steps < 1 and self.is_sorted(): return
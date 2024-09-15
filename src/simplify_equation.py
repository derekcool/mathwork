import random


class SimplifyEquationL1:
    def generate(self):
        a = random.randint(0, 20) - 10
        if random.randint(1, 10) > 3:
            if a >= 0:
                return "x + {} = 0".format(a)
            else:
                return "x - {} = 0".format(-a)
        else:
            return "{} + x = 0".format(a)


class SimplifyEquationL2:
    def generate(self):
        a = random.randint(0, 20) - 10
        c = random.randint(0, 10) - 5
        if random.randint(1, 10) > 5:
            if a >= 0:
                return "x + {} = {}".format(a, c)
            else:
                return "x - {} = {}".format(-a, c)
        else:
            if random.randint(1, 10) > 5:
                return "{} + x = {}".format(a, c)
            else:
                return "{} - x = {}".format(a, c)

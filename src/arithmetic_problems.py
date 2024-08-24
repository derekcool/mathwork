import random


class AddProblem:
    def __init__(self, min1, max1, min2, max2):
        self._min1 = min1
        self._max1 = max1
        self._min2 = min2
        self._max2 = max2
        self._question = None
        self._answer = None
        self._a = None
        self._b = None
        print("Addition Problems. Range: [{}, {}] + [{}, {}]".format(self._min1, self._max1, self._min2, self._max2))

    def generate(self):
        self._a = random.randint(self._min1, self._max1)
        self._b = random.randint(self._min2, self._max2)
        self._answer = self._a + self._b

    def description(self):
        if self._b < 0:
            return "{} + ({}) = ".format(self._a, self._b)
        else:
            return "{} + {} = ".format(self._a, self._b)

    def check_answer(self, answer):
        try:
            answerint = int(answer.lstrip().rstrip())
            return self._answer == answerint
        except:
            return False


class SubProblem:
    def __init__(self, min1, max1, min2, max2):
        self._min1 = min1
        self._max1 = max1
        self._min2 = min2
        self._max2 = max2
        self._question = None
        self._answer = None
        self._a = None
        self._b = None
        print("Subtraction Problems. Range: [{}, {}] - [{}, {}]".format(self._min1, self._max1, self._min2, self._max2))

    def generate(self):
        self._a = random.randint(self._min1, self._max1)
        self._b = random.randint(self._min2, self._max2)
        self._answer = self._a - self._b

    def description(self):
        if self._b < 0:
            return "{} - ({}) = ".format(self._a, self._b)
        else:
            return "{} - {} = ".format(self._a, self._b)

    def check_answer(self, answer):
        try:
            answerint = int(answer.lstrip().rstrip())
            return self._answer == answerint
        except:
            return False


class MulProblem:
    def __init__(self, min1, max1, min2, max2):
        self._min1 = min1
        self._max1 = max1
        self._min2 = min2
        self._max2 = max2
        self._question = None
        self._answer = None
        self._a = None
        self._b = None
        print("Multiplication Problems. Range: [{}, {}] * [{}, {}]".format(self._min1, self._max1, self._min2, self._max2))

    def generate(self):
        self._a = random.randint(self._min1, self._max1)
        self._b = random.randint(self._min2, self._max2)
        self._answer = self._a * self._b

    def description(self):
        return "{} * {} = ".format(self._a, self._b)

    def check_answer(self, answer):
        try:
            answerint = int(answer.lstrip().rstrip())
            return self._answer == answerint
        except:
            return False


class DivProblem:
    def __init__(self, min1, max1, min2, max2):
        self._answer_min = min1 // max2
        self._answer_max = max1 // min2
        self._divisor_min = min2
        self._divisor_max = max2
        self._question = None
        self._answer = None
        self._a = None
        self._b = None
        print("Division Problems. Range: [{}, {}] / [{}, {}]".format(min1, max1, min2, max2))

    def generate(self):
        self._b = random.randint(self._divisor_min, self._divisor_max)
        self._answer = random.randint(self._answer_min, self._answer_max)
        self._a = self._b * self._answer

    def description(self):
        return "{} / {} = ".format(self._a, self._b)

    def check_answer(self, answer):
        try:
            answerint = int(answer.lstrip().rstrip())
            return self._answer == answerint
        except:
            return False


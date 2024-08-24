import random


class AddProblem:
    def __init__(self, min, max):
        self._min = min
        self._max = max
        self._question = None
        self._answer = None
        self._a = None
        self._b = None

    def generate(self):
        self._a = random.randint(self._min, self._max)
        self._b = random.randint(self._min, self._max)
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
    def __init__(self, min, max):
        self._min = min
        self._max = max
        self._question = None
        self._answer = None
        self._a = None
        self._b = None

    def generate(self):
        self._a = random.randint(self._min, self._max)
        self._b = random.randint(self._min, self._max)
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


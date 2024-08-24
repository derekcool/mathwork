import myconfigs
from arithmetic_problems import *


def problem_loops(problem_generator):
    corrects = 0
    total = 0
    while True:
        total += 1
        problem_generator.generate()
        print("problem {}".format(total))
        print()
        print(problem_generator.description())
        print()
        answer = input("Enter the correct answer: ")
        is_correct = problem_generator.check_answer(answer)
        if is_correct:
            corrects += 1
            print()
            print("\tCorrect!")
        else:
            print()
            print("\tIncorrect.")
        print()
        cmd = input("Enter for the next question. q to quit: ")
        if cmd == 'q':
            break
        print()
    print("Summary: total corrects = {}/{} ({:.1f}%)".format(corrects, total, corrects * 100 / total))
    print()
    input("Press 'Enter' to continue.")


def main_loop():
    while True:
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("q: exit")
        print()
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            min1 = myconfigs.configs["add1min"]
            max1 = myconfigs.configs["add1max"]
            min2 = myconfigs.configs["add2min"]
            max2 = myconfigs.configs["add2max"]
            problem_loops(AddProblem(min1, max1, min2, max2))
        elif prog == '2':
            min1 = myconfigs.configs["sub1min"]
            max1 = myconfigs.configs["sub1max"]
            min2 = myconfigs.configs["sub2min"]
            max2 = myconfigs.configs["sub2max"]
            problem_loops(SubProblem(min1, max1, min2, max2))
        elif prog == '3':
            min1 = myconfigs.configs["mul1min"]
            max1 = myconfigs.configs["mul1max"]
            min2 = myconfigs.configs["mul2min"]
            max2 = myconfigs.configs["mul2max"]
            problem_loops(MulProblem(min1, max1, min2, max2))
        elif prog == '4':
            min1 = myconfigs.configs["div1min"]
            max1 = myconfigs.configs["div1max"]
            min2 = myconfigs.configs["div2min"]
            max2 = myconfigs.configs["div2max"]
            problem_loops(DivProblem(min1, max1, min2, max2))
        print()


if __name__ == '__main__':
    myconfigs.load_configs("configs.ini")
    myconfigs.load_configs("myconfigs.ini")
    # for k, v in myconfigs.configs.items():
    #     print("\t{} = {}".format(k, v))
    main_loop()

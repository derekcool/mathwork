import myconfigs
from multiplication_problems import MulProblem
from addsub_problems import AddProblem, SubProblem


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
        print("q: exit")
        print()
        prog = input("select the program number: ")
        print()
        if prog == 'q':
            break
        if prog == '1':
            problem_loops(AddProblem(int(myconfigs.configs["add_min"]), int(myconfigs.configs["add_max"])))
        elif prog == '2':
            problem_loops(SubProblem(int(myconfigs.configs["sub_min"]), int(myconfigs.configs["sub_max"])))
        elif prog == '3':
            problem_loops(MulProblem(int(myconfigs.configs["mul_min"]), int(myconfigs.configs["mul_max"])))
        print()


if __name__ == '__main__':
    myconfigs.load_configs("configs.ini")
    myconfigs.load_configs("myconfigs.ini")
    for k, v in myconfigs.configs.items():
        print("\t{} = {}".format(k, v))
    main_loop()

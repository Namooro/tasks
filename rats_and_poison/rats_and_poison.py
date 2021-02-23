import doctest
import math
from random import randint


class RatsAndPoison:
    """
    This class describes a solution for the rats and poison problem.
    The default amount of numbers of rats is 3, and the number of bottles where only one is poisoned is 8.
    The assumption is that the task requires only one day and for n bottles the log2(n) amount of rats needed.
    """

    def __init__(self, flasks_number: int = 8, rats_amount: int = 3, flask_number: int = -1):
        self.flasks_number = flasks_number
        self.rats_amount = rats_amount
        self.__min_days_check()

        self.flasks = list(0 for _ in range(self.flasks_number))
        if flask_number == -1:
            self.flasks[randint(0, 7)] = 1
        elif flask_number >= 0 & flask_number <= 7:
            self.flasks[flask_number] = 1
        else:
            raise NotImplementedError("Only one of 8 flasks can be poisoned")

    def print_flasks(self) -> None:
        print(f"flasks with poison: {self.flasks}")

    def __min_days_check(self) -> None:
        if math.ceil(math.log2(self.flasks_number)) == self.rats_amount:
            print("The task can be solved in just one day")
        else:
            print("The task takes more than one day to solve or it cannot be solved at all with this amount of rats")
            raise NotImplementedError("Current solution works only with 8 flasks and 3 rats")

    @staticmethod
    def poison_rats(flasks: list) -> None:
        """
        Converting the flask list to integer format via binary representation, and
        then by using bit shift operation, checking which one rats will die from poison in the flask.
         >>> RatsAndPoison.poison_rats(flasks = [0, 0, 0, 0, 0, 1, 0])
         Rat number 1 is dead
         >>> RatsAndPoison.poison_rats(flasks = [0, 0, 0, 0, 0, 0, 1])
         All rats are still alive
         >>> RatsAndPoison.poison_rats(flasks = [0, 1, 0, 0, 0, 0, 0])
         Rat number 1 is dead
         Rat number 3 is dead
        """
        binary_answer = math.ceil(math.log2(sum(2 ** i for i, v in enumerate(reversed(flasks)) if v)))
        rat_counter = 0
        while binary_answer > 0:
            rat_counter += 1
            if binary_answer % 2 == 1:
                print(f"Rat number {rat_counter} is dead")
            binary_answer = binary_answer >> 1
        if rat_counter == 0:
            print("All rats are still alive")


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    test = RatsAndPoison()
    test.print_flasks()
    RatsAndPoison.poison_rats(test.flasks)

import sys
from abc import ABC, abstractmethod

# Ready to start

# Reminder Tribonacci serie

# trib(0) = 0
# trib(1) = 0
# trib(2) = 1

# trib(n) = trib(n-3) + trib(n-2) + trib(n-1) for n > 2

# n      : 0, 1, 2, 3, 4, 5, 6, 07, 08, 09, 10, 011, 012
# trib(n): 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274


class InputReader(ABC):
    """
    The abstract class of a number input reader which could be
    inherited by other classes.
    """

    @abstractmethod
    def get_input(self) -> int:
        """
        Method which reads some kind of input.
        This method should returns an integer
        """
        pass


class StdInputReader(InputReader):
    """
    This class inherits InputReader.
    and makes reading an integer from the standard input.

    This class should have one method:
    - To read input from the keyboard, convert it to integer and return it
    """

    def get_input(self) -> int:
        """This function show a message to invite use to type an integer to the keyboard
        convert it to the integer format and return it.

        Return
        ------
        keyboard_int_input (integer): number typed by the user.
        """

        msg = "Please type the integer you want to compute its tribonacci:\n>>>"  # message to help user to know what they should type
        keyboard_int_input = int(input(msg))

        return keyboard_int_input


class TextFileInputReader(InputReader):
    """
    This class inherits InputReader
    and makes reading an integer from a text file.

    This class should have one attributes:
    - file_location (String): The location of the input file.

    This class should have one method:
    - To read input from the given file location, convert it to integer and return it

    """

    def __init__(self, file_location: str) -> None:
        super().__init__()
        self.file_location = file_location

    def get_input(self) -> int:
        """This function read an integer from a file and return it.

        Return
        ------
        read_int (integer): number read from the file.
        """

        with open(self.file_location, "r") as f:
            read_int = int(f.readline())

        return read_int


class Calculator:
    """
    One method named: tribonacci
    - one parameter: n
    - one returned value: tribonacci of n using the recursive process
    """

    def tribonacci(self, n: int) -> int:
        """function that generates the Tribonacci serie of n using the recursive process

        Parameter
        ---------
        n (integer): value to compute the Tribonacci serie on.

        Return
        ------
        tribo (integer): tribonacci of n using the recursive process.
        """

        tribo_dict = {
            0: 0,
            1: 0,
            2: 1,
        }  # dictionary to store the start of the tribonacci serie

        # put your code here

        return tribo


class CalculatorBis:
    """
    One method named: tribonacci
    - one parameter: n
    - one returned value: tribonacci of n using the iterative process
    """

    def tribonacci(self, n: int) -> int:
        """function that generates the Tribonacci serie of n iteratively

        Parameter
        ---------
        n (integer): value to compute the Tribonacci serie on.

        Return
        ------
        tribo_value (integer): tribonacci of n using the iterative process.
        """

        tribo_dict = {
            0: 0,
            1: 0,
            2: 1,
        }  # dictionary to store the tribonacci values computed until the searched value

        # put your code here

        return tribo_dict[n]


class CalculatorApp:
    """
    2 attributes:
    - a reader of type StdInputReader, or TextFileInputReader
    - a calculator of type CalculatorIterative or CalculatorRecursive


    1 method named calculate:
    - to calculate the tribonacci of the number returned by the self.reader attribute
    - using the self.calculator attribute

    - That method should return an integer
    """

    def __init__(self, reader, calculator) -> None:
        self.reader = reader
        self.calculator = calculator

    def calculate(
        self,
    ) -> int:
        """function that calculates the tribonacci of the number returned by the self.reader attribute

        Return
        ------
        tribo (integer): tribonacci value of the value read by the self.reader attribute.
        """

        # put your code here

        return tribo


def main():
    # put your code here
    pass


if __name__ == "__main__":
    # put your code here
    pass

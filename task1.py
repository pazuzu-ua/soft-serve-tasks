"""SoftServe Algorithmic Tasks

author: Dmytro Tymoshchenko

108. Дано натуральное число n. Получить наименьшее число
     вида 2**r , превосходящее n.

331. Дано натуральное число n. Можно ли представить его в
     виде суммы трех квадратов натуральных чисел? Если можно, то
а) указать тройку x, y, z таких натуральных чисел,
б) указать все тройки x, y, z таких натуральных чисел,

"""
from math import sqrt, ceil


def task_108(num: int) -> int:
    """Returns a power of two that is bigger than a *num*"""
    validate_input(num)
    power_of_two = 1
    while True:
        if 2**power_of_two > num:
            return power_of_two
        power_of_two += 1


def task_331a(num: int) -> list[tuple]:
    """Returns a represantation of a *num* as a sum of
        three squared numbers, if possible. Or returns
        an empty list.
    """
    validate_input(num)
    return form_square_sums(num, break_at_one=True)


def task_331b(num: int) -> list[tuple]:
    """Returns all represantations of a *num* as a sum of
        three squared numbers, if possible. Or returns
        an empty list.
    """
    validate_input(num)
    return form_square_sums(num)


# Helper functions
def form_square_sums(num: int, break_at_one: bool = False) -> list[tuple]:
    """ Forms all represantations of a *num* as a sum of
         three squared numbers and returns a list of them.
         List is empty if it is not possible.
         If *break_at_one* is True, it will only compute
         one possible answer.
    """
    square_root_of_num = ceil(sqrt(num))
    result = []
    for x in range(1, square_root_of_num):
        for y in range(1, square_root_of_num):
            for z in range(1, square_root_of_num):
                if square_sum_equals(x, y, z, num):
                    result.append((x, y, z))
                    if break_at_one:
                        return result
    return result


def square_sum_equals(x: int, y: int, z: int, num: int) -> bool:
    """Returns True if x^2 + y^2 + z^2 == num"""
    return x ** 2 + y ** 2 + z ** 2 == num


def validate_input(num: int) -> None:
    """Raises AssertionError if *num* < 1 or is not an integer"""
    assert isinstance(num, int), "Input needs to be a number"
    assert num > 1, "Input needs to be more than 1"


if __name__ == "__main__":

    # Check 108
    print(f"For number 12, the answer is 2^{task_108(12)}")
    print(f"For number 12, the answer is 2^{task_108(16)}")

    #Check 331 - a
    print(f"Possible representaion of 5000 is: {task_331a(5000)}")
    print(f"Possible representaion of 40 is: {task_331a(40)}")

    #Check 331 - b
    print(f"Possible representaion of 5000 is: {task_331b(5000)}")
    print(f"Possible representaion of 40 is: {task_331b(40)}")

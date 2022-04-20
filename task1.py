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


def task_108(num: int) -> None:
    """Prints a number that suffices 2**r and is bigger than *num*,
        if *num* > 1."""
    if num < 1:
        print("Please, enter integer number that is greater than 1")
    else:
        k = 1
        while True:
            if 2**k > num:
                print(f"Answer is 2^{k}, which equals to {2**k}")
                break
            k += 1


def task_331a(num: int) -> None:
    """Prints a represantation of a *num* as a sum of
        three squared numbers, if possible. 
    """
    if num < 1:
        print("Please, enter integer number that is greater than 1")
    else:
        list_of_sums = form_square_sums(num, True)
        if list_of_sums:
            print(f"It is possible: {list_of_sums[0]}")
        else:
            print("It is impossible...")


def task_331b(num: int) -> None:
    """Prints all represantations of a *num* as a sum of
        three squared numbers, if possible. 
    """
    if num < 1:
        print("Please, enter integer number that is greater than 1")
    else:
        list_of_sums = form_square_sums(num)
        if list_of_sums:
            print("Answer: ")
            for el in list_of_sums:
                print(*el)
        else:
            print("It is impossible...")


# Helper functions
def form_square_sums(num: int, break_at_one: bool = False) -> list[tuple]:
    """ Forms all represantations of a *num* as a sum of
         three squared numbers, if possible. Returns list
         of them, list can be empty.
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
                        break
    return result


def square_sum_equals(x: int, y: int, z: int, num: int) -> bool:
    """Returns True if x^2 + y^2 + z^2 == num"""
    return x ** 2 + y ** 2 + z ** 2 == num


if __name__ == "__main__":
    print("*" * 30)
    task_108("fdfdf")
    task_108(12)
    task_108(16)

    print("*" * 30)
    task_331a(12)
    task_331a(-9)
    task_331a(5000)

    print("*" * 30)
    task_331b(12)
    task_331b(-9)
    task_331b(5000)

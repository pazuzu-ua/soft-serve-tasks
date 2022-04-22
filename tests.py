"""SoftServe Algorithmic Tasks

Tests for Yaroslav's code

author: Dmytro Tymoshchenko

"""
import unittest
from tasks import count_multiples_of_three_not_five, count_square_multiples_two, pythagorean_triples


class TestTask178b(unittest.TestCase):

    def test_task178b_valid(self):
        entry_sequence = (711, 3, 5, 1, 15, 10, 8, 9, 0)
        expected_answer = 3
        answer = count_multiples_of_three_not_five(entry_sequence)
        self.assertEqual(expected_answer, answer)
 

    def test_task178b_valid_empty(self):
        entry_sequence = []
        expected_answer = 0
        answer = count_multiples_of_three_not_five(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178b_valid_str(self):
        entry_sequence = "(1, 2, 3, 4, 5, 6)"
        with self.assertRaises(TypeError):
            count_multiples_of_three_not_five(entry_sequence)


class TestTask178v(unittest.TestCase):

    def test_task178v_valid(self):
        entry_sequence = (16, 9, 1, 14, 7, 22, 25, 121, 1, 0, 100)
        expected_answer = 3
        answer = count_square_multiples_two(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178v_negative(self):
        entry_sequence = (16, 9, -1, 14, 7, 22, 25, -121, 1, 0, 100)
        with self.assertRaises(ValueError):
            count_square_multiples_two(entry_sequence)


    def test_task178v_valid_empty(self):
        entry_sequence = []
        expected_answer = 0
        answer = count_square_multiples_two(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178v_valid_str(self):
        entry_sequence = "(1, 2, 3, 4, 5, 6)"
        with self.assertRaises(TypeError):
            count_square_multiples_two(entry_sequence)


class TestTask554(unittest.TestCase):

    def test_task554_valid(self):
        entry_sequence = 10
        expected_answer = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
        answer = pythagorean_triples(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task554_valid_zero(self):
        entry_sequence = 0
        expected_answer = []
        answer = pythagorean_triples(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task554_valid_negative(self):
        entry_sequence = -8
        expected_answer = []
        answer = pythagorean_triples(entry_sequence)
        self.assertEqual(expected_answer, answer)

    def test_task178v_valid_str(self):
        entry_sequence = ""
        with self.assertRaises(TypeError):
            pythagorean_triples(entry_sequence)

    def test_task178v_valid_str(self):
        entry_sequence = []
        with self.assertRaises(TypeError):
            pythagorean_triples(entry_sequence)


if __name__ == '__main__':
    unittest.main()

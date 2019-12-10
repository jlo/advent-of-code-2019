import unittest
import functools
import math

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

def calc_total_fuel(masses):
    return functools.reduce(lambda result, mass : result + calc_fuel(mass), masses, 0)

class day1Tests(unittest.TestCase):
    def test_fuel_formula_based_on_mass(self):
        self.assertEqual(calc_fuel(12), 2)
        self.assertEqual(calc_fuel(14), 2)
        self.assertEqual(calc_fuel(1969), 654)
        self.assertEqual(calc_fuel(100756), 33583)

    def test_fuel_formula_with_list_of_masses(self):
        self.assertEqual(calc_total_fuel([12]), 2)

    def test_fuel_formula_with_input(self):
        with open('day1.txt') as f: 
            masses = [int(x) for x in f.readlines()]

        print("==BEGIN LIST==")
        print(masses)
        print("==END LIST==")

        self.assertEqual(calc_total_fuel(masses), 2)

if __name__ == '__main__':
    unittest.main()
from brave_function import get_name

print("\t Enter 'q' to quit program!")
while True:
    first_name = input("Please enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Please enter your last name: ")
    if last_name == 'q':
        break

    formatted_name = get_name(first_name, last_name)
    print(f"\t\nNeatly formatted name {formatted_name}")
    
from brave_function import get_name
import unittest
class NameTestCase(unittest.TestCase):

    def test_fullname(self):
        formatted_name = get_name('kwabena', 'agyapong')
        self.assertEqual(formatted_name, 'kwabena agyapong')

if __name__ == '__main__':
    unittest.main()

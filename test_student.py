import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_constructor(self):
        my_student = Student("1,강호민,85,90,95")
        self.assertIsNotNone(my_student)


if __name__ == "__main__":
    unittest.main()
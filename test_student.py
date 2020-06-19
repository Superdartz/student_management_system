import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_constructor(self):
        my_student = Student("1,강호민,85,90,95")
        self.assertIsNotNone(my_student)

    def test_sid(self):
        my_student = Student("1,강호민,85,90,95")
        self.assertEqual("1", my_student.sid)

    def test_sid_2(self):
        my_student = Student("2,김광호,80,70,60")
        self.assertEqual("2", my_student.sid)

if __name__ == "__main__":
    unittest.main()
import unittest
from student_management_system import StudentManagementSystem

class Test(unittest.TestCase):


    def test_constructor(self):
        sms = StudentManagementSystem()
        self.assertIsNotNone(sms)


if __name__ == "__main__":
    unittest.main()
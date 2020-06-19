import unittest
from student_management_system import StudentManagementSystem

class Test(unittest.TestCase):


    def test_constructor(self):
        sms = StudentManagementSystem()
        self.assertIsNotNone(sms)

    def test_read(self):
        sms = StudentManagementSystem()
        self.assertEqual(20, sms.read('score.csv'))


if __name__ == "__main__":
    unittest.main()
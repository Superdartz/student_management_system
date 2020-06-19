import unittest
from student_management_system import StudentManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class Test(unittest.TestCase):


    def test_constructor(self):
        sms = StudentManagementSystem()
        self.assertIsNotNone(sms)

    def test_read(self):
        m_open = mock_open(read_data="1,강호민,85,90,95\n")
        
        with patch('student_management_system.open', m_open):
            sms = StudentManagementSystem()
            self.assertEqual(1, sms.read('score.csv'))

        m_open.assert_called_with('score.csv', 'rt', encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
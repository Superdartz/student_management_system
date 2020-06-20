import unittest
from student_management_system import StudentManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class Test(unittest.TestCase):

    def setUp(self):
        self.m_open1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.m_open2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n")

    def test_constructor(self):
        sms = StudentManagementSystem()
        self.assertIsNotNone(sms)

    def test_read(self):
        
        with patch('student_management_system.open', self.m_open1):
            sms = StudentManagementSystem()
            self.assertEqual(1, sms.read('score.csv'))

        self.m_open1.assert_called_with('score.csv', 'rt', encoding="utf-8")

    def test_read_2(self):
        
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            self.assertEqual(2, sms.read('score.csv'))

        self.m_open2.assert_called_with('score.csv', 'rt', encoding="utf-8")

    def test_sort_1(self):
        with patch('student_management_system.open', self.m_open1):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,1,강호민,85,90,95,270,90', result)

    def test_sort_2(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,1,강호민,85,90,95,270,90\n2,2,김광호,80,70,60,210,70', result)

    def test_sort_3(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="des")
            self.assertEqual('2,2,김광호,80,70,60,210,70\n1,1,강호민,85,90,95,270,90', result)

    def test_sort_4(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort("stotal","asc")
            self.assertEqual('2,2,김광호,80,70,60,210,70\n1,1,강호민,85,90,95,270,90', result)
    
    def test_sort_5(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort("stotal","des")
            self.assertEqual('1,1,강호민,85,90,95,270,90\n2,2,김광호,80,70,60,210,70', result)
         

if __name__ == "__main__":
    unittest.main()
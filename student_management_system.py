class StudentManagementSystem:
    def __init__(self):
        pass

    def read(self, student_data_file):
        with open(student_data_file, 'rt', encoding='utf-8') as fo:
            lines = fo.readlines()

        return len(lines)
from student import Student

def key_stotal(item):
    return item[1].stotal
class StudentManagementSystem:
    def __init__(self):
        self._students = {}

    def read(self, student_data_file):
        with open(student_data_file, 'rt', encoding='utf-8') as fo:
            data = fo.read()
            lines = data.strip().split('\n')

        num = 0
        for line in lines:
            num = num + 1
            self._students[num] = Student(line.strip())

        return len(self._students)

    def sort_by_reg(self, order="asc"):
        if order == "asc":
            sorted_students = sorted(self._students.items())
        elif order == "des":
            sorted_students = sorted(self._students.items(), reverse=True)

        result = ""
        for key, item in sorted_students:
            result = result + str(key) + ","
            result = result + item.sid + ","
            result = result + item.sname + ","
            result = result + str(int(item.skor)) + ","
            result = result + str(int(item.seng)) + ","
            result = result + str(int(item.smat)) + ","
            result = result + str(int(item.stotal)) + ","
            result = result + str(int(item.savg)) + "\n"
        return result.strip()

    def sort_by_stotal(self, order="asc"):
        sorted_students = sorted(self._students.items(), key=key_stotal)

        result = ""
        for key, item in sorted_students:
            result = result + str(key) + ","
            result = result + item.sid + ","
            result = result + item.sname + ","
            result = result + str(int(item.skor)) + ","
            result = result + str(int(item.seng)) + ","
            result = result + str(int(item.smat)) + ","
            result = result + str(int(item.stotal)) + ","
            result = result + str(int(item.savg)) + "\n"
        return result.strip()

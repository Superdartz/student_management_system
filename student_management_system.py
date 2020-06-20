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

    def _make_students_string(self, students):
        result = ""
        
        for key, item in students:
            result = result + "{등수:"
            result = result + str(key) + "등},{ID:"
            result = result + item.sid + "},{이름:"
            result = result + item.sname + "},{국어점수:"
            result = result + str(int(item.skor)) + "},{영어점수:"
            result = result + str(int(item.seng)) + "},{수학점수:"
            result = result + str(int(item.smat)) + "},{총점:"
            result = result + str(int(item.stotal)) + "},{평균:"
            result = result + str(int(item.savg)) + "}\n"
        return result.strip()

    def sort(self, order_key="register", order_way="asc"):
        if order_key == "register" and order_way == "asc":
            sorted_students = sorted(self._students.items())
        elif order_key == "register" and order_way == "des":
            sorted_students = sorted(self._students.items(), reverse=True)
        elif order_key == "stotal" and order_way == "asc":
            sorted_students = sorted(self._students.items(), key=key_stotal)
        elif order_key == "stotal" and order_way == "des":
            sorted_students = sorted(self._students.items(), key=key_stotal, reverse=True)

        result = self._make_students_string(sorted_students)
        return result

    def sort_by_reg(self, order="asc"):
        if order == "asc":
            sorted_students = sorted(self._students.items())
        elif order == "des":
            sorted_students = sorted(self._students.items(), reverse=True)

        result = self._make_students_string(sorted_students)
        return result

    def sort_by_stotal(self, order="asc"):
        if order == "asc":
            sorted_students = sorted(self._students.items(), key=key_stotal)
        elif order == "des":
            sorted_students = sorted(self._students.items(), key=key_stotal, reverse=True)

        result = self._make_students_string(sorted_students)
        return result

    def write(self, file_name, order_key="register", order_way="asc"):
        with open(file_name, 'wt', encoding="utf-8") as fo:
            result = self.sort(order_key, order_way)
            fo.write(result)
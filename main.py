from student_management_system import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.read('score.csv')
    print(sms.sort("stotal","asc"))
    sms.write('result.csv',"stotal","asc")
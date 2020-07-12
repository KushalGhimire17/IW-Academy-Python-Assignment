# console app for enrollment
# please add details first then search else it will show error

import csv
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
student_id = 0
course_id = 0
COURSE_FILE = 'course_info.csv'
STUDENT_FILE = 'student_info.csv'
PAYMENT_FILE = "payment_info.csv"
OVERALL_FILE = "student_payment.csv"


def write_to_csv(filename, data, file_mode="a"):
    with open(filename, file_mode) as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(data)


def read_from_csv(filename):
    courses = []
    with open(filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            courses.append(row)
    return courses


class Course:

    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

    @staticmethod
    def course_add():
        global course_id
        course_name = input("ENTER NAME OF COURSE:")
        course_id += 1
        write_to_csv(COURSE_FILE, [course_name, course_id])

    @staticmethod
    def show_all_course():
        print("%20s " % "COURSE", "%2s" % "|", "%20s" % "COURSE ID")
        courses = read_from_csv(COURSE_FILE)
        for course in courses:
            print("%20s " % course[0], "%2s" % "|", "%20s" % course[1])


class Payment:
    def __init__(self):
        self.debit = 0
        self.credit = 20000

    def make_payment(self):
        count = 0
        while True:
            amount = int(input("ENTER PAYMENT AMOUNT:"))
            if count == 3:
                print("Seemed your are not qualified..!")
                return False

            if amount < 10000:
                count += 1
                print("not enough even for 1 installment")
                continue
            else:
                self.debit = amount
                self.credit = self.credit - amount
                write_to_csv(PAYMENT_FILE, [self.debit, self.credit])
                print("AMOUNT DUED IS: ", self.credit)
                return True

    @staticmethod
    def payment_info(student_name):
        overall_info = read_from_csv(OVERALL_FILE)
        for row in overall_info:
            if row[0] == student_name:
                print("{:^10}|Dedit:{:^10}|CREDIT:{:^10}|".format(row[0], row[3], row[4]))

    @staticmethod
    def payment_release(student_name):
        overall_info = read_from_csv(OVERALL_FILE)
        for i, row in enumerate(overall_info):
            if row[0] == student_name:
                row[4] = 0
            if i == 0:
                write_to_csv(OVERALL_FILE, row, "w")
            else:
                write_to_csv(OVERALL_FILE, row)


class Student:
    def __init__(self, name, id, course):
        self.name = name
        self.id = id
        self.course_enrolled = course

    def show_student_info():
        name = input("ENTER STUDENT NAME:")
        overall_info = read_from_csv(OVERALL_FILE)
        for student in overall_info:
            if name == student[0]:
                print(
                    f"NAME:{student[0]},\nID:{student[1]}\nCOURSE:{student[2]}\nDEBIT:{student[3]}\nCREDIT:{student[4]}")
                break

    def show_all_student_info():
        print("%15s" % "NAME", "%2s" % "|", "%15s" % "ID", "%2s" % "|", "%15s" % "COURSE ENROLLED")
        overall_info = read_from_csv(STUDENT_FILE)
        for student in overall_info:
            print("%15s" % student[0], "%2s" % "|", "%15s" % student[1], "%2s" % "|", "%15s" % student[2])

    @staticmethod
    def student_add():
        global students
        global student_id
        name = input("ENTER NAME:")
        courses = input("ENTER COURSE TO BE ENROLLED:")
        student_id += 1
        payment = Payment()
        if payment.make_payment():
            write_to_csv(STUDENT_FILE, [name, student_id, courses])
            write_to_csv(OVERALL_FILE, [name, student_id, courses, payment.debit, payment.credit])

    def student_remove():
        student_name = input("ENTER THE STUDENT NAME YOU WANT TO REMOVE:")
        Payment.payment_release(student_name)
        students = read_from_csv(STUDENT_FILE)
        for i, student in enumerate(students):
            if student[0] == student_name:
                print(f"{student_name} removed..!")
                continue
            if i == 0:
                write_to_csv(STUDENT_FILE, student, "w")
            else:
                write_to_csv(STUDENT_FILE, student)
            logging.debug(f"{student}")

    @staticmethod
    def student_edit(self):
        pass


courses_methods = [Course.course_add, Course.show_all_course]
student_methods = [Student.show_student_info, Student.show_all_student_info, Student.student_add,
                   Student.student_remove, Student.student_edit]


def get_options():
    choice = input("1)COURSES\n2)STUDENT\nENTER YOUR INETESTED ACTION:")
    courses_options = ["ADD COURSE", "SHOW ALL COURSES"]
    student_options = ["STUDENT INFO", "ALL STUDENT INFO", "ADD STUDENT", "REMOVE STUDENT", "STUDENT EDIT"]
    if choice == "1":
        for i, option in enumerate(courses_options):
            print(f"({i})-{option}")
        choice1 = input("ENTER ACTION YOU WANT TO PERFORM:")
        return courses_methods[int(choice1)]()
    else:
        for i, option in enumerate(student_options):
            print(f"({i})-{option}")
        choice1 = input("ENTER ACTION YOU WANT TO PERFORM:")
        return student_methods[int(choice1)]()


if __name__ == "__main__":
    while True:
        get_options()


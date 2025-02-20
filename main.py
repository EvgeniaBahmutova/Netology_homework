
class Student:
    def __init__(self, name, surname, gender, course):
        self.average_grade = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.course = course

# Creating method to count average grade.
    def av_gr_st_count(self, grades):
        grades_values = grades.values()
        grades_list_1 = list(grades_values)
        quantity_grades = len(grades_list_1)
        sum_1 = 0
        for mark in grades_list_1:
            sum_1 += mark
        average_grade = round(sum_1 / quantity_grades, 1)

# Creating method to count overall average score
    def overall_score(self, student_list, course_name):
        overall_score = 0
        student_grade = 0
        for student in student_list:
            student.av_gr_st_count(self, self.grades)
            overall_score += student.average_grade
        if len(student_list) > 0:
            average_score = overall_score / len(student_list)
        else:
            average_score = 0
        return average_score

# Creating method to check object's possibility of rating lectures.
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.course == other.course
        else:
            return False

    def rate_lecture(self, title, lec_grade, lecturer, all_grades_lec):
        if all_grades_lec is None:
            all_grades_lec = {}
        if self == lecturer:
            if title in all_grades_lec:
                all_grades_lec[title].append(lec_grade)
            else:
                all_grades_lec[title] = [lec_grade]
            print(all_grades_lec)


    # Creating method __str__
    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}'
                f'Средняя оценка за домашние задания: {self.average_grade}'
                f'Курсы в процессе изучения: {self.courses_in_progress}'
                f'Завершенные курсы: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Creating method for class Reviewer. Method helps to rate students.
    def possibility_of_rating(self, student, course, grade):
        if isinstance(self, Lecturer):
            pass
        elif isinstance(self, Reviewer):
            self.rate_hw(student, course, grade)
        else:
            pass


class Lecturer(Mentor):
    def __init__(self, name, surname, course):
        super().__init__(name, surname)
        self.course = course
        self.average_grade = None

    # Creating method to print lecturer's grades for each lecture.
    def show(self, all_grades_lec):
        for title, grades in all_grades_lec.items():
            print(f"Lecture: {title}, Grades: {grades}")

# Creating method to count average grade.
    def count_av_gr(self, all_grades_lec):
        just_grades = all_grades_lec.values()
        grades_list = list(just_grades)
        quantity_grades = len(grades_list)
        sum = 0
        for mark in grades_list:
            sum += mark
        average_grade = round(sum / quantity_grades, 1)

    # Creating method __str__
    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}'
                f'Средняя оценка за лекции {self.average_grade}')
    # Creating method to count overall average mark
    def overall_lec_mark(self, lecturers_list, course_name):
        for lecturer in lecturers_list:
            overall_mark = 0
            overall_mark += lecturer.count_av_gr(self)
        return overall_mark


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# Creating method __str__.
    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}')

student_1 = Student("Alice", "Brown", "Female", "Python")
student_2 = Student("Bob", "Green", "Male", "Python")
lecturer_1 = Lecturer("Katrin", "Belova", "Python")
lecturer_2 = Lecturer("Valentin", "Serov", "C#")
reviewer_1 = Reviewer("Olga", "Belkina")
reviewer_2 = Reviewer("Igor", "Semyonov")


# student_1.rate_lecture("OOP", 9, lecturer_1, None)
# print(student_2.__str__())
# print(student_1.overall_score([student_2, student_1],"Python")) # Here there is an error I don't know how to fix()
# lecturer_2.show("OOP":"5, 5, 7, 9, 10") Here there is an error too, it is connected with syntax
# print(lecturer_1.__str__())
# print(lecturer_2.count_av_gr("OOP":"5,5,6")) # error
# print(lecturer_1.overall_lec_mark(["OOP", "OOP2", "OOP3"], "Python")) # AttributeError: 'str' object has no attribute 'count_av_gr'
# print(reviewer_1.__str__())






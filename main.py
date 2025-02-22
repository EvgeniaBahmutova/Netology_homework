
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
        self.average_grade = 0

# Creating method to count average grade.
    def av_gr_st_count(self):
        if not self.grades:
            self.average_grade = 0
            return
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        self.average_grade = round(total / count, 1) if count > 0 else 0

    # Creating method to count overall average score
    def overall_score(student_list, course_name):
        total = 0
        count = 0
        for student in student_list:
            if course_name in student.grades:
                total += sum(student.grades[course_name])
                count += len(student.grades[course_name])
        return round(total / count, 1) if count > 0 else 0


# Creating method to check object's possibility of rating lectures.
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade == other.average_grade
        return False


# Method to rate lectures
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course == lecturer.course:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    # Creating method __str__
    def __str__(self):
        self.av_gr_st_count()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        self.grades = {}
        self.average_grade = 0


# Creating method to count average grade.
    def count_av_gr(self):
        if not self.grades:
            self.average_grade = 0
            return
        total = 0
        count = 0
        for course_grades in self.grades.values():
            total += sum(course_grades)
            count += len(course_grades)
        self.average_grade = round(total / count, 1) if count > 0 else 0

    # Creating method __str__
    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}'
                f'Средняя оценка за лекции {self.average_grade}')
    # Creating method to count overall average mark
    def overall_lec_mark(lecturers_list):
        total = 0
        count = 0
        for lecturer in lecturers_list:
            lecturer.count_av_gr()  # Calculate the average grade for the lecturer
            total += lecturer.average_grade
            count += 1
        return round(total / count, 1) if count > 0 else 0


    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade == other.average_grade
        return False



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


#    Rating students' homeworks
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Creating method __str__.
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

# Creating instances
student_1 = Student("Alice", "Brown", "Female", "Python")
student_2 = Student("Bob", "Green", "Male", "Python")
lecturer_1 = Lecturer("Katrin", "Belova", "Python")
lecturer_2 = Lecturer("Valentin", "Serov", "C#")
reviewer_1 = Reviewer("Olga", "Belkina")
reviewer_2 = Reviewer("Igor", "Semyonov")

# Fixing courses
reviewer_1.courses_attached.append("Python")
reviewer_2.courses_attached.append("C#")

# Students' marks
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Python", 8)
reviewer_1.rate_hw(student_2, "Python", 7)

# Lecturers' mark for lectures
student_1.rate_lecture(lecturer_1, "Python", 10)
student_2.rate_lecture(lecturer_1, "Python", 9)

# Print information
print(student_1)
print(lecturer_1)
print(reviewer_1)

# Counting average marks
print(f"Средняя оценка студентов по курсу Python: {Student.overall_score([student_1, student_2], 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {Lecturer.overall_lec_mark([lecturer_1])}")






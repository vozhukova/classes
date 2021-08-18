def average_grade_course(course, students):
    average_rate = []
    average_rate_grade = 0
    for student in students:
        if course in student.grades.keys():
            for grade in student.grades[course]:
                average_rate.append(grade)
            average_rate_grade = sum(average_rate) / len(average_rate)
    return print(f'Средняя оценка за ДЗ по курсу {course} равна {round(average_rate_grade, 1)}')


def average_grade_lec(course, lecturers):
    average_rate_list = []
    average_rate_grade = 0
    for lecturer in lecturers:
        if course in lecturer.grades_lect.keys():
            for grade in lecturer.grades_lect[course]:
                average_rate_list.append(grade)
            average_rate_grade = sum(average_rate_list) / len(average_rate_list)
    return print(f'Средняя оценка за лекции по курсу {course} равна {round(average_rate_grade, 1)}')

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return str(f'{self.name} {self.surname}')

    def rate_lect(self, lecturer, course, grade_lect):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_lect:
                lecturer.grades_lect[course] += [grade_lect]
                print(f'Преподавателю {lecturer} по курсу {course} поставлена оценка {grade_lect}')
            else:
                lecturer.grades_lect[course] = [grade_lect]
                print(f'Преподавателю {lecturer} по курсу {course} поставлена оценка {grade_lect}')
        else:
            print(f'Ошибка! Курс {course} не ведет преподаватель {lecturer} или Вы не проходили курс {course}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}

    def __str__(self):
        return str(f'{self.name} {self.surname}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return str(f'{self.name} {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                print(f'Студенту {student} по курсу {course} поставлена оценка {grade}')
            else:
                student.grades[course] = [grade]
                print(f'Студенту {student} по курсу {course} поставлена оценка {grade}')
        else:
            print(f'Ошибка! Курс {course} не найден у студента {student}')

#создаем студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Python']
best_student.finished_courses += ['Java']
my_student = Student('Ivor', 'Joy', 'your_gender')
my_student.courses_in_progress += ['Java']
my_student.courses_in_progress += ['JS']
my_student.finished_courses += ['Java']
my_student.finished_courses += ['JS']

#создаем проверяющих
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
my_reviewer = Reviewer('Mary', 'Jane')
my_reviewer.courses_attached += ['JS']
my_reviewer.courses_attached += ['Data Science']

#выставляем оценки студентам
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(my_student, 'Java', 8)
my_reviewer.rate_hw(my_student, 'JS', 7)
my_reviewer.rate_hw(my_student, 'Data Science', 10)

#создаем лекторов
cool_lecturer = Lecturer('Anna', 'Mar')
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['JS']
my_lecturer = Lecturer('New', 'Colson')
my_lecturer.courses_attached += ['Python']
my_lecturer.courses_attached += ['Data Science']

#студенты выставляют оценки за лекции
best_student.rate_lect(cool_lecturer, 'Java', 9)
best_student.rate_lect(my_lecturer, 'Python', 10)
my_student.rate_lect(cool_lecturer, 'Java', 8)
my_student.rate_lect(cool_lecturer, 'JS', 9)
my_student.rate_lect(my_lecturer, 'Data Science', 7)
my_student.rate_lect(my_lecturer, 'JS', 7)

#смотрим средние оценки по ДЗ
print(best_student.grades)
print(my_student.grades)
average_grade_course('Python', [best_student, my_student])
average_grade_course('Java', [best_student, my_student])
average_grade_course('JS', [best_student, my_student])

#смотрим средние оценки по лекциям
print(cool_lecturer.grades_lect)
print(my_lecturer.grades_lect)
average_grade_lec('Java', [cool_lecturer, my_lecturer])
average_grade_lec('JS', [cool_lecturer, my_lecturer])
average_grade_lec('Python', [cool_lecturer, my_lecturer])


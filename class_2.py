def average_grade(student):
    average_rate = []
    average_rate_grade = 0
    for item in student.grades.values():
        for i in item:
            average_rate.append(i)
    average_rate_grade = sum(average_rate)/len(average_rate)
    return average_rate_grade

def average_grade_lec(lecturer):
    average_rate_list = []
    for item in lecturer.grades_lect.values():
        for i in item:
            average_rate_list.append(i)
    average_rate_lec = sum(average_rate_list) / len(average_rate_list)
    return average_rate_lec

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        n1 = '\n'
        std_avg = average_grade(self)
        return str(f'Имя: {self.name} {n1}Фамилия: {self.surname} {n1}Средняя оценка за домашние задания: {round(std_avg, 1)} '
                   f'{n1}Курсы в процессе изучения: {str(self.courses_in_progress)[1:-1]} '
                   f'{n1}Завершенные курсы: {str(self.finished_courses)[1:-1]}')

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Ошибка! Один и объектов не является студентом')
            return
        else:
            first = average_grade(self)
            second = average_grade(other)
            return first <= second

    def rate_lect(self, lecturer, course, grade_lect):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_lect:
                lecturer.grades_lect[course] += [grade_lect]
            else:
                lecturer.grades_lect[course] = [grade_lect]
        else:
            print(f'Ошибка!')

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
        n1 = '\n'
        lec_avg = average_grade_lec(self)
        return str(f'Имя: {self.name} {n1}Фамилия: {self.surname} {n1}Средняя оценка за лекции: {round(lec_avg, 1)}')

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка! Один и объектов не является лектором')
            return
        else:
            first = average_grade_lec(self)
            second = average_grade_lec(other)
            return first <= second

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        n1 = '\n'
        return str(f'Имя: {self.name} {n1}Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!')

#создаем студентов
my_student = Student('Ivor', 'Joy', 'your_gender')
my_student.courses_in_progress += ['Python']
my_student.courses_in_progress += ['Java']
my_student.finished_courses += ['Java']
my_student.finished_courses += ['JS']
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Data Science']

#создаем лекторов
cool_lecturer = Lecturer('Anna', 'Mar')
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['JS']
my_student.rate_lect(cool_lecturer, 'Java', 10)
my_student.rate_lect(cool_lecturer, 'Java', 8)
my_student.rate_lect(cool_lecturer, 'JS', 7)
new_lecturer = Lecturer('Sasha', 'Lobanov')
new_lecturer.courses_attached += ['Java']
new_lecturer.courses_attached += ['JS']
my_student.rate_lect(new_lecturer, 'Java', 8)
my_student.rate_lect(new_lecturer, 'Java', 8)
my_student.rate_lect(new_lecturer, 'JS', 7)

#создаем проверяющего
cool_reviewer = Reviewer('New', 'Colson')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 10)
cool_reviewer.rate_hw(my_student, 'Python', 8)
cool_reviewer.rate_hw(my_student, 'Python', 10)
cool_reviewer.rate_hw(my_student, 'Java', 10)

print(best_student)
print(my_student)
print(best_student <= my_student)

print(cool_reviewer)

print(cool_lecturer)
print(new_lecturer)
print(cool_lecturer <= new_lecturer)


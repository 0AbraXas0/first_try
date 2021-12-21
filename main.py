import course
import student
import assignment
import trainer
import validators



courses_list = []
students_list = []
trainers_list = []
assignments_list = []


def main():

    print("Welcome to Private school program.")

    # continuous menu of 13 choices until the user presses 0

    while True:
        print(" 1.Add a course.")
        print(" 2.Add a student.")
        print(" 3.Add a trainer.")
        print(" 4.Add a assignment.")
        print(" 5.Show all courses.")
        print(" 6.Show all students.")
        print(" 7.Show all trainers.")
        print(" 8.Show all assignments.")
        print(" 9.Show students per course.")
        print("10.Show trainers per course.")
        print("11.Show assignments per course.")
        print("12.Show assignments per student.")
        print("13.Show students with multiple courses.")
        print(" 0.Exit program.")
        button = str(input(validators.valid_button(0, 13)))
        if button == "1":
            add_course()
        elif button == "2":
            add_student()
        elif button == "3":
            add_trainer()
        elif button == "4":
            add_assignment()
        elif button == "5":
            for course in courses_list:
                print(course)
        elif button == "6":
            for student in students_list:
                print(student)
        elif button == "7":
            for trainer in trainers_list:
                print(trainer)
        elif button == "8":
            for assignment in assignments_list:
                print(assignment)
        elif button == "9":
            show_students_per_course()
        elif button == "10":
            show_trainers_per_course()
        elif button == "11":
            show_assignments_per_course()
        elif button == "12":
            show_assignments_per_student()
        elif button == "13":
            show_students_multi()
        elif button == "0":
            break


# function to add a course

def add_course():
    title = str(input("Please write the title of the course.\n"))
    stream = str(input("Please write the stream of the course.\n"))
    type_of = str(input("Please write the type of the course.\n"))
    start_date = validators.valid_date("Please write the starting date of the course (yyyy-mm-dd).\n")
    end_date = validators.valid_date("Please write the ending date of the course (yyyy-mm-dd).\n")
    new_course = course.Course(title, stream, type_of, start_date, end_date)
    courses_list.append(new_course)

# function to add a student

def add_student():
    print("Please choose a course to add a student")

# menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    first_name = str(input("Please write student's first name.\n"))
    last_name = str(input("Please write student's last name.\n"))
    date_of_birth = validators.valid_date("Please write student's birthday (yyyy-mm-dd).\n")
    tuition_fees = str(input("Please write student's tuition fees.\n"))
    new_student = student.Student(first_name, last_name, date_of_birth, tuition_fees)

# adding new student to all and per course list

    students_list.append(new_student)
    courses_list[course_number-1].student_attend(new_student)
    new_student.attend_course(courses_list[course_number-1])


# function to add a trainer

def add_trainer():
    print("Please choose a course to add a trainer")

# menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    first_name = str(input("Please write trainer's first name.\n"))
    last_name = str(input("Please write trainer's last name.\n"))
    subject = str("Please write trainer's subject.\n")
    new_trainer = trainer.Trainer(first_name, last_name, subject)

# add trainer to all and per course list

    trainers_list.append(new_trainer)
    courses_list[course_number-1].trainer_teach(new_trainer)


# function to add an assignment

def add_assignment():
    print("Please choose a course to add a trainer")

# menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    title = str(input("Please write assignment's title.\n"))
    description = str(input("Please write assignment's description.\n"))
    sub_date_time = validators.valid_date("Please assignment's submission date (yyyy-mm-dd).\n")
    oral_mark = str(input("Please give oral mark"))
    total_mark = str(input("Please give total mark"))
    new_assignment = assignment.Assignment(title, description, sub_date_time, oral_mark, total_mark)

# add assignment to all and per course list

    assignments_list.append(new_assignment)
    courses_list[course_number-1].assignment_assign(new_assignment)


# function to print students per course

def show_students_per_course():
    # menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    print(f"Students of {courses_list[course_number-1]} are:")
    courses_list[course_number-1].show_students()


# function to print trainers per course

def show_trainers_per_course():
    # menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    print(f"Trainers of {courses_list[course_number-1]} are:")
    courses_list[course_number-1].show_trainers()


# function to print assignments per course

def show_assignments_per_course():
    # menu to choose a course from current list of courses

    button_icon = 0
    print("Please choose a course")
    for course in courses_list:
        button_icon += 1
        print(f"{button_icon}.{course}\n")
    course_number = int(input(validators.valid_button(1, len(courses_list))))
    print(f"Assignments of {courses_list[course_number-1]} are:")
    courses_list[course_number-1].show_assignments()


# function to print assignments per student

def show_assignments_per_student():
    # menu to choose a student from current list of students

    button_icon = 0
    print("Please choose a student")
    for student in students_list:
        button_icon += 1
        print(f"{button_icon}.{student}\n")
    student_number = int(input(validators.valid_button(1, len(students_list))))
    print(f"Assignments of {students_list[student_number-1]} are:")
    students_list[student_number-1].show_assignments()


# function to print students with multiple assignments

def show_students_multi():
    for student in students_list:
        if len(student.list_of_courses) > 1:
            print(student)


# fake data

c1 = course.Course("PYTHON", "10", "remote", "2021-05-23", "2021-11-18")  # 3 students 2 assignments 2 trainers
c2 = course.Course("JAVA", "12", "on site", "2022-06-3", "2021-12-10")
c3 = course.Course("JAVASCRIPT", "6", "remote", "2022-08-23", "2022-02-8")
courses_list.append(c1)
courses_list.append(c2)
courses_list.append(c3)
s1 = student.Student("Thomas", "Georgiadis", "1990-06-06", "2500")
students_list.append(s1)
c1.student_attend(s1)
s1.attend_course(c1)
s2 = student.Student("George", "Grigoriadis", "1995-11-02", "2500")
students_list.append(s2)
c1.student_attend(s2)
s2.attend_course(c1)
s3 = student.Student("Charalampos", "Argyriadis", "2000-08-09", "2500")  # 2 courses 3 assignments
students_list.append(s3)
c1.student_attend(s3)
s3.attend_course(c1)
c3.student_attend(s3)
s3.attend_course(c3)
s4 = student.Student("Kostas", "Lolos", "2003-12-09", "2500")  # 2 courses
students_list.append(s4)
c2.student_attend(s4)
s4.attend_course(c2)
as1 = assignment.Assignment("Assignment 1", "Create ....etc", "2021-06-25", "20", "80")
assignments_list.append(as1)
c1.assignment_assign(as1)
as2 = assignment.Assignment("Assignment 2", "Create ....etc", "2022-07-25", "20", "80")
assignments_list.append(as2)
c2.assignment_assign(as2)
as3 = assignment.Assignment("Assignment 3", "Create ....etc", "2022-12-25", "20", "80")
assignments_list.append(as3)
c3.assignment_assign(as3)
as4 = assignment.Assignment("Assignment 1-2", "Create ....etc", "2021-08-25", "20", "80")
assignments_list.append(as4)
c1.assignment_assign(as4)
tr1 = trainer.Trainer("Kostas", "Damaskos", "python")
trainers_list.append(tr1)
c1.trainer_teach(tr1)
tr2 = trainer.Trainer("Maria", "Xariskou", "SQL")
trainers_list.append(tr2)
c1.trainer_teach(tr2)
tr3 = trainer.Trainer("Zoi", "Iliadou", "Java")
trainers_list.append(tr3)
c2.trainer_teach(tr3)
tr4 = trainer.Trainer("Katerina", "Papadopoulou", "Javascript")
trainers_list.append(tr4)
c3.trainer_teach(tr4)


if __name__ == '__main__':
    main()

import student



class Course:
    def __init__(self, title, stream, type_of, start_date, end_date):
        student_list = []
        trainer_list = []
        assignment_list = []
        self.title = title
        self.stream = stream
        self.type_of = type_of
        self.start_date = start_date
        self.end_date = end_date
        self.student_list = student_list
        self.trainer_list = trainer_list
        self.assignment_list = assignment_list

    def __str__(self):
        return f"Title: {self.title} Stream: {self.stream} Type: {self.type_of} Start:{self.start_date} End: {self.end_date}"

# function to add a student to course's student list

    def student_attend(self, student):
        self.student_list.append(student)

# function to add a trainer to course's trainer list

    def trainer_teach(self, trainer):
        self.trainer_list.append(trainer)

# function to add a assignment to course's assignment list

    def assignment_assign(self, assignment):
        self.assignment_list.append(assignment)

# function to print out all students of the course

    def show_students(self):
        for student in self.student_list:
            print(student)

# function to print out all trainers of the course

    def show_trainers(self):
        for trainer in self.trainer_list:
            print(trainer)

# function to print out all assignments of the course

    def show_assignments(self):
        for assignment in self.assignment_list:
            print(assignment)


# test area


if __name__ == "__main__":
    course1 = Course("Python", "stream1", "remote", "17-3-2021", "23-6-2021")
    student1 = student.Student("Thomas", "Georgiadis", "6-6-90", 1000)
    student2 = student.Student("Thomas", "Georgiadis", "6-6-90", 1000)
    course1.student_attend(student1)
    course1.student_attend(student1)
    print(course1)
    course1.show_students()
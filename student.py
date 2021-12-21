import course



class Student:
    def __init__(self, first_name, last_name, date_of_birth, tuition_fees):
        courses_attend = []
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.tuition_fees = tuition_fees
        self.list_of_courses = courses_attend

    def __str__(self):
        return f"First: {self.first_name} Last: {self.last_name} Birthday: {self.date_of_birth} Fees: {self.tuition_fees}"

# function to add a course that the student attends to a list inside the object

    def attend_course(self, course):
        self.list_of_courses.append(course)

# function to return all courses that the student attends

    def show_courses(self):
        for course in self.list_of_courses:
            print(course)

# function to return all assignments that the student has

    def show_assignments(self):
        for course in self.list_of_courses:
            for assignment in course.assignment_list:
                print(assignment)


# test area


if __name__ == "__main__":
    student1 = Student("Thomas", "Georgiadis", "6-6-90", 1000)
    course1 = course.Course("python", "stream 1", "remote", "17-3-2021", "23-6-2021")
    course2 = course.Course("python", "stream 1", "remote", "17-3-2021", "23-6-2021")
    student1.attend_courses(course1)
    student1.attend_courses(course2)
    print(student1)
    student1.show_courses()



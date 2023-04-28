class CoreCourse:
    def _init_(self, course_code, course_name):
      self.course_code = course_code
      self.course_name = course_name


class Semester(CoreCourse):
     def _init_(self, semester_number, course_code, course_name):
       super()._init_(course_code, course_name)
       self.semester_number = semester_number


class Course(Semester):
     def _init_(self, course_code, course_name, semester_number, credits):
        super()._init_(semester_number, course_code, course_name)
        self.credits = credits


     def create_course():
course_code = input("Enter the course code: ")
course_name = input("Enter the course name: ")
semester_number = input("Enter the semester number: ")
credits = input("Enter the credits for the course: ")

course = Course(course_code, course_name, semester_number, credits)

return course

def main():
 course_list = []

num_of_courses = int(input("Enter the number of courses to be added: "))

for i in range(num_of_courses):
 course = create_course()
 course_list.append(course)

for course in course_list:
  print(course.semester_number, course.course_code, course.course_name, course.credits)


if _name_ == "_main_":
 main()
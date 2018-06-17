#Notes
#class MyClass(object):
    #a = 5
    #b = 2
    #c = "Hello"

#new_item = MyClass() <-way to call new instance of MyClass
#new_item.a = 5
#new_item.a = 10
#new_item.a -> 10

#Adding Methods to Classes
# class MyClass(object):
# 	a = 5
# 	b = 7
# 	def print_a(self):
# 		print "Hello! Here is a: {}".format(self.a)

# my_object = MyClass()
# my_object.print_a() -> Hello! Here is a: 5

#Example 2
# class School(object):
# 	name = ''
# 	address = ''
# 	type = 'grade school'
# 	def print_school(self):
# 		print self.name
# 		print self.address
# 		print "Type: " + self.type
#
#
# school1 = School()
# school2 = School2()
#
#
#school2 = School()
# school1.name = "Wyland Elementary"
# school1.address = "100 Peachtree Ave\nAtlanta GA"
# school2.name = "George Mason University"
# school2.address = "300 University Way\nFairfax VA"
# school2.type = "university"

# school1.print_school()
# Wyland Elementary
# 100 Peachtree Ave
# Atlanta GA
# Type: grade school

#school2.print_school()
# George Mason University
# 300 University Way
# Fairfax VA
# Type: university

#Setting Up Class Instances
#The __init__() Function:
# class Student(object):
# 	def __init__(self):
# 		self.name = "None"
# 		self.grade = "K"
# 		self.district = "Orange County"
#
#
# student1 = Student()
# student1.name -> 'None'
#
#Rewriting to pass values to student
#class Student(object):
# 	def __init__(self, name = "None", grade = "K", district = "Orange County"):
# 		self.name = name
# 		self.grade = grade
# 		self.district = district
#
# student1 = Student()
# student2 = Student(name = "Byron Blaze", grade = "12", district = " Fairfax County")
#student1.name -> 'none'
#student2.name -> 'Byron Blaze'

# class Student(object):
#
#     def __init__(self, name="", school="", grade=""):
#         if not name:
#             name = raw_input("What is the student's name? ")
#         if not school:
#             school = raw_input("What is the student's school? ")
#         if not grade:
#             grade = self.get_grade()
#         self.name = name
#         self.school = school
#         self.grade = get_grade
#         self.print_student()
#
#     def get_grade(self):
#         while True:
#             grade = raw_input("What is the sudent's grade? [K, 1-5] ")
#             if grade.lower() not in ['k','1','2','3','4','5']:
#                 print "I'm sorry, but {} isn't valid.".format(grade)
#             else:
#                 return grade
#
#     def print_student(self):
#         print "Name: {}".format(self.name)
#         print "School: {}".format(self.school)
#         print "Grade: {}".format(self.grade)
#
#     def main():
#         student1 = Student()
#         student2 = Student(name="Byron Blaze", grade="2", school="Minnieville")
#
#     if __name__ == "__main__":
#          main()

class Student(object):
    def __init__(self, name="", school="", grade=""):
        if not name:
            name =raw_input("What is the student's name? ")
        if not school:
            school = raw_input("What is the student's school? ")
        if not grade:
            grade = self.get_grade()
            self.name = name
            self.school = school
            self.grade = grade

    def get_grade(self):
        while True:
            grade = raw_input("What is the student's grade? [K, 1-5] ")
            if grade.lower() not in ['k','1','2','3','4','5']:
                print "I'm sorry, but {} isn't valid.".format(grade)
            else:
                return grade

    def print_student(self):
        print "Name: {}".format(self.name)
        print "School: {}".format(self.school)
        print "Grade: {}".format(self.grade)

    def print_roster(students):
        print "Students in the system:"
        for student in students:
            print "*"*15
            student.print_student()

    def main():
        student1 = Student(name="Carrie Kale", grade="3", school="Marshall")
        student2 = Student(name="Byron Bale", grade="2", school="Minnieville")
        student3 = Student(name="Sarah Chandler", grade="K", school="Woodbridge")
        students = [student1, student2, student3]
        print_roster(students)

    if __name__ == "__main__":
        main()

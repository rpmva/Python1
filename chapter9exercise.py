name = ""
grade = ""
grades = {}

def gradebook(name, grade):
    grades[name] = grade

def out(grades):
    for name, grade in grades.items():
        print "{} {}".format(name, grade)

while not name == 'q':
    name = raw_input("Please give me the name of the student (q to quit): ")
    if name == 'q':
        print "Okay, printing grades!"
        print "Student\tGrade"
        out(grades)
        break

    grade = raw_input("Please give me their grade: ")

    gradebook(name, grade)

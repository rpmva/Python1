print "Welcome to the student checker!"
attendance = ['Ryan McGovern', 'Patrick Kane', 'TJ Meder']
name = ""

def check_student(name):
    if name in attendance:
        print "Yes, that student is enrolled in the class!"
        return True
    else:
        print "No, that student is not in the class."
        return False

while name != 'q':
    name = raw_input("Please give me the name of a student (enter 'q' to quit): ")
    if name == "q":
        print "Goodbye!"
        break

    check_student(name)

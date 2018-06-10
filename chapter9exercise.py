gradebook = {}
StuName = raw_input("Please give me the name of the student (q to quit): ")
grade = raw_input("Please give me their grade: ")

def FinalGrade(StuName, grade):
    gradebook[StuName]= grade;

FinalGrade(StuName, grade)

while StuName != 'q':
    if StuName == 'q':
        print gradebook
        break

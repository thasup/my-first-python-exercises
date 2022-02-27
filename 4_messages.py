name = input("Enter your student name (separate by commas) : ").title().split(",")
num_ass = input("Enter your student assignments (separate by commas) : ").split(",")
grade = input("Enter your student grades (separate by commas) : ").split(",")

message = "Hi {}. \nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for name, num_ass, grade in zip(name, num_ass, grade):
    print(message.format(name, num_ass, grade, int(grade) + int(num_ass)*2))
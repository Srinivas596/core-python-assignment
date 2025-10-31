# Classroom Performance Tracker

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def get_student_averages(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(calculate_average(marks), 2)
    return averages

def find_top_performer(averages):
    return max(averages, key=averages.get)


if __name__ == "__main__":
    students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    averages = get_student_averages(students)
    top_student = find_top_performer(averages)

    print("Average Marks:", averages)
    print("Top Performer:", top_student)

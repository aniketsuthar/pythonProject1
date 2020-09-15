def mean(value):
    if type(value) == dict:
        avg = sum(value.values()) / len(value)
    else:
        avg = sum(value) / len(value)
    print(avg)
    return avg


student_grades = {"A": 25.0, "B": 40.0, "C": 25.0}
print(mean(student_grades))

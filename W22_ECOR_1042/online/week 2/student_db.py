from typing import Any

"""
    You are the professor of a third-year ECOR course at Carleton. It's the beginning
    of the term and you've just gotten the list of students enrolled in your
    course. The list formatted like this:

    students = [
        ["shay", 10.0, "MATH"],
        ["kayla", 9.8, "SYSC"],
        ["tobu", 11.5, "CHEM"],
        ["ray", 8.8 , "MATH"],
        ["omar", 7.7 , "SYSC"],
        ["jeon", 10.3 , "MATH"],
        ["kelci", 9.9 , "CHEM"],
        ...
    ]

    Each entry in the list is another list. The first index of the inner list is
    a student's first name, the second is their GPA and the last one is their favourite subject
    (one of MATH, SYSC or CHEM).

    You'd like to create function, analyse_students, that accepts a subject string as an input
    along with the 2D list of students.
    The program should return a tuple containing two things:
        - A list of the names of students who enjoy that subject.
        - The average GPA of those students.

    For example:
    >>> analyse_students(students, "MATH)
    >>> (["shay", "ray", "jeon"], 9.7)
"""


def analyse_students(student_list: list[list[Any]], subject: str) -> tuple[list[str], float]:
    """
    [Description]
    >>> [Examples]
    """
    count = 0
    gpa_sum = 0
    students_with_subject = []

    for student_info in student_list:
        student_fav_subject = student_info[2]

        if student_fav_subject == subject:
            students_with_subject.append(student_info[0])
            gpa_sum += student_info[1]
            count += 1

    average_gpa = gpa_sum / count

    return (students_with_subject, average_gpa)


if __name__ == "__main__":
    students = [
        ["shay", 10.0, "MATH"],
        ["kayla", 9.8, "SYSC"],
        ["tobu", 11.5, "CHEM"],
        ["ray", 8.8, "MATH"],
        ["omar", 7.7, "SYSC"],
        ["jeon", 10.3, "MATH"],
        ["kelci", 9.9, "CHEM"]
    ]

    print(analyse_students(students, "MATH"))

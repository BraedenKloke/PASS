"""
    One possible solution among many. Make sure you 
    understand why each line is needed - once you do, I 
    recommend trying to write your own solution from memory/intuition.
"""

def get_best_average(student_grades: dict) -> tuple:
    """
    Given a dictionary of students and lists of their grades, returns
    a tuple containing the average of all the students and the
    name of the student with the highest average.
    """
    # The sum of all the student averages (divide this by the number
    # of students and we get their total class average).
    total_averages = 0

    # Tracks the best average we've seen so far
    best_average_so_far = 0
    # Tracks the name of the student with this
    # best average so far
    best_av_student_so_far = ''

    # We'll loop through all the students to get their averages
    # If at any point, someone has a better average than the best
    # we've seen so far -> then they're the new best.
    # After going through everyone, we'll have the student with the 
    # highest average.


    """Loop through all the students in the dictionary

    Same as:
        for pair_tuple in student_grades.items():
            student, grades = pair_tuple

    Run a print line: print(list(student_grades.items()))
    and it should make more sense.
    """

    for student, grades in student_grades.items():
        # Calculate the average of each student
        grade_sum = 0
        for grade in grades:
            grade_sum += grade

        average = grade_sum / len(grades)

        # Update the total average by adding the 
        # one we just calculated
        total_averages += average

        # Check if this is the new highest we've seen, if
        # so, update the new highest.
        if average > best_average_so_far:
            best_av_student_so_far = student
            best_average_so_far = average

    # Calculate the overall class average - we're dividing by
    # the number of key-value pairs in the dictionary -> i.e the number of students.
    total_class_average = total_averages / len(student_grades)

    # Return both as a tuple (parantheses are optional).
    return total_class_average, best_av_student_so_far

# Test
grades = {
    "shim": 	[65, 100, 73],
    "leywin": 	[20, 88, 75],
    "shay":	[95, 99, 98]
}
print(get_best_average(grades))     # (79.22, 'shay')

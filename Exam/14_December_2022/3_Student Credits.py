def students_credits(*args):
    MAX_POINTS = 240
    total_dyian_points = 0
    dyian_result = {}

    for el in args:

        course, credit, max_points, my_points = el.split('-')
        my_credit = (float(my_points) / float (max_points)) * float(credit)
        total_dyian_points += my_credit
        dyian_result[course] = my_credit
    sorted_result = sorted(dyian_result.items(), key=lambda x: -x[1])
    result = []

    if total_dyian_points >= MAX_POINTS:
        result.append(F"Diyan gets a diploma with {total_dyian_points:.1F} credits.")
    else:
        result.append(F"Diyan needs {MAX_POINTS - total_dyian_points:.1f} credits more for a diploma.")
    for name, point in sorted_result:
        result.append(f'{name} - {point:.1F}')
    return "\n".join(result)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
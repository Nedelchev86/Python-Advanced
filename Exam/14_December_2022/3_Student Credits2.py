def students_credits(*args):
    total = 0
    courses_dict = {}
    for string in args:
        course_name, credit , max_test_points, diyan_point = string.split("-")
        percent = (int(diyan_point) / int(max_test_points)) * 100
        total +=  (percent * int(credit)) / 100
        courses_dict[course_name] =  (percent * int(credit)) / 100

    final_lsit = [F"{key} - {value:.1F}" for key, value in sorted(courses_dict.items(), key=lambda x: -x[1])]
    if total >= 240:
        final_lsit.insert(0,F"Diyan gets a diploma with {total:.1F} credits.")
        return "\n".join(final_lsit)
    else:
        final_lsit.insert(0,F"Diyan needs {240 -total:.1F} credits more for a diploma.")
        return "\n".join(final_lsit)



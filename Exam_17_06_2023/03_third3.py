def gather_credits(needed_credits, *args):
    earned_credits = 0
    passed_coursed = set()

    for course_name, course_credits in args:
        if earned_credits >= needed_credits:
            break

        if course_name in passed_coursed:
            continue

        earned_credits += course_credits
        passed_coursed.add(course_name)

    if needed_credits > earned_credits:
        credits_shortage = needed_credits - earned_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
    else:
        sorted_courses = sorted(passed_coursed)
        result = F"Enrollment finished! Maximum credits: {earned_credits}.\nCourses: {', '.join(sorted_courses)}"
        return result


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

def gather_credits(needed_credits, *args):
    earned_credits = 0
    passed_coursed = []
    for course_name, course_credits in args:
        if earned_credits >= needed_credits:
            break

        if course_name not in passed_coursed:
            earned_credits += course_credits
            passed_coursed.append(course_name)


    if needed_credits > earned_credits:
        return f"You need to enroll in more courses! You have to gather {needed_credits - earned_credits} credits more."
    else:
        result = F"Enrollment finished! Maximum credits: {earned_credits}.\nCourses: {', '.join(sorted(passed_coursed))}"
        return result

print(gather_credits(
    80,
    ("Basics", 27),
))

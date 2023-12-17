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
        credits_shortage = needed_credits - earned_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
    else:
        sorted_courses = sorted(passed_coursed)
        result = F"Enrollment finished! Maximum credits: {earned_credits}.\nCourses: {', '.join(sorted_courses)}"
        return result

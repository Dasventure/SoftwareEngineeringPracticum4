"""
MIT License

Copyright (c) 2023-2024 Kasper Engelen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from datetime import datetime


def log_error(message: str):
    pass


def get_current_date() -> datetime:
    pass


class Student:
    def get_student_nr(self) -> int:
        pass

    def has_paid_tuition(self) -> bool:
        pass

    def has_financial_aid(self) -> bool:
        pass

    def get_available_credits(self) -> int:
        pass

    def get_schedule(self) -> "StudentSchedule":
        pass

    def has_unfinished_courses(self) -> bool:
        pass

    def can_enroll_without_credits(self) -> bool:
        pass


class Course:
    def get_course_id(self) -> int:
        pass

    def get_enrollment_starting_date(self) -> datetime:
        pass

    def get_num_credits(self) -> int:
        pass

    def student_has_all_requirements(self, student: Student):
        pass

    def is_informational_course(self) -> bool:
        pass


class StudentSchedule:
    def add_course(self, course: Course):
        pass

    def is_space_available_for_course(self, course: Course) -> int:
        pass


def enroll_in_courses(student: Student, courses: list[Course], max_skipped: int, weight_factor: list[float]):
    should_return = False

    if student.has_paid_tuition():
        finance_ok = True
    else:
        if student.has_financial_aid():
            finance_ok = True
        else:
            finance_ok = False

    i = 0
    while i < len(courses):
        if should_return:
            i = len(courses)
        else:
            course = courses[i]
            if course.get_enrollment_starting_date() <= get_current_date():
                if finance_ok:
                    print("Adding course")
                else:
                    if course.is_informational_course():
                        print("Adding course")
                    else:
                        log_error(f"Cannot add course {student.get_student_nr()} for student {course.get_course_id()}")
                        should_return = True
            else:
                if course.is_informational_course():
                    print("Adding course")
                else:
                    log_error(f"Cannot add course {student.get_student_nr()} for student {course.get_course_id()}")
                    should_return = True
            i += 1

    courses_with_not_enough_credits = 0

    approved_courses = []

    if not should_return:
        schedule = student.get_schedule()

        adjusted_remaining_credits = student.get_available_credits()

        _need_stop = False

        while not _need_stop:
            if len(courses) > 0:
                if adjusted_remaining_credits > 0:

                    course = courses.pop()

                    if course.student_has_all_requirements(student):
                        if schedule.is_space_available_for_course(course):
                            adjusted_remaining_credits -= course.get_num_credits()
                            approved_courses.append(course)
                            courses_with_not_enough_credits = 0

                else:
                    _need_stop = True
            else:
                _need_stop = True

        i = 0
        while i < len(approved_courses):
            approved_course = approved_courses[i]
            schedule.add_course(approved_course)
            i += 1

    return approved_courses


'''
We guarantee that the loop continues as long as the length of [courses] is positive AND [adjusted_remaining_credits] is positive.

This means the loop ends when EITHER [courses] is zero, OR [adjusted_remaining_credits] is zero or negative.

In other words, there are three situations in which this expression can terminate:
1. [courses] is zero;
2. [adjusted_remaining_credits] is zero or negative;
3. [courses] is zero, AND [adjusted_remaining_credits] is zero or negative

The previous version implemented only option 3, manually setting the length of [courses] to zero, regardless of the actual length.
'''

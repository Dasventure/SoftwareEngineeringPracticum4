from src.user import User, Student, UserRegistrationException
from src.user_registration.signup_form import SignupForm
from logging import warn

class UserManager:
    """
        Class that manages users.
    """
    def __init__(self):
        self.users = []
        self.students = []

    def get_user(username: str) -> User:
        for user in self.users:
            if user.get_name() == username:
                return user

    def edit_user(self, facilities, userName):
        self.get_user(userName).facilities = facilities

    # add student to the system
    def add_student(self, user, student):
        self.students.append(student)
        self.users.append(user)


def register_user(form_data: SignupForm, userMan: UserManager):
    try:
        user = User(first_name=form_data.get_name().split(" ")[0],
                    last_name=form_data.get_name().split(" ")[1],
                    dob=form_data.get_dob())
        student = Student(facilities=[], user=user)
        student.set_program(form_data.get_degree())

        userMan.add_student(student, user)
    except Exception:
        warn("Error: unknown")
        raise 3
    except UserRegistrationException:
        warn("Error: unknown")
        raise 2
    except ValueError:
        warn("Error: unknown")
        raise 1




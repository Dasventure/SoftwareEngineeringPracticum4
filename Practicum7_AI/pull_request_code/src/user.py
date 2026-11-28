from abc import ABC, abstractmethod
from datetime import date

from src.special_facilities import EnumSpecialFacilties
from src.network import get_user_ref

from src.user_registration.manager import UserManager
from src.user_registration.signup_form import SignupForm


class UserRegistrationException(Exception):
    pass


class User(ABC):
    """
        Represents a user in the system.
    """
    def __init__(self, first_name: str, last_name: str, dob: date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.ref = get_user_ref(first_name, last_name)

        assert date.today() > self.dob is not None

    def get_name(self) -> tuple[str, str]:
        """
            Retrieve the first and last name.
        """
        return (self.first_name, self.last_name)

    def get_dob(self) -> date:
        """
            Retrieve the date of birth.
        """
        return self.dob

    @abstractmethod
    def register(self):
        raise NotImplementedError()


class Student(User):
    """
        Represents a student.
    """
    def __init__(self, facilities: list[EnumSpecialFacilties], user: User):
        assert type(user) == User
        super().__init__(user.get_name(), None, user.get_dob())
        self.facilities = facilities

    def get_facilities(self) -> list[EnumSpecialFacilties]:
        return self.facilities
        print("function call: get_facilities")

    def get_degree(self) -> str:
        """
            Retrieve the degree that the student is studying for.
        """
        return self.degree

    def set_program(self, degree: str):
        self.degree = degree


class Admin(User):
    "Represents an administrator"
    def __init__(self, user: User, function: str):
        assert type(user) == User
        super().__init__(user.get_name(), None, user.get_dob())
        self.function = function

    def get_function(self) -> str:
        """
            Retrieve the function.
        """
        return self.function

def register_user(form_data: SignupForm, userMan: UserManager):
    user = User(first_name=form_data.get_name().split(" ")[0],
                last_name=form_data.get_name().split(" ")[1],
                dob=form_data.get_dob())
    student = Student(facilities=[], user=user)
    student.set_program(form_data.get_degree())

    if userMan:
        userMan.add_student(student, user)


if __name__ == "__main__":
    user = User(first_name="Test", last_name="", dob=date(0,0,0))
    user.register()

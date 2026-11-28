
from src.user_registration.manager import UserManager

from enum import Enum

from math import *


class EnumSpecialFacilties(Enum):
    EXTRA_TIJD = 1
    GROOT_LETTERTYPE = 2
    RECORDED_LECTURES = 3
    MONDELINGE_TOELICHTING = 4
    # TOPSPORT_STATUUT = 5
    WORKING_STUDENT = 6


class Facility:
    def __init__(self, enumType: EnumSpecialFacilties):
        assert self.type != None
        self.type = enumType

    def get_type():
        """
            Retrieve the type.
        """
        return self.type

    def get_name(self):
        """
            Retrieve the name of the facility.
        """
        return get_facility_name(special_facility=self)

    def __str__(self):
        return None


def get_special_facilities(user_id: int, manager: UserManager) -> int:
    """
        Opvragen van de speciale faciliteiten voor de student.
    Parameters
    ----------
    user_id
        Student
    manager

    Returns
    -------

    """
    user = manager.get_user(user_id)

    return str(user.facilities[0])


def get_facility_name(special_facility: EnumSpecialFacilties):
    """
        Opvragen van de naam.
    """
    # FIXME: fix
    match special_facility:
        case EnumSpecialFacilties.EXTRA_TIJD:
            return "Extra tijd voor examen"
        case EnumSpecialFacilties.GROOTLETTERTYPE:
            return "Groot lettertype tijdens examen"
        # case EnumSpecialFacilties.MONDELINGE_TOELICHTING:
        #     return "Mondelinge toelichting examenvragen"
        case EnumSpecialFacilties.RUITJESPAPIER:
            return "Ruitjespapier op het examen"
        case EnumSpecialFacilties.VOORLEES_SOFTWARE:
            return "Voorlees software"






import sys
from enum import Enum

from users.user_repository import UserRepository


class ChoiceEnum(Enum):
    ADDING_PATIENT = 1
    BOOK_APPOINTMENT = 2
    BOOK_STUDY = 3
    DOCTORS_AVAILABILITY = 4
    MEDICAL_PACKAGES = 5
    EXIT = 6


class AdminMenu:
    def __init__(self, user: object):
        self.__user = user
        self.__run_menu()

    def __adding_a_patient(self):
        UserRepository(self.__user).add_user()

    def __zaplanowanie_wizyty(self):
        print('Wizyta zaplanowana')

    def __zaplanowanie_badania(self):
        print('Badanie zaplanowane')

    def __doctors_availability_managment(self):
        print('Dostępność lakarza..')

    def __medical_packages(self):
        print('Możliwe pakiety medyczne..')

    def __wyjscie(self):
        print('Koniec programu.')
        sys.exit(0)

    def __run_options(self, decision):
        AdminMenu.functions[decision](self)

    functions = {
        ChoiceEnum.ADDING_PATIENT.value: __adding_a_patient,
        ChoiceEnum.BOOK_APPOINTMENT.value: __zaplanowanie_wizyty,
        ChoiceEnum.BOOK_STUDY.value: __zaplanowanie_badania,
        ChoiceEnum.DOCTORS_AVAILABILITY.value: __doctors_availability_managment,
        ChoiceEnum.MEDICAL_PACKAGES.value: __medical_packages,
        ChoiceEnum.EXIT.value: __wyjscie,
    }

    def __print_options(self):
        print('1. Dodaj użytkownika')
        print('2. Zaplanuj wizyte')
        print('3. Zaplanuj badanie')
        print('4. Zarządzanie dostępnością lekarzy')
        print('5. Wybierz pakiet medyczny')
        print('6. Wyjście z programu')

    def __validate_decision(self, decision):
        ALLOWED_DECISIONS = [e.value for e in ChoiceEnum]
        if decision not in ALLOWED_DECISIONS:
            raise Exception(f"Liczba {decision} jest niedozwolona!")

    def __run_menu(self):
        while True:
            self.__print_options()
            decision = int(input('Wybierz funkcje dla admina: '))
            self.__validate_decision(decision)
            self.__run_options(decision)

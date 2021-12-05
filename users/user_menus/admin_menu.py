import sys
from enum import Enum


# TODO Needs reformatting to class
class ChoiceEnum(Enum):
    ADDING_PATIENT = 1
    BOOK_APPOINTMENT = 2
    BOOK_STUDY = 3
    DOCTORS_AVAILABILITY = 4
    MEDICAL_PACKAGES = 5
    EXIT = 6


def adding_a_patient():
    print('Nowy pacjent dodany')


def zaplanowanie_wizyty():
    print('Wizyta zaplanowana')


def zaplanowanie_badania():
    print('Badanie zaplanowane')


def doctors_availability_managment():
    print('Dostępność lakarza..')


def medical_packages():
    print('Możliwe pakiety medyczne..')


def wyjscie():
    print('Koniec programu.')
    sys.exit(0)


def run_options(decision):
    functions[decision]()


functions = {
    ChoiceEnum.ADDING_PATIENT.value: adding_a_patient,
    ChoiceEnum.BOOK_APPOINTMENT.value: zaplanowanie_wizyty,
    ChoiceEnum.BOOK_STUDY.value: zaplanowanie_badania,
    ChoiceEnum.DOCTORS_AVAILABILITY.value: doctors_availability_managment,
    ChoiceEnum.MEDICAL_PACKAGES.value: medical_packages,
    ChoiceEnum.EXIT.value: wyjscie,
}


def print_options():
    print('1. Dodaj pacjenta')
    print('2. Zaplanuj wizyte')
    print('3. Zaplanuj badanie')
    print('4. Zarządzanie dostępnością lekarzy')
    print('5. Wybierz pakiet medyczny')
    print('6. Wyjście z programu')


def validate_decision(decision):
    ALLOWED_DECISIONS = [e.value for e in ChoiceEnum]
    if decision not in ALLOWED_DECISIONS:
        raise Exception(f"Liczba {decision} jest niedozwolona!")


def run_menu():
    # while True:
    print_options()
        # decision = int(input('Wybierz funkcje dla admina: '))
        # validate_decision(decision)
        # run_options(decision)

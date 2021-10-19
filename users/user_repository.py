from enum import Enum

from user_classes.admin_user import Admin


class UserChoiceEnum(Enum):
    ADD_PATIENT = 1
    ADD_DOCTOR = 2
    ADD_RECEPTIONIST = 3


class UserRepository:
    def __init__(self, current_user: object):
        self.current_user = current_user

    def add_user(self):
        def print_options():
            print('1. Dodaj pacjenta.')
            print('2. Dodaj lekarza.')
            print('3. Dodaj recepcjonistkę.')

        def validate_decision(decision):
            ALLOWED_DECISIONS = [option.value for option in UserChoiceEnum]
            if decision not in ALLOWED_DECISIONS:
                print(f'Liczba {decision} jest niedozwolona.')
                raise ValueError

        def add_doctor():
            # TODO Implement function
            print('Creating a doc')

        def add_receptionist():
            # TODO Implement function
            print('Creating a receptionist')

        def add_patient():
            # TODO Implement function
            print('Creating a patient')

        def execute_decision(decision):
            functions = {
                UserChoiceEnum.ADD_PATIENT.value: add_patient,
                UserChoiceEnum.ADD_DOCTOR.value: add_doctor,
                UserChoiceEnum.ADD_RECEPTIONIST.value: add_receptionist,
            }
            functions[decision]()

        if isinstance(self.current_user, Admin):
            print_options()
            user_choice = int(input('Wybierz jedną z opcji: '))
            validate_decision(user_choice)
            execute_decision(user_choice)


# TODO Remove below tests
admin_user = Admin('a', 'b', 1, 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
UserRepository(admin_user).add_user()

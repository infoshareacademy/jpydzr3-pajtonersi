import json

from users.user_classes.class_user import User


class Admin(User):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            login: str,
            password: str,
            pesel: int,
            gender: str,
            phone_no: str,
            email: str,
            street: str,
            city: str,
            zip_code: str,
            is_active: str,
            hire_date: str,
            position: str,
            function: str
    ):

        super().__init__(
            first_name,
            last_name,
            login,
            password,
            pesel,
            gender,
            phone_no,
            email,
            street,
            city,
            zip_code,
            is_active
        )

        self.hire_date = hire_date
        self.position = position
        self.function = function

    def display_patient_list(self):
        # TODO implement patient list display
        pass

    def add_user(self):
        internal_users_database = {}
        first_name = input('Podaj imię użytkownika wewnętrznego: ')
        last_name = input('Podaj nazwisko użytkownika wewnętrznego: ')
        login = input('Podaj login użytkownika wewnętrznego: ')
        password = input('Podaj hasło użytkownika: ')
        pesel = int(input('Podaj PESEL użytkownika: '))
        gender = input('Podaj płeć użytkownika: ')
        phone_no = input('Podaj numer telefonu użytkownika: ')
        email = input('Podaj adres email użytkownika: ')
        street = input('Podaj adres zamieszkania użytkownika (ulicę): ')
        city = input('Podaj adres zamieszkania użytkownika (miasto): ')
        zip_code = input('Podaj adres zamieszkania użytkownika (kod pocztowy): ')
        is_active = input('Podaj status konta użytkownika: ')
        hire_date = input('Podaj datę zatrudnienia użytkownika w placówce medycznej: ')
        position = input('Podaj stanowisko pracownicze użytkownika: ')
        function = input('Podaj funkcję użytkownika: ')
        if function == 'DOCTOR':
            specialty = input('Podaj specjalizację lekarza: ')
            location = input('Podaj lokalizację, w której przyjmuje lekarz: ')
            internal_users_database['first_name'] = first_name
            internal_users_database['last_name'] = last_name
            print('Użytkownik lekarz został utworzony.')

        elif function == 'RECEPTIONIST':
            internal_users_database['first_name'] = first_name
            internal_users_database['last_name'] = last_name
            print('Użytkownik recepcjonista został utworzony.')

        else:
            print('Podana funkcja nie istnieje')

        with open('internal_users_database.json', 'w') as database_file:
            json.dump(internal_users_database, database_file)


    add_user('cos')

    def edit_user(self):
        # TODO implement user edition
        pass

    def display_user(self):
        # TODO implement display user
        pass

    def delete_user(self):
        # TODO implement user deletion
        pass

    def doctors_availability_setter(self):
        # TODO implement doctors availability settings
        pass

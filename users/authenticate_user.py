from typing import Tuple
from users.user_classes.class_patient import Patient

# TODO Remove below list when tests are over and reformat code
dummy_user_list = [Patient('Jarek', 'Majka', 'a', 'b', 'c', 'd',
                           'e', 'f', 'g', 'h', 'i', 'j', 'k')]


class AuthenticateUser:
    def __init__(self):
        self.__user = self.log_in()

    @staticmethod
    def log_in() -> object:
        """
        Checks the user name and password untill correct data provided.
        :return: logged in user
        """
        def credentials_input() -> Tuple:
            login = input('Podaj login: ')
            password = input('Podaj hasło: ')
            return login, password

        def credentials_check(credentials: tuple) -> object:
            """
            Checks if user exists in DB and returns instance of an object
            If given login or password is incorrect prompts for input again.
            """

            def login_check(login: str) -> object:
                for idx in range(len(dummy_user_list)):
                    if dummy_user_list[idx].username == login:
                        return dummy_user_list[idx]

            def password_check(user: object, password_given: str) -> object:
                if user:
                    if user.password == password_given:
                        print(f'Udane logowanie. '
                              f'Dzień dobry {user.first_name}')
                        return user
                    else:
                        return None

            return password_check(login_check(credentials[0]), credentials[1])

        while True:
            logged_user = credentials_check(credentials_input())
            if logged_user:
                return logged_user
            else:
                print('Błędny login lub hasło')

    def get_user(self):
        return self.__user

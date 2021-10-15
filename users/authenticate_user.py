from typing import Tuple
from users.user_classes.class_patient import Patient
from users.user_classes.class_doctor import Doctor

# TODO Remove below list when tests are over and reformat code
dummy_user_list = [Patient('Jarek', 'Majka', 1, 'male', 'street', 'city', 'post-code',
                           'phone number', 'email', 'active account', 'top-tier'),
                   Doctor('Doctor', 'Quinn', 2, 'female', 'street', 'city', 'post-code', 'phone number', 'email',
                          'active', 'today', 'general medic', 'doctor', 'general', 'here')]


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
            """
            Accepts user input for Login and Password fields
            :return: Tuple of user credentials
            """
            login = input('Podaj login: ')
            password = input('Podaj hasło: ')
            return login, password

        def credentials_check(credentials: tuple) -> object:
            """
            Checks if user exists in DB and returns instance of an object
            If given login or password is incorrect prompts for input again.
            :param credentials: user log-in data retrieved from credentials_input() function
            """

            def login_check(login: str) -> object:
                for idx in range(len(dummy_user_list)):
                    if dummy_user_list[idx].username == login:
                        return dummy_user_list[idx]

            def password_check(user: object, password_given: str):
                """
                Returns user object
                :param user: object that needs to be validated if can be returned
                :param password_given: password provided by the user
                """
                if user:
                    if user.password == password_given:
                        print('Udane logowanie')
                        print(type(user))
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

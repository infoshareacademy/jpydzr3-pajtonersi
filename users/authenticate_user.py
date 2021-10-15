from typing import Tuple
from users.user_classes.class_patient import Patient
from users.user_classes.class_doctor import Doctor

# TODO Remove below lists when tests are over
dummy_user_list = [Patient('Jarek', 'Majka', 1, 'male', 'street', 'city', 'post-code',
                           'phone number', 'email', 'active account', 'top-tier')]
dummy_admin_list = [Doctor('Doctor', 'Quinn', 2, 'female', 'street', 'city', 'post-code', 'phone number', 'email',
                           'active', 'today', 'general medic', 'doctor', 'general', 'here')]


class UserAuthentication:
    def __init__(self):
        self.log_in()

    def credentials_input(self) -> Tuple:
        """
        Accepts user input for Login and Password fields
        :return: Tuple of user credentials
        """
        login = input('Podaj login: ')
        password = input('Podaj hasło: ')
        return login, password

    def credentials_check(self, credentials: tuple) -> object:
        """
        Checks if user exists in DB and returns instance of an object
        If given login or password is incorrect prompts for input again.
        :param credentials: user log-in data retrieved from credentials_input() function
        """
        def login_check(login: str) -> dict:
            if dummy_user_list.get(login):
                return dummy_user_list.get(login)
            elif dummy_admin_list.get(login):
                return dummy_admin_list.get(login)
            else:
                return None

        # TODO When we will switch to proper class objects reformat below code.
        def password_check(user: dict, password_given: str):
            """
            Returns user object
            :param user: object that needs to be validated if can be returned
            :param password_given: password provided by the user
            """
            if user:
                if user['password'] == password_given:
                    print('Udane logowanie')
                    return user
                else:
                    return None

        return password_check(login_check(credentials[0]), credentials[1])

    def log_in(self) -> object:
        """
        Checks the user name and password untill correct data provided.
        :return: logged in user
        """
        while True:
            logged_user = self.credentials_check(self.credentials_input())
            if logged_user:
                return logged_user
            else:
                print('Błędny login lub hasło')

from typing import Tuple

# TODO Remove below lists when tests are over
dummy_user_list = {'Jarek': {'password': '12345', 'general_status': 'healthy'},
                   'Adrian': {'password': '1111', 'general_status': 'healthy'}}
dummy_admin_list = {'Doktor': {'password': 'Quinn'},
                    'Recepcja': {'password': 'recepcja1'}}


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


def log_in() -> object:
    """
    Checks the user name and password untill correct data provided.
    :return: logged in user
    """
    while True:
        logged_user = credentials_check(credentials_input())
        if logged_user:
            return logged_user
        else:
            print('Błędny login lub hasło')

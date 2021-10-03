from typing import Tuple


def credentials_input() -> Tuple:
    """
    Accepts user input for Login and Password fields
    :return: Tuple of user credentials
    """
    login = input('Podaj login: ')
    password = input('Podaj hasło')
    return tuple(login, password)


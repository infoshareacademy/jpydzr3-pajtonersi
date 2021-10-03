from typing import Tuple

# TODO Remove below lists when tests are over
dummy_user_list = {'Jarek': {'password': 12345, 'general_status': 'healthy'},
                   'Adrian': {'password': 1111, 'general_status': 'healthy'}}
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
    :param credentials: user log-in data retrieved from credentials_input() function
    """
    def login_check(login):
        if dummy_user_list.get(login):
            return dummy_user_list.get(login)
        elif dummy_admin_list.get(login):
            return dummy_admin_list.get(login)
        else:
            print('Nie ma takiego użytkownika.')
            credentials_input()

    login_check(credentials[0])


print(credentials_check(credentials_input()))
# TODO Step-by-step skeleton
# Sprawdzenie, czy użytkownik istnieje w bazie userów i adminów
# Sprawdzenie hasła
# Przekierowanie do odpowiedniego menu

from user_classes.admin_user import Admin


class UserRepository:
    def __init__(self, current_user: object):
        self.current_user = current_user

    def add_user(self):
        if isinstance(self.current_user, Admin):
            # TODO User ENUM
            print('1. Dodaj pacjenta.')
            print('2. Dodaj lekarza.')
            print('3. Dodaj recepcjonistkę.')
            user_choice = input('Wybierz jedną z opcji: ')


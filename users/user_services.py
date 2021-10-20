from users.authenticate_user import AuthenticateUser
from users.user_classes.class_admin import Admin
from users.user_classes.class_patient import Patient
from users.user_menus.admin_menu import run_menu


class UserServices:
    def __init__(self):
        self.__user = self.set_user()
        self.print_menu(self.get_user())

    def set_user(self) -> object:
        """Setter for __user attribute"""
        def authenticated_user() -> object:
            """Authenticates user and returns instance of user object"""
            return AuthenticateUser().get_user()
        return authenticated_user()

    def get_user(self):
        """Getter for __user attribute"""
        return self.__user

    def print_menu(self, user):
        if isinstance(user, Admin):
            run_menu()
        elif isinstance(user, Patient):
            print('It\'s a Patient')

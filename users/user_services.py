from users.authenticate_user import UserAuthentication
from users.user_classes.class_doctor import Doctor
from users.user_classes.class_receptionist import Receptionist
from users.user_classes.class_patient import Patient


class UserServices:
    def __init__(self):
        self.__user = self.set_user()

    def set_user(self) -> object:
        """Setter for __user attribute"""
        def authenticated_user() -> object:
            """Authenticates user and returns instance of user object"""
            return UserAuthentication()
        return authenticated_user()

    def get_user(self):
        """Getter for __user attribute"""
        return self.__user

    def check_user_type(self, user):
        if isinstance(user, Doctor):
            print('It\'s a Doctor')
        elif isinstance(user, Receptionist):
            print('It\'s a Receptionist')
        elif isinstance(user, Patient):
            print('It\'s a Patient')

    def menu_printer(self):
        pass

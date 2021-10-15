from login_screen import UserAuthentication


class UserServices:
    def __init__(self):
        pass

    def authenticate_user(self) -> object:
        """Authenticates user and return instance of user object"""
        UserAuthentication()

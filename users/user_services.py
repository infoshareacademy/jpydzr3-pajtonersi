from users.authenticate_user import UserAuthentication


class UserServices:
    def __init__(self):
        self.user = self.set_user()

    def set_user(self):
        return self.authenticate_user()

    def authenticate_user(self) -> object:
        """Authenticates user and return instance of user object"""
        return UserAuthentication()

    def check_user_type(self):
        pass

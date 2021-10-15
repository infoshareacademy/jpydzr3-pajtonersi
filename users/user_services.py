import login_screen


class UserServices:
    def __init__(self):
        pass

    def user_authentication(self) -> object:
        """Authenticates user and return instance of user object"""
        login_screen.log_in()

from users import authenticate_user


class AppInterface:
    def __init__(self):
        authenticate_user.log_in()

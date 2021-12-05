from users.authenticate_user import AuthenticateUser, InputProvider


class MockInputProvider(InputProvider):
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def provide_input(self, text):
        result = self.inputs[self.index]
        self.index = self.index + 1
        return result


def test_credentials_log_in(login_information):
    result = AuthenticateUser.log_in(MockInputProvider(login_information))
    assert result.username == login_information.login
    assert result.password == login_information.password



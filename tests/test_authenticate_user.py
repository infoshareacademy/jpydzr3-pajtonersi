from users.authenticate_user import AuthenticateUser
import unittest
from unittest.mock import patch


class Mock:
    login = 'Jarek.Majka'
    password = 'a'
    inputs = [login, password]
    index = 0

    @classmethod
    def provide_input(cls, text):
        result = Mock.inputs[Mock.index]
        Mock.index += 1
        return result


class TestAuthenticateUser(unittest.TestCase):
    @patch('users.authenticate_user.InputWrapper', wraps=Mock)
    def test_credentials_log_in(self, mock_class):
        login = 'Jarek.Majka'
        password = 'a'
        result = AuthenticateUser.log_in()
        assert result.username == login
        assert result.password == password

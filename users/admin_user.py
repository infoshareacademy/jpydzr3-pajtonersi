from users.base_user import User


class Admin(User):
    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, address: str, city: str,
                 postal_code: str, phone_no: str, email: str,
                 account_status: str, hire_date: str, position: str, function: str):
        super().__init__(first_name, last_name, pesel, gender, address,
                         city, postal_code, phone_no, email, account_status)
        self.hire_date = hire_date
        self.position = position
        self.function = function

    def display_patient_list(self):
        # TODO implement patient list display
        pass

    def add_user(self):
        # TODO implement new user creation
        pass

    def edit_user(self):
        # TODO implement user edition
        pass

    def display_user(self):
        # TODO implement display user
        pass

    def delete_user(self):
        # TODO implement user deletion
        pass

    def doctors_availability_setter(self):
        # TODO implement doctors availability settings
        pass

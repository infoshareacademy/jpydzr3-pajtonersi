from master_user import User


class Admin(User):
    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, phone_no: str, city: str,
                 address: str):
        super().__init__(first_name, last_name, pesel, gender, phone_no, city, address)

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

from users.user_classes.class_user import User


class Admin(User):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            password: str,
            pesel: int,
            gender: str,
            phone_no: str,
            email: str,
            street: str,
            city: str,
            zip_code: str,
            is_active: str,
            hire_date: str,
            position: str,
            function: str
    ):

        super().__init__(
            first_name,
            last_name,
            password,
            pesel,
            gender,
            phone_no,
            email,
            street,
            city,
            zip_code,
            is_active
        )

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

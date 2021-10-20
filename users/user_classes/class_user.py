class User:
    idx_increment = 1

    def __init__(
            self,
            first_name: str,
            last_name: str,
            login: str,
            password: str,
            pesel: int,
            gender: str,
            phone_no: str,
            email: str,
            street: str,
            city: str,
            zip_code: str,
            is_active: str
    ):

        self.user_idx = User.idx_increment
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.pesel = pesel
        self.gender = gender
        self.phone_no = phone_no
        self.email = email
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.is_active = is_active
        self._username = None
        User.idx_increment += 1

    @property
    def username(self):
        print('getting value...')
        if not self._username:
            return self.first_name + '.' + self.last_name
        return self._username

    @username.setter
    def username(self, value):
        print('setting value...')
        self._username = value

    def password_change(self, new_password: str) -> None:
        """
        Changes user password
        :param new_password: new value of self.password
        """
        self.password = new_password

    def schedule_a_visit(self):
        # TODO implement visit schedule
        pass

    def reschedule_a_visit(self):
        # TODO implement visit re-schedule
        pass

    def cancel_a_visit(self):
        # TODO implement visit cancelation
        pass

    def sick_leave_list(self):
        # TODO implement sick leave list
        pass

    def visit_list(self):
        # TODO implement visit list display
        pass

    def display_doctors_list(self):
        # TODO implement doctors list display
        pass

    def display_doctors_availability(self):
        # TODO implement doctors availability list
        pass







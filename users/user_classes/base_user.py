class User:
    idx_increment = 1

    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, phone_no: str, city: str, address: str):
        self.user_idx = User.idx_increment
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.gender = gender
        self.phone_no = phone_no
        User.idx_increment += 1

    @property
    def username(self):
        print('getting value...')
        return self.first_name + '.' + self.last_name

    @username.setter
    def username(self, value):
        print('setting value...')
        first_name, last_name = value.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    def username_change(self, new_username: str) -> None:
        """
        Changes default username for specified new one
        :param new_username: new value of self.username
        """
        self.username = new_username

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







from master_user import User


class Admin(User):
    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, phone_no: str, city: str,
                 address: str):
        super().__init__(first_name, last_name, pesel, gender, phone_no, city, address)




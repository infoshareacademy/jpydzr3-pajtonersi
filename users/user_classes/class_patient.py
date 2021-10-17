from users.user_classes.base_user import User


class Patient(User):
    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, address: str, city: str,
                 postal_code: str, phone_no: str, email: str, account_status: str, package):
        super().__init__(first_name, last_name, pesel, gender,  address, city,
                         postal_code, phone_no, email, account_status)
        self.package = package

    def change_password(self):
        print('Hasło zostało zmienione')

    def view_profile(self):
        print('Profil pacjenta został wyświetlony')

    def change_some_personal_data(self):
        print('Dane pacjenta zostały zmienione')

    def view_orders_with_resutls(self):
        print('Zlecenia z wynikami badań zostały wyświetlone')

    def view_perscriptions(self):
        print('Recepty zostały wyświetlone')

    def view_referrals(self):
        print('Skierowania zostały wyświetlone')

    def sign_up_visit(self):
        print('Wizyta została zarezerwowana')

    def sign_up_medical_examination(self):
        print('Badanie lekarskie zostało zarezerwowane')

    def edit_visit(self):
        print('Wizyta została zmieniona')

    def cancel_visit(self):
        print('Wizyta została odwołana')

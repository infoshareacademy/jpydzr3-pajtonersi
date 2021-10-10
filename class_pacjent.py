from master_user import User


class Pacjent(User):

    def __init__(self, gender, city, email: str, package_code, first_name: str, last_name: str,
                 phone_no: str, address: str, pesel: int, postal_code: str):
        super().__init__(first_name, last_name, pesel, gender, phone_no, city, address, postal_code, email)
        self.package_code = package_code

    def change_password(self):
        print('Hasło zostało zmienione')

    def view_profile(self):
        print('Profil pacjenta został wyświtlony')

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

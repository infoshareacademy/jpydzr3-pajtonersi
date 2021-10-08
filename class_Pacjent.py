class Pacjent:
    pacjent_number = 0

    def __init__(self, name, surname, PESEL, password, login, gender, street, city, postal_code, phone_number, email, package_code):
        self.id = self.pacjent_number
        self.name = name
        self.surname = surname
        self.PESEL = PESEL
        self.password = password
        self.login = login
        self.gender = gender
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.email = email
        self.package_code = package_code
        Pacjent.pacjent_number += 1

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

pacjent1 = Pacjent
print(pacjent1)




class Doctor:
    number = 0
    def __init__(self, name, surname, login, password, pesel, hire_date, position, function, sex, account_status,
                     street, city, postal_code, phone_number, email, specialty, location):
        self.id = self.number
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.pesel = pesel
        self.hire_date = hire_date
        self.position = position
        self.function = function
        self.sex = sex
        self.account_status = account_status
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.email = email
        self.specialty = specialty
        self.location = location
        Doctor.number += 1

    def add_availability_to_calendar(self):
        print('Wizyta została dodana do kalendarza.')

    def edit_availability_in_calendar(self):
        print('Wizyta została edytowana w kolendarzu.')

    def show_availability_in_calendar(self):
        print('Dostępność została wyświetlona.')

    def remove_availability_from_calendar(self):
        print('Wizyta została usunięta z kalendarza.')

    def register_visit(self):
        print('Wizyta została zarejestrowana.')

    def add_comments_to_visit(self):
        print('Komentarz został dodany do wizyty.')

    def write_prescription(self):
        print('Recepta została wystawiona.')

    def issue_a_sick_leave(self):
        print('Zwolnienie lekarskie zostało wystawione.')
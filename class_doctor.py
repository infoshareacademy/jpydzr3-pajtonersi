from admin_user import Admin

class Doctor(Admin):
    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, address: str, city: str,
                 postal_code: str, phone_no: str, email: str, account_status: str, hire_date: str, position: str, function: str, specialty: str, location: str):
        super().__init__(first_name, last_name, pesel, gender, phone_no, city, address, postal_code, email, account_status, hire_date, position, function)
        self.specialty = specialty
        self.location = location

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

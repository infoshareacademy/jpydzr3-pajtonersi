from admin_user import Admin

class Receptionist(Admin):

    def __init__(self, first_name: str, last_name: str, pesel: int, gender: str, phone_no: str, city: str,
                 address: str, postal_code: str, email: str, hire_date: str, position: str, function: str,
                 account_status: str):
        super().__init__(first_name, last_name, pesel, gender, phone_no, city, address, postal_code, email)
        self.hire_date = hire_date
        self.position = position
        self.function = function
        self.account_status = account_status


    def add_new_patient(self):
        print('Nowy pacjent został dodany.')

    def edit_patient(self):
        print('Dane pacjenta zostały zmienione.')

    def show_patient(self):
        print('Dane pacjenta zostały wyświetlone.')

    def remove_patient(self):
        print('Pacjent został usunięty.')

    def schedule_doctor_appointment(self):
        print('Pacjent został zapisany na wizytę lekarską.')

    def edit_doctor_appointment(self):
        print('Wizyta lekarska została zmieniona.')

    def show_doctor_appointment(self):
        print('Wizyta lekarska została wyświetlona.')

    def remove_doctor_appointment(self):
        print('Wizyta lekarska została usunięta.')

import json

class Receptionist:
    number = 0

    def __init__(self, name, surname, login, password, pesel, hire_date, position,
                 function, sex, account_status, street, city, postal_code, phone_number, email):
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
        Receptionist.number += 1

    def add_new_patient(self):
        with open('db.json') as f:
            users = json.dumps(f.read())

            def authenticate_user():
                login = input('Podaj imię pracownika recepcji:  ')
                if users.get(login):
                    password = input('Podaj hasło:  ')
                    if users[login] == password:
                        return login
                    else:
                        return False
                else:
                    return False
            def tworzenie_klienta():
                user_authenticated = False
                while not user_authenticated:
                    user_authenticated = authenticate_user()
                    print(f'user_authenticated: {user_authenticated}')

                if user_authenticated == 'admin':
                    print('Wybierz co chciałbyś zrobić')
                    print('1. Utwórz nowego pacjenta')

                    option = input('Podaj numer opcji:  ')
                    if option == '1':
                        print(users)
                        #tu podajesz nowy login i hasło
                        login = input('podaj imię nowego pacjenta:  ')
                        password = input('podaj hasło nowego pacjenta:  ')
                        #dodanie informacji do bazy danych
                        users[login] = password
                        print(users)
                        f.write(users)
                tworzenie_klienta()
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

from users.user_classes.class_doctor import Doctor
from users.user_classes.class_patient import Patient
from users.user_classes.class_receptionist import Receptionist


def add_user(self):
    def doctor_creation():
        first_name = input('Podaj imię lekarza: ')
        last_name = input('Podaj nazwisko lekarza: ')
        password = input('Podaj hasło lekarza: ')
        pesel = int(input('Podaj PESEL lekarza: '))
        gender = input('Podaj płeć lekarza: ')
        phone_no = input('Podaj numer telefonu lekarza: ')
        email = input('Podaj adres email lekarza: ')
        street = input('Podaj adres zamieszkania lekarza (ulicę): ')
        city = input('Podaj adres zamieszkania lekarza (miasto): ')
        zip_code = input('Podaj adres zamieszkania lekarza (kod pocztowy): ')
        is_active = input('Podaj status konta lekarza: ')
        hire_date = input('Podaj datę zatrudnienia lekarza w placówce medycznej: ')
        position = input('Podaj stanowisko pracownicze lekarza: ')
        specialty = input('Podaj specjalizację lekarza: ')
        location = input('Podaj lokalizację, w której przyjmuje lekarz: ')
        # return Doctor(
        #     first_name,
        #     last_name,
        #     password,
        #     pesel,
        #     gender,
        #     phone_no,
        #     email,
        #     street,
        #     city,
        #     zip_code,
        #     is_active,
        #     hire_date,
        #     position,
        #     specialty,
        #     location
        # )

        doctor = Doctor(first_name, last_name, password, pesel, gender, phone_no, email, street, city, zip_code, is_active, hire_date, position, specialty, location)
        print(vars(doctor))

    doctor_creation()

    def receptionist_creation():
        first_name = input('Podaj imię recepcjonisty: ')
        last_name = input('Podaj nazwisko recepcjonisty: ')
        password = input('Podaj hasło recepcjonisty: ')
        pesel = int(input('Podaj PESEL recepcjonisty: '))
        gender = input('Podaj płeć recepcjonisty: ')
        phone_no = input('Podaj numer telefonu recepcjonisty: ')
        email = input('Podaj adres email recepcjonisty: ')
        street = input('Podaj adres zamieszkania recepcjonisty (ulicę): ')
        city = input('Podaj adres zamieszkania recepcjonisty (miasto): ')
        zip_code = input('Podaj adres zamieszkania recepcjonisty (kod pocztowy): ')
        is_active = input('Podaj status konta recepcjonisty: ')
        hire_date = input('Podaj datę zatrudnienia recepcjonisty w placówce medycznej: ')
        position = input('Podaj stanowisko pracownicze recepcjonisty: ')
        # return Receptionist(
        #     first_name,
        #     last_name,
        #     password,
        #     pesel,
        #     gender,
        #     phone_no,
        #     email,
        #     street,
        #     city,
        #     zip_code,
        #     is_active,
        #     hire_date,
        #     position
        # )

        receptionist = Receptionist(first_name, last_name, password, pesel, gender, phone_no, email, street, city, zip_code, is_active, hire_date, position)
        print(vars(receptionist))

    receptionist_creation()

    def patient_creation():
        first_name = input('Podaj imię pacjenta: ')
        last_name = input('Podaj nazwisko pacjenta: ')
        password = input('Podaj hasło pacjenta: ')
        pesel = int(input('Podaj PESEL pacjenta: '))
        gender = input('Podaj płeć pacjenta: ')
        phone_no = input('Podaj numer telefonu pacjenta: ')
        email = input('Podaj adres email pacjenta: ')
        street = input('Podaj adres zamieszkania pacjenta (ulicę): ')
        city = input('Podaj adres zamieszkania pacjenta (miasto): ')
        zip_code = input('Podaj adres zamieszkania pacjenta (kod pocztowy): ')
        is_active = input('Podaj status konta pacjenta: ')
        package = input('Podaj pakiet medyczny pacjenta: ')
        # return Patient(
        #     first_name,
        #     last_name,
        #     password,
        #     pesel,
        #     gender,
        #     phone_no,
        #     email,
        #     street,
        #     city,
        #     zip_code,
        #     is_active,
        #     package
        # )

        patient = Patient(first_name, last_name, password, pesel, gender, phone_no, email, street, city, zip_code, is_active, package)
        print(vars(patient))

    patient_creation()

add_user('cos')


import json

class Doctor_conver:

    def __init__(
            self,
            first_name,
            last_name,
            login,
            password,
            pesel,
            gender,
            phone_no,
            email,
            street,
            city,
            zip_code,
            is_active,
            hire_date,
            position,
            function,
            specialty,
            location
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.pesel = pesel
        self.gender = gender
        self.phone_no = phone_no
        self.email = email
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.is_active = is_active
        self.hire_date = hire_date
        self.position = position
        self.function = function
        self.specialty = specialty
        self.location = location

doktor1 = Doctor_conver(
    'Antoni',
    'Nowy',
    'antoni_nowy',
    'qwert',
    '0312012',
    'male',
    '550 000 000',
    'antoni.nowy@gmail.com',
    'Lipowa',
    'Zakole',
    '00-000',
    'yes',
    '30.03.1990',
    'doctor',
    'consultation',
    'podiatrist',
    'Warsaw')

dict_doktor1 = {doktor1.first_name: (vars(doktor1))}
print(dict_doktor1)

with open('doktor1_dict.json', 'w') as database_file:
    json.dump(dict_doktor1, database_file)




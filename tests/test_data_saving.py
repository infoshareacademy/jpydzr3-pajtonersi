from database_dict_JSON import data_saving


def test_save_doctor(doctor1, doctor2):
    expected = '{"1": {' \
               '"user_idx": 1, ' \
               '"first_name": "Doctor", ' \
               '"last_name": "Quinn", ' \
               '"password": "a", ' \
               '"pesel": "b", ' \
               '"gender": "a", ' \
               '"phone_no": "b", ' \
               '"email": "a", ' \
               '"street": "a", ' \
               '"city": "a", ' \
               '"zip_code": "a", ' \
               '"is_active": "a", ' \
               '"_username": null, ' \
               '"hire_date": "a", ' \
               '"position": "a", ' \
               '"specialty": "a", ' \
               '"location": "a"}, ' \
               '"2": {' \
               '"user_idx": 2, ' \
               '"first_name": "Doctor", ' \
               '"last_name": "Quinn", ' \
               '"password": "a", ' \
               '"pesel": "b", ' \
               '"gender": "a", ' \
               '"phone_no": "b", ' \
               '"email": "a", ' \
               '"street": "a", ' \
               '"city": "a", ' \
               '"zip_code": "a", ' \
               '"is_active": "a", ' \
               '"_username": null, ' \
               '"hire_date": "a", ' \
               '"position": "a", ' \
               '"specialty": "a", ' \
               '"location": "a"}}'
    data_saving([doctor1, doctor2])
    with open("doctors_database.json", "r") as file:
        result = file.read()
        assert(expected == result)


def test_save_patient(patient1):
    expected = '{"3": {' \
               '"user_idx": 3, ' \
               '"first_name": "Patient", ' \
               '"last_name": "Quinn", ' \
               '"password": "a", ' \
               '"pesel": "b", ' \
               '"gender": "a", ' \
               '"phone_no": "b", ' \
               '"email": "a", ' \
               '"street": "a", ' \
               '"city": "a", ' \
               '"zip_code": "a", ' \
               '"is_active": "a", ' \
               '"_username": null, ' \
               '"package": "a"}}'
    data_saving([patient1])
    with open("patient_database.json", "r") as file:
        result = file.read()
        assert(expected == result)


def test_save_receptionist(receptionist1):
    expected = '{"4": {' \
               '"user_idx": 4, ' \
               '"first_name": "Receptionist", ' \
               '"last_name": "Quinn", ' \
               '"password": "a", ' \
               '"pesel": "b", ' \
               '"gender": "a", ' \
               '"phone_no": "b", ' \
               '"email": "a", ' \
               '"street": "a", ' \
               '"city": "a", ' \
               '"zip_code": "a", ' \
               '"is_active": "a", ' \
               '"_username": null, ' \
               '"hire_date": "a", ' \
               '"position": "a"}}'
    data_saving([receptionist1])
    with open("receptionist_datebase.json", "r") as file:
        result = file.read()
        assert(expected == result)

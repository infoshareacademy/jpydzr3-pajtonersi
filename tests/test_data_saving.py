from database_dict_JSON import data_saving
from users.user_classes.class_doctor import Doctor
from users.user_classes.class_patient import Patient
from users.user_classes.class_receptionist import Receptionist



def test_save_doctor():
    doc1 = Doctor('Doctor', 'Quinn', 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
    doc2 = Doctor('Doctor', 'Quinn', 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
    expected = '{"1": {"user_idx": 1, "first_name": "Doctor", "last_name": "Quinn", "password": "a", "pesel": "b", "gender": "a", "phone_no": "b", "email": "a", "street": "a", "city": "a", "zip_code": "a", "is_active": "a", "_username": null, "hire_date": "a", "position": "a", "specialty": "a", "location": "a"}, "2": {"user_idx": 2, "first_name": "Doctor", "last_name": "Quinn", "password": "a", "pesel": "b", "gender": "a", "phone_no": "b", "email": "a", "street": "a", "city": "a", "zip_code": "a", "is_active": "a", "_username": null, "hire_date": "a", "position": "a", "specialty": "a", "location": "a"}}'
    data_saving([doc1, doc2])
    with open("doctors_database.json", "r") as file:
        result = file.read()
        assert(expected == result)

def test_save_patient():
    patient = Patient('Patient', 'Quinn', 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a',)
    expected = '{"3": {"user_idx": 3, "first_name": "Patient", "last_name": "Quinn", "password": "a", "pesel": "b", "gender": "a", "phone_no": "b", "email": "a", "street": "a", "city": "a", "zip_code": "a", "is_active": "a", "_username": null, "package": "a"}}'
    data_saving([patient])
    with open("patient_database.json", "r") as file:
        result = file.read()
        assert(expected == result)


def test_save_receptionist():
    receptionist = Receptionist('Receptionist', 'Quinn', 'a', 'b', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
    expected = '{"4": {"user_idx": 4, "first_name": "Receptionist", "last_name": "Quinn", "password": "a", "pesel": "b", "gender": "a", "phone_no": "b", "email": "a", "street": "a", "city": "a", "zip_code": "a", "is_active": "a", "_username": null, "hire_date": "a", "position": "a"}}'
    data_saving([receptionist])
    with open("receptionist_datebase.json", "r") as file:
        result = file.read()
        assert(expected == result)



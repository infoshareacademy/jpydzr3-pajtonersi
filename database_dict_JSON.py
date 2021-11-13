import json
from users.user_classes.class_doctor import Doctor
from users.user_classes.class_patient import Patient
from users.user_classes.class_receptionist import Receptionist
from typing import List


def data_saving(data_for_saving: List) -> None:
    if isinstance(data_for_saving[0], Doctor):
        file_name = 'doctors_database.json'
    elif isinstance(data_for_saving[0], Patient):
        file_name = 'patient_database.json'
    elif isinstance(data_for_saving[0], Receptionist):
        file_name = 'receptionist_datebase.json'

    formatted_values = dict()
    for idx in range(len(data_for_saving)):
        formatted_values[data_for_saving[idx].user_idx] = vars(data_for_saving[idx])

    with open(file_name, 'w') as database_file:
        json.dump(formatted_values, database_file)

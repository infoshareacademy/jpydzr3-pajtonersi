import pytest
from users.user_classes.class_doctor import Doctor
from users.user_classes.class_patient import Patient
from users.user_classes.class_receptionist import Receptionist

@pytest.fixture
def doctor1():
    doc1 = Doctor('Doctor',
                  'Quinn',
                  'a',
                  'b',
                  'a',
                  'b',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a'
                )
    return doc1

@pytest.fixture
def doctor2():
    doc2 = Doctor('Doctor',
                  'Quinn',
                  'a',
                  'b',
                  'a',
                  'b',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a',
                  'a'
                )
    return doc2

@pytest.fixture
def patient1():
    pat1 = Patient('Patient',
                    'Quinn',
                    'a',
                    'b',
                    'a',
                    'b',
                    'a',
                    'a',
                    'a',
                    'a',
                    'a',
                    'a'
                )
    return pat1

@pytest.fixture
def receptionist1():
    rec1 = Receptionist('Receptionist',
                        'Quinn',
                        'a',
                        'b',
                        'a',
                        'b',
                        'a',
                        'a',
                        'a',
                        'a',
                        'a',
                        'a',
                        'a'
                    )
    return rec1
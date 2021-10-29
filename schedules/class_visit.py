class Visit:
    def __init__(
            self,
            date,
            time,
            patient: object,
            doctor: object):
        self.date = date
        self.time = time
        self.patient = patient
        self.doctor = doctor

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
        self._notes = None

    @property
    def notes(self) -> str:
        if self.notes:
            return self._notes

    @notes.setter
    def notes(self, value) -> None:
        self._notes = value

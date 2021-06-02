from core.Model import Model
from pubsub import pub


class PersonsModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "person"

    def is_email_exist(self, email: str):
        result = self.db.select_one(self.table, email=email)
        if result is not None:
            return True
        return False

    def get_person_by_email_and_password(self, email: str, password: str):
        return self.db.select_one(self.table, email=email, password=password)

    def add_person(self, email, password, role):
        return self.db.insert_one(self.table, email=email, password=password, role=role)


if __name__ == '__main__':
    person = PersonsModel()
    print(person.get_person_by_email_and_password("admin@aplikasiwisata", "admin"))

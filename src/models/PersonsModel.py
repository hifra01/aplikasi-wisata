from core.Model import Model


class PersonsModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "person"

    def get_person_by_email(self, email: str):
        return self.db.select_one(self.table, email=email)

    def add_person(self, email, password, role):
        return self.db.insert_one(self.table, email=email, password=password, role=role)


if __name__ == '__main__':
    person = PersonsModel()
    print(person.get_person_by_email("admin@aplikasiwisata"))

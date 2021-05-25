from core.Model import Model


class PersonsModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "person"

    def get_user_by_email(self, email: str):
        return self.db.select_one(self.table, email=email)


if __name__ == '__main__':
    person = PersonsModel()
    print(person.get_user_by_email("admin@aplikasiwisata"))

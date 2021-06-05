from core.Model import Model


class AdminsModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "admin"

    def get_admin_by_person_id(self, person_id):
        return self.db.select_one(self.table, person_id=person_id)

    def add_admin(self, person_id, nama):
        return self.db.insert_one(self.table, person_id=person_id, nama=nama)

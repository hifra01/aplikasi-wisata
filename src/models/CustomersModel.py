from core.Model import Model


class CustomersModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "customers"

    def get_customer_by_person_id(self, person_id):
        return self.db.select_one(self.table, person_id=person_id)

    def add_customer(self, person_id, nama_lengkap, no_ktp, no_hp):
        return self.db.insert_one(self.table, person_id=person_id, nama_lengkap=nama_lengkap, no_ktp=no_ktp,
                                  no_hp=no_hp)

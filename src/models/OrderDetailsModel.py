from core.Model import Model


class OrderDetailsModel(Model):
    def __init__(self):
        super().__init__()
        self.table = 'order_detail'

    def insert_order_detail(self, data):
        result = None
        for person in data['daftar_peserta']:
            result = self.db.insert_one(
                self.table,
                order_id=data['order_id'],
                nama_peserta=person['nama_peserta'],
                no_ktp=person['no_ktp']
            )

        return result

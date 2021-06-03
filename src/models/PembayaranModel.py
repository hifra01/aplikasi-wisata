from core.Model import Model


class PembayaranModel(Model):
    def __init__(self):
        super().__init__()
        self.table = 'pembayaran'

    def insert_new_payment(self, data):
        result = self.db.insert_one(
            self.table,
            order_id=data['order_id'],
            kode_bukti=data['kode_bukti']
        )
        return result

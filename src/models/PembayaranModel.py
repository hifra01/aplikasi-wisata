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

    def update_payment_status(self, status, pembayaran_id, admin_id):
        result = self.db.update_one(
            self.table,
            id=pembayaran_id,
            status_verifikasi=status,
            petugas_verifikasi=admin_id
        )
        return result

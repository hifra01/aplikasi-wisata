from core.Model import Model


class OrdersModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "order"

    def get_customer_order_history(self, customer_id):
        statement = "SELECT o.id as id, o.kode_booking as kode_booking, " \
                    "pw.nama as nama_paket, oss.keterangan as status " \
                    "FROM `order` o " \
                    "JOIN order_status_string oss on oss.id_status_order = o.id_status_order " \
                    "JOIN paket_wisata pw on pw.id = o.id_paket_wisata " \
                    "WHERE o.customer=:customer_id"
        where_filter = dict()
        where_filter['customer_id'] = customer_id
        result = self.db.query(statement, **where_filter)
        if result:
            return result
        return None

    def get_order_detail(self, order_id):
        order_query = "SELECT o.id, o.kode_booking, oss.keterangan,o.id_paket_wisata, " \
                      "pw.nama as paket_wisata, o.tanggal_berangkat, o.tanggal_pulang " \
                      "FROM `order` o JOIN paket_wisata pw on pw.id = o.id_paket_wisata " \
                      "JOIN order_status_string oss on oss.id_status_order = o.id_status_order " \
                      "WHERE o.id=:order_id "
        order_filter = dict()
        order_filter['order_id'] = order_id
        order_result = self.db.query(order_query, **order_filter)
        if order_result:
            order_data = order_result[0]
            data = dict()
            data['kode_booking'] = order_data['kode_booking']
            data['paket_wisata'] = order_data['paket_wisata']
            data['status'] = order_data['keterangan']
            data['tanggal_berangkat'] = order_data['tanggal_berangkat']
            data['tanggal_pulang'] = order_data['tanggal_pulang']

            tempat_wisata_query = "SELECT dw.nama_tempat FROM destinasi_dalam_paket ddp " \
                                  "JOIN paket_wisata pw ON pw.id = ddp.paket " \
                                  "JOIN destinasi_wisata dw ON dw.id = ddp.destinasi " \
                                  "where pw.id=:id_paket"
            tempat_wisata_filter = dict()
            tempat_wisata_filter['id_paket'] = order_data['id_paket_wisata']
            tempat_wisata_result = self.db.query(tempat_wisata_query, **tempat_wisata_filter)

            data['destinasi_wisata'] = tempat_wisata_result

            peserta_wisata_query = "SELECT nama_peserta, no_ktp FROM order_detail WHERE order_id=:order_id"
            peserta_wisata_filter = dict()
            peserta_wisata_filter['order_id'] = order_id
            peserta_wisata_result = self.db.query(peserta_wisata_query, **peserta_wisata_filter)

            data['peserta_wisata'] = peserta_wisata_result

            return data

        return None


if __name__ == '__main__':
    om = OrdersModel()
    print(om.get_order_detail(1))
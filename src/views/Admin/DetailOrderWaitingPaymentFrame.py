from views.interfaces_admin import detailVerifikasiPembayaran
from pubsub import pub


class DetailOrderWaitingPaymentFrame(detailVerifikasiPembayaran):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.set_form()

    def set_form(self):
        self.txt_kode_booking.SetValue(str(self.data['kode_booking']))
        self.txt_nama_pelanggan.SetValue(str(self.data['nama_pelanggan']))
        self.txt_no_hp.SetValue(str(self.data['no_hp']))
        self.txt_paket_wisata.SetValue(str(self.data['paket_wisata']))
        self.txt_tanggal_berangkat.SetValue(str(self.data['tanggal_berangkat']))
        self.txt_tanggal_pulang.SetValue(str(self.data['tanggal_pulang']))
        self.txt_status.SetValue(str(self.data['status']))
        if self.data['referensi_pembayaran'] is not None:
            self.txt_referensi_pembayaran.SetValue(str(self.data['referensi_pembayaran']))

        self.set_list_daftar_destinasi(self.data['destinasi_wisata'])
        self.set_list_daftar_peserta(self.data['peserta_wisata'])

    def set_list_daftar_destinasi(self, data):
        self.list_daftar_destinasi.ClearAll()
        self.list_daftar_destinasi.InsertColumn(0, "Destinasi Wisata", width=160)

        index = 0
        for item in data:
            self.list_daftar_destinasi.InsertItem(index, str(item['nama_tempat']))
            index += 1

    def set_list_daftar_peserta(self, data):
        self.list_daftar_peserta.ClearAll()
        self.list_daftar_peserta.InsertColumn(0, "Nama Peserta", width=160)
        self.list_daftar_peserta.InsertColumn(1, "No. KTP", width=160)

        index = 0
        for item in data:
            self.list_daftar_peserta.InsertItem(index, str(item['nama_peserta']))
            self.list_daftar_peserta.SetItem(index, 1, str(item['no_ktp']))
            index += 1

    def btn_back_onclick(self, event):
        self.Destroy()

    def btn_confirm_payment_onclick( self, event ):
        data = dict()
        data['order_id'] = self.data['order_id']
        data['pembayaran_id'] = self.data['pembayaran_id']
        pub.sendMessage("confirm_payment", data=data)

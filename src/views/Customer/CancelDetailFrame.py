from views.interfaces_user import pembatalanDetail
from pubsub import pub


class CancelDetailFrame(pembatalanDetail):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.attach_data_to_view()

    def attach_data_to_view(self):
        self.text_kode_booking.SetValue(str(self.data['kode_booking']))
        self.text_paket_wisata.SetValue(str(self.data['paket_wisata']))
        self.text_tanggal_berangkat.SetValue(self.data['tanggal_berangkat'].strftime("%d-%m-%Y"))
        self.text_tanggal_pulang.SetValue(self.data['tanggal_pulang'].strftime("%d-%m-%Y"))
        self.text_status.SetValue(str(self.data['status']))
        self.set_list_destinasi(self.data['destinasi_wisata'])
        self.set_list_peserta(self.data['peserta_wisata'])

    def set_list_destinasi(self, destinasi):
        self.list_destinasi_wisata.ClearAll()
        self.list_destinasi_wisata.InsertColumn(0, "Destinasi Wisata", width=160)

        index = 0
        for item in destinasi:
            self.list_destinasi_wisata.InsertItem(index, str(item['nama_tempat']))
            index += 1

    def set_list_peserta(self, peserta):
        self.list_peserta.ClearAll()
        self.list_peserta.InsertColumn(0, "Nama Peserta", width=160)
        self.list_peserta.InsertColumn(1, "No. KTP", width=160)

        index = 0
        for item in peserta:
            self.list_peserta.InsertItem(index, str(item['nama_peserta']))
            self.list_peserta.SetItem(index, 1, str(item['no_ktp']))
            index += 1

    def btn_back_onclick(self, event):
        self.Destroy()

    def btn_cancel_order_clicked(self, event):
        pub.sendMessage("cancel_order", order_id=self.data['order_id'])

from views.interfaces_user import bayarPesananDetail
from pubsub import pub


class PaymentFrame(bayarPesananDetail):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.attach_data_to_view()
        self.btn_bayar.Disable()

    def attach_data_to_view(self):
        self.text_kode_booking.SetValue(str(self.data['kode_booking']))
        self.text_paket_wisata.SetValue(str(self.data['paket_wisata']))
        self.text_tanggal_berangkat.SetValue(self.data['tanggal_berangkat'].strftime("%d-%m-%Y"))
        self.text_tanggal_pulang.SetValue(self.data['tanggal_pulang'].strftime("%d-%m-%Y"))
        self.text_status.SetValue(str(self.data['status']))

    def text_kode_referensi_onchange(self, event):
        current_text = self.text_kode_referensi.GetValue()
        if current_text != "":
            return self.btn_bayar.Enable()
        return self.btn_bayar.Disable()

    def btn_bayar_onclick(self, event):
        order_data = dict()
        order_data['kode_bukti'] = str(self.text_kode_referensi.GetValue())
        order_data['order_id'] = self.data['order_id']
        pub.sendMessage("make_payment", data=order_data)

    def btn_back_onclick(self, event):
        self.Destroy()


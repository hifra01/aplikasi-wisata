from views.interfaces_user import menungguPembayaran
from pubsub import pub


class WaitingPaymentFrame(menungguPembayaran):
    order_id_list = []
    selected_index = None

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.render_cells()
        self.selected_index = None

    def render_cells(self):
        self.order_id_list = []
        self.selected_index = None
        self.list_order_waiting_payment.ClearAll()
        self.list_order_waiting_payment.InsertColumn(0, 'Kode Booking', width=100)
        self.list_order_waiting_payment.InsertColumn(1, 'Paket Wisata', width=160)
        self.list_order_waiting_payment.InsertColumn(2, "Status", width=160)

        if self.data:
            index = 0
            for item in self.data:
                self.list_order_waiting_payment.InsertItem(index, str(item['kode_booking']))
                self.list_order_waiting_payment.SetItem(index, 1, str(item['nama_paket']))
                self.list_order_waiting_payment.SetItem(index, 2, str(item['status']))
                self.order_id_list.append(item['id'])
                index += 1

        self.btn_order_detail.Disable()

    def list_order_waiting_payment_on_list_selected(self, event):
        self.selected_index = event.GetIndex()
        self.btn_order_detail.Enable()

    def list_order_waiting_payment_on_list_deselected(self, event):
        self.btn_order_detail.Disable()
        self.selected_index = None

    def btn_back_onclick(self, event):
        self.Destroy()

    def btn_order_detail_onclick(self, event):
        pub.sendMessage("btn_payment_detail_clicked", order_id=self.order_id_list[self.selected_index], parent=self)

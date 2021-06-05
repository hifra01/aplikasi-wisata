from views.interfaces_admin import listVerifikasiPembayaran
from pubsub import pub


class ListOrderWaitingPaymentFrame(listVerifikasiPembayaran):
    order_id_list = []
    selected_index = None

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.render_list()
        self.btn_detail.Disable()

        pub.subscribe(self.refresh_list, "refresh_waiting_payment_list")

    def refresh_list(self, data):
        self.data = data
        self.render_list()

    def render_list(self):
        self.list_orders.ClearAll()
        self.order_id_list = []
        self.selected_index = None
        self.list_orders.InsertColumn(0, "Kode Booking", width=100)
        self.list_orders.InsertColumn(1, "Paket Wisata", width=160)
        self.list_orders.InsertColumn(2, "Status", width=160)
        self.list_orders.InsertColumn(3, "Nama Pelanggan", width=160)

        if self.data:
            index = 0
            for item in self.data:
                self.list_orders.InsertItem(index, str(item['kode_booking']))
                self.list_orders.SetItem(index, 1, str(item['nama_paket']))
                self.list_orders.SetItem(index, 2, str(item['status']))
                self.list_orders.SetItem(index, 3, str(item['nama_lengkap']))
                self.order_id_list.append(item['id'])

        self.btn_detail.Disable()

    def list_orders_selected(self, event):
        self.selected_index = event.GetIndex()
        self.btn_detail.Enable()

    def list_orders_deselected(self, event):
        self.selected_index = None
        self.btn_detail.Disable()

    def btn_back_onclick(self, event):
        self.Destroy()

    def btn_search_onclick(self, event):
        search = self.text_search.GetValue()
        pub.sendMessage("search_order_waiting_payment", search=search)
        pass

    def btn_detail_onclick(self, event):
        pub.sendMessage("show_detail_confirm_payment", order_id=self.order_id_list[self.selected_index], parent=self)
        pass

from views.interfaces_user import riwayatPesanan
from pubsub import pub


class OrderHistoryFrame(riwayatPesanan):
    order_id_list = []

    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.render_cells()
        self.selected_index = None

    def render_cells(self):
        self.order_id_list = []
        self.selected_index = None
        self.list_order_history.ClearAll()
        self.list_order_history.InsertColumn(0, 'Kode Booking', width=100)
        self.list_order_history.InsertColumn(1, 'Paket Wisata', width=160)
        self.list_order_history.InsertColumn(2, "Status", width=160)

        index = 0
        for item in self.data:
            self.list_order_history.InsertItem(index, str(item['kode_booking']))
            self.list_order_history.SetItem(index, 1, str(item['nama_paket']))
            self.list_order_history.SetItem(index, 2, str(item['status']))
            self.order_id_list.append(item['id'])
            index += 1

        self.btn_order_detail.Disable()

    def btn_back_onclick(self, event):
        self.Destroy()

    def list_order_history_on_item_selected(self, event):
        self.btn_order_detail.Enable()
        self.selected_index = event.GetIndex()

    def list_order_history_on_item_deselected(self, event):
        self.btn_order_detail.Disable()
        self.selected_index = None

    def btn_order_detail_onclick(self, event):
        pub.sendMessage("btn_order_detail_clicked", order_id=self.order_id_list[self.selected_index], parent=self)

from core.Controller import Controller
from views.Customer.HomeFrame import HomeFrame
from views.Customer.MakeOrderFrame import MakeOrderFrame
from views.Customer.WaitingPaymentFrame import WaitingPaymentFrame
from views.Customer.CancelListFrame import CancelListFrame
from pubsub import pub
from models.OrdersModel import OrdersModel
from models.PaketWisataModel import PaketWisataModel
from models.OrderDetailsModel import OrderDetailsModel
from models.PembayaranModel import PembayaranModel
from datetime import timedelta
import wx


class CustomerController(Controller):
    make_order_view = None
    waiting_payment_view = None
    payment_frame = None
    cancel_list_view = None
    cancel_detail_view = None

    def __init__(self, session):
        super().__init__(session)

        self.view = HomeFrame(parent=None)
        self.view.Show()

        self.orders_model = OrdersModel()
        self.paket_wisata_model = PaketWisataModel()
        self.order_details_model = OrderDetailsModel()
        self.pembayaran_model = PembayaranModel()

        self.daftar_paket_wisata = self.paket_wisata_model.get_all_paket_wisata()

        pub.subscribe(self.logout, "btn_logout_clicked")
        pub.subscribe(self.order_history, "btn_order_history_clicked")
        pub.subscribe(self.see_order_detail, "btn_order_detail_clicked")
        pub.subscribe(self.make_order, "btn_order_now_clicked")
        pub.subscribe(self.make_new_order, "make_new_order_clicked")
        pub.subscribe(self.show_waiting_payment, "btn_confirm_payment_clicked")
        pub.subscribe(self.see_waiting_payment_detail, "btn_payment_detail_clicked")
        pub.subscribe(self.pay_order, "make_payment")
        pub.subscribe(self.show_cancel_order_list, "btn_cancel_order_clicked")
        pub.subscribe(self.show_cancel_order_detail, "btn_cancel_detail_clicked")
        pub.subscribe(self.cancel_order, "cancel_order")

    def generate_booking_code(self, id_paket_wisata):
        id_kota = self.paket_wisata_model.get_city_id_from_paket_wisata(id_paket_wisata)
        new_id = self.orders_model.get_next_auto_increment()
        new_booking_code = str(id_kota) + str(id_paket_wisata) + str(new_id).zfill(5)
        return new_booking_code

    def make_new_order(self, order_data):
        new_order_data = order_data
        durasi = self.paket_wisata_model.get_paket_wisata_duration(new_order_data['id_paket_wisata'])
        new_order_data['tanggal_pulang'] = new_order_data['tanggal_berangkat'] + timedelta(days=int(durasi))
        new_order_data['kode_booking'] = self.generate_booking_code(new_order_data['id_paket_wisata'])
        new_order_data['customer_id'] = self.session['customer_id']
        new_order_data['order_id'] = self.orders_model.insert_new_order(new_order_data)
        add_person = self.order_details_model.insert_order_detail(order_data)
        if add_person:
            wx.MessageBox(f"Sukses! Kode Booking: {new_order_data['kode_booking']}", "Sukses")
            return self.make_order_view.Destroy()
        return wx.MessageBox("Error!", "Error!", wx.OK | wx.ICON_ERROR)

    def logout(self):
        pub.sendMessage("change_controller")

    def order_history(self):
        orders = self.orders_model.get_customer_order_history(self.session['customer_id'])
        if orders:
            from views.Customer.OrderHistoryFrame import OrderHistoryFrame
            history_view = OrderHistoryFrame(orders, parent=self.view)
            history_view.Show()

    def see_order_detail(self, order_id, parent=None):
        data = self.orders_model.get_order_detail(order_id)
        if data:
            from views.Customer.OrderDetailFrame import OrderDetailFrame
            order_detail_frame = OrderDetailFrame(data, parent=parent)
            order_detail_frame.Show()
        pass

    def make_order(self):
        self.make_order_view = MakeOrderFrame(self.daftar_paket_wisata, parent=self.view)
        self.make_order_view.Show()

    def show_waiting_payment(self):
        orders = self.orders_model.get_customer_order_awaiting_payment(self.session['customer_id'])
        self.waiting_payment_view = WaitingPaymentFrame(orders, self.view)
        self.waiting_payment_view.Show()

    def see_waiting_payment_detail(self, order_id, parent=None):
        data = self.orders_model.get_awaiting_payment_detail(order_id)
        if data:
            from views.Customer.PaymentFrame import PaymentFrame
            self.payment_frame = PaymentFrame(data, parent)
            self.payment_frame.Show()

    def pay_order(self, data):
        result = self.pembayaran_model.insert_new_payment(data)
        if result:
            self.orders_model.update_order_status(data['order_id'], 'menunggu_verifikasi')
            wx.MessageBox("Pembayaran Sukses. Silakan menunggu verifikasi dari admin.", "Pembayaran sukses!")
            data = self.orders_model.get_customer_order_awaiting_payment(self.session['customer_id'])
            self.waiting_payment_view.data = data
            self.waiting_payment_view.render_cells()
            return self.payment_frame.Destroy()
        return wx.MessageBox("Ada kesalahan!", "Error", wx.OK | wx.ICON_ERROR)

    def show_cancel_order_list(self):
        data = self.orders_model.get_order_can_cancel(self.session['customer_id'])
        self.cancel_list_view = CancelListFrame(data, self.view)
        self.cancel_list_view.Show()

    def show_cancel_order_detail(self, order_id, parent=None):
        data = self.orders_model.get_order_detail(order_id)
        if data:
            from views.Customer.CancelDetailFrame import CancelDetailFrame
            self.cancel_detail_view = CancelDetailFrame(data, parent)
            self.cancel_detail_view.Show()

    def cancel_order(self, order_id):
        result = self.orders_model.update_order_status(
            order_id=order_id,
            status='menunggu_pembatalan'
        )
        if result:
            wx.MessageBox("Pengajuan Pembatalan Sukses. Silakan menunggu verifikasi dari admin.", "Pembayaran sukses!")
            data = self.orders_model.get_order_can_cancel(self.session['customer_id'])
            self.cancel_list_view.data = data
            self.cancel_list_view.render_cells()
            return self.cancel_detail_view.Destroy()
        return wx.MessageBox("Ada kesalahan!", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == '__main__':
    session = dict()
    session['customer_id'] = 1
    c = CustomerController(session)
    c.cancel_order(1)

from core.Controller import Controller
from views.Admin.HomeFrame import HomeFrame
from views.Admin.ListOrderWaitingPaymentFrame import ListOrderWaitingPaymentFrame
from views.Admin.DetailOrderWaitingPaymentFrame import DetailOrderWaitingPaymentFrame
from views.Admin.ListOrderWaitingCancelFrame import ListOrderWaitingCancelFrame
from views.Admin.DetailOrderWaitingCancelFrame import DetailOrderWaitingCancelFrame
from views.Admin.ListAllOrderFrame import ListAllOrderFrame
from views.Admin.DetailOrderFrame import DetailOrderFrame
from views.Admin.AddAdminFrame import AddAdminFrame
from models.OrdersModel import OrdersModel
from models.PembayaranModel import PembayaranModel
from models.PersonsModel import PersonsModel
from models.AdminsModel import AdminsModel
from pubsub import pub
import wx
import re


class AdminController(Controller):
    list_waiting_payment_view = None
    detail_waiting_payment_view = None
    list_waiting_cancel_view = None
    detail_waiting_cancel_view = None
    list_all_order_view = None
    detail_all_order_view = None
    add_admin_view = None

    def __init__(self, session):
        super().__init__(session)
        self.view = HomeFrame()
        self.orders_model = OrdersModel()
        self.pembayaran_model = PembayaranModel()
        self.persons_model = PersonsModel()
        self.admins_model = AdminsModel()
        self.view.Show()

        pub.subscribe(self.show_order_waiting_payment_verification, "btn_order_waiting_payment_verification_clicked")
        pub.subscribe(self.show_order_waiting_cancel_verification, "btn_order_waiting_cancel_verification_clicked")
        pub.subscribe(self.show_all_order, "btn_all_order_clicked")
        pub.subscribe(self.show_add_admin, "btn_add_admin_clicked")
        pub.subscribe(self.logout, "btn_logout_clicked")
        pub.subscribe(self.search_order_waiting_payment, "search_order_waiting_payment")
        pub.subscribe(self.show_detail_confirm_payment, "show_detail_confirm_payment")
        pub.subscribe(self.search_order_waiting_cancel, "search_order_waiting_cancel")
        pub.subscribe(self.show_detail_confirm_cancel, "show_detail_confirm_cancel")
        pub.subscribe(self.search_all_order, "search_all_order")
        pub.subscribe(self.show_detail_order, "show_order_detail")
        pub.subscribe(self.confirm_payment, "confirm_payment")
        pub.subscribe(self.cancel_order, "cancel_order")
        pub.subscribe(self.validate_add_admin, "add_admin")

    def show_order_waiting_payment_verification(self):
        data = self.orders_model.get_orders_waiting_payment_verification()
        self.list_waiting_payment_view = ListOrderWaitingPaymentFrame(data, self.view)
        self.list_waiting_payment_view.Show()
        pass

    def show_detail_confirm_payment(self, order_id, parent):
        data = self.orders_model.get_order_detail(order_id)
        self.detail_waiting_payment_view = DetailOrderWaitingPaymentFrame(data, parent)
        self.detail_waiting_payment_view.Show()

    def search_order_waiting_payment(self, search):
        data = self.orders_model.get_orders_waiting_payment_verification(search)
        pub.sendMessage('refresh_waiting_payment_list', data=data)

    def show_order_waiting_cancel_verification(self):
        data = self.orders_model.get_orders_waiting_cancel_verification()
        self.list_waiting_cancel_view = ListOrderWaitingCancelFrame(data, self.view)
        self.list_waiting_cancel_view.Show()
        pass

    def show_detail_confirm_cancel(self, order_id, parent):
        data = self.orders_model.get_order_detail(order_id)
        self.detail_waiting_cancel_view = DetailOrderWaitingCancelFrame(data, parent)
        self.detail_waiting_cancel_view.Show()

    def search_order_waiting_cancel(self, search):
        data = self.orders_model.get_orders_waiting_cancel_verification(search)
        pub.sendMessage('refresh_waiting_payment_list', data=data)

    def show_all_order(self):
        data = self.orders_model.get_all_orders()
        self.list_all_order_view = ListAllOrderFrame(data, self.view)
        self.list_all_order_view.Show()

    def show_detail_order(self, order_id, parent):
        data = self.orders_model.get_order_detail(order_id)
        self.detail_all_order_view = DetailOrderFrame(data, parent)
        self.detail_all_order_view.Show()

    def search_all_order(self, search):
        data = self.orders_model.get_all_orders(search)
        pub.sendMessage('refresh_all_order_list', data=data)

    def show_add_admin(self):
        self.add_admin_view = AddAdminFrame(self.view)
        self.add_admin_view.Show()

    def logout(self):
        pub.sendMessage("change_controller")

    def confirm_payment(self, data):
        pembayaran_update = self.pembayaran_model.update_payment_status(
            status='telah_verifikasi',
            pembayaran_id=data['pembayaran_id'],
            admin_id=self.session['admin_id']
        )
        order_update = self.orders_model.update_order_status(
            order_id=data['order_id'],
            status='terbayar'
        )
        if pembayaran_update and order_update:
            wx.MessageBox("Verifikasi Pembayaran berhasil!")
            self.detail_waiting_payment_view.Destroy()
            return self.search_order_waiting_payment("")
        return wx.MessageBox("Ada kesalahan!")

    def cancel_order(self, data):
        order_update = self.orders_model.update_order_status(
            order_id=data['order_id'],
            status='dibatalkan'
        )
        if order_update:
            wx.MessageBox("Konfirmasi Pembatalan berhasil!")
            self.detail_waiting_cancel_view.Destroy()
            return self.search_order_waiting_cancel("")
        return wx.MessageBox("Ada kesalahan!")

    def _validate_email(self, email):
        # return True if s is a valid email, else return False
        pattern = r'^[\w-]+@[\w-]+\.[a-z]+$'
        m = re.match(pattern, email)
        if m:
            return True
        else:
            return False

    def validate_add_admin(self, data):
        for key in data.keys():
            if data[key] == "":
                return wx.MessageBox("Harap isi semua kolom!")
        if not self._validate_email(data['email']):
            return wx.MessageBox("Email tidak valid!")
        if data['password'] != data['confirm_password']:
            return wx.MessageBox("Password dan Konfirmasi password tidak sama!")
        if self.persons_model.is_email_exist(data['email']):
            return wx.MessageBox("Email sudah pernah digunakan!")
        self.add_admin(data)

    def add_admin(self, data):
        person_id = self.persons_model.add_person(
            email=data['email'],
            password=data['password'],
            role='admin'
        )
        if person_id:
            admin_id = self.admins_model.add_admin(
                person_id=person_id,
                nama=data['nama']
            )
            if admin_id:
                wx.MessageBox("Pendaftaran Admin Berhasil!")
                return self.add_admin_view.Destroy()

        return wx.MessageBox("Ada Kesalahan!")

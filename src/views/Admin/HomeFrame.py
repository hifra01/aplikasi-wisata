from views.interfaces_admin import beranda
from pubsub import pub


class HomeFrame(beranda):
    def __init__(self, parent=None):
        super().__init__(parent)

    def btn_order_waiting_payment_verification_onclick(self, event):
        pub.sendMessage("btn_order_waiting_payment_verification_clicked")

    def btn_order_waiting_cancel_verification_onclick(self, event):
        pub.sendMessage("btn_order_waiting_cancel_verification_clicked")

    def btn_all_order_onclick(self, event):
        pub.sendMessage("btn_all_order_clicked")

    def btn_add_admin_onclick(self, event):
        pub.sendMessage("btn_add_admin_clicked")

    def btn_logout_onclick(self, event):
        pub.sendMessage("btn_logout_clicked")

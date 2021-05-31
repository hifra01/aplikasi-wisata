from views.interfaces_user import beranda
from pubsub import pub


class HomeFrame(beranda):
    def __init__(self, parent):
        super().__init__(parent)

    def btn_logout_onclick(self, event):
        pub.sendMessage("btn_logout_clicked")

    def btn_cancel_order_onclick(self, event):
        pub.sendMessage("btn_cancel_order_clicked")
        pass

    def btn_confirm_payment_onclick(self, event):
        pub.sendMessage("btn_confirm_payment_clicked")
        pass

    def btn_order_history_onclick(self, event):
        pub.sendMessage("btn_order_history_clicked")
        pass

    def btn_order_now_onclick(self, event):
        pub.sendMessage("btn_order_now_clicked")
        pass

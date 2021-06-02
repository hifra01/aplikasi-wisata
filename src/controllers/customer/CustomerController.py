from core.Controller import Controller
from views.Customer.HomeFrame import HomeFrame
from pubsub import pub
from models.OrdersModel import OrdersModel
import wx


class CustomerController(Controller):
    def __init__(self, session):
        super().__init__(session)
        self.view = HomeFrame(parent=None)
        self.view.Show()
        self.orders_model = OrdersModel()
        pub.subscribe(self.logout, "btn_logout_clicked")
        pub.subscribe(self.order_history, "btn_order_history_clicked")
        pub.subscribe(self.see_order_detail, "btn_order_detail_clicked")

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

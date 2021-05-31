from core.Controller import Controller
from views.Customer.HomeFrame import HomeFrame
from pubsub import pub
import wx


class CustomerController(Controller):
    def __init__(self, session):
        super().__init__(session)
        self.view = HomeFrame(parent=None)
        self.view.Show()
        pub.subscribe(self.logout, "btn_logout_clicked")

    def logout(self):
        pub.sendMessage("change_controller")

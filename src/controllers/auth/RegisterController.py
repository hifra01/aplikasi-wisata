from core.Controller import Controller
from views.Customer.RegisterFrame import RegisterFrame
from pubsub import pub
import wx


class RegisterController(Controller):
    def __init__(self, session=None):
        super().__init__(session)
        self.view = RegisterFrame()
        self.view.Show()
        pub.subscribe(self.go_to_login, "btn_go_to_login_clicked")

    def go_to_login(self):
        pub.sendMessage("change_controller")

    def validate_registration(self, data: dict):
        for key in data.keys():
            if data[key] == "":
                return wx.MessageBox("Harap isi semua kolom!")
        if data['password'] != data['confirm_password']:
            return wx.MessageBox("Password dan Konfirmasi password tidak sama!")

    def register(self, data: dict):
        registration_data = data
        registration_data['role'] = 'customer'
#       TODO: import personmodel, customermodel, and add customer

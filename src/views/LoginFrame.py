from views.interfaces_user import loginFrame
from pubsub import pub


class LoginFrame(loginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def btn_login_onclick(self, event):
        email = self.text_email.GetValue()
        password = self.text_password.GetValue()
        pub.sendMessage("btn_login_clicked", email=email, password=password)

    def btn_go_to_register_onclick(self, event):
        pub.sendMessage("btn_go_to_register_clicked")

from views.interfaces_user import daftarForm
from pubsub import pub


class RegisterFrame(daftarForm):
    def __init__(self, parent=None):
        super().__init__(parent)

    def btn_register_onclick(self, event):
        data = dict()
        data['full_name'] = self.text_fullname.GetValue()
        data['no_ktp'] = self.text_noktp.GetValue()
        data['no_hp'] = self.text_nohp.GetValue()
        data['email'] = self.text_email.GetValue()
        data['password'] = self.text_password.GetValue()
        data['confirm_password'] = self.text_confirm_password.GetValue()


    def btn_go_to_login_onclick(self, event):
        pub.sendMessage("btn_go_to_login_clicked")

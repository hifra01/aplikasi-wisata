from views.interfaces_admin import daftarAdminBaru
from pubsub import pub


class AddAdminFrame(daftarAdminBaru):
    def __init__(self, parent=None):
        super().__init__(parent)

    def btn_register_admin_onclick(self, event):
        data = dict()
        data['nama'] = self.text_name.GetValue()
        data['email'] = self.text_email.GetValue()
        data['password'] = self.text_password.GetValue()
        data['confirm_password'] = self.text_confirm_password.GetValue()
        pub.sendMessage("add_admin", data=data)

    def btn_back_onclick(self, event):
        return self.Destroy()

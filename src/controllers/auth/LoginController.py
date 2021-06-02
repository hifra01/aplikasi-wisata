from models.PersonsModel import PersonsModel
from core.Controller import Controller
from views.LoginFrame import LoginFrame
from pubsub import pub
import wx


class LoginController(Controller):
    def __init__(self, session=None, parent=None):
        super().__init__(session)
        self.model: PersonsModel = PersonsModel()
        self.view = LoginFrame(parent=parent)
        self.view.Show()
        pub.subscribe(self.authenticate, "btn_login_clicked")
        pub.subscribe(self.go_to_register, "btn_go_to_register_clicked")

    def authenticate(self, email: str, password: str):
        person = self.model.get_person_by_email_and_password(email, password)
        if person is not None:
            self.session['person_id'] = person['id']
            if person['role'] == 'customer':
                from controllers.customer.CustomerController import CustomerController
                from models.CustomersModel import CustomersModel
                customer_model = CustomersModel()
                customer = customer_model.get_customer_by_person_id(self.session['person_id'])
                self.session['customer_id'] = customer['id']
                self.session['customer_name'] = customer['nama_lengkap']
                pub.sendMessage("change_controller", controller=CustomerController, session=self.session)
        else:
            wx.MessageBox("Login Gagal!")

    def go_to_register(self):
        from controllers.auth.RegisterController import RegisterController
        pub.sendMessage("change_controller", controller=RegisterController)


if __name__ == '__main__':
    con = LoginController()
    con.authenticate("admin@aplikasiwisata", "ADMIN")

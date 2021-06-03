from core.Controller import Controller
from views.Customer.RegisterFrame import RegisterFrame
from models.PersonsModel import PersonsModel
from pubsub import pub
import wx
import re


class RegisterController(Controller):
    def __init__(self, session=None):
        super().__init__(session)
        self.view = RegisterFrame()
        self.view.Show()
        self.model = PersonsModel()
        pub.subscribe(self.go_to_login, "btn_go_to_login_clicked")
        pub.subscribe(self.validate_registration, "btn_register_clicked")

    def _validate_email(self, email):
        # return True if s is a valid email, else return False
        pattern = r'^[\w-]+@[\w-]+\.[a-z]+$'
        m = re.match(pattern, email)
        if m:
            return True
        else:
            return False

    def go_to_login(self):
        pub.sendMessage("change_controller")

    def validate_registration(self, data: dict):
        for key in data.keys():
            if data[key] == "":
                return wx.MessageBox("Harap isi semua kolom!")
        if not data['no_ktp'].isnumeric() or len(data['no_ktp']) < 16:
            return wx.MessageBox("Nomor KTP harus berupa 16 digit angka!")
        if not data['no_hp'].isnumeric():
            return wx.MessageBox("Nomor HP harus berupa angka!")
        if not self._validate_email(data['email']):
            return wx.MessageBox("Email tidak valid!")
        if data['password'] != data['confirm_password']:
            return wx.MessageBox("Password dan Konfirmasi password tidak sama!")
        if self.model.is_email_exist(data['email']):
            return wx.MessageBox("Email sudah pernah digunakan!")
        self.register(data=data)

    def register(self, data: dict):
        new_person_id = self.model.add_person(
            email=data['email'],
            password=data['password'],
            role='customer'
        )
        from models.CustomersModel import CustomersModel
        customer_model = CustomersModel()
        new_customer_id = customer_model.add_customer(
            person_id=new_person_id,
            nama_lengkap=data['full_name'],
            no_ktp=data['no_ktp'],
            no_hp=data['no_hp']
        )

        if new_customer_id > 0:
            wx.MessageBox("Registrasi Berhasil!")
        else:
            wx.MessageBox("Registrasi Gagal!")

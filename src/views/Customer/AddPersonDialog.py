from views.interfaces_user import PesanTambahOrang
from pubsub import pub
import wx


class AddPersonDialog(PesanTambahOrang):
    def __init__(self, parent=None):
        super().__init__(parent)

    def btn_add_new_person_onclick(self, event):
        data = dict()
        data['nama_peserta'] = self.text_name.GetValue()
        data['no_ktp']: str = self.text_no_ktp.GetValue()
        if data['nama_peserta'] == "" or data['no_ktp'] == "":
            return wx.MessageBox("Harap isi semua kolom!", "Peringatan!", wx.OK | wx.ICON_WARNING)
        if not data['no_ktp'].isnumeric() or len(data['no_ktp']) != 16:
            return wx.MessageBox("Nomor KTP harus berupa 16 digit angka!", "Peringatan!", wx.OK | wx.ICON_WARNING)
        pub.sendMessage("add_new_person", data=data)
        self.Destroy()

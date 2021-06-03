from views.interfaces_user import Pesan
from views.Customer.AddPersonDialog import AddPersonDialog
from pubsub import pub
import wx


class MakeOrderFrame(Pesan):
    paket_wisata_index = []
    daftar_peserta = []
    selected_peserta = None

    def __init__(self, daftar_paket_wisata, parent=None):
        super().__init__(parent)
        self.paket_wisata_choices = daftar_paket_wisata
        self.set_paket_wisata_choices()
        self.btn_delete_person.Disable()
        pub.subscribe(self.add_new_person, "add_new_person")

    def _wxdate2pydate(self, date):
        import datetime
        assert isinstance(date, wx.DateTime)
        if date.IsValid():
            ymd = map(int, date.FormatISODate().split('-'))
            return datetime.date(*ymd)
        else:
            return None

    def add_new_person(self, data):
        self.daftar_peserta.append(data)
        self.set_daftar_peserta()
        print(self.daftar_peserta)

    def set_paket_wisata_choices(self):
        self.combobox_paket_wisata.Clear()
        for paket_wisata in self.paket_wisata_choices:
            self.combobox_paket_wisata.Append(paket_wisata['nama'])
            self.paket_wisata_index.append(paket_wisata['id'])

    def set_daftar_peserta(self):
        self.list_daftar_peserta.ClearAll()
        self.list_daftar_peserta.InsertColumn(0, "Nama", width=160)
        self.list_daftar_peserta.InsertColumn(1, "No. KTP", width=160)

        if self.daftar_peserta:
            index = 0
            for item in self.daftar_peserta:
                self.list_daftar_peserta.InsertItem(index, str(item['nama_peserta']))
                self.list_daftar_peserta.SetItem(index, 1, str(item['no_ktp']))
                index += 1

    def list_daftar_peserta_on_item_selected(self, event):
        self.selected_peserta = event.GetIndex()
        self.btn_delete_person.Enable()

    def list_daftar_peserta_on_item_deselected(self, event):
        self.selected_peserta = None
        self.btn_delete_person.Disable()

    def btn_add_person_onclick(self, event):
        add_person_dialog = AddPersonDialog(parent=self)
        add_person_dialog.ShowModal()

    def btn_delete_person_onclick(self, event):
        print(self.selected_peserta)
        if self.selected_peserta is not None:
            self.daftar_peserta.pop(self.selected_peserta)
            self.set_daftar_peserta()
            print(self.daftar_peserta)
        pass

    def btn_make_order_onclick(self, event):
        choice_paket_wisata = self.combobox_paket_wisata.GetSelection()
        if choice_paket_wisata < 0:
            return wx.MessageBox("Harap pilih salah satu paket wisata!", "Peringatan!", wx.OK | wx.ICON_WARNING)
        if not self.daftar_peserta:
            return wx.MessageBox("Harap tambahkan peserta wisata!", "Peringatan!", wx.OK | wx.ICON_WARNING)
        data = dict()
        data['id_paket_wisata'] = self.paket_wisata_index[choice_paket_wisata]
        data['tanggal_berangkat'] = self._wxdate2pydate(self.calendar_tanggal_berangkat.GetDate())
        data['daftar_peserta'] = self.daftar_peserta
        pub.sendMessage('make_new_order_clicked', order_data=data)

    def btn_back_onclick(self, event):
        self.Destroy()

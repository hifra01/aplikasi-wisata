from core.Model import Model


class PaketWisataModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "paket_wisata"

    def get_all_paket_wisata(self):
        return self.db.select_many(self.table)

    def get_paket_wisata_duration(self, id_paket_wisata):
        result = self.db.select_one(self.table, id=id_paket_wisata)
        return result['durasi']

    def get_city_id_from_paket_wisata(self, paket_wisata):
        result = self.db.select_one(self.table, id=paket_wisata)
        return result['kota'] if result else None


if __name__ == '__main__':
    pw = PaketWisataModel()
    print(pw.get_all_paket_wisata())

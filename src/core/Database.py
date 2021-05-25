import dataset
from sqlalchemy.exc import OperationalError, IntegrityError


class DB:
    __db_user = "root"
    __db_password = ""
    __db_host = "localhost"
    __db_name = "aplikasi-wisata"

    def __init__(self):
        url = f'mysql://{self.__db_user}:{self.__db_password}@{self.__db_host}/{self.__db_name}'
        self._conn = dataset.connect(url)

    def select_one(self, table_name, **column):
        table = self._conn.load_table(table_name)
        row = table.find_one(**column)
        if row is not None:
            return dict(row)
        return None

    def select_all(self, table_name):
        table = self._conn.load_table(table_name)
        rows = table.all()
        if rows is not None:
            return list(map(lambda x: dict(x), rows))
        return None

    def insert_one(self, table_name, **values):
        table = self._conn.load_table(table_name)
        return table.insert(dict(**values))

    def insert_many(self, table_name, *items: dict):
        table = self._conn.load_table(table_name)
        table.insert_many(items)

    def update_one(self, table_name, filter_id, **values):
        pass


if __name__ == '__main__':
    db = DB()
    try:
        print(db.select_one("destinasi_wisata", nama_tempat="Watu Ulo"))
        print(db.select_all("destinasi_wisata"))
    except OperationalError as e:
        print(e)

import dataset
from sqlalchemy.exc import OperationalError


class DB:
    __db_user = "root"
    __db_password = ""
    __db_host = "localhost"
    __db_name = "aplikasi-wisata"

    def __init__(self):
        url = f'mysql://{self.__db_user}:{self.__db_password}@{self.__db_host}/{self.__db_name}'
        self.__conn = dataset.connect(url)

    def select_one(self, table_name, **column):
        table = self.__conn.load_table(table_name)
        row = table.find_one(**column)
        if row is not None:
            return dict(row)
        return None

    def select_many(self, table_name, **column):
        table = self.__conn.load_table(table_name)
        rows = table.all(**column)
        if rows is not None:
            return tuple(rows)
        return None

    def insert_one(self, table_name, **values):
        table = self.__conn.load_table(table_name)
        return table.insert(dict(**values))

    def insert_many(self, table_name, *items: dict):
        table = self.__conn.load_table(table_name)
        table.insert_many(items)

    def update_one(self, table_name, **values):
        if 'id' in values:
            table = self.__conn.load_table(table_name)
            row = table.find_one(id=values['id'])
            if row is not None:
                table.update(values, keys=['id'])

    def delete_one(self, table_name, id):
        table = self.__conn.load_table(table_name)
        row = table.find_one(id=id)
        if row is not None:
            table.delete(id=id)

    def query(self, query: str, **kwargs):
        return tuple(self.__conn.query(query, **kwargs))


if __name__ == '__main__':
    db = DB()
    args = dict()
    args['kota'] = '10'
    print(bool(db.select_many("paket_wisata", kota='10')))

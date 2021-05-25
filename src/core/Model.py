from abc import ABC
from core.Database import DB


class Model(ABC):
    table: str

    def __init__(self):
        self.db = DB()

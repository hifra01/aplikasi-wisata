from abc import ABC


class Controller(ABC):
    view = None
    model = None
    session = dict()
    parent = None

    def __init__(self, session=None):
        if session is None:
            session = dict()
        self.session = session

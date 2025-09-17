from fletx import Xstate
from app.components.appbar import  create_appbar
from app.components.drawer import create_drawer

class GlobalState(Xstate):
    def __init__(self, page):
        super().__init__(page)

        self.create_drawer = create_drawer
        self.create_appbar = create_appbar

        self.to_do_list = []
        self.completed_list = []

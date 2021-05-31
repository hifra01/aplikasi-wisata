import wx
from controllers.auth.LoginController import LoginController
from pubsub import pub


class App:
    def __init__(self):
        pub.subscribe(self.change_controller, "change_controller")
        self.app = wx.App()
        self.controller = LoginController()
        self.app.MainLoop()

    def change_controller(self, controller=LoginController, session=None):
        self.controller.view.Destroy()
        self.controller = controller(session=session)

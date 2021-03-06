from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from util.client import get_students_from_admin_id, authorize
from util.firebase import firebase

class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        authorize()
        self.app.title = "Login"

    def login(self):
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(self.login_email, self.login_password)

        res = get_students_from_admin_id(user['localId'])
        self.manager.screens[0].ids.users = res
        self.manager.current = 'dashboard'

    def process_email(self):
        self.login_email = self.manager.screens[0].ids.email.text

    def process_password(self):
        self.login_password = self.manager.screens[0].ids.password.text

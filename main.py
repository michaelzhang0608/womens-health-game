# Import Libraries
from kivymd.app import MDApp
from kivy.lang import Builder

# Import Screens
from ui.loginscreen import LoginScreen
from ui.dashboard import DashBoard
from ui.settingsscreen import SettingsScreen

# Import Constants
from util.constants import _title_
from util.style import app_style

# Initialize APP
class MyApp(MDApp):

    # Constructor
    def build(self):
        self.title = _title_
        self.theme_cls.primary_palette = app_style["primary_theme"]
        return Builder.load_file("main.kv")

    def settings(self):
    	MDApp.get_running_app().root.ids.screen_manager.current = 'settings_screen'

# Start App
MyApp().run()
import copy
import curses
import npyscreen
from views.view_names import ViewNames
from utils.settings import settings
from models.cyber.cybernetics_base import CyberBase


class EditorPage(npyscreen.FormBaseNew):
    def create(self):
        self.name = f'{settings.app_name}: РЕДАКТОР'
        self.lines = 24
        self.columns = 80

        self.add(
            npyscreen.ButtonPress,
            name='Сохранить',
            rely=-3,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.cybernetics)
        )

        self.add(
            npyscreen.ButtonPress,
            name='Отменить',
            rely=-3, relx=13,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.cybernetics)
        )

        self.add(
            npyscreen.ButtonPress,
            name='Удалить',
            rely=-3, relx=27,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.cybernetics)
        )

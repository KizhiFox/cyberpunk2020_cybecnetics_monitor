import copy
import curses
from dataclasses import dataclass

import npyscreen

from views.view_names import ViewNames
from utils.settings import settings
from models.cyber.cybernetics_base import CyberBase


LIST_BASE = 'Base'


class CyberneticsListEntity(CyberBase):
    def __init__(self, name_in_list: str, add_to: str | None = None, *args, **kwargs):
        self.name_in_list = name_in_list
        self.add_to = add_to
        if add_to:
            pass
        else:
            super(CyberneticsListEntity, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.name_in_list

    def use(self):
        raise Exception


class CyberneticsList(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        super(CyberneticsList, self).__init__(*args, **kwargs)

    def actionHighlighted(self, act_on_this: CyberneticsListEntity, key_press):
        if key_press == curses.ascii.NL:
            act_on_this.use()


class CyberneticsPage(npyscreen.FormBaseNew):
    def pre_edit_loop(self):
        self.editw = 0
        self.temp_user = copy.deepcopy(settings.user)
        self.cybernetics.values = self.get_tree()

    def create(self):
        self.name = f'{settings.app_name}: КИБЕРНЕТИКА'
        self.lines = 24
        self.columns = 80

        self.cybernetics: CyberneticsList = self.add(
            CyberneticsList,
            name='Список кибернетики',
            max_height=17,
            use_two_lines=True,
            begin_entry_at=2
        )

        self.add(
            npyscreen.ButtonPress,
            name='На главную',
            rely=-4,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.main)
        )

    def get_tree(self) -> list[CyberneticsListEntity]:
        tree_data = [CyberneticsListEntity(name_in_list='Добавить...', add_to=LIST_BASE)]
        return tree_data

    def save_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)
        settings.user = self.temp_user
        settings.user.save_to_file()

    def cancel_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

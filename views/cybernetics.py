import copy
import curses
from dataclasses import dataclass

import npyscreen

from views.view_names import ViewNames
from utils.settings import settings
from models.cyber.cybernetics_base import CyberBase
from assets import ascii_arts


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
        self.cybernetics.values = self.get_tree(self.temp_user.cybernetics)

    def create(self):
        self.name = f'{settings.app_name}: КИБЕРНЕТИКА'
        self.lines = 24
        self.columns = 80

        self.cybernetics: CyberneticsList = self.add(
            CyberneticsList,
            name='Список кибернетики',
            max_height=19,
            max_width=40,
            use_two_lines=True,
            begin_entry_at=2
        )

        self.add(
            npyscreen.ButtonPress,
            name='На главную',
            rely=-3,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.main)
        )

        self.add(
            npyscreen.BoxTitle, values=ascii_arts.cog.image, editable=False,
            relx=42, rely=3, max_height=ascii_arts.cog.height, max_width=ascii_arts.cog.width
        )

    def get_tree(self, cybernetics: list[CyberBase], level=0, add_to=LIST_BASE) -> list[CyberneticsListEntity]:
        tree_data = []

        for i, implant in enumerate(cybernetics):
            sockets_counter = ''
            if implant.has_sockets and implant.max_sockets is not None:
                if implant.max_sockets != -1:
                    sockets_used = sum([im.num_sockets_use for im in implant.sockets if im.num_sockets_use is not None])
                    sockets_counter = f' [{sockets_used}/{implant.max_sockets}]'

            tree_data.append(
                CyberneticsListEntity(
                    name_in_list=f'{"│ " * (level - 1)}{"├─" if level else ""}{implant.name}{sockets_counter}',
                    **{k: implant.__dict__[k] for k in implant.__dict__.keys() if k[0] != '_'}
                )
            )

            if implant.has_sockets:
                if isinstance(implant.sockets, list):
                    tree_data += self.get_tree(implant.sockets, level + 1, add_to=implant.id)
                else:
                    tree_data += self.get_tree([], level + 1, add_to=implant.id)

        if level == 0:
            add_button_text = 'ПОДКЛЮЧИТЬ...'
        else:
            add_button_text = f'{"│ " * (level - 1)}└─ПОДКЛЮЧИТЬ...'
        tree_data.append(CyberneticsListEntity(name_in_list=add_button_text, add_to=add_to))

        return tree_data

    def save_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)
        settings.user = self.temp_user
        settings.user.save_to_file()

    def cancel_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

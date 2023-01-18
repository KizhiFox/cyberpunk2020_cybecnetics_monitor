import copy
import curses
import npyscreen
from views.view_names import ViewNames
from utils.settings import settings
from models.cyber.cybernetics_base import CyberBase


LIST_BASE = 'Base'


class CyberneticsListEntity(CyberBase):
    def __init__(self, name_in_list: str, add_to: str | None = None, root_page=None, *args, **kwargs):
        self.name_in_list = name_in_list
        self.add_to = add_to
        self.root_page: CyberneticsPage = root_page  # Link to the page
        if add_to:
            pass
        else:
            super(CyberneticsListEntity, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.name_in_list

    def use(self):
        self.root_page.parentApp.switchForm(ViewNames.editor)

    def get_text_info(self):
        if self.add_to:
            return 'Подключить...'

        text_info = f'{self.name} ({self.code})\n\n' \
                    f'{self.description}\n\n' \
                    f'Стоимость: {self.prise} §\n' \
                    f'Цена человечности: {self.hp}'

        return text_info


class CyberneticsList(npyscreen.MultiLineAction):
    def __init__(self, *args, **kwargs):
        super(CyberneticsList, self).__init__(*args, **kwargs)

    def actionHighlighted(self, act_on_this: CyberneticsListEntity, key_press):
        if key_press == curses.ascii.NL:
            act_on_this.use()

    def update(self, clear=True):
        super(CyberneticsList, self).update(clear)

        # Also update info in left column
        try:
            self.parent.implant_info.value = self.values[self.cursor_line].get_text_info()
            self.parent.implant_info.reformat_preserve_nl()
            self.parent.implant_info.update()

        # Occurs on first run
        except IndexError:
            pass

    # Fix AttributeError: 'CyberneticsListEntity' object has no attribute 'id' by removing "if not force_remake_cache:"
    def get_filtered_indexes(self, force_remake_cache=False):
        self._last_filter = self._filter
        self._last_values = copy.copy(self.values)
        if self._filter == None or self._filter == '':
            return []
        list_of_indexes = []
        for indexer in range(len(self.values)):
            if self.filter_value(indexer):
                list_of_indexes.append(indexer)
        return list_of_indexes


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
            max_width=38,
            use_two_lines=True,
            # begin_entry_at=2,
            scroll_exit=True
        )

        self.add(
            npyscreen.ButtonPress,
            name='На главную',
            rely=-3,
            when_pressed_function=lambda: self.parentApp.switchForm(ViewNames.main)
        )

        # Wrapper
        self.add(npyscreen.BoxTitle, relx=40, rely=1, max_height=21, max_width=37, editable=False)
        self.implant_info = self.add(
            npyscreen.MultiLineEdit, value='',
            relx=41, rely=2, max_height=19, max_width=35, editable=False
        )
        self.implant_info.value = 'test'

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
                    root_page=self,
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
        tree_data.append(CyberneticsListEntity(name_in_list=add_button_text, add_to=add_to, root_page=self))

        return tree_data

    def save_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)
        settings.user = self.temp_user
        settings.user.save_to_file()

    def cancel_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

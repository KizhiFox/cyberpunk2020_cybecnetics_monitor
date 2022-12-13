import copy
import npyscreen

from views.view_names import ViewNames
from utils.settings import settings
from utils.setters import setint


class SettingsPage(npyscreen.FormBaseNew):
    def pre_edit_loop(self):
        self.editw = 0

        self.temp_user = copy.deepcopy(settings.user)

        self.username_field.value = self.temp_user.name
        self.emp_current.value = str(self.temp_user.emp_current)
        self.emp_max.value = str(self.temp_user.emp_max)

    def create(self):
        self.name = f'{settings.app_name}: НАСТРОЙКИ'
        self.lines = 24
        self.columns = 80

        self.username_field = self.add(
            npyscreen.TitleText,
            name='Ваше имя:',
            begin_entry_at=10,
            use_two_lines=False,
            labelColor='WARNING'
        )
        self.username_field.when_value_edited = lambda: setattr(self.temp_user, 'name', self.username_field.value)
        self.add(npyscreen.Textfield, value='', editable=False)

        self.emp_current = self.add(
            npyscreen.TitleText,
            name='Текущая эмпатия:',
            begin_entry_at=17,
            use_two_lines=False,
            labelColor='WARNING'
        )
        self.emp_current.when_value_edited = lambda: setint(self.temp_user, 'emp_current', self.emp_current.value)

        self.emp_max = self.add(
            npyscreen.TitleText,
            name='Макс. эмпатия:',
            begin_entry_at=17,
            use_two_lines=False,
            labelColor='WARNING'
        )
        self.emp_max.when_value_edited = lambda: setint(self.temp_user, 'emp_max', self.emp_max.value)

        self.add(npyscreen.ButtonPress, name='Сохранить', rely=-5, when_pressed_function=self.save_button_pressed)
        self.add(npyscreen.ButtonPress, name='Отменить', rely=-4, when_pressed_function=self.cancel_button_pressed)

    def save_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)
        settings.user = self.temp_user
        settings.user.save_to_file()

    def cancel_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

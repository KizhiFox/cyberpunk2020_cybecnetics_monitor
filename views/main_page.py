import math
import npyscreen

from assets import ascii_arts
from views.view_names import ViewNames
from utils.settings import settings


class MainPage(npyscreen.FormBaseNew):
    def pre_edit_loop(self):
        try:
            getattr(self, 'username_field')
            self.emp_status = self.get_emp_status()
            self.emp_color = self.get_emp_color()
            self.username_field.value = f' Добрый вечер, {settings.user.name}!'
            self.user_stats.values = [
                f'Эмпатия: {str(settings.user.get_emp())}/{str(settings.user.emp_max)}',
                f'Показатель человечности: {str(settings.user.get_hp())}',
                '',
                self.emp_status
            ]
            self.user_stats.color = self.emp_color

        except AttributeError:
            self.emp_status = self.get_emp_status()
            self.emp_color = self.get_emp_color()

    def create(self):
        self.name = settings.app_name
        self.lines = 24
        self.columns = 80

        self.username_field = self.add(npyscreen.Textfield, editable=False)
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Жизненные параметры')
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Подключенные импланты')
        self.add(npyscreen.ButtonPress, name='Подключенные чипы')
        self.add(npyscreen.ButtonPress, name='Сводка влияния на статистику')
        self.add(npyscreen.ButtonPress, name='Статус интерфейсов')
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Настройки', when_pressed_function=self.setting_button_pressed)
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Выход', when_pressed_function=self.exit_button_pressed)
        self.add(npyscreen.Textfield, value='', editable=False)

        self.user_stats = self.add(
            npyscreen.BoxTitle,
            values=[],
            name='Человечность',
            max_height=6, max_width=40, editable=False
        )
        self.add(npyscreen.Textfield, value='', editable=False)

        self.add(
            npyscreen.BoxTitle, values=ascii_arts.foxy.image, editable=False,
            relx=48, rely=4, max_height=ascii_arts.foxy.height, max_width=ascii_arts.foxy.width
        )

    def get_emp_status(self) -> str:
        emp_new = math.floor(settings.user.get_hp() / 10)
        if emp_new < 0:
            emp_new = 0
        emp_current = settings.user.get_emp()
        if emp_new < emp_current:
            return f'Возможно падение эмпатии до {emp_new}!'
        if emp_new > emp_current:
            return f'Возможен рост эмпатии до {emp_new}'
        return 'Ваш уровень эмпатии стабилен'

    def get_emp_color(self) -> str:
        emp_current = settings.user.get_emp()
        if emp_current <= 3:
            return 'DANGER'
        if emp_current <= 6:
            return 'WARNING'
        return 'DEFAULT'

    def setting_button_pressed(self):
        self.parentApp.switchForm(ViewNames.settings)

    def exit_button_pressed(self):
        res = npyscreen.notify_ok_cancel('Выйти?', wrap=True, editw=1)
        if res:
            self.exit()

    def exit(self, *args, **kwargs):
        self.parentApp.switchForm(None)

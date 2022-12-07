import npyscreen

from assets import ascii_arts
from views.view_names import ViewNames


class MainPage(npyscreen.FormBaseNew):
    def create(self):
        self.name = 'CyberController™ by News24'
        self.lines = 24
        self.columns = 80

        self.add(npyscreen.Textfield, value=' Добрый вечер, Ари!', editable=False)
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

        self.add(
            npyscreen.BoxTitle,
            values=['Эмпатия: 8/8', 'Показатель человечности: -18.5', '', 'Возможно падение EMP до 0'],
            name='Человечность', color='CAUTION',
            max_height=6, max_width=40, editable=False
        )
        self.add(npyscreen.Textfield, value='', editable=False)

        self.add(
            npyscreen.BoxTitle, values=ascii_arts.foxy.image, editable=False,
            relx=48, rely=4, max_height=ascii_arts.foxy.height, max_width=ascii_arts.foxy.width
        )

    def setting_button_pressed(self):
        self.parentApp.switchForm(ViewNames.settings)

    def exit_button_pressed(self):
        res = npyscreen.notify_ok_cancel('Выйти?', wrap=True, editw=1)
        if res:
            self.exit()

    def exit(self, *args, **kwargs):
        self.parentApp.switchForm(None)

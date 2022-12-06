import npyscreen

from assets import ASCIIimages


class MainPage(npyscreen.FormBaseNew):
    def create(self):
        self.name = '#CyberAhri2020 CyberController™ by News24'
        self.lines = 24
        self.columns = 80

        self.add(npyscreen.Textfield, value=' Добрый вечер, Ари!', editable=False)

        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Подключенные импланты')
        self.add(npyscreen.ButtonPress, name='Подключенные чипы')
        self.add(npyscreen.ButtonPress, name='Сводка влияния на статистику')
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Выход', when_pressed_function=self.exitButtonPressed)
        self.add(npyscreen.Textfield, value='', editable=False)

        self.add(
            npyscreen.BoxTitle,
            values=['Эмпатия: 8/8', 'Показатель человечности: -18.5'], editable=False,
            max_height=4, max_width=35,
            name='Человечность', footer='Возможно падение EMP до 0', color='CAUTION'
        )
        self.add(npyscreen.Textfield, value='', editable=False)

        self.add(
            npyscreen.BoxTitle,
            values=['🟢 Neuralware processor', '🟢 Chipware Socket', '🟢 Inteface plugs',
                    '🟢 Cybermodem link', '🟢 Phone Splice'],
            max_height=7, max_width=35,
            name='Статус интерфейсов', color='DEFAULT'
        )

        self.add(
            npyscreen.BoxTitle, values=ASCIIimages.Foxy.image, editable=False,
            relx=48, rely=3, max_height=ASCIIimages.Foxy.height, max_width=ASCIIimages.Foxy.width
        )

    def exitButtonPressed(self):
        res = npyscreen.notify_ok_cancel('Выйти?', wrap=True, editw=1)
        if res:
            self.exit()

    def exit(self, *args, **kwargs):
        self.parentApp.switchForm(None)

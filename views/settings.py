import npyscreen

from views.view_names import ViewNames


class SettingsPage(npyscreen.FormBaseNew):
    def create(self):
        self.name = 'CyberController™ by News24: НАСТРОЙКИ'
        self.lines = 24
        self.columns = 80

        self.add(npyscreen.ButtonPress, name='Параметр 1')
        self.add(npyscreen.ButtonPress, name='Параметр 2')
        self.add(npyscreen.ButtonPress, name='Параметр 3')
        self.add(npyscreen.ButtonPress, name='Параметр 4')
        self.add(npyscreen.ButtonPress, name='Параметр 5')
        self.add(npyscreen.Textfield, value='', editable=False)
        self.add(npyscreen.ButtonPress, name='Сохранить', when_pressed_function=self.save_button_pressed)
        self.add(npyscreen.ButtonPress, name='Отменить', when_pressed_function=self.cancel_button_pressed)
        self.add(npyscreen.Textfield, value='', editable=False)

    def pre_edit_loop(self):
        self.editw = 0

    def save_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

    def cancel_button_pressed(self):
        self.parentApp.switchForm(ViewNames.main)

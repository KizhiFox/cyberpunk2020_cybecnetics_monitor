import npyscreen

import views
from views.view_names import ViewNames


class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = npyscreen.Form(
            name='Welcome to Npyscreen',
            lines=24,
            columns=80
        )
        t = F.add(npyscreen.TitleText, name='Text:', )
        fn = F.add(npyscreen.TitleFilename, name='Filename:')
        fn2 = F.add(npyscreen.TitleFilenameCombo, name='Filename2:')
        dt = F.add(npyscreen.TitleDateCombo, name='Date:')
        s = F.add(npyscreen.TitleSlider, out_of=12, name='Slider')
        ml = F.add(npyscreen.MultiLineEdit,
                   value='''try typing here!\nMutiline text, press ^R to reformat.\n''',
                   max_height=5, rely=9)
        ms = F.add(npyscreen.TitleSelectOne, max_height=4, value=[1, ], name='Pick One',
                   values=['Option1', 'Option2', 'Option3'], scroll_exit=True)
        ms2 = F.add(npyscreen.TitleMultiSelect, max_height=-2, value=[1, ], name='Pick Several',
                    values=['Option1', 'Option2', 'Option3'], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())


class CyberController(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm(ViewNames.main, views.MainPage)
        self.addForm(ViewNames.settings, views.SettingsPage)
        self.addForm(ViewNames.cybernetics, views.CyberneticsPage)
        self.addForm(ViewNames.editor, views.EditorPage)


if __name__ == '__main__':
    my_app = CyberController()
    try:
        my_app.run()
    except KeyboardInterrupt:
        pass
    print('🧡 Bye! 🧡')

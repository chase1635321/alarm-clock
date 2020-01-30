#!/usr/bin/python3

import npyscreen

class TestApp(npyscreen.NPSApp):

    def main(self):
        # These lines create the form and populate it with widgets.
        form  = npyscreen.Form(name = "Jarvis v1.0",)
        with open("asm.txt", "r") as f:
            asmText = f.read()
        form.add(npyscreen.TitleText, name="First Widget")
        form.add(npyscreen.MultiLineEdit, name="Assembly Challenge", value=asmText, max_height=20)

        # This lets the user interact with the Form.
        form.edit()
        print(ms.get_selected_objects())

App = TestApp()
App.run()


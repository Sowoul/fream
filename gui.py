from turtle import onrelease, title
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem

from kivy.lang import Builder
from depends import inp, KV


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        num = 0
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            num = num+1
            if check != instance_check:
                check.active = False
            else:
                print(num)


class demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()
        btn = MDRectangleFlatButton(text='Search', pos_hint={
                                    'center_x': 0.5, 'center_y': 0.42}, on_release=self.fin)
        screen.add_widget(btn)
        # l1 = MDLabel(text='Hello world', halign='center',
        #              theme_text_color='Custom', text_color=(255/255.0, 100/255.0, 103/255.0, 1), font_style='Button')
        # screen.add_widget(l1)
        self.m = Builder.load_string(inp)
        self.dic = Builder.load_string(KV)
        screen.add_widget(self.dic)

        screen.add_widget(self.m)
        return screen

    def doge(self, obj):
        print()

    def close(self, obj):
        self.dia.dismiss()

    def fin(self, obj):
        first = MDRectangleFlatButton(text="Back", on_release=self.close)
        self.dia = MDDialog(title=f'Results for "{self.m.text}"',
                            type="confirmation",
                            items=[
                                ItemConfirm(text="Choice 1"),
                                ItemConfirm(text="Choice 2"),
                                ItemConfirm(text="Choice 3"),
                            ],
                            buttons=[
                                first,
                            ],
                            )
        self.dia.open()


demo().run()

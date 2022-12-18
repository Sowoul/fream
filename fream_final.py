from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from urllib.request import Request, urlopen
import re
from kivy.lang import Builder
from depends import inp, KV
import webbrowser
x = []
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
                f = Request(x[num-1], headers={'User-Agent': 'Mozilla/5.0'})
                f = urlopen(f).read().decode()
                f = re.split('<a href="magnet', f)
                magnet = ("magnet" + f[1][:f[1].index('"')])
                webbrowser.open(magnet)

class Fream(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "300"
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
        if ' ' in self.m.text:
            g = Request(f"https://fitgirl-repacks.site/?s={self.m.text.replace(' ', '+')}", headers={'User-Agent': 'Mozilla/5.0'})
        else:
            g = Request(f"https://fitgirl-repacks.site/?s={self.m.text}", headers={'User-Agent': 'Mozilla/5.0'})
        f = urlopen(g).read().decode()
        f=f.split('<h1 class="entry-title"><a href="',4)
        tit=[]
        for i in range(1, 4):
            try:
                title=f[i].split('rel="bookmark">',1)
                if '&' in title[1][:title[1].index("</a>")]:
                    tit.append(f"{i}. " + title[1][:title[1].index("&")])
                else:
                    tit.append(f"{i}. " + title[1][:title[1].index("</a>")])
                x.append((f[i])[:f[i].index('"')])
            except:
                pass
        emp=[]
        for j in tit:
            emp.append(ItemConfirm(text=j))
        first = MDRectangleFlatButton(text="Back", on_release=self.close)
        self.dia = MDDialog(title=f'Results for "{self.m.text}"',
                            type="confirmation",
                            items=emp,
                            buttons=[
                                first,
                            ],
                            )
        self.dia.open()
Fream().run()
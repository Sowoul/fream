inp = """
MDTextField:
    hint_text: "Enter the game's title"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    icon_right: "gamepad-variant-outline"
    size_hint_x: None
    width:300
"""
KV = '''
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"


MDFloatLayout:

'''

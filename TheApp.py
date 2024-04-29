import re

from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

import TheModule


def refactoring(bond):
    collection_of_subscripts = {"1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
                                "7": "₇", "8": "₈", "9": "₉"}

    for key, value in collection_of_subscripts.items():
        bond = bond.replace(value, key)
    split_expression = re.findall(r"[0-9]+", bond)
    l = dict()
    for item in split_expression:
        l.update({item: f"[sub]{item}[/sub]"})
    for key, value in l.items():
        bond = bond.replace(key, value)

    return bond


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        screen = Screen()

        def perform_bond(instance):
            try:
                first_argument = TheModule.dictionary_of_elements.get(first_element.text)
                second_argument = TheModule.dictionary_of_stuff.get(second_element.text)
                display_label.text = refactoring(TheModule.bonding(first_argument, second_argument))
            except AttributeError:
                display_label.text = "There is an error somewhere"

        def dialogPUSH(instance):
            dialog_box = MDDialog(text="This app is not perfect \nIt has missing elements \nThe bonding "
                                       "is raw and \nIt lacks certain functionality")
            dialog_box.open()

        first_element = MDTextField(hint_text="Enter the element please: ",
                                    pos_hint={"center_x": 0.5, "center_y": 0.6},
                                    size_hint_x=None,
                                    width=250,
                                    helper_text="for example, 'Sodium'")
        second_element = MDTextField(helper_text="e.g 'Sulphate' or 'Chlorine'",
                                     pos_hint={"center_x": 0.5, "center_y": 0.5},
                                     width=250,
                                     hint_text="Enter the radical or element please:",
                                     size_hint_x=None)
        display_label = MDLabel(halign="center",
                                width=250,
                                text="",
                                markup=True,
                                pos_hint={"center_x": 0.5, "center_y": 0.3})
        bond_button = MDRoundFlatButton(pos_hint={"center_x": 0.5, "center_y": 0.4},
                                        text="BOND",
                                        on_release=perform_bond)
        info_button = MDRectangleFlatButton(text="INFO",
                                            on_release=dialogPUSH)
        screen.add_widget(info_button)

        screen.add_widget(first_element)
        screen.add_widget(second_element)
        screen.add_widget(display_label)
        screen.add_widget(bond_button)
        return screen


DemoApp().run()

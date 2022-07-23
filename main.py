from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector


class LiveRecord(Widget):
    my_label = ObjectProperty(None)

class DelosApp(App):
    def build(self):
        ui = LiveRecord()
        return ui

if __name__ == '__main__':
    DelosApp().run()
import kivy
from os import environ

environ['KIVY_WINDOW'] = 'sdl2'
# now you can import kivy things
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.camera import Camera


class MainApp(App):
    def build(self):
        return Camera(play=True, index=0, resolution=([-1, -1]))  # , resolution=([640,480]))


if __name__ == "__main__":
    MainApp().build()


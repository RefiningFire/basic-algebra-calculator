from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition

from kivy.core.window import Window

Window.fullscreen = 'auto'

Window.allow_screensaver = True




class MainScreen(Screen):
    pass


class BasicAlgebraCalc(App):
    def build(self):
        app.sm = ScreenManager(transition=SlideTransition())

        app.sm.add_widget(MainScreen(name='main'))

        return app.sm



if __name__ == '__main__':
    app = BasicAlgebraCalc()

    app.run()

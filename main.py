from core.guts.app import App
from core.guts.window import Window

if __name__ == "__main__":
    window = Window()
    app = App(window)
    app.run()
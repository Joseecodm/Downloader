from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class YoutubeDownloaderApp(App):
    def build(self):
        Window.size = (550, 140)
        return Builder.load_file('youtubedownloader.kv')

if __name__ == '__main__':
    YoutubeDownloaderApp().run()

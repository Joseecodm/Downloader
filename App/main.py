from kivy.lang import Builder
from kivy.app import App

class YoutubeDownloaderApp(App):
    def build(self):
        return Builder.load_file('youtubedownloader.kv')

if __name__ == '__main__':
    YoutubeDownloaderApp().run()

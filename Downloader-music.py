from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_audio():
    try:
        link = input('Enter the YouTube video or song link: ')
        print('\n')

        yt = YouTube(link)
        print("Video Title:", yt.title)
        print("Video Author:", yt.author)
        print('\n')

        duration = yt.length
        minutes, seconds = divmod(duration, 60)
        print(f"Video Duration: {minutes:02d}:{seconds:02d}")

        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        if audio_stream:
            download_path = './' 
            audio_file = audio_stream.download(download_path)

            # If the file is already an audio file, rename it directly
            if audio_file.endswith('.mp3'):
                mp3_file = audio_file
            else:
                # Convert the downloaded file to MP3
                audio_clip = AudioFileClip(audio_file)
                mp3_file = audio_file.replace(audio_file.split('.')[-1], "mp3")
                audio_clip.write_audiofile(mp3_file)
                audio_clip.close()
                os.remove(audio_file)

            print(f"The audio '{yt.title}' has been successfully downloaded to '{mp3_file}'")
        else:
            print("No suitable audio stream found for download.")

    except pytube.exceptions.RegexMatchError:
        print("Invalid YouTube link. Please check the link and try again.")
    except Exception as e:
        print(f"An error occurred while downloading the audio: {e}")

if __name__ == "__main__":
    download_audio()

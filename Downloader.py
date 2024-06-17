from pickletools import pytuple
from pytube import YouTube

def download_video():
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

        # Find the best quality progressive MP4 stream (video and audio combined)
        best_quality = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        # Check if a suitable stream was found
        if best_quality:
            download_path = './'  # You can customize the download path here
            best_quality.download(download_path)
            print(f"The video '{yt.title}' has been successfully downloaded to '{download_path}'")
        else:
            print("No suitable MP4 stream found for download.")

    except pytube.exceptions.RegexMatchError:
        print("Invalid YouTube link. Please check the link and try again.")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

if __name__ == "__main__":
    download_video()

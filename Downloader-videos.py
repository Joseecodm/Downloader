from pytube import YouTube

def download_video():
    """
    Downloads a YouTube video of the highest available quality.

    This function prompts the user to input a YouTube video link, retrieves the video's title, author, and duration,
    and downloads the video of the highest available quality in mp4 format to the current directory.

    Parameters:
    None

    Returns:
    None

    Raises:
    - pytube.exceptions.RegexMatchError: If the input YouTube link is invalid.
    - Exception: If an error occurs while downloading the video.
    """
    
    try:
        link = input('Enter the YouTube video: ')
        print('\n')

        yt = YouTube(link)
        print("Video Title:", yt.title)
        print("Video Author:", yt.author)
        print('\n')

        duration = yt.length
        minutes, seconds = divmod(duration, 60)
        print(f"Video Duration: {minutes:02d}:{seconds:02d}")

        best_quality = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
  
        if best_quality:
            download_path = './'  
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

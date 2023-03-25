from pytube import YouTube, request

import os
from pathlib import Path

# request.default_range_size = 500000

# def get_video(url, save_location, in_progress, on_complete, handle_error):
    
#     try:
#         filename = str(Path(save_location).name)
#         output_path = str(os.path.split(Path(save_location))[0])
#         print(filename)
#         print(output_path)
#         download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)
#         stream = download.streams.filter(progressive=True).get_highest_resolution()
#         stream = download(filename=filename, output_path=output_path)
#         return
#     except:
#         error = True
#         handle_error()
#         return
    

# if __name__ == "__main__":
#     filetype = "mp4"
#     url = input("Please enter URL: ")
#     get_video(url, "./")

def download_video(url, download_path=None):
    # Create a YouTube object
    yt = YouTube(url)

    # Get the highest resolution video stream available
    video = yt.streams.get_highest_resolution()

    # Set the download path
    if download_path is None:
        download_path = os.getcwd()

    # Download the video
    print(f"Downloading: {yt.title}")
    video.download(download_path)
    print(f"Download complete: {yt.title}")


def main():
    print("YouTube Video Downloader")

    # Get video URL and download path from the user
    url = input("Enter the video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ")

    # Download the video
    try:
        download_video(url, download_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

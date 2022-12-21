import os
from pytube import YouTube

# Enter the URL of the YouTube video
url = input("Enter the URL of the YouTube video: ")

# Create a YouTube object
yt = YouTube(url)

# Select the video quality and format you want to download
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').last()

# Set the download location to the "Downloads" folder
download_path = os.path.expanduser("~/Downloads")

# Download the video to the specified location
video.download(download_path)

print("Video downloaded to", download_path)

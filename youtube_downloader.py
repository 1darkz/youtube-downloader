import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
import threading


def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        status_label.config(text="Downloading...")
        stream.download()
        status_label.config(text="Download complete")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="")


def start_download_thread():
    download_thread = threading.Thread(target=download_video)
    download_thread.start()


# Initialize the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and set the layout
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# URL entry
url_label = ttk.Label(frame, text="Enter the YouTube video URL:")
url_label.grid(column=0, row=0, pady=(0, 5))
url_entry = ttk.Entry(frame, width=40)
url_entry.grid(column=0, row=1, pady=(0, 10))

# Download button
download_button = ttk.Button(frame, text="Download", command=start_download_thread)
download_button.grid(column=0, row=2, pady=(0, 10))

# Status label
status_label = ttk.Label(frame, text="")
status_label.grid(column=0, row=3, pady=(0, 5))

# Run the main loop
root.mainloop()

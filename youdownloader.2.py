import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
import winsound
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Function to play a success sound
def play_success_sound():
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

# Function to play an error sound
def play_error_sound():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

# Function to download and display thumbnail
def show_thumbnail(ytlink):
    try:
        ytobject = YouTube(ytlink)
        thumbnail_url = ytobject.thumbnail_url
        response = requests.get(thumbnail_url)
        image = Image.open(BytesIO(response.content))
        # Resize the image to a smaller size
        image = image.resize((400, 250), Image.LANCZOS)
        thumbnail = ImageTk.PhotoImage(image)

        thumbnail_label.configure(image=thumbnail)
        thumbnail_label.image = thumbnail  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Failed to load thumbnail: {e}")

# Download system settings
def startDownload():
    try:
        ytlink = url_yar.get()
        ytobject = YouTube(ytlink)
        video = ytobject.streams.get_highest_resolution()

        footer_label.configure(text=ytobject.title, text_color="white")
        show_thumbnail(ytlink)
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Downloaded!!", text_color="green")
        play_success_sound()  # Play success sound
    except Exception as e:
        finish_label.configure(text=f"Failed to download: {e}", text_color="red")
        play_error_sound()  # Play error sound
  
# System settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Creating the main application window
app = ctk.CTk()
app.geometry("800x600")
app.title("YouTube Downloader")

# Title label
title_label = ctk.CTkLabel(app, text="YouTube Downloader", width=40, height=2, font=('Arial', 30, 'bold'), text_color="green")
title_label.pack(pady=10)

# Link input
url_yar = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_yar)
link.pack(padx=12, pady=10 )

# Download Now button
download = ctk.CTkButton(app, text="Download Now!", command=startDownload, width=50, height=20, font=('Times New Roman', 20, 'bold'))
download.pack(padx=12, pady=10)

# Finish Label
finish_label = ctk.CTkLabel(app, text="", font=('Arial', 16))
finish_label.pack(pady=10)

# Footer Label
footer_label = ctk.CTkLabel(app, text="Thank You For Using 'YouTube Downloader' Made By Ebad With Love!", width=70, height=3, font=('Arial', 16, 'bold'), text_color="green")
footer_label.pack(pady=10)

# Thumbnail Label
thumbnail_label = tk.Label(app)
thumbnail_label.pack(pady=10)

# Running the application
app.mainloop()

import tkinter
import customtkinter
from pytube import YouTube


#dowload system settings

def startDownload():
  try:
    ytlink = link.get()
    ytobject = YouTube(ytlink, on_progress_callback=on_progress)
    video = ytobject.streams.get_highest_resolution()

    title.configure(text=ytobject.title, text_color="white")
    finishlabel.configure(text="")
    video.download()
    finishlabel.configure(text="Downloaded!!", text_color="green") 
  except:
    finishlabel.configure(text="Downloaded!!", text_color="green")
  
def on_progress(stream, chunk ,bytes_remaning ):
  total_size = stream.filsize
  bytes_download = total_size - bytes_remaning
  percentage_of_completion = bytes_download / total_size * 100
  print(percentage_of_completion)
  per = str(int(percentage_of_completion))
  pPercentage.configure(text=per + '%')
  pPercentage.update()

#system-settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# Our app frame
app = customtkinter.CTk()
app.geometry("700x420")
app.title("YOU DOWNLOADER")

#adding UI elements
title = customtkinter.CTkLabel(app, text ="YOUTUBE URL",  width=40,
            height=5, font=('Times New Roman', 25, 'bold'), text_color="green" )
title.pack(padx=10, pady=10)

#link input
url_yar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_yar)
link.pack(padx=20, pady=20 )

#Download Now
download = customtkinter.CTkButton(app, text="Download Now!", command=startDownload, width=40, height=10, font=('Times New Roman', 25, 'bold'), )
download.pack(padx=1, pady=1)

#progress bar
pPercentage = customtkinter.CTkLabel(app, text="")
pPercentage.pack()
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(100)
progressBar.pack(padx=10, pady = 10)

#fininshed Downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()


#adding UI elements
title = customtkinter.CTkLabel(app, text ="ThankYou For Using 'You downloader' Made By Ebad With Love! ", width=40, height=10, font=('Times New Roman', 20, 'bold'), text_color="green" )
download.pack(padx=1, pady=20)
title.pack(padx=1, pady=20)

# Run app
app.mainloop()
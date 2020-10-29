from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
Folder_Name=""
def progress_function(stream, chunk, file_handle, bytes_remaining):
    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')
#file location
def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please choose Folder!!",fg="red")

def DownloadVideo():
    choice=ytdChoices.get()
    url=ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text="")
        yt=YouTube(url, on_progress_callback=progress_function)
      
    yt.streams.order_by('resolution')
    ytdError.config(text="download completed")


    
root=Tk()
root.title("Youtube Downloader")
root.geometry("350x400")
root.columnconfigure(0,weight=1)

ytdLabel=Label(root,text="enter youtube video URL",font=("jost",15))
ytdLabel.grid()

ytdEntryVar=StringVar()
ytdEntry=Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError=Label(root,text="Error Msg",fg="red",font=("jost",10))
ytdError.grid()

saveLabel=Label(root,text="Save the video file",font=("jost",15,"bold"))
saveLabel.grid()

saveEntry=Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError=Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

ytdQuality=Label(root,text="Select quality",font=("jost",15,"bold"))
ytdQuality.grid()

choices=["720p","144p","Only audio"]
ytdChoices=ttk.Combobox(root,values=choices)
ytdChoices.grid()

downloadbtn=Button(root,text="Downlaod video",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

root.mainloop()
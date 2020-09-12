import os
import time
from watchdog.events import FileSystemEventHandler


def get_file_type(file):
   filename = file.split(".")
   return filename[-1]


def move_file(filename, original_path, new_path):
   file_moved = False

   src = original_path + '/' + filename
   new_destination = new_path + '/' + filename
   while not file_moved:
      try:
         os.rename(src, new_destination)
         file_moved = True
      except FileExistsError:
         filename = '(new)' + filename
         new_destination = new_path + '/' + filename


def add_filter(filename, filetype, destination):
   if get_file_type(filename).lower() == filetype:
      move_file(filename, pathtowatch, destination)


def event_triggered():
   for filename in os.listdir(pathtowatch):
      if filename not in notwatch:
         if get_file_type(filename) not in filetypes:
            move_file(filename, pathtowatch, other_destination)
         else:
            add_filter(filename, "pdf", pdf_destination)
            add_filter(filename, "png", png_destination)
            add_filter(filename, "jpg", jpg_destination)
            add_filter(filename, "jpeg", jpeg_destination)
            add_filter(filename, "zip", zip_destination)
            add_filter(filename, "exe", exe_destination)
            add_filter(filename, "wav", wav_destination)
            add_filter(filename, "rar", rar_destination)
            add_filter(filename, "mp3", mp3_destination)
            add_filter(filename, "mp4", mp4_destination)
            add_filter(filename, "mpeg", mpeg_destination)
            add_filter(filename, "txt", txt_destination)
            add_filter(filename, "blend", blend_destination)
            add_filter(filename, "zip", zip_destination)
            add_filter(filename, "html", html_destination)


class DownloadedFilesHandler(FileSystemEventHandler):
   def on_created(self, event):
      time.sleep(10)
      event_triggered()

   def on_moved(self, event):
      event_triggered()

filetypes = (
   "pdf", "png", "jpg", "jpeg", "zip", "exe", "wav", "rar",
   "mp3", "mp4", "mpeg", "txt", "blend", "html"
)
notwatch = (
   ".other", ".pdf", ".png", ".jpg", ".jpeg", ".zip", ".exe", ".wav", ".rar",
   ".mp3", ".mp4", ".mpeg", ".txt", ".blend", ".html"
)

pathtowatch = "D:/Usuario/Downloads"
other_destination = "D:/Usuario/Downloads/.other"
pdf_destination = "D:/Usuario/Downloads/.pdf"
png_destination = "D:/Usuario/Downloads/.png"
jpg_destination = "D:/Usuario/Downloads/.jpg"
jpeg_destination = "D:/Usuario/Downloads/.jpeg"
zip_destination = "D:/Usuario/Downloads/.zip"
exe_destination = "D:/Usuario/Downloads/.exe"
wav_destination = "D:/Usuario/Downloads/.wav"
rar_destination = "D:/Usuario/Downloads/.rar"
mp3_destination = "D:/Usuario/Downloads/.mp3"
mp4_destination = "D:/Usuario/Downloads/.mp4"
mpeg_destination = "D:/Usuario/Downloads/.mpeg"
txt_destination = "D:/Usuario/Downloads/.txt"
blend_destination = "D:/Usuario/Downloads/.blend"
html_destination = "D:/Usuario/Downloads/.html"

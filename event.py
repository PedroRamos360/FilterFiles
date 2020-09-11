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


def event_triggered():
   for filename in os.listdir(pathtowatch):
      if filename not in notwatch:
         if get_file_type(filename).lower() == "pdf":
            move_file(filename, pathtowatch, pdf_destination)

         elif get_file_type(filename).lower() == "png":
            move_file(filename, pathtowatch, png_destination)

         elif get_file_type(filename).lower() == "jpg":
            move_file(filename, pathtowatch, jpg_destination)

         elif get_file_type(filename).lower() == "zip":
            move_file(filename, pathtowatch, zip_destination)

         else:
            move_file(filename, pathtowatch, other_destination)


class FileCreationHandler(FileSystemEventHandler):
   def on_created(self, event):
      time.sleep(10)
      event_triggered()

   def on_moved(self, event):
      event_triggered()


notwatch = (".other", ".pdf", ".png", ".jpg", ".zip")
pathtowatch = "D:/Usuario/Downloads"
other_destination = "D:/Usuario/Downloads/.other"
pdf_destination = "D:/Usuario/Downloads/.pdf"
png_destination = "D:/Usuario/Downloads/.png"
jpg_destination = "D:/Usuario/Downloads/.jpg"
zip_destination = "D:/Usuario/Downloads/.zip"




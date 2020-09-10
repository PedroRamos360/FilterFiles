import os
import time
from watchdog.events import FileSystemEventHandler

class FileCreationHandler(FileSystemEventHandler):
   def on_modified(self, event):
      for filename in os.listdir(pathtowatch):
         if filename != "Images":
            src = pathtowatch + '/' + filename
            new_destination = destination + '/' + filename
            print("File moved from: {} to: {}".format(src, new_destination))
            os.rename(src, new_destination)


pathtowatch = "D:/Usuario/Downloads/Downloads"
destination = "D:/Usuario/Downloads/Downloads/Images"



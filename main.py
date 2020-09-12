import os
import time
from watchdog.observers import Observer
from event import DownloadedFilesHandler
from event import event_triggered

event_triggered()

pathtowatch = "D:/Usuario/Downloads"
event_handler = DownloadedFilesHandler()

observer = Observer()
observer.schedule(event_handler, pathtowatch, recursive=True)

observer.start()
try:
   while True:
      time.sleep(300)
except KeyboardInterrupt:
   observer.stop()
observer.join()

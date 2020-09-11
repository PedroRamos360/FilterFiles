import os
import time
from watchdog.observers import Observer
from event import FileCreationHandler
from event import event_triggered

event_triggered()

pathtowatch = "D:/Usuario/Downloads"
event_handler = FileCreationHandler()

observer = Observer()
observer.schedule(event_handler, pathtowatch, recursive=True)

observer.start()
try:
   while True:
      time.sleep(10)
except KeyboardInterrupt:
   observer.stop()
observer.join()

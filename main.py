import os
import time
from watchdog.observers import Observer
from event import FileCreationHandler

print("monitoring")

pathtowatch = "D:/Usuario/Downloads/Downloads"
event_handler = FileCreationHandler()

observer = Observer()
observer.schedule(event_handler, pathtowatch, recursive=True)

observer.start()
try:
    while True:
        print("timer")
        time.sleep(0.1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def on_created(event):
    print("File created")
    
        
if __name__ == "__main__":
    path = "D:/Usuario/Downloads"
    destination = "D:/Usuario/Downloads/Images"
    event_handler = FileSystemEventHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    event_handler.on_created = on_created
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
import os 
import shutil
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler

# Assign these folders.
downloads_folder = ""
pictures_folder = ""
documents_folder = ""


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(downloads_folder):
            if file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):
                shutil.move((os.path.join(downloads_folder, file)), (os.path.join(pictures_folder, file)))
            elif file.endswith(".pdf"): 
                shutil.move((os.path.join(downloads_folder, file)), (os.path.join(documents_folder, file)))

go_recursively = True
observer = Observer()
event_handler = MyHandler()
observer.schedule(event_handler, downloads_folder, recursive=go_recursively)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
    
    




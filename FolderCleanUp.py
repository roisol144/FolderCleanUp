import os
import shutil
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler

if __name__ == "__main__":

    downloads_folder = "/Users/USER/Downloads"
    pictures_folder = "/Users/USER/Pictures"
    documents_folder = "/Users/USER/Documents"
    music_folder = "/Users/USER/Music"

    suffix_audio = [".mp3", ".m4a", ".m4r", ".wma"]
    suffix_image = [".jpg", ".JPEG", ".jpeg", ".png", ".gif"]
    suffix_docs = [".doc", ".docx", ".pdf", ".xml", ".xla", ".xlsx"]


    class MyHandler(FileSystemEventHandler):
        def on_modified(self, event):
            for file in os.listdir(downloads_folder):
                filename, file_extension = os.path.splitext(file)

                if file_extension in suffix_image:
                    shutil.move((os.path.join(downloads_folder, file)), (os.path.join(pictures_folder, file)))
                if file_extension in suffix_docs:
                    shutil.move((os.path.join(downloads_folder, file)), (os.path.join(documents_folder, file)))
                elif file_extension in suffix_audio:
                    shutil.move((os.path.join(downloads_folder, file)), (os.path.join(music_folder, file)))


    observer = Observer()
    event_handler = MyHandler()
    observer.schedule(event_handler, downloads_folder, recursive=True)
    print("Watchdog Starts... ")
    observer.start()
    print("Watchdog Tracking... ")

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()




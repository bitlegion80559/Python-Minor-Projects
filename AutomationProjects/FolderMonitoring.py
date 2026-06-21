import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER= os.path.expanduser("~/Downloads")

FOLDER = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
}

class FileHandler(FileSystemEventHandler):
    def on_created(self,event):
        if event.is_directory:
            return
        filepath=event.src_path
        ext=os.path.splitext(filepath)[1].lower()
        dest_folder=FOLDER.get('ext',"Others")
        full_dest=os.path.join(filepath,dest_folder)
        os.makedirs(full_dest,exist_ok=True)
        try:
            shutil.move(filepath,os.path.join(full_dest,os.path.basename(filepath)))

        except:
            print("Some unexpected error occured")
    
if __name__=="__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:\\Users\\miche\\Downloads"
destination = "C:\Users\miche\Downloads\Project103"

dir_tree = {
    
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)

        time.sleep(1)

        for key, value in dir_tree.items():
         time.sleep(1)
         if extension in value: 
            fileName = os.path.basename(event.src_path)

            print("Downloaded"+fileName)

            path1 = source + '/' + fileName
            path2 = destination + '/'+ key
            path3 = destination + '/' +key+ '/' +fileName

            time.sleep(1)
            if os.path.exists(path2):
                print("Folder Exists")

                time.sleep(1)
                if os.path.exists(path3):
                    print("File already exist in " + key)
                    print("renaiming file "+ fileName)
                    newFile = os.path.splitext(fileName)[0]+str(random.randint(0,999))+ os.path.splitext(fileName)[1]
                    path4 = destination + '/' + key + '/' +newFile
                    print("Moving "+ newFile)
                    shutil.move(path1,path4)
                    time.sleep(1)
                else:
                    print("Moving" + fileName)
                    shutil.move(path1,path3)
                    time.sleep(1)
            else:
                os.makedirs(path2)
                shutil.move(path1,path3)
                time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()

observer.shedule(event_handler, source,recusive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
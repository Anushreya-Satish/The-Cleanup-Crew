import sys      # Provides access to system-specific parameters and functions
import time     # Used to handle time-related tasks
import random   
import os       # Essential for navigating directories, splitting paths, and checking files
import shutil   # Used for high-level file operations, such as copying and moving files

# Modules for monitoring file system events
import watchdog.observers
import watchdog.events

# Configuration Paths
from_dir = "C:/Users/Anushreya/Downloads"    # Target directory being monitored (PATH OF DOWNLOAD FOLDER)
to_dir = "D:/Projects"       # Destination directory for file organization (PATH OF DESTINATION FOLDER)

# File Categories Mapping
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# ---Event Hanlder Class---
# Define actions on file system changes
class FileMovementHandler(watchdog.events.FileSystemEventHandler):
   
    # Automatically triggers whenever a new file or folder is create
    def on_created(self, event):
        
        print(event) # Logs the event details to the console for debugging purposes
        print(event.src_path) # Logs the source path of the created file or folder
       
        # Extract the file extension from the created file's path in tuple format (name, extension)
        name, ext = os.path.splitext(event.src_path)

        # Iterate through the defined directory tree to find the appropriate category for the file based on its extension
        for key, value in dir_tree.items():
            if ext in value: # Checks if the file extension matches any of the extensions listed in the current category
                file_name = os.path.basename(event.src_path) # Extracts the file name from the full path of the created file
                path1 = from_dir+'/'+file_name # Constructs the full path to the created file in the source directory
                path2 = to_dir+'/'+key # Constructs the path to the target category directory in the destination folder
                path3 = to_dir+'/'+key+'/'+file_name # Constructs the full path to where the file should be moved in the destination directory
                time.sleep(3) # Waits for a short period to ensure the file is fully created and not in use before attempting to move it
               
                # Checks if the target category directory already exists in the destination folder
                if os.path.exits(path2): 
                    # If the target category directory exists, it moves the file from the source directory to the target category directory in the destination folder
                    if os.path.exists(path3):
                        shutil.move(path1,path3)
                    # If the file already exists in the target category directory, it appends a random number to the file name to avoid overwriting and then moves the file 
                    else:
                        os.makedirs(path2)
                        shutil.move(path1,path3)
                        time.sleep(1)

# ---Main Program---
# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = watchdog.observers.Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

# Keep the program running to monitor file system events until interrupted by the user
try:
    while True:
        time.sleep(2)
        print("running...")

# Handle Keyboard Interrupt to gracefully stop the observer when the user decides to terminate the program    
except KeyboardInterrupt:
    print("Stopped...")
    observer.stop()

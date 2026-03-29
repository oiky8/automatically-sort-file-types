import os
import time
import shutil
import threading
import tkinter as tk
from tkinter import messagebox

download_folder = r"D:\Doawload"

file_types = {
    "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    "Video": ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    "Apps": ['.exe', '.msi'],
    "Documents": ['.pdf', '.docx', '.doc', '.xlsx', '.pptx', '.txt'],
    "Images": ['.png', '.jpg', '.jpeg'],
    "Archives": ['.zip', '.rar']
}

running = False

def sorter():
    processed = set()
    global running

    while running:
        files = os.listdir(download_folder)

        for file in files:
            file_path = os.path.join(download_folder, file)

            if file.endswith(".crdownload"):
                continue

            if os.path.isfile(file_path) and file not in processed:
                name, ext = os.path.splitext(file)
                ext = ext.lower()

                for folder, extensions in file_types.items():
                    if ext in extensions:
                        target_folder = os.path.join(download_folder, folder)

                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)

                        shutil.move(file_path, os.path.join(target_folder, file))
                        processed.add(file)

                        messagebox.showinfo("Done", f"{file} → {folder}")
                        break

        time.sleep(2)

def start():
    global running
    if not running:
        running = True
        threading.Thread(target=sorter, daemon=True).start()

def stop():
    global running
    running = False

# UI
root = tk.Tk()
root.title("Auto Sort Download")
root.geometry("300x150")

btn_start = tk.Button(root, text="Start", command=start, bg="green", fg="white")
btn_start.pack(pady=10)

btn_stop = tk.Button(root, text="Stop", command=stop, bg="red", fg="white")
btn_stop.pack(pady=10)

root.mainloop()

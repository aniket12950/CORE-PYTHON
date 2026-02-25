"""
Project: Automatic File Organizer
Description: Organizes files into folders based on file type
"""

import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
}

def organize_folder(path):
    if not os.path.exists(path):
        print(" Folder does not exist.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(path, folder_name)

                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f" Moved {filename} → {folder_name}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(path, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f" Moved {filename} → Others")

    print("\n Files organized successfully!")


if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ")
    organize_folder(folder_path.strip())
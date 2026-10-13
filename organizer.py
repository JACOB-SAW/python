import os
import shutil

# Folder you want to organize
TARGET_FOLDER = r"C:\Users\YourName\Downloads"  # Change this to any folder

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json"]
}

def create_folders(base_path):
    """Create category folders if they don't exist."""
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organize_files(base_path):
    """Move files into categorized folders."""
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(base_path, category)
                    shutil.move(file_path, dest_folder)
                    print(f"Moved: {file} → {category}")
                    break

if __name__ == "__main__":
    print("Organizing files...")
    create_folders(TARGET_FOLDER)
    organize_files(TARGET_FOLDER)
    print("Done!")

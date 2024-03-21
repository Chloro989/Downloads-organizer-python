import os
import shutil
from pathlib import Path
from filtering_list import directories  # filtering_list.pyからdirectories辞書をインポートする

def move_other_contents_to_root(directory_path):
    """
    Move contents of the "OTHER" folder back to the root of the directory_path for reorganization.
    :param directory_path: Path to the directory being organized.
    """
    other_path = directory_path / "OTHER"
    if other_path.exists() and other_path.is_dir():
        for item in other_path.iterdir():
            shutil.move(str(item), str(directory_path))
        other_path.rmdir()  # Remove the OTHER folder after moving its contents

def create_folders(directories, directory_path):
    """
    Ensure all specified folders exist in the directory path.
    """
    for key in directories:
        folder_path = directory_path / key
        folder_path.mkdir(exist_ok=True)

def organize_folders(directories, directory_path):
    """
    Organize files into their respective folders based on file extension.
    """
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            for key, extensions in directories.items():
                if file.lower().endswith(extensions):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break

def organize_remaining_files(directory_path):
    """
    Move files that do not match any category into the "OTHER" folder.
    """
    create_folders({"OTHER": ""}, directory_path)  # Ensure OTHER folder exists
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)

def organize_remaining_folders(directories, directory_path):
    """
    Move unclassified folders into the "FOLDERS" directory.
    """
    create_folders({"FOLDERS": ""}, directory_path)  # Ensure FOLDERS folder exists
    for folder in os.listdir(directory_path):
        folder_path = Path(directory_path / folder)
        if folder_path.is_dir() and folder not in directories and folder != "OTHER" and folder != "FOLDERS":
            dest_path = directory_path / "FOLDERS" / folder
            shutil.move(str(folder_path), str(dest_path))

if __name__ == "__main__":
    home_directory = Path.home()
    directory_path = home_directory / 'Downloads'

    try:
        move_other_contents_to_root(directory_path)  # Move contents of "OTHER" to root for reorganization
        create_folders(directories, directory_path)
        organize_folders(directories, directory_path)
        organize_remaining_files(directory_path)
        organize_remaining_folders(directories, directory_path)
    except Exception as e:
        print(f"An error occurred: {e}")

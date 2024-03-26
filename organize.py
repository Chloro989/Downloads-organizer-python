import os
import shutil
from pathlib import Path
from filtering_list import (
    directories,
)  # filtering_list.pyからdirectories辞書をインポートする

def create_folders(directories, directory_path):
    """
    Ensure all specified folders exist in the directory path.
    Do not overwrite existing folders.
    """
    for key in directories:
        folder_path = directory_path / key
        # Only create the folder if it does not exist
        if not folder_path.exists():
            folder_path.mkdir()

def remove_empty_folders(directories, directory_path):
    """
    Remove folders that are empty after organization.
    """
    for key in directories:
        folder_path = directory_path / key
        if folder_path.exists() and not any(folder_path.iterdir()):
            folder_path.rmdir()

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
        if (
            folder_path.is_dir()
            and folder not in directories
            and folder != "OTHER"
            and folder != "FOLDERS"
        ):
            dest_path = directory_path / "FOLDERS" / folder
            shutil.move(str(folder_path), str(dest_path))


if __name__ == "__main__":
    home_directory = Path.home()
    directory_path = home_directory / 'Downloads'

    try:
        create_folders(directories, directory_path)
        remove_empty_folders(directories, directory_path)  # Remove empty folders after organization
        organize_folders(directories, directory_path)
        organize_remaining_files(directory_path)
        organize_remaining_folders(directories, directory_path)
    except Exception as e:
        print(f"An error occurred: {e}")


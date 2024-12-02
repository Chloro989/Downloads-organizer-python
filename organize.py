import os
import shutil
from pathlib import Path
from filtering_list import (
    directories,
)  # import filtering_list.py


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
    # Problem: Modifying the directory contents while iterating over it can cause issues.
    # Solution: Create a list of files before moving them.
    files = list(os.listdir(directory_path))
    for file in files:
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
    # Problem: Same as above, need to list files before moving
    files = list(os.listdir(directory_path))
    for file in files:
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)


def organize_remaining_folders(directories, directory_path):
    """
    Move unclassified folders into the "FOLDERS" directory.
    """
    create_folders({"FOLDERS": ""}, directory_path)  # Ensure FOLDERS folder exists
    # Problem: Need to list folders before moving them
    folders = list(os.listdir(directory_path))
    for folder in folders:
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
    # Problem: The try-except block here doesn't make sense because string concatenation won't raise an exception.
    # Solution: Check if the 'Downloads' directory exists, else use 'ダウンロード'.
    if (home_directory / "Downloads").exists():
        directory_path = home_directory / "Downloads"
    else:
        directory_path = home_directory / "ダウンロード"

    try:
        create_folders(directories, directory_path)
        # Problem: remove_empty_folders is called before files are organized, which may delete necessary folders.
        # Solution: Call remove_empty_folders after organizing files.
        # remove_empty_folders(directories, directory_path)  # Remove empty folders after organization
        organize_folders(directories, directory_path)
        organize_remaining_files(directory_path)
        organize_remaining_folders(directories, directory_path)
        remove_empty_folders(
            directories, directory_path
        )  # Now remove empty folders after organization
    except Exception as e:
        print(f"An error occurred: {e}")

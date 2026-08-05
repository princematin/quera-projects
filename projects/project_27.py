import os


def explore(extension: str, directory_path: str) -> dict[str, int]:
    Verifyed_FilesAndRoot = dict()
    extension = extension.lower()
    for root, dirs, files in os.walk(directory_path):
        nums = 0
        for item in files:
            item_lower = item.lower()
            if item_lower.endswith('.'+ extension):
                nums += 1
        if nums > 0 :
            Verifyed_FilesAndRoot[root] = nums
    return Verifyed_FilesAndRoot
